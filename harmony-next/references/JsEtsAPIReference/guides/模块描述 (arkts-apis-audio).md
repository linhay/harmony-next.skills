[]()[]()

# 模块描述

音频管理提供基础的音频控制能力，包括音量调节、设备管理、数据采集及渲染。

该模块提供以下音频相关的常用功能：

- [AudioManager](../types/interfaces/Interface (AudioManager).md)：音频管理器。
- [AudioRenderer](../types/interfaces/Interface (AudioRenderer).md)：音频渲染，用于播放PCM（Pulse Code Modulation）音频数据。
- [AudioCapturer](../types/interfaces/Interface (AudioCapturer).md)：音频采集，用于录制PCM音频数据。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### 导入模块

```ets
import { audio } from '@kit.AudioKit';
```