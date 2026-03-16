[]()[]()

# qrcode

 从API version 5开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

生成并显示二维码。

[]()[]()

#### 权限列表

无

[]()[]()

#### 子组件

不支持。

[]()[]()

#### 属性

除支持[通用属性](通用属性 (js-components-common-attributes).md)外，还支持如下属性：

名称类型默认值必填描述valuestring-是用来生成二维码的内容。typestringrect否

二维码类型。可能选项有：

- rect：矩形二维码。

- circle：圆形二维码。

[]()[]()

#### 样式

除支持[通用样式](通用样式 (js-components-common-styles).md)外，还支持如下样式：

名称类型默认值必填描述color<color>#000000否二维码颜色。background-color<color>#ffffff否二维码背景颜色。

-

width和height不一致时，取二者较小值作为二维码的边长。且最终生成的二维码居中显示。

-

width和height只设置一个时，取设置的值作为二维码的边长。都不设置时，使用200px作为默认边长。

-

生成二维码不可用时，请参考[Scan Kit(统一扫码服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-api)。

[]()[]()

#### 事件

支持[通用事件](通用事件 (js-components-common-events).md)。

[]()[]()

#### 方法

支持[通用方法](../misc/通用方法.md)。

[]()[]()

#### 示例

```ets
<!-- xxx.hml -->
<div class="container">
  <qrcode value="{{qr_value}}" type="{{qr_type}}"
  style="color: {{qr_col}};background-color: {{qr_bcol}};width: {{qr_size}};height: {{qr_size}};margin-bottom: 70px;"></qrcode>
  <text class="txt">Type</text>
  <switch showtext="true" checked="true" texton="rect" textoff="circle" onchange="setType"></switch>
  <text class="txt">Color</text>
  <select onchange="setCol">
    <option for="{{col_list}}" value="{{$item}}">{{$item}}</option>
  </select>
  <text class="txt">Background Color</text>
  <select onchange="setBCol">
    <option for="{{bcol_list}}" value="{{$item}}">{{$item}}</option>
  </select>
</div>
```

```ets
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.txt {
  margin: 30px;
  color: orangered;
}
select{
  margin-top: 40px;
  margin-bottom: 40px;
}
```

```ets
/* index.js */
export default {
  data: {
    qr_type: 'rect',
    qr_size: '300px',
    qr_col: '#87ceeb',
    col_list: ['#87ceeb','#fa8072','#da70d6','#80ff00ff','#00ff00ff'],
    qr_bcol: '#f0ffff',
    bcol_list: ['#f0ffff','#ffffe0','#d8bfd8']
  },
  setType(e) {
    if (e.checked) {
      this.qr_type = 'rect'
    } else {
      this.qr_type = 'circle'
    }
  },
  setCol(e) {
    this.qr_col = e.newValue
  },
  setBCol(e) {
    this.qr_bcol = e.newValue
  }
}
```