# Canvas组件错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](通用错误码.md)。

#### 103701 参数错误

**错误信息**

Parameter error.

**错误描述**

参数错误。

**可能原因**

参考报错接口的说明。

**处理步骤**

传入正确的参数。
#### 103702 绘制上下文未绑定Canvas组件
**错误信息**

The drawingContext is not bound to a canvas component.

**错误描述**

当前绘制上下文未绑定任何Canvas组件。

**可能原因**

当前绘制上下文没有绑定任何Canvas组件。

**处理步骤**

将绘制上下文绑定至一个Canvas组件后再调用[getContext2DFromDrawingContext](CanvasRenderingContext2D.md#ZH-CN_TOPIC_0000002553360789__getcontext2dfromdrawingcontext23)方法。