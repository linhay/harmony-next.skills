# @ohos.app.form.formInfo.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2026 Huawei Device Co., Ltd.
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
 * @kit FormKit
 */
import Want from './@ohos.app.ability.Want';
/**
 * The **formInfo** module provides types and enums related to the widget information and state.
 *
 * > **NOTE**
 *
 * > - This topic describes only system APIs provided by the module. For details about its public APIs, see
 * > [@ohos.app.form.formInfo (formInfo)]{@link @ohos.app.form.formInfo:formInfo}.
 *
 * @syscap SystemCapability.Ability.Form
 * @atomicservice [since 11]
 * @since 9
 */
declare namespace formInfo {
    /**
     * Provides information about a form.
     *
     * @typedef FormInfo
     * @syscap SystemCapability.Ability.Form
     * @atomicservice [since 11]
     * @since 9
     */
    interface FormInfo {
        /**
         * Obtains the bundle name of the application to which this form belongs.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        bundleName: string;
        /**
         * Obtains the name of the application module to which this form belongs.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        moduleName: string;
        /**
         * Obtains the class name of the ability to which this form belongs.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        abilityName: string;
        /**
         * Obtains the name of this form.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        name: string;
        /**
         * Obtains the display name of this form.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 11
         */
        displayName: string;
        /**
         * Obtains the displayName resource id of this form.
         * The value must be a positive integer.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 11
         */
        displayNameId: number;
        /**
         * Obtains the description of this form.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        description: string;
        /**
         * Obtains the description id of this form.
         * The value must be a positive integer.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 10
         */
        descriptionId: number;
        /**
         * Obtains the type of this form. Currently, JS forms are supported.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        type: FormType;
        /**
         * Obtains the JS component name of this JS form.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        jsComponentName: string;
        /**
         * Obtains the color mode of this form.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 20
         */
        colorMode: ColorMode;
        /**
         * Checks whether this form is a default form.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        isDefault: boolean;
        /**
         * Obtains the updateEnabled.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        updateEnabled: boolean;
        /**
         * Obtains whether notify visible of this form.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        formVisibleNotify: boolean;
        /**
         * Obtains the scheduledUpdateTime.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        scheduledUpdateTime: string;
        /**
         * Obtains the form config ability about this form.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        formConfigAbility: string;
        /**
         * Obtains the updateDuration.
         * The value must be an integer within [0,336].
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        updateDuration: number;
        /**
         * Obtains the default grid style of this form.
         * The value must be a positive integer, refer to {@link formInfo.FormDimension}.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        defaultDimension: number;
        /**
         * Obtains the grid styles supported by this form.
         * The minimum length is 1, refer to {@link formInfo.FormDimension}.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        supportDimensions: Array<number>;
        /**
         * Obtains the custom data defined in this form.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        customizeData: Record<string, string>;
        /**
         * Obtains whether this form is a dynamic form.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 10
         */
        isDynamic: boolean;
        /**
         * Indicates whether the form can be set as a transparent background
         *
         * @default false
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 11
         */
        transparencyEnabled: boolean;
        /**
         * Obtains the shape supported by this form.
         * The minimum length is 1, refer to {@link formInfo.FormShape}.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 12
         */
        supportedShapes: Array<number>;
    }
    /**
     * Type of form.
     *
     * @syscap SystemCapability.Ability.Form
     * @atomicservice [since 11]
     * @since 9
     */
    enum FormType {
        /**
         * JS form.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        JS = 1,
        /**
         * eTS form.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        eTS = 2
    }
    /**
     * Color mode.
     *
     * @syscap SystemCapability.Ability.Form
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 20
     */
    enum ColorMode {
        /**
         * Automatic mode.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 20
         */
        MODE_AUTO = -1,
        /**
         * Dark mode.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 20
         */
        MODE_DARK = 0,
        /**
         * Light mode.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 20
         */
        MODE_LIGHT = 1
    }
    /**
     * Provides state information about a form.
     *
     * @typedef FormStateInfo
     * @syscap SystemCapability.Ability.Form
     * @atomicservice [since 11]
     * @since 9
     */
    interface FormStateInfo {
        /**
         * Obtains the form state.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        formState: FormState;
        /**
         * Obtains the want form .
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        want: Want;
    }
    /**
     * Provides state about a form.
     *
     * @syscap SystemCapability.Ability.Form
     * @atomicservice [since 11]
     * @since 9
     */
    enum FormState {
        /**
         * Indicates that the form status is unknown due to an internal error.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        UNKNOWN = -1,
        /**
         * Indicates that the form is in the default state.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        DEFAULT = 0,
        /**
         * Indicates that the form is ready.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        READY = 1
    }
    /**
     * Form update reason.
     *
     * @syscap SystemCapability.Ability.Form
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    enum FormUpdateReason {
        /**
         * The reason for the form update is unknown.
         *
         * @syscap SystemCapability.Ability.Form
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        UNKNOWN = -1,
        /**
         * The reason for the form update is node reuse.
         *
         * @syscap SystemCapability.Ability.Form
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        FORM_NODE_REUSE = 0
    }
    /**
     * Enumerates widget parameters.
     *
     * @syscap SystemCapability.Ability.Form
     * @atomicservice [since 11]
     * @since 9
     */
    enum FormParam {
        /**
         * Indicates the key specifying the ID of the form to be obtained, which is represented as
         * want: {
         *   "parameters": {
         *       IDENTITY_KEY: "119476135"
         *    }
         * }.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        IDENTITY_KEY = "ohos.extra.param.key.form_identity",
        /**
         * Indicates the key specifying the grid style of the form to be obtained, which is represented as
         * want: {
         *   "parameters": {
         *       DIMENSION_KEY: FormDimension.Dimension_1_2
         *    }
         * }.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        DIMENSION_KEY = "ohos.extra.param.key.form_dimension",
        /**
         * Indicates the key specifying the name of the form to be obtained, which is represented as
         * want: {
         *   "parameters": {
         *       NAME_KEY: "formName"
         *    }
         * }.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        NAME_KEY = "ohos.extra.param.key.form_name",
        /**
         * Indicates the key specifying the name of the module to which the form to be obtained belongs, which is
         * represented as
         * want: {
         *   "parameters": {
         *       MODULE_NAME_KEY: "formEntry"
         *    }
         * }.
         * This constant is mandatory.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        MODULE_NAME_KEY = "ohos.extra.param.key.module_name",
        /**
         * Indicates the key specifying the width of the form to be obtained, which is represented as
         * want: {
         *   "parameters": {
         *       WIDTH_KEY: 800
         *    }
         * }.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        WIDTH_KEY = "ohos.extra.param.key.form_width",
        /**
         * Indicates the key specifying the height of the form to be obtained, which is represented as
         * want: {
         *   "parameters": {
         *       HEIGHT_KEY: 400
         *    }
         * }.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        HEIGHT_KEY = "ohos.extra.param.key.form_height",
        /**
         * Indicates the key specifying whether a form is temporary, which is represented as
         * want: {
         *   "parameters": {
         *       TEMPORARY_KEY: true
         *    }
         * }.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        TEMPORARY_KEY = "ohos.extra.param.key.form_temporary",
        /**
         * Indicates the key specifying the name of the bundle to be obtained, which is represented as
         * want: {
         *   "parameters": {
         *       BUNDLE_NAME_KEY: "bundleName"
         *    }
         * }.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        BUNDLE_NAME_KEY = "ohos.extra.param.key.bundle_name",
        /**
         * Indicates the key specifying the name of the ability to be obtained, which is represented as
         * want: {
         *   "parameters": {
         *       ABILITY_NAME_KEY: "abilityName"
         *    }
         * }.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        ABILITY_NAME_KEY = "ohos.extra.param.key.ability_name",
        /**
         * Indicates the key specifying the launch reason of the form to be obtained, which is represented as
         * want: {
         *   "parameters": {
         *       LAUNCH_REASON_KEY: LaunchReason.FORM_DEFAULT
         *    }
         * }.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 10
         */
        LAUNCH_REASON_KEY = "ohos.extra.param.key.form_launch_reason",
        /**
         * Indicates the key specifying the custom data of the form to be obtained, which is represented as
         * want: {
         *   "parameters": {
         *       PARAM_FORM_CUSTOMIZE_KEY: {
         *          "key": "userData"
         *       }
         *    }
         * }.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 10
         */
        PARAM_FORM_CUSTOMIZE_KEY = "ohos.extra.param.key.form_customize",
        /**
         * Indicates the key specifying the form location, which is represented as
         * want: {
         *   "parameters": {
         *       FORM_LOCATION_KEY: FormLocation.DESKTOP
         *    }
         * }.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 12
         */
        FORM_LOCATION_KEY = 'ohos.extra.param.key.form_location',
        /**
         * Indicates the key specifying the form rendering mode, which is represented as
         * want: {
         *   "parameters": {
         *       FORM_RENDERING_MODE_KEY: FormRenderingMode.SINGLE_COLOR
         *    }
         * }.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 12]
         * @since 11
         */
        FORM_RENDERING_MODE_KEY = 'ohos.extra.param.key.form_rendering_mode',
        /**
         * Indicates the key specifying the inverse of the host background color, which is represented as
         * want: {
         *   "parameters": {
         *       HOST_BG_INVERSE_COLOR_KEY: "#FF000000"
         *    }
         * }.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 12
         */
        HOST_BG_INVERSE_COLOR_KEY = 'ohos.extra.param.key.host_bg_inverse_color',
        /**
         * Indicates the key specifying the user granted permission name, which is represented as
         * want: {
         *   "parameters": {
         *       FORM_PERMISSION_NAME_KEY: "permissionName"
         *    }
         * }.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 12
         */
        FORM_PERMISSION_NAME_KEY = 'ohos.extra.param.key.permission_name',
        /**
         * Indicates the key specifying whether the user granted, which is represented as
         * want: {
         *   "parameters": {
         *       FORM_PERMISSION_GRANTED_KEY: true
         *    }
         * }.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 12
         */
        FORM_PERMISSION_GRANTED_KEY = 'ohos.extra.param.key.permission_granted',
        /**
         * Indicates the key specifying the original form id, used in conjunction with LaunchReason.FORM_SIZE_CHANGE.
         * which is represented as
         * want: {
         *   "parameters": {
         *       ORIGINAL_FORM_KEY: "119476135"
         *    }
         * }.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        ORIGINAL_FORM_KEY = 'ohos.extra.param.key.original_form_id',
        /**
         * Indicates the key specifying the edit form id, used in conjunction with LaunchReason.FORM_EDIT_PREVIEW.
         * which is represented as
         * want: {
         *   "parameters": {
         *       EDIT_FORM_KEY: "119476135"
         *    }
         * }.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 22
         */
        EDIT_FORM_KEY = 'ohos.extra.param.key.edit_form_id',
        /**
         * Indicates the key specifying the reason for the form update.
         * which is represented as
         * want: {
         *   "parameters": {
         *       UPDATE_FORM_REASON_KEY: FormUpdateReason.FORM_NODE_REUSE
         *    }
         * }.
         *
         * @syscap SystemCapability.Ability.Form
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        UPDATE_FORM_REASON_KEY = 'ohos.extra.param.key.update_form_reason'
    }
    /**
     * The optional options used as filters to ask
     * getFormsInfo to return formInfos from only forms that match the options.
     *
     * @typedef FormInfoFilter
     * @syscap SystemCapability.Ability.Form
     * @atomicservice [since 11]
     * @since 9
     */
    interface FormInfoFilter {
        /**
         * optional moduleName that used to ask getFormsInfo to return
         * form infos with the same moduleName.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        moduleName?: string;
    }
    /**
     * Defines the FormDimension enum.
     *
     * @syscap SystemCapability.Ability.Form
     * @atomicservice [since 11]
     * @since 9
     */
    enum FormDimension {
        /**
         * 1 x 2 form
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        Dimension_1_2 = 1,
        /**
         * 2 x 2 form
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        Dimension_2_2 = 2,
        /**
         * 2 x 4 form
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        Dimension_2_4 = 3,
        /**
         * 4 x 4 form
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        Dimension_4_4 = 4,
        /**
         * 2 x 1 form
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 20
         */
        Dimension_2_1,
        /**
         * 1 x 1 form
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 11
         */
        DIMENSION_1_1 = 6,
        /**
         * 6 x 4 form
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 12
         */
        DIMENSION_6_4 = 7,
        /**
         * 2 x 3 form used for wearable devices
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 18
         */
        DIMENSION_2_3 = 8,
        /**
         * 3 x 3 form used for wearable devices
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 18
         */
        DIMENSION_3_3 = 9
    }
    /**
     * Defines the FormShape enum.
     *
     * @syscap SystemCapability.Ability.Form
     * @atomicservice
     * @since 12
     */
    enum FormShape {
        /**
         * The rect shape.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 12
         */
        RECT = 1,
        /**
         * The circle shape.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 12
         */
        CIRCLE = 2
    }
    /**
     * The visibility of a form.
     *
     * @syscap SystemCapability.Ability.Form
     * @atomicservice [since 11]
     * @since 9
     */
    enum VisibilityType {
        /**
         * Indicates the type of the form type is unknown.
         * Often used as a condition variable in function OnVisibilityChange to specify actions only on forms that are
         * changing to unknown.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 10
         */
        UNKNOWN = 0,
        /**
         * Indicates the type of the form is visible.
         * Often used as a condition variable in function OnVisibilityChange to specify actions only on forms that are
         * changing to visible.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        FORM_VISIBLE = 1,
        /**
         * Indicates the type of the form is invisible.
         * Often used as a condition variable in function OnVisibilityChange to specify actions only on forms that are
         * changing to invisible.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        FORM_INVISIBLE = 2
    }
    /**
     * Indicates the launch reason of a form.
     *
     * @syscap SystemCapability.Ability.Form
     * @atomicservice [since 11]
     * @since 10
     */
    enum LaunchReason {
        /**
         * Indicates the launch reason of a form is default.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 10
         */
        FORM_DEFAULT = 1,
        /**
         * Indicates the launch reason of a form is share.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 10
         */
        FORM_SHARE = 2,
        /**
         * Indicates the launch reason of a form is change size.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        FORM_SIZE_CHANGE = 3
    }
    /**
     * The class of a running form information.
     *
     * @typedef RunningFormInfo
     * @syscap SystemCapability.Ability.Form
     * @atomicservice
     * @since 20
     */
    interface RunningFormInfo {
        /**
         * Obtains the id of the this form.
         *
         * @default -
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        readonly formId: string;
        /**
         * Obtains the bundle name of the application to which this form belongs.
         *
         * @default -
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        readonly bundleName: string;
        /**
         * The location of this form.
         *
         * @default -
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        readonly formLocation: FormLocation;
        /**
         * Obtains the name of the application module to which this form belongs.
         *
         * @default -
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        readonly moduleName: string;
        /**
         * Obtains the class name of the ability to which this form belongs.
         *
         * @default -
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        readonly abilityName: string;
        /**
         * Obtains the name of this form.
         *
         * @default -
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        readonly formName: string;
        /**
         * Obtains the grid style of this form.
         * The value must be a positive integer, refer to {@link formInfo.FormDimension}.
         *
         * @default -
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        readonly dimension: number;
    }
    /**
     * Enumerates the widget locations.
     *
     * @syscap SystemCapability.Ability.Form
     * @atomicservice
     * @since 20
     */
    enum FormLocation {
        /**
         * The widget is located on the home screen.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        DESKTOP = 0,
        /**
         * The widget is located in the widget center of the home screen.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        FORM_CENTER = 1,
        /**
         * The widget is located in the widget manager of the home screen.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        FORM_MANAGER = 2,
        /**
         * The widget is located on the minus 1 screen.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        NEGATIVE_SCREEN = 3,
        /**
         * The widget is located on the locked screen.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        SCREEN_LOCK = 6,
        /**
         * The widget is located in the area of AI Suggestions.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        AI_SUGGESTION = 7,
        /**
         * The widget is located on landscape standby screen.
         *
         * @syscap SystemCapability.Ability.Form
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        STANDBY = 8
    }
    /**
     * Provides OverflowInfo about funInteraction or sceneAnimation form
     *
     * @typedef { OverflowInfo }
     * @syscap SystemCapability.Ability.Form
     * @atomicservice
     * @since 20
     */
    interface OverflowInfo {
        /**
         * The overflow animation area
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        area: Rect;
        /**
         * The overflow animation duration, unit is ms
         * Unit: milliseconds, The value must be an integer within [0,3500].
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        duration: number;
        /**
         * Whether use default animation, default is true
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        useDefaultAnimation?: boolean;
    }
    /**
     * Indicates rectangle, unit is vp.
     *
     * @typedef Rect
     * @syscap SystemCapability.Ability.Form
     * @atomicservice
     * @since 20
     */
    interface Rect {
        /**
         * The left position of Rect
         * Unit: vp.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        left: number;
        /**
         * The top position of Rect
         * Unit: vp.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        top: number;
        /**
         * The width of Rect
         * Unit: vp.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        width: number;
        /**
         * The height of Rect
         * Unit: vp.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice
         * @since 20
         */
        height: number;
    }
}
export default formInfo;

```
