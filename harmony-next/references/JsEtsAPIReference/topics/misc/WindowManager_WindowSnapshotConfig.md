# WindowManager_WindowSnapshotConfig

```ets
typedef struct {...} WindowManager_WindowSnapshotConfig
```

#### 概述

主窗口截图的配置项。

**起始版本：** 21

**相关模块：**[WindowManager](WindowManager.md)

所在头文件： [oh_window_comm.h](oh_window_comm.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| bool useCache | 是否使用主窗口的已有截图。默认值为true。 true表示使用主窗口的已有截图，若主窗口无保存的截图，则使用主窗口的最新截图。false表示使用主窗口的最新截图。 |