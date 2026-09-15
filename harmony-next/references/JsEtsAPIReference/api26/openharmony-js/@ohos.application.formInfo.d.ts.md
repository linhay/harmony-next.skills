# @ohos.application.formInfo.d.ts

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
 * @kit API10LessDeprecatedModules
 */
import Want from './@ohos.app.ability.Want';
/**
 * The **formInfo** module provides types and enums related to the widget information and state.
 *
 * > **NOTE**
 *
 * > - This module is deprecated since API version 9. You are advised to use
 * > [formInfo]{@link @ohos.app.form.formInfo:formInfo} instead.
 *
 * @syscap SystemCapability.Ability.Form
 * @since 8
 * @deprecated since 9
 * @useinstead ohos.app.form.formInfo/formInfo
 */
declare namespace formInfo {
    /**
     * Widget information.
     *
     * @syscap SystemCapability.Ability.Form
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.app.form.formInfo/formInfo#FormInfo
     */
    interface FormInfo {
        /**
         * Name of the bundle to which the widget belongs.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormInfo#bundleName
         */
        bundleName: string;
        /**
         * Name of the module to which the widget belongs.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormInfo#moduleName
         */
        moduleName: string;
        /**
         * Name of the ability to which the widget belongs.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormInfo#abilityName
         */
        abilityName: string;
        /**
         * Widget name.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormInfo#name
         */
        name: string;
        /**
         * Description of the widget.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormInfo#description
         */
        description: string;
        /**
         * Type of the widget. Currently, only JS widgets are supported.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormInfo#type
         */
        type: FormType;
        /**
         * Component name of the JS widget.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormInfo#jsComponentName
         */
        jsComponentName: string;
        /**
         * Color mode of the widget.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormInfo#colorMode
         */
        colorMode: ColorMode;
        /**
         * Whether the widget is the default one.
         *
         * - **true**: The widget is the default one.
         * - **false**: The widget is not the default one.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormInfo#isDefault
         */
        isDefault: boolean;
        /**
         * Whether the widget is updatable.
         *
         * - **true**: The widget can be updated periodically.
         * - **false**: The widget cannot be updated periodically.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormInfo#updateEnabled
         */
        updateEnabled: boolean;
        /**
         * Whether to send a notification when the widget is visible.
         *
         * - **true**: The widget provider is notified of the status change.
         * - **false**: The widget provider is not notified of the status change.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormInfo#formVisibleNotify
         */
        formVisibleNotify: boolean;
        /**
         * Name of the associated bundle to which the widget belongs.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         */
        relatedBundleName: string;
        /**
         * Time when the widget was updated.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormInfo#scheduledUpdateTime
         */
        scheduledUpdateTime: string;
        /**
         * Configuration ability of the widget.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormInfo#formConfigAbility
         */
        formConfigAbility: string;
        /**
         * Update period of the widget.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormInfo#updateDuration
         */
        updateDuration: number;
        /**
         * Default dimension of the widget.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormInfo#defaultDimension
         */
        defaultDimension: number;
        /**
         * Dimensions supported by the widget.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormInfo#supportDimensions
         */
        supportDimensions: Array<number>;
        /**
         * Custom data of the widget.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormInfo#customizeData
         */
        customizeData: {
            [key: string]: [
                value: string
            ];
        };
    }
    /**
     * Enumerates the widget types.
     *
     * @syscap SystemCapability.Ability.Form
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.app.form.formInfo/formInfo#FormType
     */
    enum FormType {
        /**
         * JS widget.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormType#JS
         */
        JS = 1
    }
    /**
     * Enumerates the color modes supported by the widget.
     *
     * @syscap SystemCapability.Ability.Form
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.app.form.formInfo/formInfo#ColorMode
     */
    enum ColorMode {
        /**
         * Auto mode.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.ColorMode#MODE_AUTO
         */
        MODE_AUTO = -1,
        /**
         * Dark mode.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.ColorMode#MODE_DARK
         */
        MODE_DARK = 0,
        /**
         * Light mode.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.ColorMode#MODE_LIGHT
         */
        MODE_LIGHT = 1
    }
    /**
     * Describes the widget state information.
     *
     * @syscap SystemCapability.Ability.Form
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.app.form.formInfo/formInfo#FormStateInfo
     */
    interface FormStateInfo {
        /**
         * Widget state.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormStateInfo#formState
         */
        formState: FormState;
        /**
         * Want text.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormStateInfo#want
         */
        want: Want;
    }
    /**
     * Enumerates the widget states.
     *
     * @syscap SystemCapability.Ability.Form
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.app.form.formInfo/formInfo#FormState
     */
    enum FormState {
        /**
         * Unknown state.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormState#UNKNOWN
         */
        UNKNOWN = -1,
        /**
         * Default state.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormState#DEFAULT
         */
        DEFAULT = 0,
        /**
         * Ready state.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormState#READY
         */
        READY = 1
    }
    /**
     * Enumerates the widget parameters.
     *
     * @syscap SystemCapability.Ability.Form
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.app.form.formInfo/formInfo#FormParam
     */
    enum FormParam {
        /**
         * Widget dimension.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormParam#DIMENSION_KEY
         */
        DIMENSION_KEY = 'ohos.extra.param.key.form_dimension',
        /**
         * Widget name.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormParam#NAME_KEY
         */
        NAME_KEY = 'ohos.extra.param.key.form_name',
        /**
         * Name of the module to which the widget belongs.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormParam#MODULE_NAME_KEY
         */
        MODULE_NAME_KEY = 'ohos.extra.param.key.module_name',
        /**
         * Widget width.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormParam#WIDTH_KEY
         */
        WIDTH_KEY = 'ohos.extra.param.key.form_width',
        /**
         * Widget height.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormParam#HEIGHT_KEY
         */
        HEIGHT_KEY = 'ohos.extra.param.key.form_height',
        /**
         * Temporary widget.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.form.formInfo/formInfo.FormParam#TEMPORARY_KEY
         */
        TEMPORARY_KEY = 'ohos.extra.param.key.form_temporary'
    }
}
export default formInfo;

```
