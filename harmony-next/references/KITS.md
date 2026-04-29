# HarmonyOS Kit Navigation（Kit 识别与检索入口）

目的：先识别你要找的 Kit，再去路径清单里命中文档文件（不要在本文件里找“准确文件路径”）。

## 如何用（渐进式披露）

1. 先看下面“常用 Kit 快速入口”，拿到关键词或模块前缀。
2. 用 `rg` 在路径清单里命中目标文件路径：
   - `INDEX.md`：全库路径（包含 quickStart/、ideGuides/ 等）
   - `JsEtsAPIReference/INDEX.md`：API 分桶路径
3. 命中路径后，只打开那 1-3 个 `.md` 文件继续阅读。

## 常用 Kit 快速入口（优先看这里）

### AbilityKit（应用/能力/上下文）
- 关键词：`UIAbility` `AbilityStage` `Context` `Want` `ExtensionAbility`
- 模块前缀：`@ohos.app.ability.` `@ohos.ability.`
- 快速命中：`rg -n "(@ohos\\.app\\.ability\\.|@ohos\\.ability\\.|UIAbility|Want)" INDEX.md | rg "JsEtsAPIReference/" | head`

### ArkUI（声明式 UI / 组件 / 节点）
- 关键词：`@Entry` `@Component` `build()` `FrameNode` `UIContext` `LazyForEach`
- 模块前缀：`@ohos.arkui.`
- 目录倾向：`JsEtsAPIReference/topics/components/`、`JsEtsAPIReference/modules/ohos/`
- 快速命中：`rg -n "(@ohos\\.arkui\\.|FrameNode|LazyForEach|UIContext)" INDEX.md | rg "JsEtsAPIReference/" | head`

### ArkTS（语言特性/并发/容器）
- 关键词：`TaskPool` `Worker` `sendable` `collections`
- 快速命中：`rg -n "(TaskPool|Worker|sendable|@arkts\\.)" INDEX.md | head`

### ArkData（数据/RDB/分布式/偏好）
- 关键词：`rdb` `distributed` `Preferences` `Udmf`
- 模块前缀：`@ohos.data.`
- 快速命中：`rg -n "(@ohos\\.data\\.|rdb|Preferences|distributed)" INDEX.md | rg "JsEtsAPIReference/" | head`

### MediaKit（音视频/相机/图像）
- 关键词：`Audio` `Video` `Camera` `Image`
- 模块前缀：`@ohos.multimedia.`
- 快速命中：`rg -n "@ohos\\.multimedia\\.|Camera|Audio|Video|Image" INDEX.md | rg "JsEtsAPIReference/" | head`

### ConnectivityKit（网络/蓝牙/NFC/Wi-Fi）
- 关键词：`http` `socket` `bluetooth` `wifi` `nfc`
- 模块前缀：`@ohos.net.` `@ohos.bluetooth.` `@ohos.nfc.` `@ohos.wifi.`
- 快速命中：`rg -n "@ohos\\.(net|bluetooth|nfc|wifi)\\.|socket|http" INDEX.md | rg "JsEtsAPIReference/" | head`

### Security 相关（权限/密钥/认证）
- 关键词：`permission` `abilityAccessCtrl` `huks` `UserAuthentication`
- 模块前缀：`@ohos.abilityAccessCtrl` `@ohos.security.`
- 快速命中：`rg -n "@ohos\\.(abilityAccessCtrl|security\\.)|permission|huks" INDEX.md | rg "JsEtsAPIReference/" | head`

### NDK（C API / 头文件）
- 关键词：`napi` `arkui` `window` `ability`
- 主入口：`JsEtsAPIReference/topics/**/<header>.h.md`
- 快速命中：`rg -n "JsEtsAPIReference/topics/.*/.*\\.h\\.md$" INDEX.md | rg "(napi|arkui|window|ability)" | head`

## Kit 全名单（仅用于识别名称）

- AREngine
- AVSessionKit
- AbilityKit
- AccessibilityKit
- AccountKit
- AdsKit
- AgentFrameworkKit
- AppGalleryKit
- AppLinkingKit
- ArkData
- ArkGraphics2D
- ArkGraphics3D
- ArkTS
- ArkUI
- ArkWeb
- AssetStoreKit
- AudioKit
- BackgroundTasksKit
- BasicServicesKit
- CANNKit
- CalendarKit
- CallServiceKit
- CameraKit
- CarKit
- CloudFoundationKit
- Common/Misc
- ConnectivityKit
- ContactsKit
- CoreFileKit
- CoreSpeechKit
- CoreVisionKit
- CryptoArchitectureKit
- DataAugmentationKit
- DataProtectionKit
- DeskTopExtensionKit
- DeviceCertificateKit
- DeviceSecurityKit
- DistributedServiceKit
- DriverDevelopmentKit
- DrmKit
- EnterpriseDataGuardKit
- EnterpriseSpaceKit
- FileManagerServiceKit
- FormKit
- FusionConnectivity
- GameServiceKit
- GraphicsAccelerateKit
- HealthServiceKit
- IAPKit
- IMEKit
- IPCKit
- ImageKit
- InputKit
- IntentsKit
- LiveViewKit
- LocalizationKit
- LocationKit
- MDMKit
- MapKit
- MechanicKit
- MediaKit
- MediaLibraryKit
- MultiDeviceKit
- MultimodalAwarenessKit
- MultimodalVocalAwarenessKit
- NearbyServiceKit
- NetworkKit
- NotificationKit
- OCRKit
- OneHopKit
- OpenLinkKit
- PacketTransmissionKit
- PaymentKit
- PushKit
- RecognitionKit
- ReaderKit
- RemoteCommunicationKit
- RingtoneKit
- ScanKit
- ScenarioFusionKit
- ScreenTimeGuardKit
- SensorServiceKit
- ServiceCollaborationKit
- ShareKit
- SpatialReconKit
- SpeechKit
- TelephonyKit
- TestKit
- UIDesignKit
- UniversalKeystoreKit
- UserAuthenticationKit
- VisionKit
- WalletKit
- WearEngine
- WeatherServiceKit
