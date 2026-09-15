# @ohos.arkui.components.ContainerReader.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2026 Huawei Device Co., Ltd.
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
 * @kit ArkUI
 */
import { Size } from './arkui/Graphics';
/**
 * Defines the configuration options for ContainerReader component.
 * Used to specify the parameters for container dimension reading and breakpoint analysis.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @since 26.0.0
 */
export interface ContainerReaderInfo {
    /**
     * The target container size for layout analysis.
     * Defines the reference dimensions used for breakpoint calculation and layout adaptation.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 26.0.0
     */
    size: Size;
    /**
     * Optional width breakpoint configuration for container width analysis.
     * Defines the width thresholds that trigger different layout behaviors.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 26.0.0
     */
    widthBreakpoint?: WidthBreakpoint;
    /**
     * Optional height breakpoint configuration for container height analysis.
     * Defines the height thresholds that trigger different layout behaviors.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 26.0.0
     */
    heightBreakpoint?: HeightBreakpoint;
}
/**
 * Defines the breakpoint configuration options for container dimension analysis.
 * Specifies threshold values that trigger different layout behaviors based on container size.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @since 26.0.0
 */
export interface BreakpointOptions {
    /**
     * Optional array of width breakpoint values in vp units.
     * Defines the width thresholds for container width analysis.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 26.0.0
     */
    width?: Array<number>;
    /**
     * Optional array of height breakpoint values in vp units.
     * Defines the height thresholds for container height analysis.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 26.0.0
     */
    height?: Array<number>;
}
/**
 * Defines the ContainerReader Component.
 * Used for reading and analyzing container layout information based on size breakpoints in dynamic scenarios.
 * Provides container dimension analysis and breakpoint detection capabilities.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @since 26.0.0
 */
export interface ContainerReaderInterface {
    /**
     * Sets the container reading configuration for ContainerReader component.
     * Configures the size parameters and breakpoint rules for container layout analysis.
     *
     * @param { ContainerReaderInfo } value - The configuration options for container reading
     * @returns { ContainerReaderAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 26.0.0
     */
    (value: ContainerReaderInfo): ContainerReaderAttribute;
}
/**
 * Defines the ContainerReader attribute functions.
 * Provides methods for configuring container reading parameters and breakpoint analysis properties.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @since 26.0.0
 */
export declare class ContainerReaderAttribute extends CommonMethod<ContainerReaderAttribute> {
    /**
     * Sets the breakpoint configuration for container dimension analysis.
     * Defines a set of threshold values that trigger different layout behaviors based on container size.
     *
     * @param { BreakpointOptions } [value] - An array of breakpoint values in vp
     * @returns { ContainerReaderAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 26.0.0
     */
    breakpointConfig(value?: BreakpointOptions): ContainerReaderAttribute;
}
/**
 * Defines ContainerReader Component.
 * A component that analyzes container dimensions and provides breakpoint information for responsive layouts.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @uicomponent
 * @since 26.0.0
 */
export declare const ContainerReader: ContainerReaderInterface;
/**
 * Defines ContainerReader Component instance.
 * Provides access to ContainerReader component methods for container dimension analysis and breakpoint detection.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @uicomponent
 * @since 26.0.0
 */
export declare const ContainerReaderInstance: ContainerReaderAttribute;

```
