# LoginPanel (华为账号Panel登录组件)

本模块提供LoginPanel组件，应用通过集成该组件完成华为账号登录功能。

LoginPanel需要配合[loginComponentManager](loginComponentManager (华为账号登录组件管理).md)一起使用，用于实现华为账号登录功能。LoginPanel内的按钮文本默认支持多语言。

**起始版本：**4.1.0(11)

#### 导入模块

```ets
import { LoginPanel, loginComponentManager } from '@kit.AccountKit';
```

#### LoginPanel

该类为用来展示登录面板的UI组件。

**模型约束：**此接口仅可在Stage模型下使用。

**装饰器类型：**@Component

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| show | boolean | 是 | @Link | 该参数用于控制LoginPanel组件是否展示。 false表示不展示该组件。 true表示展示该组件，当业务需要使用LoginPanel组件时设置值为true。 说明： - 该参数必须是@State装饰的局部变量。 - LoginPanel仅支持在页面中使用，弹框、子窗口等场景暂不支持。 |
| params | LoginPanelParams | 是 | - | LoginPanel组件参数。 |
| controller | LoginPanelController | 是 | - | LoginPanel组件控制器用来接收组件的点击事件。 |

#### build

build(): void

用于创建[LoginPanel](#ZH-CN_TOPIC_0000002522242284__loginpanel)对象的构造函数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**4.1.0(11)

**示例：**

```ets
import { LoginPanel, loginComponentManager } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct PreviewLoginPanelPage {
  // 是否展示LoginPanel组件
  @State show: boolean = true;
  // 定义LoginPanel展示的隐私文本，展示用户服务协议、隐私协议和华为账号用户认证协议
  privacyText: loginComponentManager.PrivacyText[] = [{
    text: '已阅读并同意',
    type: loginComponentManager.TextType.PLAIN_TEXT
  }, {
    text: '《用户服务协议》',
    tag: '用户服务协议',
    type: loginComponentManager.TextType.RICH_TEXT
  }, {
    text: '《隐私协议》',
    tag: '隐私协议',
    type: loginComponentManager.TextType.RICH_TEXT
  }, {
    text: '和',
    type: loginComponentManager.TextType.PLAIN_TEXT
  }, {
    text: '《华为账号用户认证协议》',
    tag: '华为账号用户认证协议',
    type: loginComponentManager.TextType.RICH_TEXT
  }];
  // 定义LoginPanel展示的其他方式登录Icon
  iconArray: loginComponentManager.LoginIcon[] = [{
    // 此处为示例资源，开发者可使用应用图标进行替换，以保证正常编译运行
    icon: $r('app.media.app_icon'),
    tag: '其他方式登录'
  }];
  // 构造LoginPanel组件的控制器
  controller: loginComponentManager.LoginPanelController = new loginComponentManager.LoginPanelController()
    // 当登录类型不是QUICK_LOGIN且未设置协议时，如果需要展示自定义协议弹框，需要设置协议状态为NOT_ACCEPTED
    .setAgreementStatus(loginComponentManager.AgreementStatus.NOT_ACCEPTED)
    // 用户点击其他方式登录展示隐私协议弹框
    .setShowAgreementForOptionalLogin()
    .onClickLoginWithHuaweiIDButton((error: BusinessError, response: loginComponentManager.HuaweiIDCredential) => {
      hilog.info(0x0000, 'testTag', 'onClickLoginWithHuaweiIDButton');
      if (error) {
        this.dealAllError(error);
        return;
      }
      if (response) {
        // 获取到Authorization Code后，传给应用服务端
        const authorizationCode = response.authorizationCode;
        hilog.info(0x0000, 'testTag', 'Succeeded in getting response.');
        this.show = false;
        return;
      }
    })
    .onClickOptionalLoginButton(() => {
      hilog.info(0x0000, 'testTag', 'onClickOptionalLoginButton');
      this.show = false;
    })
    .onClickOptionalLoginIcon((error: BusinessError, tag: string) => {
      if (error) {
        this.dealAllError(error);
        return;
      }
      hilog.info(0x0000, 'testTag', `onClickOptionalLoginIcon tag: ${tag}`);
      this.show = false;
    })
    .onClickPrivacyText((error: BusinessError, tag: string) => {
      if (error) {
        this.dealAllError(error);
        return;
      }
      // 应用需要根据tag实现协议页面的跳转逻辑
      hilog.info(0x0000, 'testTag', `onClickPrivacyText tag: ${tag}`);
    })
    .onClickCloseButton(() => {
      hilog.info(0x0000, 'testTag', 'onClickCloseButton');
      this.show = false;
    })
    .onChangeAgreementStatus((error: BusinessError, agreementStatus: loginComponentManager.AgreementStatus) => {
      if (error) {
        this.dealAllError(error);
        return;
      }
      hilog.info(0x0000, 'testTag', `onChangeAgreementStatus agreementStatus: ${agreementStatus}`);
    })
    .onClickEvent((error: BusinessError, clickEvent: loginComponentManager.ClickEvent) => {
      if (error) {
        this.dealAllError(error);
        return;
      }
      hilog.info(0x0000, 'testTag', `onClickEvent clickEvent: ${clickEvent}`);
    });

  // 错误处理
  dealAllError(error: BusinessError): void {
    hilog.error(0x0000, 'testTag', `Failed to login, errorCode=${error.code}, errorMsg=${error.message}`);
    // 在应用登录涉及UI交互场景下，建议按照如下错误码指导提示用户
    if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
      // 用户未登录华为账号，请登录华为账号并重试或者尝试使用其他方式登录
    } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
      // 网络异常，请检查当前网络状态并重试或者尝试使用其他方式登录
    } else if (error.code === ErrorCode.ERROR_CODE_INTERNAL_ERROR) {
      // 登录失败，请尝试使用其他方式登录
    } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
      // 用户取消授权
    } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
      // 系统服务异常，请稍后重试或者尝试使用其他方式登录
    } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
      // 重复请求，应用无需处理
    } else if (error.code === ErrorCode.ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED) {
      // 用户未同意协议
    } else {
      // 应用登录失败，请尝试使用其他方式登录
    }

  build() {
    if (this.show) {
      Stack() {
        LoginPanel({
          show: this.show,
          params: {
            appInfo: {
              // 此处为示例资源，开发者可使用应用图标进行替换，以保证正常编译运行
              appIcon: $r('app.media.app_icon'),
              appName: '应用名称',
            },
            privacyText: this.privacyText,
            // 参考华为账号开发指南获取匿名手机号
            anonymousPhoneNumber: '139******99',
            loginType: loginComponentManager.LoginType.QUICK_LOGIN,
            // optionalLoginAreaAttr和optionalLoginButtonAttr同时存在时优先展示optionalLoginAreaAttr
            optionalLoginAreaAttr: { iconArray: this.iconArray },
            optionalLoginButtonAttr: { text: '其他方式登录' }
          },
          controller: this.controller
        })
      }
      .height('100%')
      .width('100%')
    }

export enum ErrorCode {
  // 账号未登录
  ERROR_CODE_LOGIN_OUT = 1001502001,
  // 网络错误
  ERROR_CODE_NETWORK_ERROR = 1001502005,
  // 内部错误
  ERROR_CODE_INTERNAL_ERROR = 1001502009,
  // 用户取消授权
  ERROR_CODE_USER_CANCEL = 1001502012,
  // 系统服务异常
  ERROR_CODE_SYSTEM_SERVICE = 12300001,
  // 用户未同意用户协议
  ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED = 1005300001,
  // 重复请求
  ERROR_CODE_REQUEST_REFUSE = 1001500002
}
```