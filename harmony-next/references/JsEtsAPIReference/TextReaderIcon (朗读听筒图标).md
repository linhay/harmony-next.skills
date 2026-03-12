# TextReaderIcon (朗读听筒图标)

朗读听筒图标，可以作为动态组件加载，并配置成为播放面板的主入口。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { TextReaderIcon } from '@kit.SpeechKit';
```

#### TextReaderIcon

朗读听筒图标，可以作为动态组件加载。设置onClick回调，在用户点击听筒图标时启动朗读控件。

**装饰器类型：**@Component

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AI.Component.TextReader

**起始版本：**5.0.0(12)

**参数：**

名称

类型

必填

装饰器类型

说明

readState

[ReadStateCode](ReadStateCode (播报状态).md)

是

@Link

播报状态

**说明：**

ReadState使用[@Link装饰器：父子双向同步](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-link)

#### build

build(): void

用于创建[TextReaderIcon](#section71306437290)对象的构造函数。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AI.Component.TextReader

**起始版本：**5.0.0(12)

**示例：**

```ets
import { TextReader, TextReaderIcon, ReadStateCode } from '@kit.SpeechKit';

@Entry
@Component
struct Index {

  /**
   * 待加载的文章
   */
  @State readInfoList: TextReader.ReadInfo[] = [];
  @State selectedReadInfo: TextReader.ReadInfo = this.readInfoList[0];

  /**
   * 播放状态
   */
  @State readState: ReadStateCode = ReadStateCode.WAITING;

  /**
   * 用于显示当前页的按钮状态
   */
  @State isInit: boolean = false;

  async aboutToAppear(){
    /**
     * 加载数据
     */
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
    this.init();
  }

  /**
   * 初始化
   */
  async init() {
    const readerParam: TextReader.ReaderParam = {
      isVoiceBrandVisible: true,
      businessBrandInfo: {
        panelName: '小艺朗读',
        panelIcon: $r('app.media.startIcon')
      }
    }
    try {
      let context: Context | undefined = this.getUIContext().getHostContext()
      if (context) {
        await TextReader.init(context, readerParam);
        this.isInit = true;
      }
    } catch (err) {
      console.error(`TextReader failed to init. Code: ${err.code}, message: ${err.message}`);
    }
  }

  // 设置操作监听
  setActionListener() {
    TextReader.on('stateChange', (state: TextReader.ReadState) => {
      this.onStateChanged(state)
    });
    TextReader.on('requestMore', () => this.onStateChanged);
  }

  onStateChanged = (state: TextReader.ReadState) => {
    if (this.selectedReadInfo?.id === state.id) {
      this.readState = state.state;
    } else {
      this.readState = ReadStateCode.WAITING;
    }
  }

  build() {
    Column() {
      TextReaderIcon({ readState: this.readState })
        .margin({ right: 20 })
        .width(32)
        .height(32)
        .onClick(async () => {
          try {
            this.setActionListener();
            await TextReader.start(this.readInfoList, this.selectedReadInfo?.id);
          } catch (err) {
            console.error(`TextReader failed to start. Code: ${err.code}, message: ${err.message}`);
          }
        })
    }
    .height('100%')
  }
}
```