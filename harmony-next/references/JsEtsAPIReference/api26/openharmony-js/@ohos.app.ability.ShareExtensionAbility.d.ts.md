# @ohos.app.ability.ShareExtensionAbility.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023 Huawei Device Co., Ltd.
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
 * ShareExtensionAbility provides extended capabilities for integrating a share details page. It inherits from
 * [UIExtensionAbility]{@link @ohos.app.ability.UIExtensionAbility:UIExtensionAbility}.
 *
 * By implementing ShareExtensionAbility, you can process content shared from other applications. For example, you could
 * use ShareExtensionAbility to implement the text sharing feature. When a user initiates a share action in another
 * application, your application will appear as an option in the system share panel. Upon selection, the system
 * activates your application to process the content and display the share detail page.
 *
 * For details about the inheritance relationship of each ability, see
 * [Inheritance Relationship](docroot://reference/apis-ability-kit/js-apis-app-ability-ability.md#ability-inheritance-relationship)
 * .
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @since 10
 */
export default class ShareExtensionAbility extends UIExtensionAbility {
}

```
