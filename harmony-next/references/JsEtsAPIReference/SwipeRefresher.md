# SwipeRefresher

内容加载指获取内容并加载出来，常用于衔接展示下拉加载的内容。

该组件及其子组件从 API version 10 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 导入模块

```ets
import { SwipeRefresher } from '@kit.ArkUI';
```

#### 子组件

无

#### 属性

不支持[通用属性](通用属性.md)。

#### SwipeRefresher

SwipeRefresher ({content?: ResourceStr, isLoading: boolean})

**装饰器类型：**@Component

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

名称类型必填装饰器类型说明content[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否@Prop

内容加载时显示的文本。

默认值：空字符串。

**说明**：如果文本大于列宽时，文本被截断。从API version 20开始，支持Resource类型。

isLoadingboolean是@Prop

当前是否正在加载。

 isLoading为true时，表示正在加载。

 isLoading为false时，表示未在加载。

#### 事件

不支持[通用事件](通用事件.md)。

#### 示例

展示设置属性content为空字符串及不为空、isLoading为true和false的不同加载效果。

```ets
import { SwipeRefresher } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column() {
      SwipeRefresher({
        content: '正在加载中',
        isLoading: true
      })
      SwipeRefresher({
        content: '',
        isLoading: true
      })
      SwipeRefresher({
        content: '正在加载中',
        isLoading: false
      })
    }
  }
}
```