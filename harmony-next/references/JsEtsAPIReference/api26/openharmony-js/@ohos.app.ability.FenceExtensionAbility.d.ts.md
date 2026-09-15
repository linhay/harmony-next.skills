# @ohos.app.ability.FenceExtensionAbility.d.ts

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
 * @kit LocationKit
 */
import type FenceExtensionContext from './@ohos.app.ability.FenceExtensionContext';
import geoLocationManager from './@ohos.geoLocationManager';
/**
 * Class of fence extension ability.
 *
 * @syscap SystemCapability.Location.Location.Geofence
 * @stagemodelonly
 * @since 14
 */
export default class FenceExtensionAbility {
    /**
     * Indicates the fence extension context.
     *
     * @type { FenceExtensionContext }
     * @syscap SystemCapability.Location.Location.Geofence
     * @stagemodelonly
     * @since 14
     */
    context: FenceExtensionContext;
    /**
     * Called back when geofence status is change.
     *
     * @param { geoLocationManager.GeofenceTransition } transition - Geofence transition status
     * @param { Record<string, string> } additions - Indicates additional information
     * @syscap SystemCapability.Location.Location.Geofence
     * @stagemodelonly
     * @since 14
     */
    onFenceStatusChange(transition: geoLocationManager.GeofenceTransition, additions: Record<string, string>): void;
    /**
     * Called back before a fence extension is destroyed.
     *
     * @syscap SystemCapability.Location.Location.Geofence
     * @stagemodelonly
     * @since 14
     */
    onDestroy(): void;
}

```
