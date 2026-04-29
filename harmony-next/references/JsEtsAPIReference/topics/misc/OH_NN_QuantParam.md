# OH_NN_QuantParam

```ets
typedef struct OH_NN_QuantParam {...} OH_NN_QuantParam
```

**概述**

量化信息。

在量化的场景中，32位浮点型数据根据以下公式量化为定点数据：

![image](public_sys-resources/zh-cn_image_0000002522086174.webp)

其中s和z是量化参数，在OH_NN_QuantParam中通过scale和zeroPoint保存，r是浮点数，q是量化后的结果，q_min是量化后下界，q_max是量化后的上界，计算方式如下：

![image](public_sys-resources/zh-cn_image_0000002553366089.webp)

![image](public_sys-resources/zh-cn_image_0000002522246166.webp)

clamp函数定义如下：

![image](public_sys-resources/zh-cn_image_0000002553206131.webp)

起始版本： 9

废弃版本： 11

替代接口： [NN_QuantParam](NN_QuantParam.md)

相关模块： [NeuralNetworkRuntime](NeuralNetworkRuntime.md)

所在头文件： [neural_network_runtime_type.h](neural_network_runtime_type.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| uint32_t quantCount | 指定numBits、scale和zeroPoint数组的长度。在per-layer量化的场景下，quantCount通常指定为1，即一个张量所有通道共享一套量化参数；在per-channel量化场景下，quantCount通常和张量通道数一致，每个通道使用自己的量化参数。 |
| const uint32_t *numBits | 量化位数。 |
| const double *scale | 指向量化公式中scale数据的指针。 |
| const int32_t *zeroPoint | 指向量化公式中zero point数据的指针。 |