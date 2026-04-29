# jsonObject（实体的其他字段）

Entity返回值中jsonObject的参数详细说明。

#### 基础类

#### 时间实体

识别文本中出现的时间，返回类型为JSONObject，键为“time”，键对应的值类型为JSONArray，数组里值类型为JSONObject，具体字段如下表。

| 参数名 | 类型 | 是否必选 | 说明 |
| --- | --- | --- | --- |
| repeat | string | false | 周期。 |
| rrule | string | false | 周期标识，不一定准确，具体以repeat为准（参考数据，不建议使用）。 |
| start | string | false | 开始时间。 示例如下： 1. 2021-08-28T08:00:00（日期和精确时间） 2. 2021-08-28TM（日期和模糊时间） 3. 2021-08-28（日期） 4. T08:00:00（周期时间，没有明确日期，例如“每天8点”） 5. TM（周期时间，没有明确日期，例如“每天早上”） 说明： T为分隔符，T前面为年月日，T后面为时间点，可以是精确时间，可以是用粒度表示的模糊时间。 |
| suggestStart | string | false | 具体开始时间。 大多数情况和start一样，表面上是单个时间，但实际是时间段的时候有区别。 示例如下： 1. “1月”，start（2021-01），end（2021-01），suggestStart（2021-01-01），suggestEnd（2021-01-31） 2. “1月到3月”，start（2021-01），end（2021-03），suggestStart（2021-01-01），suggestEnd（2021-03-31） |
| startTimestamp | number | false | 开始默认时间戳，因时间不一定完整，该时间戳不一定准确，具体以start和suggestStart为准（参考数据，不建议使用）。 |
| end | string | false | 结束时间。 |
| suggestEnd | string | false | 具体结束时间。 大多数情况和end一样，表面上是单个时间，但实际是时间段的时候有区别。 |
| endTimestamp | number | false | 结束时间戳（参考数据，不建议使用）。 |
| maxSection | string | false | 最大时间粒度。 P：精确时间。 M：早晨。 F：上午。 N：中午。 A：下午。 L：傍晚。 E：晚上。 W：凌晨。 |
| minSection | string | false | 最小时间粒度。 |
| isContainFuzzyTime | boolean | true | 是否包含模糊时间，true：包含，false：不包含，默认为false。 |
| containFuzzySection | string | true | 模糊时间粒度，不包含模糊时间粒度时默认为D。 |
| inferType | string | false | 时间推理类型枚举。 |
| rangeDecoration | string | false | 范围描述。 |
| rangeText | string | false | 带范围描述的文本。 |
| isFestival | boolean | false | 是否节日。 true：是。false：不是。 |
| normalFestival | string | false | 节日归一化值。 |
| isLunarTime | boolean | false | 是否包含农历时间，true：包含，false：不包含。 |
| startLunarTime | string | false | 包含的农历时间。 |
| isSolarTerm | boolean | false | 是否节气。 true：是。false：不是。 |
| isIllegal | boolean | false | 是否非法。 true：是。false：不是。 默认为false。 备注：不会将所有不符合规范的时间都识别，只有具体业务场景出现较多较特殊，且非常必要的时候，时间实体才会特意去识别，并设置非法标识，绝大多数不规范的时间不识别，或识别不正确并无影响。 示例如下： 1. “2月30号”，会把start设置为29号或28号，isIllegal设为true。 2. “每周上午8点”，缺少每周具体周几，周期会默认设置成当前周几，isIllegal设为true。 3. “每月周一8点”，缺少每月具体几号。 4. “每年8号上午9点”，缺少每年具体几月。 |
| isChangedIllegal | boolean | true | 是否自动修正了非法时间。 true：是。false：不是。 |
| isPlusTwelveHour | boolean | true | 是否包含天以内模糊时间。 true：是。false：不是。 |
| sequence | number | true | 对应实体出现频率。 |
| oriFestival | string | false | 时间里包含的节日文本。 |
| timestampZone | string | true | 时间戳所在时区，即设备上报时区。 |
| originTimestamp | number | true | 入参文本时间戳，即设备上报时间。 |

#### 地点实体

识别文本中出现的地点，返回类型为JSONObject，键为“location”，键对应的值类型为JSONArray，数组里值类型为JSONObject，具体字段如下表。

| 参数名 | 类型 | 是否必选 | 说明 |
| --- | --- | --- | --- |
| type | string | true | 地点类型：首层核心地点的实际类型。 type：参考邮政局的类型。 |
| coreLocation | JSONObject | true | 核心地点信息组成元素集合。 coreLocation：“邮政局”对应的组成元素分析结果。 |
| adornLocation | JSONObject | false | 修饰核心地点的组成元素集合，引用location定义。 adornLocation：“小肥羊旁边的”对应的组成元素分析结果。 |
| isAbstract | number | false | 0：非抽象地点。 1：和意图相关的抽象地点。 默认为0。 |

地点实体内，coreLocation参数的定义，具体字段如下表。

| 子参数 | 类型 | 是否必选 | 说明 |
| --- | --- | --- | --- |
| oriText | string | true | 地点实体。 |
| value | string | false | 核心地点信息（地点原文去除修饰地点、修饰词后（旁边|附近）的地点信息）。 value：邮政局。 当词性为nsf 、nsw开头时，只填value字段。 |
| province | JSONObject | false | 省份，原文中出现的省份。 |
| city | JSONObject | false | 城市，原文中出现的城市。 |
| county | JSONObject | false | 县，原文中出现的县。 |
| district | JSONObject | false | 行政区，原文中出现的行政区，如“江宁区”。 |
| subDistrict | JSONObject | false | 街道/社区。 |
| town | JSONObject | false | 乡/镇。 |
| village | JSONObject | false | 村。 |
| subVillage | JSONObject | false | 村组。 |
| region | JSONObject | false | 参考物，固定商区、片区（不包含行政区）的概念 ，对应大众点评region字段（识别范围大于大众点评的对应字段）。 |
| road | JSONObject | false | 道路。 |
| default | JSONObject | false | 未分类区域，语义无法区分出该区域类地点属于哪个类型，比如 福永既可能是镇、也可能是街道，文本中只出现福永且上下文无法判断类型时输出到该字段。 |
| location | JSONObject | false | 地图poi信息/组织机构/抽象地点。 |

coreLocation内，参数类型为JSONObject的参数的定义，具体字段如下表。

| 子参数 | 类型 | 是否必选 | 说明 |
| --- | --- | --- | --- |
| value | string | false | 地点类型对应的地点信息。 |
| extend | JSONObject | false | 地点扩展信息。 |

#### 姓名实体

识别文本中出现的人名，返回类型为JSONObject，键为“name”，键对应的值类型为JSONArray，数组里的值类型为JSONObject，具体字段如下表。

| 参数名 | 类型 | 是否必选 | 说明 |
| --- | --- | --- | --- |
| type | string | true | nr（正式），nrn（昵称），nrt（称谓），nrx（其他）。 |

#### 手机号实体

识别文本中出现的电话号码，返回类型为JSONObject，键为“phoneNum”，键对应的值类型为JSONArray，数组里的值类型为JSONObject，具体字段如下表。

| 参数名 | 类型 | 是否必选 | 说明 |
| --- | --- | --- | --- |
| type | number | true | 号码类型，0（固话）、1（手机）。 |
| number | string | true | 号码（去除分机号）。 |
| extNumber | string | false | 分机号，当类型为固话时可能存在该字段。 |

#### 邮箱实体

识别文本中出现的邮箱，返回类型为JSONObject，键为“email”，键对应的值为空。

#### URL实体

识别文本中出现的URL，返回类型为JSONObject， 键为“url”，键对应的值为空。

#### 娱乐类

#### 火车车次实体

识别文本中出现的火车车次，返回类型为JSONObject， 键为“trainNo”，键对应的值类型为JSONArray，数组里的值类型为JSONObject，具体字段如下表。

| 参数名 | 类型 | 是否必选 | 说明 |
| --- | --- | --- | --- |
| sequence | number | true | 对应实体出现频率。 |

#### 航班号实体

识别文本中出现的飞机航班，返回类型为JSONObject， 键为“flightNo”，键对应的值为空。

#### 生活类

#### 快递单号实体

识别文本中出现的快递单号，返回类型为JSONObject，键为“expressNo”，键对应的值类型为JSONArray，数组里的值类型为JSONObject，具体字段如下表。

| 参数名 | 类型 | 是否必选 | 说明 |
| --- | --- | --- | --- |
| isTailNum | number | true | 是否为单号尾号，0（不是尾号）、1（是尾号）。 |

#### 身份证号实体

识别文本中出现的身份证号，返回类型为JSONObject， 键为“idNo”，键对应的值类型为JSONArray，数组里的值类型为JSONObject，具体字段如下表。

| 参数名 | 类型 | 是否必选 | 说明 |
| --- | --- | --- | --- |
| number | string | true | 身份证号码字串。 |
| sequence | number | true | 对应实体出现频率。 |
| type | number | true | 0（身份证）、1（护照）。 |
| isComplete | number | true | “1”（证件号是完整的，不含*等字符），“0”（证件号不是完整的，含有*等字符，例如321***********1234）。 |

#### 验证码实体

识别文本中出现的验证码，返回类型为JSONObject， 键为“verificationCode”，键对应的值类型为JSONArray，数组里的值类型为JSONObject，具体字段如下表。

| 参数名 | 类型 | 是否必选 | 说明 |
| --- | --- | --- | --- |
| type | string | true | 验证码类型（取原文内容，如：验证码、校验码等）。 |
| supplier | string | false | 验证码提供商。 |

#### 银行卡号实体

识别文本中出现的银行卡号，返回类型为JSONObject， 键为“bankCardNo”，键对应的值类型为JSONArray，数组里的值类型为JSONObject，具体字段如下表。

| 参数名 | 类型 | 是否必选 | 说明 |
| --- | --- | --- | --- |
| number | number | true | 银行卡号中的数字。 |
| sequence | number | true | 对应实体出现频率。 |
| validDate | string | false | 银行卡号有效期。 |