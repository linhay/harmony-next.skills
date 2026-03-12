# picker

 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

滑动选择器组件，类型支持普通选择器、日期选择器、时间选择器、时间日期选择器和多列文本选择器。

#### 权限列表

无

#### 子组件

不支持。

#### 属性

除支持[通用属性](通用属性.md)外，还支持如下属性：

名称类型默认值必填描述typestring-否

该属性值不支持动态修改。可选择项有：

- text：文本选择器。

- date：日期选择器。

- time：时间选择器。

- datetime：日期时间选择器。

- multi-text：多列文本选择器。

#### 普通选择器

滑动选择器类型设置为text时表示普通选择器。

名称类型默认值必填描述rangeArray-否

设置普通选择器的取值范围，如["15", "20", "25"]。

使用时需要使用数据绑定的方式range ={{data}}，js中声明相应变量data：["15","20","25"]。

selectedstring0否设置普通选择器弹窗的默认取值，取值需要是 range 的索引值，该取值表示选择器弹窗界面的默认选择值。valuestring-否设置普通选择器的值。

#### 日期选择器

滑动选择器类型设置为date时表示日期选择器。

名称类型默认值必填描述start<time>1970-1-1否设置日期选择器的起始时间，格式为 YYYY-MM-DD。end<time>2100-12-31否设置日期选择器的结束时间，格式为 YYYY-MM-DD。selectedstring当前日期否设置日期选择器弹窗的默认取值，格式为 YYYY-MM-DD，该取值表示选择器弹窗界面的默认选择值。valuestring-是设置日期选择器的值。lunar5+booleanfalse否

设置日期选择器是否为农历展示。

默认值：false，表示设置日期选择器是公历展示。

lunarswitchbooleanfalse否

设置日期选择器是否显示农历开关。当值为true时，显示农历开关，点击农历开关可切换公历和农历。当值为false时，不显示农历开关。

当lunarswitch=true且lunar=true时，开关按钮处于被选中状态。

#### 时间选择器

滑动选择器类型设置为time时表示时间选择器。

名称类型默认值必填描述containsecondbooleanfalse否

设置时间选择器是否包含秒。

默认值：false，表示设置时间选择器不包含秒。

selectedstring当前时间否

设置时间选择器弹窗的默认取值，格式为 HH:mm；当包含秒时，格式为HH:mm:ss，

该取值表示选择器弹窗界面的默认选择值。

valuestring-否设置时间选择器的值。hoursnumber

241-4

-5+

否

设置时间选择器采用的时间格式，可选值：

- 12：按照12小时制显示，用上午和下午进行区分；

- 24：按照24小时制显示。

从API Version 5开始，默认值会依据系统当前所选地区和语言选择当地习惯的小时制(12小时制或24小时制)。

#### 日期时间选择器

滑动选择器类型设置为datetime时表示日期时间选择器，日期的选择范围为本年的日月。

名称类型默认值必填描述selectedstring当前日期时间否

设置日期时间选择器弹窗的默认取值，有两种可选格式。

- 月日时分：MM-DD-HH-mm

- 年月日时分：YYYY-MM-DD-HH-mm

不设置年时，默认使用当前年，该取值表示选择器弹窗界面的默认选择值。

valuestring-是设置日期时间选择器的值。hoursnumber

241-4

-5+

否

设置日期时间选择器采用的时间格式，可选值：

- 12：按照12小时制显示，用上午和下午进行区分；

- 24：按照24小时制显示。

从API Version 5开始，默认值会依据系统当前所选地区和语言选择当地习惯的小时制(12小时制或24小时制)。

lunar5+booleanfalse否

设置日期时间选择器是否为农历展示。

默认值：false，表示设置日期选择器为公历展示。

lunarswitchbooleanfalse否

设置日期选择器是否显示农历开关。当值为true时，显示农历开关，点击农历开关可切换公历和农历。当值为false时，不显示农历开关。

当lunarswitch=true且lunar=true时，开关按钮处于被选中状态。

#### 多列文本选择器

滑动选择器类型设置为multi-text时表示多列文本选择器。

名称类型默认值必填描述columnsnumber-是设置多列文本选择器的列数。range二维Array-否

设置多列文本选择器的选择项，其中range 为二维数组。长度表示多少列，数组的每项表示每列的数据，如 [["a","b"], ["c","d"]]。

使用时需要使用数据绑定的方式range ={{data}}，js中声明相应变量data：["15","20","25"]。

selectedArray[0,0,0,…]否设置多列文本选择器弹窗的默认值，每一列被选中项对应的索引构成的数组，该取值表示选择器弹窗界面的默认选择值。valueArray-否设置多列文本选择器的值，每一列被选中项对应的值构成的数组。

#### 样式

除支持[通用样式](通用样式.md)外，还支持如下样式：

名称类型默认值必填描述text-color<color>-否选择器的文本颜色。font-size<length>-否选择器的文本尺寸。allow-scalebooleantrue否

选择器的文本尺寸是否跟随系统设置字体缩放尺寸进行放大缩小。

如果在config描述文件中针对ability配置了fontSize的config-changes标签，则应用不会重启而直接生效。

默认值：true，表示选择器的文本尺寸跟随系统设置字体缩放尺寸进行放大缩小。

letter-spacing<length>0否选择器的字符间距。见[text组件的letter-spacing样式属性](text.md#ZH-CN_TOPIC_0000002529444973__样式)。text-decorationstring-否选择器的文本修饰。见[text组件的text-decoration样式属性](text.md#ZH-CN_TOPIC_0000002529444973__样式)。font-stylestringnormal否选择器的字体样式。见[text组件的font-style样式属性](text.md#ZH-CN_TOPIC_0000002529444973__样式)。font-weightnumber | stringnormal否选择器的字体粗细。见[text组件的font-weight样式属性](text.md#ZH-CN_TOPIC_0000002529444973__样式)。font-familystringsans-serif否选择器的字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过[自定义字体](自定义字体样式.md)指定的字体，会被选中作为文本的字体。line-height<length>0px否选择器的文本行高。column-height5+<length>-否选择器的选择项列表高度。

#### 事件

除支持[通用事件](通用事件.md)外，还支持如下事件：

#### 普通选择器

名称参数描述change{ newValue: newValue, newSelected: newSelected }普通选择器选择值后点击弹窗中的确定按钮时触发该事件（newSelected为索引）。cancel-用户点击弹窗中的取消按钮时触发该事件。

#### 日期选择器

名称参数描述change{ year: year, month: month, day: day }

日期选择器选择值后点击弹窗中的确认按钮时触发该事件。

从API Version 5开始，month值范围为： 0（1月）~11（12月）。

cancel-用户点击弹窗中的取消按钮时触发该事件。

#### 日期时间选择器

名称参数描述change{ year: year, month: month, day: day, hour: hour, minute: minute}日期时间选择器选择值后点击弹窗中的确认按钮时触发该事件。cancel-用户点击弹窗中的取消按钮时触发该事件。

#### 时间选择器

名称参数描述change{ hour: hour, minute: minute, [second: second] }时间选择器选择值后点击弹窗中的确认按钮时触发该事件，当使用时分秒时，还包含秒数据。cancel-用户点击弹窗中的取消按钮时触发该事件。

#### 多列文本选择器

名称参数描述change{ newValue: [newValue1, newValue2, newValue3, …], newSelected:[newSelected1, newSelected2, newSelected3, …] }

多列文本选择器选择值后点击弹窗中的确认按钮时触发该事件，其中：

- newValue：被选中项对应的值构成的数组。

- newSelected：被选中项对应的索引构成的数组，两者的长度和range的长度一致。

columnchange{ column: column, newValue: newValue, newSelected: newSelected }

多列文本选择器中某一列的值改变时触发该事件，其中：

- column：第几列修改。

- newValue：选中的值。

- newSelected：选中值对应的索引。

cancel-用户点击弹窗中的取消按钮时触发该事件。

#### 方法

除支持[通用方法](通用方法.md)外，支持如下方法：

名称参数描述show-显示 picker。

#### 示例

```ets
<!-- xxx.hml -->
<div class="container">
    <select @change="selectChange">
        <option value="{{ item }}" for="item in selectList">
            {{ item }}
        </option>
    </select>
    <picker id="picker0" type="text" value="{{ textvalue }}" selected="{{ textselect }}" range="{{ rangetext }}"
            onchange="textonchange"
            oncancel="textoncancel" class="pickertext" show="false"></picker>

    <picker id="picker1" type="date" value="{{ datevalue }}" start="2002-2-5" end="2030-6-5" selected="{{ dateselect }}"
            lunarswitch="true"
            onchange="dateonchange" oncancel="dateoncancel" class="pickerdate" show="false"></picker>

    <picker id="picker2" type="time" value="{{ timevalue }}" containsecond="{{ containsecond }}"
            selected="{{ timeselect }}" hours="12"
            onchange="timeonchange" oncancel="timeoncancel" class="pickertime" show="false"></picker>

    <picker id="picker3" type="datetime" value="{{ datetimevalue }}" selected="{{ datetimeselect }}" hours="24"
            lunarswitch="true"
            onchange="datetimeonchange" oncancel="datetimeoncancel" class="pickerdatetime" show="false"></picker>

    <picker id="picker4" type="multi-text" value="{{ multitextvalue }}" columns="3" range="{{ multitext }}"
            selected="{{ multitextselect }}"
            onchange="multitextonchange" oncancel="multitextoncancel" class="pickermuitl" show="false"></picker>
</div>
```

```ets
/* xxx.css */
.container {
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

picker {
    width: 60%;
    height: 80px;
    border-radius: 20px;
    text-color: white;
    font-size: 15px;
    background-color: #4747e3;
    margin-left: 20%;
}

select {
    background-color: #efecec;
    height: 50px;
    width: 60%;
    margin-left: 20%;
    margin-top: 300px;
    margin-bottom: 50px;
    font-size: 22px;
}
```

```ets
// xxx.js
import promptAction from '@ohos.promptAction';

export default {
    data: {
        selectList: ["text", "data", "time", "datetime", "multitext"],
        rangetext: ['15', "20", "25"],
        multitext: [["a", "b", "c"], ["e", "f", "g"], ["h", "i"], ["k", "l", "m"]],
        textvalue: 'default textvalue',
        datevalue: 'default datevalue',
        timevalue: 'default timevalue',
        datetimevalue: 'default datetimevalue',
        multitextvalue: 'default multitextvalue',
        containsecond: true,
        multitextselect: [1, 2, 0],
        datetimeselect: '2012-5-6-11-25',
        timeselect: '11:22:30',
        dateselect: '2021-3-2',
        textselect: '2'
    },
    selectChange(e) {
        for (let i = 0;i < this.selectList.length; i++) {
            if (e.newValue == this.selectList[i]) {
                this.$element("picker" + i).show();
            }
        }
    },
    textonchange(e) {
        this.textvalue = e.newValue;
        promptAction.showToast({
            message: "text:" + e.newValue + ",newSelected:" + e.newSelected
        })
    },
    textoncancel(e) {
        promptAction.showToast({
            message: "text: textoncancel"
        })
    },
    dateonchange(e) {
        this.datevalue = e.year + "-" + e.month + "-" + e.day;
        promptAction.showToast({
            message: "date:" + e.year + "-" + (e.month + 1) + "-" + e.day
        })
    },
    dateoncancel() {
        promptAction.showToast({
            message: "date: dateoncancel"
        })
    },
    timeonchange(e) {
        if (this.containsecond) {
            this.timevalue = e.hour + ":" + e.minute + ":" + e.second;
            promptAction.showToast({
                message: "Time:" + e.hour + ":" + e.minute + ":" + e.second
            })
        } else {
            this.timevalue = e.hour + ":" + e.minute;
            promptAction.showToast({
                message: "Time:" + e.hour + ":" + e.minute
            })
        }
    },
    timeoncancel() {
        promptAction.showToast({
            message: "timeoncancel"
        })
    },
    datetimeonchange(e) {
        this.datetimevalue = e.year + "-" + e.month + "-" + e.day + " " + e.hour + ":" + e.minute;
        promptAction.showToast({
            message: "Time:" + (e.month + 1) + "-" + e.day + " " + e.hour + ":" + e.minute
        })
    },
    datetimeoncancel() {
        promptAction.showToast({
            message: "datetimeoncancel"
        })
    },
    multitextonchange(e) {
        this.multitextvalue = e.newValue;
        promptAction.showToast({
            message: "Multi-column text change" + e.newValue
        })
    },
    multitextoncancel() {
        promptAction.showToast({
            message: "multitextoncancel"
        })
    },
    popup_picker() {
        this.$element("picker_text").show();
    },
}
```