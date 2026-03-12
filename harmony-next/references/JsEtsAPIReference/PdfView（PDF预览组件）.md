# PdfView（PDF预览组件）

本模块提供PdfView组件，HarmonyOS应用通过集成该组件完成PDF文件的预览功能。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit';
```

#### PdfView

该类为用来展示PDF文档预览的UI组件。

**装饰器类型：**@Component

**系统能力：**SystemCapability.OfficeService.PDFService.Core

**起始版本：**5.0.0(12)

参数名

类型

只读

可选

说明

controller

pdfViewManager.[PdfController](pdfViewManager（PDF预览）.md#section15202162183817)

否

否

PdfView组件控制器。

pageLayout

pdfService.[PageLayout](pdfService（PDF服务）.md#section1749384210523)

否

否

页面布局显示模式。

isContinuous

boolean

否

否

是否连续预览，true：是，false：否。

showScroll

boolean

否

否

是否显示滚动条，true：显示，false：隐藏。

pageFit

pdfService.[PageFit](pdfService（PDF服务）.md#section655755325212)

否

否

页面适配模式。

#### build

build(): void

用于创建[PdfView](#section724521414201)对象的构造函数。

**系统能力：**SystemCapability.OfficeService.PDFService.Core

**起始版本：**5.0.0(12)

**示例：**

```ets
import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit'
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();

  aboutToAppear(): void {
    let context = this.getUIContext().getHostContext() as Context;
    let dir: string = context.filesDir
    // 确保在工程目录src/main/resources/rawfile里存在input.pdf文档
    let filePath: string = dir + '/input.pdf';
    let res = fileIo.accessSync(filePath);
    if (!res) {
      let content: Uint8Array = context.resourceManager.getRawFileContentSync('rawfile/input.pdf');
      let fdSand =
        fileIo.openSync(filePath, fileIo.OpenMode.WRITE_ONLY | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
      fileIo.writeSync(fdSand.fd, content.buffer);
      fileIo.closeSync(fdSand.fd);
    }
    (async () => {
      // 该监听方法只能在文档加载前调用一次
      this.controller.registerPageCountChangedListener((pageCount: number) => {
        hilog.info(0x0000, 'registerPageCountChanged-', pageCount.toString());
      });
      let loadResult1: pdfService.ParseResult = await this.controller.loadDocument(filePath);
      // 注意：这里刚加载文档，请不要在这里立即设置PDF文档的预览方式
    })()
  }

  build() {
    Row() {
      PdfView({
        controller: this.controller,
        pageFit: pdfService.PageFit.FIT_WIDTH,
        showScroll: true
      })
        .id('pdfview_app_view')
        .layoutWeight(1);
    }
    .width('100%')
    .height('100%')
  }
}
```