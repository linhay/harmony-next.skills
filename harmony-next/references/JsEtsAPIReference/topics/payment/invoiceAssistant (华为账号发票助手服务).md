# invoiceAssistant (华为账号发票助手服务)

本模块提供Account Kit的发票助手能力。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { invoiceAssistant } from '@kit.AccountKit';
```

#### InvoiceAssistantErrorCode

该枚举定义了Account Kit发票助手服务相关接口的错误码。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.HuaweiID.InvoiceAssistant

**起始版本：**5.0.0(12)

**名称**

**值**

**说明**

USER_CANCELED

[1010060001](../../errors/ArkTS错误码.md#section165992015527)

用户取消发票助手服务。

SYSTEM_ERROR

[1010060002](../../errors/ArkTS错误码.md#section730115513413)

系统内部错误。

APP_NOT_AUTHORIZED

[1010060003](../../errors/ArkTS错误码.md#section717135217914)

应用指纹证书校验失败。

FREQUENT_CALLS

[1010060004](../../errors/ArkTS错误码.md#section12371175713102)

接口访问过频。

NETWORK_ERROR

[1010060005](../../errors/ArkTS错误码.md#section17507143210121)

网络连接错误。

ACCOUNT_NOT_LOGGED_IN

[1010060006](../../errors/ArkTS错误码.md#section569215704317)

用户未登录华为账号。

INVOICE_TITLE_EXISTS

[1010060007](../../errors/ArkTS错误码.md#section670931214512)

发票抬头信息已存在。

UNSUPPORTED

[1010060008](../../errors/ArkTS错误码.md#section16845834174215)

已登录的华为账号不支持发票助手服务。

#### InvoiceTitle

该类为发票助手服务响应的发票抬头数据对象。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.HuaweiID.InvoiceAssistant

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

type

string

否

否

抬头类型，0-个人 1-企业。

title

string

否

否

抬头名称。

taxNumber

string

否

否

纳税人识别号。如果抬头类型为企业，则根据真实值返回；如果抬头类型为个人，则返回空字符串。

companyAddress

string

否

否

公司地址。如果抬头类型为企业，则根据真实值返回；如果抬头类型为个人，则返回空字符串。

telephone

string

否

否

公司电话。如果抬头类型为企业，则根据真实值返回；如果抬头类型为个人，则返回空字符串。

bankName

string

否

否

公司银行名称。如果抬头类型为企业，则根据真实值返回；如果抬头类型为个人，则返回空字符串。

bankAccount

string

否

否

公司银行账户。如果抬头类型为企业，则根据真实值返回；如果抬头类型为个人，则返回空字符串。

#### selectInvoiceTitle

selectInvoiceTitle(context: common.Context): Promise<InvoiceTitle>

调用该方法打开发票抬头选择页面，并返回用户选择的发票抬头。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.HuaweiID.InvoiceAssistant

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-common#context)

是

Context上下文。

应用可支持的Context有：[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)和[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)调用。

元服务可支持的Context有：[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)。

**返回值：**

类型

说明

Promise<[InvoiceTitle](#section9615740103819)>

Promise对象，返回[InvoiceTitle](#section9615740103819)对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](../../errors/ArkTS错误码.md)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

[1010060001](../../errors/ArkTS错误码.md#section165992015527)

The operation was canceled by the user.

[1010060002](../../errors/ArkTS错误码.md#section730115513413)

System internal error.

[1010060003](../../errors/ArkTS错误码.md#section717135217914)

Failed to check the fingerprint of the app bundle.

[1010060004](../../errors/ArkTS错误码.md#section12371175713102)

Too frequent API calls.

[1010060005](../../errors/ArkTS错误码.md#section17507143210121)

Network connection error.

[1010060006](../../errors/ArkTS错误码.md#section569215704317)

The HUAWEI ID is not signed in.

[1010060007](../../errors/ArkTS错误码.md#section670931214512)

Failed to create a invoice title because the title already exists.

[1010060008](../../errors/ArkTS错误码.md#section16845834174215)

The invoice service does not support the logged HUAWEI ID.

**示例：**

```ets
import { invoiceAssistant } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 执行请求
if (canIUse('SystemCapability.HuaweiID.InvoiceAssistant')) {
  try {
    // 此示例为代码片段，实际需在自定义组件实例中使用，以获取UIContext对象作为函数入参
    invoiceAssistant.selectInvoiceTitle(this.getUIContext().getHostContext())
      .then((data: invoiceAssistant.InvoiceTitle) => {
        hilog.info(0x0000, 'testTag', 'Succeeded in selecting invoice title');
        const type: string = data.type;
        const title: string = data.title;
        const taxNumber: string = data.taxNumber;
        const companyAddress: string = data.companyAddress;
        const telephone: string = data.telephone;
        const bankName: string = data.bankName;
        const bankAccount: string = data.bankAccount;

        // 开发者处理type, title, taxNumber, companyAddress, telephone, bankName, bankAccount
        // ...

      })
      .catch((error: BusinessError<Object>) => {
        dealAllError(error);
      })
  } catch (error) {
    dealAllError(error);
  }
} else {
  hilog.info(0x0000, 'testTag',
    'The current device does not support the invoking of the selectInvoiceTitle interface.');
}

// 错误处理
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to authorize. Code: ${error.code}, message: ${error.message}`);
}
```