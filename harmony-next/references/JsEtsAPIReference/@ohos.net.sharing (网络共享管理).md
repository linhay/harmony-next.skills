# @ohos.net.sharing (网络共享管理)

网络共享管理模块用于将设备网络连接共享给其他连接设备。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { sharing } from '@kit.NetworkKit';
```

#### NetHandle

type NetHandle = connection.NetHandle

数据网络的句柄。在调用NetHandle的方法之前，需要先获取NetHandle对象。

**系统能力**：SystemCapability.Communication.NetManager.Core

类型说明[connection.NetHandle](@ohos.net.connection (网络连接管理).md#ZH-CN_TOPIC_0000002497605446__nethandle)网络链路信息。