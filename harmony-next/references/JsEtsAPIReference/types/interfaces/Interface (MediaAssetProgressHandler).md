# Interface (MediaAssetProgressHandler)

媒体资产进度处理器，应用在onProgress方法中获取媒体资产进度。

- 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 15开始支持。

#### 导入模块

```ets
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

#### onProgress15+

onProgress(progress: number): void

当所请求的视频资源返回进度时系统会回调此方法。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| progress | number | 是 | 返回的进度百分比，范围为0~100。 |