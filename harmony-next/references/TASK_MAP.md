# Task-Driven Index

## UI & Layout
- 推荐 Kit: ArkUI
- Keywords: ArkUI, List, Grid, Tabs, Navigation, Component
- 快速命中: `rg -n "(List|Grid|Tabs|Navigation|LazyForEach|FrameNode)" JsEtsAPIReference/INDEX.md | head`

## App LifeCycle
- 推荐 Kit: AbilityKit
- Keywords: UIAbility, AbilityStage, Context, Want
- 快速命中: `rg -n "(UIAbility|AbilityStage|Context|Want|ExtensionAbility)" JsEtsAPIReference/INDEX.md | head`

## Network
- 推荐 Kit: NetworkKit, ArkWeb
- Keywords: rcp, http, socket, Web
- 快速命中: `rg -n "(http|socket|@ohos\\.net\\.|@ohos\\.web\\.)" JsEtsAPIReference/INDEX.md | head`

## Media
- 推荐 Kit: MediaKit, CameraKit, ImageKit
- Keywords: Audio, Video, Camera, Image
- 快速命中: `rg -n "(@ohos\\.multimedia\\.|Camera|Audio|Video|Image)" JsEtsAPIReference/INDEX.md | head`

## Data Management
- 推荐 Kit: ArkData
- Keywords: rdb, Preferences, DataObject, distributedData
- 快速命中: `rg -n "(@ohos\\.data\\.|rdb|Preferences|distributed)" JsEtsAPIReference/INDEX.md | head`

## IDE & Development
- 推荐目录: ideGuides/
- Keywords: 签名, Signing, 证书, Profile
- Keywords: 模拟器, Emulator, Simulator, 真机, 运行
- Keywords: 调试, Debug, 断点, LLDB
- Keywords: 日志, Log, HiLog, 故障分析, FaultLog
- Keywords: 命令行, CLI, hdc, ohpm, hvigor, 自动化
- Keywords: 独立工具包, Standalone CLI, OHOS_BASE_SDK_HOME, 环境变量, CI/CD配置
- 快速命中: `rg -n "(签名|Signing|hdc|hvigor|ohpm|LLDB|HiLog)" INDEX.md | rg \"^ideGuides/\" | head`

## Performance & Optimization
- 推荐目录: performanceAndStandards/
- Keywords: Profiler, 性能, 调优, 卡顿, 丢帧, Jank, FPS
- Keywords: CPU分析, Call Tree, 热点函数
- Keywords: 内存泄漏, Snapshot, GC, 耗电量
- Keywords: 延迟, 启动优化, AppStartup, LazyForEach
- 快速命中: `rg -n "(Profiler|性能|调优|Jank|FPS|启动优化|AppStartup)" INDEX.md | rg \"^performanceAndStandards/\" | head`

## App Basics & Architecture
- 推荐目录: appBasics/, multiDevice/, continuation/
- Keywords: HAP, HAR, HSP, 包结构, 共享包
- Keywords: Stage模型, FA模型, UIAbility, ExtensionAbility
- Keywords: 并发模型, TaskPool, Worker, Event Loop
- Keywords: 一次开发多端部署, 一多, 自适应布局, 响应式布局, 断点, 栅格
- Keywords: 自由流转, 跨端迁移, 多端协同, Continuation
- 快速命中: `rg -n "(HAP|HAR|HSP|Stage|TaskPool|Worker|自适应|响应式|Continuation)" INDEX.md | head`

## NDK & Native
- 推荐目录: ndkGuides/, JsEtsAPIReference/capi/headers/
- Keywords: NDK, Node-API, napi, C++, CMake, 跨语言互调
- 快速命中: `rg -n "(Node-API|napi|CMake|NDK)" INDEX.md | head`

## Publishing
- 推荐目录: publishing/, distribution/
- Keywords: 上架, 发布, AGC, AppGallery Connect, 审核, Profile
- 快速命中: `rg -n "(AppGallery|AGC|上架|发布|审核)" INDEX.md | head`

## Testing
- 推荐目录: testing/
- Keywords: 测试, Hypium, 单元测试, UI测试
- Keywords: 自动化测试, 断言, Mock, By定位
- Keywords: AI辅助编程, CodeGenie, 代码生成
- 快速命中: `rg -n "(Hypium|单元测试|UI测试|By定位|Mock)" INDEX.md | rg \"^testing/\" | head`
