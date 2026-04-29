# SendableResource

本模块提供SendableResource资源相关信息，包括应用包名、应用模块名、资源类型等。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**导入模块**

```ets
import { resourceManager } from '@kit.LocalizationKit';
```

**SendableResource**

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Global.ResourceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | 应用的bundle名称。 |
| moduleName | string | 否 | 否 | 应用的module名称。 |
| id | number | 否 | 否 | 资源的id值，取值如下： - 应用资源区间：[0x01000000, 0x06FFFFFF] 和 [0x08000000, 0xFFFFFFFF] - 系统资源区间：[0x07000000, 0x07FFFFFF] |
| params | collections.Array<string | number> | 否 | 是 | 其他资源参数，包括资源名、格式化接口的替换值、复数接口的量词。 |
| type | number | 否 | 是 | 资源的类型，取值如下： - 10001：color - 10002：float - 10003：string - 10004：plural - 10005：boolean - 10006：intarray - 10007：integer - 10008：pattern - 10009：strarray - 20000：media - 30000：rawfile - 40000：symbol |