# hiai_tensor.h

#### 概述

模型推理时使用的输入输出内存相关的辅助接口。

通过以下接口，可以关联AippParam到tensor中，也可计算图片格式需要申请的tensor内存大小。

**库：** libhiai_foundation.so

**系统能力：** SystemCapability.AI.HiAIFoundation

**起始版本：** 4.1.0(11)

**相关模块：**[CANN](CANN.md)

#### 汇总

#### 函数

名称

描述

size_t [HMS_HiAITensor_GetSizeWithImageFormat](CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaitensor_getsizewithimageformat) (NN_TensorDesc *desc, [HiAI_ImageFormat](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_imageformat) format)

根据NN_TensorDesc和HiAI_ImageFormat计算申请tensor的大小。

OH_NN_ReturnCode [HMS_HiAITensor_SetAippParams](CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaitensor_setaippparams) (NN_Tensor *tensor, [HiAI_AippParam](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParams[], size_t aippNum)

给NN_Tensor设置AippParams。