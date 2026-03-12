# ringtone（铃声服务）

ringtone提供铃声设置的功能。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { ringtone } from '@kit.RingtoneKit'
```

#### RingtoneType

描述铃声的类型枚举。

系统能力：SystemCapability.Ringtone.Core

**起始版本：**5.0.0(12)

名称

值

说明

CALL

0

来电铃声。

MESSAGE

1

信息铃声。

NOTIFICATION

2

通知铃声。

ALARM

3

闹钟铃声。

#### RingtoneErrors

该枚举为设置铃声，获取铃声支持类型和获取铃声支持文件类型等接口的错误码。

**系统能力：**SystemCapability.Ringtone.Core

**起始版本：**5.0.0(12)

名称

值

说明

ERROR_INVALID_PARAM

401

参数非法。

ERROR_USER_CANCELED

1011600001

用户取消。

ERROR_FILE_NOT_FOUND

1011600002

文件不存在。

ERROR_SHOW_FAILED

1011600003

铃声弹框失败。

ERROR_CALL_SYSTEM_API_FAILED

1011600004

调用系统接口失败。

ERROR_SYSTEM

1011699999

系统内部错误。

#### ringtone.getSupportedRingtoneTypes

getSupportedRingtoneTypes(): Array<RingtoneType>

查询当前系统支持自定义的铃声类型。

**系统能力：**SystemCapability.Ringtone.Core

**起始版本：**5.0.0(12)

**返回值：**

类型

说明

Array<[RingtoneType](#section18108304244)>

当前系统支持自定义的铃声类型。

**示例：**

```ets
import { ringtone } from '@kit.RingtoneKit'
import { JSON } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';

const APP_TAG = "Msc_Demo"
const DOMAIN = 0x0001

@Entry
@Component
struct Index {
  build() {
    Stack() {
      Column() {
        Button("查询当前系统支持自定义的铃声类型")
          .width(200)
          .height(50)
          .onClick(() => {
            let typeList: Array<ringtone.RingtoneType> = ringtone.getSupportedRingtoneTypes()
            hilog.info(DOMAIN, APP_TAG, 'getSupportedRingtoneTypes : ' + JSON.stringify(typeList));
          })
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.Pink)
    }
    .height('100%')
    .width('100%')
  }
}
```

#### ringtone.getSupportedDataTypes

getSupportedDataTypes(ringtoneType: RingtoneType): Array<uniformTypeDescriptor.UniformDataType>

查询对应铃声类型支持的文件类型。

**系统能力**：SystemCapability.Ringtone.Core

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

ringtoneType

[RingtoneType](#section18108304244)

是

待查询的铃声类型。

**返回值：**

类型

说明

Array<[uniformTypeDescriptor.UniformDataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-uniformtypedescriptor#uniformdatatype)>

返回对应铃声类型支持的文件类型。

**错误码：**

以下错误码的详细介绍请参见铃声服务[ArkTS API错误码](ArkTS API 错误码.md)。

错误码ID

错误信息

401

Parameter invalid.

**示例：**

```ets
import { ringtone } from '@kit.RingtoneKit'
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor } from '@kit.ArkData';
import { JSON } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';

const APP_TAG = "Msc_Demo"
const DOMAIN = 0x0001

@Entry
@Component
struct Index {
  build() {
    Stack() {
      Column() {
        Button("查询支持的文件类型")
          .width(200)
          .height(50)
          .onClick(() => {
            try {
              let typeList: Array<uniformTypeDescriptor.UniformDataType> =
                ringtone.getSupportedDataTypes(ringtone.RingtoneType.NOTIFICATION)
              hilog.info(DOMAIN, APP_TAG, 'getSupportedDataTypes3----- : ' + JSON.stringify(typeList));
            } catch (error) {
              let err: BusinessError = error as BusinessError;
              hilog.error(DOMAIN, APP_TAG,
                'getSupportedDataType error message: ' + err.message + ', error code: ' + err.code);
            }
          })
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.Pink)
    }
    .height('100%')
    .width('100%')
  }
}
```

#### ringtone.getSupportedMaxDuration

getSupportedMaxDuration(ringtoneType: RingtoneType, dataType: uniformTypeDescriptor.UniformDataType): number

查询对应铃声类型以及文件类型支持的时长。

**系统能力**：SystemCapability.Ringtone.Core

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

ringtoneType

[RingtoneType](#section18108304244)

是

待查询的铃声类型。

dataType

[uniformTypeDescriptor.UniformDataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-uniformtypedescriptor#uniformdatatype)

是

待查询的文件类型。

**返回值：**

类型

说明

number

返回对应类型的铃声和文件支持的最大时长（单位：秒），其中闹钟铃声时长为300s，短信铃声和通知铃声时长为7s，来电铃声时长为60s。

**错误码：**

以下错误码的详细介绍请参见铃声服务[ArkTS API错误码](ArkTS API 错误码.md)。

错误码ID

错误信息

401

Parameter invalid.

**示例：**

```ets
import { ringtone } from '@kit.RingtoneKit'
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor } from '@kit.ArkData';
import { hilog } from '@kit.PerformanceAnalysisKit';

const APP_TAG = "Msc_Demo"
const DOMAIN = 0x0001

@Entry
@Component
struct Index {
  build() {
    Stack() {
      Column() {
        Button("查询最大时长")
          .width(200)
          .height(50)
          .onClick(() => {
            try {
              let maxDuration: number =
                ringtone.getSupportedMaxDuration(ringtone.RingtoneType.MESSAGE,
                  uniformTypeDescriptor.UniformDataType.MP3)
              hilog.info(DOMAIN, APP_TAG, 'getSupportedMaxDuration: ' + maxDuration);
            } catch (error) {
              let err: BusinessError = error as BusinessError;
              hilog.error(DOMAIN, APP_TAG,
                'getSupportedMaxDuration error message: ' + err.message + ', error code: ' + err.code);
            }
          })
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.Pink)
    }
    .height('100%')
    .width('100%')
  }
}
```

#### ringtone.startRingtoneSetting

startRingtoneSetting(context: common.UIAbilityContext, path: string, name: string, callback: AsyncCallback<RingtoneType>): void

拉起设置铃声弹窗，并返回点击的铃声类型，使用Callback异步回调。

**系统能力**：SystemCapability.Ringtone.Core

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

UIAbility上下文。

path

string

是

具有访问权限的文件路径。

name

string

是

文件名，限制长度1000。

callback

AsyncCallback<[RingtoneType](#section18108304244)>

是

Callback对象。返回用户选择设置的铃声类型。

**错误码：**

以下错误码的详细介绍请参见铃声服务[ArkTS API错误码](ArkTS API 错误码.md)。

错误码ID

错误信息

401

Parameter invalid.

1011600001

User canceled.

1011600002

The media file is not found.

1011600003

Failed to show the dialog box.

1011600004

Failed to call the system API.

1011699999

System exception.

```ets
import { common } from '@kit.AbilityKit';
import { ringtone } from '@kit.RingtoneKit'
import { BusinessError } from '@kit.BasicServicesKit';
import { JSON } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';

const APP_TAG = "Msc_Demo"
const DOMAIN = 0x0001

@Entry
@Component
struct Index {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    Stack() {
      Column() {
        Button("设为铃声OGG格式")
          .width(200)
          .height(50)
          .onClick(async () => {
            let audioPath: string = this.context.filesDir + '/test.ogg'
            let splitList = audioPath.split('/')
            let fileName = splitList[splitList.length - 1]
            hilog.info(DOMAIN, APP_TAG, 'audioPath:' + audioPath)
            hilog.info(DOMAIN, APP_TAG, 'fileName:' + fileName)

            try {
              ringtone.startRingtoneSetting(this.context, audioPath, fileName, (err, res) => {
                hilog.info(DOMAIN, APP_TAG, '返回值：' + JSON.stringify(res))
              })
            } catch (error) {
              let err: BusinessError = error as BusinessError;
              hilog.error(DOMAIN, APP_TAG,
                'accessSync failed with error message: ' + err.message + ', error code: ' + err.code);
            }
          })
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.Pink)
    }
    .height('100%')
    .width('100%')
  }
}
```

#### ringtone.startRingtoneSetting

startRingtoneSetting(context: common.UIAbilityContext, path: string, name: string): Promise<RingtoneType>

拉起设置铃声弹窗，并返回点击的铃声类型，使用Promise异步回调。

**系统能力**：SystemCapability.Ringtone.Core

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

UIAbility上下文。

path

string

是

具有访问权限的文件路径。

name

string

是

文件名，限制长度1000。

**返回值：**

类型

说明

Promise<[RingtoneType](#section18108304244)>

Promise对象。返回用户选择设置的铃声类型。

**错误码：**

以下错误码的详细介绍请参见铃声服务[ArkTS API错误码](ArkTS API 错误码.md)。

错误码ID

错误信息

401

Parameter invalid.

1011600001

User canceled.

1011600002

The media file is not found.

1011600003

Failed to show the dialog box.

1011600004

Failed to call the system API.

1011699999

System exception.

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { ringtone } from '@kit.RingtoneKit'
import { BusinessError } from '@kit.BasicServicesKit';
import { JSON } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';

const APP_TAG = "Msc_Demo"
const DOMAIN = 0x0001

@Entry
@Component
struct Index {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    Stack() {
      Column() {
        Button("设为铃声OGG格式")
          .width(200)
          .height(50)
          .onClick(async () => {
            let audioPath: string = this.context.filesDir + '/test.ogg'
            let splitList = audioPath.split('/')
            let fileName = splitList[splitList.length - 1]
            hilog.info(DOMAIN, APP_TAG, 'audioPath:' + audioPath)
            hilog.info(DOMAIN, APP_TAG, 'fileName:' + fileName)
            try {
              await ringtone.startRingtoneSetting(this.context, audioPath, fileName).then(res => {
                hilog.info(DOMAIN, APP_TAG, '返回值：' + JSON.stringify(res))
              })
            } catch (error) {
              let err: BusinessError = error as BusinessError;
              hilog.error(DOMAIN, APP_TAG,
                'accessSync failed with error message: ' + err.message + ', error code: ' + err.code);
            }
          })
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.Pink)
    }
    .height('100%')
    .width('100%')
  }
}
```