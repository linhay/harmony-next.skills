# @ohos.app.ability.EmbeddedUIExtensionAbility.d.ts

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
import UIExtensionAbility from './@ohos.app.ability.UIExtensionAbility';
/**
 * EmbeddedUIExtensionAbility is a component that enables cross-process UI embedding. It inherits from
 * [UIExtensionAbility]{@link @ohos.app.ability.UIExtensionAbility:UIExtensionAbility}.
 * You can implement this class to add cross-process UI embedding capabilities to your applications. A typical use case
 * is embedding a UI, provided by the application's own EmbeddedUIExtensionAbility, into a
 * [UIAbility]{@link @ohos.app.ability.UIAbility} page using an
 * [EmbeddedComponent]{@link @internal/component/ets/embedded_component}.
 * For details about the inheritance relationship of each ability, see
 * [Inheritance Relationship](docroot://reference/apis-ability-kit/js-apis-app-ability-ability.md#ability-inheritance-relationship)
 * .
 * This API can be properly called on PCs/2-in-1 devices and tablets. It is unavailable on other devices.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @since 12
 */
export default class EmbeddedUIExtensionAbility extends UIExtensionAbility {
}

```
