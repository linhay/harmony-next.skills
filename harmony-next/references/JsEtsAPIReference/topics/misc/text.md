# text

文本，用于呈现一段信息。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

**子组件**

支持<[span](span.md)>。

**属性**

支持[通用属性](通用属性.md)。

**样式**

除支持[通用样式](通用样式.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | <color> | - | 否 | 设置文本的颜色。 |
| font-size | <length> | 16px | 否 | 设置文本的尺寸。 |
| letter-spacing | <length> | 0px | 否 | 设置文本的字符间距。 |
| font-style | string | normal | 否 | 设置文本的字体样式，可选值为： - normal：标准的字体样式； - italic：斜体的字体样式。 |
| font-weight | number | string | normal | 否 | 设置文本的字体粗细，number类型取值[100, 900]，默认为400，取值越大，字体越粗。 - number取值必须为100的整数倍。 - string类型取值支持如下四个值：lighter、normal、bold、bolder。 |
| text-decoration | string | none | 否 | 设置文本的文本修饰，可选值为： - underline：文字下划线修饰； - line-through：穿过文本的修饰线； - none：标准文本。 |
| text-align | string | start | 否 | 设置文本的文本对齐方式，可选值为： - left：文本左对齐； - center：文本居中对齐； - right：文本右对齐； - start：根据文字书写相同的方向对齐； - end：根据文字书写相反的方向对齐。  如文本宽度未指定大小，文本的宽度和父容器的宽度大小相等的情况下，对齐效果可能会不明显。 |
| line-height | <length> | 0px | 否 | 设置文本的文本行高，设置为0px时，不限制文本行高，自适应字体大小。 |
| text-overflow | string | clip | 否 | 在设置了最大行数的情况下生效，可选值为： - clip：将文本根据父容器大小进行裁剪显示； - ellipsis：根据父容器大小显示，显示不下的文本用省略号代替。需配合max-lines使用。 |
| font-family | string | sans-serif | 否 | 设置文本的字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过自定义字体指定的字体，会被选中作为文本的字体。 |
| max-lines | number | - | 否 | 设置文本的最大行数。 |
| min-font-size | <length> | - | 否 | 文本最小字号，需要和文本最大字号同时设置，支持文本字号动态变化。设置最大最小字体样式后，font-size不生效。 |
| max-font-size | <length> | - | 否 | 文本最大字号，需要和文本最小字号同时设置，支持文本字号动态变化。设置最大最小字体样式后，font-size不生效。 |
| font-size-step | <length> | 1px | 否 | 文本动态调整字号时的步长，需要设置最小，最大字号样式生效。 |
| prefer-font-sizes | <array> | - | 否 | 预设的字号集合，在动态尺寸调整时，优先使用预设字号集合中的字号匹配设置的最大行数，如果预设字号集合未设置，则使用最大最小和步长调整字号。针对仍然无法满足最大行数要求的情况，使用text-overflow设置项进行截断，设置预设尺寸集后，font-size、max-font-size、min-font-size和font-size-step不生效。 如：prefer-font-sizes: 12px,14px,16px |
| word-break | string | normal | 否 | 设置文本折行模式，可选值为： - normal：默认换行规则，依据各自语言的规则，允许在字间发生换行。 - break-all：对于非中文/日文/韩文的文本，可在任意字符间断行。 - break-word：与break-all相同，不同的地方在于它要求一个没有断行破发点的词必须保持为一个整体单位。 |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

-

字体动态缩放：预设尺寸集合和最小最大字号调节基于是否满足最大行数要求，预设尺寸集合会按照从左到右顺序查看是否满足最大行数要求，最小最大字号调节则基于从大到小顺序查看是否满足最大行数要求。

-

文本换行：文本可以通过转义字符\r\n进行换行。

-

文本标签内支持以下转义字符：\a，\b，\f，\n，\r，\t，\v，'，"，\0。

-

当使用子组件span组成文本段落时，如果span属性样式异常，将导致text段落无法显示。

-

letter-spacing、text-align、line-height、text-overflow和max-lines样式作用于text及其子组件（span）组成的文本内容。

-

text组件说明：不支持text内同时存在文本内容和span子组件。（如果同时存在，只显示span内的内容)

**事件**

支持[通用事件](通用事件.md)。

**示例**

```ets
<div class="container">
    <text class="line_height">
        <span>这是设置了行高的文本。</span>
    </text>
    <text class="letter_spacing">这是设置了字符间距的文本。</text>
    <text class="font_style">这是设置为斜体的文本。</text>
    <text class="text_decoration_style">这是添加了下划线的文本。</text>
    <text class="text_over_flow">文本过长可省略，省略文本。</text>
</div>
```

```ets
.container{
    flex-direction: column;
    width: 100%;
    height: 100%;
    margin-top: 10px;
    margin-left: 30px;
}
.line_height{
    font-size: 20px;
    line-height: 40px;
}
.letter_spacing{
    font-size: 20px;
    letter-spacing: 5px;
}
.font_style{
    font-size: 20px;
    font-style: italic;
}
.text_decoration_style{
    font-size: 20px;
    text-decoration: underline;
    text-decoration-color: red;
}
.text_over_flow{
    font-size: 20px;
    width: 40%;
    max-lines: 1;
    text-overflow: ellipsis;
}
```

4*4卡片

![image](public_sys-resources/zh-cn_image_0000002522085706.webp)