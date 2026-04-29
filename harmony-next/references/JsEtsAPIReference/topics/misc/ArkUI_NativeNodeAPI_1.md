# ArkUI_NativeNodeAPI_1

```ets
typedef struct {...} ArkUI_NativeNodeAPI_1
```

**概述**

ArkUI提供的Native侧Node类型接口集合。Node模块相关接口需要在主线程上调用。

起始版本： 12

相关模块： [ArkUI_NativeModule](ArkUI_NativeModule.md)

所在头文件： [native_node.h](native_node.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int32_t version | 结构体版本，当前使用的ArkUI_NativeNodeAPI_1结构体的版本编号，由系统提供，开发者无需修改。 |

**成员函数**

| 名称 | 描述 |
| --- | --- |
| ArkUI_NodeHandle (*createNode)(ArkUI_NodeType type) | 基于ArkUI_NodeType生成对应的组件并返回组件对象指针。 |
| void (*disposeNode)(ArkUI_NodeHandle node) | 销毁组件指针指向的组件对象。 |
| int32_t (*addChild)(ArkUI_NodeHandle parent, ArkUI_NodeHandle child) | 将组件挂载到某个父节点之下。 |
| int32_t (*removeChild)(ArkUI_NodeHandle parent, ArkUI_NodeHandle child) | 将组件从父节点中移除。 |
| int32_t (*insertChildAfter)(ArkUI_NodeHandle parent, ArkUI_NodeHandle child, ArkUI_NodeHandle sibling) | 将组件挂载到某个父节点之下，挂载位置在sibling节点之后。 |
| int32_t (*insertChildBefore)(ArkUI_NodeHandle parent, ArkUI_NodeHandle child, ArkUI_NodeHandle sibling) | 将组件挂载到某个父节点之下，挂载位置在sibling节点之前。 |
| int32_t (*insertChildAt)(ArkUI_NodeHandle parent, ArkUI_NodeHandle child, int32_t position) | 将组件挂载到某个父节点之下，挂载位置由position指定。 |
| int32_t (*setAttribute)(ArkUI_NodeHandle node, ArkUI_NodeAttributeType attribute, const ArkUI_AttributeItem* item) | 属性设置函数。 |
| const ArkUI_AttributeItem* (*getAttribute)(ArkUI_NodeHandle node, ArkUI_NodeAttributeType attribute) | 属性获取函数。该接口返回的指针是ArkUI框架内部的缓冲区指针，不需要开发者主动调用delete释放内存，但是需要在该函数下一次被调用前使用，否则可能会被其他值所覆盖。 |
| int32_t (*resetAttribute)(ArkUI_NodeHandle node, ArkUI_NodeAttributeType attribute) | 重置属性函数。 |
| int32_t (*registerNodeEvent)(ArkUI_NodeHandle node, ArkUI_NodeEventType eventType, int32_t targetId, void* userData) | 注册节点事件函数。 |
| void (*unregisterNodeEvent)(ArkUI_NodeHandle node, ArkUI_NodeEventType eventType) | 反注册节点事件函数。 |
| void (*registerNodeEventReceiver)(void (*eventReceiver)(ArkUI_NodeEvent* event)) | 注册事件回调统一入口函数。ArkUI框架会统一收集过程中产生的组件事件并通过注册的eventReceiver函数回调给开发者。  重复调用时会覆盖前一次注册的函数。 避免直接保存ArkUI_NodeEvent对象指针，数据会在回调结束后销毁。  如果需要和组件实例绑定，可以使用addNodeEventReceiver函数接口。 |
| void (*unregisterNodeEventReceiver)() | 反注册事件回调统一入口函数。 |
| void (*markDirty)(ArkUI_NodeHandle node, ArkUI_NodeDirtyFlag dirtyFlag) | 强制标记当前节点，使其重新执行测量、布局或者绘制的区域。系统属性设置更新场景下，ArkUI框架会自动标记节点并重新执行测量，布局或者绘制，不需要开发者主动调用该函数。 |
| uint32_t (*getTotalChildCount)(ArkUI_NodeHandle node) | 获取子节点的个数。 |
| ArkUI_NodeHandle (*getChildAt)(ArkUI_NodeHandle node, int32_t position) | 获取子节点。 |
| ArkUI_NodeHandle (*getFirstChild)(ArkUI_NodeHandle node) | 获取第一个子节点。 |
| ArkUI_NodeHandle (*getLastChild)(ArkUI_NodeHandle node) | 获取最后一个子节点。 |
| ArkUI_NodeHandle (*getPreviousSibling)(ArkUI_NodeHandle node) | 获取上一个兄弟节点。 |
| ArkUI_NodeHandle (*getNextSibling)(ArkUI_NodeHandle node) | 获取下一个兄弟节点。 |
| int32_t (*registerNodeCustomEvent)(ArkUI_NodeHandle node, ArkUI_NodeCustomEventType eventType, int32_t targetId, void* userData) | 注册自定义节点事件函数。事件触发时通过registerNodeCustomEventReceiver注册的自定义事件入口函数返回。 |
| void (*unregisterNodeCustomEvent)(ArkUI_NodeHandle node, ArkUI_NodeCustomEventType eventType) | 反注册自定义节点事件函数。 |
| void (*registerNodeCustomEventReceiver)(void (*eventReceiver)(ArkUI_NodeCustomEvent* event)) | 注册自定义节点事件回调统一入口函数。ArkUI框架会统一收集过程中产生的自定义组件事件并通过注册的registerNodeCustomEventReceiver函数回调给开发者。  重复调用时会覆盖前一次注册的函数。  避免直接保存ArkUI_NodeCustomEvent对象指针，数据会在回调结束后销毁。  如果需要和组件实例绑定，可以使用addNodeCustomEventReceiver函数接口。 |
| void (*unregisterNodeCustomEventReceiver)() | 反注册自定义节点事件回调统一入口函数。 |
| int32_t (*setMeasuredSize)(ArkUI_NodeHandle node, int32_t width, int32_t height) | 在测算回调函数中设置组件的测算完成后的宽和高。 |
| int32_t (*setLayoutPosition)(ArkUI_NodeHandle node, int32_t positionX, int32_t positionY) | 在布局回调函数中设置组件的位置。 |
| ArkUI_IntSize (*getMeasuredSize)(ArkUI_NodeHandle node) | 获取组件测算完成后的宽高尺寸。 |
| ArkUI_IntOffset (*getLayoutPosition)(ArkUI_NodeHandle node) | 获取组件布局完成后的位置。 |
| int32_t (*measureNode)(ArkUI_NodeHandle node, ArkUI_LayoutConstraint* Constraint) | 对目标组件进行测算，可以通过getMeasuredSize接口获取测算后的大小。 |
| int32_t (*layoutNode)(ArkUI_NodeHandle node, int32_t positionX, int32_t positionY) | 对目标组件进行布局并传递该组件相对父组件的期望位置。 |
| int32_t (*addNodeEventReceiver)(ArkUI_NodeHandle node, void (*eventReceiver)(ArkUI_NodeEvent* event)) | 在组件上添加组件事件回调函数，用于接受该组件产生的组件事件。不同于registerNodeEventReceiver的全局注册函数，该函数允许在同一个组件上添加多个事件接受器。  该函数添加的监听回调函数触发时机会先于registerNodeEventReceiver注册的全局回调函数。  避免直接保存ArkUI_NodeEvent对象指针，数据会在回调结束后销毁。 |
| int32_t (*removeNodeEventReceiver)(ArkUI_NodeHandle node, void (*eventReceiver)(ArkUI_NodeEvent* event)) | 在组件上删除注册的组件事件回调函数。 |
| int32_t (*addNodeCustomEventReceiver)(ArkUI_NodeHandle node, void (*eventReceiver)(ArkUI_NodeCustomEvent* event)) | 在组件上添加自定义事件回调函数，用于接受该组件产生的自定义事件（如布局事件，绘制事件）。不同于registerNodeCustomEventReceiver的全局注册函数，该函数允许在同一个组件上添加多个事件接受器。  该函数添加的监听回调函数触发时机会先于registerNodeCustomEventReceiver注册的全局回调函数。  避免直接保存ArkUI_NodeCustomEvent对象指针，数据会在回调结束后销毁。 |
| int32_t (*removeNodeCustomEventReceiver)(ArkUI_NodeHandle node, void (*eventReceiver)(ArkUI_NodeCustomEvent* event)) | 在组件上删除注册的自定义事件回调函数。 |
| int32_t (*setUserData)(ArkUI_NodeHandle node, void* userData) | 在组件上保存自定义数据。 |
| void* (*getUserData)(ArkUI_NodeHandle node) | 获取在组件上保存的自定义数据。 |
| int32_t (*setLengthMetricUnit)(ArkUI_NodeHandle node, ArkUI_LengthMetricUnit unit) | 指定组件的单位。 |
| ArkUI_NodeHandle (*getParent)(ArkUI_NodeHandle node) | 获取父节点。 |
| int32_t (*removeAllChildren)(ArkUI_NodeHandle parent) | 从父组件上卸载所有子节点。 |

**成员函数说明**

**createNode()**

```ets
ArkUI_NodeHandle (*createNode)(ArkUI_NodeType type)
```

描述：

基于[ArkUI_NodeType](native_node.h.md#ZH-CN_TOPIC_0000002522081032__arkui_nodetype)生成对应的组件并返回组件对象指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeType type | 创建指定类型的UI组件节点。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_NodeHandle | 返回创建完成的组件操作指针，如果创建失败返回NULL。需要开发者自行管理返回的组件对象指针的生命周期，否则有可能导致Use After Free等进程崩溃或内存泄漏问题。 |

**disposeNode()**

```ets
void (*disposeNode)(ArkUI_NodeHandle node)
```

描述：

销毁组件指针指向的组件对象。在非主线程调用时需要注意待销毁组件对象的生命周期，生命周期管理不当有可能导致应用崩溃，因此不建议在非主线程上调用本接口。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 组件指针对象。 |

**addChild()**

```ets
int32_t (*addChild)(ArkUI_NodeHandle parent, ArkUI_NodeHandle child)
```

描述：

将组件挂载到某个父节点之下。本接口属于节点操作接口，不建议在非主线程上调用。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle parent | 父节点指针。 |
| ArkUI_NodeHandle child | 子节点指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。  ARKUI_ERROR_CODE_NOT_SUPPROTED_FOR_ARKTS_NODE 不支持对ArkTS创建的节点执行对应的操作。   ARKUI_ERROR_CODE_NODE_IS_ADOPTED 节点已被接纳为附属节点。从API version 22开始支持。 |

**removeChild()**

```ets
int32_t (*removeChild)(ArkUI_NodeHandle parent, ArkUI_NodeHandle child)
```

描述：

将组件从父节点中移除。本接口属于节点操作接口，不建议在非主线程上调用。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle parent | 父节点指针。 |
| ArkUI_NodeHandle child | 子节点指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。  ARKUI_ERROR_CODE_NOT_SUPPROTED_FOR_ARKTS_NODE 不支持对ArkTS创建的节点执行对应的操作。  ERROR_CODE_NATIVE_IMPL_NODE_ADAPTER_EXIST NodeAdapter已经存在。 |

**insertChildAfter()**

```ets
int32_t (*insertChildAfter)(ArkUI_NodeHandle parent, ArkUI_NodeHandle child, ArkUI_NodeHandle sibling)
```

描述：

将组件挂载到某个父节点之下，挂载位置在sibling节点之后。本接口属于节点操作接口，不建议在非主线程上调用。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle parent | 父节点指针。 |
| ArkUI_NodeHandle child | 子节点指针。 |
| ArkUI_NodeHandle sibling | 前一个兄弟节点指针，如果为空则插入位置在最后面。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。  ARKUI_ERROR_CODE_NOT_SUPPROTED_FOR_ARKTS_NODE 不支持对ArkTS创建的节点执行对应的操作。  ARKUI_ERROR_CODE_NODE_IS_ADOPTED 节点已被接纳为附属节点。从API version 22开始支持。 |

**insertChildBefore()**

```ets
int32_t (*insertChildBefore)(ArkUI_NodeHandle parent, ArkUI_NodeHandle child, ArkUI_NodeHandle sibling)
```

描述：

将组件挂载到某个父节点之下，挂载位置在sibling节点之前。本接口属于节点操作接口，不建议在非主线程上调用。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle parent | 父节点指针。 |
| ArkUI_NodeHandle child | 子节点指针。 |
| ArkUI_NodeHandle sibling | 后一个兄弟节点指针，如果为空则插入位置在最后面。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。  ARKUI_ERROR_CODE_NOT_SUPPROTED_FOR_ARKTS_NODE 不支持对ArkTS创建的节点执行对应的操作。  ARKUI_ERROR_CODE_NODE_IS_ADOPTED 节点已被接纳为附属节点。从API version 22开始支持。 |

**insertChildAt()**

```ets
int32_t (*insertChildAt)(ArkUI_NodeHandle parent, ArkUI_NodeHandle child, int32_t position)
```

描述：

将组件挂载到某个父节点之下，挂载位置由position指定。本接口属于节点操作接口，不建议在非主线程上调用。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle parent | 父节点指针。 |
| ArkUI_NodeHandle child | 子节点指针。 |
| int32_t position | 插入位置，如果插入位置为负数或者不存在，则默认插入位置在最后面。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。  ARKUI_ERROR_CODE_NOT_SUPPROTED_FOR_ARKTS_NODE 不支持对ArkTS创建的节点执行对应的操作。  ARKUI_ERROR_CODE_NODE_IS_ADOPTED 节点已被接纳为附属节点。从API version 22开始支持。 |

**setAttribute()**

```ets
int32_t (*setAttribute)(ArkUI_NodeHandle node, ArkUI_NodeAttributeType attribute, const ArkUI_AttributeItem* item)
```

描述：

属性设置函数，不建议在非主线程上调用。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 需要设置属性的节点对象。 |
| ArkUI_NodeAttributeType attribute | 需要设置的属性类型。 |
| const ArkUI_AttributeItem* item | 需要设置的属性值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。  ARKUI_ERROR_CODE_ATTRIBUTE_OR_EVENT_NOT_SUPPORTED 组件不支持该属性。  ARKUI_ERROR_CODE_NOT_SUPPROTED_FOR_ARKTS_NODE 不支持对ArkTS创建的节点执行对应的操作。  ERROR_CODE_NATIVE_IMPL_NODE_ADAPTER_EXIST NodeAdapter已经存在。 |

**getAttribute()**

```ets
const ArkUI_AttributeItem* (*getAttribute)(ArkUI_NodeHandle node, ArkUI_NodeAttributeType attribute)
```

描述：

属性获取函数。该接口返回的指针是ArkUI框架内部的缓冲区指针，不需要开发者主动调用delete释放内存，但是需要在该函数下一次被调用前使用，否则可能会被其他值所覆盖。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 需要获取属性的节点对象。 |
| ArkUI_NodeAttributeType attribute | 需要获取的属性类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const ArkUI_AttributeItem* | 当前属性类型的属性值，失败返回空指针。 |

**resetAttribute()**

```ets
int32_t (*resetAttribute)(ArkUI_NodeHandle node, ArkUI_NodeAttributeType attribute)
```

描述：

重置属性函数，不建议在非主线程上调用。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 需要重置属性的节点对象。 |
| ArkUI_NodeAttributeType attribute | 需要重置的属性类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。  ARKUI_ERROR_CODE_ATTRIBUTE_OR_EVENT_NOT_SUPPORTED 组件不支持该属性。  ARKUI_ERROR_CODE_NOT_SUPPROTED_FOR_ARKTS_NODE 不支持对ArkTS创建的节点执行对应的操作。 |

**registerNodeEvent()**

```ets
int32_t (*registerNodeEvent)(ArkUI_NodeHandle node, ArkUI_NodeEventType eventType, int32_t targetId, void* userData)
```

描述：

注册节点事件函数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 需要注册事件的节点对象。 |
| ArkUI_NodeEventType eventType | 需要注册的事件类型。 |
| int32_t targetId | 自定义事件ID，当事件触发时在回调参数ArkUI_NodeEvent 中携带回来。 |
| void* userData | 自定义事件参数，当事件触发时在回调参数ArkUI_NodeEvent 中携带回来。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。  ARKUI_ERROR_CODE_ATTRIBUTE_OR_EVENT_NOT_SUPPORTED 组件不支持该事件。  ARKUI_ERROR_CODE_NOT_SUPPROTED_FOR_ARKTS_NODE 不支持对ArkTS创建的节点执行对应的操作。 |

**unregisterNodeEvent()**

```ets
void (*unregisterNodeEvent)(ArkUI_NodeHandle node, ArkUI_NodeEventType eventType)
```

描述：

反注册节点事件函数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 需要反注册事件的节点对象。 |
| ArkUI_NodeEventType eventType | 需要反注册的事件类型。 |

**registerNodeEventReceiver()**

```ets
void (*registerNodeEventReceiver)(void (*eventReceiver)(ArkUI_NodeEvent* event))
```

描述：

注册事件回调统一入口函数。ArkUI框架会统一收集过程中产生的组件事件并通过注册的eventReceiver函数回调给开发者。

 重复调用时会覆盖前一次注册的函数。 避免直接保存[ArkUI_NodeEvent](ArkUI_NodeEvent.md)对象指针，数据会在回调结束后销毁。

 如果需要和组件实例绑定，可以使用addNodeEventReceiver函数接口。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| void (*eventReceiver)(ArkUI_NodeEvent* event) | 事件回调统一入口函数。 |

**unregisterNodeEventReceiver()**

```ets
void (*unregisterNodeEventReceiver)()
```

描述：

反注册事件回调统一入口函数。

起始版本： 12

**markDirty()**

```ets
void (*markDirty)(ArkUI_NodeHandle node, ArkUI_NodeDirtyFlag dirtyFlag)
```

描述：

强制标记当前节点，使其重新执行测量、布局或者绘制的区域。系统属性设置更新场景下，ArkUI框架会自动标记节点并重新执行测量，布局或者绘制，不需要开发者主动调用该函数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 需要标记重新执行测量、布局或者绘制的节点对象。 |
| ArkUI_NodeDirtyFlag dirtyFlag | 重新执行测量、布局或者绘制的类型。 |

**getTotalChildCount()**

```ets
uint32_t (*getTotalChildCount)(ArkUI_NodeHandle node)
```

描述：

获取子节点的个数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 目标节点对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| uint32_t | 子节点的个数, 如果没有返回0。 |

**getChildAt()**

```ets
ArkUI_NodeHandle (*getChildAt)(ArkUI_NodeHandle node, int32_t position)
```

描述：

获取子节点。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 目标节点对象。 |
| int32_t position | 子组件的位置。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_NodeHandle | 返回组件的指针，如果没有返回NULL。 |

**getFirstChild()**

```ets
ArkUI_NodeHandle (*getFirstChild)(ArkUI_NodeHandle node)
```

描述：

获取第一个子节点。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 目标节点对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_NodeHandle | 返回组件的指针，如果没有返回NULL。 |

**getLastChild()**

```ets
ArkUI_NodeHandle (*getLastChild)(ArkUI_NodeHandle node)
```

描述：

获取最后一个子节点。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 目标节点对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_NodeHandle | 返回组件的指针，如果没有返回NULL。 |

**getPreviousSibling()**

```ets
ArkUI_NodeHandle (*getPreviousSibling)(ArkUI_NodeHandle node)
```

描述：

获取上一个兄弟节点。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 目标节点对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_NodeHandle | 返回组件的指针，如果没有返回NULL。 |

**getNextSibling()**

```ets
ArkUI_NodeHandle (*getNextSibling)(ArkUI_NodeHandle node)
```

描述：

获取下一个兄弟节点。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 目标节点对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_NodeHandle | 返回组件的指针，如果没有返回NULL。 |

**registerNodeCustomEvent()**

```ets
int32_t (*registerNodeCustomEvent)(ArkUI_NodeHandle node, ArkUI_NodeCustomEventType eventType, int32_t targetId, void* userData)
```

描述：

注册自定义节点事件函数。事件触发时通过registerNodeCustomEventReceiver注册的自定义事件入口函数返回。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 需要注册事件的节点对象。 |
| ArkUI_NodeCustomEventType eventType | 需要注册的事件类型。 |
| int32_t targetId | 自定义事件ID，当事件触发时在回调参数ArkUI_NodeCustomEvent 中携带回来。 |
| void* userData | 自定义事件参数，当事件触发时在回调参数ArkUI_NodeCustomEvent 中携带回来。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。  ARKUI_ERROR_CODE_ATTRIBUTE_OR_EVENT_NOT_SUPPORTED 组件不支持该事件。 |

**unregisterNodeCustomEvent()**

```ets
void (*unregisterNodeCustomEvent)(ArkUI_NodeHandle node, ArkUI_NodeCustomEventType eventType)
```

描述：

反注册自定义节点事件函数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 需要反注册事件的节点对象。 |
| ArkUI_NodeCustomEventType eventType | 需要反注册的事件类型。 |

**registerNodeCustomEventReceiver()**

```ets
void (*registerNodeCustomEventReceiver)(void (*eventReceiver)(ArkUI_NodeCustomEvent* event))
```

描述：

注册自定义节点事件回调统一入口函数。ArkUI框架会统一收集过程中产生的自定义组件事件并通过注册的registerNodeCustomEventReceiver函数回调给开发者。

 重复调用时会覆盖前一次注册的函数。

 避免直接保存[ArkUI_NodeCustomEvent](ArkUI_NodeCustomEvent.md)对象指针，数据会在回调结束后销毁。

 如果需要和组件实例绑定，可以使用addNodeCustomEventReceiver函数接口。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| void (*eventReceiver)(ArkUI_NodeCustomEvent* event) | 事件回调统一入口函数。 |

**unregisterNodeCustomEventReceiver()**

```ets
void (*unregisterNodeCustomEventReceiver)()
```

描述：

反注册自定义节点事件回调统一入口函数。

起始版本： 12

**setMeasuredSize()**

```ets
int32_t (*setMeasuredSize)(ArkUI_NodeHandle node, int32_t width, int32_t height)
```

描述：

在测算回调函数中设置组件的测算完成后的宽和高。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 目标节点对象。 |
| int32_t width | 设置的宽。 |
| int32_t height | 设置的高。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setLayoutPosition()**

```ets
int32_t (*setLayoutPosition)(ArkUI_NodeHandle node, int32_t positionX, int32_t positionY)
```

描述：

在布局回调函数中设置组件的位置。该接口优先级低于[NODE_POSITION](native_type.h.md#ZH-CN_TOPIC_0000002553200995__枚举)。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 目标节点对象。 |
| int32_t positionX | x轴坐标。 |
| int32_t positionY | y轴坐标。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**getMeasuredSize()**

```ets
ArkUI_IntSize (*getMeasuredSize)(ArkUI_NodeHandle node)
```

描述：

获取组件测算完成后的宽高尺寸。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 目标节点对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_IntSize | ArkUI_IntSize 组件的宽高。 |

**getLayoutPosition()**

```ets
ArkUI_IntOffset (*getLayoutPosition)(ArkUI_NodeHandle node)
```

描述：

获取组件布局完成后的位置。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 目标节点对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_IntOffset | ArkUI_IntOffset 组件的位置。 |

**measureNode()**

```ets
int32_t (*measureNode)(ArkUI_NodeHandle node, ArkUI_LayoutConstraint* Constraint)
```

描述：

对目标组件进行测算，可以通过getMeasuredSize接口获取测算后的大小。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 目标节点对象。 |
| ArkUI_LayoutConstraint* Constraint | 约束尺寸。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**layoutNode()**

```ets
int32_t (*layoutNode)(ArkUI_NodeHandle node, int32_t positionX, int32_t positionY)
```

描述：

对目标组件进行布局并传递该组件相对父组件的期望位置。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 目标节点对象。 |
| int32_t positionX | x轴坐标。 |
| int32_t positionY | y轴坐标。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**addNodeEventReceiver()**

```ets
int32_t (*addNodeEventReceiver)(ArkUI_NodeHandle node, void (*eventReceiver)(ArkUI_NodeEvent* event))
```

描述：

在组件上添加组件事件回调函数，用于接受该组件产生的组件事件。不同于registerNodeEventReceiver的全局注册函数，该函数允许在同一个组件上添加多个事件接受器。

 该函数添加的监听回调函数触发时机会先于registerNodeEventReceiver注册的全局回调函数。

 避免直接保存[ArkUI_NodeEvent](ArkUI_NodeEvent.md) 对象指针，数据会在回调结束后销毁。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 用于添加组件事件回调函数的对象。 |
| void (*eventReceiver)(ArkUI_NodeEvent* event) | 组件事件回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**removeNodeEventReceiver()**

```ets
int32_t (*removeNodeEventReceiver)(ArkUI_NodeHandle node, void (*eventReceiver)(ArkUI_NodeEvent* event))
```

描述：

在组件上删除注册的组件事件回调函数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 用于删除组件事件回调函数的对象。 |
| void (eventReceiver)(ArkUI_NodeEvent event) | 待删除的组件事件回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**addNodeCustomEventReceiver()**

```ets
int32_t (*addNodeCustomEventReceiver)(ArkUI_NodeHandle node, void (*eventReceiver)(ArkUI_NodeCustomEvent* event))
```

描述：

在组件上添加自定义事件回调函数，用于接受该组件产生的自定义事件（如布局事件，绘制事件）。不同于registerNodeCustomEventReceiver的全局注册函数，该函数允许在同一个组件上添加多个事件接受器。

 该函数添加的监听回调函数触发时机会先于registerNodeCustomEventReceiver注册的全局回调函数。

 避免直接保存[ArkUI_NodeCustomEvent](ArkUI_NodeCustomEvent.md)对象指针，数据会在回调结束后销毁。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 用于添加组件自定义事件回调函数的对象。 |
| void (*eventReceiver)(ArkUI_NodeCustomEvent* event) | 组件自定义事件回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**removeNodeCustomEventReceiver()**

```ets
int32_t (*removeNodeCustomEventReceiver)(ArkUI_NodeHandle node, void (*eventReceiver)(ArkUI_NodeCustomEvent* event))
```

描述：

在组件上删除注册的自定义事件回调函数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 用于删除组件自定义事件回调函数的对象。 |
| void (*eventReceiver)(ArkUI_NodeCustomEvent* event) | 待删除的组件自定义事件回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**setUserData()**

```ets
int32_t (*setUserData)(ArkUI_NodeHandle node, void* userData)
```

描述：

在组件上保存自定义数据。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 用于保存自定义数据的组件。 |
| void* userData | 要保存的自定义数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**getUserData()**

```ets
void* (*getUserData)(ArkUI_NodeHandle node)
```

描述：

获取在组件上保存的自定义数据。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 保存了自定义数据的组件。 |

返回：

| 类型 | 说明 |
| --- | --- |
| void* | 自定义数据。 |

**setLengthMetricUnit()**

```ets
int32_t (*setLengthMetricUnit)(ArkUI_NodeHandle node, ArkUI_LengthMetricUnit unit)
```

描述：

指定组件的单位。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 用于指定单位的组件。 |
| ArkUI_LengthMetricUnit unit | 单位类型ArkUI_LengthMetricUnit，默认为 ARKUI_LENGTH_METRIC_UNIT_DEFAULT。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**getParent()**

```ets
ArkUI_NodeHandle (*getParent)(ArkUI_NodeHandle node)
```

描述：

获取父节点。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 目标节点对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_NodeHandle | 返回组件的指针，如果没有返回NULL。 |

**removeAllChildren()**

```ets
int32_t (*removeAllChildren)(ArkUI_NodeHandle parent)
```

描述：

从父组件上卸载所有子节点。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle parent | 目标节点对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。  ARKUI_ERROR_CODE_NO_ERROR 成功。  ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |