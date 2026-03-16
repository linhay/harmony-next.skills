# piece

 一种块状的入口，可包含图片和文本，常用于展示收件人。例如，邮件收件人或信息收件人。

 从API version 5开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

无

#### 属性

除支持[通用属性](通用属性.md)外，还支持如下属性：

名称类型必填描述contentstring是操作块文本内容。closableboolean否

设置当前操作块是否显示删除图标，当显示删除图标时，点击删除图标会触发close事件。

true表示显示删除图标，false表示不显示删除图标。默认为false。

iconstring否操作块删除图标的url，支持本地路径。

#### 样式

支持[通用样式](通用样式.md)。

 文本和图片默认在整个piece组件中居中。

#### 事件

除支持[通用事件](通用事件.md)外，还支持如下事件：

名称参数描述close-当piece组件点击删除图标触发，此时可以通过渲染属性if删除该组件。

#### 方法

支持[通用方法](通用方法.md)。

#### 示例

```ets
<!-- xxx.hml-->
<div class="container" >
  <piece if="{{first}}" content="example"></piece>
  <piece if="{{second}}" content="example" closable="true" onclose="closeSecond"></piece>
</div>
```

```ets
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  align-items: center;
  justify-content: center;
}
```

```ets
// xxx.js
export default {
  data: {
    first: true,
    second: true
  },
  closeSecond(e) {
    this.second = false;
  }
}
```