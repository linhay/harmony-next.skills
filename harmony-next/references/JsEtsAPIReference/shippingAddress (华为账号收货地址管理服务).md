# shippingAddress (华为账号收货地址管理服务)

本模块提供Account Kit的收货地址管理能力。应用可通过该能力获取到用户华为账号收货地址信息，包括详细地址、手机号等。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { shippingAddress } from '@kit.AccountKit';
```

#### ShippingAddressErrorCode

该枚举定义了Account Kit收货地址管理服务错误码。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.ShippingAddress

**起始版本：**5.0.0(12)

**名称**

**值**

**说明**

INTERNAL_ERROR

[1008100001](ArkTS错误码.md#section2160112171514)

内部错误。

NETWORK_ERROR

[1008100002](ArkTS错误码.md#section315852115157)

网络不可用。

ACCOUNT_NOT_LOGGED_IN

[1008100003](ArkTS错误码.md#section15158192191517)

用户未登录华为账号。

PACKAGE_FINGERPRINT_CHECK_ERROR

[1008100004](ArkTS错误码.md#section1415952110158)

应用指纹证书校验失败。

PERMISSION_CHECK_ERROR

[1008100005](ArkTS错误码.md#section515972151510)

应用未申请对应permissions权限。

USER_CANCELED

[1008100006](ArkTS错误码.md#section191591621191512)

用户未完成操作就退出了收货地址管理服务。

UNSUPPORTED

[1008100007](ArkTS错误码.md#section91601621141512)

已登录的华为账号不支持收货地址管理服务。

#### AddressInfo

该类为收货地址管理服务响应的收货地址数据对象。应用可根据实际场景获取相关收货地址信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.ShippingAddress

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

userName

string

是

否

用户名。长度限制2-20。

mobileNumber

string

是

否

手机号码。长度限制2-20。

 说明：

当前仅支持输入中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）手机号。收货地址的明文手机号支持183******58、+86183******58、0086183******58共3种格式。接口返回的手机号格式和用户输入的手机号格式保持一致。

telNumber

string

是

是

座机号码。长度限制1-256。用户未设置默认不返回。

zipCode

string

是

是

邮政编码。长度限制1-256。用户未设置默认不返回。

countryCode

string

是

否

国家码。长度限制1-256。

provinceName

string

是

否

省份名称。长度限制1-50。

cityName

string

是

否

城市名称。长度限制1-50。

districtName

string

是

否

地区名称。长度限制1-50。

 说明：

仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

streetName

string

是

否

街道名称。长度限制1-50。

detailedAddress

string

是

否

详细地址。长度限制1-50。

#### chooseAddress

chooseAddress(context: common.Context): Promise<AddressInfo>

调用该方法打开收货地址管理页面，使用Promise异步回调用户选择的收货地址。用于应用向Account Kit获取用户绑定的华为账号收货地址。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.ShippingAddress

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

应用可支持的Context有：[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)、[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)调用。

元服务可支持的Context有：[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)。

**返回值：**

类型

说明

Promise<[AddressInfo](#section9615740103819)>

Promise对象，返回[AddressInfo](#section9615740103819)对象可以获取收货地址的详细信息。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

[1008100001](ArkTS错误码.md#section2160112171514)

Internal error.

[1008100002](ArkTS错误码.md#section315852115157)

The network is unavailable.

[1008100003](ArkTS错误码.md#section15158192191517)

The user has not signed in with HUAWEI ID.

[1008100004](ArkTS错误码.md#section1415952110158)

Failed to check the fingerprint of the app bundle.

[1008100005](ArkTS错误码.md#section515972151510)

The app does not have the required permissions.

[1008100006](ArkTS错误码.md#section191591621191512)

The user quits the shipping address management service without finishing.

[1008100007](ArkTS错误码.md#section91601621141512)

The shipping address management service does not support the HUAWEI ID that is already signed in.

**示例：**

```ets
import { shippingAddress } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 执行请求
try {
  // 此示例为代码片段，实际需在自定义组件实例中使用，以获取UIContext对象作为函数入参
  shippingAddress.chooseAddress(this.getUIContext().getHostContext()).then((data: shippingAddress.AddressInfo) => {
    hilog.info(0x0000, 'testTag', 'Succeeded in choosing address');
    const userName: string = data.userName;
    const mobileNumber: string = data.mobileNumber;
    const countryCode: string = data.countryCode;
    const provinceName: string = data.provinceName;
    const cityName: string = data.cityName;
    const districtName: string = data.districtName;
    const streetName: string = data.streetName;
    const detailedAddress: string = data.detailedAddress;
    // 开发者处理获取的收货地址信息
  }).catch((error: BusinessError) => {
    dealAllError(error);
  })
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', `Failed to chooseAddress. Code: ${error.code}, message: ${error.message}`);
}
```