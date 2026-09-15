# @ohos.application.Want.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2023 Huawei Device Co., Ltd.
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
 * @kit API10LessDeprecatedModules
 */
/**
 * Want is a carrier for information transfer between objects (application components). Want can be used as a parameter
 * of **startAbility** to specify a startup target and information that needs to be carried during startup, for example,
 *  **bundleName** and **abilityName**, which respectively indicate the bundle name of the target ability and the
 * ability name in the bundle. When ability A needs to start ability B and transfer some data to ability B, it can use
 * Want a carrier to transfer the data.
 *
 * @syscap SystemCapability.Ability.AbilityBase
 * @since 8
 * @deprecated since 9
 * @useinstead ohos.app.ability.Want/Want
 */
export default class Want {
    /**
     * ID of the device running the ability. If this field is unspecified, the local device is used.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.app.ability.Want/Want#deviceId
     */
    deviceId?: string;
    /**
     * Bundle name.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.app.ability.Want/Want#bundleName
     */
    bundleName?: string;
    /**
     * Name of the ability. If both **bundleName** and **abilityName** are specified in a Want object, the Want object can
     *  match a specific ability. The value of **abilityName** must be unique in an application.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.app.ability.Want/Want#abilityName
     */
    abilityName?: string;
    /**
     * URI information to match. If **Uri** is specified in a Want object, the Want object will match the specified URI
     * information, including **scheme**, **schemeSpecificPart**, **authority**, and **path**.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.app.ability.Want/Want#uri
     */
    uri?: string;
    /**
     * MIME type, that is, the type of the file to open, for example, **'text/xml'** and **'image/*'**. For details about
     * the MIME type definition, see https://www.iana.org/assignments/media-types/media-types.xhtml?utm_source=ld246.com.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.app.ability.Want/Want#type
     */
    type?: string;
    /**
     * How the Want object will be handled. By default, numbers are passed in. For details, see
     * [flags]{@link @ohos.ability.wantConstant:wantConstant.Flags}.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.app.ability.Want/Want#flags
     */
    flags?: number;
    /**
     * Action to take, such as viewing and sharing application details. In implicit Want, you can define this property and
     *  use it together with **uri** or **parameters** to specify the operation to be performed on the data. For details,
     * see [action]{@link @ohos.ability.wantConstant:wantConstant.Action}. For details about the definition and matching
     * rules of implicit Want, see
     * [Matching Rules of Explicit Want and Implicit Want](docroot://application-models/explicit-implicit-want-mappings.md)
     * .
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.app.ability.Want/Want#action
     */
    action?: string;
    /**
     * Want parameters in the form of custom key-value (KV) pairs. By default, the following keys are carried:
     *
     * **ohos.aafwk.param.callerPid**: PID of the caller.
     *
     * **ohos.aafwk.param.callerToken**: token of the caller.
     *
     * **ohos.aafwk.param.callerUid**: UID in [bundleInfo](js-apis-bundle-BundleInfo.md#bundleinfodeprecated), that is,
     * the application UID in the bundle information.
     *
     * - **component.startup.newRules**: whether to enable the new control rule.
     * - **moduleName**: module name of the caller. No matter what this field is set to, the correct module name will be
     * sent to the peer.
     * - **ohos.dlp.params.sandbox**: available only for DLP files.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.app.ability.Want/Want#parameters
     */
    parameters?: {
        [key: string]: any;
    };
    /**
     * Additional category information (such as browser and video player) of the ability. It is a supplement to the
     * **action** field for implicit Want. and is used to filter ability types. For details, see
     * [entity]{@link @ohos.ability.wantConstant:wantConstant.Entity}.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.app.ability.Want/Want#entities
     */
    entities?: Array<string>;
}

```
