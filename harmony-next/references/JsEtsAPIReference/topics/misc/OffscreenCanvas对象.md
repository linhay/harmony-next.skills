# OffscreenCanvas对象

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

 从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

可以离屏渲染的canvas对象。

**属性**

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| width | number | offscreen canvas对象的宽度。 |
| height | number | offscreen canvas对象的高度。 |

**方法**

**getContext**

getContext(contextId: string, options?: CanvasRenderingContext2DSettings): OffscreenCanvasRenderingContext2D

获取offscreen canvas绘图上下文，返回值为2D绘制对象。

参数：

| 参数名 | 参数类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| contextId | string | 是 | 仅支持 '2d'。 |
| options | CanvasRenderingContext2DSettings | 否 | 当前仅支持配置是否开启抗锯齿功能，默认为关闭。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| OffscreenCanvasRenderingContext2D | 2D绘制对象，用于在画布组件上绘制矩形、文本、图片等。 |

**CanvasRenderingContext2DSettings**

CanvasRenderingContext2DSettings(antialias?: boolean)

用来配置OffscreenCanvasRenderingContext2D对象的参数，包括是否开启抗锯齿。

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| antialias | boolean | 是否开启抗锯齿功能，默认为false，表示不开启抗锯齿功能。 |

**toDataURL**

toDataURL(type?: string, quality?:number): string

生成一个包含图片展示的URL。

参数：

| 参数名 | 参数类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| type | string | 否 | 可选参数，用于指定图像格式，默认格式为image/png。 |
| quality | number | 否 | 在指定图片格式为image/jpeg或image/webp的情况下，可以从0到1的区间内选择图片的质量。如果超出取值范围，将会使用默认值0.92。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| string | 图像的URL地址。 |

**transferToImageBitmap**

transferToImageBitmap(): ImageBitmap

在离屏画布最近渲染的图像上创建一个ImageBitmap对象。

返回值：

| 类型 | 说明 |
| --- | --- |
| ImageBitmap | 存储离屏画布上渲染的像素数据。 |

**示例**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvasId" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    var canvas = this.$refs.canvasId.getContext('2d');
    var offscreen = new OffscreenCanvas(500,500);
    var offscreenCanvasCtx = offscreen.getContext("2d");

    // ... some drawing for the canvas using the offscreenCanvasCtx ...

    var dataURL = offscreen.toDataURL();
    console.info(dataURL); //data:image/png;base64,xxxxxx

    var bitmap = offscreen.transferToImageBitmap();
    canvas.transferFromImageBitmap(bitmap);
  }
```