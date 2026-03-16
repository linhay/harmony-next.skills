# XEG_RTShadowAODenoiserParameters

#### 概述

光线追踪阴影和环境光遮蔽算法去噪参数。

**起始版本：** 6.0.0(20)

**相关模块： **[XEngine](../misc/XEngine.md)

#### 汇总

#### 成员变量

名称

描述

float [temporalBlendFactor](#ZH-CN_TOPIC_0000002362157621__temporalblendfactor) = 0.075f

时域滤波时当前帧与历史帧混合的权重系数。一致性校验通过后，权重值越大时越多采用当前帧的信息。此参数的值将被限制在[0.01, 1.0]范围内。默认值为0.075。

float [positionConstantDistance](#ZH-CN_TOPIC_0000002362157621__positionconstantdistance) = 1.0f

时域滤波中根据世界空间距离进行一致性校验的阈值，必须大于等于0，如果传负值将被视为0。默认值为1.0。

uint32_t [spatialDenoiseTimes](#ZH-CN_TOPIC_0000002362157621__spatialdenoisetimes) = 2

空域滤波器执行的次数。次数越多生成的阴影和环境光遮蔽噪声越少，但可能会导致降噪结果更模糊。此参数的值将被限制在[0, 5]范围内。默认值为2。

float [ghostingAlpha](#ZH-CN_TOPIC_0000002362157621__ghostingalpha) = 0.0f

时域滤波器中控制运动物体引入的鬼影问题。值为0时，不解决运动物体引入的鬼影问题。值越高，鬼影问题解决的越好，但降噪结果会稍微劣化。此参数的值将被限制在[0.0, 1.0]范围内。默认值为0.0。

float [spatialNormalWeight](#ZH-CN_TOPIC_0000002362157621__spatialnormalweight) = 1.0f

空域滤波器使用的法线权重信息，值越大，法线权重越高，画质越锐利。此参数的值将被限制在[0.0, 1.0]范围内。默认值为1.0。

uint32_t [spatialMaxKernelStep](#ZH-CN_TOPIC_0000002362157621__spatialmaxkernelstep) = 0

空域滤波器采样步长，值越大，采样范围越大。此参数的值将被限制在[0, 4]范围内。默认值为0。

#### 结构体成员变量说明

#### ghostingAlpha

```ets
float XEG_RTShadowAODenoiserParameters::ghostingAlpha = 0.0f
```

**描述**

时域滤波器中控制运动物体引入的鬼影问题。值为0时，不解决运动物体引入的鬼影问题。值越高，鬼影问题解决的越好，但降噪结果会稍微劣化。此参数的值将被限制在[0.0, 1.0]范围内。默认值为0.0。

#### positionConstantDistance

```ets
float XEG_RTShadowAODenoiserParameters::positionConstantDistance = 1.0f
```

**描述**

时域滤波中根据世界空间距离进行一致性校验的阈值，必须大于等于0，如果传负值将被视为0。默认值为1.0。

#### spatialDenoiseTimes

```ets
uint32_t XEG_RTShadowAODenoiserParameters::spatialDenoiseTimes = 2
```

**描述**

空域滤波器执行的次数。次数越多生成的阴影和环境光遮蔽噪声越少，但可能会导致降噪结果更模糊。此参数的值将被限制在[0, 5]范围内。默认值为2。

#### spatialMaxKernelStep

```ets
uint32_t XEG_RTShadowAODenoiserParameters::spatialMaxKernelStep = 0
```

**描述**

空域滤波器采样步长，值越大，采样范围越大。此参数的值将被限制在[0, 4]范围内。默认值为0。

#### spatialNormalWeight

```ets
float XEG_RTShadowAODenoiserParameters::spatialNormalWeight = 1.0f
```

**描述**

空域滤波器使用的法线权重信息，值越大，法线权重越高，画质越锐利。此参数的值将被限制在[0.0, 1.0]范围内。默认值为1.0。

#### temporalBlendFactor

```ets
float XEG_RTShadowAODenoiserParameters::temporalBlendFactor = 0.075f
```

**描述**

时域滤波时当前帧与历史帧混合的权重系数。一致性校验通过后，权重值越大时越多采用当前帧的信息。此参数的值将被限制在[0.01, 1.0]范围内。默认值为0.075。