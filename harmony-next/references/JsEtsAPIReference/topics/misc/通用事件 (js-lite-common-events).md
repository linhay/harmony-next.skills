[]()[]()

# 通用事件

相对于私有事件，大部分组件都可以绑定如下事件。

名称参数描述click-点击动作触发该事件。longpress-长按动作触发该事件。swipe5+SwipeEvent组件上快速滑动后触发。

SwipeEvent 基础事件对象属性列表（继承BaseEvent）

属性类型说明directionstring

滑动方向，可能值有：

1. left：向左滑动；

2. right：向右滑动；

3. up：向上滑动；

4. down：向下滑动。