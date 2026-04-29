# HiAISingleOpDescriptor_ConvolutionParam

**概述**

[HMS_HiAISingleOpDescriptor_CreateConvolution](CANN.md#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleopdescriptor_createconvolution)输入参数。

起始版本： 5.0.0(12)

相关模块： [CANN](CANN.md)

所在头文件： [hiai_single_op.h](hiai_single_op.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| HiAI_SingleOpConvMode convMode | 卷积模式。 |
| int64_t strides [2] | 卷积核在高度和宽度上的移动步幅，是一个长度为2的int数组[strideHeight, strideWidth]。 |
| int64_t dilations [2] | 卷积核在高度和宽度上的扩张率，是一个长度为2的int数组[dilationHeight, dilationWidth]。 |
| int64_t pads [4] | 各个轴起始和末尾的填充长度，是一个长度为4的int数组[h_begin, h_end, w_begin, w_end]。该值仅在padMode为HIAI_SINGLEOP_PAD_MODE_SPECIFIC时生效。 |
| int64_t groups | 输入通道被划分成的组数。若convMode为HIAI_SINGLEOP_CONV_MODE_DEPTHWISE，groups不生效。 |
| HiAI_SingleOpPadMode padMode | 输入的填充方式。对于HIAI_SINGLEOP_CONV_MODE_COMMON和HIAI_SINGLEOP_CONV_MODE_DEPTHWISE， 支持0 (SPECIFIC)，1 (SAME)，2 (SAME_UPPER)，3 (SAME_LOWER)和4 (VALID)。对于 HIAI_SINGLEOP_CONV_MODE_TRANSPOSED, 支持0 (SPECIFIC)，1 (SAME)和4 (VALID)。 |

**结构体成员变量说明**

**convMode**

```ets
HiAI_SingleOpConvMode HiAISingleOpDescriptor_ConvolutionParam::convMode
```

描述

卷积模式。

**dilations**

```ets
int64_t HiAISingleOpDescriptor_ConvolutionParam::dilations[2]
```

描述

卷积核在高度和宽度上的扩张率，是一个长度为2的int数组[dilationHeight, dilationWidth]。

**groups**

```ets
int64_t HiAISingleOpDescriptor_ConvolutionParam::groups
```

描述

输入通道被划分成的组数。若convMode为HIAI_SINGLEOP_CONV_MODE_DEPTHWISE，groups不生效。

**padMode**

```ets
HiAI_SingleOpPadMode HiAISingleOpDescriptor_ConvolutionParam::padMode
```

描述

输入的填充方式。对于HIAI_SINGLEOP_CONV_MODE_COMMON和HIAI_SINGLEOP_CONV_MODE_DEPTHWISE， 支持0 (SPECIFIC)，1 (SAME)，2 (SAME_UPPER)，3 (SAME_LOWER)和4 (VALID)。对于 HIAI_SINGLEOP_CONV_MODE_TRANSPOSED, 支持0 (SPECIFIC)，1 (SAME)和4 (VALID)。

**pads**

```ets
int64_t HiAISingleOpDescriptor_ConvolutionParam::pads[4]
```

描述

各个轴起始和末尾的填充长度，是一个长度为4的int数组[h_begin, h_end, w_begin, w_end]。该值仅在padMode为HIAI_SINGLEOP_PAD_MODE_SPECIFIC时生效。

**strides**

```ets
int64_t HiAISingleOpDescriptor_ConvolutionParam::strides[2]
```

描述

卷积核在高度和宽度上的移动步幅，是一个长度为2的int数组[strideHeight, strideWidth]。