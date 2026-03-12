# mutex.h

#### 概述

声明mutex的C接口。

**引用文件：** <ffrt/mutex.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 10

**相关模块：**[FFRT](FFRT.md)

#### 汇总

#### 函数

名称描述[FFRT_C_API int ffrt_mutexattr_init(ffrt_mutexattr_t* attr)](#ZH-CN_TOPIC_0000002497445574__ffrt_mutexattr_init)初始化mutex属性。[FFRT_C_API int ffrt_mutexattr_settype(ffrt_mutexattr_t* attr, int type)](#ZH-CN_TOPIC_0000002497445574__ffrt_mutexattr_settype)设置mutex属性类型。[FFRT_C_API int ffrt_mutexattr_gettype(ffrt_mutexattr_t* attr, int* type)](#ZH-CN_TOPIC_0000002497445574__ffrt_mutexattr_gettype)获取mutex类型。[FFRT_C_API int ffrt_mutexattr_destroy(ffrt_mutexattr_t* attr)](#ZH-CN_TOPIC_0000002497445574__ffrt_mutexattr_destroy)销毁mutex属性，用户需要调用此接口。[FFRT_C_API int ffrt_mutex_init(ffrt_mutex_t* mutex, const ffrt_mutexattr_t* attr)](#ZH-CN_TOPIC_0000002497445574__ffrt_mutex_init)初始化mutex。[FFRT_C_API int ffrt_mutex_lock(ffrt_mutex_t* mutex)](#ZH-CN_TOPIC_0000002497445574__ffrt_mutex_lock)获取mutex。[FFRT_C_API int ffrt_mutex_unlock(ffrt_mutex_t* mutex)](#ZH-CN_TOPIC_0000002497445574__ffrt_mutex_unlock)释放mutex。[FFRT_C_API int ffrt_mutex_trylock(ffrt_mutex_t* mutex)](#ZH-CN_TOPIC_0000002497445574__ffrt_mutex_trylock)尝试获取mutex。[FFRT_C_API int ffrt_mutex_destroy(ffrt_mutex_t* mutex)](#ZH-CN_TOPIC_0000002497445574__ffrt_mutex_destroy)销毁mutex。

#### 函数说明

#### ffrt_mutexattr_init()

```ets
FFRT_C_API int ffrt_mutexattr_init(ffrt_mutexattr_t* attr)
```

**描述**

初始化mutex属性。

**起始版本：** 12

**参数：**

参数项描述[ffrt_mutexattr_t](ffrt_mutexattr_t.md)* attrmutex属性指针。

**返回：**

类型说明FFRT_C_API int

mutex属性初始化成功返回ffrt_success，

 mutex属性初始化失败返回ffrt_error_inval。

#### ffrt_mutexattr_settype()

```ets
FFRT_C_API int ffrt_mutexattr_settype(ffrt_mutexattr_t* attr, int type)
```

**描述**

设置mutex属性类型。

**起始版本：** 12

**参数：**

参数项描述[ffrt_mutexattr_t](ffrt_mutexattr_t.md)* attrmutex属性指针。int typemutex类型。

**返回：**

类型说明FFRT_C_API int

mutex属性类型设置成功返回ffrt_success，

 mutex属性指针是空或者

 mutex类型不是ffrt_mutex_normal或ffrt_mutex_recursive返回ffrt_error_inval。

#### ffrt_mutexattr_gettype()

```ets
FFRT_C_API int ffrt_mutexattr_gettype(ffrt_mutexattr_t* attr, int* type)
```

**描述**

获取mutex类型。

**起始版本：** 12

**参数：**

参数项描述[ffrt_mutexattr_t](ffrt_mutexattr_t.md)* attrmutex属性指针。int* typemutex类型指针。

**返回：**

类型说明FFRT_C_API int

mutex类型获取成功返回ffrt_success，

 mutex属性指针或mutex类型指针是空返回ffrt_error_inval。

#### ffrt_mutexattr_destroy()

```ets
FFRT_C_API int ffrt_mutexattr_destroy(ffrt_mutexattr_t* attr)
```

**描述**

销毁mutex属性，用户需要调用此接口。

**起始版本：** 12

**参数：**

参数项描述[ffrt_mutexattr_t](ffrt_mutexattr_t.md)* attrmutex属性指针。

**返回：**

类型说明FFRT_C_API int

mutex属性销毁成功返回ffrt_success，

 mutex属性销毁失败返回ffrt_error_inval。

#### ffrt_mutex_init()

```ets
FFRT_C_API int ffrt_mutex_init(ffrt_mutex_t* mutex, const ffrt_mutexattr_t* attr)
```

**描述**

初始化mutex。

**起始版本：** 10

**参数：**

参数项描述[ffrt_mutex_t](ffrt_mutex_t.md)* mutexmutex指针。[const ffrt_mutexattr_t](ffrt_mutexattr_t.md)* attrmutex属性指针。

**返回：**

类型说明FFRT_C_API int

初始化mutex成功返回ffrt_success，

 初始化mutex失败返回ffrt_error_inval。

#### ffrt_mutex_lock()

```ets
FFRT_C_API int ffrt_mutex_lock(ffrt_mutex_t* mutex)
```

**描述**

获取mutex。

**起始版本：** 10

**参数：**

参数项描述[ffrt_mutex_t](ffrt_mutex_t.md)* mutexmutex指针。

**返回：**

类型说明FFRT_C_API int

获取mutex成功返回ffrt_success，

 获取mutex失败返回ffrt_error_inval或者阻塞当前任务。

#### ffrt_mutex_unlock()

```ets
FFRT_C_API int ffrt_mutex_unlock(ffrt_mutex_t* mutex)
```

**描述**

释放mutex。

**起始版本：** 10

**参数：**

参数项描述[ffrt_mutex_t](ffrt_mutex_t.md)* mutexmutex指针。

**返回：**

类型说明FFRT_C_API int

释放mutex成功返回ffrt_success，

 释放mutex失败返回ffrt_error_inval。

#### ffrt_mutex_trylock()

```ets
FFRT_C_API int ffrt_mutex_trylock(ffrt_mutex_t* mutex)
```

**描述**

尝试获取mutex。

**起始版本：** 10

**参数：**

参数项描述[ffrt_mutex_t](ffrt_mutex_t.md)* mutexmutex指针。

**返回：**

类型说明FFRT_C_API int

获取mutex成功返回ffrt_success，

 获取mutex失败返回ffrt_error_inval或ffrt_error_busy。

#### ffrt_mutex_destroy()

```ets
FFRT_C_API int ffrt_mutex_destroy(ffrt_mutex_t* mutex)
```

**描述**

销毁mutex。

**起始版本：** 10

**参数：**

参数项描述[ffrt_mutex_t](ffrt_mutex_t.md)* mutexmutex指针。

**返回：**

类型说明FFRT_C_API int

销毁mutex成功返回ffrt_success，

销毁mutex失败返回ffrt_error_inval。