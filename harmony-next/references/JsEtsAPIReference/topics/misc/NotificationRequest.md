# NotificationRequest

描述通知的请求。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### NotificationRequest

**系统能力**：SystemCapability.Notification.Notification

名称类型只读可选说明content[NotificationContent](NotificationContent.md#ZH-CN_TOPIC_0000002497606116__notificationcontent-1)否否通知内容。idnumber否是通知ID，默认为0。当相同通知ID存在时，将更新该通知的内容。slotType(deprecated)[notification.SlotType](../../modules/ohos/@ohos.notification (Notification模块).md#ZH-CN_TOPIC_0000002529286111__slottype)否是

通知渠道类型。

从API version 7开始支持，从API version 11开始废弃，建议使用notificationSlotType替代。

notificationSlotType11+[notificationManager.SlotType](../../modules/ohos/@ohos.notificationManager (NotificationManager模块).md#ZH-CN_TOPIC_0000002497446132__slottype)否是通知渠道类型，默认为OTHER_TYPES。isOngoingboolean否是预留能力，暂未支持。isUnremovableboolean否是预留能力，暂未支持。updateOnly18+boolean否是

是否仅更新通知，默认值为false。

 - true：若相同ID通知存在，则更新通知；若相同ID通知不存在，则更新失败，不创建新的通知。

 - false：若相同ID通知存在，则更新通知；若相同ID通知不存在，则创建通知。

deliveryTimenumber否是

通知发送时间。系统自动生成，无需开发者配置。

数据格式：时间戳。

单位：ms。

tapDismissedboolean否是

通知是否自动清除。当通知携带wantAgent或actionButtons时该字段生效。默认值为true。

 - true：点击通知或按钮后，自动删除当前通知。

 - false：点击通知或按钮后，保留当前通知。

autoDeletedTimenumber否是

自动清除的时间。

数据格式：时间戳。

单位：ms。

例如，希望某通知存留3秒（3000ms）后对其进行清除，则对应的清除时间为：new Date().getTime() + 3000。

wantAgent[WantAgent](../../modules/ohos/@ohos.app.ability.wantAgent (WantAgent模块).md)否是WantAgent封装了应用的行为意图，点击通知时触发该行为。extraInfo{[key: string]: any}否是扩展参数。为应用提供定制服务。colornumber否是通知背景颜色。预留能力，暂未支持。colorEnabledboolean否是通知背景颜色是否使能。预留能力，暂未支持。isAlertOnceboolean否是

发布或更新该通知时，是否只进行一次通知提醒，默认为false。

 - true：仅首次发布通知时进行提醒，后续更新该通知时，提醒方式变更为[LEVEL_MIN](../../modules/ohos/@ohos.notificationManager (NotificationManager模块).md#ZH-CN_TOPIC_0000002497446132__slotlevel)。

 - false：每次均按照配置的通知提醒方式进行提醒。

isStopwatchboolean否是是否显示已用时间。预留能力，暂未支持。isCountDownboolean否是是否显示倒计时时间。预留能力，暂未支持。isFloatingIconboolean否是是否显示状态栏图标。预留能力，暂未支持。labelstring否是

通知标签。

label字段的功能类似于id，可以单独使用，也可与id结合共同作为通知的标识。优先推荐使用id。

如果发布通知时label不为空，那么在更新或删除该通知时，也需要指定相应的label。

badgeIconStylenumber否是通知角标类型。预留能力，暂未支持。showDeliveryTimeboolean否是是否显示分发时间。预留能力，暂未支持。actionButtonsArray<[NotificationActionButton](../components/NotificationActionButton.md)>否是通知按钮，默认一条通知中最多包含两个按钮。从API version 16开始，支持wearable设备，wearable设备中一条通知中最多包含三个按钮。smallIcon[image.PixelMap](../../types/interfaces/Interface (PixelMap).md)否是通知小图标。可选字段，图标像素的总字节数不超过192KB（图标像素的总字节数通过[getPixelBytesNumber](../../types/interfaces/Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__getpixelbytesnumber7)获取），建议图标像素长宽为128*128。实际显示效果依赖于设备能力和通知中心UI样式。largeIcon[image.PixelMap](../../types/interfaces/Interface (PixelMap).md)否是通知大图标。可选字段，图标像素的总字节数不超过192KB（图标像素的总字节数通过[getPixelBytesNumber](../../types/interfaces/Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__getpixelbytesnumber7)获取），建议图标像素长宽为128*128。实际显示效果依赖于设备能力和通知中心UI样式。creatorBundleNamestring是是创建通知的包名。creatorUidnumber是是创建通知的UID。creatorPidnumber是是创建通知的PID。creatorUserId8+number是是创建通知的UserId。hashCodestring是是通知唯一标识。groupName8+string否是组通知名称。默认为空。template8+[NotificationTemplate](NotificationTemplate.md)否是通知模板。distributedOption8+[DistributedOptions](#ZH-CN_TOPIC_0000002497606118__distributedoptions8)否是分布式通知的选项。预留能力，暂未支持。notificationFlags8+[NotificationFlags](NotificationFlags.md)是是获取NotificationFlags。removalWantAgent9+[WantAgent](../../modules/ohos/@ohos.app.ability.wantAgent (WantAgent模块).md)否是

当移除通知时，通知将被重定向到的WantAgent实例。

当前不支持跳转UIAbility，只支持发布公共事件（即[WantAgentInfo](../payment/WantAgentInfo.md#ZH-CN_TOPIC_0000002529444605__wantagentinfo-1)的actionType字段取值为4）。

badgeNumber9+number否是

应用程序图标上显示的通知数，该数量累计展示。

当badgeNumber取值小于或等于0时，将忽略本次角标设定。

当角标累加设定个数取值大于99时，通知角标将显示99+。

例如，应用发布3条通知，badgeNumber依次设置为2、0、3，应用将依次展示为2、2、5。

appMessageId12+string否是应用发送通知携带的唯一标识字段, 用于通知去重。如果同一应用通过本地和云端等不同途径发布携带相同appMessageId的通知，设备只展示一条消息，之后收到的重复通知会被静默去重，不展示、不提醒。去重标识仅在通知发布的24小时内有效，超过24小时或者设备重启失效。sound12+string否是应用通知自定义铃声文件名。该文件必须放在resources/rawfile目录下，支持m4a、aac、mp3、ogg、wav、flac、amr等格式。

#### DistributedOptions8+

描述跨设备协同选项。预留能力，暂未支持。

**系统能力**：SystemCapability.Notification.Notification

名称类型只读可选说明isDistributedboolean否是

是否支持跨设备协同通知。默认为true。

 - true：支持跨设备协同通知。

 - false：不支持跨设备协同通知。

supportDisplayDevicesArray<string>否是可以同步通知到的设备列表。supportOperateDevicesArray<string>否是可以打开通知的设备列表。