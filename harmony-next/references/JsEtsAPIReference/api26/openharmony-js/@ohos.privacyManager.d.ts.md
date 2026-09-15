# @ohos.privacyManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2022 Huawei Device Co., Ltd.
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
import { Permissions } from './permissions';
/**
 * This module primarily provides privacy management APIs such as permission usage records, supporting system
 * applications in recording, querying, listening to, and controlling the usage of sensitive permissions. A permission
 * usage record describes when a sensitive permission was used, how it was used, whether it is currently in use, and
 * whether these usage records are allowed to be recorded or queried.
 *
 * This module is mainly used in the following scenarios:
 *
 * - Adding/querying the sensitive permission access records of a specified application.
 * - Subscribing to permission usage status change events, sensing changes in permission usage from unused to
 * foreground use and background use, and linking with business logic.
 * - Controlling the permission access record toggle for the current user.
 * - Querying whether a certain permission is currently being used.
 *
 * @syscap SystemCapability.Security.AccessToken
 * @since 9
 */
declare namespace privacyManager {
}
export { Permissions };
export default privacyManager;

```
