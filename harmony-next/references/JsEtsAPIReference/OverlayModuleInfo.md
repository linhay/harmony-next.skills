# OverlayModuleInfo

OverlayModuleInfo信息，可以通过[overlay.getOverlayModuleInfo](@ohos.bundle.overlay (overlay模块).md#ZH-CN_TOPIC_0000002497604614__overlaygetoverlaymoduleinfo)接口获取当前应用中具有overlay特征模块的OverlayModuleInfo信息。

本模块首批接口从API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { overlay } from '@kit.AbilityKit';
```

#### OverlayModuleInfo

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

名称类型只读可选说明bundleNamestring是否overlay特征module所属的应用的bundle名称。moduleNamestring是否overlay特征module的名称。targetModuleNamestring是否overlay特征指定的目标module的名称，表示当前overlay包的资源需要替换生效的模块名称。prioritynumber是否overlay特征module的优先级。取值为整数，取值范围1 ~ 100，数值越大优先级越高。statenumber是否overlay特征module的[禁用使能状态](@ohos.bundle.overlay (overlay模块).md#ZH-CN_TOPIC_0000002497604614__overlaysetoverlayenabled)。0代表禁用状态，1代表使能状态。