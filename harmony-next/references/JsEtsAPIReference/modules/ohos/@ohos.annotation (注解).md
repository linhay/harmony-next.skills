# @ohos.annotation (注解)

本模块定义了HarmonyOS ArkTS API的注解类型，如生命周期最小可用版本等。

- 本模块首批接口从 API version 22 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { Available, SuppressWarnings, SuppressWarningsType } from '@kit.BasicServicesKit';
```

#### Available

@interface Available { minApiVersion: string = '' }

系统提供的API注解能力，可用于标记API支持的最低可用版本。此注解可以标注在类、接口、变量、类型、模块、枚举上。在源码定义处添加注解后，编译工具会在使用处检查潜在的兼容性问题。当minApiVersion大于build-profile.json5中指定的compatibleSDKVersion字段，会生成兼容性警告。

**卡片能力：** 从API version 22开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Base

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| minApiVersion | string | 否 | 否 | minApiVersion用于标识最低可用版本，由两部分组成：系统类型+版本号。例如：'HarmonyOS 6.0.2'。 |

**示例：**

```ets
import { Available, deviceInfo } from '@kit.BasicServicesKit';

@Available({minApiVersion: 'HarmonyOS 6.0.2'}) // 标记函数最低可用版本
function myFunc() {}

@Available({minApiVersion: 'HarmonyOS 6.0.2'}) // 标记类最低可用版本
class MyClass {}

// 不建议写法：如果工程根目录下build-profile.json5文件设置的compatibleSdkVersion值小于 6.0.2，直接调用myFunc方法且没有做版本判断处理，编译器会在myFunc方法调用处抛出告警，提示该方法可能在低版本设备上运行失败
myFunc();

// 建议写法1：使用deviceInfo.distributionOSApiVersion获取发行版系统API版本进行判断，可以避免低版本设备运行异常，消除编译告警
if (deviceInfo.distributionOSApiVersion >= 60002) {
  myFunc();
} else {
  // 根据业务逻辑选择低版本可用方法
}

// 建议写法2：在myFunc调用处的父级函数（或类）上，标记@Available起始版本信息，当新标记的版本号不低于 myFunc的最低可用版本, 消除编译告警
@Available({minApiVersion: 'HarmonyOS 6.0.2'})
function myNewFunc() {
  myFunc();
}
```

**SuppressWarnings23+**

@interface SuppressWarnings {

 rules: Array<SuppressWarningsType>;

}

系统提供的API告警屏蔽功能，允许开发者通过注解的方式来抑制API调用时产生的告警。该功能可应用于类、函数、变量、类型、接口等API元素上。在源码中添加相应标注后，编译器会根据预设规则自动屏蔽对应的告警信息。

卡片能力： 从API version 23开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Base

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rules | Array<SuppressWarningsType> | 否 | 否 | 支持告警消除的规则集合 |

注解使用示例：

预置条件：工程根目录下build-profile.json5文件设置的compatibleSdkVersion值为20。

```ets
import { Available, SuppressWarnings, SuppressWarningsType } from '@kit.BasicServicesKit';
import wifiManager from '@ohos.wifiManager';
wifiManager.startScan();  // 该接口起始版本为21，直接调用会生成兼容性告警。
// The 'startScan' API is supported since SDK version 21. However, the current compatible SDK version is 20.

@SuppressWarnings({rules: [SuppressWarningsType.COMPATIBILITY]})
function myFunc() {
  wifiManager.startScan(); // 使用@SuppressWarnings注解后，告警被抑制。
}

@SuppressWarnings({rules: [SuppressWarningsType.COMPATIBILITY]})
class MyClass {
  wifiScanResult = wifiManager.startScan(); // 使用@SuppressWarnings注解后，告警被抑制。
}
```

// @SuppressWarnings <SuppressWarningsType>

本功能支持以单行注释形式快速抑制告警。添加注释后，编译器将根据规则自动屏蔽对应的告警信息。


仅支持单行注释(//)格式，示例：// @SuppressWarnings compatibility

不支持多行注释(/**/)格式，示例：/* @SuppressWarnings compatibility */

注释使用示例：

预置条件：工程根目录下build-profile.json5文件设置的compatibleSdkVersion值为20。

```ets
import { Available } from '@kit.BasicServicesKit';
import wifiManager from '@ohos.wifiManager';
wifiManager.startScan();  // 该接口起始版本为21，直接调用会生成兼容性告警。
// The 'startScan' API is supported since SDK version 21. However, the current compatible SDK version is 20.

// @SuppressWarnings compatibility
wifiManager.startScan(); // 使用@SuppressWarnings注释后，告警被抑制。
```

**SuppressWarningsType23+**

支持消除告警的规则。

卡片能力： 从API version 23开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Base

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COMPATIBILITY | compatibility | 支持消除兼容性告警。 |
| SYSCAP | syscap | 支持消除多设备告警。 |