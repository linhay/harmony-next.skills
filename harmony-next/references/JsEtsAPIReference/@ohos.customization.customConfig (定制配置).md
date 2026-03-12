# @ohos.customization.customConfig (定制配置)

本模块接口为应用提供定制配置的获取能力，如渠道号等。

 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { customConfig } from '@kit.BasicServicesKit';
```

#### customConfig.getChannelId

getChannelId(): string

获取应用的预装渠道号。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Customization.CustomConfig

**返回值：**

类型说明string渠道号

**示例：**

```ets
import { customConfig } from '@kit.BasicServicesKit';

let channelId: string = customConfig.getChannelId();
console.info('app channelId is ' + channelId);
```