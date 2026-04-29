# CommonEventPublishData

包含公共事件内容和属性。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

如果不加限制，任何应用都可以订阅公共事件并读取相关信息，应避免在公共事件中携带敏感信息。通过本模块的subscriberPermissions和bundleName参数，可以限制公共事件接收方的范围。

#### 属性

**系统能力：** SystemCapability.Notification.CommonEvent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 是 | 表示订阅者包名称，只有包名为bundleName的订阅者才能收到该公共事件。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| code | number | 否 | 是 | 表示发布方传递的公共事件数据（number类型）。默认值为0。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| data | string | 否 | 是 | 表示发布方传递的公共事件数据（string类型）。数据大小不超过64KB。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| subscriberPermissions | Array<string> | 否 | 是 | 表示订阅者的权限。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| isOrdered | boolean | 否 | 是 | 表示是否是有序事件。默认为false。 - true：有序公共事件，根据订阅者设置的优先级等级，优先将公共事件发送给优先级较高的订阅者，等待其成功接收该公共事件之后再将事件发送给优先级较低的订阅者。如果有多个订阅者具有相同的优先级，则他们将随机接收到公共事件。 - false：无序公共事件，不考虑订阅者是否接收到该事件，也不保证订阅者接收到该事件的顺序与其订阅顺序一致。 |
| isSticky | boolean | 否 | 是 | 表示是否是粘性事件。默认为false。 - true：粘性公共事件，能够让订阅者收到在订阅前已经发送的公共事件。 - false：普通公共事件，只能让订阅者收到在订阅后才发送的公共事件。 仅系统应用或系统服务允许发送粘性事件。 需要权限：ohos.permission.COMMONEVENT_STICKY |
| parameters | {[key: string]: any} | 否 | 是 | 表示发布方传递的公共事件的附加信息。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |