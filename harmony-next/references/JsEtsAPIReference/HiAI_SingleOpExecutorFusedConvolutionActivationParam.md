# HiAI_SingleOpExecutorFusedConvolutionActivationParam

#### 概述

[HMS_HiAISingleOpExecutor_CreateFusedConvolutionActivation](CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopexecutor_createfusedconvolutionactivation)输入参数。

**起始版本：** 5.0.0(12)

**相关模块：**[CANN](CANN.md)

**所在头文件：**[hiai_single_op.h](hiai_single_op.h.md)

#### 汇总

#### 成员变量

名称

描述

[HiAI_SingleOpOptions](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopoptions) * [options](#ZH-CN_TOPIC_0000002496568498__options)

指向[HiAI_SingleOpOptions](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopoptions)对象的指针。该值不能为空指针，否则接口调用失败。

[HiAI_SingleOpDescriptor](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopdescriptor) * [convOpDesc](#ZH-CN_TOPIC_0000002496568498__convopdesc)

指卷积算子对应的[HiAI_SingleOpDescriptor](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopdescriptor)对象的指针。该值不能为空指针，否则接口调用失败。

[HiAI_SingleOpDescriptor](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopdescriptor) * [actOpDesc](#ZH-CN_TOPIC_0000002496568498__actopdesc)

指向激活算子对应的[HiAI_SingleOpDescriptor](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopdescriptor)对象的指针。该值不能为空指针，否则接口调用失败。

[HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) * [input](#ZH-CN_TOPIC_0000002496568498__input)

指向输入Tensor描述的指针。该值不能为空指针，否则接口调用失败。

[HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) * [output](#ZH-CN_TOPIC_0000002496568498__output)

指向输出Tensor描述的指针。该值不能为空指针，否则接口调用失败。

[HiAI_SingleOpTensor](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensor) * [filter](#ZH-CN_TOPIC_0000002496568498__filter)

指向卷积核Tensor的指针。该值不能为空指针，否则接口调用失败。

[HiAI_SingleOpTensor](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensor) * [bias](#ZH-CN_TOPIC_0000002496568498__bias)

指向偏置Tensor的指针。如果卷积没有偏置，则该值可以是空指针。

#### 结构体成员变量说明

#### actOpDesc

```ets
HiAI_SingleOpDescriptor* HiAI_SingleOpExecutorFusedConvolutionActivationParam::actOpDesc
```

**描述**

指向激活算子对应的[HiAI_SingleOpDescriptor](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopdescriptor)对象的指针。该值不能为空指针，否则接口调用失败。

#### bias

```ets
HiAI_SingleOpTensor* HiAI_SingleOpExecutorFusedConvolutionActivationParam::bias
```

**描述**

指向偏置Tensor的指针。如果卷积没有偏置，则该值可以是空指针。

#### convOpDesc

```ets
HiAI_SingleOpDescriptor* HiAI_SingleOpExecutorFusedConvolutionActivationParam::convOpDesc
```

**描述**

指卷积算子对应的[HiAI_SingleOpDescriptor](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopdescriptor)对象的指针。该值不能为空指针，否则接口调用失败。

#### filter

```ets
HiAI_SingleOpTensor* HiAI_SingleOpExecutorFusedConvolutionActivationParam::filter
```

**描述**

指向卷积核Tensor的指针。该值不能为空指针，否则接口调用失败。

#### input

```ets
HiAI_SingleOpTensorDesc* HiAI_SingleOpExecutorFusedConvolutionActivationParam::input
```

**描述**

指向输入Tensor描述的指针。该值不能为空指针，否则接口调用失败。

#### options

```ets
HiAI_SingleOpOptions* HiAI_SingleOpExecutorFusedConvolutionActivationParam::options
```

**描述**

指向[HiAI_SingleOpOptions](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopoptions)对象的指针。该值不能为空指针，否则接口调用失败。

#### output

```ets
HiAI_SingleOpTensorDesc* HiAI_SingleOpExecutorFusedConvolutionActivationParam::output
```

**描述**

指向输出Tensor描述的指针。该值不能为空指针，否则接口调用失败。