# @ohos.inputMethod.ExtraConfig (输入法扩展信息)

本模块提供对输入法扩展信息的管理，支持ArkUI编辑框在拉起输入法时传递扩展信息给输入法应用，通过对扩展信息的处理，使输入法应用能够获取到宿主APP增加的扩展信息，信息总长度不超过32KB。

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { InputMethodExtraConfig } from '@kit.IMEKit';
```

#### CustomValueType

type CustomValueType = number | string | boolean

表示扩展信息类型，接口参数具体类型根据其功能而定。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 类型 | 说明 |
| --- | --- |
| string | 表示值类型为字符串。 |
| number | 表示值类型为数字。 |
| boolean | 表示值类型为布尔值。 |

#### InputMethodExtraConfig

输入法扩展信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| customSettings | Record<string, CustomValueType> | 否 | 否 | 输入法扩展信息，用于储存自定义的键值对，这些键值对可以是任何与输入法相关的配置信息。例如用户的输入习惯、快捷键设置、主题颜色等。这些设置信息将在输入法应用绑定时加载，以提供个性化的用户体验。信息的总长度不超过32KB。 |