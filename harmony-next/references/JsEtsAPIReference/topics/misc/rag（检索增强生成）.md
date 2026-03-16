# rag（检索增强生成）

本模块提供创建和关闭会话（[RagSession](#section1312212528516)）、流式请求大语言模型（[ChatLLM](#section1400115191116)）以及流式问答（[streamRun](#section178721756950)）的能力。

**起始版本：**6.0.0(20)

#### 导入模块

```ets
import { rag } from '@kit.DataAugmentationKit';
```

#### LLMStreamAnswer

大模型流式问答的单次结果。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.DataAugmentation.RAG

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

isFinished

boolean

否

否

表示LLM（Large Language Model，大语言模型）流式输出是否已经结束。true表示已结束，false表示后续还有答案输出。

chunk

string

否

否

表示LLM流式输出过程中单轮返回的chunk（被拆分后的文本单元）内容。单轮流式返回结果无固定上限，单次问答所有流式返回结果长度上限为8192字节。

err

[BusinessError](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#businesserror)<string>

否

是

表示LLM流式输出过程中出现的错误。[code](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#businesserror)取值范围为[1021011000, 1021012000)，超过范围则会报错[1021000000](../../errors/ArkTS API错误码.md#section16205152494111)。基类必选参数name和message的长度上限为1000字符，超出部分将被截断。不带本参数则认为无错误发生。

#### LLMRequestStatus

流式请求大语言模型请求状态的枚举值。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.DataAugmentation.RAG

**起始版本：**6.0.0(20)

名称

值

说明

LLM_SUCCESS

0

请求LLM成功。

LLM_REQUEST_ERROR

1

请求错误。

LLM_LOAD_FAILED

2

LLM加载失败。

LLM_TIMEOUT

3

LLM请求超时。

LLM_BUSY

4

LLM繁忙。

#### LLMRequestInfo

流式请求大语言模型请求结果的信息。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.DataAugmentation.RAG

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

chatId

number

否

否

表示大模型的请求ID。

status

[LLMRequestStatus](#section19522153218174)

否

否

表示[streamChat](#section157381918121212)请求的状态。

#### ChatLLM

用于请求大模型的抽象类。开发者需继承此类并根据业务逻辑实现各接口逻辑。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.DataAugmentation.RAG

**起始版本：**6.0.0(20)

#### streamChat

abstract streamChat(query: string, callback: Callback<LLMStreamAnswer>): Promise<LLMRequestInfo>

流式请求大语言模型，用于与大语言模型交互。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.DataAugmentation.RAG

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

query

string

是

与大模型交互时的请求内容，根据输入问题、问题预处理、检索等结果动态拼接，最大长度为20000字节。

**说明：**其中已带有需要带给大模型的提示prompt，无需额外附加内容，且提示prompt中的示例数据均只是提示大模型按照预期输出的模拟数据，无其他额外用途。

callback

[Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#callback)<[LLMStreamAnswer](#section178144421252)>

是

将与大语言模型交互后得到的结果返回给RAG基础框架的回调。

**返回值：**

类型

说明

Promise<[LLMRequestInfo](#section1816505018227)>

Promise对象，返回LLM请求信息对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { http } from '@kit.NetworkKit';
import { rag } from '@kit.DataAugmentationKit';

class MyChatLLM extends rag.ChatLLM {
  httpRequest: http.HttpRequest | null = http.createHttp();
  cancel(chatId: number) {
    // 请开发者按需实现chatId与请求之前的映射关系，取消时请取消chatId相应的请求
    this.httpRequest?.off('dataReceive');
  }
  async streamChat(query: string, callback: Callback<rag.LLMStreamAnswer>): Promise<rag.LLMRequestInfo> {
    let info: rag.LLMRequestInfo = {
      chatId: 0,
      status: rag.LLMRequestStatus.LLM_SUCCESS,
    };
    try {
      // 此处开发者可自行选择想要使用的大语言模型以及对应实现
      // 假设通过httpRequest.on('dataReceive', callback)从大语言模型得到了答案：
      let err: BusinessError<string> = {
        code: 1021011000,  // 自定义错误码，取值范围[1021011000, 1021012000)
        name: 'Fill custom error name here',  // 超出1000字符部分将被截断
        message: 'Fill custom error message here'  // 超出1000字符部分将被截断
      }
      let answer: rag.LLMStreamAnswer = {
        isFinished: true,  // 可根据大语言模型回复进行判断，如果是最后一条回复则为true，反之则为false
        chunk: 'This is the last chunk',
        err: err
      }
      callback(answer);
    } catch (err) {
      // 此处示例统一返回LLM_REQUEST_ERROR，开发者可根据需要判断err.code并返回相应LLMRequestStatus
      info.status = rag.LLMRequestStatus.LLM_REQUEST_ERROR;
    }
    return info;
  }
}
```

#### cancel

abstract cancel(chatId: number): void

取消流式请求大语言模型，用于暂停与大语言模型交互。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.DataAugmentation.RAG

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

chatId

number

是

需要被取消的请求LLM的ID。与[streamChat](#section157381918121212)返回值[LLMRequestInfo](#section1816505018227)中填入的chatId保持一致。

**示例：**

```ets
import { http } from '@kit.NetworkKit';
import { rag } from '@kit.DataAugmentationKit';

class MyChatLLM extends rag.ChatLLM {
  httpRequest: http.HttpRequest | null = http.createHttp();
  cancel(chatId: number) {
    // 请开发者按需实现chatId与请求之前的映射关系，取消时请取消chatId相应的请求
    this.httpRequest?.off('dataReceive');
  }
  async streamChat(query: string, callback: Callback<rag.LLMStreamAnswer>): Promise<rag.LLMRequestInfo> {
    // 省略streamChat实现，其具体使用见streamChat接口说明
    return {
      chatId: 0,
      status: rag.LLMRequestStatus.LLM_SUCCESS,
    };
  }
}
```

#### Config

会话的配置项。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.DataAugmentation.RAG

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

llm

[ChatLLM](#section1400115191116)

否

否

表示[ChatLLM](#section1400115191116)的提供者。

retrievalConfig

[retrieval.RetrievalConfig](retrieval（检索器）.md#section95236010016)

否

否

表示检索使用的配置。

retrievalCondition

[retrieval.RetrievalCondition](retrieval（检索器）.md#section4881955192413)

否

否

表示检索的条件。

**示例：**

```ets
import { rag, retrieval } from '@kit.DataAugmentationKit';
// MyChatLlm对应文件，是自定义实现的rag.ChatLLM类MyChatLLM所在的文件，具体实现见ChatLLM章节示例
import MyChatLLM from './MyChatLlm';

let retrievalConfig: retrieval.RetrievalConfig = {
  channelConfigs: [/*假设已经按需配置*/]
};

let retrievalCondition: retrieval.RetrievalCondition = {
  recallConditions: [/*假设已经按需配置*/]
};

let config: rag.Config = {
  llm: new MyChatLLM(),
  retrievalConfig: retrievalConfig,
  retrievalCondition: retrievalCondition
};
```

#### Answer

流式问答的数据。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.DataAugmentation.RAG

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

chunk

string

否

否

表示答案的片段。长度上限为8192字节。

data

Array<[retrieval.ItemInfo](retrieval（检索器）.md#section17768581101)>

否

是

表示检索的匹配结果。

#### StreamType

流式问答回答的类型。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.DataAugmentation.RAG

**起始版本：**6.0.0(20)

名称

值

说明

THOUGHT

0

思考过程数据。

REFERENCE

1

检索到的文档或知识的来源。

ANSWER

2

生成的内容的最终结果。

#### Stream

流式问答中一次回答的结果信息。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.DataAugmentation.RAG

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

type

[StreamType](#section172106569558)

否

否

表示答案的数据类型。

answer

[Answer](#section1473315119532)

否

否

表示答案的数据。

isFinished

boolean

否

否

表示流输出是否结束。true表示本轮问答已结束，false表示本轮本轮问答还有后续回答。

#### RunConfig

流式问答的配置项。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.DataAugmentation.RAG

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

answerTypes

Array<[StreamType](#section172106569558)>

否

否

用于指定流式输出的数据类型。

#### FeedbackInfo

用户评价信息。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.DataAugmentation.RAG

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

runId

number

否

否

会话内特定流式问答的唯一标识符。

score

number

否

否

用户对返回答案的评分。取值范围：[1, 5]。

source

Record<[StreamType](#section172106569558), [Answer](#section1473315119532)>

否

是

用户采用的答案信息。

comment

string

否

是

用户反馈的文本信息。长度上限为1000字节。

#### RagSession

RAG会话，用以提供基于知识库的智能问答能力。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.DataAugmentation.RAG

**起始版本：**6.0.0(20)

#### streamRun

streamRun(question: string, config: RunConfig, callback: AsyncCallback<Stream>): Promise<number>

流式问答，答案是流式传输的，使用Promise异步回调。不支持多线程调用。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.DataAugmentation.RAG

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

question

string

是

表示本次提出的问题。长度上限为1000字节。

config

[RunConfig](#section126313912116)

是

表示本次提问的配置。

callback

[AsyncCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#asynccallback)<[Stream](#section158611717585)>

是

表示用于接受回答的回调。**注意：**streamRun的完整生命周期包含完整的callback执行。结束的callback回调执行过程中，streamRun的生命周期仍然在持续，在此时进行新的streamRun或者cancel/close操作，都可能产生针对streamRun仍然在进行中的对应错误。

**返回值：**

类型

说明

Promise<number>

Promise对象，返回本次调用的ID。

**错误码：**

 以下错误码的详细介绍请参见 [通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和 [数据增强错误码](../../errors/ArkTS API错误码 (dataaugmentation-error-code).md)。

错误码ID

错误信息

[1021000000](../../errors/ArkTS API错误码.md#section16205152494111)

Insufficient system resources or memory access exception.

[1021000001](../../errors/ArkTS API错误码.md#section067520119311)

A timeout occurred when calling the LLM.

[1021000002](../../errors/ArkTS API错误码.md#section398619111131)

A loading failure occurred when calling the LLM.

[1021000003](../../errors/ArkTS API错误码.md#section821961514310)

A request failure occurred when calling the LLM.

[1021000004](../../errors/ArkTS API错误码.md#section57321151039)

The LLM chat is busy.

[1021000005](../../errors/ArkTS API错误码.md#section151441316239)

The output of LLM chat does not comply with the constraints.

[1021000007](../../errors/ArkTS API错误码.md#section1787571610312)

The RAG session is busy.

[1021000008](../../errors/ArkTS API错误码.md#section16220417239)

The RAG session is Already closed.

[1021000009](../../errors/ArkTS API错误码.md#section12582191715318)

User has canceled the stream run.

[1021000010](../../errors/ArkTS API错误码.md#section13942117932)

A timeout occurred in the session.

[1021000011](../../errors/ArkTS API错误码.md#section3292318836)

Some parameter does not meet the constraints. Possible causes:

1. The length of the string parameter or the length of the numeric parameter does not comply with the constraints.

2. The string parameter contains invalid characters.

[1021000012](../../errors/ArkTS API错误码.md#section666413181639)

The knowledge base is not available.

[1021000013](../../errors/ArkTS API错误码.md#section138151918312)

Retrieval: An error occurred during the Retrieval.

[1021000014](../../errors/ArkTS API错误码.md#section193969191335)

Retrieval: There are invalid primary keys.

[1021000015](../../errors/ArkTS API错误码.md#section1273420195316)

Retrieval: A re-ranking algorithm that does not support composite primary keys was used.

[1021000016](../../errors/ArkTS API错误码.md#section576320538)

Retrieval: The filter input is invalid.

[1021000017](../../errors/ArkTS API错误码.md#section145418202032)

Retrieval: There are invalid recall names in RecallCondition.

[1021000018](../../errors/ArkTS API错误码.md#section78131820938)

Retrieval: The vector similarity threshold in VectorQuery is higher than the tiered threshold in VectorRerankParameter.

[1021000019](../../errors/ArkTS API错误码.md#section161717215314)

Retrieval: RerankMethod parameters do not match the channel type.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { rag } from '@kit.DataAugmentationKit';

let session: rag.RagSession | null;

let runConfig: rag.RunConfig = {
  answerTypes: [ rag.StreamType.THOUGHT, rag.StreamType.REFERENCE, rag.StreamType.ANSWER ]
};

let output: string = '';

if (session != null) {
  session.streamRun('提出的问题', runConfig, ((err: BusinessError, stream: rag.Stream) => {
    if (err) {
      hilog.error(0, 'test', `streamRun inner failed. code is ${err.code}, message is ${err.message}`);
    } else {
      hilog.info(0, 'Index', 'StreamType: %{public}d', stream.type);
      output += stream.answer.chunk;
      if (stream.isFinished) {
        output += '回答结束。';
      }
    }
  })).then((data) => {
    hilog.info(0, 'Index', 'runId: %{public}d', data);
  }).catch((e: BusinessError) => {
    hilog.error(0, 'test', `streamRun failed. code is ${e.code}, message is ${e.message}`);
  });
}
```

#### cancel

cancel(runId: number): Promise<void>

取消本次问答，使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.DataAugmentation.RAG

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

runId

number

是

表示需要取消的问答ID。与[streamRun](#section178721756950)返回值保持一致。

**返回值：**

类型

说明

Promise<void>

Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[数据增强错误码](../../errors/ArkTS API错误码 (dataaugmentation-error-code).md)。

错误码ID

错误信息

[1021000000](../../errors/ArkTS API错误码.md#section16205152494111)

Insufficient system resources or memory access exception.

[1021000008](../../errors/ArkTS API错误码.md#section16220417239)

The RAG session is Already closed.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { rag } from '@kit.DataAugmentationKit';

let session: rag.RagSession | null;

if (session != null) {
  let runId: number = 0;  // 请开发者填入streamRun实际返回值
  session.cancel(runId).then(() => {
    hilog.info(0, 'test', 'cancel successfully');
  }).catch((e: BusinessError) => {
    hilog.error(0, 'test', `cancel failed. code is ${e.code}, message is ${e.message}`);
  });
}
```

#### close

close(): Promise<void>

关闭会话，使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.DataAugmentation.RAG

**起始版本：**6.0.0(20)

**返回值：**

类型

说明

Promise<void>

Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[数据增强错误码](../../errors/ArkTS API错误码 (dataaugmentation-error-code).md)。

错误码ID

错误信息

[1021000000](../../errors/ArkTS API错误码.md#section16205152494111)

Insufficient system resources or memory access exception.

**示例：**

```ets
import { rag } from '@kit.DataAugmentationKit';

let session: rag.RagSession | null;

onWindowStageDestroy(): void {
  // Main window is destroyed, release UI related resources
  hilog.info(0, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');

  if (session != null) {
    session.close();
  }
}
```

#### createRagSession

createRagSession(context: common.Context, config: Config): Promise<RagSession>

获得一个会话，使用Promise异步回调。不支持多线程调用。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.DataAugmentation.RAG

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)

是

表示当前应用上下文。

config

[Config](#section1033315317182)

是

表示与此[RagSession](#section1312212528516)相关的配置。

**返回值：**

类型

说明

Promise<[RagSession](#section1312212528516)>

Promise对象，返回[RagSession](#section1312212528516)对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[数据增强错误码](../../errors/ArkTS API错误码 (dataaugmentation-error-code).md)。

错误码ID

错误信息

[1021000000](../../errors/ArkTS API错误码.md#section16205152494111)

Insufficient system resources or memory access exception.

[1021000006](../../errors/ArkTS API错误码.md#section34911416737)

The RAG session already exists.

**示例：**

```ets
import { AbilityConstant, ConfigurationConstant, UIAbility, Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { rag, retrieval } from '@kit.DataAugmentationKit';
import { window } from '@kit.ArkUI';
// MyChatLlm对应文件，是自定义实现的rag.ChatLLM类MyChatLLM所在的文件，具体实现见ChatLLM章节示例
import MyChatLLM from './MyChatLlm';

let session: rag.RagSession | null;

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
    });

    let retrievalConfig: retrieval.RetrievalConfig = {
      channelConfigs: [/*假设已经按需配置*/]
    };

    let retrievalCondition: retrieval.RetrievalCondition = {
      recallConditions: [/*假设已经按需配置*/]
    };

    let config: rag.Config = {
      llm: new MyChatLLM(),
      retrievalConfig: retrievalConfig,
      retrievalCondition: retrievalCondition
    };

    rag.createRagSession(this.context, config).then((result) => {
      session = result;
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', `createRagSession failed, code is ${err.code},message is ${err.message}.`);
    })
  }
}
```

#### feedback

feedback(context: common.Context, feedbackInfo: FeedbackInfo): Promise<void>

用户评价接口。用户问答结束之后，可以使用该接口对此次问答进行评价。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.DataAugmentation.RAG

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)

是

表示当前应用上下文。

feedbackInfo

[FeedbackInfo](#section18123940144515)

是

表示用户反馈的信息。

**返回值：**

类型

说明

Promise<void>

Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[数据增强错误码](../../errors/ArkTS API错误码 (dataaugmentation-error-code).md)。

错误码ID

错误信息

[1021000000](../../errors/ArkTS API错误码.md#section16205152494111)

Insufficient system resources or memory access exception.

[1021000011](../../errors/ArkTS API错误码.md#section3292318836)

Some parameter does not meet the constraints. Possible causes:

1. The length of the string parameter or the length of the numeric parameter does not comply with the constraints.

2. The string parameter contains invalid characters.

**示例：**

```ets
import { rag, retrieval } from '@kit.DataAugmentationKit';
import { relationalStore } from '@kit.ArkData';
import common from '@ohos.app.ability.common';

let context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;

async function feedback() {
  let valueTypeA: relationalStore.ValueType = 1;
  let valueTypeRecord: Record<string, relationalStore.ValueType> = {
    'a': valueTypeA,
    'b': valueTypeA,
  };
  let recallScoreA: retrieval.RecallScore = {
    score: 0,
    isReverseQuery: false
  };
  let recallScoreRecord: Record<string, retrieval.RecallScore> = {
    'a': recallScoreA,
    'b': recallScoreA,
    'c': recallScoreA
  };

  let channelTypeRecord: Record<number, Record<string, retrieval.RecallScore>> = {
    0: recallScoreRecord,
    1: recallScoreRecord
  };

  let itemInfo: retrieval.ItemInfo = {
    primaryKey: '',
    columns: valueTypeRecord,
    score: 0,
    recallScores: channelTypeRecord,
    features: {
      '111': 1,
      '222': 2
    },
    similarityLevel: retrieval.SimilarityLevel.LOW
  };
  let answerB: rag.Answer = {
    chunk: '111',
    data: [itemInfo]
  };
  let sources: Record<number, rag.Answer> = {
    0: answerB,
    1: answerB,
    2: answerB,
  };
  let feedbackInfo: rag.FeedbackInfo = {
    runId: 444,
    score: 5,
    comment: '111222333',
    source: sources
  };
  await rag.feedback(context, feedbackInfo);
}
```
