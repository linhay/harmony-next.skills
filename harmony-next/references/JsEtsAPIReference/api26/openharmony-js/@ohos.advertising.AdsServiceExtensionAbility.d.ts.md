# @ohos.advertising.AdsServiceExtensionAbility.d.ts

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
 * The AdsServiceExtensionAbility module provides ExtensionAbilities for the ads service. Device vendors can implement
 * the callbacks for ads requests.
 *
 * @file ExtensionAbility for Ads
 * @kit AdsKit
 */
import type advertising from './@ohos.advertising';
/**
 * Ad request callback.
 *
 * @syscap SystemCapability.Advertising.Ads
 * @since 11
 */
export interface RespCallback {
    /**
     * Data in the ad request callback.
     *
     * @param { Map<string, Array<advertising.Advertisement>> } respData - Callback data of ad requests.
     *     It is a mapping collection that takes ad unit ID as the key and stores acquired ad content.
     * @syscap SystemCapability.Advertising.Ads
     * @since 11
     */
    (respData: Map<string, Array<advertising.Advertisement>>): void;
}

```
