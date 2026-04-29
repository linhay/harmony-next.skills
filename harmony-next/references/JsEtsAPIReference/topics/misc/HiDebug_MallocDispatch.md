# HiDebug_MallocDispatch

```ets
typedef struct HiDebug_MallocDispatch {...} HiDebug_MallocDispatch
```

#### 概述

应用程序进程可替换/恢复的HiDebug_MallocDispatch表结构类型定义。

**起始版本：** 20

**相关模块：**[HiDebug](HiDebug.md)

所在头文件： [hidebug_type.h](hidebug_type.h.md)

#### 汇总

#### 成员函数

| 名称 | 描述 |
| --- | --- |
| void* (*malloc)(size_t) | 开发者自定义malloc函数指针。 |
| void* (*calloc)(size_t, size_t) | 开发者自定义calloc函数指针。 |
| void* (*realloc)(void*, size_t) | 开发者自定义realloc函数指针。 |
| void (*free)(void*) | 开发者自定义free函数指针。 |
| void* (*mmap)(void*, size_t, int, int, int, off_t) | 开发者自定义mmap函数指针。 |
| int (*munmap)(void*, size_t) | 开发者自定义munmap函数指针。 |

#### 成员函数说明

#### malloc()

```ets
void* (*malloc)(size_t)
```

**描述**

开发者自定义malloc函数指针。

#### calloc()

```ets
void* (*calloc)(size_t, size_t)
```

**描述**

开发者自定义calloc函数指针。

#### realloc()

```ets
void* (*realloc)(void*, size_t)
```

**描述**

开发者自定义realloc函数指针。

#### free()

```ets
void (*free)(void*)
```

**描述**

开发者自定义free函数指针。

#### mmap()

```ets
void* (*mmap)(void*, size_t, int, int, int, off_t)
```

**描述**

开发者自定义mmap函数指针。

#### munmap()

```ets
int (*munmap)(void*, size_t)
```

**描述**

开发者自定义munmap函数指针。