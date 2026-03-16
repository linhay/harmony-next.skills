[]()[]()

# 多语言支持

基于开发框架的应用会覆盖多个国家和地区，开发框架支持多语言能力后，可以让应用开发者无需开发多个不同语言的版本，就可以同时支持多种语言的切换，为项目维护带来便利。

开发者仅需要通过[定义资源文件](#ZH-CN_TOPIC_0000002497445056__定义资源文件)和[引用资源](#ZH-CN_TOPIC_0000002497445056__引用资源)两个步骤，就可以使用开发框架的多语言能力；如果需要在应用中获取当前系统语言，请参考[获取语言](#ZH-CN_TOPIC_0000002497445056__获取语言)。

[]()[]()

#### 定义资源文件

资源文件用于存放应用在多种语言场景下的资源内容，开发框架使用JSON文件保存资源定义。

在[文件组织](文件组织 (js-lite-framework-file).md)中指定的i18n文件夹内放置每个语言地区下的资源定义文件即可，资源文件命名为“语言-地区.json”格式，例如英文（美国）的资源文件命名为en-US.json。当开发框架无法在应用中找到系统语言的资源文件时，默认使用en-US.json中的资源内容。

资源文件内容格式如下：

en-US.json

```ets
{
    "strings": {
        "hello": "Hello world!",
        "object": "Object parameter substitution-{name}",
        "array": "Array type parameter substitution-{0}",
        "symbol": "@#$%^&*()_+-={}[]\\|:;\"'<>,./?"
    },

    "files": {
        "image": "image/en_picture.PNG"
    }
}
```

[]()[]()

#### 引用资源

-

在应用中使用$t方法引用资源，$t既可以在hml中使用，也可以在js中使用。系统将根据当前语言环境和指定的资源路径（通过$t的path参数设置），显示对应语言的资源文件中的内容。

参数类型必填描述pathstring是资源路径paramsArray|Object否运行时用来替换占位符的实际内容，占位符分为两种：具名占位符，例如{name}。实际内容必须用Object类型指定，例如：$t('strings.object', **{ name: 'Hello world' }**)。数字占位符，例如{0}。实际内容必须用Array类型指定，例如：$t('strings.array', **['Hello world']**)。
-

示例代码

```ets
<!-- xxx.hml -->
<div>
  <!-- 不使用占位符，text中显示“Hello world!” -->
  <text>{{ $t('strings.hello') }}</text>
  <!-- 具名占位符格式，运行时将占位符{name}替换为“Hello world” -->
  <text>{{ $t('strings.object', { name: 'Hello world' }) }}</text>
  <!-- 数字占位符格式，运行时将占位符{0}替换为“Hello world” -->
  <text>{{ $t('strings.array', ['Hello world']) }}</text>
  <!-- 先在js中获取资源内容，再在text中显示“Hello world” -->
  <text>{{ hello }}</text>
  <!-- 先在js中获取资源内容，并将占位符{name}替换为“Hello world”，再在text中显示“Object parameter substitution-Hello world” -->
  <text>{{ replaceObject }}</text>
  <!-- 先在js中获取资源内容，并将占位符{0}替换为“Hello world”，再在text中显示“Array type parameter substitution-Hello world” -->
  <text>{{ replaceArray }}</text>

  <!-- 获取图片路径 -->
  <image src="{{ $t('files.image') }}" class="image"></image>
  <!-- 先在js中获取图片路径，再在image中显示图片 -->
  <image src="{{ replaceSrc }}" class="image"></image>
</div>
```

```ets
// xxx.js
// 下面为在js文件中的使用方法。
export default {
  data: {
    hello: '',
    replaceObject: '',
    replaceArray: '',
    replaceSrc: '',
  },
  onInit() {
    this.hello = this.$t('strings.hello');
    this.replaceObject = this.$t('strings.object', { name: 'Hello world' });
    this.replaceArray = this.$t('strings.array', ['Hello world']);
    this.replaceSrc = this.$t('files.image');
  },
}
```

[]()[]()

#### 获取语言

获取语言功能请参考[应用配置](../../modules/system/@system.configuration (应用配置).md)。