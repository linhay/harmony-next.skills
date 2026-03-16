# CanvasRenderingContext2D对象

 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

使用CanvasRenderingContext2D在canvas画布组件上进行绘制，绘制对象可以是矩形、文本、图片等。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas1" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
  <input type="button" style="width: 180px; height: 60px;" value="handleClick" onclick="handleClick" />
  <input type="button" style="width: 180px; height: 60px;" value="antialias" onclick="antialias" />
</div>
```

```ets
// xxx.js
export default {
  handleClick() {
    const el = this.$refs.canvas1;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.stroke();
  },
  antialias() {
    const el = this.$refs.canvas1;
    const ctx = el.getContext('2d', { antialias: true });
    ctx.beginPath();
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.stroke();
    }
  }
```

-

示意图（关闭抗锯齿）

-

示意图（开启抗锯齿）

#### 属性

名称类型描述[fillStyle](#ZH-CN_TOPIC_0000002529285005__fillstyle)<color> | [CanvasGradient](../graphics/CanvasGradient对象.md) | [CanvasPattern](../graphics/CanvasPattern.md)

指定绘制的填充色。

- 类型为<color>时，表示设置填充区域的颜色。

- 类型为CanvasGradient时，表示渐变对象，使用 createLinearGradient()方法创建。

- 类型为CanvasPattern时，使用 createPattern()方法创建。

[lineWidth](#ZH-CN_TOPIC_0000002529285005__linewidth)number设置绘制线条的宽度。[strokeStyle](#ZH-CN_TOPIC_0000002529285005__strokestyle)<color> | [CanvasGradient](../graphics/CanvasGradient对象.md) | CanvasPattern

设置描边的颜色。

- 类型为<color>时，表示设置描边使用的颜色。

- 类型为CanvasGradient时，表示渐变对象，使用 createLinearGradient()方法创建。

- 类型为CanvasPattern时，使用 createPattern()方法创建。

[lineCap](#ZH-CN_TOPIC_0000002529285005__linecap)string

指定线端点的样式，可选值为：

- butt：线端点以方形结束。

- round：线端点以圆形结束。

- square：线端点以方形结束，该样式下会增加一个长度和线段厚度相同，宽度是线段厚度一半的矩形。

默认值：butt

[lineJoin](#ZH-CN_TOPIC_0000002529285005__linejoin)string

指定线段间相交的交点样式，可选值为：

- round：在线段相连处绘制一个扇形，扇形的圆角半径是线段的宽度。

- bevel：在线段相连处使用三角形为底填充， 每个部分矩形拐角独立。

- miter：在相连部分的外边缘处进行延伸，使其相交于一点，形成一个菱形区域，该属性可以通过设置miterLimit属性展现效果。

默认值：miter

[miterLimit](#ZH-CN_TOPIC_0000002529285005__miterlimit)number

设置斜接面限制值，该值指定了线条相交处内角和外角的距离。

默认值：10

[font](#ZH-CN_TOPIC_0000002529285005__font)string

设置文本绘制中的字体样式。

语法：ctx.font="font-style font-weight font-size font-family"5+

- font-style(可选)，用于指定字体样式，支持如下几种样式：normal, italic。

- font-weight(可选)，用于指定字体的粗细，支持如下几种类型：normal, bold, bolder, lighter, 100, 200, 300, 400, 500, 600, 700, 800, 900。

- font-size(可选)，指定字号和行高，单位只支持px。

- font-family(可选)，指定字体系列，支持如下几种类型：sans-serif, serif, monospace。

默认值："normal normal 14px sans-serif"

[textAlign](#ZH-CN_TOPIC_0000002529285005__textalign)string

设置文本绘制中的文本对齐方式，可选值为：

- left：文本左对齐。

- right：文本右对齐。

- center：文本居中对齐。

- start：文本对齐界线开始的地方。

- end：文本对齐界线结束的地方。

ltr布局模式下start和left一致，rtl布局模式下start和right一致。

默认值：left

[textBaseline](#ZH-CN_TOPIC_0000002529285005__textbaseline)string

设置文本绘制中的水平对齐方式，可选值为：

- alphabetic：文本基线是标准的字母基线。

- top：文本基线在文本块的顶部。

- hanging：文本基线是悬挂基线。

- middle：文本基线在文本块的中间。

- ideographic：文字基线是表意字基线；如果字符本身超出了alphabetic 基线，那么ideographic基线位置在字符本身的底部。

- bottom：文本基线在文本块的底部。 与 ideographic 基线的区别在于 ideographic 基线不需要考虑下行字母。

默认值： alphabetic

[globalAlpha](#ZH-CN_TOPIC_0000002529285005__globalalpha)number设置透明度，0.0为完全透明，1.0为完全不透明。[lineDashOffset](#ZH-CN_TOPIC_0000002529285005__linedashoffset)number

设置画布的虚线偏移量，精度为float。

默认值：0.0

[globalCompositeOperation](#ZH-CN_TOPIC_0000002529285005__globalcompositeoperation)string

设置合成操作的方式。类型字段可选值有source-over，source-atop，source-in，source-out，destination-over，destination-atop，destination-in，destination-out，lighter，copy，xor。具体请参考[表 类型字段说明](#ZH-CN_TOPIC_0000002529285005__globalcompositeoperation)。

默认值：source-over

[shadowBlur](#ZH-CN_TOPIC_0000002529285005__shadowblur)number

设置绘制阴影时的模糊级别，值越大越模糊，精度为float。

默认值：0.0

[shadowColor](#ZH-CN_TOPIC_0000002529285005__shadowcolor)<color>设置绘制阴影时的阴影颜色。[shadowOffsetX](#ZH-CN_TOPIC_0000002529285005__shadowoffsetx)number设置绘制阴影时和原有对象的水平偏移值。[shadowOffsetY](#ZH-CN_TOPIC_0000002529285005__shadowoffsety)number设置绘制阴影时和原有对象的垂直偏移值。[imageSmoothingEnabled](#ZH-CN_TOPIC_0000002529285005__imagesmoothingenabled)boolean

用于设置绘制图片时是否进行图像平滑度调整，true为启用，false为不启用。

默认值：true

#### fillStyle

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```ets
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = '#0000ff';
    ctx.fillRect(20, 20, 150, 100);
  }
}
```

#### lineWidth

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```ets
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.lineWidth = 5;
    ctx.strokeRect(25, 25, 85, 105);
  }
}
```

#### strokeStyle

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```ets
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.lineWidth = 10;
    ctx.strokeStyle = '#0000ff';
    ctx.strokeRect(25, 25, 155, 105);
  }
}
```

#### lineCap

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```ets
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.lineWidth = 8;
    ctx.beginPath();
    ctx.lineCap = 'round';
    ctx.moveTo(30, 50);
    ctx.lineTo(220, 50);
    ctx.stroke();
  }
}
```

#### lineJoin

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```ets
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.lineWidth = 8;
    ctx.lineJoin = 'miter';
    ctx.moveTo(30, 30);
    ctx.lineTo(120, 60);
    ctx.lineTo(30, 110);
    ctx.stroke();
  }
}
```

#### miterLimit

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
</div>
```

```ets
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.lineWidth =14;
    ctx.lineJoin = 'miter';
    ctx.miterLimit = 3;
    ctx.moveTo(30, 30);
    ctx.lineTo(120, 60);
    ctx.lineTo(30, 70);
    ctx.stroke();
  }
}
```

#### font

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```ets
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.font = '30px sans-serif';
    ctx.fillText("Hello World", 20, 60);
  }
}
```

#### textAlign

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```ets
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.strokeStyle = '#0000ff';
    ctx.moveTo(140, 10);
    ctx.lineTo(140, 160);
    ctx.stroke();
    ctx.font = '18px sans-serif';
    // Show the different textAlign values
    ctx.textAlign = 'start';
    ctx.fillText('textAlign=start', 140, 60);
    ctx.textAlign = 'end';
    ctx.fillText('textAlign=end', 140, 80);
    ctx.textAlign = 'left';
    ctx.fillText('textAlign=left', 140, 100);
    ctx.textAlign = 'center';
    ctx.fillText('textAlign=center',140, 120);
    ctx.textAlign = 'right';
    ctx.fillText('textAlign=right',140, 140);
  }
}
```

#### textBaseline

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
</div>
```

```ets
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.strokeStyle = '#0000ff';
    ctx.moveTo(0, 120);
    ctx.lineTo(400, 120);
    ctx.stroke();
    ctx.font = '20px sans-serif';
    ctx.textBaseline = 'top';
    ctx.fillText('Top', 10, 120);
    ctx.textBaseline = 'bottom';
    ctx.fillText('Bottom', 55, 120);
    ctx.textBaseline = 'middle';
    ctx.fillText('Middle', 125, 120);
    ctx.textBaseline = 'alphabetic';
    ctx.fillText('Alphabetic', 195, 120);
    ctx.textBaseline = 'hanging';
    ctx.fillText('Hanging', 295, 120);
  }
}
```

#### globalAlpha

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```ets
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(0, 0, 50, 50);
    ctx.globalAlpha = 0.4;
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(50, 50, 50, 50);

  }
}
```

#### lineDashOffset

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```ets
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.setLineDash([10,20]);
    ctx.lineDashOffset = 10.0;
    ctx.stroke();
  }
}
```

#### globalCompositeOperation

类型字段说明。

值描述source-over在现有绘制内容上显示新绘制内容，属于默认值。source-atop在现有绘制内容顶部显示新绘制内容。source-in在现有绘制内容中显示新绘制内容。source-out在现有绘制内容之外显示新绘制内容。destination-over在新绘制内容上方显示现有绘制内容。destination-atop在新绘制内容顶部显示现有绘制内容。destination-in在新绘制内容中显示现有绘制内容。destination-out在新绘制内容外显示现有绘制内容。lighter显示新绘制内容和现有绘制内容。copy显示新绘制内容而忽略现有绘制内容。xor使用异或操作对新绘制内容与现有绘制内容进行融合。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```ets
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(20, 20, 50, 50);
    ctx.globalCompositeOperation = 'source-over';
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(50, 50, 50, 50);
    // Start drawing second example
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(120, 20, 50, 50);
    ctx.globalCompositeOperation = 'destination-over';
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(150, 50, 50, 50);
  }
}
```

 示例中，新绘制内容是蓝色矩形，现有绘制内容是红色矩形。

#### shadowBlur

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```ets
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.shadowBlur = 30;
    ctx.shadowColor = 'rgb(0,0,0)';
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(20, 20, 100, 80);
  }
}
```

#### shadowColor

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```ets
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.shadowBlur = 30;
    ctx.shadowColor = 'rgb(0,0,255)';
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(30, 30, 100, 100);
  }
}
```

#### shadowOffsetX

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```ets
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.shadowBlur = 10;
    ctx.shadowOffsetX = 20;
    ctx.shadowColor = 'rgb(0,0,0)';
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(20, 20, 100, 80);
  }
}
```

#### shadowOffsetY

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```ets
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.shadowBlur = 10;
    ctx.shadowOffsetY = 20;
    ctx.shadowColor = 'rgb(0,0,0)';
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(30, 30, 100, 100);
 }
}
```

#### imageSmoothingEnabled

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```ets
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var img = new Image();
    // 'common/image/example.jpg'需要替换为开发者所需的图像资源文件
    img.src = 'common/image/example.jpg';
    img.onload = function() {
    ctx.imageSmoothingEnabled = false;
    ctx.drawImage(img, 0, 0, 400, 200);
    };
  }
}
```

#### 方法

#### fillRect

fillRect(x: number, y: number, width:number, height: number): void

填充一个矩形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是指定矩形左上角点的x坐标。ynumber是指定矩形左上角点的y坐标。widthnumber是指定矩形的宽度。heightnumber是指定矩形的高度。

**示例：**

```ets
  <!-- xxx.hml -->
  <div>
    <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
  </div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillRect(20, 20, 200, 150);
  }
}
```

#### clearRect

clearRect(x: number, y: number, width:number, height: number): void

删除指定区域内的绘制内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是指定矩形上的左上角x坐标。ynumber是指定矩形上的左上角y坐标。widthnumber是指定矩形的宽度。heightnumber是指定矩形的高度。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(0, 0, 400, 200);
    ctx.clearRect(20, 20, 150, 100);
  }
}
```

#### strokeRect

strokeRect(x: number, y: number, width:number, height: number): void

绘制具有边框的矩形，矩形内部不填充。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是指定矩形的左上角x坐标。ynumber是指定矩形的左上角y坐标。widthnumber是指定矩形的宽度。heightnumber是指定矩形的高度。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.strokeRect(30, 30, 200, 150);
  }
}
```

#### fillText

fillText(text: string, x: number, y: number): void

绘制填充类文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明textstring是需要绘制的文本内容。xnumber是需要绘制的文本的左下角x坐标。ynumber是需要绘制的文本的左下角y坐标。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.font = '35px sans-serif';
    ctx.fillText("Hello World!", 10, 60);
  }
}
```

#### strokeText

strokeText(text: string, x: number, y: number): void

绘制描边类文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明textstring是需要绘制的文本内容。xnumber是需要绘制的文本的左下角x坐标。ynumber是需要绘制的文本的左下角y坐标。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.font = '25px sans-serif';
    ctx.strokeText("Hello World!", 10, 60);
  }
}
```

#### measureText

measureText(text: string): TextMetrics

该方法返回一个文本测算的对象，通过该对象可以获取指定文本的宽度值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明textstring是需要进行测量的文本。

**返回值：**

类型说明TextMetrics包含指定字体的宽度，该宽度可以通过TextMetrics.width来获取。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.font = '20px sans-serif';
    var txt = 'Hello World';
    ctx.fillText("width:" + ctx.measureText(txt).width, 20, 60);
    ctx.fillText(txt, 20, 110);
  }
}
```

#### stroke

stroke(): void

进行边框绘制操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.moveTo(25, 25);
    ctx.lineTo(25, 250);
    ctx.lineWidth = '6';
    ctx.strokeStyle = 'rgb(0,0,255)';
    ctx.stroke();
  }
}
```

#### beginPath

beginPath(): void

创建一个新的绘制路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.lineWidth = '6';
    ctx.strokeStyle = '#0000ff';
    ctx.moveTo(15, 80);
    ctx.lineTo(280, 80);
    ctx.stroke();
  }
}
```

#### moveTo

moveTo(x: number, y: number): void

路径从当前点移动到指定点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是

指定位置的x坐标。

单位：vp

ynumber是

指定位置的y坐标。

单位：vp

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(10, 10);
    ctx.lineTo(280, 160);
    ctx.stroke();
  }
}
```

#### lineTo

lineTo(x: number, y: number): void

从当前点到指定点进行路径连接。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是

指定位置的x坐标。

单位：vp

ynumber是

指定位置的y坐标。

单位：vp

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(10, 10);
    ctx.lineTo(280, 160);
    ctx.stroke();
  }
}
```

#### closePath

closePath(): void

结束当前路径形成一个封闭路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(30, 30);
    ctx.lineTo(110, 30);
    ctx.lineTo(70, 90);
    ctx.closePath();
    ctx.stroke();
  }
}
```

#### createPattern

createPattern(image: Image, repetition: string): Object

通过指定图像和重复方式创建图片填充的模板。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明imageImage是图源对象，具体参考[Image对象](../graphics/Image对象.md)。repetitionstring是设置图像重复的方式，取值为：'repeat'、'repeat-x'、 'repeat-y'、'no-repeat'。

**返回值：**

类型说明Object指定图像填充的Pattern对象。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 1000px; height: 1000px;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var img = new Image();
    // 'common/images/example.jpg'需要替换为开发者所需的图像资源文件
    img.src = 'common/images/example.jpg';
    var pat = ctx.createPattern(img, 'repeat');
    ctx.fillStyle = pat;
    ctx.fillRect(0, 0, 500, 500);
  }
}
```

#### bezierCurveTo

bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void

创建三次贝塞尔曲线的路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明cp1xnumber是第一个贝塞尔参数的x坐标值。cp1ynumber是第一个贝塞尔参数的y坐标值。cp2xnumber是第二个贝塞尔参数的x坐标值。cp2ynumber是第二个贝塞尔参数的y坐标值。xnumber是路径结束时的x坐标值。ynumber是路径结束时的y坐标值。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(10, 10);
    ctx.bezierCurveTo(20, 100, 200, 100, 200, 20);
    ctx.stroke();
  }
}
```

#### quadraticCurveTo

quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void

创建二次贝塞尔曲线的路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明cpxnumber是贝塞尔参数的x坐标值。cpynumber是贝塞尔参数的y坐标值。xnumber是路径结束时的x坐标值。ynumber是路径结束时的y坐标值。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(20, 20);
    ctx.quadraticCurveTo(100, 100, 200, 20);
    ctx.stroke();
  }
}
```

#### arc

arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void

绘制弧线路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是弧线圆心的x坐标值。ynumber是弧线圆心的y坐标值。radiusnumber是弧线的圆半径。startAnglenumber是弧线的起始弧度。endAnglenumber是弧线的终止弧度。counterclockwiseboolean否

是否逆时针绘制圆弧，true为逆时针，false为顺时针。

默认值：false

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.stroke();
  }
}
```

#### arcTo

arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void

依据圆弧经过的点和圆弧半径创建圆弧路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明x1number是圆弧经过的第一个点的x坐标值。y1number是圆弧经过的第一个点的y坐标值。x2number是圆弧经过的第二个点的x坐标值。y2number是圆弧经过的第二个点的y坐标值。radiusnumber是圆弧的圆半径值。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.moveTo(100, 20);
    ctx.arcTo(150, 20, 150, 70, 50); // Create an arc
    ctx.stroke();
  }
}
```

#### ellipse

ellipse(x: number, y: number, radiusX: number, radiusY: number, rotation: number, startAngle: number, endAngle: number, counterclockwise?: number): void

在规定的矩形区域绘制一个椭圆。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是椭圆圆心的x轴坐标。ynumber是椭圆圆心的y轴坐标。radiusXnumber是椭圆x轴的半径长度。radiusYnumber是椭圆y轴的半径长度。rotationnumber是椭圆的旋转角度，单位为弧度。startAnglenumber是椭圆绘制的起始点角度，以弧度表示。endAnglenumber是椭圆绘制的结束点角度，以弧度表示。counterclockwisenumber否

是否以逆时针方向绘制椭圆，0为顺时针，1为逆时针。其它数值均按默认值处理。

默认值：0

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.ellipse(200, 200, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI, 1);
    ctx.stroke();
  }
}
```

#### rect

rect(x: number, y: number, width: number, height: number): void

创建矩形路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是指定矩形的左上角x坐标值。ynumber是指定矩形的左上角y坐标值。widthnumber是指定矩形的宽度。heightnumber是指定矩形的高度。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
    ctx.stroke(); // Draw it
  }
}
```

#### fill

fill(): void

对封闭路径进行填充。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
    ctx.fill(); // Draw it in default setting
  }
}
```

#### clip

clip(): void

设置当前路径为剪切路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.rect(0, 0, 200, 200);
    ctx.stroke();
    ctx.clip();
    // Draw red rectangle after clip
    ctx.fillStyle = "rgb(255,0,0)";
    ctx.fillRect(0, 0, 150, 150);
  }
}
```

#### rotate

rotate(rotate: number): void

针对当前坐标轴进行顺时针旋转。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明rotatenumber是设置顺时针旋转的弧度值，可以通过Math.PI / 180将角度转换为弧度值。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.rotate(45 * Math.PI / 180); // Rotate the rectangle 45 degrees
    ctx.fillRect(70, 20, 50, 50);
  }
}
```

#### scale

scale(x: number, y: number): void

设置canvas画布的缩放变换属性，后续的绘制操作将按照缩放比例进行缩放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是设置水平方向的缩放值。ynumber是设置垂直方向的缩放值。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.strokeRect(10, 10, 25, 25);
    ctx.scale(2, 2);// Scale to 200%
    ctx.strokeRect(10, 10, 25, 25);
  }
}
```

#### transform

transform(scaleX: number, skewX: number, skewY: number, scale: number, translateX: number, translateY: number): void

transform方法对应一个变换矩阵，想对一个图形进行变化的时候，只要设置此变换矩阵相应的参数，对图形的各个定点的坐标分别乘以这个矩阵，就能得到新的定点的坐标。矩阵变换效果可叠加。

 变换后的坐标计算方式（x和y为变换前坐标，x'和y'为变换后坐标）：

-

x' = scaleX * x + skewY * y + translateX

-

y' = skewX * x + scaleY * y + translateY

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明scaleXnumber是指定水平缩放值。skewXnumber是指定水平倾斜值。skewYnumber是指定垂直倾斜值。scaleYnumber是指定垂直缩放值。translateXnumber是指定水平移动值。translateYnumber是指定垂直移动值。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = 'rgb(0,0,0)';
    ctx.fillRect(0, 0, 100, 100);
    ctx.transform(1, 0.5, -0.5, 1, 10, 10);
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(0, 0, 100, 100);
    ctx.transform(1, 0.5, -0.5, 1, 10, 10);
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(0, 0, 100, 100);
  }
}
```

#### setTransform

setTransform(scaleX: number, skewX: number, skewY: number, scale: number, translateX: number, translateY: number): void

setTransform方法使用的参数和transform()方法相同，但setTransform()方法会重置现有的变换矩阵并创建新的变换矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明scaleXnumber是指定水平缩放值。skewXnumber是指定水平倾斜值。skewYnumber是指定垂直倾斜值。scaleYnumber是指定垂直缩放值。translateXnumber是指定水平移动值。translateYnumber是指定垂直移动值。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(0, 0, 100, 100);
    ctx.setTransform(1,0.5, -0.5, 1, 10, 10);
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(0, 0, 100, 100);
  }
}
```

#### translate

translate(x: number, y: number): void

移动当前坐标系的原点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是设置水平平移量。ynumber是设置竖直平移量。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillRect(10, 10, 50, 50);
    ctx.translate(70, 70);
    ctx.fillRect(10, 10, 50, 50);
  }
}
```

#### createPath2D6+

createPath2D(path: Path2D, cmds: string): Path2D

创建一个Path2D对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明pathPath2D是Path2D对象。cmdsstring是SVG的Path描述字符串。

**返回值：**

[Path2D对象](../graphics/Path2D对象.md)

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path1 = ctx.createPath2D();
    path1.moveTo(100, 100);
    path1.lineTo(200, 100);
    path1.lineTo(100, 200);
    path1.closePath();
    ctx.stroke(path1);
    var path2 = ctx.createPath2D("M150 150 L50 250 L250 250 Z");
    ctx.stroke(path2);
    var path3 = ctx.createPath2D(path2);
    ctx.stroke(path3);
  }
}
```

#### drawImage

drawImage(image: Image | PixelMap, sx: number, sy: number, sWidth: number, sHeight: number, dx: number, dy: number, dWidth: number, dHeight: number):void

进行图像绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明imageImage | PixelMap9+是图片资源，请参考[Image对象](../graphics/Image对象.md) 或[PixelMap对象](../../types/interfaces/Interface (PixelMap).md)。sxnumber是裁切源图像时距离源图像左上角的x坐标值。synumber是裁切源图像时距离源图像左上角的y坐标值。sWidthnumber是裁切源图像时需要裁切的宽度。sHeightnumber是裁切源图像时需要裁切的高度。dxnumber是绘制区域左上角在x轴的位置。dynumber是绘制区域左上角在y 轴的位置。dWidthnumber是绘制区域的宽度。dHeightnumber是绘制区域的高度。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    var test = this.$refs.canvas;
    var ctx = test.getContext('2d');
    var img = new Image();
    // 'common/image/test.jpg'需要替换为开发者所需的图像资源文件
    img.src = 'common/image/test.jpg';
    ctx.drawImage(img, 0, 0, 200, 200, 10, 10, 200, 200);
  }
}
```

#### restore

restore(): void

对保存的绘图上下文进行恢复。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.restore();
  }
}
```

#### save

save(): void

对当前的绘图上下文进行保存。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.save();
  }
}
```

#### createLinearGradient6+

createLinearGradient(x0: number, y0: number, x1: number, y1: number): Object

创建一个线性渐变色，返回CanvasGradient对象，请参考[CanvasGradient对象](../graphics/CanvasGradient对象.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明x0number是起点的x轴坐标。y0number是起点的y轴坐标。x1number是终点的x轴坐标。y1number是终点的y轴坐标。

**返回值：**

类型说明Object返回创建的CanvasGradient对象。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
  <input type="button" style="width: 180px; height: 60px;" value="fillStyle" onclick="handleClick" />
</div>
```

```ets
// xxx.js
export default {
  handleClick() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    // Linear gradient: start(50,0) end(300,100)
    var gradient = ctx.createLinearGradient(50,0, 300,100);
    // Add three color stops
    gradient.addColorStop(0.0, '#ff0000');
    gradient.addColorStop(0.5, '#ffffff');
    gradient.addColorStop(1.0, '#00ff00');
    // Set the fill style and draw a rectangle
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, 500, 500);
  }
}
```

#### createRadialGradient6+

createRadialGradient(x0: number, y0: number, r0: number, x1: number, y1: number, r1: number): Object

创建一个径向渐变色，返回CanvasGradient对象，请参考CanvasGradient。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明x0number是起始圆的x轴坐标。y0number是起始圆的y轴坐标。r0number是起始圆的半径。必须是非负且有限的。x1number是终点圆的x轴坐标。y1number是终点圆的y轴坐标。r1number是终点圆的半径。必须为非负且有限的。

**返回值：**

类型说明Object返回创建的CanvasGradient对象。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
  <input type="button" style="width: 180px; height: 60px;" value="fillStyle" onclick="handleClick" />
</div>
```

```ets
// xxx.js
export default {
  handleClick() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    // Radial gradient: inner circle(200,200,r:50) outer circle(200,200,r:200)
    var gradient = ctx.createRadialGradient(200,200,50, 200,200,200);
    // Add three color stops
    gradient.addColorStop(0.0, '#ff0000');
    gradient.addColorStop(0.5, '#ffffff');
    gradient.addColorStop(1.0, '#00ff00');
    // Set the fill style and draw a rectangle
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, 500, 500);
  }
}
```

#### createImageData

createImageData(width: number, height: number): ImageData

创建新的、空白的、指定大小的ImageData对象，请参考[ImageData对象](../graphics/ImageData对象.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明widthnumber是ImageData的宽度。heightnumber是ImageData的高度。

**返回值：**

类型说明[ImageData](../graphics/ImageData对象.md)返回创建的ImageData对象。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var imageData = ctx.createImageData(50, 100);  // Create ImageData with 50px width and 100px height
  }
}
```

#### createImageData

createImageData(imageData: ImageData): ImageData

根据一个现有的ImageData对象，重新创建一个宽、高相同但不会复制图像数据的ImageData对象，请参考[ImageData对象](../graphics/ImageData对象.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明imageData[ImageData](../graphics/ImageData对象.md)是复制现有的ImageData对象。

**返回值：**

类型说明[ImageData](../graphics/ImageData对象.md)返回创建的ImageData对象。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var imageData = ctx.createImageData(50, 100);  // Create ImageData with 50px width and 100px height
    var newImageData = ctx.createImageData(imageData);  // Create ImageData using the input imageData
  }
}
```

#### getImageData

getImageData(sx: number, sy: number, sw: number, sh: number): ImageData

以当前canvas指定区域内的像素创建[ImageData对象](../graphics/ImageData对象.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明sxnumber是需要输出的区域的左上角x坐标。synumber是需要输出的区域的左上角y坐标。swnumber是需要输出的区域的宽度。shnumber是需要输出的区域的高度。

**返回值：**

类型说明[ImageData](../graphics/ImageData对象.md)返回包含指定区域像素的ImageData对象。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas id="getImageData" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const test = this.$element('getImageData')
    const ctx = test.getContext('2d');
    var imageData = ctx.getImageData(0, 0, 280, 300);
  }
}
```

#### putImageData

putImageData(imageData: ImageData, dx: number, dy: number, dirtyX: number, dirtyY: number, dirtyWidth: number, dirtyHeight: number): void

使用ImageData数据裁剪后填充至新的矩形区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明imageData[ImageData](../graphics/ImageData对象.md)是包含像素值的ImageData对象。dxnumber是填充区域在x轴方向的偏移量。dynumber是填充区域在y轴方向的偏移量。dirtyXnumber是源图像数据矩形裁切范围左上角距离源图像左上角的x轴偏移量。dirtyYnumber是源图像数据矩形裁切范围左上角距离源图像左上角的y轴偏移量。dirtyWidthnumber是源图像数据矩形裁切范围的宽度。dirtyHeightnumber是源图像数据矩形裁切范围的高度。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas id="putImageData" style="width: 200px; height: 150px; background-color: #D5D5D5;"></canvas>
</div>
```

```ets
//xxx.js
export default {
    onShow() {
        const test = this.$element('putImageData')
        const ctx = test.getContext('2d');
        var imgData = ctx.createImageData(100, 100);
        for (var i = 0; i < imgData.data.length; i += 4) {
            imgData.data[i + 0] = 39;
            imgData.data[i + 1] = 135;
            imgData.data[i + 2] = 217;
            imgData.data[i + 3] = 255;
        }
        ctx.putImageData(imgData, 10, 10, 0, 0, 100, 50);
    }
}
```

#### putImageData

putImageData(imageData: ImageData, dx: number, dy: number): void

使用ImageData数据填充新的矩形区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明imageData[ImageData](../graphics/ImageData对象.md)是包含像素值的ImageData对象。dxnumber是填充区域在x轴方向的偏移量。dynumber是填充区域在y轴方向的偏移量。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas id="putImageData" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const test = this.$element('putImageData')
    const ctx = test.getContext('2d');
    var imgData = ctx.createImageData(100, 100);
    for (var i = 0; i < imgData.data.length; i += 4) {
      imgData.data[i + 0] = 255;
      imgData.data[i + 1] = 0;
      imgData.data[i + 2] = 0;
      imgData.data[i + 3] = 255;
  }
    ctx.putImageData(imgData, 10, 10);
  }
}
```

#### getPixelMap9+

getPixelMap(sx: number, sy: number, sw: number, sh: number): PixelMap

获取用当前canvas指定区域内的像素创建的PixelMap对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明sxnumber是指定区域的左上角x坐标。synumber是指定区域的左上角y坐标。swnumber是指定区域的宽度。shnumber是指定区域的高度。

**返回值：**

类型说明[PixelMap](../../types/interfaces/Interface (PixelMap).md)返回包含指定区域像素的PixelMap对象。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas id="canvasId" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const test = this.$element('canvasId')
    const ctx = test.getContext('2d');
    var pixelMap = ctx.getPixelMap(0, 0, 280, 300);
  }
}
```

#### setLineDash

setLineDash(segments: Array): void

设置画布的虚线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明segmentsArray是作为数组用来描述线段如何交替和间距长度。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.setLineDash([10,20]);
    ctx.stroke();
  }
}
```

#### getLineDash

getLineDash(): Array

获得当前画布的虚线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明Array返回数组，该数组用来描述线段如何交替和间距长度。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var info = ctx.getLineDash();
  }
}
```

#### transferFromImageBitmap7+

transferFromImageBitmap(bitmap: ImageBitmap): void

显示给定的[ImageBitmap对象](../graphics/ImageBitmap对象.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明bitmap[ImageBitmap](../graphics/ImageBitmap对象.md)是待显示的ImageBitmap对象。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
</div>
```

```ets
//xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var canvas = this.$refs.canvas.getContext('2d');
    var offscreen = new OffscreenCanvas(500,500);
    var offscreenCanvasCtx = offscreen.getContext("2d");
    offscreenCanvasCtx.fillRect(0, 0, 200, 200);

    var bitmap = offscreen.transferToImageBitmap();
    canvas.transferFromImageBitmap(bitmap);
  }
}
```