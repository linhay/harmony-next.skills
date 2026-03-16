# Interfaces (其他)

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### TargetInfo18+

指定组件绑定的目标节点。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

名称类型只读可选说明idstring | number否否

指定popup或menu绑定的目标节点。

**说明：**

1. 当id是number时，对应组件实例的UniqueID，此id由系统保证唯一性。

2. 当id是string时，对应[通用属性id](../../topics/misc/组件标识.md#ZH-CN_TOPIC_0000002497604824__id)所指定的组件，此id的唯一性需由开发者确保，但实际可能会有多个。

componentIdnumber否是目标节点所在的自定义组件的UniqueID。当上述id指定为string类型时，可通过此属性圈定范围。方便开发者在一定范围内保证id: string的唯一性。

#### PageInfo12+

Router和NavDestination等页面信息，若无对应的Router或NavDestination页面信息，则对应属性为undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明routerPageInfoobserver.[RouterPageInfo](../../modules/ohos/@ohos.arkui.observer (无感监听).md#ZH-CN_TOPIC_0000002529444737__routerpageinfo)否是Router信息。navDestinationInfoobserver.[NavDestinationInfo](../../modules/ohos/@ohos.arkui.observer (无感监听).md#ZH-CN_TOPIC_0000002529444737__navdestinationinfo)否是NavDestination信息。

#### OverlayManagerOptions15+

初始化[OverlayManager](../classes/Class (OverlayManager).md)时所用参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明renderRootOverlayboolean否是

是否渲染overlay根节点，true表示渲染overlay根节点，false表示不渲染overlay根节点，默认值为true。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

enableBackPressedEvent19+boolean否是

是否支持通过侧滑手势关闭OverlayManager下的ComponentContent，true表示可以通过侧滑关闭，false表示不可以通过侧滑关闭，默认值为false。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

#### GestureTriggerInfo20+

特定手势回调函数触发时的信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明event[GestureEvent](../../topics/misc/手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)否否手势事件对象。current[GestureRecognizer](../../topics/misc/手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gesturerecognizer12)否否手势识别器对象。可从中获取手势的详细信息，但请勿在本地保留此对象，因为当节点释放后该对象可能失效。currentPhase[GestureActionPhase](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497604786__gestureactionphase20)否否手势动作回调阶段。node[FrameNode](../../topics/components/FrameNode.md)否是触发手势的节点。默认值为null，表示没有触发手势的节点。

#### GestureObserverConfigs20+

该参数用于指定需要监听的手势回调阶段（传入空数组将无效），仅当手势触发指定阶段时才会发送通知。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明actionPhasesArray<[GestureActionPhase](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497604786__gestureactionphase20)>否否手势事件对象。

#### SwiperContentInfo23+

Swiper组件的内容区信息。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明idstring否否Swiper组件的id。uniqueIdnumber否否Swiper组件的唯一标识符。swiperItemInfosArray<[SwiperItemInfo](#ZH-CN_TOPIC_0000002529444751__swiperiteminfo23)>否否当前处于显示状态的Swiper子组件的信息。

#### SwiperItemInfo23+

Swiper子组件的信息。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明uniqueIdnumber否否Swiper子组件的唯一标识符。indexnumber否否Swiper子组件在Swiper中的索引。