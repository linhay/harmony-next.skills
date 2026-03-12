# @system.package (应用管理)

-

从API version 9开始不再维护，推荐使用该模块[@ohos.bundle.bundleManager](@ohos.bundle.bundleManager (应用程序包管理模块).md)。

-

本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import Package from '@system.package';
```

#### package.hasInstalled(deprecated)

从API version 9开始不再维护，推荐使用该模块[@ohos.bundle.bundleManager](@ohos.bundle.bundleManager (应用程序包管理模块).md)。

hasInstalled(options: CheckPackageHasInstalledOptions): void

查询指定应用是否存在，或者原生应用是否安装。

**系统能力：** SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明options[CheckPackageHasInstalledOptions](#ZH-CN_TOPIC_0000002529444611__checkpackagehasinstalledoptions)是选项参数。

**示例：**

```ets
import Package from '@system.package';

@Entry
@Component
struct MainPage {
  hasInstalled() {
    Package.hasInstalled({
      bundleName: 'com.example.bundlename',
      success: (data) => {
        console.log('package has installed: ' + data);
      },
      fail: (msg:string, code) => {
        console.log('query package fail, code: ' + code + ', data: ' + msg);
      },
    });
  }
  build() {
  }
}
```

#### CheckPackageHasInstalledResponse

从API version 9开始不再维护。

指示应用包是否已安装。

**系统能力：** SystemCapability.BundleManager.BundleFramework

名称类型必填说明resultboolean是指示应用是否已安装。

#### CheckPackageHasInstalledOptions

从API version 9开始不再维护。

查询包是否已安装时的选项。

**系统能力：** SystemCapability.BundleManager.BundleFramework

名称类型必填说明bundleNamestring是应用Bundle名称。successFunction否接口调用成功的回调函数。failFunction否接口调用失败的回调函数。completeFunction否接口调用结束的回调函数。