# @ohos.wallpaper (壁纸)

壁纸管理服务为HarmonyOS系统服务，提供壁纸切换功能。从API 9开始壁纸管理的接口调整为系统API，壁纸的切换只能通过系统应用来完成。壁纸管理提供壁纸切换通道，使用壁纸的应用（如：桌面）需订阅壁纸变化通知并刷新壁纸显示。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { wallpaper } from '@kit.BasicServicesKit';
```

#### WallpaperType7+

定义壁纸的枚举类型。

**系统能力**: SystemCapability.MiscServices.Wallpaper

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WALLPAPER_SYSTEM | 0 | 主屏幕壁纸标识。 |
| WALLPAPER_LOCKSCREEN | 1 | 锁屏壁纸标识。 |

#### RgbaColor(deprecated)

定义壁纸颜色信息结构。

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| red | number | 否 | 否 | 表示红色值，范围为 0 到 255。 |
| green | number | 否 | 否 | 表示绿色值，范围为 0 到 255。 |
| blue | number | 否 | 否 | 表示蓝色值，范围为 0 到 255。 |
| alpha | number | 否 | 否 | 表示 alpha 值，范围为 0 到 255。 |

#### wallpaper.on('colorChange')(deprecated)

on(type: 'colorChange', callback: (colors: Array<RgbaColor>, wallpaperType: WallpaperType) => void): void

订阅壁纸颜色变化结果上报事件。不支持多线程并发调用。

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取值为'colorChange'，表示壁纸颜色变化结果上报事件。 |
| callback | function | 是 | 壁纸颜色变化触发该回调方法，返回壁纸类型和壁纸的主要颜色信息。 - colors  壁纸的主要颜色信息，其类型见RgbaColor。 - wallpaperType  壁纸类型。 |

**示例：**

```ets
try {
    let listener = (colors: Array<wallpaper.RgbaColor>, wallpaperType: wallpaper.WallpaperType): void => {
        console.info(`wallpaper color changed.`);
    };
    wallpaper.on('colorChange', listener);
} catch (error) {
    console.error(`failed to on because: ${JSON.stringify(error)}`);
}
```

#### wallpaper.off('colorChange')(deprecated)

off(type: 'colorChange', callback?: (colors: Array<RgbaColor>, wallpaperType: WallpaperType) => void): void

取消订阅壁纸颜色变化结果上报事件。不支持多线程并发调用。

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取值为'colorChange'，表示取消订阅壁纸颜色变化结果上报事件。 |
| callback | function | 否 | 表示要取消的壁纸颜色变化的回调，不填写该参数则取消订阅该type对应的所有回调。 - colors  壁纸的主要颜色信息，其类型见RgbaColor。 - wallpaperType  壁纸类型。 |

**示例：**

```ets
let listener = (colors: Array<wallpaper.RgbaColor>, wallpaperType: wallpaper.WallpaperType): void => {
    console.info(`wallpaper color changed.`);
};
try {
    wallpaper.on('colorChange', listener);
} catch (error) {
    console.error(`failed to on because: ${JSON.stringify(error)}`);
}

try {
    // 取消订阅listener
    wallpaper.off('colorChange', listener);
} catch (error) {
    console.error(`failed to off because: ${JSON.stringify(error)}`);
}

try {
    // 取消所有'colorChange'类型的订阅
    wallpaper.off('colorChange');
} catch (error) {
    console.error(`failed to off because: ${JSON.stringify(error)}`);
}
```

#### wallpaper.getColors(deprecated)

getColors(wallpaperType: WallpaperType, callback: AsyncCallback<Array<RgbaColor>>): void

获取指定类型壁纸的主要颜色信息。

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wallpaperType | WallpaperType | 是 | 壁纸类型。 |
| callback | AsyncCallback<Array<RgbaColor>> | 是 | 回调函数，返回壁纸的主要颜色信息。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getColors(wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError, data: Array<wallpaper.RgbaColor>) => {
    if (error) {
        console.error(`failed to getColors because: ${JSON.stringify(error)}`);
        return;
    }
    console.info(`success to getColors: ${JSON.stringify(data)}`);
});
```

#### wallpaper.getColors(deprecated)

getColors(wallpaperType: WallpaperType): Promise<Array<RgbaColor>>

获取指定类型壁纸的主要颜色信息。

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wallpaperType | WallpaperType | 是 | 壁纸类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<RgbaColor>> | 返回壁纸的主要颜色信息。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getColors(wallpaper.WallpaperType.WALLPAPER_SYSTEM).then((data: Array<wallpaper.RgbaColor>) => {
    console.info(`success to getColors: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`failed to getColors because: ${JSON.stringify(error)}`);
});
```

#### wallpaper.getId(deprecated)

getId(wallpaperType: WallpaperType, callback: AsyncCallback<number>): void

获取指定类型壁纸的ID。

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wallpaperType | WallpaperType | 是 | 壁纸类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回壁纸的ID。如果配置了指定类型的壁纸就返回一个大于等于0的数，否则返回-1。取值范围是-1到（2^31-1）。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getId(wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError, data: Number) => {
    if (error) {
        console.error(`failed to getId because: ${JSON.stringify(error)}`);
        return;
    }
    console.info(`success to getId: ${JSON.stringify(data)}`);
});
```

#### wallpaper.getId(deprecated)

getId(wallpaperType: WallpaperType): Promise<number>

获取指定类型壁纸的ID。

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wallpaperType | WallpaperType | 是 | 壁纸类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 壁纸的ID。如果配置了这种壁纸类型的壁纸就返回一个大于等于0的数，否则返回-1。取值范围是-1到（2^31-1）。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getId(wallpaper.WallpaperType.WALLPAPER_SYSTEM).then((data: Number) => {
    console.info(`success to getId: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`failed to getId because: ${JSON.stringify(error)}`);
});
```

#### wallpaper.getMinHeight(deprecated)

getMinHeight(callback: AsyncCallback<number>): void

获取壁纸的最小高度值。

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数，返回壁纸的最小高度值，单位是像素。如果返回值等于0，说明没有设置壁纸，调用者应该使用默认显示的高度值代替。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getMinHeight((error: BusinessError, data: Number) => {
    if (error) {
        console.error(`failed to getMinHeight because: ${JSON.stringify(error)}`);
        return;
    }
    console.info(`success to getMinHeight: ${JSON.stringify(data)}`);
});
```

#### wallpaper.getMinHeight(deprecated)

getMinHeight(): Promise<number>

获取壁纸的最小高度值。

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 返回壁纸的最小高度值，单位是像素。如果返回值等于0，说明没有设置壁纸，调用者应该使用默认显示的高度值代替。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getMinHeight().then((data: Number) => {
    console.info(`success to getMinHeight: ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
    console.error(`failed to getMinHeight because: ${JSON.stringify(error)}`);
});
```

#### wallpaper.getMinWidth(deprecated)

getMinWidth(callback: AsyncCallback<number>): void

获取壁纸的最小宽度值。

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数，壁纸的最小宽度值，单位是像素。如果返回值等于0，说明没有设置壁纸，调用者应该使用默认显示的宽度值代替。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getMinWidth((error: BusinessError, data: Number) => {
    if (error) {
        console.error(`failed to getMinWidth because: ${JSON.stringify(error)}`);
        return;
    }
    console.info(`success to getMinWidth: ${JSON.stringify(data)}`);
});
```

#### wallpaper.getMinWidth(deprecated)

getMinWidth(): Promise<number>

获取壁纸的最小宽度值。

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 壁纸的最小宽度值，单位是像素。如果返回值等于0，说明没有设置壁纸，调用者应该使用默认显示的宽度值代替。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getMinWidth().then((data: Number) => {
    console.info(`success to getMinWidth: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`failed to getMinWidth because: ${JSON.stringify(error)}`);
});
```

#### wallpaper.getFile(deprecated)

getFile(wallpaperType: WallpaperType, callback: AsyncCallback<number>): void

获取指定类型的壁纸文件。

从 API version 8开始支持，从API version 9开始废弃。

**需要权限**：ohos.permission.GET_WALLPAPER

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wallpaperType | WallpaperType | 是 | 壁纸类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数，调用成功则返回壁纸文件描述符ID，调用失败则返回error信息。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getFile(wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError, data: number) => {
    if (error) {
        console.error(`failed to getFile because: ${JSON.stringify(error)}`);
        return;
    }
    console.info(`success to getFile: ${JSON.stringify(data)}`);
});
```

#### wallpaper.getFile(deprecated)

getFile(wallpaperType: WallpaperType): Promise<number>

获取指定类型的壁纸文件。

从 API version 8开始支持，从API version 9开始废弃。

**需要权限**：ohos.permission.GET_WALLPAPER

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wallpaperType | WallpaperType | 是 | 壁纸类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 调用成功则返回壁纸文件描述符ID，调用失败则返回error信息。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getFile(wallpaper.WallpaperType.WALLPAPER_SYSTEM).then((data: number) => {
    console.info(`success to getFile: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`failed to getFile because: ${JSON.stringify(error)}`);
});
```

#### wallpaper.isChangePermitted(deprecated)

isChangePermitted(callback: AsyncCallback<boolean>): void

是否允许应用改变当前用户的壁纸。

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数，返回是否允许应用改变当前用户的壁纸。如果允许返回true，否则返回false。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.isChangePermitted((error: BusinessError, data: Boolean) => {
    if (error) {
        console.error(`failed to isChangePermitted because: ${JSON.stringify(error)}`);
        return;
    }
    console.info(`success to isChangePermitted: ${JSON.stringify(data)}`);
});
```

#### wallpaper.isChangePermitted(deprecated)

isChangePermitted(): Promise<boolean>

是否允许应用改变当前用户的壁纸。

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 返回是否允许应用改变当前用户的壁纸。如果允许返回true，否则返回false。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.isChangePermitted().then((data: Boolean) => {
    console.info(`success to isChangePermitted: ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
    console.error(`failed to isChangePermitted because: ${JSON.stringify(error)}`);
});
```

#### wallpaper.isOperationAllowed(deprecated)

isOperationAllowed(callback: AsyncCallback<boolean>): void

是否允许用户设置壁纸。

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数，返回是否允许用户设置壁纸。如果允许返回true，否则返回false。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.isOperationAllowed((error: BusinessError, data: Boolean) => {
    if (error) {
        console.error(`failed to isOperationAllowed because: ${JSON.stringify(error)}`);
        return;
    }
    console.info(`success to isOperationAllowed: ${JSON.stringify(data)}`);
});
```

#### wallpaper.isOperationAllowed(deprecated)

isOperationAllowed(): Promise<boolean>

是否允许用户设置壁纸。

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 异步回调函数，返回是否允许用户设置壁纸。如果允许返回true，否则返回false。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.isOperationAllowed().then((data: Boolean) => {
    console.info(`success to isOperationAllowed: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`failed to isOperationAllowed because: ${JSON.stringify(error)}`);
});
```

#### wallpaper.reset(deprecated)

reset(wallpaperType: WallpaperType, callback: AsyncCallback<void>): void

移除指定类型的壁纸，恢复为默认显示的壁纸。

从 API version 7开始支持，从API version 9开始废弃。

**需要权限**：ohos.permission.SET_WALLPAPER

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wallpaperType | WallpaperType | 是 | 壁纸类型。 |
| callback | AsyncCallback<void> | 是 | 回调函数，移除壁纸成功，error为undefined，否则返回error信息。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.reset(wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError) => {
    if (error) {
        console.error(`failed to reset because: ${JSON.stringify(error)}`);
        return;
    }
    console.info(`success to reset.`);
});
```

#### wallpaper.reset(deprecated)

reset(wallpaperType: WallpaperType): Promise<void>

移除指定类型的壁纸，恢复为默认显示的壁纸。

从 API version 7开始支持，从API version 9开始废弃。

**需要权限**：ohos.permission.SET_WALLPAPER

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wallpaperType | WallpaperType | 是 | 壁纸类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.reset(wallpaper.WallpaperType.WALLPAPER_SYSTEM).then(() => {
    console.info(`success to reset.`);
}).catch((error: BusinessError) => {
    console.error(`failed to reset because: ${JSON.stringify(error)}`);
});
```

#### wallpaper.setWallpaper(deprecated)

setWallpaper(source: string | image.PixelMap, wallpaperType: WallpaperType, callback: AsyncCallback<void>): void

将指定资源设置为指定类型的壁纸。

从 API version 7开始支持，从API version 9开始废弃。

**需要权限**：ohos.permission.SET_WALLPAPER

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | string | image.PixelMap | 是 | JPEG或PNG文件的Uri路径，或者PNG格式文件的位图。 |
| wallpaperType | WallpaperType | 是 | 壁纸类型。 |
| callback | AsyncCallback<void> | 是 | 回调函数，设置壁纸成功，error为undefined，否则返回error信息。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

// source类型为string
let wallpaperPath = "/data/storage/el2/base/haps/entry/files/js.jpeg";
wallpaper.setWallpaper(wallpaperPath, wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError) => {
    if (error) {
        console.error(`failed to setWallpaper because: ${JSON.stringify(error)}`);
       return;
       }
    console.info(`success to setWallpaper.`);
});

// source类型为image.PixelMap
let imageSource = image.createImageSource("file://" + wallpaperPath);
let opts: image.DecodingOptions = {
    desiredSize: {
        height: 3648,
        width: 2736
    }
};
imageSource.createPixelMap(opts).then((pixelMap: image.PixelMap) => {
    wallpaper.setWallpaper(pixelMap, wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError) => {
        if (error) {
            console.error(`failed to setWallpaper because: ${JSON.stringify(error)}`);
            return;
        }
        console.info(`success to setWallpaper.`);
    });
}).catch((error: BusinessError) => {
    console.error(`failed to createPixelMap because: ${JSON.stringify(error)}`);
});
```

#### wallpaper.setWallpaper(deprecated)

setWallpaper(source: string | image.PixelMap, wallpaperType: WallpaperType): Promise<void>

将指定资源设置为指定类型的壁纸。

从 API version 7开始支持，从API version 9开始废弃。

**需要权限**：ohos.permission.SET_WALLPAPER

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | string | image.PixelMap | 是 | JPEG或PNG文件的Uri路径，或者PNG格式文件的位图。 |
| wallpaperType | WallpaperType | 是 | 壁纸类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

// source类型为string
let wallpaperPath = "/data/storage/el2/base/haps/entry/files/js.jpeg";
wallpaper.setWallpaper(wallpaperPath, wallpaper.WallpaperType.WALLPAPER_SYSTEM).then(() => {
    console.info(`success to setWallpaper.`);
  }).catch((error: BusinessError) => {
    console.error(`failed to setWallpaper because: ${JSON.stringify(error)}`);
});

// source类型为image.PixelMap
let imageSource = image.createImageSource("file://" + wallpaperPath);
let opts: image.DecodingOptions = {
    desiredSize: {
        height: 3648,
        width: 2736
    }
};
imageSource.createPixelMap(opts).then((pixelMap: image.PixelMap) => {
    wallpaper.setWallpaper(pixelMap, wallpaper.WallpaperType.WALLPAPER_SYSTEM).then(() => {
        console.info(`success to setWallpaper.`);
    }).catch((error: BusinessError) => {
        console.error(`failed to setWallpaper because: ${JSON.stringify(error)}`);
    });
  }).catch((error: BusinessError) => {
    console.error(`failed to createPixelMap because: ${JSON.stringify(error)}`);
});
```