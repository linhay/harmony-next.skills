# @ohos.identifier.oaid.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023-2026 Huawei Device Co., Ltd.
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
 * @file OAID
 * @kit AdsKit
 */
import type { AsyncCallback } from './@ohos.base';
/**
 * This module provides the capability of obtaining and resetting the Open Anonymous Device Identifier (OAID).
 *
 * > **NOTE**
 *
 *
 *
 * > To use the API for obtaining the OAID, you need to
 * > [request user authorization](docroot://security/AccessToken/request-user-authorization.md) (the permission is
 * > enabled by default): ohos.permission.APP_TRACKING_CONSENT.
 *
 * @syscap SystemCapability.Advertising.OAID
 * @since 10
 */
declare namespace identifier {
    /**
     * Obtains the OAID. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.APP_TRACKING_CONSENT
     * @param { AsyncCallback<string> } callback - Callback used to return the OAID.
     *     1. If the app has configured the ohos.permission.APP_TRACKING_CONSENT permission and the cross-app association
     *     access permission is allowed, the OAID is returned.
     *     2. If the app has configured the ohos.permission.APP_TRACKING_CONSENT permission and
     *     the cross-app association access permission is disallowed, 00000000-0000-0000-0000-000000000000 is returned.
     *     3. If the app has not configured the ohos.permission.APP_TRACKING_CONSENT permission,
     *     00000000-0000-0000-0000-000000000000 is returned.
     * @throws { BusinessError } 17300001 - System internal error.
     * @syscap SystemCapability.Advertising.OAID
     * @since 10
     */
    function getOAID(callback: AsyncCallback<string>): void;
    /**
     * Obtains the OAID. This API uses a promise to return the result.
     *
     * @permission ohos.permission.APP_TRACKING_CONSENT
     * @returns { Promise<string> } Promise used to return the OAID.
     *     1. If the app has configured the ohos.permission.APP_TRACKING_CONSENT
     *     permission and the cross-app association access permission is allowed, the OAID is returned.
     *     2. If the app has configured the ohos.permission.APP_TRACKING_CONSENT permission
     *     and the cross-app association access permission is disallowed, 00000000-0000-0000-0000-000000000000
     *     is returned.
     *     3. If the app has not configured the ohos.permission.APP_TRACKING_CONSENT permission,
     *     00000000-0000-0000-0000-000000000000 is returned.
     * @throws { BusinessError } 17300001 - System internal error.
     * @syscap SystemCapability.Advertising.OAID
     * @since 10
     */
    function getOAID(): Promise<string>;
}
export default identifier;

```
