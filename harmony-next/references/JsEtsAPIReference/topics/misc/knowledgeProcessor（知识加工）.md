# knowledgeProcessor（知识加工）

本模块提供获取知识加工对象（KnowledgeProcessor）以及获取知识加工状态（ProcessorStatus）的能力。

由于知识加工能力依赖的嵌入模型只支持在PC/2in1部署，因此当前知识加工能力仅支持PC/2in1设备。

起始版本： 6.0.0(20)

**导入模块**

```ets
import { knowledgeProcessor } from '@kit.DataAugmentationKit';
```

**getKnowledgeProcessor**

getKnowledgeProcessor(context: common.BaseContext, config: KnowledgeProcessorConfig): Promise<KnowledgeProcessor>

获取知识加工对象，用于获取知识加工状态等操作。

在schema升级场景下，首次开库或调用getKnowledgeProcessor接口前需调用[cleanKnowledgeData](#ZH-CN_TOPIC_0000002553201205__cleanknowledgedata)接口。

系统能力： SystemCapability.DataAugmentation.KnowledgeProcessor

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.BaseContext | 是 | 知识加工对象的上下文。 |
| config | KnowledgeProcessorConfig | 是 | 知识加工配置。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<KnowledgeProcessor> | Promise对象，返回知识加工对象。 |

错误码：

| 错误码ID | 错误信息 |
| --- | --- |
| 1021400000 | Internal error. |
| 1021400001 | The knowledge source is not configured. |
| 1021400002 | The knowledge schema file is not found. |
| 1021400003 | The knowledge schema content is invalid. |
| 1021400004 | An error occurred during operations on the RDB source. |

示例：

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
```

**cleanKnowledgeData**

cleanKnowledgeData(context: common.BaseContext, config: KnowledgeProcessorConfig): Promise<void>

根据入参中的知识加工配置获取对应知识库信息，将对应知识库进行清空。

在schema升级场景下，首次开库或调用[getKnowledgeProcessor](#ZH-CN_TOPIC_0000002553201205__getknowledgeprocessor)接口前调用cleanKnowledgeData接口，其他场景调用可能会导致知识库数据丢失或者数据损坏。

系统能力： SystemCapability.DataAugmentation.KnowledgeProcessor

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.BaseContext | 是 | 知识加工对象的上下文。 |
| config | KnowledgeProcessorConfig | 是 | 知识加工配置。 |

错误码：

| 错误码ID | 错误信息 |
| --- | --- |
| 1021400001 | The knowledge source is not configured. |
| 1021400002 1021400003 1021400004 | The knowledge schema file is not found. The knowledge schema content is invalid. An error occurred during operations on the RDB source. |

示例：

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
// 清理知识库的异步函数
async function cleanKnowledgeData() {
  const context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
  try {
    // 清理知识库
    await knowledgeProcessor.cleanKnowledgeData(context, knowledgeProcessorConfig);
  } catch (err) {
    console.error("Error: " + err.message + " code: " + err.code);
    return undefined;
  }
```

**KnowledgeProcessorConfig**

管理知识加工对象的配置。

系统能力： SystemCapability.DataAugmentation.KnowledgeProcessor

起始版本： 6.0.0(20)

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sourceConfig | KnowledgeSourceConfig | 是 | 当前知识加工数据源配置。 |

**KnowledgeSourceConfig**

管理知识数据源配置。

系统能力： SystemCapability.DataAugmentation.KnowledgeProcessor

起始版本： 6.0.0(20)

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | relationalStore.StoreConfig | 否 | RDB数据库配置。加工数据源为RDB数据库时配置，当前版本仅支持RDB数据源，若不填该参数，接口返回错误码1021400001。 |

**KnowledgeProcessConfig**

知识加工配置。

系统能力： SystemCapability.DataAugmentation.KnowledgeProcessor

起始版本： 6.1.0(23)

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | KnowledgeProcessorMode | 是 | 知识加工参数。倒排或者倒排+向量两种加工模式. |

**KnowledgeProcessorMode**

知识加工模式。

系统能力： SystemCapability.DataAugmentation.KnowledgeProcessor

起始版本： 6.1.0(23)

| 名称 | 说明 |
| --- | --- |
| INVERTED_INDEX | 倒排加工模式。 |
| INVERTED_INDEX_VECTORIZATION | 倒排＋向量加工模式。 |

**KnowledgeProcessor**

知识加工对象，用于获取知识加工状态等操作。

系统能力： SystemCapability.DataAugmentation.KnowledgeProcessor

起始版本： 6.0.0(20)

**getStatus**

getStatus(): Promise<ProcessorStatus>

获取知识加工状态。

系统能力： SystemCapability.DataAugmentation.KnowledgeProcessor

起始版本： 6.0.0(20)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<ProcessorStatus> | Promise对象，返回知识加工状态。 |

错误码：

| 错误码ID | 错误信息 |
| --- | --- |
| 1021400000 | Internal error. |
| 1021400004 | An error occurred during operations on the RDB source. |

示例：

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
```

**startProcess**

startProcess(config: KnowledgeProcessConfig): Promise<void>

根据入参的配置，启动知识加工。

系统能力： SystemCapability.DataAugmentation.KnowledgeProcessor

起始版本： 6.1.0(23)

错误码：

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Device type error. |
| 1021400000 | Internal error. |
| 1021400005 | Feature already active. Function called repeatedly. |

示例：

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
// 启动知识加工的异步函数
async function startProcess() {
  const context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
  try {
    // 获取知识加工对象
    const processor = await knowledgeProcessor.getKnowledgeProcessor(context, knowledgeProcessorConfig);
    // 启动知识加工
    let processMode: knowledgeProcessor.KnowledgeProcessMode = knowledgeProcessor.KnowledgeProcessMode.INVERTED_INDEX;
    let config: knowledgeProcessor.KnowledgeProcessConfig = {
      mode: processMode,
    };
    await processor.startProcess(config);
  } catch (err) {
    console.error("Error: " + err.message + " code: " + err.code);
  }
```

**stopProcess**

stopProcess(): Promise<void>

停止当前知识加工。

系统能力： SystemCapability.DataAugmentation.KnowledgeProcessor

起始版本： 6.1.0(23)

示例：

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
// 停止知识加工的异步函数
async function stopProcess() {
  const context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
  try {
    // 获取知识加工对象
    const processor = await knowledgeProcessor.getKnowledgeProcessor(context, knowledgeProcessorConfig);
    // 停止知识加工
    await processor.stopProcess();
  } catch (err) {
    console.error("Error: " + err.message + " code: " + err.code);
  }
```

**ProcessorStatus**

知识加工状态。

系统能力： SystemCapability.DataAugmentation.KnowledgeProcessor

起始版本： 6.0.0(20)

| 名称 | 说明 |
| --- | --- |
| DATA_REMAINING_TO_PROCESS | 存在待加工的数据。 |
| DATA_PROCESSING_IN_PROGRESS | 数据正在进行知识加工中。 |
| DATA_PROCESSING_COMPLETE | 所有数据已完成加工。 |