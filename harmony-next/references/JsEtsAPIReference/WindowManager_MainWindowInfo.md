# WindowManager_MainWindowInfo

```ets
typedef struct {...} WindowManager_MainWindowInfo
```

#### 概述

主窗口信息。

**起始版本：** 21

**相关模块：**[WindowManager](WindowManager.md)

**所在头文件：**[oh_window_comm.h](oh_window_comm.h.md)

#### 汇总

#### 成员变量

名称描述uint64_t displayId主窗口所在的屏幕ID。int32_t windowId主窗口ID。bool showing主窗口的前后台状态。true表示主窗口在前台，false表示主窗口不在前台。const char* label主窗口任务名称。