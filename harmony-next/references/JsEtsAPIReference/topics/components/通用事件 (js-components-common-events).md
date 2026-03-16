[]()[]()

# 通用事件

 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

[]()[]()

#### 事件说明

-

事件绑定在组件上，当组件达到事件触发条件时，会执行JS中对应的事件回调函数，实现页面UI视图和页面JS逻辑层的交互。

-

事件回调函数中通过参数可以携带额外的信息，如组件上的数据对象dataset，事件特有的回调参数。

相对于私有事件，大部分组件都可以绑定如下事件。

名称参数描述是否支持冒泡是否支持捕获touchstartTouchEvent手指刚触摸屏幕时触发该事件。TouchEvent具体可参考表2。是5+是5+touchmoveTouchEvent手指触摸屏幕后移动时触发该事件。是5+是5+touchcancelTouchEvent手指触摸屏幕中动作被打断时触发该事件。是5+是5+touchendTouchEvent手指触摸结束离开屏幕时触发该事件。是5+是5+clickBaseEvent点击动作触发该事件。是6+否doubleclick7+BaseEvent双击动作触发该事件。

否

 从API Version 9 开始支持冒泡。

否longpressBaseEvent长按动作触发该事件。

否

从API Version 9 开始支持冒泡。

否swipe5+SwipeEvent组件上快速滑动后触发该事件。 SwipeEvent具体可参考表4 。

否

从API Version 9 开始支持冒泡。

否attached6+-当前组件节点挂载在渲染树后触发。否否detached6+-当前组件节点从渲染树中移除后触发。否否pinchstart7+PinchEvent

手指开始执行捏合操作时触发该事件。

PinchEvent具体可参考表5。

否否pinchupdate7+PinchEvent手指执行捏合操作过程中触发该事件。否否pinchend7+PinchEvent手指捏合操作结束离开屏幕时触发该事件。否否pinchcancel7+PinchEvent手指捏合操作被打断时触发该事件。否否dragstart7+DragEvent

用户开始拖拽时触发该事件。

DragEvent具体可参考表6。

否否drag7+DragEvent拖拽过程中触发该事件。否否dragend7+DragEvent用户拖拽完成后触发。否否dragenter7+DragEvent进入释放目标时触发该事件。否否dragover7+DragEvent在释放目标内拖动时触发。否否dragleave7+DragEvent离开释放目标区域时触发。否否drop7+DragEvent在可释放目标区域内释放时触发。否否

 除上述事件外，其他事件均为非冒泡事件，如[input的change事件](input (js-components-basic-input).md#ZH-CN_TOPIC_0000002529284991__事件)，详见各个组件。

**表1** BaseEvent对象属性列表

属性类型说明typestring当前事件的类型，比如click、longpress等。timestampnumber该事件触发时的时间戳。deviceId8+number触发该事件的设备ID信息。target12+[Target](#ZH-CN_TOPIC_0000002529284975__target对象6)触发该事件的目标对象。

**表2** TouchEvent对象属性列表(继承BaseEvent)

属性类型说明touchesArray<TouchInfo>触摸事件时的属性集合，包含屏幕触摸点的信息数组。changedTouchesArray<TouchInfo>触摸事件时的属性集合，包括产生变化的屏幕触摸点的信息数组。数据格式和touches一样。该属性表示有变化的触摸点，如从无变有，位置变化，从有变无。例如用户手指刚接触屏幕时，touches数组中有数据，但changedTouches无数据。

**表3** TouchInfo

属性类型说明globalXnumber距离屏幕左上角（不包括状态栏）横向距离。屏幕的左上角为原点。globalYnumber距离屏幕左上角（不包括状态栏）纵向距离。屏幕的左上角为原点。localXnumber距离被触摸组件左上角横向距离。组件的左上角为原点。localYnumber距离被触摸组件左上角纵向距离。组件的左上角为原点。sizenumber触摸接触面积。force6+number接触力信息。

**表4** SwipeEvent 基础事件对象属性列表（继承BaseEvent）

属性类型说明directionstring

滑动方向，可能值有：

- left：向左滑动；

- right：向右滑动；

- up：向上滑动；

- down：向下滑动。

distance6+number在滑动方向上的滑动距离。

**表5** PinchEvent 对象属性列表7+

属性类型说明scalenumber缩放比例。pinchCenterXnumber捏合中心点X轴坐标，单位px。pinchCenterYnumber捏合中心点Y轴坐标，单位px。

**表6** DragEvent对象属性列表(继承BaseEvent)7+

属性类型说明typestring事件名称。globalXnumber距离屏幕左上角坐标原点横向距离。globalYnumber距离屏幕左上角坐标原点纵向距离。timestampnumber时间戳。dataTransfer9+[DataTransfer](#ZH-CN_TOPIC_0000002529284975__datatransfer对象9)用于传输数据。[]()[]()

#### Target对象6+

当组件触发事件后，事件回调函数默认会收到一个事件对象，通过该事件对象可以获取相应的信息。

属性类型说明dataSet6+Object组件上通过通用属性设置的[data-*](通用属性 (js-components-common-attributes).md#ZH-CN_TOPIC_0000002497604982__常规属性)的自定义属性组成的集合。

**示例：**

```ets
<!-- xxx.hml -->
<div>
  <div data-a="dataA" data-b="dataB"
    style="width: 100%; height: 50%; background-color: saddlebrown;"@touchstart='touchstartfunc'></div>
</div>
```

```ets
// xxx.js
export default {
  touchstartfunc(msg) {
    console.info(`on touch start, point is: ${msg.touches[0].globalX}`);
    console.info(`on touch start, data is: ${msg.target.dataSet.a}`);
  }
}
```

[]()[]()

#### DataTransfer对象9+

在拖拽操作的过程中，可以通过dataTransfer对象来传输数据，以便在拖拽操作结束的时候对数据进行其他操作。

[]()[]()

#### setData9+

setData(key: string, value: object): boolean

设置给定key关联的数据。如果没有与该key关联的数据，则将其添加到末尾。如果该key关联的数据已经存在，则在相同位置替换现有数据。

**参数：**

参数名参数类型必填描述keystring是数据键值。valueobject是要存储的数据。

**返回值：**

类型说明boolean执行结果，true表示成功，false表示失败。

**示例：**

```ets
// setData的value参数，可以是基本数据类型。
dragStart(e) {
    var isSetOK = e.dataTransfer.setData('name', 1);
},
// setData的value参数，也可以是对象类型。
dragStart(e) {
    var person = new Object();
    person.name = "tom";
    person.age = 21;
    var isSetOK = e.dataTransfer.setData('person', person);
}
```

[]()[]()

#### getData9+

getData(key: string): object

获取给定key关联的数据，如果没有与该key关联的数据，则返回空字符串。

**参数：**

参数名参数类型必填描述keystring是数据键值。

**返回值：**

类型说明object获取的数据。

**示例：**

```ets
dragStart(e) {
    var person = new Object();
    person.name = "tom";
    person.age = 21;
    e.dataTransfer.setData('person', person);
},
dragEnd(e){
    var person = e.dataTransfer.getData('person');
},
```

[]()[]()

#### clearData9+

clearData(key?: string): boolean

删除给定key关联的数据。如果没有与该key关联的数据，则该方法不会产生任何效果。

如果key为空，则删除所有数据。

**参数：**

参数名参数类型必填描述keystring否数据键值。

**返回值：**

类型说明boolean执行结果，true表示成功，false表示失败。

**示例：**

```ets
dragEnd(e) {
    var isSuccess = e.dataTransfer.clearData('name');
}
```

[]()[]()

#### setDragImage9+

setDragImage(pixelMap: PixelMap, offsetX: number,offsetY: number): boolean

用于设置自定义的拖动图像。

**参数：**

参数名参数类型必填描述pixelMap[PixelMap](../../types/interfaces/Interface (PixelMap).md)是前端传入的图片资源。offsetXnumber是相对于图片的横向偏移量。offsetYnumber是相对于图片的纵向偏移量。

**返回值：**

类型说明boolean执行结果，true表示成功，false表示失败。

**示例：**

```ets
import image from '@ohos.multimedia.image';

export default {
    createPixelMap() {
        let color = new ArrayBuffer(4 * 96 * 96);
        var buffer = new Uint8Array(color);
        for (var i = 0; i < buffer.length; i++) {
            buffer[i] = (i + 1) % 255;
        }
        let opts = {
            alphaType: 0,
            editable: true,
            pixelFormat: 4,
            scaleMode: 1,
            size: {
                height: 96, width: 96
            }
        }
        const promise = image.createPixelMap(color, opts);
        promise.then((data) => {
            console.error('-create pixelMap has info message:' + JSON.stringify(data));
            this.pixelMap = data;
            this.pixelMapReader = data;
        })
    },

    onInit() {
        this.createPixelMap()
    },

    dragStart(e) {
        e.dataTransfer.setDragImage(this.pixelMapReader, 50, 50);
    }
}
```