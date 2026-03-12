# NetworkBoost_WeakSignalPrediction

#### 概述

弱信号预测相关信息。

**起始版本：** 5.1.0(18)

**相关模块：**[NetworkBoost](NetworkBoost.md)

#### 汇总

#### 成员变量

名称

描述

bool [isLastPredictionValid](NetworkBoost_WeakSignalPrediction.md#ZH-CN_TOPIC_0000002496814641__aaba94cd96106bc8e7f5474642c0d7fda)

最近一次的弱信号预测是否有效，true表示最近一次的弱信号预测依旧有效，false表示最近一次的弱信号预测失效，此时startTime和duration参数忽略。

uint32_t [startTime](NetworkBoost_WeakSignalPrediction.md#ZH-CN_TOPIC_0000002496814641__a63b7e6caf5bb45d7950a9c098093c7d5)

预计多长时间进入弱信号（单位：s），取值范围为0和任意正数。

uint32_t [duration](NetworkBoost_WeakSignalPrediction.md#ZH-CN_TOPIC_0000002496814641__a5186381056b65766101e954ae175c8a1)

预计在弱信号区域停留时长（单位：s），取任意正数。取值0，此次预测结果无效。

#### 结构体成员变量说明

#### duration

```ets
uint32_t NetworkBoost_WeakSignalPrediction::duration
```

**描述**

预计在弱信号区域停留时长（单位：s），取任意正数。取值0，此次预测结果无效。

#### isLastPredictionValid

```ets
bool NetworkBoost_WeakSignalPrediction::isLastPredictionValid
```

**描述**

最近一次的弱信号预测是否有效，true表示最近一次的弱信号预测依旧有效，false表示最近一次的弱信号预测失效，此时startTime和duration参数忽略。

#### startTime

```ets
uint32_t NetworkBoost_WeakSignalPrediction::startTime
```

**描述**

预计多长时间进入弱信号（单位：s），取值范围为0和任意正数。