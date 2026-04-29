# hdsMaterial

本模块提供材质效果能力，支持通过配置材质类型、等级等参数，实现多样化的材质表现。

起始版本： 6.1.0(23)

**导入模块**

```ets
import { hdsMaterial } from '@kit.UIDesignKit';
```

**getSystemMaterialTypes**

getSystemMaterialTypes(): Array<MaterialType>

获取设备支持的所有材质类型。

卡片能力： 从6.1.0(23)开始，该接口支持在ArkTS卡片中使用。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 6.1.0(23)

返回值：

| 类型 | 说明 |
| --- | --- |
| Array<MaterialType> | 设备支持的材质类型。 |

示例：

```ets
import { hdsMaterial} from '@kit.UIDesignKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let materialTypes: Array<hdsMaterial.MaterialType> = hdsMaterial.getSystemMaterialTypes();
} catch (err) {
  let message = (err as BusinessError).message;
  let code = (err as BusinessError).code;
  console.error(`getSystemMaterialTypes failed, code: ${code}, message: ${message}`);
}
```

**MaterialType**

材质类型枚举。

卡片能力： 从6.1.0(23)开始，该接口支持在ArkTS卡片中使用。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 无材质效果。 |
| ADAPTIVE | 100 | 自适应系统材质。默认为沉浸式材质。 |
| IMMERSIVE | 101 | 沉浸式材质（新材质）。 |

**MaterialLevel**

材质等级枚举。各等级效果承载在支持配置材质属性的组件上，其中精美等级材质需要耗费的性能更多，流畅等级材质需要耗费的性能较少。

卡片能力： 从6.1.0(23)开始，该接口支持在ArkTS卡片中使用。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EXQUISITE | 0 | 精美。 |
| GENTLE | 1 | 轻柔。 |
| SMOOTH | 2 | 流畅。 |
| ADAPTIVE | 10 | 材质生效策略由系统策略决定，系统根据设备性能自适应材质等级。 |