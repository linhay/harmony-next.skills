# Image对象

 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

图片对象。

#### 属性

属性类型默认值必填描述srcstring-是图片资源的路径。width<length>0px否图片的宽度。height<length>0px否图片的高度。onloadFunction-否图片加载成功后触发该事件，无参数。onerrorFunction-否图片加载失败后触发该事件，无参数。

#### 示例

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
        var ctx = el.getContext('2d');
        var img = new Image();
        // 图片路径建议放在common目录下
        img.src = 'common/images/example.jpg';
        img.onload = function () {
            console.log('Image load success');
            ctx.drawImage(img, 0, 0, 360, 250);
        };
        img.onerror = function () {
            console.error('Image load fail');
        };
    }
}
```