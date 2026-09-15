# @ohos.arkui.ArcAlphabetIndexer.d.ts

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
 * @kit ArkUI
 */
/**
 * Initialization parameters for the **ArcAlphabetIndexer** component.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 */
declare interface ArcAlphabetIndexerInitInfo {
    /**
     * Array of alphabet index strings. It cannot be set to empty.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    arrayValue: string[];
    /**
     * Index of the initial selected item. If the value is out of range, the default value **0** is used.
     *
     * This parameter supports two-way binding through [!!](docroot://ui/state-management/arkts-new-binding.md).
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    selected: number;
}
/**
 * Defines the callback used in [onSelect]{@link ArcAlphabetIndexerAttribute#onSelect}.
 *
 * @param { number } index - Index of the selected item.
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 */
declare type OnSelectCallback = (index: number) => void;
/**
 * The **ArcAlphabetIndexer** component is an arc-shaped component designed for quick navigation through alphabetically
 * sorted items. It can be integrated with container components to quickly locate items within the visible area.
 *
 * > **NOTE**
 *
 * > - This component can be used on phones, PCs, 2-in-1 devices, tablets, TVs, and wearables. In API version 22 and
 * > earlier versions, a compilation warning will be reported when this component is used on phones, PCs, 2-in-1
 * > devices, tablets, and TVs, but the component can still run properly.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 * @noninterop
 */
export interface ArcAlphabetIndexerInterface {
    /**
     * Creates an instance of the **ArcAlphabetIndexer** component with initialization parameters.
     *
     * @param { ArcAlphabetIndexerInitInfo } info - Initialization parameters for the **ArcAlphabetIndexer** component.
     * @returns { ArcAlphabetIndexerAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    (info: ArcAlphabetIndexerInitInfo): ArcAlphabetIndexerAttribute;
}
/**
 * In addition to the [universal attributes]{@link common}, the following attributes are supported.
 *
 * In addition to the [universal events]{@link common}, the following events are supported.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 */
declare class ArcAlphabetIndexerAttribute extends CommonMethod<ArcAlphabetIndexerAttribute> {
    /**
     * Sets the text color of the index items in the normal state.
     *
     * @param { Optional<ColorMetrics> } color - Text color.<br>Default value: **0xFFFFFF**, displayed as white
     * @returns { ArcAlphabetIndexerAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    color(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute;
    /**
     * Sets the text color of the selected item.
     *
     * @param { Optional<ColorMetrics> } color - Text color of the selected item.<br>Default value: **0xFFFFFF**,
     *     displayed as white
     * @returns { ArcAlphabetIndexerAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    selectedColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute;
    /**
     * Sets the text color for the pop-up window.
     *
     * @param { Optional<ColorMetrics> } color - Text color of the pop-up window.<br>Default value: **0xFFFFFF**,
     *     displayed as white
     * @returns { ArcAlphabetIndexerAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    popupColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute;
    /**
     * Sets the background color of the selected item.
     *
     * @param { Optional<ColorMetrics> } color - Background color of the selected item.<br>Default value: **0x1F71FF**,
     *     displayed as dark blue
     * @returns { ArcAlphabetIndexerAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    selectedBackgroundColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute;
    /**
     * Sets the background color of the pop-up window.
     *
     * @param { Optional<ColorMetrics> } color - Background color of the pop-up window.<br>Default value: **0xD8404040**,
     *     displayed as dark gray with slight transparency
     * @returns { ArcAlphabetIndexerAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    popupBackground(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute;
    /**
     * Sets whether to display the pop-up window.
     *
     * @param { Optional<boolean> } enabled - Whether to display the pop-up window.<br>**true**: yes; **false**: no<br>
     *     Default value: **false**
     * @returns { ArcAlphabetIndexerAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    usePopup(enabled: Optional<boolean>): ArcAlphabetIndexerAttribute;
    /**
     * Sets the font style of the selected item, including size, weight, style, and font family.
     *
     * @param { Optional<Font> } font - Font style of the selected item.<br>Default value: {<br>size:'13.0fp',<br> style:
     *     FontStyle.Normal,<br> weight:500,<br> family:'HarmonyOS Sans'<br>}
     * @returns { ArcAlphabetIndexerAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    selectedFont(font: Optional<Font>): ArcAlphabetIndexerAttribute;
    /**
     * Sets the font style of the pop-up window.
     *
     * @param { Optional<Font> } font - Font style of the pop-up window.<br>Default value:<br>{<br>size:'19.0fp',<br>
     *     style:FontStyle.Normal,<br> weight:500,<br> family:'HarmonyOS Sans'<br>}
     * @returns { ArcAlphabetIndexerAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    popupFont(font: Optional<Font>): ArcAlphabetIndexerAttribute;
    /**
     * Sets the default font style of the index items.
     *
     * @param { Optional<Font> } font - Default font style of the index items.<br>Default value:<br>{<br>size:'13.0fp',<br
     *     > style:FontStyle.Normal,<br> weight:500,<br> family:'HarmonyOS Sans'<br>}
     * @returns { ArcAlphabetIndexerAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    font(font: Optional<Font>): ArcAlphabetIndexerAttribute;
    /**
     * Sets the size of the index item area.
     *
     * @param { Optional<LengthMetrics> } size - Size of the index item area. For the circular item area, this represents
     *     the diameter of the circle. Percentage values are not supported.<br>Default value: **24.0**<br>Unit: vp
     * @returns { ArcAlphabetIndexerAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    itemSize(size: Optional<LengthMetrics>): ArcAlphabetIndexerAttribute;
    /**
     * Sets the index of the selected item.
     *
     * @param { Optional<number> } index - Index of the selected item.<br>Default value: **0**<br>This parameter supports
     *     two-way binding through [!!](docroot://ui/state-management/arkts-new-binding.md).
     * @returns { ArcAlphabetIndexerAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    selected(index: Optional<number>): ArcAlphabetIndexerAttribute;
    /**
     * Sets whether to enable the adaptive collapse behavior for the indexer.
     *
     * @param { Optional<boolean> } enable - Whether to enable the adaptive collapse behavior for the indexer.<br>Default
     *     value: **true**.<br>**true**: Enable the adaptive collapse behavior.<br>**false**: Disable the adaptive
     *     collapse behavior.
     * @returns { ArcAlphabetIndexerAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    autoCollapse(enable: Optional<boolean>): ArcAlphabetIndexerAttribute;
    /**
     * Triggered when an index item is selected. The return value is the index of the selected item.
     *
     * @param { Optional<OnSelectCallback> } handler - Callback used to return the result.
     * @returns { ArcAlphabetIndexerAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    onSelect(handler: Optional<OnSelectCallback>): ArcAlphabetIndexerAttribute;
    /**
     * Sets the background blur style of the pop-up window. If this API is not used, the blur is disabled by default. The
     * corresponding value is **NONE** in **BlurStyle**.
     *
     * > **NOTE**
     *
     * > After configuring the pop-up window background blur style with **popupBackgroundBlurStyle**, avoid applying
     * > background colors via [popupBackground]{@link ArcAlphabetIndexerAttribute#popupBackground}.
     *
     * @param { Optional<BlurStyle> } style - Background blur style of the pop-up window.
     * @returns { ArcAlphabetIndexerAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    popupBackgroundBlurStyle(style: Optional<BlurStyle>): ArcAlphabetIndexerAttribute;
}
/**
 * The **ArcAlphabetIndexer** component is an arc-shaped component designed for quick navigation through alphabetically
 * sorted items. It can be integrated with container components to quickly locate items within the visible area.
 *
 * > **NOTE**
 *
 * > - This component can be used on phones, PCs, 2-in-1 devices, tablets, TVs, and wearables. In API version 22 and
 * > earlier versions, a compilation warning will be reported when this component is used on phones, PCs, 2-in-1
 * > devices, tablets, and TVs, but the component can still run properly.
 *
 * ###### Child Components
 *
 * Not supported
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @uicomponent [since 19]
 * @since 18
 * @noninterop
 */
declare const ArcAlphabetIndexer: ArcAlphabetIndexerInterface;
/**
 * Defines ArcAlphabetIndexer Component instance.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 * @noninterop
 */
declare const ArcAlphabetIndexerInstance: ArcAlphabetIndexerAttribute;

```
