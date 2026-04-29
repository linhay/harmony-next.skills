# ArkUI_AnimateCompleteCallback

```ets
typedef struct {...} ArkUI_AnimateCompleteCallback
```

**概述**

动画播放结束回调类型。

起始版本： 12

相关模块： [ArkUI_NativeModule](ArkUI_NativeModule.md)

所在头文件： [native_animate.h](native_animate.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| ArkUI_FinishCallbackType type | 在动画中定义结束回调的类型。 |
| void* userData | 用于动画结束回调，传递用户自定义数据。 |

**成员函数**

| 名称 | 描述 |
| --- | --- |
| void (*callback)(void* userData) | 动画播放结束回调。 |

**成员函数说明**

**callback()**

```ets
void (*callback)(void* userData)
```

描述：

动画播放结束回调。