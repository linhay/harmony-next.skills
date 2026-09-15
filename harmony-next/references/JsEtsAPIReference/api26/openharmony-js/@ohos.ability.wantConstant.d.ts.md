# @ohos.ability.wantConstant.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2023 Huawei Device Co., Ltd.
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
 * @kit API10LessDeprecatedModules
 */
/**
 * The module provides the actions, entities, and flags used in Want objects.
 *
 * @syscap SystemCapability.Ability.AbilityBase
 * @since 6
 * @deprecated since 9
 * @useinstead ohos.app.ability.wantConstant/wantConstant
 */
declare namespace wantConstant {
    /**
     * Enumerates the action constants of the Want object. **action** specifies the operation to execute.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @since 6
     * @deprecated since 9
     */
    export enum Action {
        /**
         * Action of returning to the home page.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ACTION_HOME = 'ohos.want.action.home',
        /**
         * Action of launching the numeric keypad.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ACTION_DIAL = 'ohos.want.action.dial',
        /**
         * Action of launching the search function.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ACTION_SEARCH = 'ohos.want.action.search',
        /**
         * Action of launching the UI that provides wireless network settings, for example, Wi-Fi options.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ACTION_WIRELESS_SETTINGS = 'ohos.settings.wireless',
        /**
         * Action of launching the UI for managing installed applications.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ACTION_MANAGE_APPLICATIONS_SETTINGS = 'ohos.settings.manage.applications',
        /**
         * Action of launching the UI that displays the details of an application.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ACTION_APPLICATION_DETAILS_SETTINGS = 'ohos.settings.application.details',
        /**
         * Action of launching the UI for setting the alarm clock.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ACTION_SET_ALARM = 'ohos.want.action.setAlarm',
        /**
         * Action of launching the UI that displays all alarms.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ACTION_SHOW_ALARMS = 'ohos.want.action.showAlarms',
        /**
         * Action of launching the UI for snoozing an alarm.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ACTION_SNOOZE_ALARM = 'ohos.want.action.snoozeAlarm',
        /**
         * Action of launching the UI for deleting an alarm.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ACTION_DISMISS_ALARM = 'ohos.want.action.dismissAlarm',
        /**
         * Action of launching the UI for dismissing a timer.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ACTION_DISMISS_TIMER = 'ohos.want.action.dismissTimer',
        /**
         * Action of launching the UI for sending an SMS message.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ACTION_SEND_SMS = 'ohos.want.action.sendSms',
        /**
         * Action of launching the UI for opening a contact or picture.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ACTION_CHOOSE = 'ohos.want.action.choose',
        /**
         * Action of launching the UI for photographing.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 8
         * @deprecated since 9
         */
        ACTION_IMAGE_CAPTURE = 'ohos.want.action.imageCapture',
        /**
         * Action of launching the UI for shooting a video.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 8
         * @deprecated since 9
         */
        ACTION_VIDEO_CAPTURE = 'ohos.want.action.videoCapture',
        /**
         * Action of launching the UI for application selection.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ACTION_SELECT = 'ohos.want.action.select',
        /**
         * Action of launching the UI for sending a single data record.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ACTION_SEND_DATA = 'ohos.want.action.sendData',
        /**
         * Action of launching the UI for sending multiple data records.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ACTION_SEND_MULTIPLE_DATA = 'ohos.want.action.sendMultipleData',
        /**
         * Action of requesting a media scanner to scan a file and add the file to the media library.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ACTION_SCAN_MEDIA_FILE = 'ohos.want.action.scanMediaFile',
        /**
         * Action of viewing data.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ACTION_VIEW_DATA = 'ohos.want.action.viewData',
        /**
         * Action of editing data.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ACTION_EDIT_DATA = 'ohos.want.action.editData',
        /**
         * Action of displaying selection options with an action selector.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        INTENT_PARAMS_INTENT = 'ability.want.params.INTENT',
        /**
         * Title of the character sequence dialog box used with the action selector.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        INTENT_PARAMS_TITLE = 'ability.want.params.TITLE',
        /**
         * Action of selecting a file.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 7
         * @deprecated since 9
         */
        ACTION_FILE_SELECT = 'ohos.action.fileSelect',
        /**
         * URI of the data stream associated with the target when the data is sent. The value must be an array of the string
         *  type.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 7
         * @deprecated since 9
         */
        PARAMS_STREAM = 'ability.params.stream',
        /**
         * Action of providing the OAuth service.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 8
         * @deprecated since 9
         */
        ACTION_APP_ACCOUNT_OAUTH = 'ohos.account.appAccount.action.oauth'
    }
    /**
     * Enumerates the entity constants of the Want object. **entity** specifies additional information of the target
     * ability.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @since 6
     * @deprecated since 9
     */
    export enum Entity {
        /**
         * Default entity. The default entity is used if no entity is specified.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ENTITY_DEFAULT = 'entity.system.default',
        /**
         * Home screen entity.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ENTITY_HOME = 'entity.system.home',
        /**
         * Voice interaction entity.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ENTITY_VOICE = 'entity.system.voice',
        /**
         * Browser type entity.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ENTITY_BROWSABLE = 'entity.system.browsable',
        /**
         * Video type entity.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        ENTITY_VIDEO = 'entity.system.video'
    }
    /**
     * Enumerates the flags that specify how the Want will be handled.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @since 6
     * @deprecated since 9
     * @useinstead ohos.app.ability.wantConstant/wantConstant#Flags
     */
    export enum Flags {
        /**
         * Grants the permission to read the URI.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.app.ability.wantConstant/wantConstant.Flags#FLAG_AUTH_READ_URI_PERMISSION
         */
        FLAG_AUTH_READ_URI_PERMISSION = 0x00000001,
        /**
         * Grants the permission to write data to the URI.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.app.ability.wantConstant/wantConstant.Flags#FLAG_AUTH_WRITE_URI_PERMISSION
         */
        FLAG_AUTH_WRITE_URI_PERMISSION = 0x00000002,
        /**
         * Returns the result to the ability.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        FLAG_ABILITY_FORWARD_RESULT = 0x00000004,
        /**
         * Indicates whether the ability on the local device can be continued on a remote device.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        FLAG_ABILITY_CONTINUATION = 0x00000008,
        /**
         * Indicates that a component does not belong to OHOS.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        FLAG_NOT_OHOS_COMPONENT = 0x00000010,
        /**
         * Indicates that an ability is enabled.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        FLAG_ABILITY_FORM_ENABLED = 0x00000020,
        /**
         * Indicates the support for cross-device startup in the distributed scheduler.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        FLAG_ABILITYSLICE_MULTI_DEVICE = 0x00000100,
        /**
         * Indicates that the ServiceAbility is started regardless of whether the host application has been started.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        FLAG_START_FOREGROUND_ABILITY = 0x00000200,
        /**
         * Indicates that the specific ability will be installed if it has not been installed.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.app.ability.wantConstant/wantConstant.Flags#FLAG_INSTALL_ON_DEMAND
         */
        FLAG_INSTALL_ON_DEMAND = 0x00000800,
        /**
         * Indicates that the specific ability will be installed in the background if it has not been installed.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        FLAG_INSTALL_WITH_BACKGROUND_MODE = 0x80000000,
        /**
         * Clears other operation missions. This flag can be set for the Want passed in
         * [startAbility]{@link @ohos.ability.featureAbility:featureAbility.startAbility(parameter: StartAbilityParameter, callback: AsyncCallback<number>)}
         * . It must be used together with **FLAG_ABILITY_NEW_MISSION**.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        FLAG_ABILITY_CLEAR_MISSION = 0x00008000,
        /**
         * Creates a mission on the history mission stack.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        FLAG_ABILITY_NEW_MISSION = 0x10000000,
        /**
         * Reuses an ability instance if it is on the top of an existing mission stack; creates an ability instance
         * otherwise.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 6
         * @deprecated since 9
         */
        FLAG_ABILITY_MISSION_TOP = 0x20000000
    }
}
export default wantConstant;

```
