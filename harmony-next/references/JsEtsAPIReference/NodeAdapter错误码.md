# NodeAdapter错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](通用错误码.md)。

#### 106104 适配器未绑定

**错误信息**

The lazy loading adapter is not bound to the component.

**错误描述**

组件未设置NodeAdapter。

**可能原因**

组件未设置NodeAdapter。

**处理步骤**

为组件设置NodeAdapter。

#### 106105 适配器已存在

**错误信息**

The adapter already exists.

**错误描述**

NodeAdapter已经存在。

**可能原因**

NodeAdapter已经存在，不支持添加删除子节点。

**处理步骤**

移除NodeAdapter，或放弃在此处添加删除子节点。

#### 106106 子节点已存在

**错误信息**

The corresponding node already has a child node and cannot add an adapter.

**错误描述**

组件已经有子节点

**可能原因**

组件已经有子节点，不支持设置NodeAdapter。

**处理步骤**

移除子节点，或放弃在此处设置NodeAdapter。

#### 106107 参数下标越界

**错误信息**

The parameter length in the parameter event exceeds the limit.

**错误描述**

组件事件中index参数超过数组长度限制。

**可能原因**

传入的index参数超出传入的数组长度限制。

**处理步骤**

检查index参数是否超出传入的数组长度限制。

#### 106108 数据不存在

**错误信息**

The data does not exist in the component event.

**错误描述**

组件事件中不存在该数据。

**可能原因**

试图查找事件中不包含的数据。

**处理步骤**

确认当前事件是否存在想要查询的数据。

#### 106109 不支持返回值

**错误信息**

The component event does not support return values.

**错误描述**

组件事件不支持返回值。

**可能原因**

试图获取事件返回值。

**处理步骤**

确认当前事件是否存在返回值。

#### 106110 暂不支持该事件类型

**错误信息**

The event type is not supported.

**错误描述**

注册通用事件时传入的事件类型错误。

**可能原因**

传入的事件类型参数错误，不在已支持的事件类型中。

**处理步骤**

检查函数入参的事件类型的具体值。