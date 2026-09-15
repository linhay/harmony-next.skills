# @ohos.arkui.uiMaterial.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025-2026 Huawei Device Co., Ltd.
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
 * @kit ArkUI
 */
/**
 * This module provides APIs for system materials. Different system materials correspond to different UI effects,
 * including the background color ([backgroundColor]{@link CommonMethod#backgroundColor(value: ResourceColor)}), border
 * color ([borderColor]{@link CommonMethod#borderColor}), border width ([borderWidth]{@link CommonMethod#borderWidth}),
 * and shadow ([shadow]{@link CommonMethod#shadow(value: ShadowOptions | ShadowStyle)}).
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @since 26.0.0
 */
declare namespace uiMaterial {
    /**
     * Enumerates system material types.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 26.0.0
     */
    enum MaterialType {
        /**
         * Immersive material type. It is used only by the **type** attribute of the
         * [MaterialInfo]{@link uiMaterial.MaterialInfo} API to identify the current material type and does not map to
         * underlying features. The actual material effect is implemented by the
         * [ImmersiveMaterial]{@link uiMaterial.ImmersiveMaterial} class.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        IMMERSIVE = 2
    }
    /**
     * Enumerates the material enabling states, indicating the states of the application-level immersive system material
     * configuration.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    enum MaterialState {
        /**
         * Default state. The immersive system material is enabled by default for the
         * [Dialog](docroot://ui/arkts-base-dialog-overview.md), [Toast](docroot://ui/arkts-create-toast.md), and
         * [AlphabetIndexer]{@link alphabet_indexer} components if the background color, blur, and shadow are not set for
         * the components. The immersive system material is enabled by default for the text menu triggered by long-pressing
         * or double-clicking after [copyOption]{@link TextAttribute#copyOption} is set in the [Text]{@link text} component.
         * For other components, whether the immersive system material is enabled is set by the application.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        DEFAULT = 0,
        /**
         * Enabled state. The immersive system material is enabled by default for the
         * [Dialog](docroot://ui/arkts-base-dialog-overview.md), [Toast](docroot://ui/arkts-create-toast.md),
         * [AlphabetIndexer]{@link alphabet_indexer}, [ChipGroup]{@link @ohos.arkui.advanced.ChipGroup},
         * [Chip]{@link @ohos.arkui.advanced.Chip}, [Select]{@link select}, [Menu Control]{@link common},
         * [Toggle]{@link toggle}, [SegmentButton]{@link @ohos.arkui.advanced.SegmentButton},
         * [SegmentButtonV2]{@link @ohos.arkui.advanced.SegmentButtonV2}, [Slider]{@link slider},
         * [bindSheet]{@link CommonMethod#bindSheet}, and [SelectionMenu]{@link @ohos.arkui.advanced.SelectionMenu}. After
         * [copyOption]{@link TextAttribute#copyOption} is set for the [Text]{@link text} component, the immersive system
         * material is enabled by default for the text menu triggered by long-pressing or double-clicking. In this state,
         * the immersive system material style takes precedence over the background color, blur, shadow, and border style
         * set for the components. You need to set whether to enable the immersive system material for other components.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        ENABLE = 1,
        /**
         * Disabled state. The immersive system material cannot be enabled for any component. Even if you set the immersive
         * system material parameters for a component, the settings will not take effect.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        DISABLE = 2
    }
    /**
     * Provides material configuration information, including the material enabling state and material type.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    interface MaterialInfo {
        /**
         * Material enabling state.
         *
         * @default MaterialState.DEFAULT
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        state: MaterialState;
        /**
         * Material type ID, indicating the material type corresponding to the current configuration. The value is used only
         * for type identification and does not map to underlying features.
         *
         * @default MaterialType.IMMERSIVE
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        type: MaterialType;
    }
    /**
     * Obtains the material configuration information of this application. The returned configuration information comes
     * from the metadata configured in the [module.json5](docroot://quick-start/module-configuration-file.md) file of the
     * application.
     *
     * @returns { MaterialInfo } Material configuration information of this application, including the material enabling
     *     state and material type.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    function getMaterialInfo(): MaterialInfo;
    /**
     * Enumerates immersive material styles. Different material styles correspond to different material parameters,
     * including the blur degree and brightness.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    enum ImmersiveStyle {
        /**
         * Ultra-thin style, which provides a very strong transparent effect.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        ULTRA_THIN = 0,
        /**
         * Thin style, which provides a strong transparent effect.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        THIN = 1,
        /**
         * Regular style, which means the material layer is of regular thickness.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        REGULAR = 2,
        /**
         * Thick style, which provides a strong blur effect.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        THICK = 3,
        /**
         * Ultra-thick style, which provides a very strong blur effect.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        ULTRA_THICK = 4
    }
    /**
     * Enumerates the material levels, which indicate the computing power level of the device.
     * Use [getGlobalMaterialLevel]{@link uiMaterial.getGlobalMaterialLevel()} to obtain the material level
     * of the current device.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    enum MaterialLevel {
        /**
         * Material level of devices with high-level computing power.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        EXQUISITE = 0,
        /**
         * Material level of devices with mid-level computing power.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        GENTLE = 1,
        /**
         * Material level of devices with low-level computing power.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        SMOOTH = 2
    }
    /**
     * Obtains the global material level, which is related to the device computing power. This configuration item
     * is defined by the device and cannot be modified.
     *
     * @returns { MaterialLevel } Material level of the device.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    function getGlobalMaterialLevel(): MaterialLevel;
    /**
     * Check whether [ImmersiveMaterial]{@link uiMaterial#ImmersiveMaterial} is supported on the current device.
     * If it is true, the ImmersiveMaterial object can be used in the
     * [systemMaterial]{@link CommonMethod#systemMaterial(material: SystemUiMaterial | undefined)} attribute.
     * If it is false, setting the ImmersiveMaterial object in the systemMaterial attribute will not take effect.
     * It is defined by the device and cannot be modified.
     *
     * @returns { boolean } Whether the current device supports ImmersiveMaterial. The value true indicates that the
     *     current device supports ImmersiveMaterial, and false indicates the opposite.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    function isImmersiveMaterialSupported(): boolean;
    /**
     * Immersive material parameters.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
    */
    interface ImmersiveOptions {
        /**
         * Material style. Different styles correspond to different material parameters, which affect the material
         * thickness.
         *
         * Note: This parameter takes effect only for the display effect of devices with high- and mid-level computing
         * power.
         *
         * Default value: **ImmersiveStyle.REGULAR**
         *
         * @default uiMaterial.ImmersiveStyle.REGULAR
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        style?: ImmersiveStyle;
        /**
         * Coloring of the material layer. This parameter is used to add a pure color effect for the material filter. The
         * pure color must have a certain transparency value and cannot be completely opaque. Otherwise, the material filter
         * effect will be completely blocked.
         *
         * Note: This parameter takes effect only for the display effect of devices with high- and mid-level computing
         * power.
         *
         * Default value: **Color.Transparent**
         *
         * @default Color.Transparent
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        materialColor?: ResourceColor;
        /**
         * Whether the subtree of the node of the material object automatically adapts the material to the complementary
         * color of the background color.
         *
         * **false** indicates the material is not automatically adapted to the complementary color of the background color.
         *
         * **true** indicates that the material is automatically adapted to the complementary color of the background color
         * only when the material layer is thin enough. The materials that can be adapted to the complementary color are
         * defined by the system. Such materials must have at least the **THIN** or **ULTRA_THIN** style, and are related to
         * the strength configuration of the immersive light effect of the application. The thinner the material and the
         * stronger the immersive light effect, the more likely the material meets the requirements for adapting to the
         * complementary color.
         *
         * The capability of automatically adapting the material to the complementary color takes effect only when special
         * resource values are set for some attribute APIs. The attribute APIs include
         * [fontColor]{@link TextAttribute#fontColor} of the **Text** component,
         * [fontColor]{@link ButtonAttribute#fontColor} of the **Button** component,
         * [fontColor]{@link SymbolGlyphAttribute#fontColor(value: Array<ResourceColor>)} of the **SymbolGlyph** component,
         * [fillColor]{@link ImageAttribute#fillColor(value: ResourceColor)} of the **Image** component, icon colors in
         * [placeholderColor]{@link SearchAttribute#placeholderColor}, [fontColor]{@link SearchAttribute#fontColor}, and
         * [searchIcon]{@link SearchAttribute#searchIcon} of the **Search** component, icon colors in
         * [cancelButton]{@link SearchAttribute#cancelButton}, caret colors in
         * [caretStyle]{@link SearchAttribute#caretStyle}, and text and icon colors in
         * [tabBar]{@link TabContentAttribute#tabBar(options: string | Resource | CustomBuilder | TabBarOptions)} of the
         * **TabContent** component when the [BottomTabBarStyle]{@link BottomTabBarStyle} style is used.
         *
         * Note: This parameter takes effect only for the display effect of devices with high- and mid-level computing
         * power.
         *
         * Default value: **false**
         *
         * @default false
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        colorInvert?: boolean;
        /**
         * Whether to add a shadow effect for a material.
         *
         * If this parameter is set to **true**, the added shadow effect in the material always takes effect, which takes
         * precedence over the general [shadow]{@link CommonMethod#shadow(value: ShadowOptions | ShadowStyle)} attribute. If
         * this parameter is set to **false**, only the general shadow attribute takes effect.
         *
         * Note: This parameter takes effect only for the display effect of devices with all levels of computing power.
         *
         * Default value: **true**
         *
         * @default true
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        applyShadow?: boolean;
        /**
         * Whether to set an interactive deformation effect for the component with a material set.
         *
         * Note: This parameter takes effect for the display effect of devices with all levels of computing power.
         *
         * Default value: **false**
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        interactive?: boolean;
        /**
         * Whether to set a light sensing interaction feedback effect for the component with a material set. If this
         * parameter is set to null, the light sensing interaction feedback effect is disabled.
         *
         * Note: This parameter takes effect for the display effect of devices with all levels of computing power.
         *
         * Default value: **undefined**, indicating that the light sensing interaction feedback effect is not set.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        lightEffect?: LightEffectOptions | null;
    }
    /**
     * Provides the light sensing interaction feedback configuration for immersive materials. The configuration is used to
     * customize the color of the light sensing feedback.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    interface LightEffectOptions {
        /**
         * Custom color of the light sensing feedback.
         *
         * Default value: **Color.White**
         *
         * @default Color.White
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        color?: ResourceColor;
    }
    /**
     * System material object on the UI.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 26.0.0
     */
    class Material {
        /**
         * Returns an empty material object, which is used to disable the immersive system material effect for a component.
         * The usage method is **uiMaterial.Material.empty**.
         *
         * In enabled state, you can disable the immersive system material effect for a component by setting
         * **systemMaterial(uiMaterial.Material.empty)**. If the component does not support the component-level immersive
         * system material API, the material effect cannot be disabled using this API.
         *
         * @returns { Material } Empty material object, indicating that there is no material effect.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        static get empty(): Material;
    }
    /**
     * Immersive material class, which inherits from [Material]{@link uiMaterial.MaterialType}.
     *
     * The performance of an immersive material varies based on device computing power. The high, medium, and low levels
     * of device computing power are determined by device vendors and defined in the system configuration files. On
     * devices with high- and mid-level computing power, the filter and
     * [shadow]{@link CommonMethod#shadow(value: ShadowOptions | ShadowStyle)} effects of the material layer are affected.
     * On devices with low-level computing power, the
     * [background color]{@link CommonMethod#backgroundColor(value: ResourceColor)},
     * [border color]{@link CommonMethod#borderColor}, [border width]{@link CommonMethod#borderWidth}, and
     * [shadow]{@link CommonMethod#shadow(value: ShadowOptions | ShadowStyle)} effects are affected. In addition, the
     * effect of the same material is affected by the immersive light configuration in the application. The material
     * parameters and effects vary depending on the immersive light configuration.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    class ImmersiveMaterial extends Material {
        /**
         * Constructs **ImmersiveMaterial**.
         *
         * @param { ImmersiveOptions } [options] - System material configuration options, including the material style and
         *     material layer coloring.<br>For details about the default values, see the default values of the parameters in
         *     the **ImmersiveOptions** API, that is,
         *     **{style:ImmersiveStyle.REGULAR, materialColor:Color.Transparent, colorInvert:false, applyShadow:true, interactive:false, lightEffect:undefined}**.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        constructor(options?: ImmersiveOptions);
    }
}
/**
 * export uiMaterial namespace.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @since 26.0.0
 */
export default uiMaterial;

```
