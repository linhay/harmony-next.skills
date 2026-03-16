# HiAISingleOpDescriptor_ConvolutionParam

#### 概述

[HMS_HiAISingleOpDescriptor_CreateConvolution](../misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopdescriptor_createconvolution)输入参数。

**起始版本：** 5.0.0(12)

**相关模块：**[CANN](../misc/CANN.md)

**所在头文件：**[hiai_single_op.h](../../capi/headers/hiai_single_op.h.md)

#### 汇总

#### 成员变量

名称

描述

[HiAI_SingleOpConvMode](../misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopconvmode)[convMode](#ZH-CN_TOPIC_0000002496888510__convmode)

卷积模式。

int64_t [strides](#ZH-CN_TOPIC_0000002496888510__strides) [2]

卷积核在高度和宽度上的移动步幅，是一个长度为2的int数组[strideHeight, strideWidth]。

int64_t [dilations](#ZH-CN_TOPIC_0000002496888510__dilations) [2]

卷积核在高度和宽度上的扩张率，是一个长度为2的int数组[dilationHeight, dilationWidth]。

int64_t [pads](#ZH-CN_TOPIC_0000002496888510__pads) [4]

各个轴起始和末尾的填充长度，是一个长度为4的int数组[h_begin, h_end, w_begin, w_end]。该值仅在**padMode**为**HIAI_SINGLEOP_PAD_MODE_SPECIFIC**时生效。

int64_t [groups](#ZH-CN_TOPIC_0000002496888510__groups)

输入通道被划分成的组数。若**convMode**为**HIAI_SINGLEOP_CONV_MODE_DEPTHWISE**，**groups**不生效。

[HiAI_SingleOpPadMode](../misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoppadmode)[padMode](#ZH-CN_TOPIC_0000002496888510__padmode)

输入的填充方式。对于**HIAI_SINGLEOP_CONV_MODE_COMMON**和**HIAI_SINGLEOP_CONV_MODE_DEPTHWISE**， 支持**0** (SPECIFIC)，**1** (SAME)，**2** (SAME_UPPER)，**3** (SAME_LOWER)和**4** (VALID)。对于 **HIAI_SINGLEOP_CONV_MODE_TRANSPOSED**, 支持**0** (SPECIFIC)，**1** (SAME)和**4** (VALID)。

#### 结构体成员变量说明

#### convMode

```ets
HiAI_SingleOpConvMode HiAISingleOpDescriptor_ConvolutionParam::convMode
```

**描述**

卷积模式。

#### dilations

```ets
int64_t HiAISingleOpDescriptor_ConvolutionParam::dilations[2]
```

**描述**

卷积核在高度和宽度上的扩张率，是一个长度为2的int数组[dilationHeight, dilationWidth]。

#### groups

```ets
int64_t HiAISingleOpDescriptor_ConvolutionParam::groups
```

**描述**

输入通道被划分成的组数。若**convMode**为**HIAI_SINGLEOP_CONV_MODE_DEPTHWISE**，**groups**不生效。

#### padMode

```ets
HiAI_SingleOpPadMode HiAISingleOpDescriptor_ConvolutionParam::padMode
```

**描述**

输入的填充方式。对于**HIAI_SINGLEOP_CONV_MODE_COMMON**和**HIAI_SINGLEOP_CONV_MODE_DEPTHWISE**， 支持**0** (SPECIFIC)，**1** (SAME)，**2** (SAME_UPPER)，**3** (SAME_LOWER)和**4** (VALID)。对于 **HIAI_SINGLEOP_CONV_MODE_TRANSPOSED**, 支持**0** (SPECIFIC)，**1** (SAME)和**4** (VALID)。

#### pads

```ets
int64_t HiAISingleOpDescriptor_ConvolutionParam::pads[4]
```

**描述**

各个轴起始和末尾的填充长度，是一个长度为4的int数组[h_begin, h_end, w_begin, w_end]。该值仅在**padMode**为**HIAI_SINGLEOP_PAD_MODE_SPECIFIC**时生效。

#### strides

```ets
int64_t HiAISingleOpDescriptor_ConvolutionParam::strides[2]
```

**描述**

卷积核在高度和宽度上的移动步幅，是一个长度为2的int数组[strideHeight, strideWidth]。