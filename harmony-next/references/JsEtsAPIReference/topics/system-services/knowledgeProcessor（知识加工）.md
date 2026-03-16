# knowledgeProcessor（知识加工）

本模块提供获取知识加工对象（KnowledgeProcessor）以及获取知识加工状态（ProcessorStatus）的能力。

**起始版本：**6.0.0(20)

#### 导入模块

```ets
import { knowledgeProcessor } from '@kit.DataAugmentationKit';
```

#### getKnowledgeProcessor

getKnowledgeProcessor(context: common.BaseContext, config: KnowledgeProcessorConfig): Promise<KnowledgeProcessor>

获取知识加工对象，用于获取知识加工状态。

**系统能力：** SystemCapability.DataAugmentation.KnowledgeProcessor

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

context

[common.BaseContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-basecontext)

是

知识加工对象的上下文。

config

[KnowledgeProcessorConfig](#section7916104025215)

是

知识加工配置。

**返回值：**

类型

说明

Promise<[KnowledgeProcessor](#section395619456396)>

Promise对象，返回知识加工对象。

**错误码：**

错误码ID

错误信息

[1021400000](../../errors/ArkTS API错误码.md#section184111958125913)

Internal error.

[1021400001](../../errors/ArkTS API错误码.md#section8963194719118)

The knowledge source is not configured.

[1021400002](../../errors/ArkTS API错误码.md#section18580829439)

The knowledge schema file is not found.

[1021400003](../../errors/ArkTS API错误码.md#section581782218519)

The knowledge schema content is invalid.

[1021400004](../../errors/ArkTS API错误码.md#section0678102120612)

An error occurred during operations on the RDB source.

**示例：**

```ets
import { knowledgeProcessor } from '@kit.DataAugmentationKit';
import { common } from '@kit.AbilityKit';
import { relationalStore } from '@kit.ArkData';

const storeName: string = "testmail_store.db";
const storeConfig: relationalStore.StoreConfig = {
  name: storeName, // 已触发知识加工的数据库名
  securityLevel: relationalStore.SecurityLevel.S3,
  tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER,
};
const knowledgeSourceConfig: knowledgeProcessor.KnowledgeSourceConfig = {
  rdbSource: storeConfig,
};
const knowledgeProcessorConfig: knowledgeProcessor.KnowledgeProcessorConfig = {
  sourceConfig: knowledgeSourceConfig,
};
// 获取知识加工器的异步函数
async function getProcessor() {
  const context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
  try {
    // 获取知识加工对象
    const processor = await knowledgeProcessor.getKnowledgeProcessor(context, knowledgeProcessorConfig);
    return processor;
  } catch (err) {
    console.error("Error: " + err.message + " code: " + err.code);
    return undefined;
  }
}
```

#### KnowledgeProcessorConfig

管理知识加工对象的配置。

**系统能力：**SystemCapability.DataAugmentation.KnowledgeProcessor

**起始版本：**6.0.0(20)

名称

类型

必填

说明

sourceConfig

[KnowledgeSourceConfig](#section5324144573013)

是

当前知识加工数据源配置。

#### KnowledgeSourceConfig

管理知识数据源配置。

**系统能力：**SystemCapability.DataAugmentation.KnowledgeProcessor

**起始版本：**6.0.0(20)

名称

类型

必填

说明

rdbSource

[relationalStore.StoreConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-i#storeconfig)

否

RDB数据库配置。加工数据源为RDB数据库时配置，当前版本仅支持RDB数据源，若不填该参数，接口返回错误码[1021400001](../../errors/ArkTS API错误码.md#section8963194719118)。

#### KnowledgeProcessor

知识加工对象，用于获取知识加工状态等操作。

**系统能力：**SystemCapability.DataAugmentation.KnowledgeProcessor

**起始版本：**6.0.0(20)

#### getStatus

getStatus(): Promise<ProcessorStatus>

获取知识加工状态。

**系统能力：** SystemCapability.DataAugmentation.KnowledgeProcessor

**设备行为差异：**该接口在PC/2in1设备可以正常调用，在Phone、Tablet中依赖数据源表中是否存在数据记录返回知识加工状态，如果数据源表中无数据记录返回所有数据已完成加工（DATA_PROCESSING_COMPLETE），否则返回存在待加工的数据（DATA_REMAINING_TO_PROCESS）。

**起始版本：**6.0.0(20)

**返回值：**

类型

说明

Promise<[ProcessorStatus](#section174782032163713)>

Promise对象，返回知识加工状态。

**错误码：**

**错误码ID**

**错误信息**

[1021400000](../../errors/ArkTS API错误码.md#section184111958125913)

Internal error.

[1021400004](../../errors/ArkTS API错误码.md#section0678102120612)

An error occurred during operations on the RDB source.

**示例：**

```ets
import { knowledgeProcessor } from '@kit.DataAugmentationKit';
import { common } from '@kit.AbilityKit';
import { relationalStore } from '@kit.ArkData';

const storeName: string = "testmail_store.db";
const storeConfig: relationalStore.StoreConfig = {
  name: storeName, // 已触发知识加工的数据库名
  securityLevel: relationalStore.SecurityLevel.S3,
  tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER,
};
const knowledgeSourceConfig: knowledgeProcessor.KnowledgeSourceConfig = {
  rdbSource: storeConfig,
};
const knowledgeProcessorConfig: knowledgeProcessor.KnowledgeProcessorConfig = {
  sourceConfig: knowledgeSourceConfig,
};
// 获取知识加工状态的异步函数
async function getStatus() {
  const context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
  try {
    // 获取知识加工对象
    const processor = await knowledgeProcessor.getKnowledgeProcessor(context, knowledgeProcessorConfig);
    // 获取知识加工状态
    const status: knowledgeProcessor.ProcessorStatus = await processor.getStatus();
    return status;
  } catch (err) {
    console.error("Error: " + err.message + " code: " + err.code);
    return undefined;
  }
}
```

#### ProcessorStatus

知识加工状态。

**系统能力：**SystemCapability.DataAugmentation.KnowledgeProcessor

**起始版本：**6.0.0(20)

名称

值

说明

DATA_REMAINING_TO_PROCESS

0

存在待加工的数据。

DATA_PROCESSING_IN_PROGRESS

1

数据正在进行知识加工中。

DATA_PROCESSING_COMPLETE

2

所有数据已完成加工。