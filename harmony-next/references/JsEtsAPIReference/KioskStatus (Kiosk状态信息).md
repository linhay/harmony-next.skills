# KioskStatus (Kiosk状态信息)

表示Kiosk状态信息，包括系统是否处于Kiosk模式以及该模式下的应用信息。

- 本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本模块接口仅可在Stage模型下使用。

#### KioskStatus

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明isKioskModeboolean否否当前系统是否处于Kiosk模式。true表示处于Kiosk模式，false表示不处于。kioskBundleNamestring否否进入Kiosk模式的应用的名称。kioskBundleUidnumber否否进入Kiosk模式的应用的UID。