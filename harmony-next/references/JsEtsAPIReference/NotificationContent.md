# NotificationContent

描述通知类型。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### NotificationContent

通知内容。

**系统能力**：SystemCapability.Notification.Notification

名称类型只读可选说明contentType(deprecated)[notification.ContentType](@ohos.notification (Notification模块).md#ZH-CN_TOPIC_0000002529286111__contenttype)否是

通知内容类型。

从API version 7开始支持，从API version 11开始废弃，建议使用notificationContentType替代。

notificationContentType11+[notificationManager.ContentType](@ohos.notificationManager (NotificationManager模块).md#ZH-CN_TOPIC_0000002497446132__contenttype)否是通知内容类型。normal[NotificationBasicContent](#ZH-CN_TOPIC_0000002497606116__notificationbasiccontent)否是基本类型通知内容。longText[NotificationLongTextContent](#ZH-CN_TOPIC_0000002497606116__notificationlongtextcontent)否是长文本类型通知内容。multiLine[NotificationMultiLineContent](#ZH-CN_TOPIC_0000002497606116__notificationmultilinecontent)否是多行类型通知内容。picture[NotificationPictureContent](#ZH-CN_TOPIC_0000002497606116__notificationpicturecontent)否是图片类型通知内容。systemLiveView11+[NotificationSystemLiveViewContent](#ZH-CN_TOPIC_0000002497606116__notificationsystemliveviewcontent)否是系统实况窗类型通知内容。不支持三方应用直接创建该类型通知，可以由系统代理创建系统实况窗类型通知后，三方应用发布同ID的通知来更新指定内容。

#### NotificationBasicContent

描述普通文本通知。

**系统能力**：SystemCapability.Notification.Notification

名称类型只读可选说明titlestring否否通知标题（不可为空字符串，大小不超过1024字节，超出部分会被截断）。textstring否否通知内容（不可为空字符串，大小不超过3072字节，超出部分会被截断）。additionalTextstring否是通知附加内容，是对通知内容的补充（大小不超过3072字节，超出部分会被截断）。lockscreenPicture12+[image.PixelMap](Interface (PixelMap).md)否是通知在锁屏界面显示的图片。当前仅支持实况窗类型通知。图标像素的总字节数不超过192KB（图标像素的总字节数通过[getPixelBytesNumber](Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__getpixelbytesnumber7)获取），建议图标像素长宽为128*128。实际显示效果依赖于设备能力和通知中心UI样式。

#### NotificationLongTextContent

描述长文本通知。继承自[NotificationBasicContent](#ZH-CN_TOPIC_0000002497606116__notificationbasiccontent)。

实际显示效果依赖于设备能力和通知中心UI样式。

**系统能力**：SystemCapability.Notification.Notification

名称类型只读可选说明longTextstring否否通知的长文本（不可为空字符串，大小不超过3072字节，超出部分会被截断）。briefTextstring否否通知概要内容，是对通知内容的总结（不可为空字符串，大小不超过1024字节，超出部分会被截断）。expandedTitlestring否否通知展开时的标题（不可为空字符串，大小不超过1024字节，超出部分会被截断）。

#### NotificationMultiLineContent

描述多行文本通知。继承自[NotificationBasicContent](#ZH-CN_TOPIC_0000002497606116__notificationbasiccontent)。

-

当该类型通知与其他通知形成组通知时，该通知显示默认与[普通文本](#ZH-CN_TOPIC_0000002497606116__notificationbasiccontent)相同。展开组通知后，标题显示为展开时的标题longTitle，多行文本内容lines多行显示。

当该类型通知单独呈现时，该通知标题显示为展开时的标题longTitle，多行文本内容lines多行显示。

-

实际显示效果依赖于设备能力和通知中心UI样式。

**系统能力**：SystemCapability.Notification.Notification

名称类型只读可选说明briefTextstring否否通知概要内容，是对通知内容的总结（不可为空字符串，大小不超过1024字节，超出部分会被截断）。longTitlestring否否通知展开时的标题（不可为空字符串，大小不超过1024字节，超出部分会被截断）。linesArray<string>否否通知的多行文本（最多支持三行，每行大小不超过1024字节，超出部分会被截断）。

#### NotificationPictureContent

描述附有图片的通知。继承自[NotificationBasicContent](#ZH-CN_TOPIC_0000002497606116__notificationbasiccontent)。

实际显示效果依赖于设备能力和通知中心UI样式。

**系统能力**：SystemCapability.Notification.Notification

名称类型只读可选说明briefTextstring否否通知概要内容，是对通知内容的总结（不可为空字符串，大小不超过1024字节，超出部分会被截断）。expandedTitlestring否否通知展开时的标题（不可为空字符串，大小不超过1024字节，超出部分会被截断）。picture[image.PixelMap](Interface (PixelMap).md)否否通知的图片内容(图像像素的总字节数不能超过2MB)。

#### NotificationSystemLiveViewContent

描述系统实况窗通知内容。不支持三方应用直接创建该类型通知，可以由系统代理创建系统实况窗类型通知后，三方应用发布同ID的通知来更新指定内容。继承自[NotificationBasicContent](#ZH-CN_TOPIC_0000002497606116__notificationbasiccontent)。

**系统能力**：SystemCapability.Notification.Notification

名称类型只读可选说明typeCode11+number否否类型标识符，标记调用方业务类型。capsule11+[NotificationCapsule](#ZH-CN_TOPIC_0000002497606116__notificationcapsule11)否是实况通知的胶囊。button11+[NotificationButton](#ZH-CN_TOPIC_0000002497606116__notificationbutton11)否是实况通知的按钮。time11+[NotificationTime](#ZH-CN_TOPIC_0000002497606116__notificationtime11)否是实况通知的时间。progress11+[NotificationProgress](#ZH-CN_TOPIC_0000002497606116__notificationprogress11)否是实况内容的进度。

#### NotificationCapsule11+

描述通知胶囊。

**系统能力**：SystemCapability.Notification.Notification

名称类型只读可选说明titlestring否是胶囊标题。大小不超过200字节，超出部分会被截断。icon[image.PixelMap](Interface (PixelMap).md)否是胶囊图片。backgroundColorstring否是背景颜色。

#### NotificationButton11+

描述通知按钮。

**系统能力**：SystemCapability.Notification.Notification

名称类型只读可选说明namesArray<string>否是按钮名称（最多支持3个）。iconsArray<[image.PixelMap](Interface (PixelMap).md)>否是按钮图片（最多支持3个）。iconsResource12+Array<[Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)>否是按钮资源（最多支持3个）。

#### NotificationTime11+

描述通知计时信息。

**系统能力**：SystemCapability.Notification.Notification

名称类型只读可选说明initialTimenumber否是计时起始时间。单位：ms。isCountDownboolean否是

是否倒计时。默认为false。

 - true：是。

 - false：否。

isPausedboolean否是

是否暂停。默认为false。

 - true：是。

 - false：否。

isInTitleboolean否是

时间是否展示在title中。默认为false。

 - true：是。

 - false：否。

**示例：**

```ets
// 该通知从3秒开始倒计时，并且时间展示在title中。
time: {
    initialTime: 3000,
    isCountDown: true,
    isPaused: false,
    isInTitle: true,
}
```

#### NotificationProgress11+

描述通知进度。

**系统能力**：SystemCapability.Notification.Notification

名称类型只读可选说明maxValuenumber否是进度最大值。currentValuenumber否是进度当前值。isPercentageboolean否是

是否按百分比展示。默认为false。

 - true：是。

 - false：否。