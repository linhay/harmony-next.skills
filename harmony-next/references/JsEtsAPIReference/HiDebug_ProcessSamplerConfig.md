# HiDebug_ProcessSamplerConfig

```ets
typedef struct HiDebug_ProcessSamplerConfig {...} HiDebug_ProcessSamplerConfig
```

#### 概述

采样配置的结构定义

**起始版本：** 22

**相关模块：**[HiDebug](HiDebug.md)

**所在头文件：**[hidebug_type.h](hidebug_type.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t* tids待采样的线程号数组。最大支持10个线程的同时采样，数组长度超出时，将取前10个线程进行采样。uint32_t sizetids指向的数组长度。uint32_t frequency采样频率，取值范围[1-200]，单位HZ。超出取值范围时取默认值100。uint32_t duration采样时长，取值范围[1000-10000]，单位ms。小于1000时，接口调用异常；大于10000时，取10000。uint32_t reserved保留字段。