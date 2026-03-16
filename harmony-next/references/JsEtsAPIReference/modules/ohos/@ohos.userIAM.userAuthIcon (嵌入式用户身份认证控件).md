# @ohos.userIAM.userAuthIcon (嵌入式用户身份认证控件)

提供应用界面上展示的人脸、指纹认证图标，具体功能如下：

1.

提供嵌入式的人脸、指纹认证控件图标，可被应用集成。

1.

支持自定义图标的颜色和大小，但图标样式不可变更。

1.

点击控件图标后将以系统弹窗的方式，拉起人脸、指纹认证控件。

- 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { userAuth, UserAuthIcon } from '@kit.UserAuthenticationKit';
```

#### 子组件

无

#### 属性

不支持通用属性。

#### UserAuthIcon

UserAuthIcon({

 authParam: userAuth.AuthParam,

 widgetParam: userAuth.WidgetParam,

 iconHeight?: Dimension,

 iconColor?: ResourceColor,

 onIconClick?: ()=>void,

 onAuthResult: (result: userAuth.UserAuthResult)=>void

})

**装饰器类型：**@Component

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

名称类型必填说明authParam[userAuth.AuthParam](@ohos.userIAM.userAuth (用户认证).md#ZH-CN_TOPIC_0000002529445377__authparam10)是用户认证相关参数。widgetParam[userAuth.WidgetParam](@ohos.userIAM.userAuth (用户认证).md#ZH-CN_TOPIC_0000002529445377__widgetparam10)是用户认证界面配置相关参数。iconHeight[Dimension](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)否设置icon的高度，宽高比1:1，默认64。iconColor[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否设置icon的颜色，默认值：$r('sys.color.ohos_id_color_activated')。onIconClick()=>void否用户点击icon回调接口。onAuthResult(result: [userAuth.UserAuthResult](@ohos.userIAM.userAuth (用户认证).md#ZH-CN_TOPIC_0000002529445377__userauthresult10))=>void是

用户认证结果信息回调接口。

应用需要申请ohos.permission.ACCESS_BIOMETRIC权限，否则应用将仅展示图标，无法正常拉起身份认证控件。

#### 事件

不支持通用事件。

#### 示例

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth, UserAuthIcon } from '@kit.UserAuthenticationKit';

@Entry
@Component
struct Index {
  rand = cryptoFramework.createRandom();
  len: number = 16;
  randData: Uint8Array = this.rand?.generateRandomSync(this.len)?.data;
  authParam: userAuth.AuthParam = {
    challenge: this.randData,
    authType: [userAuth.UserAuthType.FACE, userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3
  };
  widgetParam: userAuth.WidgetParam = {
    title: '请进行身份认证'
  };

  build() {
    Row() {
      Column() {
        UserAuthIcon({
          authParam: this.authParam,
          widgetParam: this.widgetParam,
          iconHeight: 200,
          iconColor: Color.Blue,
          onIconClick: () => {
            console.info('The user clicked the icon.');
          },
          onAuthResult: (result: userAuth.UserAuthResult) => {
            console.info(`Get user auth result, result = ${JSON.stringify(result)}`);
          }
        })
      }
    }
  }
}
```

调用onAuthResult可能会抛出错误码，错误码详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[用户认证错误码](../../errors/用户认证错误码.md)。

**人脸认证图例：**

**指纹认证图例：**