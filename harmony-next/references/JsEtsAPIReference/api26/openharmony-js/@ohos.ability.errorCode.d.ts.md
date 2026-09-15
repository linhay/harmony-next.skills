# @ohos.ability.errorCode.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2023 Huawei Device Co., Ltd.
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
 * @kit AbilityKit
 */
/**
 * Enumerates the error codes that may be returned when an ability is started.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @since 6
 */
export enum ErrorCode {
    /**
     * Permission denied.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 6
     */
    PERMISSION_DENY = -3,
    /**
     * The ability is not found.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 6
     */
    ABILITY_NOT_FOUND = -2,
    /**
     * Invalid parameter.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 6
     */
    INVALID_PARAMETER = -1,
    /**
     * No error.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 6
     */
    NO_ERROR = 0
}

```
