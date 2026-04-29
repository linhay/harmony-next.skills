# drag_and_drop.h

**概述**

提供NativeDrag相关接口定义。

引用文件： <arkui/drag_and_drop.h>

库： libace_ndk.z.so

系统能力： SystemCapability.ArkUI.ArkUI.Full

起始版本： 12

相关模块： [ArkUI_NativeModule](ArkUI_NativeModule.md)

相关示例： [NativeDragDrop](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeDragDrop)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_NodeEvent | ArkUI_NodeEvent | 组件事件的通用结构类型。 |
| ArkUI_Context | ArkUI_Context | native UI的上下文实例对象。 |
| ArkUI_Context* | ArkUI_ContextHandle | native UI的上下文实例对象指针定义。 |
| ArkUI_DragEvent | ArkUI_DragEvent | 拖拽事件。 |
| ArkUI_DragPreviewOption | ArkUI_DragPreviewOption | 设置拖拽跟手图的相关自定义参数。 |
| ArkUI_DragAction | ArkUI_DragAction | 拖拽行为，用于主动发起拖拽。 |
| ArkUI_DragAndDropInfo | ArkUI_DragAndDropInfo | 主动发起拖拽后，通过拖拽状态监听返回的系统拖拽相关数据。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_DragResult | ArkUI_DragResult | 拖拽结果定义，由数据接收方设置，并由系统传递给数据拖出方，拖出方可感知接收方对数据的处理结果。 |
| ArkUI_DropOperation | ArkUI_DropOperation | 定义拖拽释放时的数据处理方式，可影响角标的显示。 |
| ArkUI_PreDragStatus | ArkUI_PreDragStatus | 定义拖拽发起前的长按交互阶段的变化状态。 |
| ArkUI_DragPreviewScaleMode | ArkUI_DragPreviewScaleMode | 拖拽预览缩放模式。 |
| ArkUI_DragStatus | ArkUI_DragStatus | 拖拽状态。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| ArkUI_DragEvent* OH_ArkUI_NodeEvent_GetDragEvent(ArkUI_NodeEvent* nodeEvent) | 从 NodeEvent 中获取DragEvent。 |
| ArkUI_PreDragStatus OH_ArkUI_NodeEvent_GetPreDragStatus(ArkUI_NodeEvent* nodeEvent) | 获取预览拖拽事件状态。 |
| int32_t OH_ArkUI_DragEvent_DisableDefaultDropAnimation(ArkUI_DragEvent* event, bool disable) | 设置是否禁用松手时的系统默认动效，默认不禁用，通常在应用需要自定义落位动效时配置。 |
| int32_t OH_ArkUI_DragEvent_SetSuggestedDropOperation(ArkUI_DragEvent* event, ArkUI_DropOperation dropOperation) | 设置数据处理方式。 |
| int32_t OH_ArkUI_DragEvent_SetDragResult(ArkUI_DragEvent* event, ArkUI_DragResult result) | 设置拖拽事件的结果。 |
| int32_t OH_ArkUI_DragEvent_SetData(ArkUI_DragEvent* event, OH_UdmfData* data) | 向ArkUI_DragEvent中设置拖拽数据。 |
| ArkUI_ErrorCode OH_ArkUI_DragEvent_SetDataLoadParams(ArkUI_DragEvent* event, OH_UdmfDataLoadParams* dataLoadParams) | 调用此方法向系统提供数据加载参数，而非直接传入完整的数据对象。当用户将数据拖拽至目标应用程序并释放时，系统将使用dataLoadParams请求数据。这可以显著提高拖拽大量数据及目标应用程序处理释放数据的效率。此方法应始终优先于OH_ArkUI_DragEvent_SetData使用。请参考udmf.h中的OH_UdmfDataLoadParams_Create了解如何创建和准备数据加载参数。该方法与OH_ArkUI_DragEvent_SetData存在冲突，系统始终以最后调用的方法为准。 |
| int32_t OH_ArkUI_DragEvent_GetUdmfData(ArkUI_DragEvent* event, OH_UdmfData *data) | 从ArkUI_DragEvent中获取拖拽默认相关数据。 |
| int32_t OH_ArkUI_DragEvent_GetDataTypeCount(ArkUI_DragEvent* event, int32_t* count) | 从ArkUI_DragEvent中获取所拖拽的数据类型种类个数。 |
| int32_t OH_ArkUI_DragEvent_GetDataTypes(ArkUI_DragEvent *event, char *eventTypeArray[], int32_t length, int32_t maxStrLen) | 从ArkUI_DragEvent中获取拖拽数据的类型列表。 |
| int32_t OH_ArkUI_DragEvent_GetDragResult(ArkUI_DragEvent* event, ArkUI_DragResult* result) | 从ArkUI_DragEvent中获取拖拽结果。 |
| int32_t OH_ArkUI_DragEvent_GetDropOperation(ArkUI_DragEvent* event, ArkUI_DropOperation* operation) | 从ArkUI_DragEvent中获取数据处理方式。 |
| float OH_ArkUI_DragEvent_GetPreviewTouchPointX(ArkUI_DragEvent* event) | 从ArkUI_DragEvent中获取预览图跟手点的x轴坐标。 |
| float OH_ArkUI_DragEvent_GetPreviewTouchPointY(ArkUI_DragEvent* event) | 从ArkUI_DragEvent中获取预览图跟手点的y轴坐标。 |
| float OH_ArkUI_DragEvent_GetPreviewRectWidth(ArkUI_DragEvent* event) | 从ArkUI_DragEvent中获取预览图的宽。 |
| float OH_ArkUI_DragEvent_GetPreviewRectHeight(ArkUI_DragEvent* event) | 从ArkUI_DragEvent中获取预览图的高。 |
| float OH_ArkUI_DragEvent_GetTouchPointXToWindow(ArkUI_DragEvent* event) | 从ArkUI_DragEvent中获取跟手点相对于window的x轴坐标。 |
| float OH_ArkUI_DragEvent_GetTouchPointYToWindow(ArkUI_DragEvent* event) | 从ArkUI_DragEvent中获取跟手点相对于window的y轴坐标。 |
| float OH_ArkUI_DragEvent_GetTouchPointXToDisplay(ArkUI_DragEvent* event) | 从ArkUI_DragEvent中获取跟手点相对于当前Display的x轴坐标。 |
| float OH_ArkUI_DragEvent_GetTouchPointYToDisplay(ArkUI_DragEvent* event) | 从ArkUI_DragEvent中获取跟手点相对于当前Display的y轴坐标。 |
| float OH_ArkUI_DragEvent_GetVelocityX(ArkUI_DragEvent* event) | 获取当前拖拽的x轴方向拖动速度。 |
| float OH_ArkUI_DragEvent_GetVelocityY(ArkUI_DragEvent* event) | 获取当前拖拽的y轴方向拖动速度。 |
| float OH_ArkUI_DragEvent_GetVelocity(ArkUI_DragEvent* event) | 获取当前拖拽的主方向拖动速度。 |
| int32_t OH_ArkUI_DragEvent_GetModifierKeyStates(ArkUI_DragEvent* event, uint64_t* keys) | 获取功能键按压状态。 |
| int32_t OH_ArkUI_DragEvent_StartDataLoading(ArkUI_DragEvent* event, OH_UdmfGetDataParams* options, char* key, unsigned int keyLen) | 使用指定的同步参数开始数据同步。 |
| int32_t OH_ArkUI_CancelDataLoading(ArkUI_ContextHandle uiContext, const char* key) | 取消正在进行的数据同步。 |
| int32_t OH_ArkUI_DisableDropDataPrefetchOnNode(ArkUI_NodeHandle node, bool disabled) | 设置是否在执行onDrop回调之前禁用数据预获取过程。系统将重试获取数据，直到达到最大时间限制（目前为2.4秒），这对跨设备的拖动操作非常有用，因为它有助于系统稳定通信。然而，对于OH_ArkUI_DragEvent_StartDataLoading方法而言，这一特性显得多余。该方法采用异步机制获取数据，因此在onDrop中使用OH_ArkUI_DragEvent_StartDataLoading时，为了避免在onDrop执行前意外获取数据，必须将此字段设置为true。 |
| int32_t OH_ArkUI_SetDragEventStrictReportWithNode(ArkUI_NodeHandle node, bool enabled) | 控制是否使能严格dragEvent上报，建议开启；默认是不开启的；当不开启时，从父组件拖移进子组件时，父组件并不会收到leave的通知；而开启之后，只要前后两个组件发生变化，上一个组件就会收到leave，新的组件收到enter通知；该配置与具体的UI实例相关，需要通过传入一个当前UI实例上的一个具体的组件节点来关联。 |
| int32_t OH_ArkUI_SetDragEventStrictReportWithContext(ArkUI_ContextHandle uiContext, bool enabled) | 控制是否使能严格dragEvent上报，建议开启；默认是不开启的;当不开启时，从父组件拖移进子组件时，父组件并不会收到leave的通知；而开启之后，只要前后两个组件发生变化，上一个组件就会收到leave，新的组件收到enter通知；该配置与具体的UI实例相关，可通过传入一个UI实例进行关联。 |
| int32_t OH_ArkUI_SetNodeAllowedDropDataTypes(ArkUI_NodeHandle node, const char* typesArray[], int32_t count) | 配置组件允许接受落入的数据类型，该接口会重置通过 OH_ArkUI_DisallowNodeAnyDropDataTypes 或OH_ArkUI_AllowNodeAllDropDataTypes进行的配置。 |
| int32_t OH_ArkUI_DisallowNodeAnyDropDataTypes(ArkUI_NodeHandle node) | 配置组件不允许接受任何数据类型，该接口会重置通过OH_ArkUI_SetNodeAllowedDropDataTypes配置的数据类型。 |
| int32_t OH_ArkUI_AllowNodeAllDropDataTypes(ArkUI_NodeHandle node) | 配置组件允许接受任意数据类型，该接口会重置通过OH_ArkUI_SetNodeAllowedDropDataTypes配置的数据类型。 |
| int32_t OH_ArkUI_SetNodeDraggable(ArkUI_NodeHandle node, bool enabled) | 设置该组件是否允许进行拖拽。 |
| int32_t OH_ArkUI_SetNodeDragPreview(ArkUI_NodeHandle node, OH_PixelmapNative* preview) | 设置组件在被拖拽时的自定义跟手图。 |
| ArkUI_DragPreviewOption* OH_ArkUI_CreateDragPreviewOption(void) | 构建一个ArkUI_DragPreviewOption对象。 |
| void OH_ArkUI_DragPreviewOption_Dispose(ArkUI_DragPreviewOption* option) | 销毁跟手图自定义参数对象实例。 |
| int32_t OH_ArkUI_DragPreviewOption_SetScaleMode(ArkUI_DragPreviewOption* option, ArkUI_DragPreviewScaleMode scaleMode) | 设置拖拽跟手图是否根据系统定义自动进行缩放。 |
| int32_t OH_ArkUI_DragPreviewOption_SetDefaultShadowEnabled(ArkUI_DragPreviewOption* option, bool enabled) | 设置跟手图背板默认的投影效果，默认不开启。 |
| int32_t OH_ArkUI_DragPreviewOption_SetDefaultRadiusEnabled(ArkUI_DragPreviewOption* option, bool enabled) | 设置跟手图背板默认的圆角效果，默认不开启。 |
| int32_t OH_ArkUI_DragPreviewOption_SetNumberBadgeEnabled(ArkUI_DragPreviewOption* option, bool enabled) | 设置跟手图背板是否显示角标,开启后,系统会根据拖拽数量自动进行角标显示。 |
| int32_t OH_ArkUI_DragPreviewOption_SetBadgeNumber(ArkUI_DragPreviewOption* option, uint32_t forcedNumber) | 强制显示角标的数量,覆盖SetDragPreviewNumberBadgeEnabled设置的值。 |
| int32_t OH_ArkUI_DragPreviewOption_SetDefaultAnimationBeforeLiftingEnabled(ArkUI_DragPreviewOption* option, bool enabled) | 配置是否开启点按时的默认动画。 |
| int32_t OH_ArkUI_SetNodeDragPreviewOption(ArkUI_NodeHandle node, ArkUI_DragPreviewOption* option) | 将构造的ArkUI_DragPreviewOption设置给组件。 |
| ArkUI_DragAction* OH_ArkUI_CreateDragActionWithNode(ArkUI_NodeHandle node) | 创建一个拖拽操作对象，该对象需与一个UI实例相关联，可通过传入一个当前UI实例的某个组件节点来指定。 |
| ArkUI_DragAction* OH_ArkUI_CreateDragActionWithContext(ArkUI_ContextHandle uiContext) | 创建一个拖拽操作对象，该对象需与一个UI实例相关联，可通过传入一个UI实例指针来关联。 |
| void OH_ArkUI_DragAction_Dispose(ArkUI_DragAction* dragAction) | 销毁创建的 ArkUI_DragAction 对象。 |
| int32_t OH_ArkUI_DragAction_SetPointerId(ArkUI_DragAction* dragAction, int32_t pointer) | 设置手指ID，当屏幕上仅有一只手指在操作时，pointer ID 为 0；一般情况下，配置 0 即可。 |
| int32_t OH_ArkUI_DragAction_SetPixelMaps(ArkUI_DragAction* dragAction, OH_PixelmapNative* pixelmapArray[], int32_t size) | 设置拖拽跟手图，只能使用 pixelmap 格式对象。 |
| int32_t OH_ArkUI_DragAction_SetTouchPointX(ArkUI_DragAction* dragAction, float x) | 设置跟手点，相对于设置的第一个pixelmap的左上角。 |
| int32_t OH_ArkUI_DragAction_SetTouchPointY(ArkUI_DragAction* dragAction, float y) | 设置跟手点,相对于设置的第一个pixelmap的左上角。 |
| int32_t OH_ArkUI_DragAction_SetData(ArkUI_DragAction* dragAction, OH_UdmfData* data) | 设置拖拽数据。 |
| ArkUI_ErrorCode OH_ArkUI_DragAction_SetDataLoadParams(ArkUI_DragAction* dragAction,OH_UdmfDataLoadParams* dataLoadParams) | 使用此方法为系统提供一个数据加载参数，而不是直接提供一个完整的数据对象。当用户拖拽到目标应用程序并落入时，系统将使用dataLoadParams请求数据。可以极大地提高拖拽大量数据的效率，以及目标应用程序中处理落入数据的效率。此方法应始终优先于OH_ArkUI_DragAction_SetData使用。请参考udmf.h中的OH_UdmfDataLoadParams_Create了解如何创建和准备数据加载参数。该方法与OH_ArkUI_DragAction_SetData存在冲突，系统始终以最后调用的方法为准。 |
| int32_t OH_ArkUI_DragAction_SetDragPreviewOption(ArkUI_DragAction* dragAction, ArkUI_DragPreviewOption* option) | 将构造的ArkUI_DragPreviewOption设置给ArkUI_DragAction。 |
| int32_t OH_ArkUI_DragAction_RegisterStatusListener(ArkUI_DragAction* dragAction, void* userData,void(*listener)(ArkUI_DragAndDropInfo* dragAndDropInfo, void* userData)) | 注册拖拽状态监听回调，该回调可感知到拖拽已经发起或用户松手结束的状态，可通过该监听获取到落入方对数据的接收处理是否成功。 |
| ArkUI_ErrorCode OH_ArkUI_DragEvent_GetDisplayId(ArkUI_DragEvent event, int32_t* displayId) | 获取当前拖拽事件发生时所在的屏幕ID，不支持当eventType为NODE_ON_DRAG_END时获取。 |
| void OH_ArkUI_DragAction_UnregisterStatusListener(ArkUI_DragAction* dragAction) | 解注册拖拽状态监听回调。 |
| ArkUI_DragStatus OH_ArkUI_DragAndDropInfo_GetDragStatus(ArkUI_DragAndDropInfo* dragAndDropInfo) | 获取dragAction发起拖拽的状态，获取异常时返回 ArkUI_DRAG_STATUS_UNKNOWN。 |
| ArkUI_DragEvent* OH_ArkUI_DragAndDropInfo_GetDragEvent(ArkUI_DragAndDropInfo* dragAndDropInfo) | 通过dragAndDropInfo获取到DragEvent，可通过DragEvent获取释放结果等。 |
| int32_t OH_ArkUI_StartDrag(ArkUI_DragAction* dragAction) | 通过构造的DragAction对象发起拖拽。 |
| int32_t OH_ArkUI_DragEvent_RequestDragEndPending(ArkUI_DragEvent* event, int32_t* requestIdentify) | 请求延迟处理拖拽结束事件，等待应用程序确认操作结果。应用程序需通过 OH_ArkUI_NotifyDragResult接口将最终结果回传至系统，并在所有处理完成后调用 OH_ArkUI_NotifyDragEndPendingDone。最大等待时间为2秒。 |
| int32_t OH_ArkUI_NotifyDragResult(int32_t requestIdentify, ArkUI_DragResult result) | 通知系统最终拖拽结果。系统会校验请求标识符是否与OH_ArkUI_DragEvent_RequestDragEndPending返回的一致，不一致则忽略本次调用。 |
| int32_t OH_ArkUI_NotifyDragEndPendingDone(int32_t requestIdentify) | 通知系统所有异步处理已完成，可结束拖拽结束挂起状态。 |
| ArkUI_ErrorCode OH_ArkUI_EnableDropDisallowedBadge(ArkUI_ContextHandle uiContext, bool enabled) | 设置是否可以显示禁用角标。 |
| float OH_ArkUI_DragEvent_GetTouchPointXToGlobalDisplay(ArkUI_DragEvent* event) | 从ArkUI_DragEvent中获取跟手点相对于全局屏幕的x轴坐标。 |
| float OH_ArkUI_DragEvent_GetTouchPointYToGlobalDisplay(ArkUI_DragEvent* event) | 从ArkUI_DragEvent中获取跟手点相对于全局屏幕的y轴坐标。 |
| ArkUI_ErrorCode OH_ArkUI_DragEvent_GetDragSource(ArkUI_DragEvent* event, char *bundleName, int32_t length) | 获取拖拽发起方的应用包名信息，需要传递一个字符数组来接收包名字符串，并显式指明数组长度，该数组长度不小于128个字符。 |
| ArkUI_ErrorCode OH_ArkUI_DragEvent_IsRemote(ArkUI_DragEvent* event, bool* isRemote) | 判断当前的拖拽操作是否是跨设备拖拽。 |

**枚举类型说明**

**ArkUI_DragResult**

```ets
enum ArkUI_DragResult
```

描述：

拖拽结果定义，由数据接收方设置，并由系统传递给数据拖出方，拖出方可感知接收方对数据的处理结果。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_DRAG_RESULT_SUCCESSFUL = 0 | 拖拽处理成功。 |
| ARKUI_DRAG_RESULT_FAILED = 1 | 拖拽处理失败。 |
| ARKUI_DRAG_RESULT_CANCELED = 2 | 拖拽处理取消。 |

**ArkUI_DropOperation**

```ets
enum ArkUI_DropOperation
```

描述：

定义拖拽释放时的数据处理方式，可影响角标的显示。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_DROP_OPERATION_COPY = 0 | 复制行为。 |
| ARKUI_DROP_OPERATION_MOVE = 1 | 剪切行为。 |

**ArkUI_PreDragStatus**

```ets
enum ArkUI_PreDragStatus
```

描述：

定义拖拽发起前的长按交互阶段的变化状态。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_PRE_DRAG_STATUS_UNKNOWN = -1 | Unknown。 |
| ARKUI_PRE_DRAG_STATUS_ACTION_DETECTING = 0 | 拖拽手势启动阶段。 |
| ARKUI_PRE_DRAG_STATUS_READY_TO_TRIGGER_DRAG = 1 | 拖拽准备完成，可发起拖拽阶段。 |
| ARKUI_PRE_DRAG_STATUS_PREVIEW_LIFT_STARTED = 2 | 拖拽浮起动效发起阶段。 |
| ARKUI_PRE_DRAG_STATUS_PREVIEW_LIFT_FINISHED = 3 | 拖拽浮起动效结束阶段。 |
| ARKUI_PRE_DRAG_STATUS_PREVIEW_LANDING_STARTED = 4 | 拖拽落回动效发起阶段。 |
| ARKUI_PRE_DRAG_STATUS_PREVIEW_LANDING_FINISHED = 5 | 拖拽落回动效结束阶段。 |
| ARKUI_PRE_DRAG_STATUS_CANCELED_BEFORE_DRAG = 6 | 拖拽浮起落位动效中断。 |

**ArkUI_DragPreviewScaleMode**

```ets
enum ArkUI_DragPreviewScaleMode
```

描述：

拖拽预览缩放模式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_DRAG_PREVIEW_SCALE_AUTO = 0 | 系统根据拖拽场景自动改变跟手点位置，根据规则自动对拖拽背板图进行缩放变换等。 |
| ARKUI_DRAG_PREVIEW_SCALE_DISABLED = 1 | 禁用系统对拖拽背板图的缩放行为。 |

**ArkUI_DragStatus**

```ets
enum ArkUI_DragStatus
```

描述：

拖拽状态。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_DRAG_STATUS_UNKNOWN = -1 | 未知的拖拽状态。 |
| ARKUI_DRAG_STATUS_STARTED = 0 | 拖拽开始。 |
| ARKUI_DRAG_STATUS_ENDED = 1 | 拖拽结束。 |

**函数说明**

**OH_ArkUI_NodeEvent_GetDragEvent()**

```ets
ArkUI_DragEvent* OH_ArkUI_NodeEvent_GetDragEvent(ArkUI_NodeEvent* nodeEvent)
```

描述：

从 NodeEvent 中获取DragEvent。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeEvent* nodeEvent | ArkUI_NodeEvent事件指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_DragEvent* | ArkUI_DragEvent 事件指针，当传入的 NodeEvent 无效或不是拖拽相关的事件时，则返回空。 |

**OH_ArkUI_NodeEvent_GetPreDragStatus()**

```ets
ArkUI_PreDragStatus OH_ArkUI_NodeEvent_GetPreDragStatus(ArkUI_NodeEvent* nodeEvent)
```

描述：

获取预览拖拽事件状态。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeEvent* nodeEvent | ArkUI_NodeEvent节点对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_PreDragStatus | ArkUI_PreDragStatus 拖拽发起前交互状态。 |

**OH_ArkUI_DragEvent_DisableDefaultDropAnimation()**

```ets
int32_t OH_ArkUI_DragEvent_DisableDefaultDropAnimation(ArkUI_DragEvent* event, bool disable)
```

描述：

设置是否禁用松手时的系统默认动效，默认不禁用，通常在应用需要自定义落位动效时配置。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |
| bool disable | 是否禁用松手时的系统默认动效，true禁用，false不禁用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragEvent_SetSuggestedDropOperation()**

```ets
int32_t OH_ArkUI_DragEvent_SetSuggestedDropOperation(ArkUI_DragEvent* event, ArkUI_DropOperation dropOperation)
```

描述：

设置数据处理方式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |
| ArkUI_DropOperation dropOperation | 角标显示状态的类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragEvent_SetDragResult()**

```ets
int32_t OH_ArkUI_DragEvent_SetDragResult(ArkUI_DragEvent* event, ArkUI_DragResult result)
```

描述：

设置拖拽事件的结果。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |
| ArkUI_DragResult result | 拖拽数据处理结果。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragEvent_SetData()**

```ets
int32_t OH_ArkUI_DragEvent_SetData(ArkUI_DragEvent* event, OH_UdmfData* data)
```

描述：

向ArkUI_DragEvent中设置拖拽数据。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |
| OH_UdmfData* data | 拖拽数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragEvent_SetDataLoadParams()**

```ets
ArkUI_ErrorCode OH_ArkUI_DragEvent_SetDataLoadParams(ArkUI_DragEvent* event, OH_UdmfDataLoadParams* dataLoadParams)
```

描述：

使用此方法为系统提供一个数据加载参数，而不是直接提供一个完整的数据对象。当用户拖拽到目标应用程序并落入时，系统将使用dataLoadParams请求数据。可以极大地提高拖拽大量数据的效率，以及目标应用程序中处理落入数据的效率。此方法应始终优先于[OH_ArkUI_DragEvent_SetData](drag_and_drop.h.md#ZH-CN_TOPIC_0000002522241024__oh_arkui_dragevent_setdata)使用。请参考udmf.h中的[OH_UdmfDataLoadParams_Create](udmf.h.md#ZH-CN_TOPIC_0000002522240654__oh_udmfdataloadparams_create)了解如何创建和准备数据加载参数。该方法与[OH_ArkUI_DragEvent_SetData](drag_and_drop.h.md#ZH-CN_TOPIC_0000002522241024__oh_arkui_dragevent_setdata)存在冲突，系统始终以最后调用的方法为准。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |
| OH_UdmfDataLoadParams* dataLoadParams | 落入操作时使用的数据加载参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragEvent_GetUdmfData()**

```ets
int32_t OH_ArkUI_DragEvent_GetUdmfData(ArkUI_DragEvent* event, OH_UdmfData *data)
```

描述：

从ArkUI_DragEvent中获取拖拽默认相关数据。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |
| OH_UdmfData *data | OH_UdmfData 拖拽的数据指针，应用在接收时需通过 OH_UdmfData_Create 方法创建一个用于接收数据的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragEvent_GetDataTypeCount()**

```ets
int32_t OH_ArkUI_DragEvent_GetDataTypeCount(ArkUI_DragEvent* event, int32_t* count)
```

描述：

从ArkUI_DragEvent中获取所拖拽的数据类型种类个数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |
| int32_t* count | 出参，返回所拖拽数据的类型的数量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragEvent_GetDataTypes()**

```ets
int32_t OH_ArkUI_DragEvent_GetDataTypes(ArkUI_DragEvent *event, char *eventTypeArray[], int32_t length, int32_t maxStrLen)
```

描述：

从ArkUI_DragEvent中获取拖拽数据的类型列表。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent *event | ArkUI_DragEvent事件指针。 |
| char *eventTypeArray[] | 返回拖拽数据的类型列表，需要先自行创建字符串数组。 |
| int32_t length | 数组总长度，不应少于使用OH_ArkUI_DragEvent_GetDataTypesCount获取到的数量。 |
| int32_t maxStrLen | 拖拽数据类型的最大字符串长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。  ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR 缓冲区大小不足。 |

**OH_ArkUI_DragEvent_GetDragResult()**

```ets
int32_t OH_ArkUI_DragEvent_GetDragResult(ArkUI_DragEvent* event, ArkUI_DragResult* result)
```

描述：

从ArkUI_DragEvent中获取拖拽结果。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |
| ArkUI_DragResult* result | 出参，返回拖拽事件对应的拖拽结果。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragEvent_GetDropOperation()**

```ets
int32_t OH_ArkUI_DragEvent_GetDropOperation(ArkUI_DragEvent* event, ArkUI_DropOperation* operation)
```

描述：

从ArkUI_DragEvent中获取数据处理方式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |
| ArkUI_DropOperation* operation | 数据的处理方式. |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。  可能原因: 1. 参数为空或event非有效的DragEvent. |

**OH_ArkUI_DragEvent_GetPreviewTouchPointX()**

```ets
float OH_ArkUI_DragEvent_GetPreviewTouchPointX(ArkUI_DragEvent* event)
```

描述：

从ArkUI_DragEvent中获取预览图跟手点的x轴坐标。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | float 返回拖拽跟手点的x轴坐标，单位为px，传入参数无效时返回默认值0。 |

**OH_ArkUI_DragEvent_GetPreviewTouchPointY()**

```ets
float OH_ArkUI_DragEvent_GetPreviewTouchPointY(ArkUI_DragEvent* event)
```

描述：

从ArkUI_DragEvent中获取预览图跟手点的y轴坐标。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | float 返回拖拽跟手点的y轴坐标，单位px，传入参数无效时返回默认值0。 |

**OH_ArkUI_DragEvent_GetPreviewRectWidth()**

```ets
float OH_ArkUI_DragEvent_GetPreviewRectWidth(ArkUI_DragEvent* event)
```

描述：

从ArkUI_DragEvent中获取预览图的宽。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | float 返回拖拽跟手图宽度，单位为px，传入参数无效时返回默认值0。 |

**OH_ArkUI_DragEvent_GetPreviewRectHeight()**

```ets
float OH_ArkUI_DragEvent_GetPreviewRectHeight(ArkUI_DragEvent* event)
```

描述：

从ArkUI_DragEvent中获取预览图的高。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | float 返回拖拽跟手图高度，单位为px，传入参数无效时返回默认值0。 |

**OH_ArkUI_DragEvent_GetTouchPointXToWindow()**

```ets
float OH_ArkUI_DragEvent_GetTouchPointXToWindow(ArkUI_DragEvent* event)
```

描述：

从ArkUI_DragEvent中获取跟手点相对于window的x轴坐标。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | float 返回跟手点相对于window的x轴坐标，单位为px，传入参数无效时返回默认值0。 |

**OH_ArkUI_DragEvent_GetTouchPointYToWindow()**

```ets
float OH_ArkUI_DragEvent_GetTouchPointYToWindow(ArkUI_DragEvent* event)
```

描述：

从ArkUI_DragEvent中获取跟手点相对于window的y轴坐标。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | float 返回跟手点相对于window的y轴坐标，单位为px，传入参数无效时返回默认值0。 |

**OH_ArkUI_DragEvent_GetTouchPointXToDisplay()**

```ets
float OH_ArkUI_DragEvent_GetTouchPointXToDisplay(ArkUI_DragEvent* event)
```

描述：

从ArkUI_DragEvent中获取跟手点相对于当前Display的x轴坐标。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | float 返回拖拽跟手点相对于当前Display的x轴坐标，单位为px，传入参数无效时返回默认值0。 |

**OH_ArkUI_DragEvent_GetTouchPointYToDisplay()**

```ets
float OH_ArkUI_DragEvent_GetTouchPointYToDisplay(ArkUI_DragEvent* event)
```

描述：

从ArkUI_DragEvent中获取跟手点相对于当前Display的y轴坐标。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | float 返回拖拽跟手点相对于当前Display的y轴坐标，单位为px，传入参数无效时返回默认值0。 |

**OH_ArkUI_DragEvent_GetVelocityX()**

```ets
float OH_ArkUI_DragEvent_GetVelocityX(ArkUI_DragEvent* event)
```

描述：

获取当前拖拽的x轴方向拖动速度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | float 返回当前拖拽的x轴方向移动速度，单位为px/s，传入参数无效时返回默认值0。 |

**OH_ArkUI_DragEvent_GetVelocityY()**

```ets
float OH_ArkUI_DragEvent_GetVelocityY(ArkUI_DragEvent* event)
```

描述：

获取当前拖拽的y轴方向拖动速度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | float 返回当前拖拽的y轴方向移动速度，单位为px/s，传入参数无效时返回默认值0。 |

**OH_ArkUI_DragEvent_GetVelocity()**

```ets
float OH_ArkUI_DragEvent_GetVelocity(ArkUI_DragEvent* event)
```

描述：

获取当前拖拽的主方向拖动速度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | float 返回当前拖拽移动速度，单位为px/s，传入参数无效时返回默认值0。 |

**OH_ArkUI_DragEvent_GetModifierKeyStates()**

```ets
int32_t OH_ArkUI_DragEvent_GetModifierKeyStates(ArkUI_DragEvent* event, uint64_t* keys)
```

描述：

获取功能键按压状态。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |
| uint64_t* keys | 返回当前处于按下状态的 modifier key组合，应用可通过位运算进行判断。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragEvent_StartDataLoading()**

```ets
int32_t OH_ArkUI_DragEvent_StartDataLoading(ArkUI_DragEvent* event, OH_UdmfGetDataParams* options, char* key, unsigned int keyLen)
```

描述：

使用指定的同步参数开始数据同步。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |
| OH_UdmfGetDataParams* options | OH_UdmfGetDataParams参数指针。 |
| char* key | 返回数据设置成功之后的key值，字符串长度不小于UDMF_KEY_BUFFER_LEN。 |
| unsigned int keyLen | 表示key字符串的长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_CancelDataLoading()**

```ets
int32_t OH_ArkUI_CancelDataLoading(ArkUI_ContextHandle uiContext, const char* key)
```

描述：

取消正在进行的数据同步。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ContextHandle uiContext | UI实例对象指针。 |
| const char* key | 表示数据的key值并通过 OH_ArkUI_DragEvent_StartDataLoading 返回。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DisableDropDataPrefetchOnNode()**

```ets
int32_t OH_ArkUI_DisableDropDataPrefetchOnNode(ArkUI_NodeHandle node, bool disabled)
```

描述：

设置是否在执行onDrop回调之前禁用数据预获取过程。系统将重试获取数据，直到达到最大时间限制（目前为2.4秒），这对跨设备的拖动操作非常有用，因为它有助于系统稳定通信。然而，对于[OH_ArkUI_DragEvent_StartDataLoading](drag_and_drop.h.md#ZH-CN_TOPIC_0000002522241024__oh_arkui_dragevent_startdataloading)方法而言，这一特性显得多余。该方法采用异步机制获取数据，因此在onDrop中使用[OH_ArkUI_DragEvent_StartDataLoading](drag_and_drop.h.md#ZH-CN_TOPIC_0000002522241024__oh_arkui_dragevent_startdataloading)时，为了避免在onDrop执行前意外获取数据，必须将此字段设置为true。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 组件节点指针。 |
| bool disabled | 表示是禁用数据预取过程。true表示禁止，false表示不禁止。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_SetDragEventStrictReportWithNode()**

```ets
int32_t OH_ArkUI_SetDragEventStrictReportWithNode(ArkUI_NodeHandle node, bool enabled)
```

描述：

控制是否使能严格dragEvent上报，建议开启；默认是不开启的；当不开启时，从父组件拖移进子组件时，父组件并不会收到leave的通知；而开启之后，只要前后两个组件发生变化，上一个组件就会收到leave，新的组件收到enter通知；该配置与具体的UI实例相关，需要通过传入一个当前UI实例上的一个具体的组件节点来关联。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 组件节点指针。 |
| bool enabled | 是否开启严格上报。true表示开启严格上报，false表示关闭严格上报。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_SetDragEventStrictReportWithContext()**

```ets
int32_t OH_ArkUI_SetDragEventStrictReportWithContext(ArkUI_ContextHandle uiContext, bool enabled)
```

描述：

控制是否使能严格dragEvent上报，建议开启；默认是不开启的;当不开启时，从父组件拖移进子组件时，父组件并不会收到leave的通知；而开启之后，只要前后两个组件发生变化，上一个组件就会收到leave，新的组件收到enter通知；该配置与具体的UI实例相关，可通过传入一个UI实例进行关联。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ContextHandle uiContext | UI实例指针。 |
| bool enabled | 是否开启严格上报。true表示开启严格上报，false表示关闭严格上报。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_SetNodeAllowedDropDataTypes()**

```ets
int32_t OH_ArkUI_SetNodeAllowedDropDataTypes(ArkUI_NodeHandle node, const char* typesArray[], int32_t count)
```

描述：

配置组件允许接受落入的数据类型，该接口会重置通过 [OH_ArkUI_DisallowNodeAnyDropDataTypes](drag_and_drop.h.md#ZH-CN_TOPIC_0000002522241024__oh_arkui_disallownodeanydropdatatypes) 或[OH_ArkUI_AllowNodeAllDropDataTypes](drag_and_drop.h.md#ZH-CN_TOPIC_0000002522241024__oh_arkui_allownodealldropdatatypes)进行的配置。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 组件节点指针。 |
| const char* typesArray[] | 允许落入的数据类型数组。 |
| int32_t count | 数组的长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DisallowNodeAnyDropDataTypes()**

```ets
int32_t OH_ArkUI_DisallowNodeAnyDropDataTypes(ArkUI_NodeHandle node)
```

描述：

配置组件不允许接受任何数据类型，该接口会重置通过[OH_ArkUI_SetNodeAllowedDropDataTypes](drag_and_drop.h.md#ZH-CN_TOPIC_0000002522241024__oh_arkui_setnodealloweddropdatatypes)配置的数据类型。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 组件节点指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_AllowNodeAllDropDataTypes()**

```ets
int32_t OH_ArkUI_AllowNodeAllDropDataTypes(ArkUI_NodeHandle node)
```

描述：

配置组件允许接受任意数据类型，该接口会重置通过[OH_ArkUI_SetNodeAllowedDropDataTypes](drag_and_drop.h.md#ZH-CN_TOPIC_0000002522241024__oh_arkui_setnodealloweddropdatatypes)配置的数据类型。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 组件节点指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_SetNodeDraggable()**

```ets
int32_t OH_ArkUI_SetNodeDraggable(ArkUI_NodeHandle node, bool enabled)
```

描述：

设置该组件是否允许进行拖拽。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 组件节点指针。 |
| bool enabled | 是否支持拖出。true表示支持拖出，false表示不支持拖出。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_SetNodeDragPreview()**

```ets
int32_t OH_ArkUI_SetNodeDragPreview(ArkUI_NodeHandle node, OH_PixelmapNative* preview)
```

描述：

设置组件在被拖拽时的自定义跟手图。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 目标组件节点指针。 |
| OH_PixelmapNative* preview | 自定义跟手图，使用 pixelmap 格式。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_CreateDragPreviewOption()**

```ets
ArkUI_DragPreviewOption* OH_ArkUI_CreateDragPreviewOption(void)
```

描述：

构建一个ArkUI_DragPreviewOption对象。

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_DragPreviewOption* | ArkUI_DragPreviewOption对象。 |

**OH_ArkUI_DragPreviewOption_Dispose()**

```ets
void OH_ArkUI_DragPreviewOption_Dispose(ArkUI_DragPreviewOption* option)
```

描述：

销毁跟手图自定义参数对象实例。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragPreviewOption* option | 自定义参数。 |

**OH_ArkUI_DragPreviewOption_SetScaleMode()**

```ets
int32_t OH_ArkUI_DragPreviewOption_SetScaleMode(ArkUI_DragPreviewOption* option, ArkUI_DragPreviewScaleMode scaleMode)
```

描述：

设置拖拽跟手图是否根据系统定义自动进行缩放。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragPreviewOption* option | 自定义参数。 |
| ArkUI_DragPreviewScaleMode scaleMode | 设置组件拖拽过程中的跟手图缩放模式。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragPreviewOption_SetDefaultShadowEnabled()**

```ets
int32_t OH_ArkUI_DragPreviewOption_SetDefaultShadowEnabled(ArkUI_DragPreviewOption* option, bool enabled)
```

描述：

设置跟手图背板默认的投影效果，默认不开启。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragPreviewOption* option | 自定义参数。 |
| bool enabled | 是否使用默认投影效果。true表示使用默认投影效果，false表示不使用默认投影效果。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragPreviewOption_SetDefaultRadiusEnabled()**

```ets
int32_t OH_ArkUI_DragPreviewOption_SetDefaultRadiusEnabled(ArkUI_DragPreviewOption* option, bool enabled)
```

描述：

设置跟手图背板默认的圆角效果，默认不开启。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragPreviewOption* option | 自定义参数。 |
| bool enabled | 是否开启圆角效果显示。true表示开启圆角效果显示，false表示不开启圆角效果显示。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragPreviewOption_SetNumberBadgeEnabled()**

```ets
int32_t OH_ArkUI_DragPreviewOption_SetNumberBadgeEnabled(ArkUI_DragPreviewOption* option, bool enabled)
```

描述：

设置跟手图背板是否显示角标,开启后,系统会根据拖拽数量自动进行角标显示。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragPreviewOption* option | 自定义参数。 |
| bool enabled | 是否开启角标显示。true表示开启角标显示，false表示不开启角标显示。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragPreviewOption_SetBadgeNumber()**

```ets
int32_t OH_ArkUI_DragPreviewOption_SetBadgeNumber(ArkUI_DragPreviewOption* option, uint32_t forcedNumber)
```

描述：

强制显示角标的数量,覆盖SetDragPreviewNumberBadgeEnabled设置的值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragPreviewOption* option | 自定义参数。 |
| uint32_t forcedNumber | 角标的数量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragPreviewOption_SetDefaultAnimationBeforeLiftingEnabled()**

```ets
int32_t OH_ArkUI_DragPreviewOption_SetDefaultAnimationBeforeLiftingEnabled(ArkUI_DragPreviewOption* option, bool enabled)
```

描述：

配置是否开启点按时的默认动画。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragPreviewOption* option | 自定义参数。 |
| bool enabled | 是否开启默认点按效果。true表示开启默认点按效果，false表示不开启默认点按效果。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_SetNodeDragPreviewOption()**

```ets
int32_t OH_ArkUI_SetNodeDragPreviewOption(ArkUI_NodeHandle node, ArkUI_DragPreviewOption* option)
```

描述：

将构造的ArkUI_DragPreviewOption设置给组件。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 组件节点指针。 |
| ArkUI_DragPreviewOption* option | 自定义参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_CreateDragActionWithNode()**

```ets
ArkUI_DragAction* OH_ArkUI_CreateDragActionWithNode(ArkUI_NodeHandle node)
```

描述：

创建一个拖拽操作对象，该对象需与一个UI实例相关联，可通过传入一个当前UI实例的某个组件节点来指定。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 组件节点指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_DragAction* | ArkUI_DragAction对象指针，如果创建失败，则返回空。 |

**OH_ArkUI_CreateDragActionWithContext()**

```ets
ArkUI_DragAction* OH_ArkUI_CreateDragActionWithContext(ArkUI_ContextHandle uiContext)
```

描述：

创建一个拖拽操作对象，该对象需与一个UI实例相关联，可通过传入一个UI实例指针来关联。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ContextHandle uiContext | UI实例对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_DragAction* | ArkUI_DragAction对象，如果创建失败，则返回空。 |

**OH_ArkUI_DragAction_Dispose()**

```ets
void OH_ArkUI_DragAction_Dispose(ArkUI_DragAction* dragAction)
```

描述：

销毁创建的 ArkUI_DragAction 对象。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragAction* dragAction | 拖拽行为对象。 |

**OH_ArkUI_DragAction_SetPointerId()**

```ets
int32_t OH_ArkUI_DragAction_SetPointerId(ArkUI_DragAction* dragAction, int32_t pointer)
```

描述：

设置手指ID，当屏幕上仅有一只手指在操作时，pointer ID 为 0；一般情况下，配置 0 即可。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragAction* dragAction | 拖拽行为对象。 |
| int32_t pointer | 手指ID，范围 0～9。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragAction_SetPixelMaps()**

```ets
int32_t OH_ArkUI_DragAction_SetPixelMaps(ArkUI_DragAction* dragAction, OH_PixelmapNative* pixelmapArray[], int32_t size)
```

描述：

设置拖拽跟手图，只能使用 pixelmap 格式对象。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragAction* dragAction | 拖拽行为对象。 |
| OH_PixelmapNative* pixelmapArray[] | 拖拽跟手图位图数组。 说明： 该参数必须为堆上分配对象，请开发者手动管理其生命周期。 |
| int32_t size | 拖拽跟手图数量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragAction_SetTouchPointX()**

```ets
int32_t OH_ArkUI_DragAction_SetTouchPointX(ArkUI_DragAction* dragAction, float x)
```

描述：

设置跟手点，相对于设置的第一个pixelmap的左上角。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragAction* dragAction | 拖拽行为对象。 |
| float x | 跟手点坐标x值，单位为px。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragAction_SetTouchPointY()**

```ets
int32_t OH_ArkUI_DragAction_SetTouchPointY(ArkUI_DragAction* dragAction, float y)
```

描述：

设置跟手点,相对于设置的第一个pixelmap的左上角。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragAction* dragAction | 拖拽行为对象。 |
| float y | 跟手点坐标y值，单位为px。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragAction_SetData()**

```ets
int32_t OH_ArkUI_DragAction_SetData(ArkUI_DragAction* dragAction, OH_UdmfData* data)
```

描述：

设置拖拽数据。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragAction* dragAction | 拖拽行为对象。 |
| OH_UdmfData* data | 拖拽数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragAction_SetDataLoadParams()**

```ets
ArkUI_ErrorCode OH_ArkUI_DragAction_SetDataLoadParams(ArkUI_DragAction* dragAction,OH_UdmfDataLoadParams* dataLoadParams)
```

描述：

使用此方法为系统提供一个数据加载参数，而不是直接提供一个完整的数据对象。当用户拖拽到目标应用程序并落入时，系统将使用dataLoadParams请求数据。可以极大地提高拖拽大量数据的效率，以及目标应用程序中处理落入数据的效率。此方法应始终优先于[OH_ArkUI_DragAction_SetData](drag_and_drop.h.md#ZH-CN_TOPIC_0000002522241024__oh_arkui_dragaction_setdata)使用。请参考udmf.h中的[OH_UdmfDataLoadParams_Create](udmf.h.md#ZH-CN_TOPIC_0000002522240654__oh_udmfdataloadparams_create)了解如何创建和准备数据加载参数。该方法与[OH_ArkUI_DragAction_SetData](drag_and_drop.h.md#ZH-CN_TOPIC_0000002522241024__oh_arkui_dragaction_setdata)存在冲突，系统始终以最后调用的方法为准。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragAction* dragAction | 拖拽行为对象。 |
| OH_UdmfDataLoadParams* dataLoadParams | 在落入操作时使用的数据加载参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragAction_SetDragPreviewOption()**

```ets
int32_t OH_ArkUI_DragAction_SetDragPreviewOption(ArkUI_DragAction* dragAction, ArkUI_DragPreviewOption* option)
```

描述：

将构造的ArkUI_DragPreviewOption设置给ArkUI_DragAction。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragAction* dragAction | 拖拽行为对象。 |
| ArkUI_DragPreviewOption* option | 自定义参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragAction_RegisterStatusListener()**

```ets
int32_t OH_ArkUI_DragAction_RegisterStatusListener(ArkUI_DragAction* dragAction, void* userData,void(*listener)(ArkUI_DragAndDropInfo* dragAndDropInfo, void* userData))
```

描述：

注册拖拽状态监听回调，该回调可感知到拖拽已经发起或用户松手结束的状态，可通过该监听获取到落入方对数据的接收处理是否成功。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragAction* dragAction | 拖拽行为对象。 |
| void* userData | 应用自定义数据。 |
| listener | 状态监听回调，回调触发时，系统会返回一个拖拽状态对象指针，该指针会在回调执行完成后被销毁，应用不应再持有。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragEvent_GetDisplayId()**

```ets
ArkUI_ErrorCode OH_ArkUI_DragEvent_GetDisplayId(ArkUI_DragEvent event, int32_t* displayId)
```

描述：

获取当前拖拽事件发生时所在的屏幕ID，不支持当eventType为NODE_ON_DRAG_END时获取。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent event | ArkUI_DragEvent事件指针。 |
| int32_t* displayId | 返回当前拖拽事件发生时所在的屏幕ID。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragAction_UnregisterStatusListener()**

```ets
void OH_ArkUI_DragAction_UnregisterStatusListener(ArkUI_DragAction* dragAction)
```

描述：

解注册拖拽状态监听回调。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragAction* dragAction | 拖拽行为对象。 |

**OH_ArkUI_DragAndDropInfo_GetDragStatus()**

```ets
ArkUI_DragStatus OH_ArkUI_DragAndDropInfo_GetDragStatus(ArkUI_DragAndDropInfo* dragAndDropInfo)
```

描述：

获取dragaction发起拖拽的状态，获取异常时返回 ArkUI_DRAG_STATUS_UNKNOWN。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragAndDropInfo* dragAndDropInfo | 拖拽状态监听返回的拖拽相关信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_DragStatus | ArkUI_DragStatus 拖拽状态，如果获取失败，返回默认值 ArkUI_DRAG_STATUS_UNKNOWN。 |

**OH_ArkUI_DragAndDropInfo_GetDragEvent()**

```ets
ArkUI_DragEvent* OH_ArkUI_DragAndDropInfo_GetDragEvent(ArkUI_DragAndDropInfo* dragAndDropInfo)
```

描述：

通过dragAndDropInfo获取到DragEvent，可通过DragEvent获取释放结果等。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragAndDropInfo* dragAndDropInfo | 拖拽状态监听返回的拖拽相关信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_DragEvent* | ArkUI_DragEvent 拖拽事件，如果获取失败，则返回空。 |

**OH_ArkUI_StartDrag()**

```ets
int32_t OH_ArkUI_StartDrag(ArkUI_DragAction* dragAction)
```

描述：

通过构造的DragAction对象发起拖拽。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragAction* dragAction | 拖拽action对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragEvent_RequestDragEndPending()**

```ets
int32_t OH_ArkUI_DragEvent_RequestDragEndPending(ArkUI_DragEvent* event, int32_t* requestIdentify)
```

描述：

请求延迟处理拖拽结束事件，等待应用程序确认操作结果。应用程序需通过 [OH_ArkUI_NotifyDragResult](drag_and_drop.h.md#ZH-CN_TOPIC_0000002522241024__oh_arkui_notifydragresult)接口将最终结果回传至系统，并在所有处理完成后调用 [OH_ArkUI_NotifyDragEndPendingDone](drag_and_drop.h.md#ZH-CN_TOPIC_0000002522241024__oh_arkui_notifydragendpendingdone)。最大等待时间为2秒。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | 指向 ArkUI_DragEvent 对象的指针。 |
| int32_t* requestIdentify | 系统自动生成的请求标识符，是一个输出参数，需要为一个有效的地址。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。  ARKUI_ERROR_CODE_DRAG_DROP_OPERATION_NOT_ALLOWED 当前阶段不允许该操作。 |

**OH_ArkUI_NotifyDragResult()**

```ets
int32_t OH_ArkUI_NotifyDragResult(int32_t requestIdentify, ArkUI_DragResult result)
```

描述：

通知系统最终拖拽结果。系统会校验请求标识符是否与[OH_ArkUI_DragEvent_RequestDragEndPending](drag_and_drop.h.md#ZH-CN_TOPIC_0000002522241024__oh_arkui_dragevent_requestdragendpending)返回的一致，不一致则忽略本次调用。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| int32_t requestIdentify | 由 OH_ArkUI_DragEvent_RequestDragEndPending 返回的标识符。 |
| ArkUI_DragResult result | 拖拽结果枚举值（ArkUI_DragResult 类型）。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。  ARKUI_ERROR_CODE_DRAG_DROP_OPERATION_NOT_ALLOWED 当前阶段不允许该操作。 |

**OH_ArkUI_NotifyDragEndPendingDone()**

```ets
int32_t OH_ArkUI_NotifyDragEndPendingDone(int32_t requestIdentify)
```

描述：

通知系统所有异步处理已完成，可结束拖拽结束挂起状态。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| int32_t requestIdentify | 由 OH_ArkUI_DragEvent_RequestDragEndPending 返回的标识符。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。  ARKUI_ERROR_CODE_DRAG_DROP_OPERATION_NOT_ALLOWED 当前阶段不允许该操作。 |

**OH_ArkUI_EnableDropDisallowedBadge()**

```ets
ArkUI_ErrorCode OH_ArkUI_EnableDropDisallowedBadge(ArkUI_ContextHandle uiContext, bool enabled)
```

描述：

设置是否可以显示禁用角标。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ContextHandle uiContext | UI实例对象指针。 |
| bool enabled | 是否可以显示禁用角标。true表示可以显示禁用角标，false表示不可以显示禁用角标。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragEvent_GetTouchPointXToGlobalDisplay()**

```ets
float OH_ArkUI_DragEvent_GetTouchPointXToGlobalDisplay(ArkUI_DragEvent* event)
```

描述：

从ArkUI_DragEvent中获取跟手点相对于全局屏幕的x轴坐标。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | float 返回拖拽跟手点相对于全局Display的x轴坐标，单位为px，传入参数无效时返回默认值0。 |

**OH_ArkUI_DragEvent_GetTouchPointYToGlobalDisplay()**

```ets
float OH_ArkUI_DragEvent_GetTouchPointYToGlobalDisplay(ArkUI_DragEvent* event)
```

描述：

从ArkUI_DragEvent中获取跟手点相对于全局屏幕的y轴坐标。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | ArkUI_DragEvent事件指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | float 返回拖拽跟手点相对于全局Display的y轴坐标，单位为px，传入参数无效时返回默认值0。 |

**OH_ArkUI_DragEvent_GetDragSource()**

```ets
ArkUI_ErrorCode OH_ArkUI_DragEvent_GetDragSource(ArkUI_DragEvent* event, char *bundleName, int32_t length)
```

描述：

获取拖拽发起方的应用包名信息，需要传递一个字符数组来接收包名字符串，并显式指明数组长度，该数组长度不小于128个字符。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | 指向ArkUI_DragEvent对象的指针。 |
| char *bundleName | 用来接收拖起方包名的字符串数组，长度不应小于128个字符。 |
| int32_t length | 用来显式指明传入的字符串数组长度，不应小于128个字符。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_DragEvent_IsRemote()**

```ets
ArkUI_ErrorCode OH_ArkUI_DragEvent_IsRemote(ArkUI_DragEvent* event, bool* isRemote)
```

描述：

判断当前的拖拽操作是否是跨设备拖拽。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DragEvent* event | 指向ArkUI_DragEvent对象的指针。 |
| bool* isRemote | 布尔变量指针，用来接收是否是跨设备拖拽。true表示是跨设备拖拽，false表示非跨设备拖拽。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |