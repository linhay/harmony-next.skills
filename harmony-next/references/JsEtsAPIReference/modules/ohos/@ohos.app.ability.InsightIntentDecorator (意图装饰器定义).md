# @ohos.app.ability.InsightIntentDecorator (意图装饰器定义)

InsightIntentDecorator模块提供了几类意图装饰器，用于装饰类或方法。开发者可以[使用装饰器开发意图](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/insight-intent-decorator-development), 将应用的功能定义为意图，并集成到智能问答、智能搜索、智能推荐等AI入口。

- [@InsightIntentLink](#ZH-CN_TOPIC_0000002497604590__insightintentlink)装饰器：使用该装饰器装饰当前应用的uri链接，可以将该uri链接定义为意图，便于AI入口通过意图快速跳转到当前应用。该装饰器支持的参数参见[LinkIntentDecoratorInfo](#ZH-CN_TOPIC_0000002497604590__linkintentdecoratorinfo)。
- [@InsightIntentPage](#ZH-CN_TOPIC_0000002497604590__insightintentpage)装饰器：使用该装饰器装饰当前应用的Page页面，可以将该Page页面定义为意图，便于AI入口通过意图快速跳转到当前Page页面。该装饰器支持的参数参见[PageIntentDecoratorInfo](#ZH-CN_TOPIC_0000002497604590__pageintentdecoratorinfo)。
- [@InsightIntentFunction](#ZH-CN_TOPIC_0000002497604590__insightintentfunction)装饰器与[@InsightIntentFunctionMethod](#ZH-CN_TOPIC_0000002497604590__insightintentfunctionmethod)装饰器：两者必须组合使用。使用[@InsightIntentFunction](#ZH-CN_TOPIC_0000002497604590__insightintentfunction)装饰器来装饰类，同时使用[@InsightIntentFunctionMethod](#ZH-CN_TOPIC_0000002497604590__insightintentfunctionmethod)装饰器来装饰类中的静态函数，可以将对应的静态函数定义为意图，便于AI入口能够快速执行此函数。
- [@InsightIntentEntry](#ZH-CN_TOPIC_0000002497604590__insightintententry)装饰器：使用该装饰器装饰一个继承自[InsightIntentEntryExecutor](@ohos.app.ability.InsightIntentEntryExecutor (@InsightIntentEntry的意图执行基类).md)的类，实现意图操作并配置意图依赖的Ability组件，便于AI入口拉起依赖的Ability组件时，执行对应的意图操作。该装饰器支持的参数参见[EntryIntentDecoratorInfo](#ZH-CN_TOPIC_0000002497604590__entryintentdecoratorinfo)。
- [@InsightIntentForm](#ZH-CN_TOPIC_0000002497604590__insightintentform)装饰器：使用该装饰器装饰[FormExtensionAbility](@ohos.app.form.FormExtensionAbility (FormExtensionAbility).md)并配置FormExtensionAbility绑定的卡片名称，便于AI入口通过意图添加卡片。该装饰器支持的参数参见[FormIntentDecoratorInfo](#ZH-CN_TOPIC_0000002497604590__formintentdecoratorinfo)。
- [@InsightIntentEntity](#ZH-CN_TOPIC_0000002497604590__insightintententity)装饰器：使用该装饰器装饰一个继承自[IntentEntity](@ohos.app.ability.insightIntent (意图框架基础定义).md#ZH-CN_TOPIC_0000002529284581__intententity20)的类，可将该类定义为意图实体，用于传递意图调用时所需的参数。该装饰器支持的参数参见[IntentEntityDecoratorInfo](#ZH-CN_TOPIC_0000002497604590__intententitydecoratorinfo)。

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 基本概念

意图可以分为标准意图和自定义意图。

系统会根据[IntentDecoratorInfo](#ZH-CN_TOPIC_0000002497604590__intentdecoratorinfo)中的schema与intentVersion字段，在标准意图列表查询是否存在匹配的意图。

- 如果存在匹配的意图，则对应的意图为标准意图。
- 如果不存在匹配的意图，则对应的意图为自定义意图。

#### 导入模块

```ets
import { InsightIntentLink, InsightIntentPage, InsightIntentFunctionMethod, InsightIntentFunction, InsightIntentEntry } from '@kit.AbilityKit';
```

#### @InsightIntentLink

使用该装饰器装饰当前应用的uri链接，可以将该uri链接定义为意图，便于AI入口通过定义的意图快速跳转到当前应用。该装饰器支持的参数参见[LinkIntentDecoratorInfo](#ZH-CN_TOPIC_0000002497604590__linkintentdecoratorinfo)。

uri链接格式需要符合[应用链接说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-uri-config)中的要求。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**示例：**

以自定义意图为例：自定义意图的parameters需要传入标准的JSON Schema数据结构。

```ets
import { InsightIntentLink, LinkParamCategory } from '@kit.AbilityKit';

@InsightIntentLink({
  intentName: 'PlayMusic',
  domain: 'MusicDomain',
  intentVersion: '1.0.1',
  displayName: '播放歌曲',
  displayDescription: '播放音乐意图',
  icon: $r('app.media.app_icon'), // $r表示本地图标，需要在资源目录中定义
  llmDescription: '支持传递歌曲名称，播放音乐',
  keywords: ['音乐播放', '播放歌曲', 'PlayMusic'],
  uri: 'https://www.example.com/music/',
  paramMappings: [{
    paramName: 'songName',
    paramMappingName: 'music',
    paramCategory: LinkParamCategory.LINK
  }],
  parameters: {
    'schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'title': 'Song Schema',
    'description': 'A schema for describing songs and their artists',
    'properties': {
      'songName': {
        'type': 'string',
        'description': 'The name of the song',
        'minLength': 1
      }
    },
    'required': ['songName'],
    'additionalProperties': false
  },
  result: {
    'type': 'object',
    'propertyNames': {
      'enum': [
        'code',
        'result'
      ]
    },
    'required': [
      'code',
      'result'
    ],
    'properties': {
      'code': {
        'description': '执行结果码',
        'type': 'number'
      },
      'result': {}
    }
  }
})
export class ClassForLink {
  private _playback: string = 'intention_test';

  public set playback(value: string) {
    this._playback = value;
  }

  public get playback(): string {
    return this._playback;
  }

  constructor(playback: string) {
    this._playback = playback;
  }

  static Function1(playbackProgress: number, playback?: number): void {
    console.info(`Function1, playbackProgress: ${playbackProgress}.`);
  }
}
```

#### IntentDecoratorInfo

意图装饰器的通用属性，用于定义意图的基本信息（包括意图名称、意图版本号）。适用于本模块的所有装饰器。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**属性：**

如果根据schema与intentVersion字段，在标准意图列表存在匹配的标准意图，系统会将intentName、domain、llmDescription、keywords、parameters、result字段均设置为标准意图的相应字段值。

名称类型只读可选说明intentNamestring否否表示意图名称，是意图的唯一标识。domainstring否否表示意图垂域，用于将意图按垂直领域分类（例如：视频、音乐、游戏），取值范围参见[各垂域的智慧分发特性列表](https://developer.huawei.com/consumer/cn/doc/service/intents-ai-distribution-characteristic-0000001901922213#section2656133582215)中的垂域字段。intentVersionstring否否表示意图版本号。当意图能力演进时，可通过版本号进行区分和管理。displayNamestring否否表示显示给用户的意图名称。displayDescriptionstring否是表示显示给用户的意图描述。schemastring否是表示接入的标准意图的名称。开发者[接入标准意图](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/insight-intent-definition#接入标准意图)时，需要配置该字段，[创建自定义意图](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/insight-intent-definition#创建自定义意图)时，无需配置该字段。标准意图列表参见[附录：标准意图接入规范](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/insight-intent-access-specifications)。iconResourceStr否是

表示意图图标，用于在AI入口显示。

- 当取值为字符串类型时，表示图标读取网络资源。

- 当取值为[Resource](@ohos.resourceManager (资源管理).md)时，表示图标读取本地资源。

llmDescriptionstring否是表示意图的功能，用于大型语言模型理解该意图。keywordsstring[]否是表示意图的搜索关键字。parametersRecord<string, Object>否是表示意图参数的数据格式声明，用于意图调用时定义入参的数据格式。取值参见[各垂域意图Schema](https://developer.huawei.com/consumer/cn/doc/service/intents-schema-0000001901962713)resultRecord<string, Object>否是表示意图调用返回结果的数据格式声明，用于定义意图调用返回结果的数据格式。

#### LinkIntentDecoratorInfo

LinkIntentDecoratorInfo继承自[IntentDecoratorInfo](#ZH-CN_TOPIC_0000002497604590__intentdecoratorinfo)，用于描述[@InsightIntentLink](#ZH-CN_TOPIC_0000002497604590__insightintentlink)装饰器支持的参数，例如应用间跳转需要的uri信息。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**属性：**

名称类型只读可选说明uristring否否表示意图的uri信息。paramMappings[LinkIntentParamMapping](#ZH-CN_TOPIC_0000002497604590__linkintentparammapping)[]否是意图参数和uri信息的映射。

#### LinkIntentParamMapping

LinkIntentParamMapping是[@InsightIntentLink](#ZH-CN_TOPIC_0000002497604590__insightintentlink)装饰器的意图参数和uri信息的映射。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**属性：**

名称类型只读可选说明paramNamestring否否表示意图参数的名称。paramMappingNamestring否是表示意图参数映射名称。paramCategory[LinkParamCategory](#ZH-CN_TOPIC_0000002497604590__linkparamcategory)否是

表示意图参数类别。

若意图参数类别取值为[LINK](#ZH-CN_TOPIC_0000002497604590__linkparamcategory)，系统获取paramName字段对应的意图参数映射名称，并将该意图参数映射名称拼接到uri链接的末尾(以键值对的形式key=value，key为意图参数映射名称，value为意图参数值)。

若意图参数类别为[WANT](#ZH-CN_TOPIC_0000002497604590__linkparamcategory)，系统获取paramName字段对应的意图参数映射名称，并将该意图参数映射名称及取值通过[Want](@ohos.app.ability.Want (Want).md)的parameters字段进行传递。

#### LinkParamCategory

[@InsightIntentLink](#ZH-CN_TOPIC_0000002497604590__insightintentlink)装饰器的意图参数类别，用于定义意图参数的传递形式。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

名称值说明LINK'link'表示意图参数类别为'link'。意图参数将被拼接到uri链接的末尾，以uri链接的形式传给应用。WANT'want'表示意图参数类别为'want'。意图参数将通过[Want](@ohos.app.ability.Want (Want).md)的parameters字段传给应用。

#### @InsightIntentPage

使用该装饰器装饰当前应用的页面，可以将页面定义为意图，便于AI入口通过意图快速跳转到指定页面。该装饰器支持的参数参见[PageIntentDecoratorInfo](#ZH-CN_TOPIC_0000002497604590__pageintentdecoratorinfo)。

该装饰器仅支持装饰struct页面。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**示例：**

```ets
import { InsightIntentPage } from '@kit.AbilityKit';

@Entry
@Component
@InsightIntentPage({
  intentName: 'SearchMusic',
  domain: 'MusicDomain',
  intentVersion: '1.0.1',
  displayName: '搜索歌曲',
  displayDescription: '搜索歌曲意图',
  schema: 'SearchMusic',
  uiAbility: 'Entry',
  pagePath: './ets/pages/Index',
  navigationId: '1',
  navDestinationName: 'PageOne',
})
struct Index {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

#### PageIntentDecoratorInfo

PageIntentDecoratorInfo继承自[IntentDecoratorInfo](#ZH-CN_TOPIC_0000002497604590__intentdecoratorinfo)，用于描述[@InsightIntentPage](#ZH-CN_TOPIC_0000002497604590__insightintentpage)装饰器支持的参数，例如目标页面的[NavDestination](../../topics/misc/Navigation.md#ZH-CN_TOPIC_0000002497444902__navdestination10)名称。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**属性：**

名称类型只读可选说明uiAbilitystring否是表示与意图绑定的UIAbility名称。pagePathstring否否表示与意图绑定的页面路径，该页面需要是一个实际存在的文件。navigationIdstring否是表示与意图绑定的[Navigation组件](../../topics/misc/Navigation.md#ZH-CN_TOPIC_0000002497444902__属性)的id属性。navDestinationNamestring否是表示与意图绑定[NavDestination组件](../../topics/misc/Navigation.md#ZH-CN_TOPIC_0000002497444902__navdestination10)的名称。

#### @InsightIntentFunction

该装饰器与[@InsightIntentFunctionMethod](#ZH-CN_TOPIC_0000002497604590__insightintentfunctionmethod)装饰器必须组合使用。

使用该装饰器来装饰类，同时使用[@InsightIntentFunctionMethod](#ZH-CN_TOPIC_0000002497604590__insightintentfunctionmethod)装饰器来装饰类中的静态函数，可以将对应的静态函数定义为意图，便于AI入口能够快速执行此函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

#### @InsightIntentFunctionMethod

该装饰器与[@InsightIntentFunction](#ZH-CN_TOPIC_0000002497604590__insightintentfunction)装饰器必须组合使用。

使用该装饰器来装饰类中的静态函数，同时使用[@InsightIntentFunction](#ZH-CN_TOPIC_0000002497604590__insightintentfunction)装饰器来装饰静态函数所属的类，可以将对应的静态函数定义为意图，便于AI入口能够快速执行此函数。

静态方法所在的类需要通过export导出。

函数的参数名称、参数类型需要与意图定义的参数名称、参数类型保持一致。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**示例：**

```ets
import { InsightIntentFunction, InsightIntentFunctionMethod } from '@kit.AbilityKit';

@InsightIntentFunction()
export class ClassForFuncDemo {
  @InsightIntentFunctionMethod({
  intentName: 'GetWeather',
  domain: 'LifeDomain',
  intentVersion: '1.0.1',
  displayName: '查询天气',
  displayDescription: '显示天气信息',
  icon: $r('app.media.app_icon'), // $r表示本地图标，需要在资源目录中定义
  llmDescription: 'Get weather of an location',
  parameters: {
    'schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'title': 'Weather Schema',
    'description': 'A schema for get weather of an location',
    'properties': {
      'location': {
        'type': 'string',
        'description': 'The city and state, e.g. Hangzhou',
        'minLength': 1
      }
    },
    'required': ['location'],
    'additionalProperties': false
  }
})
  static getWeather(location: string): string {
    console.info(`location: ${location}`);
    return 'The current temperature in Hangzhou is 24℃';
  }
}
```

#### FunctionIntentDecoratorInfo

[@InsightIntentFunctionMethod](#ZH-CN_TOPIC_0000002497604590__insightintentfunctionmethod)装饰器的参数类型，当前全部属性均继承自[IntentDecoratorInfo](#ZH-CN_TOPIC_0000002497604590__intentdecoratorinfo)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

#### @InsightIntentEntry

使用该装饰器装饰一个继承自[InsightIntentEntryExecutor](@ohos.app.ability.InsightIntentEntryExecutor (@InsightIntentEntry的意图执行基类).md)的类，实现意图操作并配置意图依赖的Ability组件，便于AI入口拉起依赖的Ability组件时，执行对应的意图操作。该装饰器支持的参数参见[EntryIntentDecoratorInfo](#ZH-CN_TOPIC_0000002497604590__entryintentdecoratorinfo)。

- 如果使用该装饰器接入标注意图，必须实现标准意图Json Schema中定义的所有必选参数且类型匹配。
- 如果创建自定义意图，必须实现parameters字段中定义的所有必选参数且类型匹配。
- 被装饰的类需要使用export default导出。类的属性仅支持基础类型或意图实体，返回值仅支持意图实体。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**示例：**

```ets
import { insightIntent, InsightIntentEntry, InsightIntentEntryExecutor } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const LOG_TAG: string = 'testTag-EntryIntent';

// 使用@InsightIntentEntry装饰器定义意图
@InsightIntentEntry({
  intentName: 'PlayMusic',
  domain: 'MusicDomain',
  intentVersion: '1.0.1',
  displayName: '播放歌曲',
  displayDescription: '播放音乐意图',
  icon: $r('app.media.app_icon'), // $r表示本地图标，需要在资源目录中定义
  llmDescription: '支持传递歌曲名称，播放音乐',
  keywords: ['音乐播放', '播放歌曲', 'PlayMusic'],
  abilityName: 'EntryAbility',
  executeMode: [insightIntent.ExecuteMode.UI_ABILITY_FOREGROUND],
  parameters: {
    'schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'title': 'Song Schema',
    'description': 'A schema for describing songs and their artists',
    'properties': {
      'songName': {
        'type': 'string',
        'description': 'The name of the song',
        'minLength': 1
      }
    },
    'required': ['songName']
  }
})
export default class PlayMusicDemo extends InsightIntentEntryExecutor<string> {
  songName: string = '';

  onExecute(): Promise<insightIntent.IntentResult<string>> {
    hilog.info(0x0000, LOG_TAG, 'PlayMusicDemo executeMode %{public}s', JSON.stringify(this.executeMode));
    hilog.info(0x0000, LOG_TAG, '%{public}s', JSON.stringify(this));
    let storage = new LocalStorage();
    storage.setOrCreate('songName', this.songName);
    // 根据executeMode参数的不同情况，提供不同拉起PlayMusicPage页面的方式。
    if (this.executeMode == insightIntent.ExecuteMode.UI_ABILITY_FOREGROUND) {
      this.windowStage?.loadContent('pages/PlayMusicPage', storage);
    } else if (this.executeMode == insightIntent.ExecuteMode.UI_EXTENSION_ABILITY) {
      this.uiExtensionSession?.loadContent('pages/PlayMusicPage', storage);
    }
    // 定义意图的执行结果
    let result: insightIntent.IntentResult<string> = {
      code: 123,
      result: 'result'
    }
    hilog.info(0x0000, LOG_TAG, 'PlayMusicDemo return %{public}s', JSON.stringify(result));
    // 以Promise的方式返回意图执行结果
    return Promise.reject(result);
  }
}
```

#### EntryIntentDecoratorInfo

EntryIntentDecoratorInfo继承自[IntentDecoratorInfo](#ZH-CN_TOPIC_0000002497604590__intentdecoratorinfo)，用于描述[@InsightIntentEntry](#ZH-CN_TOPIC_0000002497604590__insightintententry)装饰器支持的参数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**属性：**

名称类型只读可选说明abilityNamestring否否表示与意图绑定的Ability名称。executeMode[insightIntent.ExecuteMode](@ohos.app.ability.insightIntent (意图框架基础定义).md#ZH-CN_TOPIC_0000002529284581__executemode)[]否否表示意图调用执行模式。即拉起绑定的Ability时支持的执行模式。

#### @InsightIntentForm

使用该装饰器装饰[FormExtensionAbility](@ohos.app.form.FormExtensionAbility (FormExtensionAbility).md)并配置FormExtensionAbility绑定的卡片名称，便于AI入口通过意图添加卡片。该装饰器支持的参数参见[FormIntentDecoratorInfo](#ZH-CN_TOPIC_0000002497604590__formintentdecoratorinfo)。

卡片名称定义的要求参见[卡片配置](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-configuration#卡片配置)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**示例：**

```ets
import { formBindingData, FormExtensionAbility, formInfo } from '@kit.FormKit';
import { insightIntent, Want, InsightIntentForm } from '@kit.AbilityKit';

// 使用@InsightIntentForm装饰器将该FormExtensionAbility名为widget的卡片定义为意图
@InsightIntentForm({
  intentName: 'PlayMusic',
  domain: 'MusicDomain',
  intentVersion: '1.0.1',
  displayName: '播放歌曲',
  displayDescription: '播放音乐意图',
  icon: $r('app.media.app_icon'), // $r表示本地图标，需要在资源目录中定义
  llmDescription: '支持传递歌曲名称，播放音乐',
  keywords: ['音乐播放', '播放歌曲', 'PlayMusic'],
  parameters: {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'title': 'Song Schema',
    'description': 'A schema for describing songs and their artists',
    'properties': {
      'songName': {
        'type': 'string',
        'description': 'The name of the song',
        'minLength': 1
      },
      'artist': {
        'type': 'object',
        'description': 'Information about the artist',
        'properties': {
          'country': {
            'type': 'string',
            'description': 'The artist\'s country of origin',
            'default': 'zh'
          },
          'city': {
            'type': 'object',
            'description': 'The artist\' city of origin'
          },
          'name': {
            'type': 'string',
            'description': 'The name of the artist',
            'minLength': 1
          }
        },
        'required': ['name']
      }
    },
    'required': ['songName']
  },
  formName: 'widget'
})
export default class EntryFormAbility extends FormExtensionAbility {
  songName: string = '';

  onAddForm(want: Want) {
    // 该方法被调用时，将返回FormBindingData对象
    let formData = '';
    return formBindingData.createFormBindingData(formData);
  }
}
```

#### FormIntentDecoratorInfo

FormIntentDecoratorInfo继承自[IntentDecoratorInfo](#ZH-CN_TOPIC_0000002497604590__intentdecoratorinfo)，用于描述[@InsightIntentForm](#ZH-CN_TOPIC_0000002497604590__insightintentform)装饰器支持的参数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**属性：**

名称类型只读可选说明formNamestring否否表示FormExtensionAbility绑定的卡片名称。

#### @InsightIntentEntity

使用该装饰器装饰一个继承自[IntentEntity](@ohos.app.ability.insightIntent (意图框架基础定义).md#ZH-CN_TOPIC_0000002529284581__intententity20)的类，可将该类定义为意图实体，用于传递意图调用时所需的参数。该装饰器支持的参数参见[IntentEntityDecoratorInfo](#ZH-CN_TOPIC_0000002497604590__intententitydecoratorinfo)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**示例：**

```ets
import { insightIntent, InsightIntentEntity } from '@kit.AbilityKit';

@InsightIntentEntity({
  entityCategory: 'artist entity category',
  parameters: {
    '$id': '/schemas/ArtistClassDef',
    'type': 'object',
    'description': 'Information about the artist',
    'properties': {
      'country': {
        'type': 'string',
        'description': 'The artist\'s country of origin',
        'default': 'zh'
      },
      'city': {
        'type': 'string',
        'description': 'The artist\'s city of origin'
      },
      'name': {
        'type': 'string',
        'description': 'The name of the artist',
        'minLength': 1
      }
    },
    'required': ['name']
  }
})
export class ArtistClassDef implements insightIntent.IntentEntity {
  entityId: string = 'id';
  name: string = '';
}
```

#### IntentEntityDecoratorInfo

用于描述[@InsightIntentEntity](#ZH-CN_TOPIC_0000002497604590__insightintententity)装饰器支持的参数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**属性：**

名称类型只读可选说明entityCategorystring否否表示意图实体类别。可以基于意图实体类别对意图实体进行归类parametersRecord<string, Object>否是表示意图实体的数据格式声明。用于定义意图实体的数据格式。