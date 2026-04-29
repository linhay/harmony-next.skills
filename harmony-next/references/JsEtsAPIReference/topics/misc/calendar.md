# calendar

日历组件，用于呈现日历界面。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

**子组件**

不支持。

**属性**

支持[通用属性](通用属性.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| date | string | 当前日期 | 否 | 当前页面选中的日期，默认是当前日期，格式为年-月-日，如"2019-11-22"。 |
| cardcalendar | boolean | false | 否 | 标识当前日历是否为卡片日历。 默认值：false，表示标识当前日历不是卡片日历。 |
| startdayofweek | int | 6 | 否 | 标识卡片显示的起始天，默认是星期天（取值范围：0-6）。 |
| offdays | string | 5，6 | 否 | 标识卡片显示的休息日，默认是星期六、星期天（取值范围：0-6）。 |
| calendardata | string | - | 是 | 卡片需要显示的月视图数据信息，包括5*7或者6*7格的日数据信息，格式为JSON字符串。"data"标签属性信息见表1 calendardata的日属性。 |
| showholiday | boolean | true | 否 | 标识当前是否显示节假日信息。 默认值：true，表示标识当前要显示节假日信息。 |

 表1 calendardata的日属性

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| index | int | 数据的索引，表示第几个日期。 |
| day | int | 表示具体哪一天。 |
| month | int | 表示月份。 |
| year | int | 表示年份。 |
| isFirstOfLunar | boolean | 表示是否是农历的第一天，在农历第一天的数据下绘制横线。取值true，表示是农历的第一天。取值false，表示不是农历的第一天。 |
| hasSchedule | boolean | 表示是否有日程，在有日程的日期数据上绘制圆。取值true，表示当前有日程。取值false，表示当前无日程。 |
| markLunarDay | boolean | 表示节假日时，农历数据部分是否会变成蓝色。取值true，表示当天为节假日时，农历数据部分会变成蓝色。取值false，表示当天为节假日时，农历数据部分不会变成蓝色。 |
| lunarDay | string | 农历日期。 |
| lunarMonth | string | 农历月份。 |
| dayMark | string | 表示工作日。 - “work”：工作日。 - “off”：休息日。 |
| dayMarkValue | string | 表示具体需要显示的“班”、“休”信息。 |

calendardata示例：

```ets
{
"year":2021,
"month":1,
"data": [{
    "index": 0,
    "lunarMonth": "十一",
    "lunarDay": "十三",
    "year": 2020,
    "month": 12,
    "day": 27,
    "dayMark": "work",
    "dayMarkValue": "班",
    "isFirstOfLunar": true,
    "hasSchedule": true,
    "markLunarDay": true
  },  {
    "index": 1,
    "lunarMonth": "十一",
    "lunarDay": "十四",
    "year": 2020,
    "month": 12,
    "day": 28,
    "dayMark": "work",
    "dayMarkValue": "班",
    "isFirstOfLunar": true,
    "hasSchedule": true,
    "markLunarDay": true
  },  {
    "index": 2,
    "lunarMonth": "十一",
    "lunarDay": "十五",
    "year": 2020,
    "month": 12,
    "day": 29,
    "dayMark": "work",
    "dayMarkValue": "班",
    "isFirstOfLunar": true,
    "hasSchedule": true,
    "markLunarDay": true
  },
  ...
  ]
}
```

**样式**

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| background-color | <color> | - | 否 | 设置背景颜色。 |

**事件**

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| selectedchange | changeEvent | 在点击日期和上下月跳转时触发。 |
| requestdata | requestEvent | 请求日期时触发。 |

 表2 changeEvent

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| $event.day | string | 选择的日期。 |
| $event.month | string | 选择的月份。 |
| $event.year | string | 选择的年份。 |

 表3 requestEvent

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| $event.month | string | 请求的月份。 |
| $event.year | string | 请求的年份。 |
| $event.currentYear | string | 当前显示的年份。 |
| $event.currentMonth | string | 当前显示的月份。 |

**示例**

当前数据仅为示例数据，实际使用时请补充完整的日期数据。

```ets
<!-- xxx.hml -->
<div class="container">
    <calendar class="container_test"
        cardcalendar="true"
        onselectedchange="clickOneDay"
        onrequestdata="messageEventData"
        date="{{currentDate}}"
        offdays="{{offDays}}"
        showholiday="{{showHoliday}}"
        startdayofweek="{{startDayOfWeek}}"
        calendardata="{{calendarData}}">
   </calendar>
</div>
```

```ets
/* xxx.css */
.container {
    flex-direction:column;
    width: 100%;
    height: 100%;
    align-items:center;
    padding-start: 4px;
    padding-end: 4px;
}
.container_test {
    background-color: white;
}
```

```ets
{
    "data": {
        "currentDate": "",
        "offDays": "",
        "startDayOfWeek": 6,
        "showHoliday": true,
        "calendarData": ""
    },
    "actions": {
        "clickOneDay": {
            "action": "router",
            "bundleName": "com.example.calendar",
            "abilityName": "EntryAbility",
            "params": {
                "action": "click_month_view_event",
                "day": "$event.day",
                "month": "$event.month",
                "year": "$event.year"
            }
        },
        "messageEventData": {
            "action": "message",
            "params": {
                "month": "$event.month",
                "year": "$event.year",
                "currentMonth": "$event.currentMonth",
                "currentYear": "$event.currentYear"
            }
```

4*4卡片

![image](public_sys-resources/zh-cn_image_0000002522245690.webp)