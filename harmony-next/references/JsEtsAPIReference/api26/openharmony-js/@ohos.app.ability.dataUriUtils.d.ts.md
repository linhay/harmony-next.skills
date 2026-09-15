# @ohos.app.ability.dataUriUtils.d.ts

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
 * The DataUriUtils module provides APIs to process URI objects. You can use the APIs to attach an ID to the end of a
 * given URI and obtain, delete, or update the ID attached to the end of a given URI.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @since 9
 */
declare namespace dataUriUtils {
    /**
     * Obtains the ID attached to the end of a given URI.
     *
     * @param { string } uri - Target URI object.
     * @returns { number } ID obtained.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 9
     */
    function getId(uri: string): number;
    /**
     * Attaches an ID to the end of a given URI.
     *
     * @param { string } uri - Target URI object.
     * @param { number } id - ID to be attached.
     * @returns { string } URI object with the ID attached.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 9
     */
    function attachId(uri: string, id: number): string;
    /**
     * Deletes the ID from the end of a given URI.
     *
     * @param { string } uri - URI object from which the ID is to be deleted.
     * @returns { string } URI object with the ID deleted.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 9
     */
    function deleteId(uri: string): string;
    /**
     * Updates the ID in a given URI.
     *
     * @param { string } uri - Target URI object.
     * @param { number } id - New ID.
     * @returns { string } URI object with the new ID.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 9
     */
    function updateId(uri: string, id: number): string;
}
export default dataUriUtils;

```
