# @ohos.ability.screenLockFileManager (锁屏敏感数据管理)

敏感数据密钥在锁屏后会触发销毁，销毁后敏感数据无法读写，需解锁屏幕触发恢复敏感数据密钥后方可访问。本模块提供应用锁屏下敏感数据保护的能力，支持申请和释放锁屏下敏感数据访问权限等。

本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { screenLockFileManager } from '@kit.AbilityKit';
```

#### DataType

枚举，指定锁屏下访问的敏感数据类型。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

名称值说明MEDIA_DATA0x00000001媒体类型数据。ALL_DATA0xffffffff所有敏感加密数据。

#### AccessStatus

表示锁屏下敏感数据访问权限申请的状态枚举。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

名称值说明ACCESS_DENIED-1拒绝授予锁屏下敏感数据访问。ACCESS_GRANTED0授予锁屏下敏感数据访问。

#### ReleaseStatus

表示锁屏下敏感数据访问权限释放的状态枚举。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

名称值说明RELEASE_DENIED-1拒绝锁屏下敏感数据访问释放。RELEASE_GRANTED0释放锁屏下敏感数据访问。

#### KeyStatus18+

表示锁屏下敏感数据访问权限的状态枚举。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

名称值说明KEY_NOT_EXIST-2应用未开启锁屏敏感数据保护功能。KEY_RELEASED-1锁屏敏感数据访问权限已释放。KEY_EXIST0应用可以访问锁屏敏感数据。

#### screenLockFileManager.acquireAccess

acquireAccess(): AccessStatus

以同步方法申请锁屏下应用敏感数据访问权限。锁屏后，敏感数据无法被访问，但可通过调用该方法，访问本应用的敏感数据。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**返回值：**

类型说明[AccessStatus](#ZH-CN_TOPIC_0000002529444571__accessstatus)锁屏下敏感数据访问权限申请的状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.screenLockFileManager错误码](锁屏敏感数据管理错误码.md)。

错误码ID错误信息801The specified SystemCapability name was not found.29300002The system ability work abnormally.29300003The application is not enabled the data protection under lock screen.29300004File access is denied.

**示例：**

```ets
// 申请锁屏下应用敏感数据访问权限
import { screenLockFileManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
    let acquireStatus = screenLockFileManager.acquireAccess();
    if (acquireStatus === screenLockFileManager.AccessStatus.ACCESS_GRANTED) {
        hilog.info(0x0000, 'testTag', 'acquireAccess successfully.');
    }
} catch (err) {
    let message = (err as BusinessError).message;
    hilog.error(0x0000, 'testTag', 'acquireAccess failed: %{public}s', message);
}
```

#### screenLockFileManager.releaseAccess

releaseAccess(): ReleaseStatus

以同步方法取消锁屏下本应用敏感数据访问权限。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**返回值：**

类型说明[ReleaseStatus](#ZH-CN_TOPIC_0000002529444571__releasestatus)锁屏下敏感数据访问权限释放的状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.screenLockFileManager错误码](锁屏敏感数据管理错误码.md)。

错误码ID错误信息801The specified SystemCapability name was not found.29300002The system ability work abnormally.29300003The application is not enabled the data protection under lock screen.29300005File access was not acquired.

**示例：**

```ets
// 释放锁屏下应用敏感数据访问权限
import { screenLockFileManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
    let releaseStatus = screenLockFileManager.releaseAccess();
    if (releaseStatus === screenLockFileManager.ReleaseStatus.RELEASE_GRANTED) {
        hilog.info(0x0000, 'testTag', 'releaseAccess successfully.');
    }
} catch (err) {
    let message = (err as BusinessError).message;
    hilog.error(0x0000, 'testTag', 'releaseAccess failed: %{public}s', message);
}
```

#### screenLockFileManager.queryAppKeyState18+

queryAppKeyState(): KeyStatus

以同步方法查询锁屏下本应用敏感数据访问权限。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**返回值：**

类型说明[KeyStatus](#ZH-CN_TOPIC_0000002529444571__keystatus18)锁屏下敏感数据访问权限的状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.screenLockFileManager错误码](锁屏敏感数据管理错误码.md)。

错误码ID错误信息801The specified SystemCapability name was not found.29300002The system ability work abnormally.

**示例：**

```ets
// 查询锁屏下应用敏感数据访问权限
import { screenLockFileManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
    let keyStatus = screenLockFileManager.queryAppKeyState();
    if (keyStatus === screenLockFileManager.KeyStatus.KEY_NOT_EXIST) {
        hilog.info(0x0000, 'testTag', 'Key does not exist.');
    } else if (keyStatus === screenLockFileManager.KeyStatus.KEY_RELEASED) {
        hilog.info(0x0000, 'testTag', 'Key has been released.');
    } else if (keyStatus === screenLockFileManager.KeyStatus.KEY_EXIST) {
        hilog.info(0x0000, 'testTag', 'Key exists.');
    }
} catch (err) {
    let message = (err as BusinessError).message;
    hilog.error(0x0000, 'testTag', 'queryAppKeyState failed: %{public}s', message);
}
```