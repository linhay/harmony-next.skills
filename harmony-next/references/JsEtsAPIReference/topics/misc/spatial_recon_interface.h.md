# spatial_recon_interface.h

**概述**

3D空间重建任务设计模块，通过处理多视角图像输入来生成立体场景。

引用文件： <SpatialReconKit/spatial_recon_interface.h>

库： libspatial_recon_ndk.z.so

系统能力： SystemCapability.Graphics.SpatialRecon

起始版本： 6.1.0(23)

相关模块： [SpatialRecon](SpatialRecon.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| HMS_SpatialRecon_ModelWriteInfo | - | 空间重建模型写入的结构体。 |
| HMS_SpatialRecon_DataFrame | HMS_SpatialRecon_DataFrame | 定义HMS（Huawei Mobile Services）空间重建数据帧的结构体，包含用于空间重建的相机内参、姿态信息、时间戳和图像数据。 |
| HMS_SpatialRecon_Session | HMS_SpatialRecon_Session | 定义用于空间重建会话句柄的结构体，用于3D场景重建。 |
| AREngine_ARSession | AREngine_ARSession | 表示华为AR Engine中AR会话的不透明句柄。 |
| AREngine_ARFrame | AREngine_ARFrame | 定义一个结构体，用于存储AR Engine中捕获的单帧AR图像数据，包含特定时间戳下的相机图像、追踪状态、锚点及AR相关信息。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| HMS_SpatialReconStatus | HMS_SpatialReconStatus | 表示空间重建操作状态的枚举。 |
| HMS_SpatialReconOutputFormat | HMS_SpatialReconOutputFormat | 定义空间重建模型输出格式的枚举。 |
| HMS_SpatialReconRunningMode | HMS_SpatialReconRunningMode | 空间重建运行模式类型。 |
| HMS_SpatialReconStage | HMS_SpatialReconStage | 3D重建流水线中的某特定阶段。此枚举定义了空间重建过程中从初始化到完成或终止的所有可能状态。 |
| HMS_SpatialReconModelType | HMS_SpatialReconModelType | 空间重建模型类型的枚举。目前仅支持3DGS（3D Gaussian Splatting）模型类型。 |
| HMS_SpatialReconImageDataFormat | HMS_SpatialReconImageDataFormat | 空间重建图像数据格式。定义用于空间重建的图像数据格式的枚举，当前仅支持RGB格式。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void (*HMS_SpatialReconCallbackFunc)(HMS_SpatialReconStatus) | HMS_SpatialReconCallbackFunc | 用于处理空间重建状态更新的回调函数类型定义。当系统提供关于空间重建过程的更新时，会调用此回调。 |
| HMS_SpatialReconStatus HMS_SpatialRecon_IsSupport(HMS_SpatialReconModelType type) | - | 查询当前设备是否支持指定的空间重建模型类型。该函数检查设备使用给定模型类型执行空间重建的能力。 |
| HMS_SpatialReconStatus HMS_SpatialRecon_CreateSession(HMS_SpatialReconModelType type, const char* workPath, HMS_SpatialRecon_Session **outSpatialReconSession) | - | 创建一个新的空间重建会话。 |
| HMS_SpatialReconStatus HMS_SpatialRecon_DestroySession(HMS_SpatialRecon_Session *spatialReconSession) | - | 销毁一个空间重建会话并释放其资源。该函数终止空间重建会话并释放与其关联的所有内存和系统资源。调用此函数后，提供的会话指针将失效，不应再次使用。 |
| HMS_SpatialReconStatus HMS_SpatialRecon_PushFrame(HMS_SpatialRecon_Session *spatialReconSession, HMS_SpatialRecon_DataFrame *inputFrame) | - | 将空间重建数据帧推送到空间重建会话中进行处理。该函数将捕获的空间数据帧提交到重建会话中进行处理。会话使用此数据更新或完善其内部空间模型。 |
| HMS_SpatialReconStatus HMS_SpatialRecon_PushARFrame(HMS_SpatialRecon_Session spatialReconSession, AREngine_ARSession arSession, AREngine_ARFrame *arFrame) | - | 将AREngine会话中的AREngine帧推送到空间重建会话中。该函数将包含摄像头图像、姿态和AR跟踪数据的AREngine帧提交到空间重建会话中。它允许重建系统利用实时的AR跟踪信息（如摄像头姿态、特征点）来提升空间映射效果。 |
| HMS_SpatialReconStatus HMS_SpatialRecon_StartSession(HMS_SpatialRecon_Session spatialReconSession, HMS_SpatialRecon_ModelWriteInfo writeInfo, HMS_SpatialReconCallbackFunc onSpatialReconFinished) | - | 启动空间重建会话。该操作是异步执行的，完成状态通过回调函数报告。 |
| HMS_SpatialReconStatus HMS_SpatialRecon_SetRunningMode(HMS_SpatialRecon_Session *spatialReconSession, HMS_SpatialReconRunningMode runningMode) | - | 设置空间重建会话的运行模式。 |
| HMS_SpatialReconStatus HMS_SpatialRecon_PauseSession(HMS_SpatialRecon_Session *spatialReconSession) | - | 暂停一个正在进行的空间重建会话。 |
| HMS_SpatialReconStatus HMS_SpatialRecon_ResumeSession(HMS_SpatialRecon_Session *spatialReconSession) | - | 恢复一个被暂停的空间重建会话。 |
| HMS_SpatialReconStatus HMS_SpatialRecon_GetProgress(HMS_SpatialRecon_Session spatialReconSession, float progress, HMS_SpatialReconStage* stage) | - | 获取当前任务的进度。该函数查询正在进行的任务（即重建或保存）的进度比例，并通过指针变量返回结果。 |
| HMS_SpatialReconStatus HMS_SpatialRecon_GetRefinedFrame(HMS_SpatialRecon_Session *spatialReconSession, int iFrame, HMS_SpatialRecon_DataFrame *outFrame) | - | 从空间重建会话中获取优化后的相机帧。该函数为指定帧索引提供经过重建处理后的优化相机内外参数。 |
| HMS_SpatialReconStatus HMS_SpatialRecon_SaveResultToFile(HMS_SpatialRecon_Session *spatialReconSession, HMS_SpatialRecon_ModelWriteInfo *writeInfo, HMS_SpatialReconCallbackFunc onSaved) | - | 将空间重建结果保存到文件。该函数将处理后的空间重建数据导出到指定的文件格式。操作是异步执行的，完成状态通过回调函数报告。 |

**枚举类型说明**

**HMS_SpatialReconStatus**

```ets
enum HMS_SpatialReconStatus
```

描述

表示空间重建操作状态的枚举。

起始版本： 6.1.0(23)

| 枚举项 | 描述 |
| --- | --- |
| SPATIAL_RECON_STATUS_SUCCESS = 0 | 空间重建成功。 |
| SPATIAL_RECON_STATUS_EXCEEDS_MAXIMUM = 1023700001 | 超过最大空间重建帧数。 |
| SPATIAL_RECON_STATUS_DEVICE_NOT_SUPPORT = 801 | 当前设备不支持空间重建。 |
| SPATIAL_RECON_STATUS_INVALID_WORK_PATH = 1023700002 | 输入的工作路径无效。 |
| SPATIAL_RECON_STATUS_INVALID_FRAME_DATA = 1023700003 | 输入的帧数据无效。 |
| SPATIAL_RECON_STATUS_STAGE_NOT_INITIALIZED = 1023700004 | 会话未初始化。 |
| SPATIAL_RECON_STATUS_STAGE_BUILDING = 1023700005 | 重建会话已开始。 |
| SPATIAL_RECON_STATUS_STAGE_NOT_FINISHED = 1023700006 | 重建会话未完成。 |
| SPATIAL_RECON_STATUS_FAILED = 1023700007 | 空间重建失败。 |

**HMS_SpatialReconOutputFormat**

```ets
enum HMS_SpatialReconOutputFormat
```

描述

定义空间重建模型输出格式的枚举。

起始版本： 6.1.0(23)

| 枚举项 | 描述 |
| --- | --- |
| SPATIAL_RECON_OUTPUT_FORMAT_PLY | PLY格式。 |
| SPATIAL_RECON_OUTPUT_FORMAT_MP4 | MPEG-4视频格式。 |

**HMS_SpatialReconRunningMode**

```ets
enum HMS_SpatialReconRunningMode
```

描述

空间重建运行模式类型。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

SpatialRecon会话支持前台和后台两种运行模式。当应用切换到后台或返回前台时，需要调用HMS_SpatialReconRunningMode，允许系统针对每种运行模式优化功耗。

起始版本： 6.1.0(23)

| 枚举项 | 描述 |
| --- | --- |
| SPATIAL_RECON_RUNNING_FOREGROUND_MODE | 默认前台模式。当空间重建在前台执行时，系统会分配更多资源给重建任务，以确保更快的重建速度。 |
| SPATIAL_RECON_RUNNING_BACKGROUND_MODE | 后台模式。当空间重建在后台运行时，系统会优先处理前台应用的操作，重建速度相对较慢。 |

**HMS_SpatialReconStage**

```ets
enum HMS_SpatialReconStage
```

描述

3D重建流水线中的某特定阶段。此枚举定义了空间重建过程中从初始化到完成或终止的所有可能状态。

起始版本： 6.1.0(23)

| 枚举项 | 描述 |
| --- | --- |
| SPATIAL_RECON_STAGE_INIT | 初始化阶段：正在准备资源和环境。 |
| SPATIAL_RECON_STAGE_BUILDING | 重建阶段：正在处理数据并构建3D模型。 |
| SPATIAL_RECON_STAGE_PAUSED | 重建过程已暂停。 |
| SPATIAL_RECON_STAGE_FINISHED | 重建成功完成。 |
| SPATIAL_RECON_STAGE_SAVING | 保存阶段：3D模型正被保存为文件。 |
| SPATIAL_RECON_STAGE_UNKNOWN | 阶段未知或不确定。 |

**HMS_SpatialReconModelType**

```ets
enum HMS_SpatialReconModelType
```

描述

空间重建模型类型的枚举。目前仅支持3DGS（3D Gaussian Splatting）模型类型。

起始版本： 6.1.0(23)

| 枚举项 | 描述 |
| --- | --- |
| SPATIAL_RECON_MODEL_TYPE_GS | 用于场景重建的3DGS模型。 |

**HMS_SpatialReconImageDataFormat**

```ets
enum HMS_SpatialReconImageDataFormat
```

描述

空间重建图像数据格式。定义用于空间重建的图像数据格式的枚举，当前仅支持RGB格式。

起始版本： 6.1.0(23)

| 枚举项 | 描述 |
| --- | --- |
| SPATIAL_RECON_IMAGEDATA_FORMAT_RGB | RGB格式，一种基于红、绿、蓝的三通道色彩表示方法。 |

**函数说明**

**HMS_SpatialReconCallbackFunc()**

```ets
typedef void (*HMS_SpatialReconCallbackFunc)(HMS_SpatialReconStatus)
```

描述

用于处理空间重建状态更新的回调函数类型定义。当系统提供关于空间重建过程的更新时，会调用此回调。

起始版本： 6.1.0(23)

参数：

| 参数项 | 描述 |
| --- | --- |
| HMS_SpatialReconStatus | 空间重建过程的当前状态。HMS_SpatialReconStatus用于标识重建结果的状态。 |

**HMS_SpatialRecon_IsSupport()**

```ets
HMS_SpatialReconStatus HMS_SpatialRecon_IsSupport(HMS_SpatialReconModelType type)
```

描述

查询当前设备是否支持指定的空间重建模型类型。该函数检查设备使用给定模型类型执行空间重建的能力。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

支持状态可能因设备硬件、系统版本或当前环境条件而异。

起始版本： 6.1.0(23)

参数：

| 参数项 | 描述 |
| --- | --- |
| HMS_SpatialReconModelType type | 要检查支持性的空间重建模型类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| HMS_SpatialReconStatus | HMS_SpatialReconStatus用于指示是否支持该模型类型。 |

**HMS_SpatialRecon_CreateSession()**

```ets
HMS_SpatialReconStatus HMS_SpatialRecon_CreateSession(HMS_SpatialReconModelType type, const char* workPath, HMS_SpatialRecon_Session **outSpatialReconSession)
```

描述

创建一个新的空间重建会话。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

在不支持的设备上，会话对象将无法成功创建，函数将返回错误。可以先调用HMS_SpatialRecon_IsSupport来确认当前设备是否支持此能力。

起始版本： 6.1.0(23)

参数：

| 参数项 | 描述 |
| --- | --- |
| HMS_SpatialReconModelType type | 要使用的重建模型类型。这决定了重建会话的算法和能力。 |
| const char* workPath | 文件系统路径，用于存储重建数据和临时文件，必须为已存在的目录。 |
| HMS_SpatialRecon_Session **outSpatialReconSession | 输出参数，接收指向新创建的空间重建会话对象的指针。调用方负责管理此对象的生命周期，并且最终必须使用适当的清理函数销毁它。 |

返回：

| 类型 | 说明 |
| --- | --- |
| HMS_SpatialReconStatus | HMS_SpatialReconStatus指示操作结果。 |

**HMS_SpatialRecon_DestroySession()**

```ets
HMS_SpatialReconStatus HMS_SpatialRecon_DestroySession(HMS_SpatialRecon_Session *spatialReconSession)
```

描述

销毁一个空间重建会话并释放其资源。该函数终止空间重建会话并释放与其关联的所有内存和系统资源。调用此函数后，提供的会话指针将失效，不应再次使用。

   ![image](public_sys-resources/caution_3.0-zh-cn.webp)

一旦销毁会话，将无法恢复。所有未保存的重建数据将会丢失。如果需要数据持久化，请在销毁前调用HMS_SpatialRecon_SaveResultToFile()进行保存。

起始版本： 6.1.0(23)

参数：

| 参数项 | 描述 |
| --- | --- |
| HMS_SpatialRecon_Session *spatialReconSession | 指向要销毁的空间重建会话的指针。该会话必须是先前创建的，如果为NULL，则函数无效果。 |

返回：

| 类型 | 说明 |
| --- | --- |
| HMS_SpatialReconStatus | HMS_SpatialReconStatus表示操作的结果。 |

**HMS_SpatialRecon_PushFrame()**

```ets
HMS_SpatialReconStatus HMS_SpatialRecon_PushFrame(HMS_SpatialRecon_Session *spatialReconSession, HMS_SpatialRecon_DataFrame *inputFrame)
```

描述

将空间重建数据帧推送到空间重建会话中进行处理。该函数将捕获的空间数据帧提交到重建会话中进行处理。会话使用此数据更新或完善其内部空间模型。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

如果调用HMS_SpatialRecon_StartSession启动建模过程，则帧数据将无法成功推送。

起始版本： 6.1.0(23)

参数：

| 参数项 | 描述 |
| --- | --- |
| HMS_SpatialRecon_Session *spatialReconSession | 指向空间重建会话句柄的指针。 |
| HMS_SpatialRecon_DataFrame *inputFrame | 指向包含传感器数据的空间重建数据帧的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| HMS_SpatialReconStatus | 状态码，表示操作的结果。 |

**HMS_SpatialRecon_PushARFrame()**

```ets
HMS_SpatialReconStatus HMS_SpatialRecon_PushARFrame(HMS_SpatialRecon_Session *spatialReconSession, AREngine_ARSession* arSession, AREngine_ARFrame *arFrame)
```

描述

将AREngine会话中的AREngine帧推送到空间重建会话中。该函数将包含摄像头图像、姿态和AR跟踪数据的AREngine帧提交到空间重建会话中。它允许重建系统利用实时的AR跟踪信息（如摄像头姿态、特征点）来提升空间映射效果。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

如果调用HMS_SpatialRecon_StartSession启动建模过程，则帧数据将无法成功推送。

起始版本： 6.1.0(23)

参数：

| 参数项 | 描述 |
| --- | --- |
| HMS_SpatialRecon_Session *spatialReconSession | 指向空间重建会话句柄的指针。 |
| AREngine_ARSession* arSession | 指向生成AREngine帧的AREngine会话的指针。 |
| AREngine_ARFrame *arFrame | 指向包含AR跟踪数据和摄像头图像的AREngine帧的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| HMS_SpatialReconStatus | 状态码，表示操作的结果。 |

**HMS_SpatialRecon_StartSession()**

```ets
HMS_SpatialReconStatus HMS_SpatialRecon_StartSession(HMS_SpatialRecon_Session *spatialReconSession, HMS_SpatialRecon_ModelWriteInfo* writeInfo, HMS_SpatialReconCallbackFunc onSpatialReconFinished)
```

描述

启动空间重建会话。该操作是异步执行的，完成状态通过回调函数报告。

起始版本： 6.1.0(23)

参数：

| 参数项 | 描述 |
| --- | --- |
| HMS_SpatialRecon_Session *spatialReconSession | 指向空间重建会话句柄的指针。如果spatialReconSession为空，则函数将返回错误码。 |
| HMS_SpatialRecon_ModelWriteInfo* writeInfo | 指向模型写入配置信息的指针。包含保存重建输出的参数。如果writeInfo指针为空，则重建完成后不会执行写入操作，之后可以单独调用HMS_SpatialRecon_SaveResultToFile接口。 |
| HMS_SpatialReconCallbackFunc onSpatialReconFinished | 重建过程完成后将被调用的回调函数指针。回调函数可以设为NULL，此时不会触发回调。 |

返回：

| 类型 | 说明 |
| --- | --- |
| HMS_SpatialReconStatus | HMS_SpatialReconStatus表示成功或特定错误的状态码。 |

**HMS_SpatialRecon_SetRunningMode()**

```ets
HMS_SpatialReconStatus HMS_SpatialRecon_SetRunningMode(HMS_SpatialRecon_Session *spatialReconSession, HMS_SpatialReconRunningMode runningMode)
```

描述

设置空间重建会话的运行模式。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

该函数必须在 HMS_SpatialRecon_StartSession() 之后调用，并且在重建完成之前调用。如果在非活动会话期间调用，则不会产生任何效果。

起始版本： 6.1.0(23)

参数：

| 参数项 | 描述 |
| --- | --- |
| HMS_SpatialRecon_Session *spatialReconSession | 指向空间重建会话句柄的指针。 |
| HMS_SpatialReconRunningMode runningMode | 空间重建的期望运行模式。 |

返回：

| 类型 | 说明 |
| --- | --- |
| HMS_SpatialReconStatus | HMS_SpatialReconStatus表示成功或特定错误的状态码。 |

**HMS_SpatialRecon_PauseSession()**

```ets
HMS_SpatialReconStatus HMS_SpatialRecon_PauseSession(HMS_SpatialRecon_Session *spatialReconSession)
```

描述

暂停一个正在进行的空间重建会话。

起始版本： 6.1.0(23)

参数：

| 参数项 | 描述 |
| --- | --- |
| HMS_SpatialRecon_Session *spatialReconSession | 指向空间重建会话句柄的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| HMS_SpatialReconStatus | 状态码，表示操作的结果。如果不存在活动会话，则返回错误。 |

**HMS_SpatialRecon_ResumeSession()**

```ets
HMS_SpatialReconStatus HMS_SpatialRecon_ResumeSession(HMS_SpatialRecon_Session *spatialReconSession)
```

描述

恢复一个被暂停的空间重建会话。

起始版本： 6.1.0(23)

参数：

| 参数项 | 描述 |
| --- | --- |
| HMS_SpatialRecon_Session *spatialReconSession | 指向空间重建会话句柄的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| HMS_SpatialReconStatus | HMS_SpatialReconStatus表示操作的结果。如果会话未被暂停，则返回错误。 |

**HMS_SpatialRecon_GetProgress()**

```ets
HMS_SpatialReconStatus HMS_SpatialRecon_GetProgress(HMS_SpatialRecon_Session *spatialReconSession, float* progress, HMS_SpatialReconStage* stage)
```

描述

获取当前任务的进度。该函数查询正在进行的任务（即重建或保存）的进度比例，并通过指针变量返回结果。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

一旦调用HMS_SpatialRecon_SaveResultToFile函数，会话将手动开始将3D模型保存到文件。返回的进度值将仅反映文件保存的进度，而不是整个进度。

起始版本： 6.1.0(23)

参数：

| 参数项 | 描述 |
| --- | --- |
| HMS_SpatialRecon_Session *spatialReconSession | 指向空间重建会话实例的指针。 |
| float* progress | 指向一个浮点变量的指针，用于存储进度比例。该值范围为0.0f（0%）到1.0f（100%）。如果指针为NULL，则函数将返回错误码。 |
| HMS_SpatialReconStage* stage | 指向一个阶段变量的指针，用于存储阶段值。如果指针为NULL，则不会写入阶段值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| HMS_SpatialReconStatus | HMS_SpatialReconStatus表示成功或特定错误的状态码。 |

**HMS_SpatialRecon_GetRefinedFrame()**

```ets
HMS_SpatialReconStatus HMS_SpatialRecon_GetRefinedFrame(HMS_SpatialRecon_Session *spatialReconSession, int iFrame, HMS_SpatialRecon_DataFrame *outFrame)
```

描述

从空间重建会话中获取优化后的相机帧。该函数为指定帧索引提供经过重建处理后的优化相机内外参数。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

该函数不返回图像像素数据，imageData字段将被设置为null。

起始版本： 6.1.0(23)

参数：

| 参数项 | 描述 |
| --- | --- |
| HMS_SpatialRecon_Session *spatialReconSession | 指向空间重建会话句柄的指针。 |
| int iFrame | 要获取的帧的索引（从0开始）。 |
| HMS_SpatialRecon_DataFrame *outFrame | 输出参数，存储优化后的帧数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| HMS_SpatialReconStatus | HMS_SpatialReconStatus表示操作成功或失败的状态码。 |

**HMS_SpatialRecon_SaveResultToFile()**

```ets
HMS_SpatialReconStatus HMS_SpatialRecon_SaveResultToFile(HMS_SpatialRecon_Session *spatialReconSession, HMS_SpatialRecon_ModelWriteInfo *writeInfo, HMS_SpatialReconCallbackFunc onSaved)
```

描述

将空间重建结果保存到文件。该函数将处理后的空间重建数据导出到指定的文件格式。操作是异步执行的，完成状态通过回调函数报告。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

该函数只能在模型成功构建后调用；否则，将返回错误值。

起始版本： 6.1.0(23)

参数：

| 参数项 | 描述 |
| --- | --- |
| HMS_SpatialRecon_Session *spatialReconSession | 指向空间重建会话对象的指针。必须不为 NULL，并且应为有效且活跃的会话。 |
| HMS_SpatialRecon_ModelWriteInfo *writeInfo | 指向包含文件导出参数的结构体指针，如文件路径、格式和可选配置标志。必须不为NULL。 |
| HMS_SpatialReconCallbackFunc onSaved | 保存操作完成后将被调用的回调函数指针。如果不需要回调，可以设为NULL。 |

返回：

| 类型 | 说明 |
| --- | --- |
| HMS_SpatialReconStatus | 返回HMS_SpatialReconStatus表示初始验证状态或即时错误（例如无效参数）。文件导出的实际结果通过回调函数传递。 |