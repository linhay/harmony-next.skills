# @ohos.net.vpn.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2023 Huawei Device Co., Ltd.
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
 * @file VPN Management
 * @kit NetworkKit
 */
import type connection from './@ohos.net.connection';
import type _AbilityContext from './application/UIAbilityContext';
/**
 * This module is the built-in VPN function provided by the OS. It allows users to set up VPN connections through the
 * network settings of the OS. Generally, this module provides only limited functions and is subject to strict
 * restrictions.
 *
 * @syscap SystemCapability.Communication.NetManager.Vpn
 * @since 10
 */
declare namespace vpn {
    /**
     * Defines the network link address information.
     *
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 10
     */
    export type LinkAddress = connection.LinkAddress;
    /**
     * Defines the network route information.
     *
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 10
     */
    export type RouteInfo = connection.RouteInfo;
    /**
     * The context of an ability. It allows access to ability-specific resources.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 10
     */
    export type AbilityContext = _AbilityContext;
}
export default vpn;

```
