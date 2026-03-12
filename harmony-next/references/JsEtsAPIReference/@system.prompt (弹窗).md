# @system.prompt (弹窗)

创建并显示文本提示框、对话框和操作菜单。

-

从API Version 8 开始，该接口不再维护，推荐使用新接口[@ohos.promptAction (弹窗)](@ohos.promptAction (弹窗).md)。

-

本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import prompt from '@system.prompt';
```

#### prompt.showToast

showToast(options: ShowToastOptions): void

显示文本弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[ShowToastOptions](#ZH-CN_TOPIC_0000002497444830__showtoastoptions)是定义ShowToast的选项。

**示例：**

```ets
import prompt from '@system.prompt';
class A{
  showToast() {
    prompt.showToast({
      message: 'Message Info',
      duration: 2000
    });
  }
}
export default new A()
```

#### prompt.showDialog

showDialog(options: ShowDialogOptions): void

显示对话框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[ShowDialogOptions](#ZH-CN_TOPIC_0000002497444830__showdialogoptions)是定义显示对话框的选项。

**示例：**

```ets
import prompt from '@system.prompt';
class B{
  showDialog() {
    prompt.showDialog({
      title: 'Title Info',
      message: 'Message Info',
      buttons: [
        {
          text: 'button',
          color: '#666666'
        },
      ],
      success: (data)=> {
        console.log('dialog success callback，click button : ' + data.index);
      },
      cancel: ()=> {
        console.log('dialog cancel callback');
      },
    });
  }
}
export default new B()
```

#### prompt.showActionMenu6+

showActionMenu(options: ShowActionMenuOptions): void

显示操作菜单。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[ShowActionMenuOptions](#ZH-CN_TOPIC_0000002497444830__showactionmenuoptions6)是定义ShowActionMenu的选项。

**示例：**

```ets
import prompt from '@system.prompt';
class C{
  showActionMenu() {
    prompt.showActionMenu({
      title: 'Title Info',
      buttons: [
        {
          text: 'item1',
          color: '#666666'
        },
        {
          text: 'item2',
          color: '#000000'
        },
      ],
      success: (tapIndex)=> {
        console.log('dialog success callback，click button : ' + tapIndex);
      },
      fail: (errMsg)=> {
        console.log('dialog fail callback' + errMsg);
      },
    });
  }
}
export default new C()
```

#### ShowToastOptions

定义ShowToast的选项。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

名称类型必填说明messagestring是显示的文本信息。durationnumber否默认值1500ms，建议区间：1500ms-10000ms。若小于1500ms则取默认值，最大取值为10000ms。bottom5+string|number否设置弹窗边框距离屏幕底部的位置。

#### Button

定义按钮的提示信息。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

名称类型必填说明textstring是定义按钮信息。colorstring是定义按钮颜色。

#### ShowDialogSuccessResponse

定义ShowDialog的响应。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

名称类型必填说明indexnumber是定义数据的索引信息。

#### ShowDialogOptions

定义显示对话框的选项。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

名称类型必填说明titlestring否标题文本。messagestring否文本内容。buttons[[Button](#ZH-CN_TOPIC_0000002497444830__button), [Button](#ZH-CN_TOPIC_0000002497444830__button)?, [Button](#ZH-CN_TOPIC_0000002497444830__button)?]否对话框中按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-6个按钮。大于6个按钮时弹窗不显示。success(data: [ShowDialogSuccessResponse](#ZH-CN_TOPIC_0000002497444830__showdialogsuccessresponse)) => void否接口调用成功的回调函数。cancel(data: string, code: string) => void否接口调用失败的回调函数。complete(data: string) => void否接口调用结束的回调函数。

#### ShowActionMenuOptions6+

定义ShowActionMenu的选项。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

名称类型必填说明titlestring否标题文本。buttons[[Button](#ZH-CN_TOPIC_0000002497444830__button), [Button](#ZH-CN_TOPIC_0000002497444830__button)?, [Button](#ZH-CN_TOPIC_0000002497444830__button)?, [Button](#ZH-CN_TOPIC_0000002497444830__button)?, [Button](#ZH-CN_TOPIC_0000002497444830__button)?, [Button](#ZH-CN_TOPIC_0000002497444830__button)?]是对话框中按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-6个按钮。success(tapIndex: number, errMsg: string) => void否弹出对话框时调用。fail(errMsg: string) => void否接口调用失败的回调函数。complete(data: string) => void否关闭对话框时调用。