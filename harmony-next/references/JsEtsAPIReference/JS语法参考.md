# JS语法参考

JS文件用来定义HML页面的业务逻辑，支持ECMA规范的JavaScript语言。基于JavaScript语言的动态化能力，可以使应用更加富有表现力，具备更加灵活的设计。下面讲述JS文件的编译和运行的支持情况。

#### 语法

支持ES6语法。轻量级智能穿戴支持的ES6语法有限，仅支持以下ES6 语法：

1.

let/const

1.

arrow functions

1.

class

1.

default value

1.

destructuring assignment

1.

destructuring binding pattern

1.

enhanced object initializer

1.

for-of

1.

rest parameter

1.

template strings

-

模块声明

使用import方法引入功能模块：

```ets
import router from '@ohos.router';
```

-

代码引用

使用import方法导入js代码：

```ets
import utils from '../../common/utils.js';
```

#### 对象

- 页面对象 属性类型描述dataObject/Function

页面的数据模型，类型是对象或者函数，如果类型是函数，返回值必须是对象。属性名不能以$或_开头，不要使用保留字for, if, show, tid。

$refsObject持有注册过ref 属性的DOM元素或子组件实例的对象。示例见[获取DOM元素](#ZH-CN_TOPIC_0000002497445058__获取dom元素)。

#### 获取DOM元素

1.

通过$refs获取DOM元素

```ets
<!-- index.hml -->
<div class="container">
  <image-animator class="image-player" ref="animator" images="{{images}}" duration="1s" onclick="handleClick"></image-animator>
</div>
```

```ets
// index.js
export default {
  data: {
    images: [
      { src: '/common/frame1.png' },
      { src: '/common/frame2.png' },
      { src: '/common/frame3.png' },
    ],
  },
  handleClick() {
    const animator = this.$refs.animator; // 获取ref属性为animator的DOM元素
    const state = animator.getState();
    if (state === 'paused') {
      animator.resume();
    } else if (state === 'stopped') {
      animator.start();
    } else {
      animator.pause();
    }
  },
};
```