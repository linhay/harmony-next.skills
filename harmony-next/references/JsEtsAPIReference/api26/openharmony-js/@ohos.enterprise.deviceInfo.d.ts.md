# @ohos.enterprise.deviceInfo.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2024 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * @file Device Information Management
 * @kit MDMKit
 */
import type Want from './@ohos.app.ability.Want';
/**
 * This module provides APIs for enterprise device information management, including obtaining device serial numbers,
 * device names, and SIM card information. Enterprise administrators can use this module to query device details,
 * enabling unified management and tracking of device assets.
 *
 * **Use cases:**
 *
 * - Device asset management and tracking
 * - Enterprise device compliance check
 * - Device information collection and statistics
 * - Fault diagnosis and device identification
 *
 * > **NOTE**
 * >
 * > The APIs of this module can be called only by a device administrator application that is enabled. For details, see
 * > [MDM Kit Development](docroot://mdm/mdm-kit-guide.md).
 *
 * @syscap SystemCapability.Customization.EnterpriseDeviceManager
 * @since 12
 */
declare namespace deviceInfo {
    /**
     * Obtains device information.
     *
     * @permission ohos.permission.ENTERPRISE_GET_DEVICE_INFO
     * @param { Want } admin - Enterprise device management extension component, which is used to specify the target
     *     application that has the device management capability. The **Want** object must contain **abilityName** (
     *     extended ability name) and **bundleName** (application bundle name) parameters.
     * @param { string } label - Device information label that can be obtained.
     *     <br>- **deviceName**: device name.
     *     <br>- **deviceSerial**: device serial number.
     *     <br>- **simInfo**: SIM card information.
     * @returns { string } Device information obtained.
     *     <br>If **label** is **simInfo**, the return value is the SIM card information in a JSON string. For example,
     *     [{"slotId": 0, "MEID": "", "IMSI": "", "ICCID": "", "IMEI": "", "NUMBER": ""},
     *     {"slotId": 1, "MEID": "", "IMSI": "", "ICCID": "", "IMEI": "", "NUMBER": ""}],
     *     where **slotId:0** indicates card slot 1, and **slotId:1** indicates card slot 2. **NUMBER** indicates the
     *     phone number and is supported since API version 23. The value is in the E.164 international standard format (
     *     for example, +8612345678901) that contains the country code.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200007 - The system ability works abnormally.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @StageModelOnly
     * @since 12
     */
    function getDeviceInfo(admin: Want, label: string): string;
}
export default deviceInfo;

```
