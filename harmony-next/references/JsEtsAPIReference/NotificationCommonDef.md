# NotificationCommonDef

描述应用的包信息。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### BundleOption

描述BundleOption信息，即应用的包信息。

**系统能力**：SystemCapability.Notification.Notification

名称类型只读可选说明bundlestring否否应用程序的名称。uidnumber否是应用程序的UID。从[ApplicationInfo](ApplicationInfo.md)获取，默认为0。

#### GrantedBundleInfo22+

描述已授权的包信息。

**系统能力**：SystemCapability.Notification.Notification

名称类型只读可选说明bundleNamestring否否应用程序的包名。appNamestring是是标识应用的名称。从[ApplicationInfo](ApplicationInfo.md)中label获取。appIndexint是否应用包的分身索引标识，仅在分身应用中生效。从[ApplicationInfo](ApplicationInfo.md)中appIndex获取。