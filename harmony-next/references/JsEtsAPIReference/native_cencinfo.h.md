# native_cencinfo.h

#### 概述

声明用于设置解密参数的Native API。

**引用文件：** <multimedia/player_framework/native_cencinfo.h>

**库：** libnative_media_avcencinfo.so

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 12

**相关模块：**[Multimedia_Drm](Multimedia_Drm.md)

#### 汇总

#### 结构体

名称typedef关键字描述[DrmSubsample](DrmSubsample.md)DrmSubsampleSubsample结构类型定义。[OH_AVBuffer](OH_AVBuffer.md)OH_AVBufferAVBuffer结构。[OH_AVCencInfo](OH_AVCencInfo.md)OH_AVCencInfoAVCencInfo结构。

#### 枚举

名称typedef关键字描述[DrmCencAlgorithm](#ZH-CN_TOPIC_0000002497605744__drmcencalgorithm)DrmCencAlgorithmDrm CENC算法类型。[DrmCencInfoMode](#ZH-CN_TOPIC_0000002497605744__drmcencinfomode)DrmCencInfoMode枚举类型，表示cencInfo中keyId/iv/subsample信息是否设置。

#### 宏定义

名称描述DRM_KEY_ID_SIZE 16

Key id长度为16字节。

**起始版本：** 12

DRM_KEY_IV_SIZE 16

Iv长度为16字节。

**起始版本：** 12

DRM_KEY_MAX_SUB_SAMPLE_NUM 64

最大的Subsample数量为64个。

**起始版本：** 12

#### 函数

名称描述[OH_AVCencInfo *OH_AVCencInfo_Create()](#ZH-CN_TOPIC_0000002497605744__oh_avcencinfo_create)创建用于设置cencInfo的OH_AVCencInfo实例。[OH_AVErrCode OH_AVCencInfo_Destroy(OH_AVCencInfo *cencInfo)](#ZH-CN_TOPIC_0000002497605744__oh_avcencinfo_destroy)

销毁OH_AVCencInfo实例并释放内部资源。

 同一个实例只能销毁一次。在再次创建实例之前，不应使用该实例。建议在实例销毁成功后立即将实例指针设置为nullptr。

[OH_AVErrCode OH_AVCencInfo_SetAlgorithm(OH_AVCencInfo *cencInfo, enum DrmCencAlgorithm algo)](#ZH-CN_TOPIC_0000002497605744__oh_avcencinfo_setalgorithm)设置cencInfo加密算法。[OH_AVErrCode OH_AVCencInfo_SetKeyIdAndIv(OH_AVCencInfo *cencInfo, uint8_t *keyId, uint32_t keyIdLen, uint8_t *iv, uint32_t ivLen)](#ZH-CN_TOPIC_0000002497605744__oh_avcencinfo_setkeyidandiv)设置cencInfo的keyId和iv。[OH_AVErrCode OH_AVCencInfo_SetSubsampleInfo(OH_AVCencInfo *cencInfo, uint32_t encryptedBlockCount, uint32_t skippedBlockCount, uint32_t firstEncryptedOffset, uint32_t subsampleCount, DrmSubsample *subsamples)](#ZH-CN_TOPIC_0000002497605744__oh_avcencinfo_setsubsampleinfo)设置cencInfo的subsamples信息。[OH_AVErrCode OH_AVCencInfo_SetMode(OH_AVCencInfo *cencInfo, enum DrmCencInfoMode mode)](#ZH-CN_TOPIC_0000002497605744__oh_avcencinfo_setmode)设置cencInfo的模式。[OH_AVErrCode OH_AVCencInfo_SetAVBuffer(OH_AVCencInfo *cencInfo, OH_AVBuffer *buffer)](#ZH-CN_TOPIC_0000002497605744__oh_avcencinfo_setavbuffer)将cencInfo设置到AVBuffer。

#### 枚举类型说明

#### DrmCencAlgorithm

```ets
enum DrmCencAlgorithm
```

**描述**

Drm CENC算法类型。

**起始版本：** 12

枚举项描述DRM_ALG_CENC_UNENCRYPTED = 0x0不加密算法。DRM_ALG_CENC_AES_CTR = 0x1AES CTR算法。DRM_ALG_CENC_AES_WV = 0x2AES WV算法。DRM_ALG_CENC_AES_CBC = 0x3AES CBC算法。DRM_ALG_CENC_SM4_CBC = 0x4SM4 CBC算法。DRM_ALG_CENC_SM4_CTR = 0x5SM4 CTR算法。

#### DrmCencInfoMode

```ets
enum DrmCencInfoMode
```

**描述**

枚举类型，表示cencInfo中keyId/iv/subsample信息是否设置。

**起始版本：** 12

枚举项描述DRM_CENC_INFO_KEY_IV_SUBSAMPLES_SET = 0x0keyId/iv/subsample信息已设置。DRM_CENC_INFO_KEY_IV_SUBSAMPLES_NOT_SET = 0x1keyId/iv/subsample信息未设置。

#### 函数说明

#### OH_AVCencInfo_Create()

```ets
OH_AVCencInfo *OH_AVCencInfo_Create()
```

**描述**

创建用于设置cencInfo的OH_AVCencInfo实例。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 12

**返回：**

类型说明[OH_AVCencInfo](OH_AVCencInfo.md) *

返回新创建的OH_AVCencInfo对象。如果返回nullptr，则表示创建对象失败。

 可能失败的原因：应用程序地址空间已满，或者对象中的数据初始化失败。

#### OH_AVCencInfo_Destroy()

```ets
OH_AVErrCode OH_AVCencInfo_Destroy(OH_AVCencInfo *cencInfo)
```

**描述**

销毁OH_AVCencInfo实例并释放内部资源。

 同一个实例只能销毁一次。在再次创建实例之前，不应使用该实例。建议在实例销毁成功后立即将实例指针设置为nullptr。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 12

**参数：**

参数项描述[OH_AVCencInfo](OH_AVCencInfo.md) *cencInfo指向OH_AVCencInfo实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：cencInfo为空。

#### OH_AVCencInfo_SetAlgorithm()

```ets
OH_AVErrCode OH_AVCencInfo_SetAlgorithm(OH_AVCencInfo *cencInfo, enum DrmCencAlgorithm algo)
```

**描述**

设置cencInfo加密算法。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 12

**参数：**

参数项描述[OH_AVCencInfo](OH_AVCencInfo.md) *cencInfo指向OH_AVCencInfo实例的指针。[enum DrmCencAlgorithm](#ZH-CN_TOPIC_0000002497605744__drmcencalgorithm) algo加密算法模式。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：cencInfo为空。

#### OH_AVCencInfo_SetKeyIdAndIv()

```ets
OH_AVErrCode OH_AVCencInfo_SetKeyIdAndIv(OH_AVCencInfo *cencInfo, uint8_t *keyId, uint32_t keyIdLen, uint8_t *iv, uint32_t ivLen)
```

**描述**

设置cencInfo的keyId和iv。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 12

**参数：**

参数项描述[OH_AVCencInfo](OH_AVCencInfo.md) *cencInfo指向OH_AVCencInfo实例的指针。uint8_t *keyIdKey标识。uint32_t keyIdLenKey标识长度。uint8_t *iv初始化向量。uint32_t ivLen初始化向量长度。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：cencInfo为空、keyId为空、keyIdLen != DRM_KEY_ID_SIZE、iv是空、ivLen != DRM_KEY_IV_SIZE、keyId拷贝失败，或者iv拷贝失败。

#### OH_AVCencInfo_SetSubsampleInfo()

```ets
OH_AVErrCode OH_AVCencInfo_SetSubsampleInfo(OH_AVCencInfo *cencInfo, uint32_t encryptedBlockCount, uint32_t skippedBlockCount, uint32_t firstEncryptedOffset, uint32_t subsampleCount, DrmSubsample *subsamples)
```

**描述**

设置cencInfo的subsamples信息。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 12

**参数：**

参数项描述[OH_AVCencInfo](OH_AVCencInfo.md) *cencInfo指向OH_AVCencInfo实例的指针。uint32_t encryptedBlockCount加密块的数量。uint32_t skippedBlockCount不加密块的数量。uint32_t firstEncryptedOffset第一个加密有效负载的偏移量。uint32_t subsampleCountSubsample数量。[DrmSubsample](DrmSubsample.md) *subsamplesSubsample内容集。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：cencInfo为空、subsampleCount > DRM_KEY_MAX_SUB_SAMPLE_NUM，或者subsamples为空。

#### OH_AVCencInfo_SetMode()

```ets
OH_AVErrCode OH_AVCencInfo_SetMode(OH_AVCencInfo *cencInfo, enum DrmCencInfoMode mode)
```

**描述**

设置cencInfo的模式。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 12

**参数：**

参数项描述[OH_AVCencInfo](OH_AVCencInfo.md) *cencInfo指向OH_AVCencInfo实例的指针。[enum DrmCencInfoMode](#ZH-CN_TOPIC_0000002497605744__drmcencinfomode) modecencInfo模式，指示是否设置了keyId/iv/subsample。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：cencInfo为空。

#### OH_AVCencInfo_SetAVBuffer()

```ets
OH_AVErrCode OH_AVCencInfo_SetAVBuffer(OH_AVCencInfo *cencInfo, OH_AVBuffer *buffer)
```

**描述**

将cencInfo设置到AVBuffer。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 12

**参数：**

参数项描述[OH_AVCencInfo](OH_AVCencInfo.md) *cencInfo指向OH_AVCencInfo实例的指针。[OH_AVBuffer](OH_AVBuffer.md) *buffer携带数据的帧buffer。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：cencInfo为空、buffer为空、buffer->buffer_为空，或者buffer->buffer_->meta_为空。