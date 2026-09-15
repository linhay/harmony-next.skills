# @ohos.userIAM.userAccessCtrl.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2024 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License"),
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
 * @file User Access Control
 * @kit UserAuthenticationKit
 */
/**
 * The **userAccessCtrl** module is a core component of the OpenHarmony user identity and access management (UserIAM)
 * system. It is dedicated to the verification and management of authentication tokens. This module provides APIs for
 * verifying authentication tokens (**AuthToken**). It can parse and verify user authentication results and return
 * detailed authentication information.
 *
 * This module applies to the following scenarios:
 *
 * - System-level applications need to verify the validity of user authentication tokens.
 * - Detailed information about the authentication token needs to be obtained, such as the authentication type, trust
 * level, and user ID.
 * - Access control decisions need to be made based on the authentication result.
 *
 * @syscap SystemCapability.UserIAM.UserAuth.Core
 * @since 18
 */
declare namespace userAccessCtrl {
}
export default userAccessCtrl;

```
