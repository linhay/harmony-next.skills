# WindowManager_WindowProperties

```ets
typedef struct {...} WindowManager_WindowProperties
```

#### 概述

窗口属性。

**起始版本：** 15

**相关模块：**[WindowManager](WindowManager.md)

**所在头文件：**[oh_window_comm.h](oh_window_comm.h.md)

#### 汇总

#### 成员变量

名称描述[WindowManager_Rect](WindowManager_Rect.md) windowRect窗口的位置和尺寸。[WindowManager_Rect](WindowManager_Rect.md) drawableRect窗口内可绘制区域的尺寸。[WindowManager_WindowType](oh_window_comm.h.md#ZH-CN_TOPIC_0000002529285075__windowmanager_windowtype) type窗口类型。bool isFullScreen窗口是否全屏模式。默认值为false。true表示窗口是全屏模式，false表示窗口是非全屏模式。bool isLayoutFullScreen窗口布局是否沉浸式。默认值为false。true表示窗口布局是沉浸式，false表示窗口布局是非沉浸式。bool focusable窗口是否能获取焦点。默认值为true。true表示窗口能获取焦点，false表示窗口不能获取焦点。bool touchable窗口是否可触。默认值为true。true表示窗口可触，false表示窗口不可触。float brightness窗口亮度值。该参数为浮点数，取值范围为[0.0, 1.0]或-1.0。1.0表示最亮，-1.0表示默认亮度。bool isKeepScreenOn是否打开屏幕常亮。默认值为false。true表示屏幕常亮，false表示屏幕不常亮。bool isPrivacyMode窗口是否打开隐私模式。默认值为false。true表示窗口打开隐私模式，false表示窗口关闭隐私模式。bool isTransparent窗口是否透明。默认值为false。true表示窗口透明，false表示窗口非透明。uint32_t id窗口id。默认值为0，该参数为整数。uint32_t displayId窗口所在屏幕的id，默认返回主屏幕id，该参数为整数