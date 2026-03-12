# log.h

#### 概述

HiLog模块日志接口定义，通过这些接口实现日志打印相关功能。用户输出日志时，先定义日志所属业务领域、日志TAG，然后按照类型、级别选择对应API，指定参数隐私标识输出日志内容。

业务领域：指定日志所对应的业务领域，用户自定义使用，用于标识业务的子系统、模块。16进制整数，范围0x0~0xFFFF，超出范围则日志无法打印。

日志TAG：字符串常量，用于标识调用所在的类或者业务。

日志级别：DEBUG、INFO、WARN、ERROR、FATAL。

参数格式：类printf的%方式，包括格式字符串（包括参数类型标识）和变参。

隐私参数标识：在格式字符串每个参数中%符号后类型前增加{public}、{private}标识。注意：每个参数未指定隐私标识时，缺省为隐私。

**引用文件：** <hilog/log.h>

**库：** libhilog_ndk.z.so

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 8

**相关模块：**[HiLog](HiLog.md)

#### 汇总

#### 枚举

名称typedef关键字描述[LogType](#ZH-CN_TOPIC_0000002529445637__logtype)LogType

日志类型。该枚举类型用于定义应用开发者可以使用的日志类型。当前有应用日志LOG_APP。

[LogLevel](#ZH-CN_TOPIC_0000002529445637__loglevel)LogLevel

日志级别。该枚举类型用于定义日志级别。各级别建议使用方式：

DEBUG：比INFO级别更详细的流程记录，通过该级别的日志可以更详细地分析业务流程和定位分析问题。DEBUG级别的日志在正式发布版本中默认不会被打印，只有在调试版本或打开调试开关的情况下才会打印。

INFO：用来记录业务关键流程节点，可以还原业务的主要运行过程；用来记录非正常情况信息，但这些情况都是可以预期的(如无网络信号、登录失败等)。这些日志都应该由该业务内处于支配地位的模块来记录，避免在多个被调用的模块或低级函数中重复记录。

WARN：发生了较为严重的非预期情况，但是对用户影响不大，程序可以自动恢复或通过简单的操作就可以恢复的问题。

ERROR：程序或功能发生了错误，该错误会影响功能的正常运行或用户的正常使用，可以恢复但恢复代价较高，如重置数据等。

FATAL：重大致命异常，表明程序或功能即将崩溃，故障无法恢复。

[PreferStrategy](#ZH-CN_TOPIC_0000002529445637__preferstrategy)PreferStrategy

偏好策略。在[OH_LOG_SetLogLevel](#ZH-CN_TOPIC_0000002529445637__oh_log_setloglevel)中使用。不同策略，实际生效的最低日志级别也不同。

#### 宏定义

名称描述OH_LOG_DEBUG(type, ...) ((void)OH_LOG_Print((type), LOG_DEBUG, LOG_DOMAIN, LOG_TAG, __VA_ARGS__))

DEBUG级别写日志，宏封装接口。使用时需要先定义日志业务领域、日志TAG，一般在源文件起始处统一定义一次。

**起始版本：** 8

OH_LOG_INFO(type, ...) ((void)OH_LOG_Print((type), LOG_INFO, LOG_DOMAIN, LOG_TAG, __VA_ARGS__))

INFO级别写日志，宏封装接口。使用时需要先定义日志业务领域、日志TAG，一般在源文件起始处统一定义一次。

**起始版本：** 8

OH_LOG_WARN(type, ...) ((void)OH_LOG_Print((type), LOG_WARN, LOG_DOMAIN, LOG_TAG, __VA_ARGS__))

WARN级别写日志，宏封装接口。使用时需要先定义日志业务领域、日志TAG，一般在源文件起始处统一定义一次。

**起始版本：** 8

OH_LOG_ERROR(type, ...) ((void)OH_LOG_Print((type), LOG_ERROR, LOG_DOMAIN, LOG_TAG, __VA_ARGS__))

ERROR级别写日志，宏封装接口。使用时需要先定义日志业务领域、日志TAG，一般在源文件起始处统一定义一次。

**起始版本：** 8

OH_LOG_FATAL(type, ...) ((void)OH_LOG_Print((type), LOG_FATAL, LOG_DOMAIN, LOG_TAG, __VA_ARGS__))

FATAL级别写日志，宏封装接口。使用时需要先定义日志业务领域、日志TAG，一般在源文件起始处统一定义一次。

**起始版本：** 8

#### 函数

名称typedef关键字描述[int OH_LOG_Print(LogType type, LogLevel level, unsigned int domain, const char *tag, const char *fmt, ...)](#ZH-CN_TOPIC_0000002529445637__oh_log_print)-写日志接口。指定日志类型、日志级别、业务领域、TAG，按照类printf格式类型和隐私指示确定需要输出的变参。[int OH_LOG_PrintMsg(LogType type, LogLevel level, unsigned int domain, const char *tag, const char *message)](#ZH-CN_TOPIC_0000002529445637__oh_log_printmsg)-写日志接口。输出指定type、level、domain、tag的常量日志字符串。[int OH_LOG_PrintMsgByLen(LogType type, LogLevel level, unsigned int domain, const char *tag, size_t tagLen, const char *message, size_t messageLen)](#ZH-CN_TOPIC_0000002529445637__oh_log_printmsgbylen)-写日志接口。输出指定domain、tag和日志级别的常量日志字符串，需要指定tag及字符串长度，和OH_LOG_PrintMsg区别是可以接受不带结束符的字符串。[int OH_LOG_VPrint(LogType type, LogLevel level, unsigned int domain, const char *tag, const char *fmt, va_list ap)](#ZH-CN_TOPIC_0000002529445637__oh_log_vprint)-写日志接口。指定日志类型、日志级别、业务领域、TAG，按照类printf格式类型和隐私指示确定需要输出的变参，变参为va_list类型。[bool OH_LOG_IsLoggable(unsigned int domain, const char *tag, LogLevel level)](#ZH-CN_TOPIC_0000002529445637__oh_log_isloggable)-检查指定业务领域、TAG、级别的日志是否可以打印。[typedef void (*LogCallback)(const LogType type, const LogLevel level, const unsigned int domain, const char *tag,const char *msg)](#ZH-CN_TOPIC_0000002529445637__logcallback)LogCallback函数指针，开发者自定义回调函数内容，在回调函数中，可自行对hilog日志进行处理。[void OH_LOG_SetCallback(LogCallback callback)](#ZH-CN_TOPIC_0000002529445637__oh_log_setcallback)-

注册函数。调用此函数后，用户实现的回调函数可以接收当前进程的所有hilog日志。

请注意，无论是否调用该接口，它都不会更改当前进程的hilog日志的默认行为。

[void OH_LOG_SetMinLogLevel(LogLevel level)](#ZH-CN_TOPIC_0000002529445637__oh_log_setminloglevel)-设置应用日志打印的最低日志级别，用于拦截低级别日志打印。[void OH_LOG_SetLogLevel(LogLevel level, PreferStrategy prefer)](#ZH-CN_TOPIC_0000002529445637__oh_log_setloglevel)-设置当前应用程序进程的最低日志级别。可以配置不同的偏好策略。

如果设置的日志级别低于[全局日志级别](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hilog#查看和设置日志级别)，OH_LOG_SetMinLogLevel()设置不生效。

debug版本应用下，OH_LOG_SetMinLogLevel()和OH_LOG_SetLogLevel()函数均不生效。

#### 枚举类型说明

#### LogType

```ets
enum LogType
```

**描述**

日志类型。该枚举类型用于定义应用开发者可以使用的日志类型。当前有应用日志LOG_APP。

**起始版本：** 8

枚举项描述LOG_APP = 0应用日志

#### LogLevel

```ets
enum LogLevel
```

**描述**

日志级别。该枚举类型用于定义日志级别。各级别建议使用方式：

DEBUG：比INFO级别更详细的流程记录，通过该级别的日志可以更详细地分析业务流程和定位分析问题。DEBUG级别的日志在正式发布版本中默认不会被打印，只有在调试版本或打开调试开关的情况下才会打印。

INFO：用来记录业务关键流程节点，可以还原业务的主要运行过程；用来记录非正常情况信息，但这些情况都是可以预期的(如无网络信号、登录失败等)。这些日志都应该由该业务内处于支配地位的模块来记录，避免在多个被调用的模块或低级函数中重复记录。

WARN：发生了较为严重的非预期情况，但是对用户影响不大，程序可以自动恢复或通过简单的操作就可以恢复的问题。

ERROR：程序或功能发生了错误，该错误会影响功能的正常运行或用户的正常使用，可以恢复但恢复代价较高，如重置数据等。

FATAL：重大致命异常，表明程序或功能即将崩溃，故障无法恢复。

**起始版本：** 8

枚举项描述LOG_DEBUG = 3DEBUG日志级别，使用OH_LOG_DEBUG接口打印。LOG_INFO = 4INFO日志级别，使用OH_LOG_INFO接口打印。LOG_WARN = 5WARN日志级别，使用OH_LOG_WARN接口打印。LOG_ERROR = 6ERROR日志级别，使用OH_LOG_ERROR接口打印。LOG_FATAL = 7FATAL日志级别，使用OH_LOG_FATAL接口打印。

#### PreferStrategy

```ets
enum PreferStrategy
```

**描述**

偏好策略。在[OH_LOG_SetLogLevel](#ZH-CN_TOPIC_0000002529445637__oh_log_setloglevel)中使用。不同策略，实际生效的最低日志级别也不同。

**起始版本：** 21

枚举项描述UNSET_LOGLEVEL = 0清除设置, 实际生效的最低日志级别是系统控制的最低级别。PREFER_CLOSE_LOG = 1实际生效的最低日志级别是新设置的级别和系统控制的最低级别两个值的较大值。PREFER_OPEN_LOG = 2实际生效的最低日志级别是新设置的级别和系统控制的最低级别两个值的较小值。

#### 函数说明

#### OH_LOG_Print()

```ets
int OH_LOG_Print(LogType type, LogLevel level, unsigned int domain, const char *tag, const char *fmt, ...)
```

**描述**

写日志接口。指定日志类型、日志级别、业务领域、TAG，按照类printf格式类型和隐私指示确定需要输出的变参。

**起始版本：** 8

**参数：**

参数项描述[LogType](log.h.md#ZH-CN_TOPIC_0000002529445637__logtype) type日志类型，三方应用日志类型为LOG_APP。[LogLevel](log.h.md#ZH-CN_TOPIC_0000002529445637__loglevel) level日志级别，日志级别包括LOG_DEBUG、LOG_INFO、LOG_WARN、LOG_ERROR、LOG_FATAL。unsigned int domain日志业务领域，16进制整数，范围0x0~0xFFFF，超出范围则日志无法打印。const char *tag日志TAG，字符串，标识调用所在的类或者业务。tag最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。const char *fmt格式化字符串，基于类printf格式的增强，支持隐私参数标识，即在格式字符串每个参数中'%'符号后类型前增加{public}、{private}标识。...与格式字符串里参数类型对应的参数列表，参数数目、参数类型必须与格式字符串中的标识一一对应。

**返回：**

类型说明int

大于等于0表示成功；小于0表示失败。

失败原因：LogLevel传入的级别低于当前允许打印的级别、domain超出范围、tag为空指针、以及CPU高负载、低内存、整机日志量过大等场景下日志写入socket失败。

#### OH_LOG_PrintMsg()

```ets
int OH_LOG_PrintMsg(LogType type, LogLevel level, unsigned int domain, const char *tag, const char *message)
```

**描述**

写日志接口。输出指定type、level、domain、tag的常量日志字符串。

**起始版本：** 18

**参数：**

参数项描述[LogType](log.h.md#ZH-CN_TOPIC_0000002529445637__logtype) type日志类型，三方应用日志类型为LOG_APP。[LogLevel](log.h.md#ZH-CN_TOPIC_0000002529445637__loglevel) level日志级别，日志级别包括LOG_DEBUG、LOG_INFO、LOG_WARN、LOG_ERROR、LOG_FATAL。unsigned int domain日志业务领域，16进制整数，范围为0x0~0xFFFF，超出范围则日志无法打印。const char *tag日志TAG，字符串，标识调用所在的类或者业务。tag最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。const char *message常量日志字符串。

**返回：**

类型说明int

大于等于0表示成功；小于0表示失败。

失败原因：LogLevel传入的级别低于当前允许打印的级别、domain超出范围、tag为空指针、以及CPU高负载、低内存、整机日志量过大等场景下日志写入socket失败。

#### OH_LOG_PrintMsgByLen()

```ets
int OH_LOG_PrintMsgByLen(LogType type, LogLevel level, unsigned int domain, const char *tag, size_t tagLen, const char *message, size_t messageLen)
```

**描述**

写日志接口。输出指定domain、tag和日志级别的常量日志字符串，需要指定tag及字符串长度，和OH_LOG_PrintMsg区别是可以接受不带结束符的字符串。

**起始版本：** 18

**参数：**

参数项描述[LogType](log.h.md#ZH-CN_TOPIC_0000002529445637__logtype) type日志类型，三方应用日志类型为LOG_APP。[LogLevel](log.h.md#ZH-CN_TOPIC_0000002529445637__loglevel) level日志级别，日志级别包括LOG_DEBUG、LOG_INFO、LOG_WARN、LOG_ERROR、LOG_FATAL。unsigned int domain日志业务领域，16进制整数，范围为0x0~0xFFFF，超出范围则日志无法打印。const char *tag日志TAG，字符串，标识调用所在的类或者业务。tag最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。size_t tagLentag长度。const char *message常量日志字符串。size_t messageLen常量字符串长度，小于3500。

**返回：**

类型说明int

大于等于0表示成功；小于0表示失败。

失败原因：LogLevel传入的级别低于当前允许打印的级别、domain超出范围、tag为空指针、以及CPU高负载、低内存、整机日志量过大等场景下日志写入socket失败。

#### OH_LOG_VPrint()

```ets
int OH_LOG_VPrint(LogType type, LogLevel level, unsigned int domain, const char *tag, const char *fmt, va_list ap)
```

**描述**

写日志接口。指定日志类型、日志级别、业务领域、TAG，按照类printf格式类型和隐私指示确定需要输出的变参，变参为va_list类型。

**起始版本：** 18

**参数：**

参数项描述[LogType](log.h.md#ZH-CN_TOPIC_0000002529445637__logtype) type日志类型，三方应用日志类型为LOG_APP。[LogLevel](log.h.md#ZH-CN_TOPIC_0000002529445637__loglevel) level日志级别，日志级别包括LOG_DEBUG、LOG_INFO、LOG_WARN、LOG_ERROR、LOG_FATAL。unsigned int domain日志业务领域，16进制整数，范围为0x0~0xFFFF，超出范围则日志无法打印。const char *tag日志TAG，字符串，标识调用所在的类或者业务。tag最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。const char *fmt格式化字符串，基于类printf格式的增强，支持隐私参数标识，即在格式字符串每个参数中符号后类型前增加{public}、{private}标识。va_list apva_list类型，与格式字符串里参数类型对应的参数列表，参数数目、参数类型必须与格式字符串中的标识一一对应。

**返回：**

类型说明int

大于等于0表示成功；小于0表示失败。

失败原因：LogLevel传入的级别低于当前允许打印的级别、domain超出范围、tag为空指针、以及CPU高负载、低内存、整机日志量过大等场景下日志写入socket失败。

#### OH_LOG_IsLoggable()

```ets
bool OH_LOG_IsLoggable(unsigned int domain, const char *tag, LogLevel level)
```

**描述**

检查指定业务领域、TAG、级别的日志是否可以打印。

**起始版本：** 8

**参数：**

参数项描述unsigned int domain日志业务领域，16进制整数，范围0x0~0xFFFF，超出范围则日志无法打印。const char *tag日志TAG，字符串，标识调用所在的类或者业务。tag最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。[LogLevel](log.h.md#ZH-CN_TOPIC_0000002529445637__loglevel) level日志级别，日志级别包括LOG_DEBUG、LOG_INFO、LOG_WARN、LOG_ERROR、LOG_FATAL。

**返回：**

类型说明bool如果指定domain、tag、level日志可以打印则返回true；否则返回false。

#### OH_LOG_DEBUG()

```ets
OH_LOG_DEBUG(type, ...)((void)OH_LOG_Print((type), LOG_DEBUG, LOG_DOMAIN, LOG_TAG, __VA_ARGS__))
```

**描述**

DEBUG级别写日志，宏封装接口。使用时需要先定义日志业务领域、日志TAG，一般在源文件起始处统一定义一次。

**起始版本：** 8

**参数：**

参数项描述type日志类型，三方应用日志类型为[LOG_APP](log.h.md#ZH-CN_TOPIC_0000002529445637__logtype)。fmt格式化字符串，基于类printf格式的增强，支持隐私参数标识，即在格式字符串每个参数中'%'符号后类型前增加{public}、{private}标识。...与格式字符串里参数类型对应的参数列表，参数数目、参数类型必须与格式字符串中的标识一一对应。

**参考：**

[OH_LOG_Print](log.h.md#ZH-CN_TOPIC_0000002529445637__oh_log_print)

#### OH_LOG_INFO()

```ets
OH_LOG_INFO(type, ...)((void)OH_LOG_Print((type), LOG_INFO, LOG_DOMAIN, LOG_TAG, __VA_ARGS__))
```

**描述**

INFO级别写日志，宏封装接口。使用时需要先定义日志业务领域、日志TAG，一般在源文件起始处统一定义一次。

**起始版本：** 8

**参数：**

参数项描述type日志类型，三方应用日志类型为LOG_APP。fmt格式化字符串，基于类printf格式的增强，支持隐私参数标识，即在格式字符串每个参数中'%'符号后类型前增加{public}、{private}标识。...与格式字符串里参数类型对应的参数列表，参数数目、参数类型必须与格式字符串中的标识一一对应。

**参考：**

[OH_LOG_Print](log.h.md#ZH-CN_TOPIC_0000002529445637__oh_log_print)

#### OH_LOG_WARN()

```ets
OH_LOG_WARN(type, ...)((void)OH_LOG_Print((type), LOG_WARN, LOG_DOMAIN, LOG_TAG, __VA_ARGS__))
```

**描述**

WARN级别写日志，宏封装接口。使用时需要先定义日志业务领域、日志TAG，一般在源文件起始处统一定义一次。

**起始版本：** 8

**参数：**

参数项描述type日志类型，三方应用日志类型为[LOG_APP](log.h.md#ZH-CN_TOPIC_0000002529445637__logtype)。fmt格式化字符串，基于类printf格式的增强，支持隐私参数标识，即在格式字符串每个参数中'%'符号后类型前增加{public}、{private}标识。...与格式字符串里参数类型对应的参数列表，参数数目、参数类型必须与格式字符串中的标识一一对应。

**参考：**

[OH_LOG_Print](log.h.md#ZH-CN_TOPIC_0000002529445637__oh_log_print)

#### OH_LOG_ERROR()

```ets
OH_LOG_ERROR(type, ...)((void)OH_LOG_Print((type), LOG_ERROR, LOG_DOMAIN, LOG_TAG, __VA_ARGS__))
```

**描述**

ERROR级别写日志，宏封装接口。使用时需要先定义日志业务领域、日志TAG，一般在源文件起始处统一定义一次。

**起始版本：** 8

**参数：**

参数项描述type日志类型，三方应用日志类型为[LOG_APP](log.h.md#ZH-CN_TOPIC_0000002529445637__logtype)。fmt格式化字符串，基于类printf格式的增强，支持隐私参数标识，即在格式字符串每个参数中'%'符号后类型前增加{public}、{private}标识。...与格式字符串里参数类型对应的参数列表，参数数目、参数类型必须与格式字符串中的标识一一对应。

**参考：**

[OH_LOG_Print](log.h.md#ZH-CN_TOPIC_0000002529445637__oh_log_print)

#### OH_LOG_FATAL()

```ets
OH_LOG_FATAL(type, ...)((void)OH_LOG_Print((type), LOG_FATAL, LOG_DOMAIN, LOG_TAG, __VA_ARGS__))
```

**描述**

FATAL级别写日志，宏封装接口。使用时需要先定义日志业务领域、日志TAG，一般在源文件起始处统一定义一次。

**起始版本：** 8

**参数：**

参数项描述type日志类型，三方应用日志类型为[LOG_APP](log.h.md#ZH-CN_TOPIC_0000002529445637__logtype)。fmt格式化字符串，基于类printf格式的增强，支持隐私参数标识，即在格式字符串每个参数中'%'符号后类型前增加{public}、{private}标识。...与格式字符串里参数类型对应的参数列表，参数数目、参数类型必须与格式字符串中的标识一一对应。

**参考：**

[OH_LOG_Print](log.h.md#ZH-CN_TOPIC_0000002529445637__oh_log_print)

#### LogCallback()

```ets
typedef void (*LogCallback)(const LogType type, const LogLevel level, const unsigned int domain, const char *tag, const char *msg)
```

**描述**

函数指针，开发者自定义回调函数内容，在回调函数中，可自行对hilog日志进行处理。

**起始版本：** 11

**参数：**

参数项描述[const LogType](log.h.md#ZH-CN_TOPIC_0000002529445637__logtype) type日志类型，三方应用日志类型为[LOG_APP](log.h.md#ZH-CN_TOPIC_0000002529445637__logtype)。[ const LogLevel](log.h.md#ZH-CN_TOPIC_0000002529445637__loglevel) level日志级别，日志级别包括LOG_DEBUG、LOG_INFO、LOG_WARN、LOG_ERROR、LOG_FATAL。const unsigned int domain日志业务领域，16进制整数，范围为0x0~0xFFFF，超出范围则日志无法打印。const char *tag日志TAG，字符串，标识调用所在的类或者业务。tag最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。const char *msg日志内容，格式化之后的日志字符串。

#### OH_LOG_SetCallback()

```ets
void OH_LOG_SetCallback(LogCallback callback)
```

**描述**

注册函数。调用此函数后，用户实现的回调函数可以接收当前进程的所有hilog日志。

请注意，无论是否调用该接口，它都不会更改当前进程的hilog日志的默认行为。

**起始版本：** 11

**参数：**

参数项描述[LogCallback](log.h.md#ZH-CN_TOPIC_0000002529445637__logcallback) callback用户实现的回调函数。如果不需要处理hilog日志，可以传输空指针。

#### OH_LOG_SetMinLogLevel()

```ets
void OH_LOG_SetMinLogLevel(LogLevel level)
```

**描述**

设置应用日志打印的最低日志级别，用于拦截低级别日志打印。

注意：

1.

如果设置的日志级别低于[全局日志级别](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hilog#查看和设置日志级别)，设置不生效。

1.

debug版本应用下，此函数不生效。

**起始版本：** 15

**参数：**

参数项描述[LogLevel](log.h.md#ZH-CN_TOPIC_0000002529445637__loglevel) level日志级别。

#### OH_LOG_SetLogLevel()

```ets
void OH_LOG_SetLogLevel(LogLevel level, PreferStrategy prefer)
```

**描述**

设置当前应用程序进程的最低日志级别。

可通过prefer参数配置不同的偏好策略。如果选择策略PREFER_CLOSE_LOG，等同于调用OH_LOG_SetMinLogLevel。

注意：debug版本应用下，此函数不生效。

**起始版本：** 21

**参数：**

参数项描述[LogLevel](log.h.md#ZH-CN_TOPIC_0000002529445637__loglevel) level日志级别。[PreferStrategy](log.h.md#ZH-CN_TOPIC_0000002529445637__preferstrategy) prefer偏好策略。