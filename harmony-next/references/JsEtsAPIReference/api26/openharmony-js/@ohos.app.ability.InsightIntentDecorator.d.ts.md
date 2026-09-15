# @ohos.app.ability.InsightIntentDecorator.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
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
 * The InsightIntentDecorator module provides several types of intent decorators for decorating classes or methods. You
 * can [use these decorators to develop intents](docroot://application-models/insight-intent-decorator-development.md),
 * define application functionalities as intents, and integrate them into AI entry points such as intelligent Q&A,
 * intelligent search, and intelligent recommendation systems.
 *
 * -
 * [@InsightIntentLink](docroot://reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentlink)
 * : decorates a URI in your application as an intent, enabling AI systems to quickly jump to your application via this
 * intent. For details on the parameters supported by this decorator, see
 * [LinkIntentDecoratorInfo]{@link LinkIntentDecoratorInfo}.
 * -
 * [@InsightIntentPage](docroot://reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentpage)
 * : decorates a page in your application as an intent, enabling AI systems to swiftly navigate to that page. For
 * details on the parameters supported by this decorator, see [PageIntentDecoratorInfo]{@link PageIntentDecoratorInfo}.
 * -
 * [@InsightIntentFunction](docroot://reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentfunction)
 *  and
 * [@InsightIntentFunctionMethod](docroot://reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentfunctionmethod)
 * : The two decorators must be used together.
 * [@InsightIntentFunction](docroot://reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentfunction)
 *  is used to decorate a class, and
 * [@InsightIntentFunctionMethod](docroot://reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentfunctionmethod)
 *  is used to decorate a static function in that class. This setup defines the static function as an intent, enabling
 * AI systems to execute it rapidly.
 * -
 * [@InsightIntentEntry](docroot://reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintententry)
 * : decorates a class that inherits from
 * [InsightIntentEntryExecutor]{@link @ohos.app.ability.InsightIntentEntryExecutor:InsightIntentEntryExecutor} to
 * implement intent operations and configure the ability on which the intent depends. This helps the AI entry point to
 * easily invoke the associated ability and perform the intended action. For details on the parameters supported by this
 *  decorator, see [EntryIntentDecoratorInfo]{@link EntryIntentDecoratorInfo}.
 * -
 * [@InsightIntentForm](docroot://reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentform)
 * : decorates a [FormExtensionAbility]{@link @ohos.app.form.FormExtensionAbility} to specify the name of the widget
 * bound to the FormExtensionAbility. This enables the AI entry point to add the widget via intent calls. For details on
 *  the parameters supported by this decorator, see [FormIntentDecoratorInfo]{@link FormIntentDecoratorInfo}.
 * -
 * [@InsightIntentEntity](docroot://reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintententity)
 * : decorates a class that inherits from
 * [IntentEntity]{@link @ohos.app.ability.insightIntent:insightIntent.IntentEntity} to define the class as an intent
 * entity, which can pass parameters required for intent calls. For details on the parameters supported by this
 * decorator, see [IntentEntityDecoratorInfo]{@link IntentEntityDecoratorInfo}.
 *
 * @file
 * @kit AbilityKit
 */
import insightIntent from './@ohos.app.ability.insightIntent';
/**
 * Common properties for intent decorators, used to define basic information about an intent (including the intent name
 * and version number). It applies to all decorators provided by this module.
 *
 * > **NOTE**
 * >
 * > If a matching intent is found in the standard intent list based on the **schema** and **intentVersion** fields, the
 * >  system automatically populates the **intentName**, **domain**, **llmDescription**, **keywords**, **parameters**,
 * > and **result** fields with the values from the matching standard intent.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 20
 */
declare interface IntentDecoratorInfo {
    /**
     * Intent name, which is the unique identifier of an intent.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    intentName: string;
    /**
     * Vertical domain of the intent. It is used to categorize intents by vertical fields (for example, video, music, and
     * games). For details about the value range, see the vertical domain fields in
     * [smart distribution features in different vertical domains](https://developer.huawei.com/consumer/en/doc/service/intents-ai-distribution-characteristic-0000001901922213#section2656133582215)
     * .
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    domain: string;
    /**
     * Version number of the intent. It is used to distinguish and manage intents when their capabilities evolve.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    intentVersion: string;
    /**
     * Name of the intent displayed to users.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    displayName: string;
    /**
     * Description of the intent displayed to users.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    displayDescription?: string;
    /**
     * Name of a standard intent schema. This field is required when you
     * [access a standard intent](docroot://application-models/insight-intent-definition.md#accessing-standard-intents).
     * It is not required when you
     * [create a custom intent](docroot://application-models/insight-intent-definition.md#creating-custom-intents). For
     * details about the standard intent list, see
     * [Appendix: Standard Intent Access Specifications](docroot://application-models/insight-intent-access-specifications.md)
     * .
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    schema?: string;
    /**
     * Icon of the intent. It is displayed in the AI entry point.
     *
     * - If the value is a string, the icon is read from a network resource.
     * - If the value is a [resource](../../reference/apis-localization-kit/js-apis-resource-manager.md), the icon is read
     *  from a local resource.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    icon?: ResourceStr;
    /**
     * Function of an intent, which helps large language models understand the intent.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    llmDescription?: string;
    /**
     * Search keywords for the intent.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    keywords?: string[];
    /**
     * Data format of intent parameters, which is used to define the input data format during intent calls.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    parameters?: Record<string, Object>;
    /**
     * Data format for the results returned by intent calls. It defines how the data should be structured.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    result?: Record<string, Object>;
}
/**
 * LinkIntentDecoratorInfo inherits from [IntentDecoratorInfo]{@link IntentDecoratorInfo} and describes the parameters
 * supported by the
 * [@InsightIntentLink](docroot://reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentlink)
 *  decorator, such as the URI information required for application redirection.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 20
 */
declare interface LinkIntentDecoratorInfo extends IntentDecoratorInfo {
    /**
     * URI information associated with the intent.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    uri: string;
    /**
     * Mapping between intent parameters and URI information.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    paramMappings?: LinkIntentParamMapping[];
}
/**
 * Enumerates the intent parameter categories available for the
 * [@InsightIntentLink](docroot://reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentlink)
 *  decorator. The enum is used to define how intent parameters should be passed.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 20
 */
declare enum LinkParamCategory {
    /**
     * Category of link. Intent parameters are appended to the end of a URI link and passed to the application via the
     * URI.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    LINK = 'link',
    /**
     * Category of want. Intent parameters are passed to the application through the **parameters** field in
     * [Want]{@link @ohos.app.ability.Want:Want}.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    WANT = 'want'
}
/**
 * LinkIntentParamMapping defines the mapping between intent parameters and URI information for the
 * [@InsightIntentLink](docroot://reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentlink)
 *  decorator.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 20
 */
declare interface LinkIntentParamMapping {
    /**
     * Name of the intent parameter.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    paramName: string;
    /**
     * Mapping name of the intent parameter.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    paramMappingName?: string;
    /**
     * Category of the intent parameter.
     *
     * If an intent parameter is of the [LINK](#linkparamcategory) category, the system retrieves **paramMappingName**
     * corresponding to **paramName** and appends it to the URI as a key-value pair (where **key** is the value of
     * **paramMappingName**, and **value** is the intent parameter value).
     *
     * If an intent parameter is of the [WANT](#linkparamcategory) category, the system retrieves **paramMappingName**
     * corresponding to **paramName** and passes the mapping name and value using the **parameters** field in
     * [Want](./js-apis-app-ability-want.md).
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    paramCategory?: LinkParamCategory;
}
/**
 * Define InsightIntentLink.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 20
 */
export declare const InsightIntentLink: ((intentInfo: LinkIntentDecoratorInfo) => ClassDecorator);
/**
 * PageIntentDecoratorInfo inherits from [IntentDecoratorInfo]{@link IntentDecoratorInfo} and describes the parameters
 * supported by the
 * [@InsightIntentPage](docroot://reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentpage)
 *  decorator, such as the name of
 * [NavDestination](docroot://reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md#navdestination10) of the
 * target page.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 20
 */
declare interface PageIntentDecoratorInfo extends IntentDecoratorInfo {
    /**
     * Name of the UIAbility bound to the intent.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    uiAbility?: string;
    /**
     * Path of the page bound to the intent. The page must be a file that actually exists.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    pagePath: string;
    /**
     * ID of the [Navigation](docroot://reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md#attributes)
     * component bound to the intent.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    navigationId?: string;
    /**
     * Name of the
     * [NavDestination](docroot://reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md#navdestination10)
     * component bound to the intent.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    navDestinationName?: string;
}
/**
 * Decorates a page in the application as an intent, enabling AI systems to swiftly navigate to that page. For details
 * on the parameters supported by this decorator, see [PageIntentDecoratorInfo]{@link PageIntentDecoratorInfo}.
 *
 * > **NOTE**
 * >
 * > This decorator is only applicable to struct pages.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 20
 */
export declare const InsightIntentPage: ((intentInfo: PageIntentDecoratorInfo) => ClassDecorator);
/**
 * Parameter type of the
 * [@InsightIntentFunctionMethod](docroot://reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentfunctionmethod)
 *  decorator. All properties inherit from [IntentDecoratorInfo]{@link IntentDecoratorInfo}.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 20
 */
declare interface FunctionIntentDecoratorInfo extends IntentDecoratorInfo {
}
/**
 * This decorator must be used together with the [@InsightIntentFunction]{@link InsightIntentFunction} decorator.
 * [@InsightIntentFunction]{@link InsightIntentFunction} is used to decorate a class, and this decorator is used to
 * decorate a static function in that class. This setup defines the static function as an intent, enabling AI systems
 * to execute it rapidly.
 *
 * > **NOTE**
 * >
 * > The class containing static methods must be exported using export.
 * > Parameter names and types of a function must align with those specified in the intent definition.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 20
 */
export declare const InsightIntentFunctionMethod: ((intentInfo: FunctionIntentDecoratorInfo) => MethodDecorator);
/**
 * This decorator must be used together with the [@InsightIntentFunctionMethod]{@link InsightIntentFunctionMethod}
 * decorator.
 * This decorator is used to decorate a class, and [@InsightIntentFunctionMethod]{@link InsightIntentFunctionMethod} is
 *  used to decorate a static function in that class. This setup defines the static function as an intent, enabling AI
 * systems to execute it rapidly.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 20
 */
export declare const InsightIntentFunction: (() => ClassDecorator);
/**
 * Inherits from [IntentDecoratorInfo]{@link IntentDecoratorInfo} and is used to describe the parameters supported by
 * the
 * [@InsightIntentEntry](docroot://reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintententry)
 *  decorator.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 20
 */
declare interface EntryIntentDecoratorInfo extends IntentDecoratorInfo {
    /**
     * Name of the ability bound to the intent.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    abilityName: string;
    /**
     * Execution mode of the intent call, that is, execution mode supported when the bound ability is started.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    executeMode: insightIntent.ExecuteMode[];
}
/**
 * Decorates a class that inherits from
 * [InsightIntentEntryExecutor]{@link @ohos.app.ability.InsightIntentEntryExecutor:InsightIntentEntryExecutor} to
 * implement intent operations and configure the ability on which the intent depends. This helps the AI entry point to
 * easily invoke the associated ability and perform the intended action. For details on the parameters supported by
 * this decorator, see [EntryIntentDecoratorInfo]{@link EntryIntentDecoratorInfo}.
 *
 * > **NOTE: **
 * >
 * > If this decorator is used to access a standard intent, all mandatory parameters defined in the standard intent
 * > JSON schema must be implemented and their parameter types must match.
 * > If this decorator is used to access a custom intent, all mandatory parameters defined in parameters must be
 * > implemented and their parameter types must match.
 * > Classes decorated by this decorator must be exported using export default. Class properties are limited to basic
 * > types or intent entities, and the return value must be intent entities.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 20
 */
export declare const InsightIntentEntry: ((intentInfo: EntryIntentDecoratorInfo) => ClassDecorator);
/**
 * Inherits from [IntentDecoratorInfo]{@link IntentDecoratorInfo} and is used to describe the parameters supported by
 * the
 * [@InsightIntentForm](docroot://reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentform)
 *  decorator.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 20
 */
declare interface FormIntentDecoratorInfo extends IntentDecoratorInfo {
    /**
     * Name of the widget bound to the FormExtensionAbility.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    formName: string;
}
/**
 * Decorates a [FormExtensionAbility]{@link @ohos.app.form.FormExtensionAbility} to specify the name of the widget
 * bound to the [FormExtensionAbility]{@link @ohos.app.form.FormExtensionAbility}. This enables the AI entry point to
 * add the widget via intent calls. For details on the parameters supported by this decorator, see
 * [FormIntentDecoratorInfo]{@link FormIntentDecoratorInfo}.
 *
 * > **NOTE: **
 * > For details about the requirements for defining widget names, see Widget Configuration.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 20
 */
export declare const InsightIntentForm: ((intentInfo: FormIntentDecoratorInfo) => ClassDecorator);
/**
 * Describes the parameters supported by the
 * [@InsightIntentEntity](docroot://reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintententity)
 *  decorator.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 20
 */
declare interface IntentEntityDecoratorInfo {
    /**
     * Category of the intent entity. Intents can be classified based on intent entity categories.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    entityCategory: string;
    /**
     * Data format of the intent entity.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    parameters?: Record<string, Object>;
    /**
     * Supported query properties.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    supportedQueryProperties?: string[];
}
/**
 * Decorates a class that inherits from
 * [IntentEntity]{@link @ohos.app.ability.insightIntent:insightIntent.IntentEntity} to define the class as an intent
 * entity, which can pass parameters required for intent calls. For details on the parameters supported by this
 * decorator, see [IntentEntityDecoratorInfo]{@link IntentEntityDecoratorInfo}.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 20
 */
export declare const InsightIntentEntity: ((intentEntityInfo: IntentEntityDecoratorInfo) => ClassDecorator);

```
