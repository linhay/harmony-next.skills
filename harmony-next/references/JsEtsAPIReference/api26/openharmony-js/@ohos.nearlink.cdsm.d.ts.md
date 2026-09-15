# @ohos.nearlink.cdsm.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2026 Huawei Device Co., Ltd.
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
 * @kit ConnectivityKit
 */
import type { Callback } from '@ohos.base';
/**
 * Provides methods related to nearlink CDSM(Coordinated Devices Set Management).
 *
 * @syscap SystemCapability.Communication.NearLink.Base
 * @stagemodelonly
 * @since 26.0.0
 */
declare namespace cdsm {
    /**
     * Creates a CDSM client instance.
     *
     * @permission ohos.permission.ACCESS_NEARLINK
     * @param { string } address - Indicates the address of CDSM server.
     *     <br>The length must be 17. Value constraint: The value consists of hexadecimal digits and colons (:),
     *     for example, 11:22:33:AA:BB:FF.
     * @returns { CdsmClient } Returns a CDSM client instance.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100003 - NearLink disabled.
     * @throws { BusinessError } 36100041 - Invalid address.
     * @throws { BusinessError } 36100050 - Coordinated Devices Set Management not supported.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function createCdsmClient(address: string): CdsmClient;
    /**
     * Manages a CDSM client instance. Before invoking any CDSM client method,
     * you must use {@link createCdsmClient} to create a CDSM client instance.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface CdsmClient {
        /**
         * Gets the coordinated devices set information.
         *
         * @permission ohos.permission.ACCESS_NEARLINK
         * @returns { CdsmInfo } Returns the coordinated devices set information.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 36100003 - NearLink disabled.
         * @throws { BusinessError } 36100099 - Operation failed.
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        getCdsmInfo(): CdsmInfo;
        /**
         * Subscribes to coordinated devices set information change event.
         *
         * This event is accessible only to applications that granted the ohos.permission.NEARLINK_ACCESS permission.
         * If the application is granted the ohos.permission.GET_NEARLINK_PEER_MAC permission,
         * the callback returns the real device address; otherwise, a random device address is returned.
         *
         * @param { Callback<CdsmInfo> } callback - Callback used to listen for the coordinated devices set information.
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        onCdsmInfoChange(callback: Callback<CdsmInfo>): void;
        /**
         * Unsubscribes from coordinated devices set information change event.
         *
         * @param { Callback<CdsmInfo> } [callback] - Callback used to listen for the coordinated devices set information.
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        offCdsmInfoChange(callback?: Callback<CdsmInfo>): void;
    }
    /**
     * Describes the coordinated devices set information.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface CdsmInfo {
        /**
         * Indicates the members of coordinated devices set.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        members: CdsmMemberInfo[];
    }
    /**
     * Describes the member information of coordinated devices set.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface CdsmMemberInfo {
        /**
         * Indicates the device address.
         * The length must be 17, The value consists of hexadecimal digits and colons (:), for example, 11:22:33:AA:BB:FF.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        address: string;
        /**
         * Member's connection state.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        state: CdsmConnectionState;
    }
    /**
     * The enum of member's connection state.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    enum CdsmConnectionState {
        /**
         * The member is disconnected.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        DISCONNECTED = 0,
        /**
         * The member is connected.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        CONNECTED = 1
    }
}
export default cdsm;

```
