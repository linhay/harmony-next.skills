# @ohos.data.intelligence (智慧数据平台)

智慧数据平台（ArkData Intelligence Platform，AIP）提供端侧数据智慧化构建，使应用数据向量化，通过嵌入模型将非结构化的文本、图像等多模态数据，转换成具有语义的向量。

本模块首批接口从API version 15开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

考虑到数据向量化处理的计算量和资源占用较大，当前仅支持在2in1设备上使用。

#### 导入模块

```ets
import { intelligence } from '@kit.ArkData';
```

#### intelligence.getTextEmbeddingModel

getTextEmbeddingModel(config: ModelConfig): Promise<TextEmbedding>

获取文本嵌入模型。使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备类型中返回801错误码。

**参数：**

参数名类型必填说明config[ModelConfig](#ZH-CN_TOPIC_0000002529444655__modelconfig)是嵌入模型的配置信息。

**返回值：**

类型说明Promise<[TextEmbedding](#ZH-CN_TOPIC_0000002529444655__textembedding)>Promise对象，返回文本嵌入模型对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[智慧数据平台错误码](../../errors/智慧数据平台错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.801Capability not supported.31300000Inner error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let textConfig:intelligence.ModelConfig = {
  version:intelligence.ModelVersion.BASIC_MODEL,
  isNpuAvailable:false,
  cachePath:"/data"
}
let textEmbedding:intelligence.TextEmbedding;

intelligence.getTextEmbeddingModel(textConfig)
  .then((data:intelligence.TextEmbedding) => {
    console.info("Succeeded in getting TextModel");
    textEmbedding = data;
  })
  .catch((err:BusinessError) => {
    console.error("Failed to get TextModel and code is " + err.code);
  })
```

#### intelligence.getImageEmbeddingModel

getImageEmbeddingModel(config: ModelConfig): Promise<ImageEmbedding>

获取图像嵌入模型。使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备类型中返回801错误码。

**参数：**

参数名类型必填说明config[ModelConfig](#ZH-CN_TOPIC_0000002529444655__modelconfig)是嵌入模型的配置信息。

**返回值：**

类型说明Promise<[ImageEmbedding](#ZH-CN_TOPIC_0000002529444655__imageembedding)>Promise对象，返回图像嵌入模型对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[智慧数据平台错误码](../../errors/智慧数据平台错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.801Capability not supported.31300000Inner error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let imageConfig:intelligence.ModelConfig = {
    version:intelligence.ModelVersion.BASIC_MODEL,
    isNpuAvailable:false,
    cachePath:"/data"
}
let imageEmbedding:intelligence.ImageEmbedding;

intelligence.getImageEmbeddingModel(imageConfig)
  .then((data:intelligence.ImageEmbedding) => {
    console.info("Succeeded in getting ImageModel");
    imageEmbedding = data;
  })
  .catch((err:BusinessError) => {
    console.error("Failed to get ImageModel and code is " + err.code);
  })
```

#### intelligence.splitText

splitText(text: string, config: SplitConfig): Promise<Array<string>>

获取文本的分块。使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备类型中返回801错误码。

**参数：**

参数名类型必填说明textstring是用于分块的文本，可取任意值。config[SplitConfig](#ZH-CN_TOPIC_0000002529444655__splitconfig)是文本分块的配置信息。

**返回值：**

类型说明Promise<Array<string>>Promise对象，返回分块结果的数组对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[智慧数据平台错误码](../../errors/智慧数据平台错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.801Capability not supported.31300000Inner error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let splitConfig:intelligence.SplitConfig = {
  size:10,
  overlapRatio:0.1
}
let splitText = 'text';

intelligence.splitText(splitText, splitConfig)
  .then((data:Array<string>) => {
    console.info("Succeeded in splitting Text");
  })
  .catch((err:BusinessError) => {
    console.error("Failed to split Text and code is " + err.code);
  })
```

#### ModelConfig

管理嵌入模型的配置信息。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

名称类型只读可选说明version[ModelVersion](#ZH-CN_TOPIC_0000002529444655__modelversion)否否模型的版本。isNpuAvailableboolean否否指示是否使用NPU加速向量化过程，true表示使用，false表示不使用。如果设备不支持NPU，调用加载模型会失败，并抛出错误码31300000。cachePathstring否是如果使用NPU进行加速，则需要本地路径进行模型缓存。格式为/xxx/xxx/xxx，xxx为路径地址，例如"/data"。长度上限为512个字符。默认值为""。

#### ModelVersion

模型版本枚举。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

名称值说明BASIC_MODEL0基本嵌入模型版本。

#### Image

type Image = string

表示图片的URI地址，对应为string类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

类型说明string图片的URI地址。长度上限为512个字符。

#### SplitConfig

管理文本分块的配置信息。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

名称类型只读可选说明sizenumber否否分块的最大大小，取值为非负整数。overlapRationumber否否相邻分块之间的重叠比率。范围为[0,1]，0表示重叠比率最低，1表示重叠比率最高。

#### TextEmbedding

描述多模态嵌入模型的文本嵌入函数。

下列接口都需先使用[intelligence.getTextEmbeddingModel](#ZH-CN_TOPIC_0000002529444655__intelligencegettextembeddingmodel)获取到TextEmbedding实例，再通过此实例调用对应接口。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

#### loadModel

loadModel(): Promise<void>

加载文本嵌入模型。使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备类型中返回801错误码。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[智慧数据平台错误码](../../errors/智慧数据平台错误码.md)。

**错误码ID****错误信息**801Capability not supported.31300000Inner error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

textEmbedding.loadModel()
  .then(() => {
    console.info("Succeeded in loading Model");
  })
  .catch((err:BusinessError) => {
    console.error("Failed to load Model and code is " + err.code);
  })
```

#### releaseModel

releaseModel(): Promise<void>

释放文本嵌入模型。使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备类型中返回801错误码。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[智慧数据平台错误码](../../errors/智慧数据平台错误码.md)。

**错误码ID****错误信息**801Capability not supported.31300000Inner error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

textEmbedding.releaseModel()
  .then(() => {
    console.info("Succeeded in releasing Model");
  })
  .catch((err:BusinessError) => {
    console.error("Failed to release Model and code is " + err.code);
  })
```

#### getEmbedding

getEmbedding(text: string): Promise<Array<number>>

获取给定文本的嵌入向量。使用Promise异步回调。

该接口需先调用[loadModel](#ZH-CN_TOPIC_0000002529444655__loadmodel)加载嵌入模型，加载成功后调用getEmbedding。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备类型中返回801错误码。

**参数：**

参数名类型必填说明textstring是嵌入模型的输入文本。长度上限为512个字符。

**返回值：**

类型说明Promise<Array<number>>Promise对象，返回向量化结果的数组对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[智慧数据平台错误码](../../errors/智慧数据平台错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.801Capability not supported.31300000Inner error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

textEmbedding.loadModel();
let text = 'text';
textEmbedding.getEmbedding(text)
  .then((data:Array<number>) => {
    console.info("Succeeded in getting Embedding");
  })
  .catch((err:BusinessError) => {
    console.error("Failed to get Embedding and code is " + err.code);
  })
```

#### getEmbedding

getEmbedding(batchTexts: Array<string>): Promise<Array<Array<number>>>

获取给定批次文本的嵌入向量。使用Promise异步回调。

该接口需先调用[loadModel](#ZH-CN_TOPIC_0000002529444655__loadmodel)加载嵌入模型，加载成功后调用getEmbedding。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备类型中返回801错误码。

**参数：**

参数名类型必填说明batchTextsArray<string>是嵌入模型的文本输入批次。单个文本长度上限为512个字符。

**返回值：**

类型说明Promise<Array<Array<number>>>Promise对象，返回向量化结果的数组对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[智慧数据平台错误码](../../errors/智慧数据平台错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.801Capability not supported.31300000Inner error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

textEmbedding.loadModel();
let batchTexts = ['text1','text2'];
textEmbedding.getEmbedding(batchTexts)
  .then((data:Array<Array<number>>) => {
    console.info("Succeeded in getting Embedding");
  })
  .catch((err:BusinessError) => {
    console.error("Failed to get Embedding and code is " + err.code);
  })
```

#### ImageEmbedding

描述多模态嵌入模型的图像嵌入函数。

下列接口都需先使用[intelligence.getImageEmbeddingModel](#ZH-CN_TOPIC_0000002529444655__intelligencegetimageembeddingmodel)获取到ImageEmbedding实例，再通过此实例调用对应接口。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

#### loadModel

loadModel(): Promise<void>

加载图像嵌入模型。使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备类型中返回801错误码。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[智慧数据平台错误码](../../errors/智慧数据平台错误码.md)。

**错误码ID****错误信息**801Capability not supported.31300000Inner error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

imageEmbedding.loadModel()
  .then(() => {
    console.info("Succeeded in loading Model");
  })
  .catch((err:BusinessError) => {
    console.error("Failed to load Model and code is " + err.code);
  })
```

#### releaseModel

releaseModel(): Promise<void>

释放图像嵌入模型。使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备类型中返回801错误码。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[智慧数据平台错误码](../../errors/智慧数据平台错误码.md)。

**错误码ID****错误信息**801Capability not supported.31300000Inner error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

imageEmbedding.releaseModel()
  .then(() => {
    console.info("Succeeded in releasing Model");
  })
  .catch((err:BusinessError) => {
    console.error("Failed to release Model and code is " + err.code);
  })
```

#### getEmbedding

getEmbedding(image: Image): Promise<Array<number>>

获取给定图像的嵌入向量。使用Promise异步回调。

该接口需先调用[loadModel](#ZH-CN_TOPIC_0000002529444655__loadmodel)加载嵌入模型，加载成功后调用getEmbedding。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备类型中返回801错误码。

**参数：**

参数名类型必填说明image[Image](#ZH-CN_TOPIC_0000002529444655__image)是嵌入模型的输入图像类型的URI地址。

**返回值：**

类型说明Promise<Array<number>>Promise对象，返回向量化结果的数组对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[智慧数据平台错误码](../../errors/智慧数据平台错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.801Capability not supported.31300000Inner error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

imageEmbedding.loadModel();
let image = 'file://<packageName>/data/storage/el2/base/haps/entry/files/xxx.jpg';
imageEmbedding.getEmbedding(image)
  .then((data:Array<number>) => {
    console.info("Succeeded in getting Embedding");
  })
  .catch((err:BusinessError) => {
    console.error("Failed to get Embedding and code is " + err.code);
  })
```