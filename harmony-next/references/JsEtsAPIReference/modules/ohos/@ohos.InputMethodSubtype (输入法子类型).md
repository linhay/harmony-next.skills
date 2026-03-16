# @ohos.InputMethodSubtype (输入法子类型)

本模块提供对输入法子类型的属性管理。输入法子类型允许输入法根据需要显示不同的输入模式或语言，完成模式或语言切换，如：输入法的中文/英文键盘等均属于输入法的子类型。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { InputMethodSubtype } from '@kit.IMEKit';
```

#### InputMethodSubtype

输入法子类型属性。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

名称类型只读可选说明labelstring是是非必填。输入法子类型的标签。labelId10+number是是非必填。输入法子类型的标签资源号。namestring是否必填。输入法子类型所属应用的包名。idstring是否必填。输入法子类型的id。mode'upper' | 'lower'是是非必填。输入法子类型的模式，包括upper（大写）和lower（小写）。localestring是否必填。输入法子类型的方言版本。languagestring是否必填。 输入法子类型的语言。iconstring是是非必填。输入法子类型的图标，可以通过iconId查询获取。预留字段，暂不支持使用。iconIdnumber是是非必填。输入法子类型的图标id。extraobject否是

必填。输入法子类型的其他信息。

说明：

- 从API version 10开始为非必填参数。

- 预留字段，当前无具体含义，暂不支持使用。