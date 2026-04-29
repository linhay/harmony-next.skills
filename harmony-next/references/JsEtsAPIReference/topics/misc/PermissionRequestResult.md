# PermissionRequestResult

权限请求结果对象，在调用[requestPermissionsFromUser](@ohos.abilityAccessCtrl (程序访问控制管理).md#ZH-CN_TOPIC_0000002553360477__requestpermissionsfromuser9)申请权限时返回此对象表明此次权限申请的结果。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

- 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

- 本模块接口仅可在Stage模型下使用。

**属性**

系统能力：以下各项对应的系统能力均为SystemCapability.Security.AccessToken

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| permissions | Array<string> | 否 | 否 | 用户传入的权限。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| authResults | Array<number> | 否 | 否 | 相应请求权限的结果： - -1：未授权。①dialogShownResults返回为true，表示用户首次申请；②dialogShownResults返回为false，表示权限已设置，无需弹窗，需要用户在"设置"中修改。 - 0：已授权。 - 2：未授权，表示请求无效。可能原因有：①未在设置文件中声明目标权限；②权限名非法；③部分权限存在特殊申请条件，在申请对应权限时未满足其指定的条件，见ohos.permission.LOCATION与ohos.permission.APPROXIMATELY_LOCATION。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| dialogShownResults12+ | Array<boolean> | 否 | 是 | 此权限申请是否有弹窗： - true：有弹窗。 - false：无弹窗。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| errorReasons18+ | Array<number> | 否 | 是 | 申请相应权限的返回值说明： 0：本次申请合法。 1：权限名非法。 2：权限未声明。 3：不满足对应权限的申请条件，请参考权限列表中具体权限的说明。当前仅位置权限涉及。 4：用户未同意隐私声明。 5：该权限不支持通过权限弹窗进行申请，可能原因为该权限不支持申请或被系统策略强制管控。 6：该权限授权方式为manual_settings，无法通过权限弹窗申请。 12：服务异常。 元服务API：从API version 18开始，该接口支持在元服务中使用。 |

**使用说明**

通过atManager实例来获取。

示例：

示例中context的获取方式请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { abilityAccessCtrl, Context, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager = abilityAccessCtrl.createAtManager();
try {
  // 请在组件内获取context
  let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  atManager.requestPermissionsFromUser(context, ["ohos.permission.CAMERA"]).then((data) => {
      console.info("data permissions:" + data.permissions);
      console.info("data authResults:" + data.authResults);
      console.info("data dialogShownResults:" + data.dialogShownResults);
      console.info("data errorReasons:" + data.errorReasons);
  }).catch((err: BusinessError) => {
      console.error(`code: ${err.code}, message: ${err.message}`);
  })
} catch(err) {
  console.error(`catch errcode: ${err.code}, message: ${err.message}`);
}
```