[]()[]()

# 通用属性

 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

[]()[]()

#### 常规属性

常规属性是指组件普遍支持的用来设置组件基本标识和外观显示特征的属性。

名称类型默认值必填描述idstring-否组件的唯一标识。stylestring-否组件的样式声明。classstring-否组件的样式类，用于引用样式表。refstring-否用来指定指向子元素或子组件的引用信息，该引用将注册到父组件的$refs 属性对象上。disabledbooleanfalse否当前组件是否被禁用，在禁用场景下，组件将无法响应用户交互。设置为true时，组件不响应交互事件。设置为false时，组件响应交互事件。datastring-否

给当前组件设置data属性，进行相应的数据存储和读取。JS文件中：

- 在事件回调中使用 e.target.attr.data 读取数据，e为事件回调函数入参。

- 使用$element或者$refs获取DOM元素后，通过attr.data 进行访问。

从API Version 6 开始，建议使用data-*。

data-*6+string-否

给当前组件设置data-*属性，进行相应的数据存储和读取。大小写不敏感，如data-A和data-a默认相同。JS文件中：

- 在事件回调中使用 e.target.dataSet.a读取数据，e为事件回调函数入参。

- 使用$element或者$refs获取DOM元素后，通过dataSet.a进行访问。

click-effect5+string-否

通过这个属性可以设置组件的弹性点击效果，当前支持如下三种效果：

- spring-small：建议小面积组件设置，缩放(90%)。

- spring-medium：建议中面积组件设置，缩放(95%)。

- spring-large：建议大面积组件设置，缩放(95%)。

dir6+stringauto否

设置元素布局模式，支持设置rtl、ltr和auto三种属性值：

- rtl：使用从右往左布局模式。

- ltr：使用从左往右布局模式。

- auto：跟随系统语言环境。

[]()[]()

#### 渲染属性

渲染属性是指组件普遍支持的用来设置组件是否渲染的属性。

名称类型默认值描述forArray-根据设置的数据列表，展开当前元素。ifboolean-根据设置的boolean值，添加或移除当前元素。true表示添加当前元素，false表示移除当前元素。showboolean-根据设置的boolean值，显示或隐藏当前元素。true表示显示当前元素，false表示隐藏当前元素。

 属性和样式不能混用，不能在属性字段中进行样式设置。

[]()[]()

#### 示例

[]()[]()

#### 示例1

```ets
<!-- xxx.hml -->
<div id="container">
    <button class="btn" type="capsule" value="toggleDisplay" onclick="toggleDisplay"></button>
    <list class="list">
        <list-item for="{{ array }}" class="listItem">
            <text class="text" onclick="toggleShow" show="{{ visible }}"
                  if="{{ display }}">{{ $item.value }}</text>
        </list-item>
    </list>
</div>
```

```ets
/* xxx.css */
#container {
    flex-direction: column;
    width: 100%;
    margin-top: 10px;
}
.text {
    font-size: 50px;
    font-weight: 500;
    margin-left: 12px;
}
.listItem {
    width: 100%;
    height: 100px;
    line-height: 60px;
    border-bottom: 1px solid #DEDEDE;
    font-size: 20px;
}
.btn{
    width: 280px;
    font-size: 26px;
    margin: 10px 0;
}
```

```ets
// xxx.js
export default {
    data: {
        visible: true,
        display: true,
        title: "",
        i: 4,
        array: [
            {"value": "列表文本0"},
            {"value": "列表文本1"},
            {"value": "列表文本2"},
            {"value": "列表文本3"},
        ],
    },
    toggleShow: function() {
        this.array.push({"value": "列表文本" + this.i })
        this.i++
    },
    toggleDisplay: function() {
        this.display = !this.display
    },
}
```

[]()[]()

#### 示例2

```ets
<!-- xxx.hml -->
<div class="container">
    <div>
        <text class="text1" dir='rtl' >hello world</text>
    </div>
    <div>
        <text class="text2" dir='ltr' >hello world</text>
    </div>
</div>
```

```ets
/* xxx.css */
.container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
}
.text1{
    width: 90%;
    height: 100px;
    background-color: aqua;
}
.text2{
    width: 90%;
    height: 100px;
    background-color: blue;
}
```