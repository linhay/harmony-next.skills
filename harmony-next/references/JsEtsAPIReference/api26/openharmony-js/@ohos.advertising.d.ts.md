# @ohos.advertising.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023-2026 Huawei Device Co., Ltd.
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
 * @file Ads Service Framework
 * @kit AdsKit
 */
import type web_webview from './@ohos.web.webview';
import type common from './@ohos.app.ability.common';
import type { Advertisement as _Advertisement } from './advertising/advertisement';
/**
 * The advertising module provides APIs for requesting and displaying ads.
 *
 * > **NOTE**
 * > The initial APIs of this module are supported since API version 11.
 * > Newly added APIs will be marked with a superscript to indicate their earliest API version.
 *
 * @syscap SystemCapability.Advertising.Ads
 * @atomicservice [since 12]
 * @since 11
 */
declare namespace advertising {
    /**
     * Defines the requested ad content.
     *
     * @syscap SystemCapability.Advertising.Ads
     * @atomicservice [since 12]
     * @since 11
     */
    export type Advertisement = _Advertisement;
    /**
     * Defines the ad request parameters.
     *
     * @syscap SystemCapability.Advertising.Ads
     * @atomicservice [since 12]
     * @since 11
     */
    export interface AdRequestParams {
        /**
         * Ad slot ID.
         *
         * Note: The getAdRequestBody API can omit this parameter.
         *
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        adId: string;
        /**
         * Requested ad type.
         *
         * - 1: Splash ad.
         * - 3: Native ad.
         * - 7: Rewarded ad.
         * - 8: Banner ad.
         * - 12: Interstitial ad
         * - 60: Roll ad.
         *
         * If not set, the default is the native ad type.
         *
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        adType?: number;
        /**
         * Number of ads requested. If not set, the business logic prevails.
         *
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        adCount?: number;
        /**
         * Expected creative width when requesting an ad, in vp (mandatory for banner ads).
         * If not set, the business logic prevails.
         *
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        adWidth?: number;
        /**
         * Expected creative height when requesting an ad,
         * in vp (mandatory for banner ads). If not set, the business logic prevails.
         *
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        adHeight?: number;
        /**
         * Ad keyword. Defaults to "" if not set.
         *
         * Note: Not supported for use currently.
         *
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        adSearchKeyword?: string;
        /**
         * Custom parameter.
         *
         * <!--RP2--><!--RP2End-->
         *
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        [key: string]: number | boolean | string | undefined;
    }
    /**
     * Defines the ad configuration.
     *
     * @syscap SystemCapability.Advertising.Ads
     * @atomicservice [since 12]
     * @since 11
     */
    export interface AdOptions {
        /**
         * Whether you want your content to be treated as child-directed for purposes of COPPA.
         *
         * -1: Default value, unspecified.
         * 0: No.
         * 1: Yes.
         *
         * The default value is -1.
         *
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        tagForChildProtection?: number;
        /**
         * Sets the maximum ad content rating.
         *
         * W: ages 3+, all audiences.
         * PI: ages 7+, parental guidance.
         * J: ages 12+, teen.
         * A: ages 16+/18+, adult audience.
         *
         * If not set, the business logic prevails.
         *
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        adContentClassification?: string;
        /**
         * Sets whether to request only non-personalized ads.
         *
         * 0: Request both personalized and non-personalized ads.
         * 1: Request only non-personalized ads.
         *
         * If not set, the business logic prevails.
         *
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        nonPersonalizedAd?: number;
        /**
         * Custom parameters.
         *
         * <!--RP1--><!--RP1End-->
         *
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        [key: string]: number | boolean | string | undefined;
    }
    /**
     * Defines the ad display parameters.
     *
     * @syscap SystemCapability.Advertising.Ads
     * @atomicservice [since 12]
     * @since 11
     */
    export interface AdDisplayOptions {
        /**
         * Media custom data. Used for the server to notify the media server
         * that a user should be rewarded for interacting with a rewarded video ad,
         * thereby preventing fraudulent behavior (no notification will be sent if not set).
         *
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        customData?: string;
        /**
         * Media custom user ID.
         * Used for the server to notify the media server that
         * a user should be rewarded for interacting with a rewarded video ad,
         * thereby preventing fraudulent behavior (no notification will be sent if not set).
         *
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        userId?: string;
        /**
         * Whether to display a pop-up notification to the user when using mobile data
         * to play videos or download apps.
         *
         * - true: Display pop-up notification.
         * - false: Do not display pop-up notification.
         * - This parameter depends on the traffic pop-up feature,
         * which currently does not support full functionality,
         * so the default value is temporarily uncertain.
         *
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        useMobileDataReminder?: boolean;
        /**
         * Whether to mute the ad video playback.
         *
         * - true: Mute playback.
         * - false: Non-mute playback.
         *
         * If not set, the business logic prevails.
         *
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        mute?: boolean;
        /**
         * Scenario type for obtaining audio focus during video playback.
         *
         * - 0: Obtain focus during both muted and non-muted video playback.
         * - 1: Do not obtain focus during muted video playback.
         * - 2: Do not obtain focus during either muted or non-muted video playback.
         * - The related features that this API depends on are currently not supported for use,
         * so the default value is temporarily uncertain.
         *
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        audioFocusType?: number;
        /**
         * Custom parameter.
         *
         * - refreshTime: An optional custom parameter for the AutoAdComponent,
         * used to control the ad rotation interval. Type number, unit: ms, value range [30000, 120000].
         * If not set or the value is non-numeric or less than or equal to 0, no rotation occurs,
         * and only the first ad content in the ad response is displayed. Values less than 30000 are set to 30000,
         * and values greater than 120000 are set to 120000.
         *
         * <!--RP3--><!--RP3End-->
         *
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        [key: string]: number | boolean | string | undefined;
    }
    /**
     * Defines the ad status change callback.
     *
     * @syscap SystemCapability.Advertising.Ads
     * @atomicservice [since 12]
     * @since 11
     */
    export interface AdInteractionListener {
        /**
         * Called when the ad display status changes.
         *
         * @param { string } status - Ad show status.
         *     - onAdLoad: Ad loaded successfully.
         *     - onAdFail: Ad failed to load.
         *     - onAdOpen: Ad opened.
         *     - onAdClick: Ad clicked.
         *     - onAdClose: Ad closed.
         *     - onMediaProgress: Ad playback progress.
         *     - onMediaStart: Ad playback started.
         *     - onMediaPause: Ad playback paused.
         *     - onMediaStop: Ad playback stopped.
         *     - onMediaComplete: Ad playback completed.
         *     - onMediaCountDown: Ad countdown.
         *     - onMediaError: Ad playback failed.
         *     - onLandscape: Full-screen button clicked in portrait mode.
         *     - onPortrait: Back button clicked in full-screen mode.
         *     - onBackClicked: Back button clicked.
         *     - onAdSubWindow: Sheet opened.
         * @param { Advertisement } ad - Content of the ad.
         * @param { string } data - Extended information.
         *     When **status** is **onAdClose**,
         *     the data value is the close reason, described as follows:
         *     - adShowEnded: Ad show ended.
         *     - adCloseBtnClicked: Close button clicked.
         *     - adSkipBtnClicked: Skip button clicked.
         *     - adFeedbackClosed: The ad is closed due to negative feedback.
         *     - adBackgroundClosed: The splash ad is closed when the app switches to the background.
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        onStatusChanged(status: string, ad: Advertisement, data: string);
    }
    /**
     * Enumerates the callbacks used for the request for loading an ad.
     *
     * @syscap SystemCapability.Advertising.Ads
     * @atomicservice [since 12]
     * @since 11
     */
    export interface AdLoadListener {
        /**
         * Called when an ad request fails.
         *
         * @param { number } errorCode - Error code for the ad request failure.
         * @param { string } errorMsg - Error message for the ad request failure.
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        onAdLoadFailure(errorCode: number, errorMsg: string): void;
        /**
         * Called when an ad request is successful.
         *
         * @param { Array<Advertisement> } ads - Ad data.
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        onAdLoadSuccess(ads: Array<Advertisement>): void;
    }
    /**
     * Enumerates the callbacks used for the request for loading multiple ads.
     *
     * @syscap SystemCapability.Advertising.Ads
     * @atomicservice [since 12]
     * @since 11
     */
    export interface MultiSlotsAdLoadListener {
        /**
         * Called when an ad request fails.
         *
         * @param { number } errorCode - Error code for the ad request failure.
         * @param { string } errorMsg - Error message for the ad request failure.
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        onAdLoadFailure(errorCode: number, errorMsg: string): void;
        /**
         * Called when a request for loading multiple ads is successful.
         *
         * @param { Map<string, Array<Advertisement>> } adsMap - Ad data, which is a mapping set that
         *     uses ad slot IDs as keys to store the requested ad content.
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        onAdLoadSuccess(adsMap: Map<string, Array<Advertisement>>): void;
    }
    /**
     * Shows a full-screen ad.
     *
     * @param { Advertisement } ad - Ad object.
     * @param { AdDisplayOptions } options - Ad display parameters.
     * @param { common.UIAbilityContext } context - Context of the UIAbility. If not set, it is obtained from the api:
     *     [@ohos.app.ability.common](https://developer.huawei.com/consumer/en/doc/harmonyos-references/
     *     js-apis-app-ability-common). [since 11 - 11]
     * @param { common.UIAbilityContext } [context] - Context of the UIAbility. If this parameter is not set, the value is
     *     obtained from @ohos.app.ability.common. [since 12]
     * @throws { BusinessError } 401 - Invalid input parameter. Possible causes: 1. Mandatory parameters are left
     *     unspecified.
     * @throws { BusinessError } 21800001 - System internal error.
     * @throws { BusinessError } 21800004 - Failed to display the ad.
     * @syscap SystemCapability.Advertising.Ads
     * @atomicservice [since 12]
     * @since 11
     */
    function showAd(ad: Advertisement, options: AdDisplayOptions, context?: common.UIAbilityContext): void;
    /**
     * Provides the APIs for loading ads.
     *
     * @syscap SystemCapability.Advertising.Ads
     * @atomicservice [since 12]
     * @since 11
     */
    export class AdLoader {
        /**
         * Constructor.
         *
         * @param { common.Context } context - Context of the ability or application.
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        constructor(context: common.Context);
        /**
         * Loads an ad.
         *
         * @param { AdRequestParams } adParam - Ad request parameters.
         * @param { AdOptions } adOptions - Ad configuration parameters.
         * @param { AdLoadListener } listener - Callback listener for ad requests.
         * @throws { BusinessError } 401 - Invalid input parameter. Possible causes: 1. Mandatory parameters are left
         *     unspecified.2. Incorrect parameter types. 3.Parameter verification failed
         * @throws { BusinessError } 21800001 - System internal error.
         * @throws { BusinessError } 21800003 - Failed to load the ad request.
         * @throws { BusinessError } 801 - Device not supported. [since 12]
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        loadAd(adParam: AdRequestParams, adOptions: AdOptions, listener: AdLoadListener): void;
        /**
         * Loads multiple ads.
         *
         * @param { AdRequestParams[] } adParams - Ad request parameters.
         * @param { AdOptions } adOptions - Ad configuration parameters.
         * @param { MultiSlotsAdLoadListener } listener - Callback listener for ad requests.
         * @throws { BusinessError } 401 - Invalid input parameter. Possible causes: 1. Mandatory parameters are left
         *     unspecified.2. Incorrect parameter types. 3.Parameter verification failed
         * @throws { BusinessError } 21800001 - System internal error.
         * @throws { BusinessError } 21800003 - Failed to load the ad request.
         * @throws { BusinessError } 801 - Device not supported. [since 12]
         * @syscap SystemCapability.Advertising.Ads
         * @atomicservice [since 12]
         * @since 11
         */
        loadAdWithMultiSlots(adParams: AdRequestParams[], adOptions: AdOptions, listener: MultiSlotsAdLoadListener): void;
    }
    /**
     * Obtains the body of an ad request. This API uses a promise to return the result
     * (this API is only open to some pre-installed system applications).
     *
     * @param { AdRequestParams[] } adParams - Ad request parameters.
     *     **Note:** The **adId** parameter of this API can be empty.
     * @param { AdOptions } adOptions - Ad configuration parameters.
     * @returns { Promise<string> } Promise used to return the ad data of the string type.
     * @throws { BusinessError } 401 - Invalid input parameter. Possible causes: 1. Mandatory parameters are
     *     left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Device not supported.
     * @throws { BusinessError } 21800001 - System internal error.
     * @syscap SystemCapability.Advertising.Ads
     * @since 12
     */
    function getAdRequestBody(adParams: AdRequestParams[], adOptions: AdOptions): Promise<string>;
    /**
     * Parses and processes the body of an ad response
     * (this API is only open to some pre-installed system applications).
     *
     * @param { string } adResponse - Ad response body.
     * @param { MultiSlotsAdLoadListener } listener - Callback listener for ad requests.
     * @param { common.UIAbilityContext } context - Context of the UIAbility.
     * @throws { BusinessError } 401 - Invalid input parameter.Possible causes: 1. Mandatory parameters are
     *     left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Device not supported.
     * @throws { BusinessError } 21800001 - System internal error.
     * @throws { BusinessError } 21800005 - Failed to parse the ad response.
     * @syscap SystemCapability.Advertising.Ads
     * @since 12
     */
    function parseAdResponse(adResponse: string, listener: MultiSlotsAdLoadListener, context: common.UIAbilityContext): void;
    /**
     * Injects an ad JavaScript object to the **Web** component
     * (this API is only open to some pre-installed system applications).
     *
     * @param { web_webview.WebviewController } controller - Web component controller.
     * @param { common.UIAbilityContext } context - Context of the UIAbility.
     * @throws { BusinessError } 401 - Invalid input parameter. Possible causes: 1. Mandatory parameters are left
     *     unspecified.
     * @throws { BusinessError } 21800001 - System internal error.
     * @syscap SystemCapability.Advertising.Ads
     * @atomicservice
     * @since 12
     */
    function registerWebAdInterface(controller: web_webview.WebviewController, context: common.UIAbilityContext): void;
    /**
     * Injects an ad JavaScript object to the **Web** component
     * (this API is only open to some pre-installed system applications).
     *
     * @param { web_webview.WebviewController } controller - Web component controller.
     * @param { common.UIAbilityContext } context - Context of the UIAbility.
     * @param { boolean } needRefresh - Whether to refresh the page (true: yes; false: no).
     * @throws { BusinessError } 401 - Invalid input parameter. Possible causes: Mandatory parameters are left
     *     unspecified.
     * @throws { BusinessError } 21800001 - System internal error.
     * @syscap SystemCapability.Advertising.Ads
     * @atomicservice
     * @since 16
     */
    function registerWebAdInterface(controller: web_webview.WebviewController, context: common.UIAbilityContext, needRefresh: boolean): void;
    /**
     * Deletes the ad JavaScript object injected through **registerWebAdInterface**
     * (this API is only open to some pre-installed system applications).
     *
     * @param { web_webview.WebviewController } controller - Web component controller.
     * @param { boolean } needRefresh - Whether to refresh the page (true: yes; false: no).
     * @throws { BusinessError } 401 - Invalid input parameter. Possible causes: Mandatory parameters are left
     *     unspecified.
     * @throws { BusinessError } 21800001 - System internal error.
     * @syscap SystemCapability.Advertising.Ads
     * @atomicservice
     * @since 16
     */
    function deleteWebAdInterface(controller: web_webview.WebviewController, needRefresh: boolean): void;
}
export default advertising;

```
