# CommonEventSubscribeInfo

用于表示订阅者的信息。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

订阅自定义公共事件后，任意应用都可以向订阅者发送潜在的恶意公共事件。通过本模块的publisherPermission和publisherBundleName参数，可以限制公共事件发布方的范围。

#### 属性

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| events | Array<string> | 否 | 否 | 表示要订阅的公共事件。 |
| publisherPermission | string | 否 | 是 | 表示发布者的权限，订阅方将只能接收到具有该权限的发送方发布的事件。 |
| publisherDeviceId | string | 否 | 是 | 表示设备ID。通过@ohos.deviceInfo获取udid，作为订阅者的设备ID。预留能力，暂不支持。 |
| userId | number | 否 | 是 | 表示用户ID。此参数是可选的，默认值当前用户的ID。如果指定了此参数，则该值必须是系统中现有的用户ID。通过getOsAccountLocalId获取系统账号ID，作为订阅者的用户ID。 |
| priority | number | 否 | 是 | 表示订阅者的优先级。值的范围是-100到1000，超过上下限的优先级将被设置为上下限值。 |
| publisherBundleName11+ | string | 否 | 是 | 表示要订阅的发布者的bundleName。 |