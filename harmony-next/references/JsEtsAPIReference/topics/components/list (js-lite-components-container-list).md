[]()[]()

# list

列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。

该组件从API version 4 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

[]()[]()

#### 子组件

仅支持<[list-item](list-item (js-lite-components-container-list-item).md)>。

[]()[]()

#### 属性

名称类型默认值必填描述idstring-否组件的唯一标识。stylestring-否组件的样式声明。classstring-否组件的样式类，用于引用样式表。refstring-否用来指定指向子元素的引用信息，该引用将注册到父组件的$refs 属性对象上。[]()[]()

#### 事件

名称参数描述scrollend-列表滑动已经结束。click-点击动作触发该事件。longpress-长按动作触发该事件。swipe5+[SwipeEvent](../misc/通用事件 (js-lite-common-events).md)组件上快速滑动后触发。scrolltop8+-当前列表已滑动到顶部位置。scrollbottom8+-当前列表已滑动到底部位置。[]()[]()

#### 样式

名称类型默认值必填描述flex-directionstringcolumn否

设置flex容器主轴的方向，指定flex项如何放置在flex容器中，可选值为：

- column：主轴为纵向。

- row：主轴为横向。

其他组件默认值为row，在list组件中默认值为column。轻量级智能穿戴设备不支持动态修改。

width<length> | <percentage>5+-否

设置组件自身的宽度。

未设置时组件宽度默认为0。

height<length> | <percentage>5+-否

设置组件自身的高度。

未设置时组件高度默认为0。

padding<length>0否

使用简写属性设置所有的内边距属性。

 该属性可以有1到4个值：

- 指定一个值时，该值指定四个边的内边距。

- 指定两个值时，第一个值指定上下两边的内边距，第二个指定左右两边的内边距。

- 指定三个值时，第一个指定上边的内边距，第二个指定左右两边的内边距，第三个指定下边的内边距。

- 指定四个值时分别为上、右、下、左边的内边距（顺时针顺序）。

padding-[left|top|right|bottom]<length>0否设置左、上、右、下内边距属性。margin<length> | <percentage>5+0否

使用简写属性设置所有的外边距属性，该属性可以有1到4个值。

- 只有一个值时，这个值会被指定给全部的四个边。

- 两个值时，第一个值被匹配给上和下，第二个值被匹配给左和右。

- 三个值时，第一个值被匹配给上, 第二个值被匹配给左和右，第三个值被匹配给下。

- 四个值时，会依次按上、右、下、左的顺序匹配 (即顺时针顺序)。

margin-[left|top|right|bottom]<length> | <percentage>5+0否设置左、上、右、下外边距属性。border-width<length>0否使用简写属性设置元素的所有边框宽度。border-color<color>black否使用简写属性设置元素的所有边框颜色。border-radius<length>-否border-radius属性是设置元素的外边框圆角半径。background-color<color>-否设置背景颜色。opacity5+number1否元素的透明度，取值范围为0到1，1表示为不透明，0表示为完全透明。displaystringflex否

确定一个元素所产生的框的类型，可选值为：

- flex：弹性布局。

- none：不渲染此元素。

[left|top]<length> | <percentage>6+-否

left|top确定元素的偏移位置。

- left属性规定元素的左边缘。该属性定义了定位元素左外边距边界与其包含块左边界之间的偏移。

- top属性规定元素的顶部边缘。该属性定义了一个定位元素的上外边距边界与其包含块上边界之间的偏移。

[]()[]()

#### 方法

名称参数描述scrollTo{ index: number(指定位置) }list滑动到指定index的item位置。rotation{ focus: boolean }控制list是否请求旋转表冠的焦点。设置focus参数为true，list将获取旋转表冠的焦点，允许用户通过旋转表冠来滚动选择器中的选项；设置为false将释放旋转表冠的焦点。[]()[]()

#### 示例

```ets
<!-- index.hml -->
<div class="container">
    <list class="todo-wrapper">
        <list-item for="{{todolist}}" class="todo-item">
            <div style="flex-direction: column;align-items: center;justify-content: center;">
                <text class="todo-title">{{$item.title}}</text>
                <text class="todo-title">{{$item.date}}</text>
            </div>
        </list-item>
    </list>
</div>
```

```ets
// index.js
export default {
    data: {
        todolist: [{
            title: '刷题',
            date: '2021-12-31 10:00:00',
        }, {
            title: '看电影',
            date: '2021-12-31 20:00:00',
        }
        , {
            title: '看书',
            date: '2021-12-31 21:00:00',
        },
        {
            title: '洗澡',
            date: '2021-12-31 22:00:00',
        },
        {
            title: '睡觉',
            date: '2021-12-31 23:00:00',
        }],
    },
    onShow() {
        this.$refs.listObj.rotation({focus: true})
    }
}
```

```ets
/* index.css */
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}
.todo-wrapper {
  width: 454px;
  height: 500px;
}
.todo-item {
  width: 454px;
  height: 80px;
  flex-direction: column;
}
.todo-title {
  width: 454px;
  height: 40px;
  text-align: center;
}
```