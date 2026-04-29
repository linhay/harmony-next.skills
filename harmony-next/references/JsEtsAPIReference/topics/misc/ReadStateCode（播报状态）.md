# ReadStateCode（播报状态）

朗读控件的播报状态枚举类。

起始版本： 5.0.0(12)

**导入模块**

```ets
import { ReadStateCode } from '@kit.SpeechKit';
```

**ReadStateCode**

播报状态枚举类。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PLAYING | 1 | 播放。 |
| PAUSED | 2 | 暂停。 |
| COMPLETED | 3 | 播放完成。 |
| WAITING | 4 | 未播放/停止。 |
| NOT_IN_READ_LIST | 5 | 未在播放列表。 |