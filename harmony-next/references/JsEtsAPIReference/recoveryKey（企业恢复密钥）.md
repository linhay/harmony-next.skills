# recoveryKey（企业恢复密钥）

在保证用户数据安全性前提下，保证用户数据的健壮性，用于加密硬盘数据的安全解密。

仅供企业安全管控类MDM应用申请权限后使用。

**起始版本：**5.0.3(15)

#### 导入模块

```ets
import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
```

#### EnterpriseRecoveryKeyInfo

企业恢复密钥及相关加密参数。

**系统能力：**SystemCapability.PCService.RecoveryKeyService

**起始版本：**5.0.3(15)

名称

类型

只读

可选

说明

enterpriseRecoveryKey

Uint8Array

否

否

AES-GCM-256加密后的企业恢复密钥。

exportPublicKey

Uint8Array

否

否

AES-GCM-256加密时使用的临时公钥。

iv

Uint8Array

否

否

AES-GCM-256加密时使用的iv。

tag

Uint8Array

否

否

AES-GCM-256加密时使用的tag。

#### getEnterpriseRecoveryKey

getEnterpriseRecoveryKey(userId: number): Promise<EnterpriseRecoveryKeyInfo>

获取企业恢复密钥。

**需要权限：**ohos.permission.ENTERPRISE_RECOVERY_KEY

**系统能力：**SystemCapability.PCService.RecoveryKeyService

**起始版本：**5.0.3(15)

**参数：**

参数名

类型

必填

说明

userId

number

是

需要获取企业恢复密钥的用户ID。

**返回值：**

类型

说明

Promise<[EnterpriseRecoveryKeyInfo](#section35870815206)>

Promise对象，返回企业恢复密钥及相关加密参数的对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

错误码ID

错误信息

201

Permission denied.

401

The parameter check failed.

1014400001

System service exception.

1014400201

Invalid device type, current device is not enterprise device.

1014400202

Invalid userId.

1014400203

Enterprise recovery key is already existed.

**示例：**

```ets
import { buffer } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

let userId: number = 100;
recoveryKey.getEnterpriseRecoveryKey(userId).then((info: recoveryKey.EnterpriseRecoveryKeyInfo) => {
  console.info(`Succeeded in getting enterprise recovery key.`);
  console.info(`EnterpriseRecoveryKeyInfo enterpriseRecoveryKey: ${buffer.from(info.enterpriseRecoveryKey).toString('hex')}`);
  console.info(`EnterpriseRecoveryKeyInfo exportPublicKey: ${buffer.from(info.exportPublicKey).toString('hex')}`);
  console.info(`EnterpriseRecoveryKeyInfo iv: ${buffer.from(info.iv).toString('hex')}`);
  console.info(`EnterpriseRecoveryKeyInfo tag: ${buffer.from(info.tag).toString('hex')}`);
}).catch((error: BusinessError) => {
  console.error(`Failed to get enterprise recovery key. Code: ${error.code}, message: ${error.message}`);
});
```

#### getAuthChallenge

getAuthChallenge(): Promise<Uint8Array>

获取挑战值，在发起更新企业公钥证书、删除企业恢复密钥数据流程前，需要先获取挑战值。

**需要权限：**ohos.permission.ENTERPRISE_RECOVERY_KEY

**系统能力：**SystemCapability.PCService.RecoveryKeyService

**起始版本：**5.0.3(15)

**返回值：**

类型

说明

Promise<Uint8Array>

在发起更新企业公钥证书、清理企业恢复密钥数据流程前，获取到的挑战值。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

错误码ID

错误信息

201

Permission denied.

1014400001

System service exception.

1014400201

Invalid device type, current device is not enterprise device.

**示例：**

```ets
import { buffer } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

recoveryKey.getAuthChallenge().then((challenge: Uint8Array) => {
  console.info(`Succeeded in getting challenge. challenge is: ${buffer.from(challenge).toString('hex')}`);
}).catch((error: BusinessError) => {
  console.error(`Failed to get challenge. Code: ${error.code}, message: ${error.message}`);
});
```

#### updateEnterpriseCertificate

updateEnterpriseCertificate(signature: Uint8Array, cert: Uint8Array): Promise<number>

更新企业公钥证书流程，需要先调[getAuthChallenge](#section41041418113717)接口获取挑战值并[签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-signature)。

**需要权限：**ohos.permission.ENTERPRISE_RECOVERY_KEY

**系统能力：**SystemCapability.PCService.RecoveryKeyService

**起始版本：**5.0.3(15)

**参数：**

参数名

类型

必填

说明

signature

Uint8Array

是

挑战值的[签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-signature)。

cert

Uint8Array

是

PEM格式的公钥证书，以二进制的格式完整传递。

**返回值：**

类型

说明

Promise<number>

Promise对象。成功返回0，失败无返回。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

错误码ID

错误信息

201

Permission denied.

401

The parameter check failed.

1014400001

System service exception.

1014400201

Invalid device type, current device is not enterprise device.

1014400204

Invalid signature.

1014400205

Invalid cert.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let signature: Uint8Array = new Uint8Array([0]);
let cert: Uint8Array = new Uint8Array([0]);
recoveryKey.updateEnterpriseCertificate(signature, cert).then((ret: number)=>{
  console.info(`Succeeded in updating certificate. result is: ${ret}`);
}).catch((error: BusinessError) => {
  console.error(`Failed to update certificate. Code: ${error.code}, message: ${error.message}`);
});
```

#### deleteEnterpriseRecoveryKey

deleteEnterpriseRecoveryKey(userId: number, signature: Uint8Array): Promise<number>

删除企业恢复密钥相关数据，需要先调[getAuthChallenge](#section41041418113717)接口获取挑战值并[签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-signature)。

**需要权限：**ohos.permission.ENTERPRISE_RECOVERY_KEY

**系统能力：**SystemCapability.PCService.RecoveryKeyService

**起始版本：**5.0.3(15)

**参数：**

参数名

类型

必填

说明

userId

number

是

需要删除企业恢复密钥的用户ID。

signature

Uint8Array

是

挑战值的[签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-signature)。

**返回值：**

类型

说明

Promise<number>

Promise对象。成功返回0，失败无返回。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

错误码ID

错误信息

201

Permission denied.

401

The parameter check failed.

1014400001

System service exception.

1014400201

Invalid device type, current device is not enterprise device.

1014400202

Invalid userId.

1014400204

Invalid signature.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let signature: Uint8Array = new Uint8Array([0]);
let userId: number = 100;
recoveryKey.deleteEnterpriseRecoveryKey(userId, signature).then((ret: number)=>{
  console.info(`Succeeded in deleting enterprise recovery key. result is: ${ret}`);
}).catch((error: BusinessError)=>{
  console.error(`Failed to delete enterprise recovery key. Code: ${error.code}, message: ${error.message}`);
});
```

#### verifyUserIdentityEnterprise

verifyUserIdentityEnterprise(userId: number, userType: number, pinCode: string): Promise<void>

验证企业用户身份。在导出企业恢复密钥以重置锁屏密码之前，请先验证用户的锁屏密码。

**需要权限：**ohos.permission.ENTERPRISE_RECOVERY_KEY

**系统能力：**SystemCapability.PCService.RecoveryKeyService

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

userId

number

是

需要导出企业恢复密钥的用户ID。

userType

number

是

[用户类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-osaccount#osaccounttype) 。可以通过调用[getOsAccountType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-osaccount#getosaccounttype9)获取。

pinCode

string

是

用户锁屏密码，字符长度不超过64位。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

错误码ID

错误信息

201

Permission denied.

1014400001

System service exception.

1014400103

Authentication is failed.

1014400201

Invalid device type, current device is not enterprise device.

1014400202

Invalid userId.

**示例：**

```ets
import { BusinessError, osAccount } from '@kit.BasicServicesKit';

async function verifyUserIdentityEnterprise() {
  try {
    let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
    let accountType: osAccount.OsAccountType = await accountManager.getOsAccountType();

    let userId: number = await accountManager.getOsAccountLocalId();
    let userType: number = accountType.valueOf();
    let pinCode: string = '111111';
    recoveryKey.verifyUserIdentityEnterprise(userId, userType, pinCode).then(() => {
      console.info(`Succeeded in verifying user identity.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to verified user identity. Code: ${error.code}, message: ${error.message}`);
    })
  } catch (e) {
    console.error(`Failed to verifyUserIdentityEnterprise. Code: ${e.code}, message: ${e.message}`);
  }
}
```

#### getEnterpriseRecoveryKeyForResettingPin

getEnterpriseRecoveryKeyForResettingPin(userId: number, userType: number): Promise<EnterpriseRecoveryKeyInfo>

导出用于重置锁屏密码的企业恢复密钥。先需要调用[verifyUserIdentityEnterprise](#section1894251193414)接口验证身份，并在30秒内调用此接口。

**需要权限：**ohos.permission.ENTERPRISE_RECOVERY_KEY

**系统能力：**SystemCapability.PCService.RecoveryKeyService

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

userId

number

是

需要导出企业恢复密钥的用户ID。

userType

number

是

[用户类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-osaccount#osaccounttype) 。可以通过调用[getOsAccountType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-osaccount#getosaccounttype9)获取。

**返回值：**

类型

说明

Promise<[EnterpriseRecoveryKeyInfo](#section35870815206)>

Promise对象，返回企业恢复密钥及相关加密参数的对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](ArkTS API 错误码.md)。

错误码ID

错误信息

201

Permission denied.

1014400001

System service exception.

1014400201

Invalid device type, current device is not enterprise device.

1014400202

Invalid userId.

**示例：**

```ets
import { buffer } from '@kit.ArkTS';
import { BusinessError, osAccount } from '@kit.BasicServicesKit';

async function getEnterpriseRecoveryKeyForResettingPin() {
  try {
    let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
    let accountType: osAccount.OsAccountType = await accountManager.getOsAccountType();

    let userId: number = await accountManager.getOsAccountLocalId();
    let userType: number = accountType.valueOf();
    recoveryKey.getEnterpriseRecoveryKeyForResettingPin(userId, userType)
      .then((info: recoveryKey.EnterpriseRecoveryKeyInfo) => {
        console.info(`Succeeded in getting enterprise recovery key for resetting pin.`);
        console.info(`EnterpriseRecoveryKeyInfo enterpriseRecoveryKey: ${buffer.from(info.enterpriseRecoveryKey)
          .toString('hex')}`);
        console.info(`EnterpriseRecoveryKeyInfo exportPublicKey: ${buffer.from(info.exportPublicKey)
          .toString('hex')}`);
        console.info(`EnterpriseRecoveryKeyInfo iv: ${buffer.from(info.iv).toString('hex')}`);
        console.info(`EnterpriseRecoveryKeyInfo tag: ${buffer.from(info.tag).toString('hex')}`);
      }).catch((err: BusinessError) => {
      console.error(`Failed to get enterprise recovery key for resetting pin. Code: ${err.code}, message: ${err.message}`);
    })
  } catch (e) {
    console.error(`Failed to getEnterpriseRecoveryKeyForResettingPin. Code: ${e.code}, message: ${e.message}`);
  }
}
```