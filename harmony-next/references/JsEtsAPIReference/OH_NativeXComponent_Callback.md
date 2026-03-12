# OH_NativeXComponent_Callback

```ets
typedef struct OH_NativeXComponent_Callback {...} OH_NativeXComponent_Callback
```

#### 概述

注册Surface生命周期和触摸事件回调。

**起始版本：** 8

**相关模块：**[OH_NativeXComponent Native XComponent](OH_NativeXComponent Native XComponent.md)

**所在头文件：**[native_interface_xcomponent.h](native_interface_xcomponent.h.md)

#### 汇总

#### 成员函数

名称描述[void (*OnSurfaceCreated)(OH_NativeXComponent* component, void* window)](#ZH-CN_TOPIC_0000002529285105__onsurfacecreated)创建Surface时调用。[void (*OnSurfaceChanged)(OH_NativeXComponent* component, void* window)](#ZH-CN_TOPIC_0000002529285105__onsurfacechanged)当Surface改变时调用。[void (*OnSurfaceDestroyed)(OH_NativeXComponent* component, void* window)](#ZH-CN_TOPIC_0000002529285105__onsurfacedestroyed)当Surface被销毁时调用。[void (*DispatchTouchEvent)(OH_NativeXComponent* component, void* window)](#ZH-CN_TOPIC_0000002529285105__dispatchtouchevent)当触摸事件被触发时调用。

#### 成员函数说明

#### OnSurfaceCreated()

```ets
void (*OnSurfaceCreated)(OH_NativeXComponent* component, void* window)
```

**描述：**

创建Surface时调用。

**起始版本：** 8

**参数：**

参数项描述[OH_NativeXComponent](OH_NativeXComponent.md)* component表示指向[OH_NativeXComponent](OH_NativeXComponent.md)实例的指针。void* window表示NativeWindow句柄。

#### OnSurfaceChanged()

```ets
void (*OnSurfaceChanged)(OH_NativeXComponent* component, void* window)
```

**描述：**

当Surface改变时调用。

**起始版本：** 8

**参数：**

参数项描述[OH_NativeXComponent](OH_NativeXComponent.md)* component表示指向[OH_NativeXComponent](OH_NativeXComponent.md)实例的指针。void* window

表示NativeWindow句柄。

通过XComponent生命周期获取的NativeWindow本身由系统侧持有了一次引用计数，并会在OnSurfaceDestroyed回调触发之后将引用计数减一，引用计数归零后NativeWindow将被释放。

#### OnSurfaceDestroyed()

```ets
void (*OnSurfaceDestroyed)(OH_NativeXComponent* component, void* window)
```

**描述：**

当Surface被销毁时调用。

**起始版本：** 8

**参数：**

参数项描述[OH_NativeXComponent](OH_NativeXComponent.md)* component表示指向[OH_NativeXComponent](OH_NativeXComponent.md)实例的指针。void* window表示NativeWindow句柄。

#### DispatchTouchEvent()

```ets
void (*DispatchTouchEvent)(OH_NativeXComponent* component, void* window)
```

**描述：**

当触摸事件被触发时调用。

**起始版本：** 8

**参数：**

参数项描述[OH_NativeXComponent](OH_NativeXComponent.md)* component表示指向[OH_NativeXComponent](OH_NativeXComponent.md)实例的指针。void* window表示NativeWindow句柄。