# ArkUI_NativeGestureAPI_1

```ets
typedef struct {...} ArkUI_NativeGestureAPI_1
```

**概述**

手势模块接口集合。

起始版本： 12

相关模块： [ArkUI_NativeModule](ArkUI_NativeModule.md)

所在头文件： [native_gesture.h](native_gesture.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int32_t version | 结构版本号 = 1。 |

**成员函数**

| 名称 | 描述 |
| --- | --- |
| ArkUI_GestureRecognizer* (*createTapGesture)(int32_t countNum, int32_t fingersNum) | 创建敲击手势。1. 支持单击、双击和多次点击事件的识别。  2. 当配置多击时，上一次的最后一根手指抬起和下一次的第一根手指按下的超时时间为300毫秒。  3. 当上次点击的位置与当前点击的位置距离超过60vp等效像素点时，手势识别失败。  4. 当配置多指时，第一根手指按下后300毫秒内未有足够的手指数按下，手势识别失败，  第一根手指抬起后300毫秒内未有足够的手指抬起，手势识别失败。  5. 实际点击手指数超过配置值，手势识别成功。 |
| ArkUI_GestureRecognizer* (*createLongPressGesture)(int32_t fingersNum, bool repeatResult, int32_t durationNum) | 创建长按手势。1. 用于触发长按手势事件，触发长按手势的最少手指数为1，最短长按时间为500毫秒。  2. 当组件默认支持可拖拽时，如Text、TextInput、TextArea、HyperLink、Image和RichEditor等组件。  长按手势与拖拽会出现冲突，事件优先级如下：  长按触发时间 < 500ms，长按事件优先拖拽事件响应。  长按触发时间 >= 500ms，拖拽事件优先长按事件响应。  3. 手指按下后若发生超过15px的移动，则判定当前长按手势识别失败。 |
| ArkUI_GestureRecognizer* (*createPanGesture)(int32_t fingersNum, ArkUI_GestureDirectionMask directions, double distanceNum) | 创建滑动手势。1. 当滑动的最小距离超过设定的最小值时触发滑动手势事件。  2. Tabs组件滑动与该滑动手势事件同时存在时，可将distanceNum值设为1，使拖动更灵敏，避免造成事件错乱。 |
| ArkUI_GestureRecognizer* (*createPinchGesture)(int32_t fingersNum, double distanceNum) | 创建捏合手势。1. 触发捏合手势的最少手指为2指，最大为5指，最小识别距离为distanceNum 像素点。  2. 触发手势手指可以多于fingersNum数目，但只有先落下的与fingersNum相同数目的手指参与手势计算。 |
| ArkUI_GestureRecognizer* (*createRotationGesture)(int32_t fingersNum, double angleNum) | 创建旋转手势。1. 触发旋转手势的最少手指为2指，最大为5指，最小改变度数为1度。  2. 触发手势手指可以多于fingers数目，但只有先落下的两指参与手势计算。 |
| ArkUI_GestureRecognizer* (*createSwipeGesture)(int32_t fingersNum, ArkUI_GestureDirectionMask directions, double speedNum) | 创建快滑手势。1. 用于触发快滑事件，滑动速度大于speedNum px/s时可识别成功。 |
| ArkUI_GestureRecognizer* (*createGroupGesture)(ArkUI_GroupGestureMode gestureMode) | 创建手势组。 |
| void (*dispose)(ArkUI_GestureRecognizer* recognizer) | 销毁手势，释放资源。 |
| int32_t (*addChildGesture)(ArkUI_GestureRecognizer* group, ArkUI_GestureRecognizer* child) | 手势组增加子手势。 |
| int32_t (*removeChildGesture)(ArkUI_GestureRecognizer* group, ArkUI_GestureRecognizer* child) | 删除子手势。 |
| int32_t (*setGestureEventTarget)(ArkUI_GestureRecognizer* recognizer, ArkUI_GestureEventActionTypeMask actionTypeMask, void* extraParams,void (*targetReceiver)(ArkUI_GestureEvent* event, void* extraParams)) | 创建手势关联回调方法。 |
| int32_t (*addGestureToNode)(ArkUI_NodeHandle node, ArkUI_GestureRecognizer* recognizer, ArkUI_GesturePriority mode, ArkUI_GestureMask mask) | 将手势添加到UI组件。 |
| int32_t (*removeGestureFromNode)(ArkUI_NodeHandle node, ArkUI_GestureRecognizer* recognizer) | 在节点中移除手势。 |
| int32_t (*setGestureInterrupterToNode)(ArkUI_NodeHandle node, ArkUI_GestureInterruptResult (*interrupter)(ArkUI_GestureInterruptInfo* info)) | 设置节点手势打断回调。 |
| ArkUI_GestureRecognizerType (*getGestureType)(ArkUI_GestureRecognizer* recognizer) | 获取手势类别。 |
| int32_t (*setInnerGestureParallelTo)(ArkUI_NodeHandle node, void* userData, ArkUI_GestureRecognizer* (*parallelInnerGesture)(ArkUI_ParallelInnerGestureEvent* event)) | 设置并行内部手势事件回调。 |
| ArkUI_GestureRecognizer* (*createTapGestureWithDistanceThreshold)(int32_t countNum, int32_t fingersNum, double distanceThreshold) | 创建带移动范围限制的敲击手势。1. 支持单击、双击和多次点击事件的识别。  2. 当配置多击时，上一次的最后一根手指抬起和下一次的第一根手指按下的超时时间为300毫秒。  3. 当上次点击的位置与当前点击的位置距离超过60vp等效像素点时，手势识别失败。  4. 当配置多指时，第一根手指按下后300毫秒内未有足够的手指数按下，手势识别失败，  第一根手指抬起后300毫秒内未有足够的手指抬起，手势识别失败。  5. 实际点击手指数超过配置值，手势识别成功。  6. 当手指移动距离超出所设置的距离值时，手势识别失败。 |

**成员函数说明**

**createTapGesture()**

```ets
ArkUI_GestureRecognizer* (*createTapGesture)(int32_t countNum, int32_t fingersNum)
```

描述：

创建敲击手势。

1. 支持单击、双击和多次点击事件的识别。

1. 当配置多击时，上一次的最后一根手指抬起和下一次的第一根手指按下的超时时间为300毫秒。

1. 当上次点击的位置与当前点击的位置距离超过60vp等效像素点时，手势识别失败。

1. 当配置多指时，第一根手指按下后300毫秒内未有足够的手指数按下，手势识别失败，第一根手指抬起后300毫秒内未有足够的手指抬起，手势识别失败。

1. 实际点击手指数超过配置值，手势识别成功。

参数：

| 参数项 | 描述 |
| --- | --- |
| int32_t countNum | 识别的连续点击次数。当设置的值小于1或不设置时，会被转化为默认值 1。 |
| int32_t fingersNum | 触发点击的手指数，最小为1指， 最大为10指。当设置小于1的值或不设置时，会被转化为默认值 1。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_GestureRecognizer* | 返回创建的敲击手势指针。 |

**createLongPressGesture()**

```ets
ArkUI_GestureRecognizer* (*createLongPressGesture)(int32_t fingersNum, bool repeatResult, int32_t durationNum)
```

描述：

创建长按手势。1. 用于触发长按手势事件，触发长按手势的最少手指数为1，最短长按时间为500毫秒。

 2. 当组件默认支持可拖拽时，如Text、TextInput、TextArea、HyperLink、Image和RichEditor等组件。

 长按手势与拖拽会出现冲突，事件优先级如下：

 长按触发时间 < 500ms，长按事件优先拖拽事件响应。

 长按触发时间 >= 500ms，拖拽事件优先长按事件响应。

 3. 手指按下后若发生超过15px的移动，则判定当前长按手势识别失败。

参数：

| 参数项 | 描述 |
| --- | --- |
| int32_t fingersNum | 触发长按的最少手指数，最小为1指，最大取值为10指。超出取值范围时按照默认值1处理。 |
| bool repeatResult | 是否连续触发事件回调。 true：连续触发；false：不连续触发。 |
| int32_t durationNum | 触发长按的最短时间，单位为毫秒（ms）。设置小于等于0时，按照默认值500处理。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_GestureRecognizer* | 返回创建的敲击手势指针。 |

**createPanGesture()**

```ets
ArkUI_GestureRecognizer* (*createPanGesture)(int32_t fingersNum, ArkUI_GestureDirectionMask directions, double distanceNum)
```

描述：

创建滑动手势。1. 当滑动的最小距离超过设定的最小值时触发滑动手势事件。

 2. Tabs组件滑动与该滑动手势事件同时存在时，可将distanceNum值设为1，使拖动更灵敏，避免造成事件错乱。

参数：

| 参数项 | 描述 |
| --- | --- |
| int32_t fingersNum | 用于指定触发滑动的最少手指数，最小为1指，最大取值为10指。当设置的值小于1或不设置时，会被转化为默认值 1。 |
| ArkUI_GestureDirectionMask directions | 用于指定触发滑动的手势方向，此枚举值支持逻辑与(&)和逻辑或（|）运算。 |
| double distanceNum | 用于指定触发滑动手势事件的最小拖动距离，单位为px。当设定的值小于等于0时，按默认值5px处理。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_GestureRecognizer* | 返回创建的滑动手势指针。 |

**createPinchGesture()**

```ets
ArkUI_GestureRecognizer* (*createPinchGesture)(int32_t fingersNum, double distanceNum)
```

描述：

创建捏合手势。1. 触发捏合手势的最少手指为2指，最大为5指，最小识别距离为distanceNum 像素点。

 2. 触发手势手指可以多于fingersNum数目，但只有先落下的与fingersNum相同数目的手指参与手势计算。

参数：

| 参数项 | 描述 |
| --- | --- |
| int32_t fingersNum | 触发捏合的最少手指数，最小为2指，最大为5指。超出取值范围时按照默认值2处理。 |
| double distanceNum | 最小识别距离，单位为px。当设置识别距离的值小于等于0时，会被转化为默认值5px处理。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_GestureRecognizer* | 返回创建的手势指针。 |

**createRotationGesture()**

```ets
ArkUI_GestureRecognizer* (*createRotationGesture)(int32_t fingersNum, double angleNum)
```

描述：

创建旋转手势。1. 触发旋转手势的最少手指为2指，最大为5指，最小改变度数为1度。

 2. 触发手势手指可以多于fingersNum数目，但只有先落下的两指参与手势计算。

参数：

| 参数项 | 描述 |
| --- | --- |
| int32_t fingersNum | 触发旋转的最少手指数，最小为2指，最大为5指。超出取值范围时按照默认值2处理。 |
| double angleNum | 触发旋转手势的最小改变度数，单位为deg。默认值：1。当改变度数的值小于等于0或大于360时，会被转化为默认值 1。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_GestureRecognizer* | 返回创建的手势指针。 |

**createSwipeGesture()**

```ets
ArkUI_GestureRecognizer* (*createSwipeGesture)(int32_t fingersNum, ArkUI_GestureDirectionMask directions, double speedNum)
```

描述：

创建快滑手势。1. 用于触发快滑事件，滑动速度大于speedNum px/s时可识别成功。

参数：

| 参数项 | 描述 |
| --- | --- |
| int32_t fingersNum | 触发滑动的最少手指数，默认为1，最小为1指，最大为10指。 |
| ArkUI_GestureDirectionMask directions | 触发快滑手势的滑动方向。 |
| double speedNum | 识别滑动的最小速度，单位 px/s。当设置滑动速度的值小于等于0时，会被转化为默认值100px/s。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_GestureRecognizer* | 返回创建的手势指针。 |

**createGroupGesture()**

```ets
ArkUI_GestureRecognizer* (*createGroupGesture)(ArkUI_GroupGestureMode gestureMode)
```

描述：

创建手势组。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_GroupGestureMode gestureMode | 手势组模式。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_GestureRecognizer* | 返回创建的手势组指针。 |

**dispose()**

```ets
void (*dispose)(ArkUI_GestureRecognizer* recognizer)
```

描述：

销毁手势，释放资源。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_GestureRecognizer* recognizer | 指向自定义弹窗控制器的指针。 |

**addChildGesture()**

```ets
int32_t (*addChildGesture)(ArkUI_GestureRecognizer* group, ArkUI_GestureRecognizer* child)
```

描述：

手势组增加子手势。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_GestureRecognizer* group | 需要被关联子手势的手势组。 |
| ArkUI_GestureRecognizer* child | 子手势。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 0 - 成功。  401 - 参数错误。比如添加手势到非手势组对象内。 |

**removeChildGesture()**

```ets
int32_t (*removeChildGesture)(ArkUI_GestureRecognizer* group, ArkUI_GestureRecognizer* child)
```

描述：

删除子手势。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_GestureRecognizer* group | 需要被删除子手势的手势组。 |
| ArkUI_GestureRecognizer* child | 子手势。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 0 - 成功。  401 - 参数错误。 |

**setGestureEventTarget()**

```ets
int32_t (*setGestureEventTarget)(ArkUI_GestureRecognizer* recognizer, ArkUI_GestureEventActionTypeMask actionTypeMask, void* extraParams,void (*targetReceiver)(ArkUI_GestureEvent* event, void* extraParams))
```

描述：

创建手势关联回调方法。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_GestureRecognizer* recognizer | 需要被绑定回调事件的各类手势指针。 |
| ArkUI_GestureEventActionTypeMask actionTypeMask | 需要相应的手势事件类型集合，一次性可以注册多个回调，在回调中区分回调事件类型。例：actionTypeMask = GESTURE_EVENT_ACTION_ACCEPT | GESTURE_EVENT_ACTION_UPDATE; |
| void* extraParams | targetReceiver 回调时传入的上下文数据。 |
| targetReceiver | 对应注册手势类型的事件回调处理， event 返回手势回调数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 0 - 成功。  401 - 参数错误。 |

**addGestureToNode()**

```ets
int32_t (*addGestureToNode)(ArkUI_NodeHandle node, ArkUI_GestureRecognizer* recognizer, ArkUI_GesturePriority mode, ArkUI_GestureMask mask)
```

描述：

将手势添加到UI组件。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 需要被绑定手势的ArkUI组件节点指针。 |
| ArkUI_GestureRecognizer* recognizer | 绑定此节点的手势。 |
| ArkUI_GesturePriority mode | 标识此手势的模式。 |
| ArkUI_GestureMask mask | 手势屏蔽模式。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 0 - 成功。  401 - 参数错误。 |

**removeGestureFromNode()**

```ets
int32_t (*removeGestureFromNode)(ArkUI_NodeHandle node, ArkUI_GestureRecognizer* recognizer)
```

描述：

在节点中移除手势。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 需要被移除手势的节点指针。 |
| ArkUI_GestureRecognizer* recognizer | 需要被移除的手势。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 0 - 成功。  401 - 参数错误。 |

**setGestureInterrupterToNode()**

```ets
int32_t (*setGestureInterrupterToNode)(ArkUI_NodeHandle node, ArkUI_GestureInterruptResult (*interrupter)(ArkUI_GestureInterruptInfo* info))
```

描述：

设置节点手势打断回调。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 需要被设置手势打断回调的ArkUI节点指针。 |
| ArkUI_GestureInterruptResult (*interrupter)(ArkUI_GestureInterruptInfo* info) | 打断回调，info返回手势打断数据。interrupter返回GESTURE_INTERRUPT_RESULT_CONTINUE，手势正常进行；返回GESTURE_INTERRUPT_RESULT_REJECT，手势打断。设置此参数为nullptr时将取消注册回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 0 - 成功。  401 - 参数错误。 |

**getGestureType()**

```ets
ArkUI_GestureRecognizerType (*getGestureType)(ArkUI_GestureRecognizer* recognizer)
```

描述：

获取手势类别。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_GestureRecognizer* recognizer | 手势指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_GestureRecognizerType | 手势类型。 |

**setInnerGestureParallelTo()**

```ets
int32_t (*setInnerGestureParallelTo)(ArkUI_NodeHandle node, void* userData, ArkUI_GestureRecognizer* (*parallelInnerGesture)(ArkUI_ParallelInnerGestureEvent* event))
```

描述：

设置并行内部手势事件回调。

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 需要被设置并行内部手势事件回调的ArkUI节点指针。 |
| void* userData | 用户自定义数据。 |
| parallelInnerGesture | 并行内部手势事件，event 返回并行内部手势事件数据。parallelInnerGesture 返回 需要并行的手势识别器指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | ARKUI_ERROR_CODE_NO_ERROR - 成功。  ARKUI_ERROR_CODE_PARAM_INVALID - 参数错误。 |

**createTapGestureWithDistanceThreshold()**

```ets
ArkUI_GestureRecognizer* (*createTapGestureWithDistanceThreshold)(int32_t countNum, int32_t fingersNum, double distanceThreshold)
```

描述：

创建带移动范围限制的敲击手势。1. 支持单击、双击和多次点击事件的识别。

 2. 当配置多击时，上一次的最后一根手指抬起和下一次的第一根手指按下的超时时间为300毫秒。

 3. 当上次点击的位置与当前点击的位置距离超过60vp等效像素点时，手势识别失败。

 4. 当配置多指时，第一根手指按下后300毫秒内未有足够的手指数按下，手势识别失败，

 第一根手指抬起后300毫秒内未有足够的手指抬起，手势识别失败。

 5. 实际点击手指数超过配置值，手势识别成功。

 6. 当手指移动距离超出所设置的距离值时，手势识别失败。

参数：

| 参数项 | 描述 |
| --- | --- |
| int32_t countNum | 识别的连续点击次数。当设置的值小于1或不设置时，会被转化为默认值 1。 |
| int32_t fingersNum | 触发点击的手指数，最小为1指， 最大为10指。当设置小于1的值或不设置时，会被转化为默认值 1。 |
| double distanceThreshold | 手指允许的移动距离范围。当设置的值小于0或者不设置时，会被转化为默认值无穷大。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_GestureRecognizer* | 返回创建的敲击手势指针。 |