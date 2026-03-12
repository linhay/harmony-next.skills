# calendar

日历组件，用于呈现日历界面。

从API Version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

不支持。

#### 属性

支持[通用属性](通用属性.md)外，还支持如下属性：

名称类型默认值必填描述datestring当前日期否当前页面选中的日期，默认是当前日期，格式为年-月-日，如"2019-11-22"。cardcalendarbooleanfalse否

标识当前日历是否为卡片日历。

默认值：false，表示标识当前日历不是卡片日历。

startdayofweekint6否标识卡片显示的起始天，默认是星期天（取值范围：0-6）。offdaysstring5，6否标识卡片显示的休息日，默认是星期六、星期天（取值范围：0-6）。calendardatastring-是卡片需要显示的月视图数据信息，包括5*7或者6*7格的日数据信息，格式为JSON字符串。"data"标签属性信息见**表1** calendardata的日属性。showholidaybooleantrue否

标识当前是否显示节假日信息。

默认值：true，表示标识当前要显示节假日信息。

**表1** calendardata的日属性

名称类型描述indexint数据的索引，表示第几个日期。dayint表示具体哪一天。monthint表示月份。yearint表示年份。isFirstOfLunarboolean表示是否是农历的第一天，在农历第一天的数据下绘制横线。取值true，表示是农历的第一天。取值false，表示不是农历的第一天。hasScheduleboolean表示是否有日程，在有日程的日期数据上绘制圆。取值true，表示当前有日程。取值false，表示当前无日程。markLunarDayboolean表示节假日时，农历数据部分是否会变成蓝色。取值true，表示当天为节假日时，农历数据部分会变成蓝色。取值false，表示当天为节假日时，农历数据部分不会变成蓝色。lunarDaystring农历日期。lunarMonthstring农历月份。dayMarkstring

表示工作日。

- “work”：工作日。

- “off”：休息日。

dayMarkValuestring表示具体需要显示的“班”、“休”信息。

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

#### 样式

名称类型默认值必填描述background-color<color>-否设置背景颜色。

#### 事件

名称参数描述selectedchangechangeEvent在点击日期和上下月跳转时触发。requestdatarequestEvent请求日期时触发。

**表2** changeEvent

名称类型描述$event.daystring选择的日期。$event.monthstring选择的月份。$event.yearstring选择的年份。

**表3** requestEvent

名称类型描述$event.monthstring请求的月份。$event.yearstring请求的年份。$event.currentYearstring当前显示的年份。$event.currentMonthstring当前显示的月份。

#### 示例

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
        }
    }
}
```

**4*4卡片**