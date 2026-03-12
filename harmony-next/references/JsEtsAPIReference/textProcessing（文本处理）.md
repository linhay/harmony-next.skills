# textProcessing（文本处理）

自然语言理解服务提供将输入的普通文本都标注为带词性的文本，标注每个词是名词、动词、形容词或其他词性。

还提供实体抽取功能，通过对用户输入的文本进行实体识别。然后依据Kit中的实体类别来进行分类，其中用户可以根据实体类别列表中的类别来进行选择。输出结果中包含实体的类别、实体在原文本中的位置、实体的原文本以及实体解析后的其他字段。实体字段内容可参考[EntityType](#section4298938144913)详情。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { textProcessing, EntityType } from '@kit.NaturalLanguageKit';
```

#### WordSegment

分词的输出结果，包含词语和词性。

**系统能力：**SystemCapability.AI.NaturalLanguage.TextProcessing

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

word

string

否

否

词语。

wordTag

string

否

否

词性。词性分类参考[wordTag](wordTag（词性）.md)。

#### EntityConfig

可选配置项，实体的类别。

**系统能力：**SystemCapability.AI.NaturalLanguage.TextProcessing

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

entityTypes

[EntityType](#section4298938144913)[]

否

是

实体的类别。

默认全选。

#### EntityType

实体类别的枚举类。

**系统能力：**SystemCapability.AI.NaturalLanguage.TextProcessing

**起始版本：**5.0.0(12)

名称

值

说明

DATETIME

datetime

时间实体

EMAIL

email

邮箱实体

EXPRESS_NO

expressNo

快递单号实体

FLIGHT_NO

flightNo

航班号实体

LOCATION

location

地点实体

NAME

name

姓名实体

PHONE_NO

phoneNo

手机号实体

URL

url

url实体

VERIFICATION_CODE

verificationCode

验证码实体

ID_NO

idNo

身份证号实体

#### Entity

实体抽取的结果。

**系统能力：**SystemCapability.AI.NaturalLanguage.TextProcessing

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

text

string

否

否

实体原文本。

charOffset

number

否

否

实体在原文本中的位置。所在位置以字符计算。

type

[EntityType](#section4298938144913)

否

否

实体类别。

jsonObject

string

否

否

实体的其他字段。详情参考[jsonObject](jsonObject（实体的其他字段）.md)。

#### textProcessing.getWordSegment

getWordSegment(text: string): Promise<Array<WordSegment>>

创建分词实例，并初始化引擎。使用Promise异步回调。

**系统能力：**SystemCapability.AI.NaturalLanguage.TextProcessing

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

text

string

是

输入待分析的文本内容。相关规格参考[约束与限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/natural-language-introduction#section1454714381942)。

**返回值：**

类型

说明

Promise<Array<[WordSegment](#section12706154134017)>>

Promise对象，返回分词结果的集合。

**错误码：**

以下错误码的详细介绍请参见[Natural Language Kit错误码](ArkTS API错误码.md)。

错误码ID

错误信息

200

Run timed out, please try again later.

401

The parameter check failed.

1011200001

Failed to run, please try again.

1011200002

The service is abnormal.

**示例：**

```ets
import { textProcessing } from '@kit.NaturalLanguageKit'
import { BusinessError } from '@kit.BasicServicesKit';

async function testWordSegment(inputText: string) {
  textProcessing.getWordSegment(inputText)
    .then(result => {
      let outputText = formatWordSegmentResult(result);
      hilog.info(0x0000, 'NLUDemo', `getWordSegment result:${outputText}`);
    })
    .catch((err: BusinessError) => {
      hilog.error(0x0000, 'NLUDemo', `getWordSegment errorCode: ${err.code} errorMessage: ${err.message}`);
    });
}

function formatWordSegmentResult(segments: textProcessing.WordSegment[]): string {
  let output = 'Word Segments:\n';
  segments.forEach((segment, index) => {
    output += `Word[${index}]: ${segment.word}, Tag: ${segment.wordTag}\n`;
  });
  return output;
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('Start').onClick(() => {
        // 测试文本分词
        let inputText = 'test for nlp word segment';
        testWordSegment(inputText);
      })
    }
  }
}
```

#### textProcessing.getEntity

getEntity(text: string, entityConfig?: EntityConfig): Promise<Array<Entity>>

创建实体抽取实例，并初始化引擎。使用Promise异步回调。

**系统能力：**SystemCapability.AI.NaturalLanguage.TextProcessing

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

text

string

是

输入的字符串。相关规格参考[约束与限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/natural-language-introduction#section1454714381942)。

entityConfig

[EntityConfig](#section7467975499)

否

实体配置项：实体类别。

默认全选。推荐按需加载实体类别，以提高应用性能。

**返回值：**

类型

说明

Promise<Array<[Entity](#section1518613358392)>>

Promise对象，返回实体的结果集合。

**错误码：**

以下错误码的详细介绍请参见[Natural Language Kit错误码](ArkTS API错误码.md)。

错误码ID

错误信息

200

Run timed out, please try again later.

401

The parameter check failed.

1011200001

Failed to run, please try again.

1011200002

The service is abnormal.

**示例：**

```ets
import { textProcessing, EntityType } from '@kit.NaturalLanguageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function testEntityRecognition(inputText: string) {
  textProcessing.getEntity(inputText, {
    entityTypes: [EntityType.NAME]
  }).then(result => {
    let outputText = formatEntityResult(result);
    hilog.info(0x0000, 'NLUDemo', `getEntity result:${outputText}`);
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'NLUDemo', `getEntity errorCode: ${err.code} errorMessage: ${err.message}`);
  })
}

function formatEntityResult(entities: textProcessing.Entity[]): string {
  if (!entities || !entities.length) {
    return 'No entities found.';
  }

  let output = 'Entities:\n';
  for (let i = 0; i < entities.length; i++) {
    let entity = entities[i];
    output += `Entity[${i}]:\n`;
    output += `  oriText: ${entity.text}\n`;
    output += `  charOffset: ${entity.charOffset}\n`;
    output += `  entityType: ${entity.type}\n`;
    output += `  jsonObject: ${entity.jsonObject}\n\n`;
  }
  return output;
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('Start').onClick(() => {
        // 测试实体识别
        let inputText = 'test for nlp getEntity. Mary, Bob and Mike.';
        testEntityRecognition(inputText);
      })
    }
  }
}
```

#### textProcessing.init

init(): Promise<boolean>

初始化自然语言处理的引擎。使用Promise异步回调。

**系统能力：**SystemCapability.AI.NaturalLanguage.TextProcessing

**起始版本：**5.0.0(12)

**返回值：**

类型

说明

Promise<boolean>

Promise对象，true表示初始化成功，false表示初始化失败。

此初始化接口非必须调用。在主动使用时，可以提前初始化该功能，减少首次调用文本处理能力的时延。

**错误码：**

以下错误码的详细介绍请参见[Natural Language Kit错误码](ArkTS API错误码.md)。

错误码ID

错误信息

200

Run timed out, please try again later.

1011200001

Failed to run, please try again.

1011200002

The service is abnormal.

**示例：**

```ets
import { textProcessing } from '@kit.NaturalLanguageKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('init').onClick(() => {
        textProcessing.init().then(async result => {
        console.info(`textProcess init result: ${result}`)
      }).catch((err: BusinessError) => {
        console.error(`textProcess init failed errorCode: ${err.code} errorMessage: ${err.message}`);
      })
      })
    }
  }
}
```

#### textProcessing.release

release(): Promise<boolean>

释放引擎。使用Promise异步回调。

**系统能力：**SystemCapability.AI.NaturalLanguage.TextProcessing

**起始版本：**5.0.0(12)

**返回值：**

类型

说明

Promise<boolean>

Promise对象，true表示释放引擎成功，false表示释放引擎失败。

**错误码：**

以下错误码的详细介绍请参见[Natural Language Kit错误码](ArkTS API错误码.md)。

错误码ID

错误信息

200

Run timed out, please try again later.

1011200001

Failed to run, please try again.

1011200002

The service is abnormal.

**示例：**

```ets
import { textProcessing } from '@kit.NaturalLanguageKit';

export async function runTextProcessing() {
  await textProcessing.init();
  console.info('Text processing initialized successfully');

  try {
    const result = await textProcessing.release();
    console.info(`textProcess release result: ${result}`);
  } catch (err) {
    console.error(`textProcess release failed errorCode: ${err.code} errorMessage: ${err.message}`);
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('Start').onClick(() => {
        runTextProcessing()
      })
    }
  }
}
```