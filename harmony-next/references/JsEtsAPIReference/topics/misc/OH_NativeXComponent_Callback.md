# OH_NativeXComponent_Callback

```ets
typedef struct OH_NativeXComponent_Callback {...} OH_NativeXComponent_Callback
```

**概述**

注册Surface生命周期和触摸事件回调。

起始版本： 8

相关模块： [OH_NativeXComponent Native XComponent](OH_NativeXComponent Native XComponent.md)

所在头文件： [native_interface_xcomponent.h](native_interface_xcomponent.h.md)

**汇总**

**成员函数**

| 名称 | 描述 |
| --- | --- |
| void (*OnSurfaceCreated)(OH_NativeXComponent* component, void* window) | 创建Surface时调用。 |
| void (*OnSurfaceChanged)(OH_NativeXComponent* component, void* window) | 当Surface改变时调用。 |
| void (*OnSurfaceDestroyed)(OH_NativeXComponent* component, void* window) | 当Surface被销毁时调用。 |
| void (*DispatchTouchEvent)(OH_NativeXComponent* component, void* window) | 当触摸事件被触发时调用。 |

**成员函数说明**

**OnSurfaceCreated()**

```ets
void (*OnSurfaceCreated)(OH_NativeXComponent* component, void* window)
```

描述：

创建Surface时调用。

起始版本： 8

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| void* window | 表示NativeWindow句柄。 通过XComponent生命周期获取的NativeWindow本身由系统侧持有了一次引用计数，并会在OnSurfaceDestroyed回调触发之后将引用计数减一，引用计数归零后NativeWindow将被释放。 |

**OnSurfaceChanged()**

```ets
void (*OnSurfaceChanged)(OH_NativeXComponent* component, void* window)
```

描述：

当Surface改变时调用。

起始版本： 8

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| void* window | 表示NativeWindow句柄。 |

**OnSurfaceDestroyed()**

```ets
void (*OnSurfaceDestroyed)(OH_NativeXComponent* component, void* window)
```

描述：

当Surface被销毁时调用。

起始版本： 8

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| void* window | 表示NativeWindow句柄。 |

**DispatchTouchEvent()**

```ets
void (*DispatchTouchEvent)(OH_NativeXComponent* component, void* window)
```

描述：

当触摸事件被触发时调用。

起始版本： 8

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| void* window | 表示NativeWindow句柄。 |