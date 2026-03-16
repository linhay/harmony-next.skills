[]()[]()

# canvas组件

 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

提供画布组件。用于自定义绘制图形。

[]()[]()

#### 权限列表

无

[]()[]()

#### 子组件

不支持。

[]()[]()

#### 属性

支持[通用属性](通用属性 (js-components-common-attributes).md)。

[]()[]()

#### 样式

支持[通用样式](通用样式 (js-components-common-styles).md)。

[]()[]()

#### 事件

支持[通用事件](通用事件 (js-components-common-events).md)。

[]()[]()

#### 方法

除支持[通用方法](../misc/通用方法.md)外，还支持如下方法：

[]()[]()

#### getContext

getContext(type: '2d', options?: ContextAttrOptions): CanvasRenderingContext2D

获取canvas绘图上下文。不支持在onInit和onReady中进行调用。

**参数：**

参数名参数类型必填描述typestring是设置为'2d'，返回值为2D绘制对象，该对象可用于在画布组件上绘制矩形、文本、图片等。options6+ContextAttrOptions否当前仅支持配置是否开启抗锯齿功能，默认为关闭。

**表1** ContextAttrOptions

参数名类型说明antialiasboolean是否开启抗锯齿功能，默认为false，表示不开启抗锯齿功能。

**返回值：**

类型说明[CanvasRenderingContext2D](CanvasRenderingContext2D对象 (js-components-canvas-canvasrenderingcontext2d).md)用于在画布组件上绘制矩形、文本、图片等。[]()[]()

#### toDataURL6+

toDataURL(type?: string, quality?: number): string

生成一个包含图片展示的URL。

**参数：**

参数名参数类型必填描述typestring否可选参数，用于指定图像格式，默认格式为image/png。qualitynumber否在指定图片格式为image/jpeg或image/webp的情况下，可以从0到1的区间内选择图片的质量。如果超出取值范围，将会使用默认值0.92。

**返回值：**

类型说明string图像的URL地址。[]()[]()

#### 示例

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas1" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
  <input type="button" style="width: 180px; height: 60px;" value="fillStyle" onclick="handleClick" />
</div>
```

```ets
// xxx.js
export default {
  handleClick() {
    const el = this.$refs.canvas1;
    var dataURL = el.toDataURL();
    console.info(dataURL);
    // "data:image/png;base64,xxxxxxxx..."
  }
}
```