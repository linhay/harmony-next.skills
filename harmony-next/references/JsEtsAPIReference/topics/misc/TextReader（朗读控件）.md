# TextReader（朗读控件）

朗读控件使用AI能力将文本实时转化成语音并进行朗读，适用于一些新闻类文本内容浏览类APP，帮助用户在一些无法直接浏览文本内容的场景下，通过文本朗读来高效获取信息。

起始版本： 5.0.0(12)

**导入模块**

```ets
import { TextReader } from '@kit.SpeechKit';
```

**注意事项**

调用朗读控件接口前，必须先调用[init](#ZH-CN_TOPIC_0000002522082600__init)初始化，否则会报错。

**init**

init(context: common.BaseContext, readParams: ReaderParam): Promise<void>

朗读控件初始化，用于初始化TTS引擎和底层播放器，初始化失败会返回对应错误码。

使用Promise异步回调。若要配置长时权限，请参考[开发指南步骤9](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/speech-textreader-guide)。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

需要权限：ohos.permission.KEEP_BACKGROUND_RUNNING

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.BaseContext | 是 | 当前应用上下文。 |
| readParams | ReaderParam | 是 | 朗读参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. Interface caller does not have permission ohos.permission.KEEP_BACKGROUND_RUNNING. |
| 401 | Parameter error. |
| 1010600011 | Initialize failed. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  // 获取应用上下文

  async aboutToAppear(): Promise<void> {
    let context: Context | undefined = this.getUIContext().getHostContext();
    if (context) {
      // 设置朗读参数
      const readerParams: TextReader.ReaderParam = {
        isVoiceBrandVisible: true,
        businessBrandInfo: {
          panelName: '小艺朗读',
          panelIcon: $r('app.media.startIcon')
        }
      };
      // 初始化朗读控件
      await TextReader.init(context, readerParams).then(() => {
        console.info(`TextReader succeeded in initializing.`);
      }).catch((e: BusinessError) => {
        console.error(`TextReader failed to initialize. Code: ${e.code}, message: ${e.message}`);
      })
    }

  build() {
    // ...
  }
```

**start**

start(readInfoList: ReadInfo[], articleId?: string): Promise<void>

朗读控件起播。播放失败返回对应错误码。

使用Promise异步回调。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| readInfoList | ReadInfo[] | 是 | 播放文章列表。 - 若列表的第一篇文章是有分类的（即带有category或categoryObject字段），后续文章不带分类，也会归为“其他”分类下。 - 若列表的第一篇是没有分类的，后续文章即使带分类，也不会生效。 |
| articleId | string | 否 | 文章id，articleId不传时，默认从文章列表中的第一篇开始播放；传参时，从传入articleId对应的文章开始依次往下播放。（文章id不能重复，否则从列表进入同id的文章，会自动选择同id的第一篇朗读） |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1010600012 | The TextReader is not initialized. |
| 1010600013 | Text-to-speech engine error. |
| 1010600014 | AudioRenderer play error. |
| 1010600015 | Audio decode error. |
| 1010600016 | AVSession error. |
| 1010600017 | Other error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';

const readInfoList: TextReader.ReadInfo[] = [{
  id: '001',
  title: {
    text:'水调歌头.明月几时有',
    isClickable:true
  },
  author:{
    text:'宋.苏轼',
    isClickable:true
  },
  date: {
    text:'2024/01/01',
    isClickable:false
  },
  bodyInfo: '明月几时有？把酒问青天。'
}];
// 启动朗读控件
TextReader.start(readInfoList).then(() => {
  console.info(`TextReader succeeded in starting`);
}).catch((e: BusinessError) => {
  console.error(`TextReader failed to start. Code: ${e.code}, message: ${e.message}`);
})
```

**start**

start(readInfoList: ReadInfo[], articleId: string | undefined, startParams: StartParams): Promise<void>

朗读控件起播，可以通过设置startParams参数实现隐藏Minibar等效果。播放失败返回对应错误码。

使用Promise异步回调。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.2(14)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| readInfoList | ReadInfo[] | 是 | 播放文章列表。 - 若列表的第一篇文章是有分类的（即带有category或categoryObject字段），后续文章不带分类，也会归为“其他”分类下。 - 若列表的第一篇是没有分类的，后续文章即使带分类，也不会生效。 |
| articleId | string | undefined | 是 | 文章id（文章id不能重复，否则从列表进入同id的文章，会自动选择同id的第一篇文章），articleId不传时，默认从文章列表中的第一篇开始播放；传参时，从传入articleId对应的文章开始依次往下播放。 |
| startParams | StartParams | 是 | 朗读控件起播参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1010600012 | The TextReader is not initialized. |
| 1010600013 | Text-to-speech engine error. |
| 1010600014 | AudioRenderer play error. |
| 1010600015 | Audio decode error. |
| 1010600016 | AVSession error. |
| 1010600017 | Other error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';

const readInfoList: TextReader.ReadInfo[] = [{
  id: '001',
  title: {
    text:'水调歌头.明月几时有',
    isClickable:true
  },
  author:{
    text:'宋.苏轼',
    isClickable:true
  },
  date: {
    text:'2024/01/01',
    isClickable:false
  },
  bodyInfo: '明月几时有？把酒问青天。'
}];
const startParams: TextReader.StartParams = {
  isMinibarHidden: false,
  callbackParam: '0'
}
// 启动朗读控件
TextReader.start(readInfoList, undefined, startParams).then(() => {
  console.info(`TextReader succeeded in starting`);
}).catch((e: BusinessError) => {
  console.error(`TextReader failed to start. Code: ${e.code}, message: ${e.message}`);
})
```

**stop**

stop(): Promise<void>

朗读控件停止朗读，执行播放面板的关闭，注销监听，重置参数。

使用Promise异步回调。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010600012 | The TextReader is not initialized. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';

TextReader.stop().then(() => {
  console.info(`TextReader succeeded in stopping.`);
}).catch((e: BusinessError) => {
  console.error(`TextReader failed to stop. Code: ${e.code}, message: ${e.message}`);
})
```

**resetParam**

resetParam(paramName: ResetParamType) : void

提供重置初始化参数、清除播放列表接口。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.2(14)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| paramName | ResetParamType | 是 | 重置参数类型。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.resetParam(TextReader.ResetParamType.BAR_PARAM)
  console.info(`TextReader succeeded in resetParam.`);
} catch (e) {
  console.error(`TextReader failed to resetParam. Code: ${e.code}, message: ${e.message}`);
}
```

**release**

release(): Promise<void>

释放朗读控件的所有资源。

使用Promise异步回调。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010600012 | The TextReader is not initialized. |
| 1010600020 | Release error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';

TextReader.release().then(() => {
  console.info(`TextReader succeeded in releasing.`);
}).catch((e: BusinessError) => {
  console.error(`TextReader failed to release. Code: ${e.code}, message: ${e.message}`);
})
```

**pause**

pause(): void

暂停播放。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010600012 | The TextReader is not initialized. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.pause();
} catch (e) {
  console.error(`TextReader failed to pause. Code: ${e.code}, message: ${e.message}`);
}
```

**resume**

resume(): void

继续播放。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010600012 | The TextReader is not initialized. |
| 1010600013 | Text-to-speech engine error. |
| 1010600014 | AudioRenderer play error. |
| 1010600015 | Audio decode error. |
| 1010600016 | AVSession error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.resume();
} catch (e) {
  console.error(`TextReader failed to resume. Code: ${e.code}, message: ${e.message}`);
}
```

**playPrev**

playPrev(): void

播放上一篇文章。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010600012 | The TextReader is not initialized. |
| 1010600018 | playPrev failed. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.playPrev();
} catch (e) {
  console.error(`TextReader failed to play previous article. Code: ${e.code}, message: ${e.message}`);
}
```

**playNext**

playNext(): void

播放下一篇文章。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010600012 | The TextReader is not initialized. |
| 1010600019 | playNext failed. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.playNext();
} catch (e) {
  console.error(`TextReader failed to play next article. Code: ${e.code}, message: ${e.message}`);
}
```

**hidePanel**

hidePanel(): void

隐藏播放面板。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010600012 | The TextReader is not initialized. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.hidePanel();
} catch (e) {
  console.error(`TextReader failed to hide panel. Code: ${e.code}, message: ${e.message}`);
}
```

**showPanel**

showPanel(): void

打开播放面板。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010600012 | The TextReader is not initialized. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.showPanel();
} catch (e) {
  console.error(`TextReader failed to show panel. Code: ${e.code}, message: ${e.message}`);
}
```

**showMinibar**

showMinibar(): void

显示Minibar。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.2(14)

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010600012 | The TextReader is not initialized. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.showMinibar();
} catch (e) {
  console.error(`TextReader failed to show Minibar. Code: ${e.code}, message: ${e.message}`);
}
```

**hideMinibar**

hideMinibar(): void

隐藏Minibar。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.2(14)

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010600012 | The TextReader is not initialized. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.hideMinibar();
} catch (e) {
  console.error(`TextReader failed to hide Minibar. Code: ${e.code}, message: ${e.message}`);
}
```

**queryReadState**

queryReadState(id?: string): ReadState

查询文章播报状态。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 | 文章id，默认为当前正在朗读的文章id。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| ReadState | 文章播报状态 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  let readState = TextReader.queryReadState('article_01');
  console.info(`Succeeded in querying read state, read state: ${JSON.stringify(readState)}`);
} catch(e) {
  console.error(`TextReader failed to queryReadState. Code: ${e.code}, message: ${e.message}`);
}
```

**setArticleContent**

setArticleContent(id: string, content?: string): void

设置文章内容。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 文章id。 |
| content | string | 否 | 文章内容，content不传或者为空时，播放指定id的文章时，控件内容页显示加载失败；传参时，将指定id文章的内容设置为content。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.setArticleContent('article_01', '明月几时有？把酒问青天。');
} catch (e) {
  console.error(`TextReader failed to setArticleContent. Code: ${e.code}, message: ${e.message}`);
}
```

**setArticle**

setArticle(readInfo: ReadInfo): void

设置指定文章的信息，并立即播放。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| readInfo | ReadInfo | 是 | 文章信息，仅更新image、imageUrl、bodyInfo、bodyInfoObject；如果文章的ID不在列表中，则不会生效。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';
import { image } from '@kit.ImageKit';

const readInfo: TextReader.ReadInfo = {
  id: '001',
  title: {
    text:'水调歌头.明月几时有',
    isClickable:true
  },
  author:{
    text:'宋.苏轼',
    isClickable:true
  },
  date: {
    text:'2024/01/01',
    isClickable:false
  },
  bodyInfo: '明月几时有？把酒问青天。',
  image: {} as image.PixelMap
};
try {
  TextReader.setArticle(readInfo);
} catch (e) {
  console.error(`TextReader failed to setArticle. Code: ${e.code}, message: ${e.message}`);
}

```

**loadMore**

loadMore(readInfos: ReadInfo[], isEnd: boolean): void

加载更多文章到文章列表。需在项目init和start之后调用，建议在'requestMore'操作监听中使用。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| readInfos | ReadInfo[] | 是 | 要加载的文章列表。 |
| isEnd | boolean | 是 | 是否还有更多内容需要加载。 - true：已加载所有内容。 - false：还有内容未加载完。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { ReadStateCode, TextReader, TextReaderIcon } from '@kit.SpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {

  @State readInfoList: TextReader.ReadInfo[] = [];
  @State readState: ReadStateCode = ReadStateCode.WAITING;
  @State isInit: boolean = false;
  @State selectedReadInfo: TextReader.ReadInfo = this.readInfoList[0];
  aboutToAppear(){
    let context: Context | undefined = this.getUIContext().getHostContext();
    if (!context) {
      console.error(`context is undefined.`);
      return;
    }

    // 设置朗读参数
    const readerParams: TextReader.ReaderParam = {
      isVoiceBrandVisible: true,
      businessBrandInfo: {
        panelName: '小艺朗读',
        panelIcon: $r('app.media.startIcon')
      }
    };

    // 初始化朗读控件
    TextReader.init(context, readerParams).then(() => {
      console.info(`TextReader succeeded in initializing.`);
    }).catch((e: BusinessError) => {
      console.error(`TextReader failed to initialize. Code: ${e.code}, message: ${e.message}`);
    })

    /**
     * 加载数据
     */
    console.info(`ReadStateCode: ${JSON.stringify(this.readState)}`);
    let readInfoList: TextReader.ReadInfo[] = [{
      id: '001',
      title: {
        text:'水调歌头.明月几时有',
        isClickable:true
      },
      author:{
        text:'宋.苏轼',
        isClickable:true
      },
      date: {
        text:'2024/01/01',
        isClickable:false
      },
      bodyInfo: '明月几时有？把酒问青天。'
    }];
    this.readInfoList = readInfoList;
    this.selectedReadInfo = this.readInfoList[0];
  }

  // 设置操作监听
  setActionListener() {
    // ...
    TextReader.on('requestMore', () => {
      console.info(`requestMore`);
      try {
        console.info(`loadMore`);
        TextReader.loadMore(this.readInfoList, true);
      } catch (e) {
        console.error(`TextReader failed to loadMore. Code: ${e.code}, message: ${e.message}`);
      }
    });
  }

  build() {
    Column() {
      TextReaderIcon({ readState: this.readState })
        .margin({ right: 20 })
        .width(32)
        .height(32)
        .onClick(() => {
          try {
            this.setActionListener();
            void TextReader.start(this.readInfoList, this.selectedReadInfo?.id);
          } catch(e) {
            console.error(`TextReader failed to start`);
          }
        })
    }
    .height('100%')
  }
```

**queryReadStateByCategoryId**

queryReadStateByCategoryId(categoryId: string): ReadState

根据分类id查询文章状态，查询当前分类是否有正在播报的文章。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.2(14)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| categoryId | string | 是 | 当前播报文章的分类id。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| ReadState | 文章播报状态 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  let readState = TextReader.queryReadStateByCategoryId('categoryId_01');
  console.info(`Succeeded in querying read state by category id, read state: ${JSON.stringify(readState)}`);
} catch(e) {
  console.error(`TextReader failed to queryReadStateByCategoryId. Code: ${e.code}, message: ${e.message}`);
}
```

**on(type: 'setArticle')**

on(type: 'setArticle', callback: Callback<string>): void

注册设置文章回调函数，点击文章或者切换文章时，若目标文章内容为空（bodyInfo值为空）时，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'setArticle'，设置文章后，目标文章内容为空（bodyInfo值为空）时，触发该事件。 |
| callback | Callback<string> | 是 | 点击文章或者切换文章时，执行的回调函数，参数为文章id。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.on('setArticle', (id: string) => {
    console.info(`Succeeded in setting setArticleListener: ${id}`);
  });
} catch (e) {
  console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
}
```

**off(type: 'setArticle')**

off(type: 'setArticle', callback?: Callback<string>): void

在on(type: 'setArticle')函数调用之后使用，用于注销设置文章回调函数。注销监听后，可以重新注册。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'setArticle'，设置文章后，触发该事件。 |
| callback | Callback<string> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数（当前仅有一个）。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.off('setArticle');
} catch (e) {
  console.error(`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}`);
}
```

**on(type: 'clickArticle' | 'clickAuthor' | 'clickNotification')**

on(type: 'clickArticle' | 'clickAuthor' | 'clickNotification', callback: Callback<string>): void

注册点击事件回调函数，点击标题、作者、通知栏时，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型。 - 'clickArticle'：点击文章标题，触发回调。 - 'clickAuthor'：点击作者，触发回调。 - 'clickNotification'：点击通知栏，触发回调。预留参数，暂未支持。 |
| callback | Callback<string> | 是 | 点击事件回调函数，参数为文章id。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.on('clickArticle', (id: string) => {
    console.info(`Succeeded in setting clickArticleListener: ${id}`);
  });
  TextReader.on('clickAuthor', (id: string) => {
    console.info(`Succeeded in setting clickAuthorListener: ${id}`);
  });
  TextReader.on('clickNotification', (id: string) => {
    console.info(`Succeeded in setting clickNotificationListener: ${id}`);
  });
} catch (e) {
  console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
}
```

**off(type: 'clickArticle' | 'clickAuthor' | 'clickNotification')**

off(type: 'clickArticle' | 'clickAuthor' | 'clickNotification', callback?: Callback<string>): void

在on(type: 'clickArticle' | 'clickAuthor' | 'clickNotification')函数调用之后使用，用于注销点击事件回调函数。注销监听后，可以重新注册。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型。 - 'clickArticle'：点击文章标题，取消回调。 - 'clickAuthor'：点击作者事件，取消回调。 - 'clickNotification'：点击通知栏事件，取消回调。 |
| callback | Callback<string> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数（当前仅有一个）。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.off('clickArticle');
  TextReader.off('clickAuthor');
  TextReader.off('clickNotification');
} catch (e) {
  console.error(`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}`);
}
```

**on(type: 'showPanel' | 'hidePanel')**

on(type: 'showPanel' | 'hidePanel', callback: Callback<void>): void

注册拉起/收回播放面板回调函数，拉起/收回播放面板时，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型。 - 'showPanel'：拉起面板，触发回调。 - 'hidePanel'：收回面板，触发回调。 |
| callback | Callback<void> | 是 | 面板事件回调函数。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.on('showPanel', () => {
    console.info(`Succeeded in setting showPanelListener.`);
  });
  TextReader.on('hidePanel', () => {
    console.info(`Succeeded in setting hidePanelListener.`);
  });
} catch (e) {
  console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
}
```

**off(type: 'showPanel' | 'hidePanel')**

off(type: 'showPanel' | 'hidePanel', callback?: Callback<void>): void

在on(type: 'showPanel' | 'hidePanel')函数调用之后使用，用于注销拉起/收回播放面板监听事件。注销监听后，可以重新注册。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型。 - 'showPanel'：拉起面板，取消回调。 - 'hidePanel'：收起面板，取消回调。 |
| callback | Callback<void> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数（当前仅有一个）。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.off('showPanel');
  TextReader.off('hidePanel');
} catch (e) {
  console.error(`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}`);
}
```

**on(type: 'stop' | 'release')**

on(type: 'stop' | 'release', callback: Callback<void>): void

注册停止/释放回调函数，调用stop/release时，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型。 - 'stop'：调用stop接口。 - 'release'：调用release释放资源。 |
| callback | Callback<void> | 是 | stop/release事件回调函数。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.on('stop', () => {
    console.info(`Succeeded in setting stopListener.`);
  });
  TextReader.on('release', () => {
    console.info(`Succeeded in setting releaseListener.`);
  });
} catch (e) {
  console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
}
```

**off(type: 'stop' | 'release')**

off(type: 'stop' | 'release', callback?: Callback<void>): void

在on(type: 'stop' | 'release')函数调用之后使用，用于注销stop/release事件的回调函数。注销监听后，可以重新注册。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型。 - 'stop'：调用stop接口或用户主动滑动通知栏退出。 - 'release'：调用release释放资源。 |
| callback | Callback<void> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数（当前仅有一个）。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.off('stop');
  TextReader.off('release');
} catch (e) {
  console.error(`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}`);
}
```

**on(type: 'stateChange')**

on(type: 'stateChange', callback: Callback<ReadState>): void

注册状态变化回调函数，当前正在播放的文章状态变更时，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'stateChange'，当前正在播放的文章状态变更时，触发该事件。 |
| callback | Callback<ReadState> | 是 | 正在播放的文章状态变更时，执行的回调函数。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.on('stateChange', (state: TextReader.ReadState) => {
    console.info(`Succeeded in setting stateChangeListener: ${JSON.stringify(state)}`);
  });
} catch (e) {
  console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
}
```

**off(type: 'stateChange')**

off(type: 'stateChange', callback?: Callback<ReadState>): void

在on(type: 'stateChange')函数调用之后使用，用于注销正在播放的文章状态变更的回调函数。注销监听后，可以重新注册。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'stateChange'，当前正在播放的文章状态变更时，触发该事件。 |
| callback | Callback<ReadState> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数（当前仅有一个）。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.off('stateChange');
} catch (e) {
  console.error(`TextReader failed to unset on(type: 'requestMore')eventListener. Code: ${e.code}, message: ${e.message}`);
}
```

**on(type: 'requestMore')**

on(type: 'requestMore', callback: Callback<void>): void

注册请求更多文章回调函数，拉到播放列表底端或播放到文章最后一篇，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'requestMore'，请求更多文章时，触发该事件监听。 |
| callback | Callback<void> | 是 | 拉到播放列表底端或播放到文章最后一篇，触发该回调执行。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.on('requestMore', () => {
    console.info(`Succeeded in setting requestMoreListener.`);
  });
} catch (e) {
  console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
}
```

**on(type: 'requestMore')**

on(type: 'requestMore', callback: Callback<string>): void

注册请求更多文章回调函数，拉到播放列表底端或播放到文章最后一篇，触发该回调执行，返回用户自定义参数。同一类型监听，注册多个回调函数，仅第一次注册有效。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.2(14)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'requestMore'，拉到播放列表底端请求更多文章时，触发该事件监听。 |
| callback | Callback<string> | 是 | 拉到播放列表底端或播放到文章最后一篇，触发该回调执行。返回的自定义参数在StartParams的callbackParam属性配置。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.on('requestMore', (callback) => {
    console.info(`Succeeded in setting requestMoreListener. Callback is ${callback}`);
  });
} catch (e) {
  console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
}
```

**off(type: 'requestMore')**

off(type: 'requestMore', callback?: Callback<void>): void

在on(type: 'requestMore')函数调用之后使用，用于注销拉到播放列表底端或播放到文章最后一篇的回调函数。注销监听后，可以重新注册。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'requestMore'，请求更多文章时，触发该事件监听。 |
| callback | Callback<void> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数（当前仅有一个）。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.off('requestMore');
} catch (e) {
  console.error(`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}`);
}
```

**off(type: 'requestMore')**

off(type: 'requestMore', callback: Callback<string>): void

在on(type: 'requestMore')函数调用之后使用，用于注销拉到播放列表底端或播放到文章最后一篇带用户自定义参数的回调函数。注销监听后，可以重新注册。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.3(15)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'requestMore'，请求更多文章时，触发该事件监听。 |
| callback | Callback<string> | 是 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.off('requestMore', (callback:string) => {
    console.info(`Succeeded in setting requestMoreListener. Callback is ${callback}`);
  });
} catch (e) {
  console.error(`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}`);
}
```

**on(type: 'eventNotification' | 'eventPanel')**

on(type: 'eventNotification' | 'eventPanel', callback: Callback<NotificationEvent| PanelEvent>): void

注册播控中心/播放面板状态回调函数，播控中心/播放面板状态发生变化时，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型。 - 'eventNotification'：播控中心状态变化。 - 'eventPanel'：播放面板状态变化，其中PanelEvent中的BPC_10 click事件回调只支持手机。 |
| callback | Callback<NotificationEvent | PanelEvent> | 是 | 播控中心/播放面板状态发生变化时，触发该回调执行。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.on('eventNotification', (ne: TextReader.NotificationEvent) => {
    console.info(`Succeeded in setting eventNotificationListener: ${JSON.stringify(ne)}`);
  });
  TextReader.on('eventPanel', (pe: TextReader.PanelEvent) => {
    console.info(`Succeeded in setting eventPanelListener: ${JSON.stringify(pe)}`);
  });
} catch (e) {
  console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
}
```

**off(type: 'eventNotification' | 'eventPanel')**

off(type: 'eventNotification' | 'eventPanel', callback?: Callback<NotificationEvent | PanelEvent>): void

在on(type: 'eventNotification' | 'eventPanel')函数调用之后使用，用于注销播控中心、播放面板状态发生变化的回调函数。注销监听后，可以重新注册。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型。 - 'eventNotification'：播控中心状态变化。 - 'eventPanel'：播放面板状态变化。 |
| callback | Callback<NotificationEvent | PanelEvent> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数（当前仅有一个）。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.off('eventNotification');
  TextReader.off('eventPanel');
} catch (e) {
  console.error(`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}`);
}
```

**on(type: 'eventReadList')**

on(type: 'eventReadList', callback: Callback<Array<ListEventState>>): void

注册播报列表相关事件监听，点击播报列表图标时，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'eventReadList'。 |
| callback | Callback<Array<ListEventState>> | 是 | 播报列表发生相关事件时，触发该回调执行。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.on('eventReadList', (list: Array<TextReader.ListEventState>) => {
    list.forEach((id) => {
      console.info(`Succeeded in setting eventReadListListener, article id: ${id}`);
    })
  });
} catch (e) {
  console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
}
```

**off(type: 'eventReadList')**

off(type: 'eventReadList', callback?: Callback<Array<ListEventState>>): void

在on(type: 'eventReadList')函数调用之后使用，用于注销播报列表相关事件的回调函数。注销监听后，可以重新注册。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'eventReadList'。 |
| callback | Callback<Array<ListEventState>> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数（当前仅有一个）。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.off('eventReadList');
} catch (e) {
  console.error(`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}`);
}
```

**on(type: 'readProgress')**

on(type: 'readProgress', callback: Callback<ReadProgress>): void

注册已播放时长相关事件监听，已播放时长发生相关事件时，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.2(14)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'readProgress'。 |
| callback | Callback<ReadProgress> | 是 | 已播放时长发生相关事件时，触发该回调执行。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.on('readProgress', (readProgress: TextReader.ReadProgress) => {
    console.info(`Succeeded in setting readProgressListener: ${JSON.stringify(readProgress)}`);
  });
} catch (e) {
  console.error(`TextReader failed to set readProgressListener. Code: ${e.code}, message: ${e.message}`);
}
```

**off(type: 'readProgress')**

off(type: 'readProgress', callback?: Callback<ReadProgress>): void

在on(type: 'readProgress')函数调用之后使用，用于注销已播放时长相关事件的回调函数。注销监听后，可以重新注册。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.2(14)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'readProgress'。 |
| callback | Callback<ReadProgress> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数（当前仅有一个）。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.off('readProgress');
} catch (e) {
  console.error(`TextReader failed to unset readProgressListener. Code: ${e.code}, message: ${e.message}`);
}
```

**Person**

人物语气和风格信息

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tone | number | 否 | 否 | 人物语气信息。 0：女声。 |
| style | string | 否 | 否 | 人物风格信息。 - reading：朗读风格。（暂不支持） - interaction-oral：口语化风格。（暂不支持） - interaction-broadcast：播音风格。 |

**ReaderParam**

朗读参数

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isVoiceBrandVisible | boolean | 否 | 否 | 是否显示播报品牌。 - 默认false：不显示品牌信息。 - 配置为true：显示品牌信息。 |
| businessBrandInfo | BusinessBrandInfo | 否 | 是 | 播报品牌信息。 - 默认是：小艺朗读。 |
| isFastForward | boolean | 否 | 是 | 快进快退逻辑。 - 默认false：上下一句切换。 - 配置为true：快进快退15秒。 |
| keepBackgroundRunning | boolean | 否 | 是 | 是否使用保持后台运行的功能。 预留参数，暂未支持。 如需要设置后台运行功能，请配置长时任务权限。 |
| online | number | 否 | 是 | 默认离线合成模式。 0为在线（暂不支持），1为离线。 |
| person | Person | 否 | 是 | 朗读人员语气和风格信息，默认参数如下。 { tone: 0, style: 'interaction-broadcast' } 起始版本： 5.0.2(14) |
| isMinibarNeeded | boolean | 否 | 是 | 是否使用Minibar功能。 - 默认true：使用Minibar功能。 - 配置为false：不使用Minibar功能，这时hideMinibar、showMinibar 方法无效。 起始版本： 5.0.2(14) |
| minibarParams | MinibarParams | 否 | 是 | Minibar位置设置，默认吸附左边。 起始版本： 5.0.2(14) |
| customFeatures | CustomFeature[] | 否 | 是 | 朗读控件的自定义功能，默认空。 起始版本： 5.0.2(14) |
| displayTab | DisplayTab | 否 | 是 | 显示Tab页配置，默认显示封面和内容页。 起始版本： 5.0.2(14) |
| reportProgressPeriod | number | 否 | 是 | 多久返回一次已播放时长日志信息，默认为0，不回调。 单位：毫秒。 起始版本： 5.0.2(14) |

**StartParams**

朗读控件起播参数

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isMinibarHidden | boolean | 否 | 是 | Minibar是否隐藏。 - 默认false：不隐藏Minibar。 - 配置为true：隐藏Minibar。 元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| callbackParam | string | 否 | 是 | 用于三方自定义场景参数，在requestMore监听中返回，默认空。 元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| startPercent | number | 否 | 是 | 指定起始播报位置，取值范围[0,100]，默认为0。 元服务API： 从版本6.0.1(21)开始，该接口支持在元服务中使用。 起始版本： 6.0.1(21) |

**MinibarParams**

起播时控制Minibar的参数，可以设置Minibar初始化位置，以及与底部边框的距离。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| defaultAlignment | BarAlignment | 否 | 否 | Minibar默认吸附位置。 元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| bottom | number | 否 | 是 | Minibar离底部边缘距离，垂直方向固定，仅支持左右拖动。 取值大于等于0，默认值为50，单位为vp，超过屏幕范围不显示Minibar。 元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| isSpeedIconVisible | boolean | 否 | 是 | Minibar是否显示倍速播放按钮。 默认是true，显示播放按钮。 配置为false，不显示播放按钮。 元服务API： 从版本6.0.1(21)开始，该接口支持在元服务中使用。 起始版本： 6.0.1(21) |
| isNextIconVisible | boolean | 否 | 是 | Minibar是否显示下一篇按钮。 配置是true，显示下一篇按钮。 默认为false，不显示下一篇按钮。 元服务API： 从版本6.0.1(21)开始，该接口支持在元服务中使用。 起始版本： 6.0.1(21) |

**BusinessBrandInfo**

播报品牌信息

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| panelName | string | 否 | 是 | - 播放面板顶部展示的业务名称，系统字体大小为标准时，英文占1个字符长度，中文占2个字符长度，累计超过24个字符长度时会省略显示。（系统字体大小有变动时，显示长度会有变化） - Pura X设备不显示。 |
| panelIcon | ResourceStr | 否 | 是 | 播放面板顶部展示的业务图标。 预留参数，暂未支持。 |
| notificationIcon | ResourceStr | 否 | 是 | 通知栏展示的业务图标。 预留参数，暂未支持。 |
| notificationName | string | 否 | 是 | 通知栏展示的业务名称。 预留参数，暂未支持。 |

**ReadState**

播报状态。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 文章id。 |
| state | ReadStateCode | 否 | 否 | 当前的朗读状态。 |
| categoryId | string | 否 | 是 | 文章分类ID。 起始版本： 5.0.2(14) |
| isLastArticle | boolean | 否 | 是 | 分组播报情况时： true表示是分组的最后一篇文章。 false则不是。 非分组播报情况时： true表示是列表最后一篇文章。 false则不是。 起始版本： 5.0.2(14) |

**CustomFeature**

朗读控件面板中的自定义功能。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | CustomFeatureType | 否 | 否 | 自定义特征的类型，系统应用或者用户自定义功能。 |
| name | string | 否 | 否 | 自定义特征的名称。 当type=CustomFeatureType.SYSTEM时，支持的系统特征名称包括： - favorite（收藏）。 - countdown（定时器）。 |
| icon | ResourceStr | 否 | 是 | 自定义特性图标，支持url及本地资源。 默认为空。 当type=CustomFeatureType.SYSTEM时，系统特征为固定图标，不需要额外指定。 |
| callback | Callback<string> | 否 | 是 | 自定义特性的回调，回调参数为当前播放的文章id。 |

示例：

```ets
import { TextReader } from '@kit.SpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  // 获取应用上下文
  aboutToAppear() {
    const customFeaturesToAdd: TextReader.CustomFeature[] = [
      {
        type: TextReader.CustomFeatureType.SYSTEM,
        name: 'countdown',
        icon: '',
        callback: (id) => {
          console.info(`Custom feature callback.`)
        }
    ]
    const readerParams: TextReader.ReaderParam = {
      // ... 其他字段配置
      customFeatures: customFeaturesToAdd,
      isVoiceBrandVisible: false
    }
    let context: Context | undefined = this.getUIContext().getHostContext();
    if (context) {
      TextReader.init(context, readerParams).then(() => {
        console.info(`TextReader succeeded in initializing.`);
      }).catch((e: BusinessError) => {
        console.error(`TextReader failed to initialize. Code: ${e.code}, message: ${e.message}`);
      })
    }

  build() {
    // ...
  }
```

**ReadInfo**

朗读信息。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 文章标识ID，不能为空字符串。 |
| title | TextInfo | 否 | 否 | 标题。 |
| category | string | 否 | 是 | 类目，默认空。 |
| author | TextInfo | 否 | 是 | 文章的作者，默认空。 |
| date | TextInfo | 否 | 是 | 文章的时间（例:Mon Jul 08 2024 21:25:41 GMT+0800）。 预留参数，暂未支持。 |
| image | image.PixelMap | 否 | 是 | 封面图图片。图片转为PixelMap后的最大大小为8MB。 若未传，采用默认封面图。 |
| imageUrl | string | 否 | 是 | 文章封面图片链接。 若未传，采用默认封面图。图片的宽高大于10242048时会进行压缩。 image和imageUrl同时存在的时候，image设置生效。 起始版本： 5.0.2(14) |
| bodyInfo | string | 否 | 是 | setArticle以及loadMore接口必填。 实时朗读的正文信息。 从6.1.0(23)版本开始，正文长度支持10000字符以上。6.0.2(22)及之前版本，正文中无标点符号和换行符的情况下，长度须小于等于10000字符。 |
| bodyInfoObject | BodyInfo | 否 | 是 | 正文内容信息，默认空。 起始版本： 5.0.2(14) |
| categoryObject | CategoryInfo | 否 | 是 | 文章分类信息，默认空。 起始版本： 5.0.2(14) |
| audioInfo | AudioInfo[] | 否 | 是 | 音频信息，默认空。 若配置此参数，则优先使用传入音频进行播报。 起始版本： 5.0.2(14) |
| isFavorite | boolean | 否 | 是 | true表示已喜欢/收藏。 false表示不喜欢/未收藏。 默认false。 起始版本： 5.0.2(14) |

**CategoryInfo**

文章分类信息

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.2(14)

参数：

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 文章分类ID。 |
| name | string | 否 | 否 | 文章分类的名称。 |
| image | image.PixelMap | string | 否 | 否 | 文章分类的图片或者图片的url，优先级大于文章封面图片。 |

**TextInfo**

文字信息

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | string | 否 | 否 | 文本。 |
| isClickable | boolean | 否 | 否 | 是否支持点击收回播报面板。 - true：点击收回播报面板。 - false：点击不收回播报面板。 |

**BodyInfo**

readInfo的正文内容信息

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.2(14)

参数：

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | BodyInfoType | 否 | 否 | 类型。 |
| body | string | 否 | 是 | 正文内容，默认空。 |

**AudioInfo**

朗读控件中的音频信息

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.2(14)

参数：

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| format | string | 否 | 否 | 音频信息格式，如mp3、mp4a、wma、wav。 |
| duration | number | 否 | 否 | 音频信息的持续时间，单位：秒。 |
| size(deprecated) | number | 否 | 否 | 音频信息的大小，单位：字节。 说明： 从6.1.0(23)开始废弃。 |
| person | Person | 否 | 是 | 音频信息的声音信息，包括音色、风格，语言等。 默认为如下参数 { tone: 3, style: 'interaction-broadcast' } |
| url | string | 否 | 否 | 音频信息的URL。 |

**ReadProgress**

朗读控件中的音频信息

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.2(14)

参数：

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 播报文章ID。 元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| categoryId | string | 否 | 否 | 文章列表分组ID。 元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| readProgressType | ReadProgressType | 否 | 否 | 定时上报类型。 元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| person | Person | 否 | 否 | 正在播报的文章使用的音色。 元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| maxPercent | number | 否 | 否 | 触发该事件回调时，用户曾经播放的最大的百分比，而不是当前用户所处于的百分比 取值[0,100]。 【计算生成方式】 音频播放的最大百分比进度，四舍五入取整。例如音频播放到80%，拖动滚动条回到20%后停止播放，最终取值为80。 重播时重置。 元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| currentPercent | number | 否 | 否 | 触发该事件回调时，返回用户当前播放的百分比，取值[0,100]。可用于记录上次播放位置，和start接口配合实现下次继续播放。 元服务API： 从版本6.0.1(21)开始，该接口支持在元服务中使用。 起始版本： 6.0.1(21) |

**PanelEvent**

播放面板事件

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 文章ID。 |
| click | string | 否 | 否 | - BPC_01：播放按钮点击。 - BPC_02：暂停按钮点击。 - BPC_03：上一条按钮点击。 - BPC_04：下一条按钮点击。 - BPC_05：语速按钮点击。 - BPC_06：音色按钮点击。 - BPC_07：播报列表点击。 - BPC_08：标题点击。 - BPC_09：作者点击。 - BPC_10：左上角箭头或下滑关掉。 |
| categoryId | string | 否 | 是 | 文章分类ID。 起始版本： 5.0.2(14) |

**NotificationEvent**

通知栏事件

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 文章ID。 |
| type | number | 否 | 否 | 1：通知栏点击回调。 2：播控中心点击回调。 |
| click | string | 否 | 否 | - NBC_01：播放按钮点击。 - NBC_02：暂停按钮点击、移除通知栏播控中心。 - NBC_03：关闭按钮点击（预留能力，暂未支持）。 - NBC_04：上一条按钮点击。 - NBC_05：下一条按钮点击。 - NBC_06：文章图片点击（预留能力，暂未支持）。 - NBC_07：文章标题点击（预留能力，暂未支持）。 |
| categoryId | string | 否 | 是 | 文章分类ID。 起始版本： 5.0.2(14) |

**ListEventState**

列表事件状态

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.0(12)

参数：

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 文章ID。 |
| categoryId | string | 否 | 是 | 文章分类ID。 起始版本： 5.0.2(14) |

**ResetParamType**

用于确定重置类型的枚举类。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.2(14)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BAR_PARAM | 1 | 重置Minibar参数。 |
| ALL | 2 | 重置所有本地数据，恢复为初始化配置参数，包括Minibar参数重置，文章列表置空。 |
| READ_LIST | 3 | 重置文章列表。 |

**DisplayTab**

用于确定播控面板显示的Tab标签及Tab内容的枚举类。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

设备行为差异： 该接口在PC/2in1中无效果，在其他设备类型中可正常调用。

起始版本： 5.0.2(14)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COVER_AND_CONTENT | 1 | 显示封面页和内容页，并且显示Tab标签按钮。 |
| CONTENT | 2 | 仅显示内容页，不显示Tab标签按钮。 |
| COVER | 3 | 仅显示封面页，不显示Tab标签按钮。 |

**BarAlignment**

用于确定Minibar默认吸附位置的枚举类。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.2(14)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEFT | 1 | 吸附在左侧。 |
| RIGHT | 2 | 吸附在右侧。 |

**BodyInfoType**

用于确定正文信息类型的枚举类。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.2(14)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONTENT | 1 | 正文内容类型。 |
| FILE_PATH | 2 | 文件路径类型。 |

**CustomFeatureType**

用于确定自定义特征类型的枚举类。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.2(14)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SYSTEM | 1 | 系统自定义功能。 |
| USER | 2 | 用户自定义功能。 |

**ReadProgressType**

用于确定已播报时长上报类型的枚举类。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AI.Component.TextReader

起始版本： 5.0.2(14)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PROGRESS | 1 | 播放中定时上报。 |
| PAUSE | 2 | 暂停时上报。 |
| STOP | 3 | 停止播放时上报。 |
| COMPLETED | 4 | 文章读完时上报。 |