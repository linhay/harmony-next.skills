# Constants

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

名称类型只读说明DEFAULT_VOLUME_GROUP_ID9+number是

默认音量组id。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

DEFAULT_INTERRUPT_GROUP_ID9+number是

默认音频中断组id。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**示例：**

```ets
import { audio } from '@kit.AudioKit';

const defaultVolumeGroupId = audio.DEFAULT_VOLUME_GROUP_ID;
const defaultInterruptGroupId = audio.DEFAULT_INTERRUPT_GROUP_ID;
```