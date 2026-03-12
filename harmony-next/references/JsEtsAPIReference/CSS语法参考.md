# CSS语法参考

CSS是描述HML页面结构的样式语言。所有组件均存在系统默认样式，也可在页面CSS样式文件中对组件、页面自定义不同的样式。

#### 尺寸单位

1.

逻辑像素px（文档中以<length>表示）：

  1. 默认卡片具有的逻辑宽度为150px，实际显示时会将页面布局缩放至屏幕实际宽度，如100px在宽度为300的卡片上，实际渲染为200物理像素（从150px向300物理像素，所有尺寸放大2倍）。
  1. 额外配置autoDesignWidth为true时，逻辑像素px将按照屏幕密度进行缩放，如100px在屏幕密度为3的设备上，实际渲染为300物理像素。应用需要适配多种设备时，建议采用此方法。

1.

百分比（文档中以<percentage>表示）：表示该组件占父组件尺寸的百分比，如组件的width设置为50%，代表其宽度为父组件的50%。

#### 样式导入

为了模块化管理和代码复用，CSS样式文件支持 @import 语句，导入 CSS 文件。

#### 声明样式

每个页面目录下存在一个与布局hml文件同名的css文件，用来描述该hml页面中组件的样式，决定组件应该如何显示。

1.

内部样式，支持使用style、class属性来控制组件的样式。例如：

```ets
<!-- index.hml -->
<div class="container">
  <text style="color: red">Hello World</text>
</div>
```

```ets
/* index.css */
.container {
  justify-content: center;
}
```

1.

文件导入，合并外部样式文件。例如，在common目录中定义样式文件style.css，并在index.css中进行导入：

```ets
/* style.css */
.title {
  font-size: 50px;
}
```

```ets
/* index.css */
@import '../../common/style.css';
.container {
  justify-content: center;
}
```

#### 选择器

css选择器用于选择需要添加样式的元素，支持的选择器如下表所示：

选择器样例样例描述.class.container用于选择class="container"的组件。#id#titleId用于选择id="titleId"的组件。

示例：

```ets
<!-- 页面布局xxx.hml -->
<div id="containerId" class="container">
  <text id="titleId" class="title">标题</text>
  <div class="content">
    <text id="contentId">内容</text>
  </div>
</div>
```

```ets
/* 页面样式xxx.css */
/* 对class="title"的组件设置样式 */
.title {
  font-size: 30px;
}
/* 对id="contentId"的组件设置样式 */
#contentId {
  font-size: 20px;
}
```

#### 选择器优先级

选择器的优先级计算规则与w3c规则保持一致（只支持：内联样式，id，class），其中内联样式为在元素style属性中声明的样式。

当多条选择器声明匹配到同一元素时，各类选择器优先级由高到低顺序为：内联样式 > id > class 。