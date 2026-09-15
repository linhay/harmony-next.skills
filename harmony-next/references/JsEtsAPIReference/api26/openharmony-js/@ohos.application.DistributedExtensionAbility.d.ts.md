# @ohos.application.DistributedExtensionAbility.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025-2026 Huawei Device Co., Ltd.
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
import Want from './@ohos.app.ability.Want';
import AbilityConstant from './@ohos.app.ability.AbilityConstant';
import type DistributedExtensionContext from './@ohos.application.DistributedExtensionContext';
/**
 * The **DistributedExtensionAbility** module provides distributed extension capabilities and lifecycle callbacks for
 * distributed ability creation, destruction, and connection.
 *
 *
 * @syscap SystemCapability.DistributedSched.AppCollaboration
 * @stagemodelonly
 * @since 20
 */
declare class DistributedExtensionAbility {
    /**
     * Context of the **DistributedExtension**. This context inherits from **ExtensionContext**.
     *
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 20
     */
    context: DistributedExtensionContext;
    /**
     * Callback invoked to initialize the service logic when a **DistributedExtensionAbility** instance is created.
     *
     * @param { Want } want - Want information related to the **DistributedExtensionAbility** instance, including the ability
     *     name and bundle name.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 20
     */
    onCreate(want: Want): void;
    /**
     * Callback invoked to clear resources when a **ServiceExtensionAbility** instance is destroyed.
     *
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 20
     */
    onDestroy(): void;
    /**
     * Callback invoked to return the collaboration result in multi-device collaboration scenarios.
     *
     * @param { Record<string, Object> } wantParam - Want parameter, which supports only the key **"
     *     ohos.extra.param.key.supportCollaborateIndex"**. The key can be used to obtain the data passed by the caller and
     *     perform corresponding processing.
     * @returns { AbilityConstant.CollaborateResult } Collaboration result, that is, whether the target application accepts the
     *     collaboration request.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 20
     */
    onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult;
}
export default DistributedExtensionAbility;

```
