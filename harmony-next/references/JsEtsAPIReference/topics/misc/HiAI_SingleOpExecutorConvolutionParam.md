# HiAI_SingleOpExecutorConvolutionParam

**概述**

[HMS_HiAISingleOpExecutor_CreateConvolution](CANN.md#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleopexecutor_createconvolution)输入参数。

起始版本： 5.0.0(12)

相关模块： [CANN](CANN.md)

所在头文件： [hiai_single_op.h](hiai_single_op.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| HiAI_SingleOpOptions * options | 指向HiAI_SingleOpOptions对象的指针。该值不能为空指针，否则接口调用失败。 |
| HiAI_SingleOpDescriptor * opDesc | 指向卷积算子对应的HiAI_SingleOpDescriptor对象的指针。该值不能为空指针，否则接口调用失败。 |
| HiAI_SingleOpTensorDesc * input | 指向输入Tensor描述的指针。该值不能为空指针，否则接口调用失败。 |
| HiAI_SingleOpTensorDesc * output | 指向输出Tensor描述的指针。该值不能为空指针，否则接口调用失败。 |
| HiAI_SingleOpTensor * filter | 指向卷积核Tensor的指针。该值不能为空指针，否则接口调用失败。 |
| HiAI_SingleOpTensor * bias | 指向偏置Tensor的指针。如果卷积没有偏置，则该值可以是空指针。 |

**结构体成员变量说明**

**bias**

```ets
HiAI_SingleOpTensor* HiAI_SingleOpExecutorConvolutionParam::bias
```

描述

指向偏置Tensor的指针。如果卷积没有偏置，则该值可以是空指针。

**filter**

```ets
HiAI_SingleOpTensor* HiAI_SingleOpExecutorConvolutionParam::filter
```

描述

指向卷积核Tensor的指针。该值不能为空指针，否则接口调用失败。

**input**

```ets
HiAI_SingleOpTensorDesc* HiAI_SingleOpExecutorConvolutionParam::input
```

描述

指向输入Tensor描述的指针。该值不能为空指针，否则接口调用失败。

**opDesc**

```ets
HiAI_SingleOpDescriptor* HiAI_SingleOpExecutorConvolutionParam::opDesc
```

描述

指向卷积算子对应的[HiAI_SingleOpDescriptor](CANN.md#ZH-CN_TOPIC_0000002553362477__hiai_singleopdescriptor)对象的指针。该值不能为空指针，否则接口调用失败。

**options**

```ets
HiAI_SingleOpOptions* HiAI_SingleOpExecutorConvolutionParam::options
```

描述

指向[HiAI_SingleOpOptions](CANN.md#ZH-CN_TOPIC_0000002553362477__hiai_singleopoptions)对象的指针。该值不能为空指针，否则接口调用失败。

**output**

```ets
HiAI_SingleOpTensorDesc* HiAI_SingleOpExecutorConvolutionParam::output
```

描述

指向输出Tensor描述的指针。该值不能为空指针，否则接口调用失败。