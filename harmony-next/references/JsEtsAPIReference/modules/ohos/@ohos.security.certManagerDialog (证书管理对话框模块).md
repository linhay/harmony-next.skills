# @ohos.security.certManagerDialog (证书管理对话框模块)

证书管理对话框主要提供拉起证书管理界面的能力，用户在拉起的证书管理对话框可对证书进行管理（安装，存储，使用，销毁）。

本模块首批接口从API version 13开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
```

#### CertificateDialogPageType

表示证书管理对话框的页面类型。

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PAGE_MAIN | 1 | 证书管理应用主页面。 |
| PAGE_CA_CERTIFICATE | 2 | CA证书列表页面。 |
| PAGE_CREDENTIAL | 3 | 凭据列表页面。 |
| PAGE_INSTALL_CERTIFICATE | 4 | 安装证书页面。 |

#### CertificateType14+

表示安装证书的类型。

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CA_CERT | 1 | CA证书。 |
| CREDENTIAL_USER22+ | 2 | 用户公共凭据。 |
| CREDENTIAL_APP22+ | 3 | 应用私有凭据。 |
| CREDENTIAL_UKEY22+ | 4 | USB凭据。 |
| CREDENTIAL_SYSTEM23+ | 5 | 系统凭据。 |

#### CertificateScope14+

表示安装证书的使用范围。

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOT_SPECIFIED18+ | 0 | 未指定用户。 |
| CURRENT_USER | 1 | 当前用户。 |
| GLOBAL_USER18+ | 2 | 公共目录。 |

#### CertificateDialogErrorCode

表示调用证书管理对话框相关API的错误码。

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ERROR_GENERIC | 29700001 | 表示调用接口时发生内部错误。 |
| ERROR_OPERATION_CANCELED14+ | 29700002 | 表示调用接口时用户取消操作。 |
| ERROR_OPERATION_FAILED14+ | 29700003 | 表示调用接口时安装证书失败。 |
| ERROR_DEVICE_NOT_SUPPORTED14+ | 29700004 | 表示调用接口时设备类型不支持。 |
| ERROR_NOT_COMPLY_SECURITY_POLICY18+ | 29700005 | 表示调用接口时不符合设备安全策略。 |
| ERROR_PARAMETER_VALIDATION_FAILED22+ | 29700006 | 表示调用接口时参数校验失败。 例如：参数格式不正确、参数范围无效 |
ERROR_NO_AVAILABLE_CERTIFICATE22+29700007表示没有可用证书。

#### CertificateDialogProperty18+

表示证书管理对话框的属性。

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| showInstallButton | boolean | 否 | 否 | 表示是否显示安装证书的按钮，true为显示，false为不显示。 |

#### CertReference22+

表示证书凭据的引用信息。

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| certType | CertificateType | 否 | 否 | 表示证书类型。 |
| keyUri | string | 否 | 否 | 表示证书凭据的唯一标识符，长度限制256字节以内。 |

#### UkeyAuthRequest22+

USB证书凭据授权请求信息。

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| keyUri | string | 否 | 否 | 表示USB证书凭据的唯一标识符，长度限制256字节以内。 |

#### AuthorizeRequest22+

证书授权请求信息。

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| certTypes | Array<CertificateType> | 否 | 否 | 表示证书类型的列表。 |
| certPurpose | certificateManager.CertificatePurpose | 否 | 是 | 表示证书用途。 若certTypes参数中存在CertificateType.CREDENTIAL_UKEY类型，则certPurpose参数生效。 |

#### certificateManagerDialog.openCertificateManagerDialog

openCertificateManagerDialog(context: common.Context, pageType: CertificateDialogPageType): Promise<void>

表示拉起证书管理对话框，显示相应的页面，使用Promise方式异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**模型约束：** 此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | 表示应用的上下文信息。 |
| pageType | CertificateDialogPageType | 是 | 表示页面类型。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理对话框错误码]([证书管理对话框错误码](../../errors/证书管理对话框错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 29700001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```ets
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

/* context为应用的上下文信息，调用方自行获取，此处仅为示例 */
let context: common.Context = new UIContext().getHostContext() as common.Context;
/* pageType为页面类型，此处赋值PAGE_MAIN，即拉起证书管理主界面 */
let pageType: certificateManagerDialog.CertificateDialogPageType = certificateManagerDialog.CertificateDialogPageType.PAGE_MAIN;
try {
  certificateManagerDialog.openCertificateManagerDialog(context, pageType).then(() => {
    console.info('Succeeded in opening certificate manager dialog.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to open certificate manager dialog. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to open certificate manager dialog. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManagerDialog.openInstallCertificateDialog14+

openInstallCertificateDialog(context: common.Context, certType: CertificateType, certScope: CertificateScope, cert: Uint8Array): Promise<string>

表示拉起证书管理安装证书向导，显示相应的页面，使用Promise方式异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManagerDialog

设备行为差异： 该接口在PC/2in1设备可正常调用，在其他设备中certType传入CA_CERT时返回29700004错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | 表示应用的上下文信息。 |
| certType | CertificateType | 是 | 表示安装证书类型，目前支持CA_CERT、CREDENTIAL_USER、CREDENTIAL_SYSTEM。 |
| certScope | CertificateScope | 是 | 表示安装证书的使用范围，目前支持CURRENT_USER、NOT_SPECIFIED。 |
| cert | Uint8Array | 是 | 表示安装证书数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。表示返回证书uri的结果，最大长度为256字节。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理对话框错误码](证书管理对话框错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 29700001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 29700002 | The user cancels the installation operation. |
| 29700003 | The user install certificate failed in the certificate manager dialog, such as the certificate is in an invalid format. |
| 29700004 | The API is not supported on this device. |
| 29700005 | The operation does not comply with the device security policy, such as the device does not allow users to manage the ca certificate of the global user. |

**示例**：

```ets
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

/* context为应用的上下文信息，调用方自行获取，此处仅为示例 */
let context: common.Context = new UIContext().getHostContext() as common.Context;
/* certificateType为证书类型，此处赋值CA_CERT，即安装CA证书 */
let certificateType: certificateManagerDialog.CertificateType = certificateManagerDialog.CertificateType.CA_CERT;
/* certificateScope为证书使用范围，此处赋值CURRENT_USER，即当前用户下可用 */
let certificateScope: certificateManagerDialog.CertificateScope = certificateManagerDialog.CertificateScope.CURRENT_USER;
/* 安装的CA证书数据需要业务赋值，本例数据非CA证书数据 */
let caCert: Uint8Array = new Uint8Array([
  0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01,
]);
try {
  certificateManagerDialog.openInstallCertificateDialog(context, certificateType, certificateScope, caCert).then((uri: string) => {
    console.info('Succeeded opening install certificate');
  }).catch((err: BusinessError) => {
    console.error(`Failed to open install certificate dialog. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to open install certificate dialog. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManagerDialog.openUninstallCertificateDialog18+

openUninstallCertificateDialog(context: common.Context, certType: CertificateType, certUri: string): Promise<void>

表示拉起证书管理删除证书向导，显示相应的页面，使用Promise方式异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**设备行为差异：** 该接口在PC/2in1设备可正常调用，在其他设备中返回29700004错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | 表示应用的上下文信息。 |
| certType | CertificateType | 是 | 表示删除证书类型。 |
| certUri | string | 是 | 表示待删除证书的唯一标识符，最大长度为256字节。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理对话框错误码](证书管理对话框错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 29700001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 29700002 | The user cancels the uninstallation operation. |
| 29700003 | The user uninstall certificate failed in the certificate manager dialog, such as the certificate uri is not exist. |
| 29700004 | The API is not supported on this device. |
| 29700005 | The operation does not comply with the device security policy, such as the device does not allow users to manage the ca certificate of the global user. |

**示例**：

```ets
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

/* context为应用的上下文信息，调用方自行获取，此处仅为示例 */
let context: common.Context = new UIContext().getHostContext() as common.Context;
/* certificateType为证书类型，此处赋值CA_CERT，即安装CA证书 */
let certificateType: certificateManagerDialog.CertificateType = certificateManagerDialog.CertificateType.CA_CERT;
/* certUri为业务安装证书返回的唯一标识符，此处仅为示例 */
let certUri: string = "test";
try {
  certificateManagerDialog.openUninstallCertificateDialog(context, certificateType, certUri).then(() => {
    console.info('Succeeded opening uninstall certificate');
  }).catch((err: BusinessError) => {
    console.error(`Failed to open uninstall certificate dialog. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to open uninstall certificate dialog. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManagerDialog.openCertificateDetailDialog18+

openCertificateDetailDialog(context: common.Context, cert: Uint8Array, property: CertificateDialogProperty): Promise<void>

表示拉起证书管理对话框显示证书的详情，使用Promise方式异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**设备行为差异：** 该接口在PC/2in1设备可正常调用，在其他设备中返回29700004错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | 表示应用的上下文信息。 |
| cert | Uint8Array | 是 | 表示安装证书数据。 |
| property | CertificateDialogProperty | 是 | 表示拉起证书管理对话框的属性。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理对话框错误码](证书管理对话框错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 29700001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 29700003 | Show the certificate detail dialog failed, such as the certificate is in an invalid format. |
| 29700004 | The API is not supported on this device. |

**示例**：

```ets
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

/* context为应用的上下文信息，调用方自行获取，此处仅为示例 */
let context: common.Context = new UIContext().getHostContext() as common.Context;
/* 安装的CA证书数据需要业务赋值，本例数据非CA证书数据 */
let caCert: Uint8Array = new Uint8Array([
  0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01,
]);
let property: certificateManagerDialog.CertificateDialogProperty = {
  showInstallButton: false /* 不显示安装按钮 */
};
try {
  certificateManagerDialog.openCertificateDetailDialog(context, caCert, property).then(() => {
    console.info('Succeeded opening certificate detail dialog.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to open certificate detail dialog. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to open certificate detail dialog. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManagerDialog.openAuthorizeDialog20+

openAuthorizeDialog(context: common.Context): Promise<string>

打开证书管理对话框的授权页面。在弹出的页面中，用户可以为应用授权证书。使用Promise方式异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**模型约束：** 此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | 表示应用的上下文信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。表示返回授权证书uri的结果，最大长度为256字节。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理对话框错误码](证书管理对话框错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Invalid parameter. Possible causes: 1. A mandatory parameter is left unspecified. 2. Incorrect parameter type. 3. Parameter verification failed. |
| 29700001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 29700002 | The user cancels the authorization. |

**示例**：

```ets
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

/* context为应用的上下文信息，调用方自行获取，此处仅为示例 */
let context: common.Context = new UIContext().getHostContext() as common.Context;
try {
    certificateManagerDialog.openAuthorizeDialog(context).then((uri: string) => {
        console.info(`Success to authorize certificate, uri: ${uri}`)
    }).catch((err: BusinessError) => {
        console.error(`Failed to authorize certificate. Code: ${err.code}, message: ${err.message}`);
    });
} catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to authorize certificate. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManagerDialog.openAuthorizeDialog22+

openAuthorizeDialog(context: common.Context, authorizeRequest: AuthorizeRequest): Promise<CertReference>

打开USB凭据PIN码认证对话框的授权页面。在弹出的页面中，用户为应用程序授权证书，可授权的证书类型包括应用私有凭据、用户公共凭据和USB凭据。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**设备行为差异：** 该接口在PC设备可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | 表示应用的上下文信息。 |
| authorizeRequest | AuthorizeRequest | 是 | 表示授权请求信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<CertReference> | Promise对象，返回授权证书引用的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[证书管理对话框错误码](证书管理对话框错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. |
| 29700001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error; 4. Call other service failed. Please try again. |
| 29700002 | The user cancels the authorization. |
| 29700006 | Indicates that the input parameters validation failed. for example, the parameter format is incorrect or the value range is invalid. |
| 29700007 | No available certificate for authorization |

**示例**：

```ets
import { certificateManagerDialog, certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

/* context为应用的上下文信息，调用方自行获取，此处仅为示例 */
let context: common.Context = new UIContext().getHostContext() as common.Context;
let certTypes: Array<certificateManagerDialog.CertificateType> = [
  certificateManagerDialog.CertificateType.CREDENTIAL_USER,
  certificateManagerDialog.CertificateType.CREDENTIAL_APP,
  certificateManagerDialog.CertificateType.CREDENTIAL_UKEY
];
let certPurpose: certificateManager.CertificatePurpose = certificateManager.CertificatePurpose.PURPOSE_DEFAULT;
let authorizeRequest: certificateManagerDialog.AuthorizeRequest = { certTypes: certTypes, certPurpose: certPurpose };
try {
    certificateManagerDialog.openAuthorizeDialog(context, authorizeRequest).then((certReference: certificateManagerDialog.CertReference) => {
      let reference = certReference;
      console.info(`Success to open authorize dialog.`)
    }).catch((err: BusinessError) => {
        console.error(`Failed to open authorize dialog. Code: ${err.code}, message: ${err.message}`);
    });
} catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to open authorize dialog. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManagerDialog.openUkeyAuthDialog22+

openUkeyAuthDialog(context: common.Context, ukeyAuthRequest: UkeyAuthRequest): Promise<void>

打开USB凭据PIN码认证对话框的授权页面。在弹出的页面中，用户可以输入PIN码授权USB证书凭据。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**设备行为差异：** 该接口在PC设备可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | 表示应用的上下文信息。 |
| ukeyAuthRequest | UkeyAuthRequest | 是 | 表示USB凭据授权请求信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[证书管理对话框错误码](证书管理对话框错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. |
| 29700001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 29700002 | The user cancels the authentication operation. |
| 29700003 | The authentication operation failed, such as the USB key certificate does not exist, the USB key status is abnormal. |
| 29700006 | Indicates that the input parameters validation failed. For example, the parameter format is incorrect or the value range is invalid. |

**示例**：

```ets
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

/* context为应用的上下文信息，调用方自行获取，此处仅为示例 */
let context: common.Context = new UIContext().getHostContext() as common.Context;
/* keyUri为证书凭据的唯一标识符，调用方自行获取，此处仅为示例 */
let keyUri: string = "test"
let ukeyAuthRequest: certificateManagerDialog.UkeyAuthRequest = { keyUri: keyUri }
try {
    certificateManagerDialog.openUkeyAuthDialog(context, ukeyAuthRequest).then(() => {
        console.info(`Success to open ukey authorization dialog`)
    }).catch((err: BusinessError) => {
        console.error(`Failed to open ukey authorization dialog. Code: ${err.code}, message: ${err.message}`);
    });
} catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to open ukey authorization dialog. Code: ${error.code}, message: ${error.message}`);
}
```