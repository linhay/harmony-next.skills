# @ohos.net.policy.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2023 Huawei Device Co., Ltd.
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
 * @file Network Policy Management
 * @kit NetworkKit
 */
import type connection from './@ohos.net.connection';
import Context from './application/Context';
/**
 * The **policy** module provides APIs for managing network policies, which allow you to use firewall technology to
 * control and manage the data traffic used.
 *
 * @syscap SystemCapability.Communication.NetManager.Core
 * @since 10
 */
declare namespace policy {
    /**
     * Defines the network type.
     *
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 10
     */
    type NetBearType = connection.NetBearType;
    /**
     * Queries the network access policy of an application (whether cellular or Wi-Fi network access is allowed). You can
     * check the policy by choosing **Settings** > **Mobile network** > **Manage data usage** > **Network access**. This
     * API uses a promise to return the result.
     *
     * @returns { Promise<NetAccessPolicy> } Promise used to return the network access policy of the application.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error, such as nullptr。
     * @syscap SystemCapability.Communication.NetManager.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    function getNetAccessPolicy(): Promise<NetAccessPolicy>;
    /**
     * Sets whether the current application can connect to the Wi-Fi or cellular network. You can call this API to open
     * the network access settings page of the current application and set the network access permission of the
     * application. This API uses a promise to return the result.
     *
     * @param { Context } context - Application context of the stage model. (Only **UIAbilityContext** and
     *     **ExtensionContext** are supported.)
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.Communication.NetManager.Core
     * @stagemodelonly
     * @since 22
     */
    function showAppNetPolicySettings(context: Context): Promise<void>;
    /**
     * Defines the network access policy information.
     *
     * @syscap SystemCapability.Communication.NetManager.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    export interface NetAccessPolicy {
        /**
         * Whether to allow Internet access over Wi-Fi.
         *
         * **true**: yes;
         *
         * **false**: no.
         *
         * @syscap SystemCapability.Communication.NetManager.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        allowWiFi: boolean;
        /**
         * Whether to allow Internet access over the cellular network.
         *
         * **true**: yes.
         *
         * **false**: no.
         *
         * @syscap SystemCapability.Communication.NetManager.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        allowCellular: boolean;
    }
}
export default policy;

```
