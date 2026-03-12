# @system.app (应用上下文)

本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import app, { AppResponse } from '@system.app';
```

#### App

#### getInfo

static getInfo(): AppResponse

获取当前应用配置文件中声明的信息。在Stage模型下接口返回值为null。

从API Version9开始，推荐使用[bundleManager.getBundleInfoForSelf](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**返回值：**

参数类型说明[AppResponse](#ZH-CN_TOPIC_0000002529284799__appresponse)定义AppResponse信息。

**示例：**

```ets
import app, { AppResponse } from '@system.app';
export default class Info {
  getInfo() {
    let info:AppResponse = app.getInfo();
    console.log(JSON.stringify(info));
  }
}
```

#### terminate

static terminate(): void

退出当前Ability。在Stage模型下接口功能不生效。

从API Version 7开始，推荐使用[@ohos.ability.featureAbility](@ohos.ability.featureAbility (FeatureAbility模块).md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**示例：**

```ets
import app, { AppResponse } from '@system.app';
export default class TerM {
  terminate() {
    app.terminate();
  }
}
```

#### setImageCacheCount7+

static setImageCacheCount(value: number): void

设置内存中缓存解码后图片的数量上限，提升再次加载同源图片的加载速度。如果不设置则默认为0，不进行缓存。缓存采用内置的LRU策略，新图片加载后，如果超过缓存上限，会删除最久未再次加载的缓存。建议根据应用内存需求，设置合理缓存数量，数字过大可能导致内存使用过高。

setImageCacheCount方法需要在@Entry标记的页面，[onPageShow](自定义组件的生命周期.md#ZH-CN_TOPIC_0000002529444913__onpageshow)或[aboutToAppear](自定义组件的生命周期.md#ZH-CN_TOPIC_0000002529444913__abouttoappear)里面设置才生效。

setImageCacheCount、setImageRawDataCacheSize、和setImageFileCacheSize并不灵活，后续不继续演进，对于复杂情况，更推荐使用[ImageKnife](https://gitcode.com/HarmonyOS-tpc/ImageKnife)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuenumber是内存中解码后图片的缓存数量。number取值需大于0。

**示例：**

```ets
// xxx.ets
import app, { AppResponse } from '@system.app';

@Entry
@Component
struct Index {
  onPageShow() {
    // 设置解码后图片内存缓存上限为100张
    app.setImageCacheCount(100);
    console.info('Application onPageShow');
  }
  onDestroy() {
    console.info('Application onDestroy');
  }

  build() {
    Row(){
      // xxxxxxxxxxxxx为图片地址
      Image('xxxxxxxxxxxxx')
        .width(200)
        .height(50)
    }.width('100%')
  }
}
```

#### setImageRawDataCacheSize7+

static setImageRawDataCacheSize(value: number): void

设置内存中缓存解码前图片数据的大小上限，单位为字节，提升再次加载同源图片的加载速度。如果不设置则默认为0，不进行缓存。缓存采用内置的LRU策略，新图片加载后，如果解码前数据超过缓存上限，会删除最久未再次加载的图片数据缓存。建议根据应用内存需求，设置合理缓存上限，过大可能导致应用内存使用过高。

setImageRawDataCacheSize方法需要在@Entry标记的页面，[onPageShow](自定义组件的生命周期.md#ZH-CN_TOPIC_0000002529444913__onpageshow)或[aboutToAppear](自定义组件的生命周期.md#ZH-CN_TOPIC_0000002529444913__abouttoappear)里面设置才生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuenumber是内存中解码前图片数据的缓存大小，单位为字节。number取值需大于0。

**示例：**

```ets
// xxx.ets
import app, { AppResponse } from '@system.app';

@Entry
@Component
struct Index {
  onPageShow() {
    // 设置解码前图片数据内存缓存上限为100MB (100MB=100*1024*1024B=104857600B)
    app.setImageRawDataCacheSize(104857600);
    console.info('Application onPageShow');
  }
  onDestroy() {
    console.info('Application onDestroy');
  }

  build() {
    Row(){
      // xxxxxxxxxxxxx为图片地址
      Image('xxxxxxxxxxxxx')
        .width(200)
        .height(50)
    }.width('100%')
  }
}
```

#### setImageFileCacheSize7+

static setImageFileCacheSize(value: number): void

设置图片文件缓存的大小上限，单位为字节，提升再次加载同源图片的加载速度，特别是对网络图源会有较明显提升。如果不设置则默认为100MB。缓存采用内置的LRU策略，新图片加载后，如果超过文件缓存上限，会按照时间由远到近删除缓存图片文件直到缓存图片大小满足缓存上限。建议根据应用实际需求，设置合理文件缓存上限，数字过大可能导致磁盘空间占用过高。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuenumber是图片文件的缓存大小，单位为字节。number取值需大于0。

**示例：**

```ets
// app.ets
import app, { AppResponse } from '@system.app';

export default class OnC {
  onCreate() {
    app.setImageFileCacheSize(209715200);
    // 设置图片文件数据缓存上限为200MB (200MB=200*1024*1024B=209715200B)
    console.info('Application onCreate');
  }
  onDestroy() {
    console.info('Application onDestroy');
  }
}
```

#### ScreenOnVisible(deprecated)

static screenOnVisible(options?: ScreenOnVisibleOptions): void

定义屏幕唤醒时是否保持应用可见。

该接口从API Version 8 开始废弃。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

名称类型必填说明options[ScreenOnVisibleOptions](#ZH-CN_TOPIC_0000002529284799__screenonvisibleoptions)否当启动保活时，锁屏时将阻止系统返回桌面显示，以保持屏幕唤醒时应用可见。

#### requestFullWindow(deprecated)

static requestFullWindow(options?: RequestFullWindowOptions): void

请求应用以全窗口运行，FA在某些场景下（如半模态FA）会以非全窗口运行，调用该接口会从非全窗口切换为全窗口运行，如果已经以全窗口运行则该接口调用无效。

从API Version 7开始，推荐使用[@ohos.window](模块描述.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[RequestFullWindowOptions](#ZH-CN_TOPIC_0000002529284799__requestfullwindowoptions)否请求全屏时，设定非全屏到全屏的过渡时间，单位为毫秒，默认时间与非全屏到全屏的距离成正比。

**示例：**

```ets
import app, { AppResponse } from '@system.app';
export default class Req {
  requestFullWindow() {
    app.requestFullWindow({
      duration: 200
    });
  }
}
```

#### AppResponse

定义AppResponse信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** 以下各项对应的系统能力有所不同，详见下表。

名称类型必填说明appID6+string是

表示应用的包名，用于标识应用的唯一性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

appNamestring是

表示应用的名称。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

versionNamestring是

表示应用的版本名称。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

versionCodenumber是

表示应用的版本号。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

#### ScreenOnVisibleOptions

定义屏幕上可见接口的选项。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

名称类型必填说明visibleboolean否是否启动保活，默认值false。success() => void否接口调用成功的回调函数。fail(data: string, code: number) => void否接口调用失败的回调函数。complete() => void否接口调用结束的回调函数。

#### RequestFullWindowOptions

定义RequestFullWindow接口的选项。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

名称类型必填说明durationnumber是定义动画选项的持续时间，单位为毫秒。