# @ohos.app.ability.EmbeddableUIAbility.d.ts

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
 * @file
 * @kit AbilityKit
 */
import UIAbility from './@ohos.app.ability.UIAbility';
import type EmbeddableUIAbilityContext from './application/EmbeddableUIAbilityContext';
/**
 * EmbeddableUIAbility is an embeddable UIAbility component provided for atomic services. It inherits from
 * [UIAbility]{@link @ohos.app.ability.UIAbility}.
 * You can implement EmbeddableUIAbility to enable atomic services to be launched by other applications either as a
 * standalone window or embedded within the host application's UI.
 * For details about the inheritance relationship of each ability, see
 * [Inheritance Relationship](docroot://reference/apis-ability-kit/js-apis-app-ability-ability.md#ability-inheritance-relationship)
 * .
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 12
 */
export default class EmbeddableUIAbility extends UIAbility {
    /**
     * Context of the EmbeddableUIAbility.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    context: EmbeddableUIAbilityContext;
}

```
