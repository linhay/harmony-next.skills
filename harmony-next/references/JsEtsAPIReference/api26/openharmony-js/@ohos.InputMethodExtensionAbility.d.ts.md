# @ohos.InputMethodExtensionAbility.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022 Huawei Device Co., Ltd.
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
 * @kit IMEKit
 */
import Want from './@ohos.app.ability.Want';
import type InputMethodExtensionContext from './@ohos.InputMethodExtensionContext';
/**
 * The **InputMethodExtensionAbility** module provides APIs for developing input methods and managing the lifecycle of
 * input method extensions.
 *
 * > **NOTE**
 * >
 * > - The APIs of this module can be used only in the stage model.
 *
 * @syscap SystemCapability.MiscServices.InputMethodFramework
 * @stagemodelonly
 * @since 9
 */
declare class InputMethodExtensionAbility {
    /**
     * Context of the **InputMethodExtension**, which is inherited from **ExtensionContext**.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @stagemodelonly
     * @since 9
     */
    context: InputMethodExtensionContext;
    /**
     * Called when the **InputMethodExtensionAbility** is started to implement initialization.
     *
     * @param { Want } want - Information related to the **InputMethodExtensionAbility**, including the ability name and
     *     bundle name.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @stagemodelonly
     * @since 9
     */
    onCreate(want: Want): void;
    /**
     * Called when this **InputMethodExtensionAbility** is destroyed to clear resources.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @stagemodelonly
     * @since 9
     */
    onDestroy(): void;
}
export default InputMethodExtensionAbility;

```
