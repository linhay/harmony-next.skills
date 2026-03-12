# RawFileDescriptor

本模块提供rawfile文件所在hap的descriptor信息。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { resourceManager } from '@kit.LocalizationKit'
```

#### RawFileDescriptor

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

名称类型只读可选说明fdnumber否否文件描述符。offsetnumber否否起始偏移量。lengthnumber否否文件长度。