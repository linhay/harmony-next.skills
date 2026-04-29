# appInfoManager（应用元数据管理服务）

提供查询动态图标信息、选择动态图标、禁用动态图标功能。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

调用接口需捕获异常。

起始版本： 5.0.3(15)

**导入模块**

```ets
import { appInfoManager } from '@kit.AppGalleryKit';
```

**DynamicIconInfo**

动态图标信息。

系统能力： SystemCapability.AppGalleryService.AppInfoManager

起始版本： 5.0.3(15)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iconUrl | string | 是 | 否 | 动态图标链接。 |
| iconId | string | 是 | 否 | 动态图标ID。 |
| enabled | boolean | 是 | 否 | 该动态图标是否正在使用中。true表示当前正在使用中，false表示当前未使用。 |

**appInfoManager.queryDynamicIcons**

queryDynamicIcons(): Promise<DynamicIconInfo[]>

查询动态图标信息。通过Promise异步回调。

系统能力： SystemCapability.AppGalleryService.AppInfoManager

起始版本： 5.0.3(15)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<DynamicIconInfo[]> | Promise对象，返回动态图标信息。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1006800001 | The specified service extension connect failed. |
| 1006800009 | System internal error. |
| 1006800010 | No dynamic icon data. |

示例：

```ets
import { appInfoManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appInfoManager.queryDynamicIcons()
    .then((queryResult: appInfoManager.DynamicIconInfo[]) => {
      hilog.info(0, 'TAG', "Succeeded in getting DynamicIconInfo size = " + queryResult.length);
      for (let i = 0; i < queryResult.length; i++) {
        hilog.info(0, 'TAG', "Succeeded in getting DynamicIconInfo iconUrl = " + queryResult[i]["iconUrl"] + ", iconId = " + queryResult[i]["iconId"] + ", enabled = "+queryResult[i]["enabled"]);
      }
    }).catch((error: BusinessError) => {
      hilog.error(0, 'TAG', "queryDynamicIcons failed, code: " + error.code + ", exception message: " + error.message);
    });
} catch (error) {
  hilog.error(0, 'TAG', "queryDynamicIcons exception code: " + error.code + ", exception message: " + error.message);
}
```

**appInfoManager.selectDynamicIcon**

selectDynamicIcon(iconId: string): Promise<void>

选择动态图标。通过Promise异步回调。

系统能力： SystemCapability.AppGalleryService.AppInfoManager

起始版本： 5.0.3(15)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| iconId | string | 是 | 动态图标ID。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006800009 | System internal error. |
| 1006800011 | Select dynamic icon failed. |
| 1006800013 | Failed to switch to the custom icon because a custom theme icon is currently in use. |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从版本6.0.0(20)开始，该接口支持返回1006800013错误码。

示例：

```ets
import { appInfoManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let iconId: string = 'iconId';
  appInfoManager.selectDynamicIcon(iconId).then(() => {
      hilog.info(0, 'TAG', "Succeeded in selecting dynamic icon");
  }).catch((error: BusinessError) => {
    hilog.error(0, 'TAG', "selectDynamicIcon failed, code: " + error.code + ", exception message: " + error.message);
  });
} catch (error) {
  hilog.error(0, 'TAG', "selectDynamicIcon exception code: " + error.code + ", exception message: " + error.message);
}
```

**appInfoManager.disableDynamicIcon**

disableDynamicIcon(): Promise<void>

禁用动态图标，恢复默认图标。通过Promise异步回调。

系统能力： SystemCapability.AppGalleryService.AppInfoManager

起始版本： 5.0.3(15)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1006800009 | System internal error. |
| 1006800012 | Disable dynamic icon failed. |

示例：

```ets
import { appInfoManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appInfoManager.disableDynamicIcon().then(() => {
      hilog.info(0, 'TAG', "Succeeded in disabling dynamic icon");
  }).catch((error: BusinessError) => {
    hilog.error(0, 'TAG', "disableDynamicIcon failed, code: " + error.code + ", exception message: " + error.message);
  });
} catch (error) {
  hilog.error(0, 'TAG', "disableDynamicIcon exception code: " + error.code + ", exception message: " + error.message);
}
```