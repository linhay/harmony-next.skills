# @ohos.multimodalInput.inputDevice (输入设备)

本模块提供输入设备管理能力，包括监听输入设备的连接和断开状态，查询设备名称等输入设备信息。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { inputDevice } from '@kit.InputKit';
```

#### inputDevice.getDeviceList9+

getDeviceList(callback: AsyncCallback<Array<number>>): void

获取所有输入设备的ID列表，使用Callback回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

参数名类型必填说明callbackAsyncCallback<Array<number>>是回调函数，返回所有输入设备的ID列表。ID是输入设备的唯一标识。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            inputDevice.getDeviceList((error: BusinessError, ids: Array<Number>) => {
              if (error) {
                console.error(`Failed to get device id list, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`Device id list: ${JSON.stringify(ids)}`);
            });
          } catch (error) {
            console.error(`Failed to get device id list, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### inputDevice.getDeviceList9+

getDeviceList(): Promise<Array<number>>

获取所有输入设备的ID列表，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**返回值**：

类型说明Promise<Array<number>>Promise对象，返回所有输入设备的ID列表。ID是输入设备的唯一标识。

**示例**：

```ets
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            inputDevice.getDeviceList().then((ids: Array<Number>) => {
              console.info(`Device id list: ${JSON.stringify(ids)}`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to get device id list, error: ${JSON.stringify(error, [`code`, `message`])}`);
            });
          } catch (error) {
            console.error(`Failed to get device id list, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### inputDevice.getDeviceInfo9+

getDeviceInfo(deviceId: number, callback: AsyncCallback<InputDeviceData>): void

获取指定输入设备的信息，使用Callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

参数名类型必填说明deviceIdnumber是输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。callbackAsyncCallback<[InputDeviceData](#ZH-CN_TOPIC_0000002529445531__inputdevicedata)>是回调函数。返回输入设备信息，包括输入设备ID、名称、支持的输入能力、物理地址、版本信息及产品信息。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 获取输入设备ID为1的设备信息。
          try {
            inputDevice.getDeviceInfo(1, (error: BusinessError, deviceData: inputDevice.InputDeviceData) => {
              if (error) {
                console.error(`Failed to get device info, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`Device info: ${JSON.stringify(deviceData)}`);
            });
          } catch (error) {
            console.error(`Failed to get device info, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### inputDevice.getDeviceInfo9+

getDeviceInfo(deviceId: number): Promise<InputDeviceData>

获取指定id的输入设备信息，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

参数名类型必填说明deviceIdnumber是输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。

**返回值**：

类型说明Promise<[InputDeviceData](#ZH-CN_TOPIC_0000002529445531__inputdevicedata)>Promise对象，返回输入设备信息，包括输入设备ID、名称、支持的输入能力、物理地址、版本信息及产品信息。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 获取输入设备ID为1的设备信息。
          try {
            inputDevice.getDeviceInfo(1).then((deviceData: inputDevice.InputDeviceData) => {
              console.info(`Device info: ${JSON.stringify(deviceData)}`);
            }).catch((error: BusinessError) => {
              console.error(`Get device info failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            });
          } catch (error) {
            console.error(`Failed to get device info, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### inputDevice.getDeviceInfoSync10+

getDeviceInfoSync(deviceId: number): InputDeviceData

获取指定输入设备的信息。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

参数名类型必填说明deviceIdnumber是输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。

**返回值**：

类型说明[InputDeviceData](#ZH-CN_TOPIC_0000002529445531__inputdevicedata)返回输入设备信息，包括输入设备ID、名称、支持的输入能力、物理地址、版本信息及产品信息。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { inputDevice } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 获取输入设备ID为1的设备信息。
          try {
            let deviceData: inputDevice.InputDeviceData = inputDevice.getDeviceInfoSync(1);
            console.info(`Device info: ${JSON.stringify(deviceData)}`);
          } catch (error) {
            console.error(`Failed to get device info, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### inputDevice.on9+

on(type: "change", listener: Callback<DeviceListener>): void

注册监听输入设备的热插拔事件，使用时需连接鼠标、键盘、触摸屏等外部设备。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

参数名类型必填说明typestring是输入设备的事件类型，固定值为'change'。listenerCallback<[DeviceListener](#ZH-CN_TOPIC_0000002529445531__devicelistener9)>是回调函数，异步上报输入设备热插拔事件。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { inputDevice } from '@kit.InputKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;

@Entry
@Component
struct Index {
  @State isPhysicalKeyboardExist: boolean = false;
  @State message: string = "Click to obtain the device list and monitor device hot-plug events";
  keyBoards: Map<number, inputDevice.KeyboardType> = new Map();

  build() {
    RelativeContainer() {
      Column() {
        Text(this.message)
          .onClick(() => {
            try {
              // 1.获取设备列表，判断是否有物理键盘连接
              inputDevice.getDeviceList().then(data => {
                for (let i = 0; i < data.length; ++i) {
                  inputDevice.getKeyboardType(data[i]).then(type => {
                    if (type === inputDevice.KeyboardType.ALPHABETIC_KEYBOARD) {
                      // 物理键盘已连接
                      this.isPhysicalKeyboardExist = true;
                      this.keyBoards.set(data[i], type);
                    }
                  });
                }
              });
              // 2.监听设备热插拔
              inputDevice.on("change", (data) => {
                hilog.info(DOMAIN, 'InputDevice', `Device event info: %{public}s`, JSON.stringify(data));
                inputDevice.getKeyboardType(data.deviceId).then((type) => {
                  hilog.info(DOMAIN, 'InputDevice', 'The keyboard type is: %{public}d', type);
                  if (type === inputDevice.KeyboardType.ALPHABETIC_KEYBOARD && data.type === 'add') {
                    // 物理键盘已插入
                    this.isPhysicalKeyboardExist = true;
                    this.keyBoards.set(data.deviceId, type);
                  }
                });
                if (this.keyBoards.get(data.deviceId) === inputDevice.KeyboardType.ALPHABETIC_KEYBOARD &&
                  data.type === 'remove') {
                  // 物理键盘已拔掉
                  this.isPhysicalKeyboardExist = false;
                  this.keyBoards.delete(data.deviceId);
                }
              });
              this.message = "Device monitoring enabled successfully"
            } catch (error) {
              hilog.error(DOMAIN, 'InputDevice', `Execute failed, error: %{public}s`,
                JSON.stringify(error, ["code", "message"]));
              this.message = `Failed to enable device monitoring. Click to retry. Error message:${JSON.stringify(error,
                ["code", "message"])}`
            }
          })
      }
    }
  }
}
```

#### inputDevice.off9+

off(type: "change", listener?: Callback<DeviceListener>): void

取消监听输入设备的热插拔事件。在应用退出前调用，取消监听。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

参数名类型必填说明typestring是输入设备的事件类型，固定值为'change'。listenerCallback<[DeviceListener](#ZH-CN_TOPIC_0000002529445531__devicelistener9)>否取消监听的回调函数，缺省时取消所有输入设备热插拔事件的监听。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { inputDevice } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          let callback = (data: inputDevice.DeviceListener) => {
            console.info(`Report device event info: ${JSON.stringify(data, [`type`, `deviceId`])}`);
          };

          try {
            inputDevice.on("change", callback);
          } catch (error) {
            console.error(`Listen device event failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }

          // 取消指定的监听。
          try {
            inputDevice.off("change", callback);
          } catch (error) {
            console.error(`Cancel listening device event failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }

          // 取消所有监听。
          try {
            inputDevice.off("change");
          } catch (error) {
            console.error(`Cancel all listening device event failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### inputDevice.getDeviceIds(deprecated)

getDeviceIds(callback: AsyncCallback<Array<number>>): void

获取所有输入设备的ID列表，使用Callback异步回调。

从API version 8 开始支持，从API version 9 开始废弃，建议使用[inputDevice.getDeviceList](#ZH-CN_TOPIC_0000002529445531__inputdevicegetdevicelist9)替代。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

参数名类型必填说明callbackAsyncCallback<Array<number>>是回调函数，返回所有输入设备的ID列表。ID是输入设备的唯一标识。

**示例**：

```ets
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          inputDevice.getDeviceIds((error: BusinessError, ids: Array<Number>) => {
            if (error) {
              console.error(`Failed to get device id list, error: ${JSON.stringify(error, [`code`, `message`])}`);
              return;
            }
            console.info(`Device id list: ${JSON.stringify(ids)}`);
          });
        })
    }
  }
}
```

#### inputDevice.getDeviceIds(deprecated)

getDeviceIds(): Promise<Array<number>>

获取所有输入设备的ID列表，使用Promise异步回调。

从API version 8 开始支持，从API version 9 开始废弃，建议使用[inputDevice.getDeviceList](#ZH-CN_TOPIC_0000002529445531__inputdevicegetdevicelist9)替代。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**返回值**：

类型说明Promise<Array<number>>Promise对象，返回所有输入设备的ID列表。ID是输入设备的唯一标识。

**示例**：

```ets
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          inputDevice.getDeviceIds().then((ids: Array<Number>) => {
            console.info(`Device id list: ${JSON.stringify(ids)}`);
          }).catch((error: BusinessError) => {
            console.error(`Failed to get device id list, error: ${JSON.stringify(error, [`code`, `message`])}`);
          })
        })
    }
  }
}
```

#### inputDevice.getDevice(deprecated)

getDevice(deviceId: number, callback: AsyncCallback<InputDeviceData>): void

获取指定id的输入设备信息，使用Callback异步回调。

从API version 8 开始支持，从API version 9 开始废弃，建议使用[inputDevice.getDeviceInfo](#ZH-CN_TOPIC_0000002529445531__inputdevicegetdeviceinfo9)替代。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

参数名类型必填说明deviceIdnumber是输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。callbackAsyncCallback<[InputDeviceData](#ZH-CN_TOPIC_0000002529445531__inputdevicedata)>是回调函数，返回输入设备信息，包括输入设备ID、名称、支持的输入能力、物理地址、版本信息及产品信息。

**示例**：

```ets
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 获取输入设备ID为1的设备信息。
          inputDevice.getDevice(1, (error: BusinessError, deviceData: inputDevice.InputDeviceData) => {
            if (error) {
              console.error(`Failed to get device info, error: ${JSON.stringify(error, [`code`, `message`])}`);
              return;
            }
            console.info(`Device info: ${JSON.stringify(deviceData)}`);
          });
        })
    }
  }
}
```

#### inputDevice.getDevice(deprecated)

getDevice(deviceId: number): Promise<InputDeviceData>

获取指定id的输入设备信息，使用Promise异步回调。

从API version 8 开始支持，从API version 9 开始废弃，建议使用[inputDevice.getDeviceInfo](#ZH-CN_TOPIC_0000002529445531__inputdevicegetdeviceinfo9)替代。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

参数名类型必填说明deviceIdnumber是输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。

**返回值**：

类型说明Promise<[InputDeviceData](#ZH-CN_TOPIC_0000002529445531__inputdevicedata)>Promise对象，返回输入设备信息，包括输入设备ID、名称、支持的输入能力、物理地址、版本信息及产品信息。

**示例**：

```ets
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 获取输入设备ID为1的设备信息。
          inputDevice.getDevice(1).then((deviceData: inputDevice.InputDeviceData) => {
            console.info(`Device info: ${JSON.stringify(deviceData)}`);
          }).catch((error: BusinessError) => {
            console.error(`Failed to get device info, error: ${JSON.stringify(error, [`code`, `message`])}`);
          })
        })
    }
  }
}
```

#### inputDevice.supportKeys9+

supportKeys(deviceId: number, keys: Array<KeyCode>, callback: AsyncCallback <Array<boolean>>): void

查询指定输入设备是否支持指定按键，使用Callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

参数名类型必填说明deviceIdnumber是输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。keysArray[<KeyCode>](@ohos.multimodalInput.keyCode (键值).md#ZH-CN_TOPIC_0000002529285559__keycode)是需要查询的键值，最多支持5个按键查询。callbackAsyncCallback<Array<boolean>>是回调函数，返回查询结果。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 查询ID为1的输入设备对于17、22和2055按键的支持情况。
          try {
            inputDevice.supportKeys(1, [17, 22, 2055], (error: BusinessError, supportResult: Array<Boolean>) => {
              console.info(`Query result: ${JSON.stringify(supportResult)}`);
            });
          } catch (error) {
            console.error(`Query failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### inputDevice.supportKeys9+

supportKeys(deviceId: number, keys: Array<KeyCode>): Promise<Array<boolean>>

查询指定输入设备是否支持指定按键，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

参数名类型必填说明deviceIdnumber是输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。keysArray[<KeyCode>](@ohos.multimodalInput.keyCode (键值).md#ZH-CN_TOPIC_0000002529285559__keycode)是需要查询的键值，最多支持查询5个按键。

**返回值**：

类型说明Promise<Array<boolean>>Promise对象，返回查询结果。true 表示支持，false表示不支持。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 查询ID为1的输入设备对于17、22和2055按键的支持情况。
          try {
            inputDevice.supportKeys(1, [17, 22, 2055]).then((supportResult: Array<Boolean>) => {
              console.info(`Query result: ${JSON.stringify(supportResult)}`);
            }).catch((error: BusinessError) => {
              console.error(`Query support Keys failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            });
          } catch (error) {
            console.error(`Query failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### inputDevice.supportKeysSync10+

supportKeysSync(deviceId: number, keys: Array<KeyCode>): Array<boolean>

查询指定id的输入设备对指定键值的支持情况。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

参数名类型必填说明deviceIdnumber是输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。keysArray[<KeyCode>](@ohos.multimodalInput.keyCode (键值).md#ZH-CN_TOPIC_0000002529285559__keycode)是需要查询的键值，最多支持查询5个按键。

**返回值**：

类型说明Array<boolean>返回查询结果。true表示支持，false表示不支持。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { inputDevice } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 查询ID为1的输入设备对于17、22和2055按键的支持情况。
          try {
            let supportResult: Array<Boolean> = inputDevice.supportKeysSync(1, [17, 22, 2055])
            console.info(`Query result: ${JSON.stringify(supportResult)}`)
          } catch (error) {
            console.error(`Query failed, error: ${JSON.stringify(error, [`code`, `message`])}`)
          }
        })
    }
  }
}
```

#### inputDevice.getKeyboardType9+

getKeyboardType(deviceId: number, callback: AsyncCallback<KeyboardType>): void

获取输入设备的键盘类型，如全键盘、小键盘等，使用callback异步回调。输入设备的键盘类型以接口返回结果为准。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

参数名类型必填说明deviceIdnumber是输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。callbackAsyncCallback<[KeyboardType](#ZH-CN_TOPIC_0000002529445531__keyboardtype9)>是回调函数，返回查询结果。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 查询ID为1的输入设备的键盘类型。
          try {
            inputDevice.getKeyboardType(1, (error: BusinessError, type: Number) => {
              if (error) {
                console.error(`Failed to get keyboard type, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`Keyboard type: ${JSON.stringify(type)}`);
            });
          } catch (error) {
            console.error(`Failed to get keyboard type, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### inputDevice.getKeyboardType9+

getKeyboardType(deviceId: number): Promise<KeyboardType>

获取输入设备的键盘类型，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

参数名类型必填说明deviceIdnumber是输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。

**返回值**：

类型说明Promise<[KeyboardType](#ZH-CN_TOPIC_0000002529445531__keyboardtype9)>Promise对象，返回查询结果。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 示例查询设备ID为1的设备键盘类型。
          try {
            inputDevice.getKeyboardType(1).then((type: number) => {
              console.info(`Keyboard type: ${JSON.stringify(type)}`);
            }).catch((error: BusinessError) => {
              console.error(`Get keyboard type failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`Failed to get keyboard type, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### inputDevice.getKeyboardTypeSync10+

getKeyboardTypeSync(deviceId: number): KeyboardType

获取输入设备的键盘类型。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

参数名类型必填说明deviceIdnumber是输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。

**返回值**：

类型说明[KeyboardType](#ZH-CN_TOPIC_0000002529445531__keyboardtype9)返回查询结果。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例**：

```ets
import { inputDevice } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 示例查询设备ID为1的设备键盘类型。
          try {
            let type: number = inputDevice.getKeyboardTypeSync(1)
            console.info(`Keyboard type: ${JSON.stringify(type)}`)
          } catch (error) {
            console.error(`Failed to get keyboard type, error: ${JSON.stringify(error, [`code`, `message`])}`)
          }
        })
    }
  }
}
```

#### inputDevice.isFunctionKeyEnabled15+

isFunctionKeyEnabled(functionKey: FunctionKey): Promise<boolean>

检查功能键（如：CapsLock键）是否使能。使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

参数名类型必填说明functionKey[FunctionKey](#ZH-CN_TOPIC_0000002529445531__functionkey15)是需要设置的功能键类型。

**返回值**：

类型说明Promise<boolean>Promise对象。返回查询结果，true表示功能键使能，false表示功能键未使能。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[输入设备错误码](输入设备错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.3900002There is currently no keyboard device connected.

**示例**：

```ets
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            inputDevice.isFunctionKeyEnabled(inputDevice.FunctionKey.CAPS_LOCK).then((state: boolean) => {
              console.info(`capslock state: ${JSON.stringify(state)}`);
            }).catch((error: BusinessError) => {
              console.error(`Get capslock state failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`Failed to get capslock state, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

#### inputDevice.setFunctionKeyEnabled15+

setFunctionKeyEnabled(functionKey: FunctionKey, enabled: boolean): Promise<void>

设置功能键（如：CapsLock键）使能状态。使用Promise异步回调。

**需要权限**：ohos.permission.INPUT_KEYBOARD_CONTROLLER

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

参数名类型必填说明functionKey[FunctionKey](#ZH-CN_TOPIC_0000002529445531__functionkey15)是需要设置的功能键类型。enabledboolean是功能键使能状态。取值为true表示使能功能键，取值为false表示不使能功能键。

**返回值**：

类型说明Promise<void>Promise对象，无返回结果的Promise对象。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[输入设备错误码](输入设备错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.3900002There is currently no keyboard device connected.3900003It is prohibited for non-input applications.

**示例**：

```ets
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            inputDevice.setFunctionKeyEnabled(inputDevice.FunctionKey.CAPS_LOCK, true).then(() => {
              console.info(`Set capslock state success`);
            }).catch((error: BusinessError) => {
              console.error(`Set capslock state failed, error=${JSON.stringify(error)}`);
            });
          } catch (error) {
            console.error(`Set capslock enable error`);
          }
        })
    }
  }
}
```

#### inputDevice.getIntervalSinceLastInput14+

getIntervalSinceLastInput(): Promise<number>

获取距离上次系统输入事件的时间间隔（包含设备休眠时间），使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**返回值**：

类型说明Promise<number>Promise对象，返回距离上次系统输入事件的时间间隔，单位：μs。

**示例**：

```ets
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          inputDevice.getIntervalSinceLastInput().then((timeInterval: number) => {
            console.info(`Interval since last input: ${JSON.stringify(timeInterval)}`);
          }).catch((error: BusinessError) => {
            console.error(`Get interval since last input failed, error: ${JSON.stringify(error)}`);
          })
        })
    }
  }
}
```

#### DeviceListener9+

描述输入设备热插拔的信息。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

名称类型只读可选说明type[ChangedType](#ZH-CN_TOPIC_0000002529445531__changedtype9)否否输入设备插入或者移除。deviceIdnumber否否输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。

#### InputDeviceData

描述输入设备的信息。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

名称类型只读可选说明idnumber否否输入设备的唯一标识，同一个物理设备反复插拔，设备ID可能会发生变化。namestring否否输入设备的名称。sourcesArray<[SourceType](#ZH-CN_TOPIC_0000002529445531__sourcetype9)>否否输入设备的输入能力。包括键盘、鼠标、触摸屏、轨迹球、触控板、操纵杆等。axisRangesArray<[AxisRange](#ZH-CN_TOPIC_0000002529445531__axisrange)>否否输入设备的轴信息。bus9+number否否输入设备的总线类型，该值以输入设备上报为准。product9+number否否输入设备的产品信息。vendor9+number否否输入设备的厂商信息。version9+number否否输入设备的版本信息。phys9+string否否输入设备的物理地址。uniq9+string否否输入设备的唯一标识。

#### AxisType9+

type AxisType = 'touchmajor' | 'touchminor' | 'orientation' | 'x' | 'y' | 'pressure' | 'toolminor' | 'toolmajor' | 'null'

输入设备的轴类型。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

类型说明'touchmajor'椭圆触摸区域长轴。'touchminor'椭圆触摸区域短轴。'toolminor'工具区域短轴。'toolmajor'工具区域长轴。'orientation'方向轴。'pressure'压力轴。'x'横坐标轴。'y'纵坐标轴。'null'无。

#### AxisRange

输入设备的轴信息。

**系统能力**： SystemCapability.MultimodalInput.Input.InputDevice

名称类型只读可选说明source[SourceType](#ZH-CN_TOPIC_0000002529445531__sourcetype9)否否输入设备的输入能力。包括键盘、鼠标、触摸屏、轨迹球、触控板、操纵杆等。axis[AxisType](#ZH-CN_TOPIC_0000002529445531__axistype9)否否输入设备的轴类型。maxnumber否否轴的最大值。minnumber否否轴的最小值。fuzz9+number否否轴的模糊值。flat9+number否否轴的基准值。resolution9+number否否轴的分辨率。

#### SourceType9+

type SourceType = 'keyboard' | 'mouse' | 'touchpad' | 'touchscreen' | 'joystick' | 'trackball'

输入设备的输入能力。包括键盘、鼠标、触摸屏、轨迹球、触控板、操纵杆等。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

类型说明'keyboard'表示输入设备是键盘。'touchscreen'表示输入设备是触摸屏。'mouse'表示输入设备是鼠标。'trackball'表示输入设备是轨迹球。'touchpad'表示输入设备是触控板。'joystick'表示输入设备是操纵杆。

#### ChangedType9+

type ChangedType = 'add' | 'remove'

监听设备热插拔事件类型。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

类型说明'add'插入输入设备。'remove'移除输入设备。

#### KeyboardType9+

键盘输入设备的类型。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

名称值说明NONE0表示无按键设备。UNKNOWN1表示未知按键设备。ALPHABETIC_KEYBOARD2表示全键盘设备。DIGITAL_KEYBOARD3表示小键盘设备。HANDWRITING_PEN4表示手写笔设备。REMOTE_CONTROL5表示遥控器设备。

#### FunctionKey15+

功能键的类型。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

名称值说明CAPS_LOCK1CapsLock键，仅支持对输入键盘扩展的CapsLock键设置使能。