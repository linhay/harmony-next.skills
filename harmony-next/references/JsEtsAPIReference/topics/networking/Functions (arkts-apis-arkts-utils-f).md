[]()[]()

# Functions

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

[]()[]()

#### 导入模块

```ets
import { ArkTSUtils } from '@kit.ArkTS'
```

[]()[]()

#### ArkTSUtils.isSendable

isSendable(value: Object | null | undefined): boolean

该方法用于判断value是否为Sendable数据类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明valueObject | null | undefined是待校验的对象。

**返回值：**

类型说明booleanvalue是否为Sendable数据类型，true表示value是Sendable数据类型，否则为false。

**示例：**

```ets
import { ArkTSUtils } from '@kit.ArkTS';

@Sendable
function sendableFunc() {
  console.info("sendableFunc");
}

if (ArkTSUtils.isSendable(sendableFunc)) {
  console.info("sendableFunc is Sendable");
} else {
  console.info("sendableFunc is not Sendable");
}
// 期望输出: 'SendableFunc is Sendable'
```