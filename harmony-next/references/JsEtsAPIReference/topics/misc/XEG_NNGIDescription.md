# XEG_NNGIDescription

#### 概述

此结构体描述更新NNGI用于计算光线追踪全局光照的所需的信息。

**起始版本：** 6.0.0(20)

**相关模块： **[XEngine](XEngine.md)

所在头文件： [xeg_vulkan_rtgi.h](xeg_vulkan_rtgi.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [XEG_StructureType](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_structuretype) sType | 识别此结构的XEG_StructureType值，必须是XEG_STRUCTURE_TYPE_NNGI_DESCRIPTION。 |
| const void * pNext | 指向扩展结构的指针。 |
| float inferenceCameraViewMatrix [16] | 推理图像的相机观察矩阵，与用户生成Gbuffer使用的矩阵保持一致，必须是4*4列主序矩阵。 |
| float inferenceCameraProjectionMatrix [16] | 推理图像的相机投影矩阵，与用户生成Gbuffer使用的矩阵保持一致，必须是4*4列主序矩阵。 |
| VkImageView inferenceInputDepthImage | 推理输入深度图像，不能为空，格式必须支持深度模板附件，存储Gbuffer的depth纹理。其分辨率和[XEG_NNGICreateInfo](XEG_NNGICreateInfo.md)中inferenceInputSize的分辨率保持一致。 |
| VkImageView inferenceInputNormalImage | 推理输入法线向量图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储法线的xyz分量。其分辨率和[XEG_NNGICreateInfo](XEG_NNGICreateInfo.md)中inferenceInputSize的分辨率保持一致。 |
| VkImageView inferenceInputBaseColorMetallicImage | 推理输入基础颜色图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量，忽略alpha通道信息。其分辨率和[XEG_NNGICreateInfo](XEG_NNGICreateInfo.md)中inferenceInputSize的分辨率保持一致。 |
| VkImageView inferenceOutputGIImage | 推理输出GI图像，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量的间接光照值，忽略alpha通道信息。其分辨率和[XEG_NNGICreateInfo](XEG_NNGICreateInfo.md)中inferenceOutputSize的分辨率保持一致。 |
| float trainingCameraViewMatrix [16] | 训练图像的相机观察矩阵，该矩阵与用户生成PathTracing使用的矩阵保持一致，必须是4*4列主序矩阵。 |
| float trainingCameraProjectionMatrix [16] | 训练图像的相机投影矩阵，该矩阵与用户生成PathTracing使用的矩阵保持一致，必须是4*4列主序矩阵。 |
| VkImageView trainingInputPositionImage | 训练输入位置图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储每个像素的xyz轴坐标。其分辨率和[XEG_NNGICreateInfo](XEG_NNGICreateInfo.md)中trainingSize的分辨率保持一致。 |
| VkImageView trainingInputNormalImage | 训练输入法向量图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储法线的xyz分量。其分辨率和[XEG_NNGICreateInfo](XEG_NNGICreateInfo.md)中trainingSize的分辨率保持一致。 |
| VkImageView trainingInputBaseColorMetallicImage | 训练输入基础颜色图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量，忽略alpha通道信息。其分辨率和[XEG_NNGICreateInfo](XEG_NNGICreateInfo.md)中trainingSize的分辨率保持一致。 |
| VkImageView trainingInputGIImage | 训练输入GI图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量的辐射度值，忽略alpha通道信息。该训练图像的GI结果的质量越高，推理输出的GI结果的质量就越高。其分辨率和[XEG_NNGICreateInfo](XEG_NNGICreateInfo.md)中trainingSize的分辨率保持一致。 |
| VkAabbPositionsKHR sceneAabb | 渲染包围盒范围。 |
| bool isSceneUnbounded = false | 渲染场景是否无界，当前只支持false。 |
| float spatialScaleFactor = 0 | 场景缩放因子，对于有界场景，无需设置，XEngine根据sceneAabb计算该值，对于无界场景，建议设置为平均深度。 |

#### 结构体成员变量说明

#### inferenceCameraProjectionMatrix

```ets
float XEG_NNGIDescription::inferenceCameraProjectionMatrix[16]
```

**描述**

推理图像的相机投影矩阵，与用户生成Gbuffer使用的矩阵保持一致，必须是4*4列主序矩阵。

#### inferenceCameraViewMatrix

```ets
float XEG_NNGIDescription::inferenceCameraViewMatrix[16]
```

**描述**

推理图像的相机观察矩阵，与用户生成Gbuffer使用的矩阵保持一致，必须是4*4列主序矩阵。

#### inferenceInputBaseColorMetallicImage

```ets
VkImageView XEG_NNGIDescription::inferenceInputBaseColorMetallicImage
```

**描述**

推理输入基础颜色图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量，忽略alpha通道信息。其分辨率和[XEG_NNGICreateInfo](XEG_NNGICreateInfo.md)中inferenceInputSize的分辨率保持一致。

#### inferenceInputDepthImage

```ets
VkImageView XEG_NNGIDescription::inferenceInputDepthImage
```

**描述**

推理输入深度图像，不能为空，格式必须支持深度模板附件，存储Gbuffer的depth纹理。其分辨率和[XEG_NNGICreateInfo](XEG_NNGICreateInfo.md)中inferenceInputSize的分辨率保持一致。

#### inferenceInputNormalImage

```ets
VkImageView XEG_NNGIDescription::inferenceInputNormalImage
```

**描述**

推理输入法线向量图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储法线的xyz分量。其分辨率和[XEG_NNGICreateInfo](XEG_NNGICreateInfo.md)中inferenceInputSize的分辨率保持一致。

#### inferenceOutputGIImage

```ets
VkImageView XEG_NNGIDescription::inferenceOutputGIImage
```

**描述**

推理输出GI图像，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量的间接光照值，忽略alpha通道信息。其分辨率和[XEG_NNGICreateInfo](XEG_NNGICreateInfo.md)中inferenceOutputSize的分辨率保持一致。

#### isSceneUnbounded

```ets
bool XEG_NNGIDescription::isSceneUnbounded = false
```

**描述**

渲染场景是否无界，当前只支持false。

#### pNext

```ets
const void* XEG_NNGIDescription::pNext
```

**描述**

指向扩展结构的指针。

#### sceneAabb

```ets
VkAabbPositionsKHR XEG_NNGIDescription::sceneAabb
```

**描述**

渲染包围盒范围。

#### spatialScaleFactor

```ets
float XEG_NNGIDescription::spatialScaleFactor = 0
```

**描述**

场景缩放因子，对于有界场景，无需设置，XEngine根据sceneAabb计算该值，对于无界场景，建议设置为平均深度。

#### sType

```ets
XEG_StructureType XEG_NNGIDescription::sType
```

**描述**

识别此结构的[XEG_StructureType](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_structuretype)值，必须是XEG_STRUCTURE_TYPE_NNGI_DESCRIPTION。

#### trainingCameraProjectionMatrix

```ets
float XEG_NNGIDescription::trainingCameraProjectionMatrix[16]
```

**描述**

训练图像的相机投影矩阵，该矩阵与用户生成PathTracing使用的矩阵保持一致，必须是4*4列主序矩阵。

#### trainingCameraViewMatrix

```ets
float XEG_NNGIDescription::trainingCameraViewMatrix[16]
```

**描述**

训练图像的相机观察矩阵，该矩阵与用户生成PathTracing使用的矩阵保持一致，必须是4*4列主序矩阵。

#### trainingInputBaseColorMetallicImage

```ets
VkImageView XEG_NNGIDescription::trainingInputBaseColorMetallicImage
```

**描述**

训练输入基础颜色图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量，忽略alpha通道信息。其分辨率和[XEG_NNGICreateInfo](XEG_NNGICreateInfo.md)中trainingSize的分辨率保持一致。

#### trainingInputGIImage

```ets
VkImageView XEG_NNGIDescription::trainingInputGIImage
```

**描述**

训练输入GI图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量的辐射度值，忽略alpha通道信息。该训练图像的GI结果的质量越高，推理输出的GI结果的质量就越高。其分辨率和[XEG_NNGICreateInfo](XEG_NNGICreateInfo.md)中trainingSize的分辨率保持一致。

#### trainingInputNormalImage

```ets
VkImageView XEG_NNGIDescription::trainingInputNormalImage
```

**描述**

训练输入法向量图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储法线的xyz分量。其分辨率和[XEG_NNGICreateInfo](XEG_NNGICreateInfo.md)中trainingSize的分辨率保持一致。

#### trainingInputPositionImage

```ets
VkImageView XEG_NNGIDescription::trainingInputPositionImage
```

**描述**

训练输入位置图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储每个像素的xyz轴坐标。其分辨率和[XEG_NNGICreateInfo](XEG_NNGICreateInfo.md)中trainingSize的分辨率保持一致。
