# dialog

 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

自定义弹窗容器。

#### 权限列表

无

#### 子组件

支持单个子组件。

#### 属性

除支持[通用属性](通用属性.md)外，支持如下属性：

名称类型默认值必填描述dragable7+booleanfalse否设置对话框是否支持拖拽。true表示支持拖拽，false表示不支持拖拽。

 弹窗类组件不支持focusable、click-effect属性。

#### 样式

仅支持[通用样式](通用样式.md)中的width、height、margin、margin-[left | top | right | bottom]、margin-[start | end]样式。

#### 事件

不支持[通用事件](通用事件.md)，仅支持如下事件：

名称参数描述cancel-用户点击非dialog区域触发取消弹窗时触发的事件。show7+-对话框弹出时触发该事件。close7+-对话框关闭时触发该事件。

#### 方法

不支持[通用方法](通用方法.md)，仅支持如下方法。

名称参数描述show-弹出对话框。close-关闭对话框。

 dialog属性、样式均不支持动态更新。

#### 示例

```ets
<!-- xxx.hml -->
<div class="doc-page">
  <div class="btn-div">
    <button type="capsule" value="Click here" class="btn" onclick="showDialog"></button>
  </div>
  <dialog id="simpledialog" dragable="true" class="dialog-main" oncancel="cancelDialog">
    <div class="dialog-div">
      <div class="inner-txt">
        <text class="txt" ondoubleclick="doubleclick">Simple dialog</text>
      </div>
      <div class="inner-btn">
        <button type="capsule" value="Cancel" onclick="cancelSchedule" class="btn-txt"></button>
        <button type="capsule" value="Confirm" onclick="setSchedule" class="btn-txt"></button>
      </div>
    </div>
  </dialog>
</div>
```

```ets
/* xxx.css */
.doc-page {
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.btn-div {
  width: 100%;
  height: 200px;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.btn {
  background-color: #F2F2F2;
  text-color: #0D81F2;
}
.txt {
  color: #000000;
  font-weight: bold;
  font-size: 39px;
}
.dialog-main {
  width: 500px;
}
.dialog-div {
  flex-direction: column;
  align-items: center;
}
.inner-txt {
  width: 400px;
  height: 160px;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
}
.inner-btn {
  width: 400px;
  height: 120px;
  justify-content: space-around;
  align-items: center;
}
.btn-txt {
  background-color: #F2F2F2;
  text-color: #0D81F2;
}
```

```ets
// xxx.js
import promptAction from '@ohos.promptAction';
export default {
  showDialog() {
    this.$element('simpledialog').show()
  },
  cancelDialog() {
    promptAction.showToast({
      message: 'Dialog cancelled'
    })
  },
  cancelSchedule() {
    this.$element('simpledialog').close()
    promptAction.showToast({
      message: 'Successfully cancelled'
    })
  },
  setSchedule() {
    this.$element('simpledialog').close()
    promptAction.showToast({
      message: 'Successfully confirmed'
    })
  },
  doubleclick(){
    promptAction.showToast({
      message: 'doubleclick'
    })
  }
}
```