# @ohos.distributedHardware.deviceManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2020-2024 Huawei Device Co., Ltd.
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
 * @file
 * @kit DistributedServiceKit
 */
/**
 * The APIs of this module are deprecated. You are advised to use
 * [@ohos.distributedDeviceManager]{@link @ohos.distributedDeviceManager:distributedDeviceManager}.
 * The **deviceManager** module provides APIs for distributed device management.
 * System applications can call the APIs to do the following:
 *
 * - Subscribe to or unsubscribe from device state changes.
 * - Discover devices nearby.
 * - Authenticate or deauthenticate a device.
 * - Query the trusted device list.
 * - Query local device information, including the device name, type, and ID.
 * - Publishes device information for discovery purposes.
 *
 * @syscap SystemCapability.DistributedHardware.DeviceManager
 * @since 7
 * @deprecated since 11
 * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager
 */
declare namespace deviceManager {
    /**
     * Provides APIs to obtain information about trusted devices and local devices. Before calling any API in
     * **DeviceManager**, you must use **createDeviceManager** to create a **DeviceManager** instance, for example,
     * **dmInstance**.
     *
     * @syscap SystemCapability.DistributedHardware.DeviceManager
     * @since 7
     * @deprecated since 11
     * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager
     */
    interface DeviceManager {
    }
}
export default deviceManager;

```
