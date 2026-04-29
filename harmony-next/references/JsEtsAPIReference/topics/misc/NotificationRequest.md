# NotificationRequest

描述通知的请求。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### NotificationRequest

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | [NotificationContent](NotificationContent.md#ZH-CN_TOPIC_0000002497606116__notificationcontent-1) | 否 | 否 | 通知展示内容。 |
| id | number | 否 | 是 | 通知ID，默认值为0。若已存在相同ID的通知，则更新该通知；若不存在相同ID的通知，则创建新的通知。 |
| updateOnly18+ | boolean | 否 | 是 | 是否仅更新通知，默认值为false。 - true：若已存在相同ID的通知，则更新该通知；若不存在相同ID的通知，则更新失败，并且不创建新的通知。 - false：若已存在相同ID的通知，则更新该通知；若不存在相同ID的通知，则创建新的通知。 |
| appMessageId12+ | string | 否 | 是 | 应用发送通知携带的唯一标识字段，用于通知去重。如果同一应用通过本地和云端等不同途径发布携带相同appMessageId的通知，设备只展示一条消息，之后收到的重复通知会被静默去重，不展示、不提醒。去重标识仅在通知发布的24小时内有效，超过24小时或者设备重启失效。 |
| notificationSlotType11+ | notificationManager.SlotType | 否 | 是 | 通知渠道类型，默认值为OTHER_TYPES。不同渠道类型的通知提醒方式不同。 |
| notificationFlags8+ | [NotificationFlags](NotificationFlags.md) | 否 | 是 | 设置或获取NotificationFlags。从API version 23开始成为可写参数，可以按需削减通知的提醒方式。 |
| priorityNotificationType23+ | notificationManager.PriorityNotificationType | 否 | 是 | 通知优先级类型。设置该参数可使通知置顶，并且在通知中心以突出方式显示。 仅当应用申请并获得优先通知权益后，该字段方可生效。实际显示效果依赖于设备能力和通知中心UI样式。 模型约束： 此接口仅可在Stage模型下使用。 |
| isAlertOnce | boolean | 否 | 是 | 发布或更新该通知时，是否只进行一次通知提醒，默认为false。 - true：仅首次发布通知时进行提醒，后续更新该通知时，提醒方式变更为LEVEL_LOW。 - false：每次均按照配置的通知提醒方式进行提醒。 |
| sound12+ | string | 否 | 是 | 应用通知自定义铃声文件名。该文件必须放在resources/rawfile目录下，支持m4a、aac、mp3、ogg、wav、flac、amr等格式。 |
| badgeNumber9+ | number | 否 | 是 | 应用程序图标上显示的通知数，该数量累计展示。 当badgeNumber取值小于或等于0时，将忽略本次角标设定。 当角标累加设定个数取值大于99时，通知角标将显示99+。 例如，应用发布3条通知，badgeNumber依次设置为2、0、3，应用将依次展示为2、2、5。 |
| wantAgent | WantAgent | 否 | 是 | 封装了应用的行为意图，点击通知时触发该行为。 |
| actionButtons | Array<[NotificationActionButton](NotificationActionButton.md)> | 否 | 是 | 通知按钮，默认一条通知中最多包含两个按钮。从API version 16开始，支持wearable设备，wearable设备中一条通知中最多包含三个按钮。 |
| removalWantAgent9+ | WantAgent | 否 | 是 | 封装了应用的行为意图，移除通知时触发该行为。 当前不支持跳转UIAbility，只支持发布公共事件（即[WantAgentInfo](WantAgentInfo.md#ZH-CN_TOPIC_0000002529444605__wantagentinfo-1)的actionType字段取值为4）。 |
| tapDismissed | boolean | 否 | 是 | 点击通知携带的wantAgent或actionButtons时，该通知是否自动清除。当通知携带wantAgent或actionButtons时该字段生效。默认值为true。 - true：点击通知或按钮后，自动删除当前通知。 - false：点击通知或按钮后，保留当前通知。 |
| autoDeletedTime | number | 否 | 是 | 通知定时清除时间。设置该参数可使通知在指定时间后自动清除。 数据格式：时间戳。 单位：ms。 例如，希望某通知存留3秒（3000ms）后对其进行清除，则对应的清除时间为：new Date().getTime() + 3000。 |
| deliveryTime | number | 否 | 是 | 通知发送时间。系统自动生成，无需开发者配置。 数据格式：时间戳。 单位：ms。 |
| label | string | 否 | 是 | 通知标签。 label字段的功能类似于id，可以单独使用，也可与id结合共同作为通知的标识。优先推荐使用id。 如果发布通知时label不为空，那么在更新或删除该通知时，也需要指定相应的label。 |
| smallIcon | image.PixelMap | 否 | 是 | 通知小图标。图标像素的总字节数不超过192KB（图标像素的总字节数通过getPixelBytesNumber获取），建议图标像素长宽为128*128。实际显示效果依赖于设备能力和通知中心UI样式。 |
| largeIcon | image.PixelMap | 否 | 是 | 通知大图标。图标像素的总字节数不超过192KB（图标像素的总字节数通过getPixelBytesNumber获取），建议图标像素长宽为128*128。实际显示效果依赖于设备能力和通知中心UI样式。 |
| overlayIcon23+ | image.PixelMap | 否 | 是 | 通知重叠图标。图像像素的总字节数不超过192KB（图标像素的总字节数通过getPixelBytesNumber获取）。 此接口只在notificationSlotType类型设置为SOCIAL_COMMUNICATION时生效。建议图标像素长宽为128*128。实际显示效果依赖于设备能力和通知中心UI样式。 |
| groupName8+ | string | 否 | 是 | 通知所属组。当不同通知的groupName相同时，这些通知将成组展示。默认为空。 |
| template8+ | [NotificationTemplate](NotificationTemplate.md) | 否 | 是 | 通知模板。 |
| extraInfo | {[key: string]: any} | 否 | 是 | 扩展参数。为应用提供定制服务。 以下Key由系统赋值，开发者手动修改也不会生效，系统在数据传递时会自动修改为实际值。 - 'ohos.notificationManager.wantUri'：用户点击通知时传递给应用的Want 中的uri字段，使用getActiveNotifications接口获取该信息。 |
| slotType(deprecated) | notification.SlotType | 否 | 是 | 通知渠道类型。 从API version 7开始支持，从API version 11开始废弃，建议使用notificationSlotType替代。 |
| hashCode | string | 是 | 是 | 通知唯一标识。 |
| creatorBundleName | string | 是 | 是 | 创建通知的应用名称。 |
| creatorUid | number | 是 | 是 | 创建通知的应用UID。 |
| creatorPid | number | 是 | 是 | 创建通知的PID。 |
| creatorUserId8+ | number | 是 | 是 | 创建通知的用户ID。 |
| isOngoing | boolean | 否 | 是 | 预留能力，暂未支持。 |
| isUnremovable | boolean | 否 | 是 | 预留能力，暂未支持。 |
| color | number | 否 | 是 | 通知背景颜色。预留能力，暂未支持。 |
| colorEnabled | boolean | 否 | 是 | 通知背景颜色是否使能。预留能力，暂未支持。 |
| isStopwatch | boolean | 否 | 是 | 是否显示已用时间。预留能力，暂未支持。 |
| isCountDown | boolean | 否 | 是 | 是否显示倒计时时间。预留能力，暂未支持。 |
| isFloatingIcon | boolean | 否 | 是 | 是否显示状态栏图标。预留能力，暂未支持。 |
| distributedOption8+ | DistributedOptions | 否 | 是 | 分布式通知的选项。预留能力，暂未支持。 |
| badgeIconStyle | number | 否 | 是 | 通知角标类型。预留能力，暂未支持。 |
| showDeliveryTime | boolean | 否 | 是 | 是否显示分发时间。预留能力，暂未支持。 |

#### DistributedOptions8+

描述跨设备协同选项。预留能力，暂未支持。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isDistributed | boolean | 否 | 是 | 是否支持跨设备协同通知。默认为true。 - true：支持跨设备协同通知。 - false：不支持跨设备协同通知。 |
| supportDisplayDevices | Array<string> | 否 | 是 | 可以同步通知到的设备列表。 |
| supportOperateDevices | Array<string> | 否 | 是 | 可以打开通知的设备列表。 |
