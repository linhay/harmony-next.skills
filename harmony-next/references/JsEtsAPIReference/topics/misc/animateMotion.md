# animateMotion

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

路径动效。

**权限列表**

无

**子组件**

不支持。

**属性**

支持animate属性（values不生效）和以下表格中的属性。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| keyPoints | string | - | 是 | 一组关键帧的点位置，每帧的值为对象沿路径的距离比例。功能与animate属性中的values相同。 |
| path | string | - | 是 | 定义运动的路径，使用与path组件d属性相同的语法。 |
| rotate | [auto | auto-reverse | <number>] | auto | 否 | 设置动画对象的旋转方向。 |