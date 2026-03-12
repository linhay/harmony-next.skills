# @ohos.screenLock (锁屏管理)

锁屏管理服务是HarmonyOS中的系统服务，为锁屏应用提供注册亮屏、灭屏、开启屏幕、结束休眠、退出动画、请求解锁结果监听，并提供回调结果给锁屏应用。锁屏管理服务向三方应用提供请求解锁、查询锁屏状态、查询是否设置锁屏密码的能力。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import screenLock from '@ohos.screenLock';
```

#### screenLock.isScreenLocked(deprecated)

isScreenLocked(callback: AsyncCallback<boolean>): void

判断屏幕是否锁屏。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。替代接口仅面向系统应用开放。

**系统能力：** SystemCapability.MiscServices.ScreenLock

**参数：**

参数名类型必填说明callbackAsyncCallback<boolean>是回调函数。返回true表示屏幕已锁屏；返回false表示屏幕未锁屏。

**示例：**

```ets
import { BusinessError } from '@ohos.base';

screenLock.isScreenLocked((err: BusinessError, data: Boolean)=>{
  if (err) {
    console.error(`Failed to obtain whether the screen is locked, Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in Obtaining whether the screen is locked. result: ${data}`);
});
```

#### screenLock.isScreenLocked(deprecated)

isScreenLocked(): Promise<boolean>

判断屏幕是否锁屏。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.MiscServices.ScreenLock

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示屏幕已锁屏；返回false表示屏幕未锁屏。

**示例：**

```ets
import { BusinessError } from '@ohos.base';

screenLock.isScreenLocked().then((data: Boolean) => {
  console.info(`Succeeded in Obtaining whether the screen is locked. result: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain whether the screen is locked, Code: ${err.code}, message: ${err.message}`);
});
```

#### screenLock.isSecureMode(deprecated)

isSecureMode(callback: AsyncCallback<boolean>): void

判断当前设备的屏幕锁定是否安全（安全屏幕锁定意味着解锁屏幕需要密码、图案或其他用户身份识别）。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.MiscServices.ScreenLock

**参数：**

参数名类型必填说明callbackAsyncCallback<boolean>是回调函数。返回true表示当前设备的屏幕锁定安全；返回false表示当前设备的屏幕锁定不安全。

**示例：**

```ets
import { BusinessError } from '@ohos.base';

screenLock.isSecureMode((err: BusinessError, data: Boolean)=>{
  if (err) {
    console.error(`Failed to obtain whether the device is in secure mode, Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in Obtaining whether the device is in secure mode. result: ${data}`);
});
```

#### screenLock.isSecureMode(deprecated)

isSecureMode(): Promise<boolean>

判断当前设备的屏幕锁定是否安全（安全屏幕锁定意味着解锁屏幕需要密码、图案或其他用户身份识别）。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.MiscServices.ScreenLock

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示当前设备的屏幕锁定安全；返回false表示当前设备的屏幕锁定不安全。

**示例：**

```ets
import { BusinessError } from '@ohos.base';

screenLock.isSecureMode().then((data: Boolean) => {
  console.info(`Succeeded in Obtaining whether the device is in secure mode. result: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain whether the device is in secure mode, Code: ${err.code}, message: ${err.message}`);
});
```

#### screenLock.unlockScreen(deprecated)

unlockScreen(callback: AsyncCallback<void>): void

解锁屏幕。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.MiscServices.ScreenLock

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。解锁屏幕成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@ohos.base';

screenLock.unlockScreen((err: BusinessError) => {
  if (err) {
    console.error(`Failed to unlock the screen, Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded unlocking the screen.`);
});
```

#### screenLock.unlockScreen(deprecated)

unlockScreen(): Promise<void>

解锁屏幕。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.MiscServices.ScreenLock

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@ohos.base';

screenLock.unlockScreen().then(() => {
  console.info('Succeeded unlocking the screen.');
}).catch((err: BusinessError) => {
  console.error(`Failed to unlock the screen, Code: ${err.code}, message: ${err.message}`);
});
```