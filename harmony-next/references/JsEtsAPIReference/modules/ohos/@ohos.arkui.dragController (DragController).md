# @ohos.arkui.dragController (DragController)

本模块提供发起主动拖拽的能力，当应用接收到触摸或长按等事件时可以主动发起拖拽的动作，并在其中携带拖拽信息。

-

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](../../types/classes/Class (UIContext).md)的地方使用，参见[UIContext](Class (UIContext).md)说明。

-

示例效果请以真机运行为准，当前 DevEco Studio预览器不支持。

#### 导入模块

```ets
import { dragController } from '@kit.ArkUI';
```

#### dragController.executeDrag(deprecated)

executeDrag(custom: [CustomBuilder](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8) | [DragItemInfo](../../topics/components/拖拽事件.md#ZH-CN_TOPIC_0000002529444781__dragiteminfo), dragInfo: DragInfo,callback:AsyncCallback<DragEventParam>): void

主动发起拖拽能力，传入拖拽发起后跟手效果所拖拽的对象以及携带拖拽信息。使用callback异步回调。


-

从API version 10开始支持，从API version 18开始废弃，建议使用[executeDrag](Class (DragController).md#ZH-CN_TOPIC_0000002522080726__executedrag11)替代。executeDrag需先通过[UIContext](Class (UIContext).md)中的[getDragController](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getdragcontroller11)方法获取[DragController](Class (DragController).md)实例，然后通过该对象进行调用。

-

从API version 11开始，可以通过使用[UIContext](Class (UIContext).md)中的[getDragController](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getdragcontroller11)方法获取当前UI上下文关联的[DragController](Class (DragController).md)对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| custom | [CustomBuilder](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8) | DragItemInfo | 是 | 拖拽发起后跟手效果所拖拽的对象。 说明： 不支持全局builder。如果builder中使用了[Image](../../types/interfaces/Image.md)组件，应尽量开启同步加载，即配置Image的[syncLoad](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__syncload8)为true。该builder只用于生成当次拖拽中显示的图片。builder的根组件宽高为0时，无法生成拖拽显示的图片导致拖拽失败。builder的修改不会同步到当前正在拖拽的图片，对builder的修改需要在下一次拖拽时生效。 |
| dragInfo | DragInfo | 是 | 拖拽信息。 |
| callback | AsyncCallback<[DragEvent](../../topics/components/拖拽事件.md#ZH-CN_TOPIC_0000002529444781__dragevent7)Param> | 是 | 回调函数。当拖拽成功结束，err为undefined，data为获取到的DragEventParam；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal handling failed. |

**示例：**


推荐通过使用[UIContext](Class (UIContext).md)中的[getDragController](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getdragcontroller11)方法获取当前UI上下文关联的DragController对象。

```ets
import { dragController } from '@kit.ArkUI';
import { unifiedDataChannel } from '@kit.ArkData';

class DragInfo {
  event: DragEvent | undefined = undefined;
  extraParams: string = '';
}

@Entry
@Component
struct DragControllerPage {
  @State text: string = ''

  @Builder
  DraggingBuilder() {
    Column() {
      Text("DraggingBuilder")
        .fontColor(Color.White)
        .fontSize(12)
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  build() {
    Column() {
      Button('touch to execute drag')
        .margin(10)
        .onTouch((event?:TouchEvent) => {
          if(event){
            if (event.type == TouchType.Down) {
              let text = new unifiedDataChannel.PlainText()
              text.textContent = 'drag text'
              text.abstract = 'abstract'
              let unifiedData = new unifiedDataChannel.UnifiedData(text)

              let dragInfo: dragController.DragInfo = {
                pointerId: 0,
                data: unifiedData,
                extraParams: ''
              }
              let eve: DragInfo = new DragInfo();
              this.getUIContext().getDragController().executeDrag(() => {
                this.DraggingBuilder()
              }, dragInfo, (err, eve) => { // 建议使用 this.getUIContext().getDragController().executeDrag()接口
                if(eve.event){
                  if (eve.event.getResult() == DragResult.DRAG_SUCCESSFUL) {
                    // ...
                  } else if (eve.event.getResult() == DragResult.DRAG_FAILED) {
                    // ...
                  }
              })
          }
        })
      Text(this.text)
        .height(100)
        .width(150)
        .margin({top:20})
        .border({color:Color.Black,width:1})
        .onDrop((dragEvent?:DragEvent)=>{
          if(dragEvent){
            let records: Array<unifiedDataChannel.UnifiedRecord> = dragEvent.getData().getRecords();
            let plainText: unifiedDataChannel.PlainText = records[0] as unifiedDataChannel.PlainText;
            this.text = plainText.textContent;
          }
        })
    }
    .width('100%')
    .height('100%')
  }
```

#### dragController.executeDrag(deprecated)

executeDrag(custom: [CustomBuilder](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8) | DragItemInfo, dragInfo: DragInfo): Promise<DragEventParam>

主动发起拖拽能力，传入拖拽发起后跟手效果所拖拽的对象以及携带拖拽信息。使用Promise异步回调。


-

从API version 10开始支持，从API version 18开始废弃，建议使用[executeDrag](Class (DragController).md#ZH-CN_TOPIC_0000002522080726__executedrag11-1)替代。executeDrag需先通过[UIContext](Class (UIContext).md)中的[getDragController](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getdragcontroller11)方法获取[DragController](Class (DragController).md)实例，然后通过该对象进行调用。

-

从API version 11开始，可以通过使用[UIContext](Class (UIContext).md)中的[getDragController](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getdragcontroller11)方法获取当前UI上下文关联的[DragController](Class (DragController).md)对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| custom | [CustomBuilder](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8) | DragItemInfo | 是 | 拖拽发起后跟手效果所拖拽的对象。 |
| dragInfo | DragInfo | 是 | 拖拽信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DragEvent](../../topics/components/拖拽事件.md#ZH-CN_TOPIC_0000002529444781__dragevent7)Param> | Promise对象，拖拽结束返回结果的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal handling failed. |

**示例：**


推荐通过使用[UIContext](Class (UIContext).md)中的[getDragController](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getdragcontroller11)方法获取当前UI上下文关联的DragController对象。

```ets
import { dragController } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';
import { unifiedDataChannel } from '@kit.ArkData';

class DragInfo {
  event: DragEvent | undefined = undefined;
  extraParams: string = '';
}

@Entry
@Component
struct DragControllerPage {
  @State pixmap: image.PixelMap|undefined = undefined
  @State text: string = ''

  @Builder
  DraggingBuilder() {
    Column() {
      Text("DraggingBuilder")
        .fontColor(Color.White)
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  @Builder
  PixmapBuilder() {
    Column() {
      Text("PixmapBuilder")
        .fontColor(Color.White)
        .fontSize(15)
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  aboutToAppear() {
    let pb: CustomBuilder = (): void => {
      this.PixmapBuilder()
    }
    this.getUIContext().getComponentSnapshot().createFromBuilder(pb).then((pix: image.PixelMap) => {
      this.pixmap = pix;
    })
  }

  build() {
    Column() {
      Button('touch to execute drag')
        .margin(10)
        .onTouch((event?:TouchEvent) => {
          if(event){
            if (event.type == TouchType.Down) {
              let text = new unifiedDataChannel.PlainText()
              text.textContent = 'drag text'
              text.abstract = 'abstract'
              let unifiedData = new unifiedDataChannel.UnifiedData(text)

              let dragInfo: dragController.DragInfo = {
                pointerId: 0,
                data: unifiedData,
                extraParams: ''
              }
              let dragItemInfo: DragItemInfo = {
                pixelMap: this.pixmap,
                builder: () => {
                  this.DraggingBuilder()
                },
                extraInfo: "DragItemInfoTest"
              }
              let eve: DragInfo = new DragInfo();
              this.getUIContext()
                .getDragController()
                .executeDrag(dragItemInfo, dragInfo) // 建议使用 this.getUIContext().getDragController().executeDrag()接口
                .then((eve) => {
                  if (eve.event.getResult() == DragResult.DRAG_SUCCESSFUL) {
                    // ...
                  } else if (eve.event.getResult() == DragResult.DRAG_FAILED) {
                    // ...
                  }
                })
                .catch((err:Error) => {
                })
          }
        })
      Text(this.text)
        .height(100)
        .width(150)
        .margin({top:20})
        .border({color:Color.Black,width:1})
        .onDrop((dragEvent?:DragEvent)=>{
          if(dragEvent){
            let records: Array<unifiedDataChannel.UnifiedRecord> = dragEvent.getData().getRecords();
            let plainText: unifiedDataChannel.PlainText = records[0] as unifiedDataChannel.PlainText;
            this.text = plainText.textContent;
          }
        })
    }
    .width('100%')
    .height('100%')
  }
```

#### DragInfo

发起拖拽所需要的属性和拖拽时携带的信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pointerId | number | 否 | 否 | 设置启动拖拽时屏幕上触摸点的Id。取值范围为[0, 9]的整数。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| data | unifiedDataChannel.UnifiedData | 否 | 是 | 设置拖拽过程中携带的数据。 默认值：空 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| extraParams | string | 否 | 是 | 设置拖拽事件额外信息，具体功能暂未实现。 默认值：空 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| touchPoint11+ | [TouchPoint](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__touchpoint11) | 否 | 是 | 配置跟手点坐标。不配置时，左右居中，顶部向下偏移20%。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| previewOptions11+ | [DragPreviewOptions](../../topics/components/拖拽控制.md#ZH-CN_TOPIC_0000002497604842__dragpreviewoptions11) | 否 | 是 | 设置拖拽过程中背板图处理模式及数量角标的显示。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| dataLoadParams20+ | unifiedDataChannel.DataLoadParams | 否 | 是 | 设置拖起方延迟提供数据。调用此方法向系统提供数据加载参数，而非直接传入完整的数据对象。当用户将数据拖拽至目标应用程序并释放时，系统将使用此参数从起拖方请求实际数据。与data同时设置时，dataLoadParams生效。 默认值：空 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |

#### dragController.createDragAction(deprecated)

createDragAction(customArray: Array<[CustomBuilder](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8) | DragItemInfo>, dragInfo: DragInfo): DragAction

创建拖拽的Action对象，需要显式指定拖拽背板图(可多个)，以及拖拽的数据，跟手点等信息；当通过一个已创建的 Action 对象发起的拖拽未结束时，无法再次创建新的 Action 对象，接口会抛出异常；当Action对象的生命周期结束后，注册在该对象上的回调函数会失效，因此需要在一个尽量长的作用域下持有该对象，并在每次发起拖拽前通过createDragAction返回新的对象覆盖旧值。


-

从API version 11开始支持，从API version 18开始废弃，建议使用[createDragAction](Class (DragController).md#ZH-CN_TOPIC_0000002522080726__createdragaction11)替代。createDragAction需先通过[UIContext](Class (UIContext).md)中的[getDragController](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getdragcontroller11)方法获取[DragController](Class (DragController).md)实例，然后通过该对象进行调用。

-

从API version 11开始，可以通过使用[UIContext](Class (UIContext).md)中的[getDragController](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getdragcontroller11)方法获取当前UI上下文关联的[DragController](Class (DragController).md)对象。

-

建议控制传递的拖拽背板数量，传递过多容易导致拖起的效率问题。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| customArray | Array<[CustomBuilder](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8) | DragItemInfo> | 是 | 拖拽发起后跟手效果所拖拽的对象。 |
| dragInfo | DragInfo | 是 | 拖拽信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DragAction | 创建拖拽Action对象，主要用于后面实现注册监听拖拽状态改变事件和启动拖拽服务。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal handling failed. |

**示例：**


推荐通过使用[UIContext](Class (UIContext).md)中的[getDragController](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getdragcontroller11)方法获取当前UI上下文关联的DragController对象。

```ets
import { dragController } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';
import { unifiedDataChannel } from '@kit.ArkData';

@Entry
@Component
struct DragControllerPage {
  @State pixmap: image.PixelMap | null = null
  @State text: string = ''
  private dragAction: dragController.DragAction | null = null;
  customBuilders:Array<CustomBuilder | DragItemInfo> = new Array<CustomBuilder | DragItemInfo>();

  @Builder
  DraggingBuilder() {
    Column() {
      Text("DraggingBuilder")
        .fontColor(Color.White)
        .fontSize(12)
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  build() {
    Column() {

      Column() {
        Text(this.text)
          .width('100%')
          .height('100%')
          .fontColor(Color.White)
          .fontSize(18)
          .onDrop((dragEvent?:DragEvent)=>{
            if(dragEvent){
              let records: Array<unifiedDataChannel.UnifiedRecord> = dragEvent.getData().getRecords();
              let plainText: unifiedDataChannel.PlainText = records[0] as unifiedDataChannel.PlainText;
              this.text = plainText.textContent;
            }
          })
      }
      .width(100)
      .height(100)
      .backgroundColor(Color.Red)
      .margin(10)

      Button('多对象dragAction customBuilder拖拽').onTouch((event?:TouchEvent) => {
        if(event){
          if (event.type == TouchType.Down) {
            console.info("multi drag Down by listener");
            this.customBuilders.splice(0, this.customBuilders.length);
            this.customBuilders.push(() => {
              this.DraggingBuilder()
            });
            this.customBuilders.push(() => {
              this.DraggingBuilder()
            });
            this.customBuilders.push(() => {
              this.DraggingBuilder()
            });
            let text = new unifiedDataChannel.PlainText()
            text.textContent = 'drag text'
            let unifiedData = new unifiedDataChannel.UnifiedData(text)
            let dragInfo: dragController.DragInfo = {
              pointerId: 0,
              data: unifiedData,
              extraParams: ''
            }
            try{
              this.dragAction = this.getUIContext()
                .getDragController()
                .createDragAction(this.customBuilders,
                  dragInfo) // 建议使用 this.getUIContext().getDragController().createDragAction()接口
              if(!this.dragAction){
                console.info("listener dragAction is null");
                return
              }
              this.dragAction.on('statusChange', (dragAndDropInfo: dragController.DragAndDropInfo)=>{
                if (dragAndDropInfo.status == dragController.DragStatus.STARTED) {
                  console.info("drag has start");
                } else if (dragAndDropInfo.status == dragController.DragStatus.ENDED){
                  console.info("drag has end");
                  if (!this.dragAction) {
                    return
                  }
                  this.dragAction.off('statusChange')
                }
              })
              this.dragAction.startDrag().then(() => {
              }).catch((err: Error) => {
                console.error(`start drag Error:${err.message}`);
              })
            } catch(err) {
              console.error(`create dragAction Error:${err.message}`);
        }
      }).margin({top:20})
}
```

#### DragAction11+

监听状态改变，启动拖拽服务的对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### startDrag11+

startDrag(): Promise<void>

启动拖拽服务。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 100001 | Internal handling failed. |

**示例1：**


推荐通过使用[UIContext](Class (UIContext).md)中的[getDragController](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getdragcontroller11)方法获取当前UI上下文关联的DragController对象。

```ets
import { dragController } from '@kit.ArkUI';
import { unifiedDataChannel } from '@kit.ArkData';

@Entry
@Component
struct DragControllerPage {
  private dragAction: dragController.DragAction | null = null;
  customBuilders:Array<CustomBuilder | DragItemInfo> = new Array<CustomBuilder | DragItemInfo>();

  @Builder
  DraggingBuilder() {
    Column() {
      Text("DraggingBuilder")
        .fontColor(Color.White)
        .fontSize(12)
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  build() {
    Column() {
      Button('touch to execute drag').onTouch((event?:TouchEvent) => {
        if(event){
          if (event.type == TouchType.Down) {
            this.customBuilders.splice(0, this.customBuilders.length);
            this.customBuilders.push(() => {
              this.DraggingBuilder()
            });
            let text = new unifiedDataChannel.PlainText()
            text.textContent = 'drag text'
            let unifiedData = new unifiedDataChannel.UnifiedData(text)
            let dragInfo: dragController.DragInfo = {
              pointerId: 0,
              data: unifiedData,
              extraParams: ''
            }
            try{
              this.dragAction = this.getUIContext()
                .getDragController()
                .createDragAction(this.customBuilders,
                  dragInfo) // 建议使用 this.getUIContext().getDragController().createDragAction()接口
              if(!this.dragAction){
                console.info("listener dragAction is null");
                return;
              }
              this.dragAction.startDrag().then(() => {
              }).catch((err: Error) => {
                console.error(`start drag Error: ${err.message}`);
              })
            } catch(err) {
              console.error(`create dragAction Error: ${err.message}`);
            }
      }).margin({top:20})
    }
```

**示例2：**

从API version 20开始，在[DragInfo](#ZH-CN_TOPIC_0000002522240718__draginfo)中配置dataLoadParams，设置拖起方延迟提供数据。

```ets
import { unifiedDataChannel, uniformTypeDescriptor, uniformDataStruct } from '@kit.ArkData';
import { fileUri, fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
import { dragController } from '@kit.ArkUI';

@Entry
@Component
struct ImageExample {
  private dragAction: dragController.DragAction | null = null;
  customBuilders: Array<CustomBuilder | DragItemInfo> = new Array<CustomBuilder | DragItemInfo>();
  @State uri: string = "";
  @State blockArr: string[] = [];
  uiContext = this.getUIContext();
  udKey: string = '';

  @Builder
  DraggingBuilder() {
    Video({ src: $rawfile('test1.mp4'), controller: new VideoController() })
      .width(100)
      .height(100)
  }

  build() {
    Column() {
      Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceAround }) {
        Button('touch to execute drag')
          .margin(10)
          .onTouch((event?: TouchEvent) => {
            if (event) {
              if (event.type == TouchType.Down) {
                this.customBuilders.splice(0, this.customBuilders.length);
                this.customBuilders.push(() => {
                  this.DraggingBuilder()
                });
                const context: Context | undefined = this.uiContext.getHostContext();
                if (context) {
                  let loadHandler: unifiedDataChannel.DataLoadHandler = () => {
                    let data =
                      context.resourceManager.getRawFdSync('test1.mp4');
                    let filePath = context.filesDir + '/test1.mp4';
                    let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
                    let bufferSize = data.length as number;
                    let buf = new ArrayBuffer(bufferSize);
                    fs.readSync(data.fd, buf, { offset: data.offset, length: bufferSize });
                    fs.writeSync(file.fd, buf, { offset: 0, length: bufferSize });
                    fs.closeSync(file.fd);
                    context.resourceManager.closeRawFdSync('test1.mp4')
                    this.uri = fileUri.getUriFromPath(filePath);
                    let videoMp: uniformDataStruct.FileUri = {
                      uniformDataType: 'general.file-uri',
                      oriUri: this.uri,
                      fileType: 'general.video',
                    }
                    let unifiedRecord = new unifiedDataChannel.UnifiedRecord();
                    let unifiedData = new unifiedDataChannel.UnifiedData();
                    unifiedRecord.addEntry(uniformTypeDescriptor.UniformDataType.FILE_URI, videoMp);
                    unifiedData.addRecord(unifiedRecord);
                    return unifiedData;
                  }

                  let dragInfo: dragController.DragInfo = {
                    pointerId: 0,
                    extraParams: '',
                    dataLoadParams: {
                      loadHandler: loadHandler,
                      dataLoadInfo: { types: new Set([uniformTypeDescriptor.UniformDataType.VIDEO]), recordCount: 1 }
                    }

                  let func = (dragAndDropInfo: dragController.DragAndDropInfo) => {
                    console.info(`ndq Register to listen on drag status ${JSON.stringify(dragAndDropInfo)}`);
                  }
                  try {
                    this.dragAction = this.getUIContext()
                      .getDragController()
                      .createDragAction(this.customBuilders,
                        dragInfo)
                    if (!this.dragAction) {
                      console.info("listener dragAction is null");
                      return;
                    }
                    this.dragAction.on('statusChange', func);
                    this.dragAction.startDrag().then(() => {
                    }).catch((err: Error) => {
                      console.error(`start drag Error: ${err.message}`);
                    })
                  } catch (err) {
                    console.error(`create dragAction Error: ${err.message}`);
            }
          })
      }
      .margin({ bottom: 20 })

      Row() {
        Column() {
          Text('可释放区域')
            .fontSize('15dp')
            .height('10%')
          List() {
            ForEach(this.blockArr, (item: string, index) => {
              ListItem() {
                Video({ src: item, controller: new VideoController() })
                  .width(100)
                  .height(100)
                  .border({ width: 1 })
              }
              .margin({ left: 30, top: 30 })
            }, (item: string) => item)
          }
          .border({ width: 1 })
          .height('90%')
          .width('100%')
          .allowDrop([uniformTypeDescriptor.UniformDataType.VIDEO])
          .onDrop((event?: DragEvent, extraParams?: string) => {
            let context = this.uiContext.getHostContext() as common.UIAbilityContext;
            let pathDir: string = context.distributedFilesDir;
            let destUri = fileUri.getUriFromPath(pathDir);
            let progressListener: unifiedDataChannel.DataProgressListener =
              (progress: unifiedDataChannel.ProgressInfo, dragData: UnifiedData | null) => {
                if (dragData != null) {
                  let arr: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
                  if (arr.length > 0) {
                    if (arr[0].getType() === uniformTypeDescriptor.UniformDataType.VIDEO) {
                      this.blockArr.splice(JSON.parse(extraParams as string).insertIndex, 0, this.uri);
                    }
                  } else {
                    console.info('dragData arr is null');
                  }
                } else {
                  console.info('dragData is undefined');
                }
                console.info(`percentage: ${progress.progress}`);
              };
            let options: DataSyncOptions = {
              destUri: destUri,
              fileConflictOptions: unifiedDataChannel.FileConflictOptions.OVERWRITE,
              progressIndicator: unifiedDataChannel.ProgressIndicator.DEFAULT,
              dataProgressListener: progressListener,
            }
            try {
              this.udKey = (event as DragEvent).startDataLoading(options);
              console.info('udKey: ', this.udKey);
            } catch (e) {
              console.error(`startDataLoading errorCode: ${e.code}, errorMessage: ${e.message}`);
            }
          }, { disableDataPrefetch: true })
        }
        .height("50%")
        .width("90%")
        .border({ width: 1 })
      }

      Button('取消数据传输')
        .onClick(() => {
          try {
            this.getUIContext().getDragController().cancelDataLoading(this.udKey);
          } catch (e) {
            console.error(`cancelDataLoading errorCode: ${e.code}, errorMessage: ${e.message}`);
          }
        })
        .margin({ top: 10 })
    }.width('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002522084680.webp)

#### on('statusChange')11+

on(type: 'statusChange', callback: Callback<[DragAndDropInfo](#ZH-CN_TOPIC_0000002522240718__draganddropinfo11)>): void

注册监听拖拽状态改变事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'statusChange'，即注册监听拖拽状态改变事件。 |
| callback | Callback<DragAndDropInfo> | 是 | 回调函数，返回当前的DragAndDropInfo组件状态。 |

**示例：**


推荐通过使用[UIContext](Class (UIContext).md)中的[getDragController](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getdragcontroller11)方法获取当前UI上下文关联的DragController对象。

```ets
import { dragController } from '@kit.ArkUI';
import { unifiedDataChannel } from '@kit.ArkData';

@Entry
@Component
struct DragControllerPage {
  private dragAction: dragController.DragAction | null = null;
  customBuilders:Array<CustomBuilder | DragItemInfo> = new Array<CustomBuilder | DragItemInfo>();

  @Builder
  DraggingBuilder() {
    Column() {
      Text("DraggingBuilder")
        .fontColor(Color.White)
        .fontSize(12)
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  build() {
    Column() {
      Button('touch to execute drag').onTouch((event?:TouchEvent) => {
        if(event){
          if (event.type == TouchType.Down) {
            this.customBuilders.splice(0, this.customBuilders.length);
            this.customBuilders.push(() => {
              this.DraggingBuilder()
            });
            let text = new unifiedDataChannel.PlainText()
            text.textContent = 'drag text'
            let unifiedData = new unifiedDataChannel.UnifiedData(text)
            let dragInfo: dragController.DragInfo = {
              pointerId: 0,
              data: unifiedData,
              extraParams: ''
            }
            let func = (dragAndDropInfo: dragController.DragAndDropInfo) => {
              console.info(`Register to listen on drag status ${JSON.stringify(dragAndDropInfo)}`);
            }
            try{
              this.dragAction = this.getUIContext()
                .getDragController()
                .createDragAction(this.customBuilders,
                  dragInfo) // 建议使用 this.getUIContext().getDragController().createDragAction()接口
              if(!this.dragAction){
                console.info("listener dragAction is null");
                return;
              }
              // 监听状态改变，触发后打印func中的日志
              this.dragAction.on('statusChange', func);
              this.dragAction.startDrag().then(() => {
              }).catch((err: Error) => {
                console.error(`start drag Error: ${err.message}`);
              })
            } catch(err) {
              console.error(`create dragAction Error: ${err.message}`);
            }
      }).margin({top:20})
    }
```

#### off('statusChange')11+

off(type: 'statusChange', callback?: Callback<[DragAndDropInfo](#ZH-CN_TOPIC_0000002522240718__draganddropinfo11)>): void

取消注册监听拖拽状态改变事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'statusChange'，即取消监听拖拽状态改变事件。 |
| callback | Callback<DragAndDropInfo> | 否 | 回调函数，返回当前的DragAndDropInfo组件状态。 |

**示例：**


推荐通过使用[UIContext](Class (UIContext).md)中的[getDragController](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getdragcontroller11)方法获取当前UI上下文关联的DragController对象。

```ets
import { dragController } from '@kit.ArkUI';
import { unifiedDataChannel } from '@kit.ArkData';

@Entry
@Component
struct DragControllerPage {
  private dragAction: dragController.DragAction | null = null;
  customBuilders:Array<CustomBuilder | DragItemInfo> = new Array<CustomBuilder | DragItemInfo>();

  @Builder
  DraggingBuilder() {
    Column() {
      Text("DraggingBuilder")
        .fontColor(Color.White)
        .fontSize(12)
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  build() {
    Column() {
      Button('touch to execute drag').onTouch((event?:TouchEvent) => {
        if(event){
          if (event.type == TouchType.Down) {
            this.customBuilders.splice(0, this.customBuilders.length);
            this.customBuilders.push(() => {
              this.DraggingBuilder()
            });
            let text = new unifiedDataChannel.PlainText()
            text.textContent = 'drag text'
            let unifiedData = new unifiedDataChannel.UnifiedData(text)
            let dragInfo: dragController.DragInfo = {
              pointerId: 0,
              data: unifiedData,
              extraParams: ''
            }
            let func = (dragAndDropInfo: dragController.DragAndDropInfo) => {
              console.info(`Register to listen on drag status ${JSON.stringify(dragAndDropInfo)}`);
            }
            this.dragAction = this.getUIContext()
              .getDragController()
              .createDragAction(this.customBuilders,
                dragInfo) // 建议使用 this.getUIContext().getDragController().createDragAction()接口
            if(!this.dragAction){
              console.info("listener dragAction is null");
              return;
            }
            this.dragAction.on('statusChange', func);
            // 取消监听，发起拖拽后不会打印func中的日志
            this.dragAction.off('statusChange', func);
            this.dragAction.startDrag().then(() => {
            }).catch((err: Error) => {
              console.error(`start drag Error: ${err.message}`);
            })
          }
      }).margin({top:20})
}
```

#### DragAndDropInfo11+

拖拽过程中监听到status改变时上报的数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| status | DragStatus | 否 | 否 | 当前拖拽状态（启动和结束）。 |
| event | [DragEvent](../../topics/components/拖拽事件.md#ZH-CN_TOPIC_0000002529444781__dragevent7) | 否 | 否 | 当前状态所对应的拖拽事件。通过dragController发起的dragEvent仅支持获取result和behavior，且用于拖拽结束状态。 |
| extraParams | string | 否 | 是 | 设置拖拽事件额外信息，具体功能暂未实现。默认值为空。 |

#### DragStatus11+

拖拽开始和结束状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STARTED | 0 | 拖拽已成功发起。 |
| ENDED | 1 | 拖拽结束。 |

#### AnimationOptions11+

拖拽相关的动效参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 否 | 是 | 动画持续时间，单位为毫秒。 默认值：1000 说明： - 设置小于0的值时按0处理。 - 设置浮点型类型的值时，向下取整。例如，设置值为1.2，按照1处理。 |
| curve | [Curve](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__curve) | ICurve | 否 | 是 | 设置动画曲线。 默认值：Curve.EaseInOut |

#### [DragEvent](../../topics/components/拖拽事件.md#ZH-CN_TOPIC_0000002529444781__dragevent7)Param12+

拖拽结束返回结果的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| event10+ | [DragEvent](../../topics/components/拖拽事件.md#ZH-CN_TOPIC_0000002529444781__dragevent7) | 否 | 否 | 拖拽事件信息，仅包括拖拽结果。 |
| extraParams10+ | string | 否 | 否 | 拖拽事件额外信息。 |

#### dragController.getDragPreview(deprecated)

getDragPreview(): DragPreview

返回一个代表拖拽背板的对象。


-

从API version 11开始支持，从API version 18开始废弃，建议使用[getDragPreview](Class (DragController).md#ZH-CN_TOPIC_0000002522080726__getdragpreview11)替代。getDragPreview需先通过[UIContext](Class (UIContext).md)中的[getDragController](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getdragcontroller11)方法获取[DragController](Class (DragController).md)实例，然后通过该对象进行调用。

-

从API version 11开始，可以通过使用[UIContext](Class (UIContext).md)中的[getDragController](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getdragcontroller11)方法获取当前UI上下文关联的[DragController](Class (DragController).md)对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DragPreview | 一个代表拖拽背板的对象，提供背板样式设置的接口，在OnDrop和OnDragEnd回调中使用不生效。 |

**示例：**

请参考[animate](#ZH-CN_TOPIC_0000002522240718__animate11)

#### DragPreview11+

拖拽背板的对象，在OnDrop和OnDragEnd回调中使用不生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### setForegroundColor11+

setForegroundColor(color: [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)): void

设置背板蒙版颜色，在OnDrop和OnDragEnd回调中使用不生效，仅支持通过 [getDragPreview()](Class (DragController).md#ZH-CN_TOPIC_0000002522080726__getdragpreview11) 方法获取到的对象上使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 是 | 背板蒙版颜色。 |

**示例：**

请参考[animate](#ZH-CN_TOPIC_0000002522240718__animate11)

#### animate11+

animate(options: AnimationOptions, handler: () => void): void

设置背板蒙版颜色变化动效，在OnDrop和OnDragEnd回调中使用不生效，仅支持通过 [getDragPreview()](Class (DragController).md#ZH-CN_TOPIC_0000002522080726__getdragpreview11) 方法获取到的对象上使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | AnimationOptions | 是 | 动效参数。 |
| handler | () => void | 是 | 用于修改背板蒙版颜色等属性的回调方法。 |

**示例：**


推荐通过使用[UIContext](Class (UIContext).md)中的[getDragController](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getdragcontroller11)方法获取当前UI上下文关联的DragController对象。

1. 在EntryAbility.ets中获取UI上下文并保存至LocalStorage中。
```ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window, UIContext } from '@kit.ArkUI';

let uiContext: UIContext;
let localStorage: LocalStorage = new LocalStorage('uiContext');

export default class EntryAbility extends UIAbility {
  storage: LocalStorage = localStorage;

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', this.storage, (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s',
          `Code is ${err.code}, message is ${err.message}`);
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s',
        `Code is ${err.code}, message is ${err.message}`);
      windowStage.getMainWindow((err, data) => {
        if (err.code) {
          hilog.error(0x0000, `Failed to obtain the main window. Cause: ${err.message}`, '');
          return;
        }
        uiContext = data.getUIContext();
        this.storage.setOrCreate<UIContext>('uiContext', uiContext);
      })
    });
}
```

1. 在Index.ets中通过this.getUIContext().getSharedLocalStorage()获取UI上下文，进而获取DragController对象实施后续操作。
```ets
import { unifiedDataChannel } from '@kit.ArkData';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { dragController, curves, promptAction, UIContext } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

class DragInfo {
  event: DragEvent | undefined = undefined;
  extraParams: string = '';
}

@Entry()
@Component
struct DragControllerPage {
  @State pixmap: image.PixelMap|null = null;
  storages = this.getUIContext().getSharedLocalStorage();

  @Builder
  DraggingBuilder() {
    Column() {
      Text("DraggingBuilder")
        .fontColor(Color.White)
        .fontSize(12)
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  @Builder
  PixmapBuilder() {
    Column() {
      Text("PixmapBuilder")
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  build() {
    Column() {
      Button('拖拽至此处')
        .margin(10)
        .onDragEnter(() => {
        try {
          let uiContext: UIContext = this.storages?.get<UIContext>('uiContext') as UIContext;
          let previewObj: dragController.DragPreview = uiContext.getDragController().getDragPreview();
          let foregroundColor: ResourceColor = Color.Green;

          let previewAnimation: dragController.AnimationOptions = {
            curve: curves.cubicBezierCurve(0.2,0,0,1),
          }
          previewObj.animate(previewAnimation, () => {
            previewObj.setForegroundColor(foregroundColor);
          });
        } catch (error) {
          let msg = (error as BusinessError).message;
          let code = (error as BusinessError).code;
          hilog.error(0x0000, `show error code is ${code}, message is ${msg}`, '');
        }
      })
        .onDrop(() => {
          this.getUIContext().getPromptAction().showToast({duration: 100, message: 'Drag Success', bottom: 400})
        })
      Button('拖起').onTouch((event?:TouchEvent) => {
        if(event){
          if (event.type == TouchType.Down) {
            let text = new unifiedDataChannel.Text()
            let unifiedData = new unifiedDataChannel.UnifiedData(text)
            let dragInfo: dragController.DragInfo = {
              pointerId: 0,
              data: unifiedData,
              extraParams: ''
            }
            let eve: DragInfo = new DragInfo();
            this.getUIContext()
              .getDragController()
              .executeDrag(() => { // 建议使用 this.getUIContext().getDragController().executeDrag()接口
              this.DraggingBuilder()
            }, dragInfo, (err , eve) => {
              hilog.info(0x0000, `${JSON.stringify(err)}`, '')
              if (eve && eve.event) {
                if (eve.event.getResult() == DragResult.DRAG_SUCCESSFUL) {
                  hilog.info(0x0000, 'success', '');
                } else if (eve.event.getResult() == DragResult.DRAG_FAILED) {
                  hilog.info(0x0000, 'failed', '');
                }
            })
        }
      }).margin({top:100})
    }
    .width('100%')
    .height('100%')
  }
```

#### DragStartRequestStatus18+

定义应用是否可以发起拖拽的枚举类型。仅在[onDragStart](拖拽事件.md#ZH-CN_TOPIC_0000002553200729__ondragstart)调用时有效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WAITING | 0 | 应用在准备数据阶段，无法发起拖拽。 |
| READY | 1 | 应用数据准备完成，可以发起拖拽。 |

#### DragSpringLoadingState20+

定义拖拽的悬停检测状态的枚举类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BEGIN | - | 拖拽进入组件范围静止一段时间，被识别为悬停状态。此时允许进行一些悬停检测的准备操作。 |
| UPDATE | - | 拖拽已处于悬停状态，如果继续静止会定期触发UPDATE通知，以检查悬停状态。此时允许UI效果刷新以突出悬停状态。 |
| END | - | 如果最后一次UPDATE通知后拖拽继续静止会进入END，整个悬停检测结束。进入END后拖拽需要移出组件范围后再次进入组件或移入组件内子组件才会重新开始悬停检测。此时应用程序可进行清理、导航或视图切换操作。 |
| CANCEL | - | 拖拽进入BEGIN后，在手指/鼠标抬起、切换窗口、息屏、移出组件范围、移入组件内子组件或组件内移动超过检测阈值等场景会触发CANCEL通知，悬停检测中断。应用程序将恢复UI样式，并取消待定的导航及视图切换操作。 |

#### DragSpringLoadingConfiguration20+

定义拖拽的悬停检测配置参数的接口。默认的配置参数通常已能满足需求。可以通过在绑定[onDragSpringLoading](拖拽事件.md#ZH-CN_TOPIC_0000002553200729__ondragspringloading20)时指定配置，或者通过在BEGIN状态期间使用[updateConfiguration](#ZH-CN_TOPIC_0000002522240718__updateconfiguration20)方法动态修改的方式以自定义该配置参数。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| stillTimeLimit | number | 否 | 是 | 进入悬停检测BEGIN状态所需保持静止的时间（ms）。取值范围为[0, 231-1]的整数。输入浮点数时只取整数部分。输入非法值（负数、null、undefined、NaN）时取默认值500。 |
| updateInterval | number | 否 | 是 | 进入悬停检测UPDATE状态后，更新通知的时间间隔（ms）。取值范围为[0, 231-1]的整数。输入浮点数时只取整数部分。输入非法值（负数、null、undefined、NaN）时取默认值100。 |
| updateNotifyCount | number | 否 | 是 | 进入悬停检测UPDATE状态后，更新通知的最大次数。取值范围为[0, 231-1]的整数。输入浮点数时只取整数部分。输入非法值（负数、null、undefined、NaN）时取默认值3。 |
| updateToFinishInterval | number | 否 | 是 | 从UPDATE状态到END状态的最长等待时间（ms）。取值范围为[0, 231-1]的整数。输入浮点数时只取整数部分。输入非法值（负数、null、undefined、NaN）时取默认值100。 |

#### SpringLoadingDragInfos20+

定义触发悬停检测时拖拽事件信息的接口。该接口提供了拖拽数据摘要和拖拽事件额外信息，应用程序可以据此决定是否响应悬停检测回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dataSummary | unifiedDataChannel.Summary | 否 | 是 | 拖拽数据的摘要，默认为null。 |
| extraInfos | string | 否 | 是 | 拖拽事件额外信息，默认为空字符串。 |

#### SpringLoadingContext20+

定义回调上下文信息的类，用于在悬停检测回调中传递给应用程序，使其能访问拖拽状态、动态刷新UI效果以及访问拖拽数据以确定是否处理拖拽操作。

#### 属性

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | DragSpringLoadingState | 否 | 否 | 当前悬停检测的状态。 |
| currentNotifySequence | number | 否 | 否 | 在一次悬停检测流转中的回调通知次数，从0开始。 |
| dragInfos | SpringLoadingDragInfos | 否 | 是 | 拖拽信息，当悬停检测状态为CANCEL时缺失，为undefined时取SpringLoadingDragInfos默认值。 |
| currentConfig | DragSpringLoadingConfiguration | 否 | 是 | 当前回调中的配置信息，当悬停检测状态为CANCEL时缺失，为undefined时取DragSpringLoadingConfiguration默认值。 |

#### abort20+

abort(): void

终止后续的悬停检测。本方法不会触发CANCEL状态通知，应用程序需要在执行本方法时进行状态清理。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### updateConfiguration20+

updateConfiguration(config: DragSpringLoadingConfiguration): void

更新悬停检测的配置，仅在悬停检测状态为BEGIN时生效。应用程序通常在绑定[onDragSpringLoading](拖拽事件.md#ZH-CN_TOPIC_0000002553200729__ondragspringloading20)时设置悬停检测配置或使用默认配置。该方法不会修改绑定时的原始配置，而是在后续悬停检测中更新动态的配置信息。请谨慎使用本方法，因为不同的拖拽数据类型可能需要不同的UX时间。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | DragSpringLoadingConfiguration | 是 | 悬停检测配置。 |