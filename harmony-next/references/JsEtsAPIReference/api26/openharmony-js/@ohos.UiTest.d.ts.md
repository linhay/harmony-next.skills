# @ohos.UiTest.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2022 Huawei Device Co., Ltd.
 * Licensed under the Apache License,Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,software
 * distributed under the License is distributed on an "ASIS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * The **UiTest** module provides APIs that you can use to simulate UI actions during testing, such as clicks, double-
 * clicks, long-clicks, and swipes.
 * This module provides the following functions:
 *
 * - [On<sup>9+</sup>]{@link On}: provides UI component feature description APIs for component filtering and matching.
 * - [Component<sup>9+</sup>]{@link Component}: represents a component on the UI and provides APIs for obtaining
 *   component attributes, clicking a component, scrolling to search for a component, and text injection.
 * - [Driver<sup>9+</sup>]{@link Driver}: works as the entry class and provides APIs for features such as component
 *   matching/search, key injection, coordinate clicking/sliding, and screenshot.
 * - [UiWindow<sup>9+</sup>]{@link UiWindow}: works as the entry class and provides APIs for obtaining window attributes,
 *   dragging windows, and adjusting window sizes.
 * - [By<sup>(deprecated)</sup>]{@link BY}: provides UI component feature description APIs for component filtering and
 *   matching. This API is supported since API version 8 and deprecated since API version 9.
 *   You are advised to use {@link On} instead.
 * - [UiComponent<sup>(deprecated)</sup>]{@link UiComponent}: represents a component on the UI and provides APIs for
 *   obtaining component attributes, clicking a component, scrolling to search for a component, and text injection.
 *   This API is supported since API version 8 and deprecated since API version 9.
 *   You are advised to use [Component<sup>9+</sup>]{@link Component} instead.
 * - [UiDriver<sup>(deprecated)</sup>]{@link UiDriver}: works as the entry class and provides APIs for features such as
 *   component matching/search, key injection, coordinate clicking/sliding, and screenshot.
 *   This API is supported since API version 8 and deprecated since API version 9.
 *   You are advised to use [Driver<sup>9+</sup>]{@link Driver} instead.
 *
 * > **NOTE**
 * >
 * > - The APIs of this module can be used only in <!--RP1-->[UITest](docroot://application-test/uitest-guidelines.md)<!--RP1End-->.
 * >
 * > - The APIs of this module do not support concurrent calls.
 *
 * @file
 * @kit TestKit
 *
 */
import { Callback } from './@ohos.base';
/**
 * Enumerates the match patterns supported for component attributes.
 *
 * @syscap SystemCapability.Test.UiTest
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 8
 */
declare enum MatchPattern {
    /**
     * Equals the given value.
     *
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     * @test
     */
    EQUALS = 0,
    /**
     * Contains the given value.
     *
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     * @test
     */
    CONTAINS = 1,
    /**
     * Starts with the given value.
     *
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     * @test
     */
    STARTS_WITH = 2,
    /**
     * Ends with the given value.
     *
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     * @test
     */
    ENDS_WITH = 3,
    /**
     * Uses regular expression matching.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 18
     * @test
     */
    REG_EXP = 4,
    /**
     * Uses case-insensitive regular expression matching.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 18
     * @test
     */
    REG_EXP_ICASE = 5
}
/**
 * The UiTest framework provides a wide range of UI component feature description APIs in the **By** class to filter and
 * match components.
 *
 * The APIs provided by the **By** class exhibit the following features:
 *
 * 1. Allow one or more attributes as the match conditions.
 *    For example, you can specify both the **text** and **id** attributes to find the target component.
 * 2. Provide multiple match patterns for component attributes.
 * 3. Support absolute positioning and relative positioning for components.
 *    APIs such as [By.isBefore<sup>(deprecated)</sup>]{@link By#isBefore} and [By.isAfter<sup>(deprecated)</sup>]{@link By#isAfter}
 *    can be used to specify the features of adjacent components to assist positioning.
 *
 * All APIs provided in the **By** class are synchronous. You are advised to use the static constructor **BY** to create
 * a **By** object in chain mode.
 *
 * @syscap SystemCapability.Test.UiTest
 * @since 8
 * @deprecated since 9
 * @useinstead On
 */
declare class By {
    /**
     * Specifies the text attribute of the target component. Multiple match patterns are supported.
     *
     * @param { string } txt - Component text, used to match the target component.
     * @param { MatchPattern } pattern - Match pattern {@link MatchPattern}.
     *     <br>Default value: {@link MatchPattern.EQUALS}
     * @returns { By } - **By** object that matches the text attribute of the target component.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead On#text
     * @test
     */
    text(txt: string, pattern?: MatchPattern): By;
    /**
     * Specifies the key attribute of the target component.
     *
     * @param { string } key - Component key.
     * @returns { By } - **By** object that matches the key attribute of the target component.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead On#id(id: string)
     * @test
     */
    key(key: string): By;
    /**
     * Specifies the ID attribute of the target component.
     *
     * @param { number } id - Component ID.
     * @returns { By } - **By** object that matches the ID attribute of the target component.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead On#id(id: string)
     * @test
     */
    id(id: number): By;
    /**
     * Specifies the type attribute of the target component.
     *
     * @param { string } tp - Component type.
     * @returns { By } - **By** object that matches the type attribute of the target component.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead On#type(tp: string)
     * @test
     */
    type(tp: string): By;
    /**
     * Specifies the clickable attribute of the target component.
     *
     * @param { boolean } b - Clickable status of the component. The value **true** indicates that the component is clickable,
     *     and **false** indicates the opposite. Default value: **true**
     * @returns { By } - **By** object that matches the clickable attribute of the target component.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead On#clickable
     * @test
     */
    clickable(b?: boolean): By;
    /**
     * Specifies the scrollable attribute of the target component.
     *
     * @param { boolean } b - Scrollable status of the component. The value **true** indicates that the component is scrollable
     *     , and **false** indicates the opposite. Default value: **true**
     * @returns { By } - **By** object that matches the scrollable attribute of the target component.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead On#scrollable
     * @test
     */
    scrollable(b?: boolean): By;
    /**
     * Specifies the enabled attribute of the target component.
     *
     * @param { boolean } b - Enabled status of the component. The value **true** indicates that the component is enabled, and
     *     **false** indicates the opposite. Default value: **true**
     * @returns { By } - **By** object that matches the enabled attribute of the target component.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead On#enabled
     * @test
     */
    enabled(b?: boolean): By;
    /**
     * Specifies the focused attribute of the target component.
     *
     * @param { boolean } b - Focused status of the component. The value **true** indicates that the component is focused, and
     *     **false** indicates the opposite. Default value: **true**
     * @returns { By } - **By** object that matches the focused attribute of the target component.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead On#focused
     * @test
     */
    focused(b?: boolean): By;
    /**
     * Specifies the selected status of the target component.
     *
     * @param { boolean } b - Selected status of the component. The value **true** indicates that the component is selected,
     *     and **false** indicates the opposite. Default value: **true**
     * @returns { By } - **By** object that matches the selected attribute of the target component.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead On#selected
     * @test
     */
    selected(b?: boolean): By;
    /**
     * Specifies that the target component is located before the given attribute component.
     *
     * @param { By } by - Information about the attribute component.
     * @returns { By } - **By** object.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead On#isBefore(on: On)
     * @test
     */
    isBefore(by: By): By;
    /**
     * Specifies that the target component is located after the given attribute component.
     *
     * @param { By } by - Information about the attribute component.
     * @returns { By } - **By** object.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead On#isAfter(on: On)
     * @test
     */
    isAfter(by: By): By;
}
/**
 * In **UiTest**, the **UiComponent** class represents a component on the UI and provides APIs for obtaining component
 * attributes, clicking a component, scrolling to search for a component, and text injection.
 * All APIs provided in this class use a promise to return the result and must be invoked using **await**.
 *
 * @syscap SystemCapability.Test.UiTest
 * @since 8
 * @deprecated since 9
 * @useinstead Component
 * @test
 */
declare class UiComponent {
    /**
     * Clicks this component. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } - Promise that returns no value.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Component#click
     * @test
     */
    click(): Promise<void>;
    /**
     * Double-clicks this component. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } - Promise that returns no value.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Component#doubleClick
     * @test
     */
    doubleClick(): Promise<void>;
    /**
     * Long-clicks this component. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } - Promise that returns no value.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Component#longClick
     * @test
     */
    longClick(): Promise<void>;
    /**
     * Obtains the ID of this component. This API uses a promise to return the result.
     *
     * @returns { Promise<number> } - Promise used to return the component ID.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Component#getId
     * @test
     */
    getId(): Promise<number>;
    /**
     * Obtains the key of this component. This API uses a promise to return the result.
     *
     * @returns { Promise<string> } - Promise used to return the key value.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Component#getId
     * @test
     */
    getKey(): Promise<string>;
    /**
     * Obtains the text information of this component. This API uses a promise to return the result.
     *
     * @returns { Promise<string> } - Promise used to return the text information of the component.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Component#getText
     * @test
     */
    getText(): Promise<string>;
    /**
     * Obtains the type of this component. This API uses a promise to return the result.
     *
     * @returns { Promise<string> } - Promise used to return the component type.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Component#getType
     * @test
     */
    getType(): Promise<string>;
    /**
     * Obtains the clickable status of this component. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } - Promise used to return whether the component is clickable. The value **true** indicates
     *     that the component is clickable, and **false** indicates the opposite.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Component#isClickable
     * @test
     */
    isClickable(): Promise<boolean>;
    /**
     * Obtains the scrollable status of this component. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } - Promise used to return whether the component is scrollable. The value **true** indicates
     *     that the component is scrollable, and **false** indicates the opposite.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Component#isScrollable
     * @test
     */
    isScrollable(): Promise<boolean>;
    /**
     * Obtains the enabled status of this component. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } - Promise used to return whether the component is enabled. The value **true** indicates
     *     that the component is enabled, and **false** indicates the opposite.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Component#isEnabled
     * @test
     */
    isEnabled(): Promise<boolean>;
    /**
     * Obtains the focused status of this component. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } - Promise used to return whether the component is focused. The value **true** indicates
     *     that the component is focused, and **false** indicates the opposite.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Component#isFocused
     * @test
     */
    isFocused(): Promise<boolean>;
    /**
     * Obtains the selected status of this component. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } - Promise used to return whether the component is selected. The value **true** indicates
     *     that the component is selected, and **false** indicates the opposite.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Component#isSelected
     * @test
     */
    isSelected(): Promise<boolean>;
    /**
     * Inputs text to a component. This API takes effect only for editable text components. This API uses a promise to
     * return the result.
     *
     * @param { string } text - Text to enter.
     * @returns { Promise<void> } - Promise that returns no value.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Component#inputText(text: string)
     * @test
     */
    inputText(text: string): Promise<void>;
    /**
     * Scrolls on this component to search for the target component (applicable to components that support scrolling, such
     * as **List**). This API uses a promise to return the result.
     *
     * @param { By } by - Attributes of the target component.
     * @returns { Promise<UiComponent> } - Promise used to return the target component.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Component#scrollSearch(on: On)
     * @test
     */
    scrollSearch(by: By): Promise<UiComponent>;
}
/**
 * The **UiDriver** class is the main entry to the UiTest framework. It provides APIs for features such as component
 * matching/search, key injection, coordinate clicking/sliding, and screenshot.
 * All APIs provided by this class, except **UiDriver.create()**, use a promise to return the result and must be invoked
 * using **await**.
 *
 * @syscap SystemCapability.Test.UiTest
 * @since 8
 * @deprecated since 9
 * @useinstead Driver
 * @test
 */
declare class UiDriver {
    /**
     * Creates a **UiDriver** object and returns the object created. This API is a static API.
     *
     * > **NOTE**
     * >
     * > This method is supported since API version 8 and deprecated since API version 9. You are advised to use
     * > [create<sup>9+</sup>]{@link Driver#create} instead.
     *
     * @returns { UiDriver } - **UiDriver** object created.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Driver#create
     * @test
     */
    static create(): UiDriver;
    /**
     * Delays this **UiDriver** object within the specified duration. This API uses a promise to return the result.
     *
     * @param { number } duration - Duration of time.
     *     <br>Unit: ms
     * @returns { Promise<void> } - Promise that returns no value.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Driver#delayMs
     * @test
     */
    delayMs(duration: number): Promise<void>;
    /**
     * Searches this **UiDriver** object for the target component that matches the given attributes. This API uses a
     * promise to return the result.
     *
     * @param { By } by - Attributes of the target component.
     * @returns { Promise<UiComponent> } - Promise used to return the component.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Driver#findComponent(on: On)
     * @test
     */
    findComponent(by: By): Promise<UiComponent>;
    /**
     * Searches this **UiDriver** object for all components that match the given attributes. This API uses a promise to
     * return the result.
     *
     * @param { By } by - Attributes of the target component.
     * @returns { Promise<Array<UiComponent>> } - Promise used to return the list of components.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Driver#findComponents(on: On)
     * @test
     */
    findComponents(by: By): Promise<Array<UiComponent>>;
    /**
     * Asserts that a component that matches the given attributes exists on the current page. If the component does not
     * exist, the API throws a JS exception, causing the current test case to fail. This API uses a promise to return the
     * result.
     *
     * @param { By } by - Attributes of the target component.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws {BusinessError} 401 - if the input parameters are invalid.
     * @throws {BusinessError} 17000002 - The API does not support concurrent calls.
     * @throws {BusinessError} 17000003 - if the assertion failed.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Driver#assertComponentExist
     * @test
     */
    assertComponentExist(by: By): Promise<void>;
    /**
     * Presses the Back button on this **UiDriver** object. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } - Promise that returns no value.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Driver#pressBack()
     * @test
     */
    pressBack(): Promise<void>;
    /**
     * Triggers the key of this **UiDriver** object that matches the given key code. This API uses a promise to return the
     * result.
     *
     * @param { number } keyCode - Key value. The value is an integer greater than or equal to 0.
     *     For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
     * @returns { Promise<void> } - Promise that returns no value.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Driver#triggerKey(keyCode: int)
     * @test
     */
    triggerKey(keyCode: number): Promise<void>;
    /**
     * Clicks a specific point of this **UiDriver** object based on the given coordinates. This API uses a promise to
     * return the result.
     *
     * @param { number } x - Number, which indicates the horizontal coordinate of the target point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @param { number } y - Number, which indicates the vertical coordinate of the target point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @returns { Promise<void> } - Promise that returns no value.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Component#click
     * @test
     */
    click(x: number, y: number): Promise<void>;
    /**
     * Double-clicks a specific point of this **UiDriver** object based on the given coordinates. This API uses a promise
     * to return the result.
     *
     * @param { number } x - Number, which indicates the horizontal coordinate of the target point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @param { number } y - Number, which indicates the vertical coordinate of the target point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @returns { Promise<void> } - Promise that returns no value.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Component#doubleClick
     * @test
     */
    doubleClick(x: number, y: number): Promise<void>;
    /**
     * Long-clicks a specific point of this **UiDriver** object based on the given coordinates. This API uses a promise to
     * return the result.
     *
     * @param { number } x - Number, which indicates the horizontal coordinate of the target point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @param { number } y - Number, which indicates the vertical coordinate of the target point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @returns { Promise<void> } - Promise that returns no value.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Component#longClick
     * @test
     */
    longClick(x: number, y: number): Promise<void>;
    /**
     * Swipes on this **UiDriver** object from the start point to the end point based on the given coordinates. This API
     *  uses a promise to return the result.
     *
     * @param { number } startx - Number, which indicates the horizontal coordinate of the start point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @param { number } starty - Number, which indicates the vertical coordinate of the start point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @param { number } endx - Number, which indicates the horizontal coordinate of the target point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @param { number } endy - Number, which indicates the vertical coordinate of the target point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @returns { Promise<void> } - Promise that returns no value.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Driver#swipe
     * @test
     */
    swipe(startx: number, starty: number, endx: number, endy: number): Promise<void>;
    /**
     * Captures the current screen of this **UiDriver** object and saves it as a PNG image to the given save path. This
     * API uses a promise to return the result.
     *
     * @param { string } savePath - File save path.
     * @returns { Promise<boolean> } - Promise used to return whether the screenshot operation is successful. The value **true*
     *     The value **true** indicates the screenshot operation is successful, and **false** indicates the opposite.
     * @syscap SystemCapability.Test.UiTest
     * @since 8
     * @deprecated since 9
     * @useinstead Driver#screenCap(savePath: string)
     * @test
     */
    screenCap(savePath: string): Promise<boolean>;
}
/**
 * Enumerates the window modes.
 *
 * @syscap SystemCapability.Test.UiTest
 * @atomicservice [since 11]
 * @since 9
 */
declare enum WindowMode {
    /**
     * Full-screen mode.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    FULLSCREEN = 0,
    /**
     * Primary window mode.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    PRIMARY = 1,
    /**
     * Secondary window mode.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    SECONDARY = 2,
    /**
     * Floating window mode.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    FLOATING = 3
}
/**
 * Enumerates the directions in which a window can be resized.
 *
 * @syscap SystemCapability.Test.UiTest
 * @atomicservice [since 11]
 * @since 9
 */
declare enum ResizeDirection {
    /**
     * Left.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    LEFT = 0,
    /**
     * Right.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    RIGHT = 1,
    /**
     * Up.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    UP = 2,
    /**
     * Down.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    DOWN = 3,
    /**
     * Upper left.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    LEFT_UP = 4,
    /**
     * Lower left.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    LEFT_DOWN = 5,
    /**
     * Upper right.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    RIGHT_UP = 6,
    /**
     * Lower right.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    RIGHT_DOWN = 7
}
/**
 * Describes the display rotation of the device.
 *
 * @syscap SystemCapability.Test.UiTest
 * @crossplatform [since 26.0.0]
 * @atomicservice [since 11]
 * @since 9
 */
declare enum DisplayRotation {
    /**
     * The device display is not rotated and is in its original vertical orientation.
     *
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 26.0.0]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    ROTATION_0 = 0,
    /**
     * The device display rotates 90° clockwise and is in landscape orientation.
     *
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 26.0.0]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    ROTATION_90 = 1,
    /**
     * The device display rotates 180° clockwise and is in reverse vertical orientation.
     *
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 26.0.0]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    ROTATION_180 = 2,
    /**
     * The device display rotates 270° clockwise and is in reverse landscape orientation.
     *
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 26.0.0]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    ROTATION_270 = 3
}
/**
 * Represents the point on the device screen.
 *
 * @syscap SystemCapability.Test.UiTest
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare interface Point {
    /**
     * Horizontal coordinate of a coordinate point. The value is an integer greater than 0.
     *
     * @readonly [since 9 - 19]
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    x: number;
    /**
     * Vertical coordinate of a coordinate point. The value is an integer greater than 0.
     *
     * @readonly [since 9 - 19]
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    y: number;
    /**
     * ID of the display to which the coordinate point belongs. The value is an integer greater than or equal to 0. The
     * default value is the default screen ID of the device.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     */
    displayId?: number;
}
/**
 * Represents the rectangle area on the device screen.
 *
 * @syscap SystemCapability.Test.UiTest
 * @crossplatform [since 12]
 * @atomicservice [since 11]
 * @since 9
 */
declare interface Rect {
    /**
     * X coordinate of the upper left corner of the component border. The value is an integer greater than 0.
     *     <br>Unit: px
     * @readonly [since 9 - 19]
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 9
     */
    left: number;
    /**
     * Y coordinate of the upper left corner of the component border. The value is an integer greater than 0.
     *     <br>Unit: px
     * @readonly [since 9 - 19]
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 9
     */
    top: number;
    /**
     * X coordinate of the lower right corner of the component border. The value is an integer greater than 0.
     *     <br>Unit: px
     * @readonly [since 9 - 19]
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 9
     */
    right: number;
    /**
     * Y coordinate of the lower right corner of the component border. The value is an integer greater than 0.
     *     <br>Unit: px
     * @readonly [since 9 - 19]
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 9
     */
    bottom: number;
    /**
     * ID of the display to which the component border belongs. The value is an integer greater than or equal to 0.
     *     <br>Default value: the default screen ID of the device.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     */
    displayId?: number;
}
/**
 * Provides the flag attributes of this window.
 *
 * @syscap SystemCapability.Test.UiTest
 * @atomicservice [since 11]
 * @since 9
 */
declare interface WindowFilter {
    /**
     * Bundle name of the application to which the window belongs. The default value is empty.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     */
    bundleName?: string;
    /**
     * Title of the window. The default value is empty.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     */
    title?: string;
    /**
     * Whether the window is focused. The value **true** indicates that the window is focused, and **false** indicates the
     *  opposite. The default value is **false**.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     */
    focused?: boolean;
    /**
     * Whether the window is interacting with the user. The value **true** indicates that the window is interacting with
     * the user, and **false** indicates the opposite.
     *
     * This API is deprecated since API version 11. You are advised to use the **active** API instead.
     *
     * @syscap SystemCapability.Test.UiTest
     * @since 9
     * @deprecated since 11
     * @useinstead ohos.UiTest.WindowFilter#active
     */
    actived?: boolean;
    /**
     * Whether the window is interacting with the user. The value **true** indicates that the window is interacting with
     * the user, and **false** indicates the opposite.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 11
     */
    active?: boolean;
    /**
     * ID of the display to which the window belongs. The value is an integer greater than or equal to 0. The default
     * value is the default screen ID of the device.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     */
    displayId?: number;
}
/**
 * Enumerates the window change event types that can be listened for.
 *
 * @syscap SystemCapability.Test.UiTest
 * @atomicservice
 * @since 22
 */
declare enum WindowChangeType {
    /**
     * Non-window change event.
     *      <br>Note: This value can only be used as a return value. If it is passed in an API, an exception will be thrown.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    WINDOW_UNDEFINED = 0,
    /**
     * Window adding event.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    WINDOW_ADDED = 1,
    /**
     * Window removing event.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    WINDOW_REMOVED = 2,
    /**
     * Window bounds change event.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    WINDOW_BOUNDS_CHANGED = 3
}
/**
 * Enumerates the component operation event types that can be listened for.
 *
 * @syscap SystemCapability.Test.UiTest
 * @atomicservice
 * @since 22
 */
declare enum ComponentEventType {
    /**
     * Non-component operation event.
     *
     * Note: This value can only be used as a return value. If it is passed in an API, an exception will be thrown.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    COMPONENT_UNDEFINED = 0,
    /**
     * Component clicked event.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    COMPONENT_CLICKED = 1,
    /**
     * Component long-clicked event.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    COMPONENT_LONG_CLICKED = 2,
    /**
     * Component scroll start event.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    COMPONENT_SCROLL_START = 3,
    /**
     * Component scroll end event.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    COMPONENT_SCROLL_END = 4,
    /**
     * Text change event of the [text input component](docroot://ui/arkts-common-components-text-input.md).
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    COMPONENT_TEXT_CHANGED = 5
}
/**
 * Describes the extended configuration of window change event listening,
 * which is used to specify the listening process configuration and event filtering conditions.
 *
 * @syscap SystemCapability.Test.UiTest
 * @atomicservice
 * @since 22
 * @test
 */
declare interface WindowChangeOptions {
    /**
     * Listening timeout interval, to prevent listening failures casued by event notification delay.
     *     <br>Value range: The value should be >= 500
     *     <br>Default value: 10000
     *     <br>Unit: ms
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    timeout?: number;
    /**
     * Bundle name of the window to be listened for. By default, all windows are listened for.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    bundleName?: string;
}
/**
 * Describes the extended configuration of component operation event listening,
 * which is used to specify the listening process configuration and event filtering conditions.
 *
 * @syscap SystemCapability.Test.UiTest
 * @atomicservice
 * @since 22
 * @test
 */
declare interface ComponentEventOptions {
    /**
     * Listening timeout interval , to prevent listening failures casued by event notification delay.
     * <br>Value range: The value should be >= 500
     * <br>Default value: 10000
     *     <br>Unit: ms
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    timeout?: number;
    /**
     * Attribute requirements of the target component to listen for. By default, all components are listened for.
     * **Note**: Only components with specified attributes can be listened for. Components with relative positions such as
     * **On.isBefore**, **On.isAfter**, and **On.within** cannot be listened for.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    on?: On;
}
/**
 * Provides information about the UI event.
 *
 * @syscap SystemCapability.Test.UiTest
 * @atomicservice [since 11]
 * @since 10
 * @test
 */
declare interface UIElementInfo {
    /**
     * Bundle name of the application.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 10
     * @test
     */
    readonly bundleName: string;
    /**
     * Component or window type.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 10
     * @test
     */
    readonly type: string;
    /**
     * Text information of the component or window.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 10
     * @test
     */
    readonly text: string;
    /**
     * Window change event type.
     * If the event is not a window change event, {@link WindowChangeType.WINDOW_UNDEFINED} is returned.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    readonly windowChangeType?: WindowChangeType;
    /**
     * Component operation event type.
     * If it is not a component operation event, {@link ComponentEventType.COMPONENT_UNDEFINED} is returned.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    readonly componentEventType?: ComponentEventType;
    /**
     * ID of the window where the component belongs.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    readonly windowId?: number;
    /**
     * Component ID. If it is not a component operation event, an empty string is returned.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    readonly componentId?: string;
    /**
     * The rect of the component, set all attributes of rect to 0 if it's a window.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    readonly componentRect?: Rect;
}
/**
 * Observer to monitor UI events.
 *
 * @syscap SystemCapability.Test.UiTest
 * @atomicservice [since 11]
 * @since 10
 * @test
 */
declare interface UIEventObserver {
    /**
     * Subscribes to events of the toast component. This API uses a callback to return the result.
     *
     * @param { 'toastShow' } type - Event type. The value is fixed at **'toastShow'**.
     * @param { Callback<UIElementInfo> } callback - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 10
     * @test
     */
    once(type: 'toastShow', callback: Callback<UIElementInfo>): void;
    /**
     * Subscribes to events of the dialog component. This API uses a callback to return the result.
     *
     * @param { 'dialogShow' } type - Event type. The value is fixed at **'dialogShow'**.
     * @param { Callback<UIElementInfo> } callback - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 10
     * @test
     */
    once(type: 'dialogShow', callback: Callback<UIElementInfo>): void;
    /**
     * Starts listening for window change events of the specified type with extended configuration supported. This API
     * triggers a callback when a specified window change event is detected.
     * This API can be used only in [free windows](docroot://windowmanager/window-terminology.md#free-windows) mode.
     *
     * @param { 'windowChange' } type - Type of the event to subscribe to, which can be **windowChange**. This event is
     *     triggered when the window changes.
     * @param { WindowChangeType } windowChangeType - Type of the window change event.
     * @param { WindowChangeOptions } options - Extended configuration, including the listening timeout interval and the
     *      bundle name of the window to be listened for.
     * @param { Callback<UIElementInfo> } callback - Callback triggered to return event information when an event occurs.
     * @throws { BusinessError } 17000005 - This operation is not supported.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    once(type: 'windowChange', windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void;
    /**
     * Starts listening for component operation events of the specified type with extended configuration supported. This
     * API triggers a callback when a specified component operation event is detected.
     *
     * @param { 'componentEventOccur' } type - Type of the event to subscribe to, which can be **componentEventOccur**.
     *     This event is triggered when the component operation is detected.
     * @param { ComponentEventType } componentEventType - Type of the component operation event.
     * @param { ComponentEventOptions } options - Extended configuration, including the listening timeout interval and
     *     the matching condition of the component to be listened for.
     * @param { Callback<UIElementInfo> } callback - Callback used to return the result.
     * @throws { BusinessError } 17000005 - This operation is not supported.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    once(type: 'componentEventOccur', componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void;
}
/**
 * Describes the direction of a UI operation such as fling.
 *
 * @syscap SystemCapability.Test.UiTest
 * @crossplatform [since 12]
 * @atomicservice [since 11]
 * @since 10
 */
declare enum UiDirection {
    /**
     * Leftward.
     *
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     * @test
     */
    LEFT = 0,
    /**
     * Rightward.
     *
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     * @test
     */
    RIGHT = 1,
    /**
     * Upward.
     *
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     * @test
     */
    UP = 2,
    /**
     * Downward.
     *
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     * @test
     */
    DOWN = 3
}
/**
 * Describes the injected simulated mouse button.
 *
 * @syscap SystemCapability.Test.UiTest
 * @atomicservice [since 11]
 * @since 10
 * @test
 */
declare enum MouseButton {
    /**
     * Left button on the mouse.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 10
     * @test
     */
    MOUSE_BUTTON_LEFT = 0,
    /**
     * Right button on the mouse.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 10
     * @test
     */
    MOUSE_BUTTON_RIGHT = 1,
    /**
     * MIDDLE button on the mouse.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 10
     * @test
     */
    MOUSE_BUTTON_MIDDLE = 2
}
/**
 * Describes information about the touchpad swipe gesture option.
 * @syscap SystemCapability.Test.UiTest
 * @atomicservice
 * @since 18
 * @test
 */
declare interface TouchPadSwipeOptions {
    /**
     * Whether the swipe gesture stays on the touchpad for 1s before it is lifted.
     * The value **true** indicates that the swipe gesture stays on the touchpad for 1s, and **false** indicates the opposite.
     * <br>Default value: false
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 18
     * @test
     */
    stay?: boolean;
    /**
     * Swipe speed.
     * <br>Value range:[200, 40000]
     * <br>Unit: px/s.
     * <br>Throws error code 17000007 if negative.
     * <br>Default value: 2000
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 18
     * @test
     */
    speed?: number;
}
/**
 * Describes the text input mode.
 * @syscap SystemCapability.Test.UiTest
 * @atomicservice
 * @since 20
 * @test
 */
declare interface InputTextMode {
    /**
     * Whether to copy and paste text. The value **true** means to copy and paste text, and **false** means to type text.
     * Default value: **false**
     *
     * **Note**: If the input text contains Chinese characters, special characters, or the text length exceeds 200
     * characters, the text is copied and pasted regardless of the value of this parameter.
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    paste?: boolean;
    /**
     * Whether to input text in addition mode. The value **true** means to input text in addition mode, and **false**
     * means the opposite. Default value: **false**
     *
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    addition?: boolean;
}
/**
 * Represents the options for key operations.
 *
 * @syscap SystemCapability.Test.UiTest
 * @FaAndStageModel
 * @atomicservice
 * @since 26.0.0
 * @test
 */
declare interface KeyOptions {
    /**
     * The first keyCode to press during the operation.
     * If not set, no key event will be injected.
     * Setting only key2 without key1 will result in a BusinessError 17000007.
     *
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    key1?: number;
    /**
     * The second KeyCode to press during the operation.
     * If not set, no key event will be injected.
     * Setting only key2 without key1 will result in a BusinessError 17000007.
     *
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    key2?: number;
}
/**
 * Common options for touch operations.
 *
 * @syscap SystemCapability.Test.UiTest
 * @FaAndStageModel
 * @atomicservice
 * @since 26.0.0
 * @test
 */
declare interface TouchOptions {
    /**
     * Speed of touch action.
     * <br>Value range:[200, 40000]
     * <br>Unit: px/s.
     * <br>Throws error code 17000007 if negative.
     * <br>Default value: 600
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    speed?: number;
    /**
     * Duration of the operation in milliseconds.
     * <br>Value range: The value should be >= 1500
     * <br>Unit: ms
     * <br>Default value: 1500
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    duration?: number;
    /**
     * The pressure of the touch.
     * <br>Value range:[0.0, 1.0]
     * <br>Default value: 1.0
     *
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    pressure?: number;
}
/**
 * Pen key type enum.
 *
 * @syscap SystemCapability.Test.UiTest
 * @FaAndStageModel
 * @atomicservice
 * @since 26.0.0
 * @test
 */
declare enum PenKey {
    /**
     * Handwriting key.
     *
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    HANDWRITING = 0,
    /**
     * Smart key.
     *
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    SMART = 1,
    /**
     * Air mouse key.
     *
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    AIR_MOUSE = 2
}
/**
 * Pen key operation type enum.
 *
 * @syscap SystemCapability.Test.UiTest
 * @FaAndStageModel
 * @atomicservice
 * @since 26.0.0
 * @test
 */
declare enum PenKeyOperation {
    /**
     * Single click.
     *
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    CLICK = 0,
    /**
     * Double click.
     *
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    DOUBLE_CLICK = 1
}
/**
 * Pen mode enum.
 *
 * @syscap SystemCapability.Test.UiTest
 * @FaAndStageModel
 * @atomicservice
 * @since 26.0.0
 * @test
 */
declare enum PenMode {
    /**
     * Handwriting mode.
     *
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    HANDWRITING = 0,
    /**
     * Air mouse mode.
     *
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    AIR_MOUSE = 1
}
/**
 * Pen key operation options.
 *
 * @syscap SystemCapability.Test.UiTest
 * @FaAndStageModel
 * @atomicservice
 * @since 26.0.0
 * @test
 */
declare interface PenKeyOperationOptions {
    /**
     * The coordinate point for air mouse mode operations. Required when key is AIR_MOUSE in air mouse mode.
     *
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    point?: Point;
}
/**
 * Since API version 9, the UiTest framework provides a wide range of UI component feature description APIs in the
 * **On** class to filter and match components.
 *
 * The APIs provided by the **On** class exhibit the following features:
 *
 * 1. Allow one or more attributes as the match conditions.
 *    For example, you can specify both the **text** and **id** attributes to find the target component.
 * 2. Provide multiple match patterns for component attributes.
 * 3. Support absolute positioning and relative positioning for components.
 *    APIs such as [ON.isBefore]{@link On.isBefore(on: On)} and [ON.isAfter]{@link On.isAfter(on: On)} can be used to specify
 *    the features of adjacent components to assist positioning.
 *
 * All APIs provided in the **On** class are synchronous. You are advised to use the static constructor **ON** to create
 * an **On** object in chain mode.
 *
 * @syscap SystemCapability.Test.UiTest
 * @crossplatform [since 12]
 * @atomicservice [since 11]
 * @since 9
 */
declare class On {
    /**
     * Specifies the text attribute of the target component. Multiple match patterns are supported.
     *
     * > **NOTE**
     * >
     * > If the [accessibilityLevel]{@link ./@internal/component/ets/common:CommonMethod#accessibilityLevel}
     * > of a component is set to **no** or **no-hide-descendants**, this API cannot be used to specify the text attribute
     * > of the target component for searching for the component. In this case, you can use the
     * > [On.originalText()]{@link On#originalText} API.
     *
     * @param { string } txt - Component text, used to match the target component.<!--RP2--><!--RP2End-->
     * @param { MatchPattern } [pattern] - Match pattern {@link MatchPattern} .
     *     <br>Default value: {@link MatchPattern.EQUALS}
     * @returns { On } - **On** object that matches the text attribute of the target component.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    text(txt: string, pattern?: MatchPattern): On;
    /**
     * Specifies the ID attribute of the target component.
     *
     * @param { string } id - Component ID.<!--RP2--><!--RP2End-->
     * @returns { On } - **On** object that matches the ID attribute of the target component.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    id(id: string): On;
    /**
     * Specifies the type attribute of the target component.
     *
     * @param { string } tp - Component type.<!--RP2--><!--RP2End-->
     * @returns { On } - **On** object that matches the type attribute of the target component.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    type(tp: string): On;
    /**
     * Specifies the clickable attribute of the target component.
     *
     * @param { boolean } [b] - Clickable status of the component. The value **true** indicates that the component is clickable
     *     , and **false** indicates the opposite. Default value: **true**<!--RP2--><!--RP2End-->
     * @returns { On } - **On** object that matches the clickable attribute of the target component.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter
     *     verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    clickable(b?: boolean): On;
    /**
     * Specifies the long-clickable attribute of the target component.
     *
     * @param { boolean } [b] - Long-clickable status of the component. The value **true** indicates that the component is long
     *     -clickable, and **false** indicates the opposite. Default value: **true**<!--RP2--><!--RP2End-->
     * @returns { On } - **On** object that matches the long-clickable attribute of the target component.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter
     *     verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    longClickable(b?: boolean): On;
    /**
     * Specifies the scrollable attribute of the target component.
     *
     * @param { boolean } [b] - Scrollable status of the component. The value **true** indicates that the component is
     *     scrollable, and **false** indicates the opposite. Default value: **true**<!--RP2--><!--RP2End-->
     * @returns { On } - **On** object that matches the scrollable attribute of the target component.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter
     *     verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    scrollable(b?: boolean): On;
    /**
     * Specifies the enabled attribute of the target component.
     *
     * @param { boolean } [b] - Enabled status of the component. The value **true** indicates that the component is enabled,
     *     and **false** indicates the opposite. Default value: **true**<!--RP2--><!--RP2End-->
     * @returns { On } - **On** object that matches the enabled attribute of the target component.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter
     *     verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    enabled(b?: boolean): On;
    /**
     * Specifies the focused attribute of the target component.
     *
     * @param { boolean } [b] - Focused status of the component. The value **true** indicates that the component is focused,
     *     and **false** indicates the opposite. Default value: **true**<!--RP2--><!--RP2End-->
     * @returns { On } - **On** object that matches the focused attribute of the target component.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter
     *     verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    focused(b?: boolean): On;
    /**
     * Specifies the selected attribute of the target component.
     *
     * @param { boolean } [b] - Selected status of the component. The value **true** indicates that the component is selected,
     *     and **false** indicates the opposite. Default value: **true**<!--RP2--><!--RP2End-->
     * @returns { On } - **On** object that matches the selected attribute of the target component.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter
     *     verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    selected(b?: boolean): On;
    /**
     * Specifies the checked attribute of the target component.
     *
     * @param { boolean } [b] - Checked status of the component. The value **true** indicates that the component is checked,
     *     and **false** indicates the opposite. Default value: **true**<!--RP2--><!--RP2End-->
     * @returns { On } - **On** object that matches the checked attribute of the target component.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter
     *     verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    checked(b?: boolean): On;
    /**
     * Specifies the checkable attribute of the target component.
     *
     * @param { boolean } [b] - Checkable status of the component. The value **true** indicates that the component is checkable
     *     , and **false** indicates the opposite. Default value: **true**<!--RP2--><!--RP2End-->
     * @returns { On } - **On** object that matches the checkable attribute of the target component.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    checkable(b?: boolean): On;
    /**
     * Specifies that the target component is located before the given attribute component.
     *
     * @param { On } on - Information about the attribute component.<!--RP3--><!--RP3End-->
     * @returns { On } - **On** object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    isBefore(on: On): On;
    /**
     * Requires that the target Component which is before another Component that specified by the given {@link Component}
     * object,used to locate Component relatively.
     *
     * @param { Component } com - describes the Component which the target one is in front of.
     * @returns { On } this {@link On} object.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    beforeComponent(com: Component): On;
    /**
     * Specifies that the target component is located after the given attribute component.
     *
     * @param { On } on - Information about the attribute component.<!--RP3--><!--RP3End-->
     * @returns { On } - **On** object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    isAfter(on: On): On;
    /**
     * Requires that the target Component which is after another Component that specified by the given {@link Component}
     * object,used to locate Component relatively.
     *
     * @param { Component } com - describes the Component which the target one is in back of.
     * @returns { On } this {@link On} object.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    afterComponent(com: Component): On;
    /**
     * Specifies that the target component is located within the given attribute component.
     *
     * @param { On } on - Information about the attribute component.<!--RP3--><!--RP3End-->
     * @returns { On } - **On** object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 10
     * @test
     */
    within(on: On): On;
    /**
     * Requires that the target Component which is inside of another Component that specified by the given {@link Component}
     * object,used to locate Component relatively.
     *
     * @param { Component } com - describes the Component which the target one is inside of.
     * @returns { On } this {@link On} object.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    withinComponent(com: Component): On;
    /**
     * Specifies that the target component is located within the given application window.
     *
     * @param { string } bundleName - Bundle name of the application window.<!--RP2--><!--RP2End-->
     * @returns { On } - **On** object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 10
     * @test
     */
    inWindow(bundleName: string): On;
    /**
     * Obtains the component object on the specified display.
     *
     * @param { number } displayId - ID of the display to which the component belongs. The value is an integer greater than
     *     or equal to 0.
     *     <br>**Note**: If the input **displayId** does not exist, the exception **17000007** is reported. You can use
     *     [getAllDisplays]{@link @ohos.display:display.getAllDisplays(callback: AsyncCallback<Array<Display>>)} to obtain
     *     all current **display** objects and use them to obtain the corresponding display IDs.<!--RP2--><!--RP2End-->
     * @returns { On } - The **On** object of the display to which the specified component belongs.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    belongingDisplay(displayId: number): On;
    /**
     * Specifies the description of the target component. Multiple match patterns are supported.
     *
     * @param { string } val - Description of the component.<!--RP2--><!--RP2End-->
     * @param { MatchPattern } [pattern] - Match pattern {@link MatchPattern} .
     *     <br>Default value: {@link MatchPattern.EQUALS}
     * @returns { On } - **On** object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 11
     * @test
     */
    description(val: string, pattern?: MatchPattern): On;
    /**
     * Specifies the **id** attribute and match pattern of the target component.
     *
     * @param { string } id - Component ID.<!--RP2--><!--RP2End-->
     * @param { MatchPattern } pattern - Text matching pattern {@link MatchPattern}.
     * @returns { On } - **On** object that matches the ID attribute of the target component.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 18
     * @test
     */
    id(id: string, pattern: MatchPattern): On;
    /**
     * Specifies the **type** attribute and match pattern of the target component.
     *
     * @param { string } tp - Component type.<!--RP2--><!--RP2End-->
     * @param { MatchPattern } pattern - Text matching pattern {@link MatchPattern}.
     * @returns { On } - **On** object that matches the type attribute of the target component.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 18
     * @test
     */
    type(tp: string, pattern: MatchPattern): On;
    /**
     * Obtains the component object of the specified hint text and returns the **On** object.
     *
     * @param { string } val - The specified hint text of the component.<!--RP2--><!--RP2End-->
     * @param { MatchPattern } [pattern] - Match pattern{@link MatchPattern}.
     *     <br>Default value: {@link MatchPattern.EQUALS}
     * @returns { On } - The **On** object of the specified hint text component.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 18
     * @test
     */
    hint(val: string, pattern?: MatchPattern): On;
    /**
     * Specifies the text content and text matching pattern of the component.
     *
     * > **NOTE**
     * >
     * > If the [accessibilityLevel]{@link ./@internal/component/ets/common:CommonMethod#accessibilityLevel}
     * > of a component is set to **no** or **no-hide-descendants**, this API can be used to specify the text attribute of
     * > the target component for searching for the component. In this case, the [On.text()]{@link On#text} API does not
     * > take effect.
     *
     * @param { string } text - Component text, used to match the target component.<!--RP2--><!--RP2End-->
     * @param { MatchPattern } [pattern] - Match pattern{@link MatchPattern}.
     *     <br>Default value: {@link MatchPattern.EQUALS}
     * @returns { On } - **On** object that matches the text attribute of the target component.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    originalText(text: string, pattern?: MatchPattern): On;
}
/**
 * Represents a component on the UI and provides APIs for obtaining component attributes, clicking a component,
 * scrolling to search for a component, and text injection.
 * All APIs provided in this class use a promise to return the result and must be invoked using **await**.
 *
 * @syscap SystemCapability.Test.UiTest
 * @crossplatform [since 12]
 * @atomicservice [since 11]
 * @since 9
 * @test
 */
declare class Component {
    /**
     * Clicks this component. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    click(): Promise<void>;
    /**
     * Double-clicks this component. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    doubleClick(): Promise<void>;
    /**
     * Long-clicks this component. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    longClick(): Promise<void>;
    /**
     * Obtains the ID of this component. This API uses a promise to return the result.
     *
     * @returns { Promise<string> } - Promise used to return the component ID.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    getId(): Promise<string>;
    /**
     * Obtains the ID of the display to which the component belongs. This API uses a promise to return the result.
     *
     * @returns { Promise<number> } - Promise used to return the ID of the display to which the component belongs.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    getDisplayId(): Promise<number>;
    /**
     * Obtains the text information of this component. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > If the [accessibilityLevel]{@link ./@internal/component/ets/common:CommonMethod#accessibilityLevel}
     * > attribute of the component is set to **no** or **no-hide-descendants**, this API cannot be used to obtain the
     * > text information of the component. In this case, you can use
     * > [Component.getOriginalText ()]{@link Component#getOriginalText} instead.
     *
     * @returns { Promise<string> } - Promise used to return the text information of the component.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    getText(): Promise<string>;
    /**
     * Obtains the type of this component. This API uses a promise to return the result.
     *
     * @returns { Promise<string> } - Promise used to return the component type.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    getType(): Promise<string>;
    /**
     * Obtains the clickable status of this component. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } - Promise used to return whether the component object is clickable.
     *     The value **true** indicates that the component is clickable, and **false** indicates the opposite.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    isClickable(): Promise<boolean>;
    /**
     * Obtains the clickable status of this component. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } - Promise used to return whether the component object is clickable.
     *     The value **true** indicates that the component is clickable, and **false** indicates the opposite.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    isLongClickable(): Promise<boolean>;
    /**
     * Obtains the scrollable status of this component. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } - Promise used to return whether the component object is scrollable.
     *     The value **true** indicates that the component is scrollable, and **false** indicates the opposite.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    isScrollable(): Promise<boolean>;
    /**
     * Obtains the enabled status of this component. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } - Promise used to return whether the component is enabled.
     *     The value **true** indicates that the component is enabled, and **false** indicates the opposite.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    isEnabled(): Promise<boolean>;
    /**
     * Checks whether a component is focused. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } - Promise used to return whether the component is focused.
     *     The value **true** indicates that the component is focused, and **false** indicates the opposite.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    isFocused(): Promise<boolean>;
    /**
     * Obtains the selected status of this component. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } - Promise used to return whether the component is selected.
     *     The value **true** indicates that the component is selected, and **false** indicates the opposite.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    isSelected(): Promise<boolean>;
    /**
     * Obtains the checked status of this component. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } - Promise used to return the checked status of the component object.
     *     The value **true** indicates indicates that the component is checked, and **false** indicates the opposite.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    isChecked(): Promise<boolean>;
    /**
     * Obtains the checkable status of this component. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } - Promise used to return whether the component object is checkable.
     *     The value **true** indicates indicates that the component is checkable, and **false** indicates the opposite.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    isCheckable(): Promise<boolean>;
    /**
     * Clears the original text in a component and inputs the specified text. This API takes effect only for editable
     * text components. This API uses a promise to return the result.
     *
     * @param { string } text - Input text. Currently, English, Chinese, and special characters are supported.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    inputText(text: string): Promise<void>;
    /**
     * Inputs text to a component in a specified text input mode. This API takes effect only for editable text
     * components. This API uses a promise to return the result.
     *
     * @param { string } text - Input text. Currently, English, Chinese, and special characters are supported.
     * @param { InputTextMode } mode - Text input mode.
     *     For details, see [InputTextMode]{@link InputTextMode}.
     *     <br> **Note**: If **InputTextMode.addition** is set to **true**, the specified text is added to the end of the
     *     existing text in the component. Otherwise, the specified text overwrites the existing text of the component.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Function can not work correctly due to limited device
     *     capabilities.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    inputText(text: string, mode: InputTextMode): Promise<void>;
    /**
     * Clears the text information of a component. This API takes effect only for editable text components. This API
     * uses a promise to return the result.
     *
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    clearText(): Promise<void>;
    /**
     * Scrolls to the top of this component. This API is applicable to components that support scrolling. This API uses
     * a promise to return the result.
     *
     * @param { number } [speed] - Scroll speed.
     *     <br>Value range:[200, 40000]
     *     <br>Unit: px/s.
     *     <br>Throws error code 401 if negative.
     *     <br>Default value: 600
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter
     *     verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    scrollToTop(speed?: number): Promise<void>;
    /**
     * Scrolls to the bottom of this component. This API is applicable to components that support scrolling. This API
     * uses a promise to return the result.
     *
     * @param { number } [speed] - Scroll speed.
     *     <br>Value range:[200, 40000]
     *     <br>Unit: px/s.
     *     <br>Throws error code 401 if negative.
     *     <br>Default value: 600
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter
     *     verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    scrollToBottom(speed?: number): Promise<void>;
    /**
     * Obtains the bounds information of this component. This API uses a promise to return the result.
     *
     * @returns { Promise<Rect> } - Promise used to return the bound information of the component object.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    getBounds(): Promise<Rect>;
    /**
     * Scrolls on this component to search for the target component. This API is applicable to components that support
     * scrolling. This API uses a promise to return the result.
     *
     * @param { On } on - Attributes of the target component.
     * @returns { Promise<Component> } - Promise used to return the target component.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    scrollSearch(on: On): Promise<Component>;
    /**
     * Obtains the center point of the area occupied by this component. This API uses a promise to return the result.
     *
     * @returns { Promise<Point> } - Promise used to return the center point of the area occupied by the component object.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    getBoundsCenter(): Promise<Point>;
    /**
     * Drags a component to the target component. This API uses a promise to return the result.
     *
     * @param { Component } target - Target component.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    dragTo(target: Component): Promise<void>;
    /**
     * Pinches out a component at the specified scale. This API uses a promise to return the result.
     *
     * @param { number } scale - Scale factor, which is a value greater than 1.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    pinchOut(scale: number): Promise<void>;
    /**
     * Pinches in a component at the specified scale. This API uses a promise to return the result.
     *
     * @param { number } scale - Scale factor, which is a value ranging from 0 to 1.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    pinchIn(scale: number): Promise<void>;
    /**
     * Obtains the description of this component. This API uses a promise to return the result.
     *
     * @returns { Promise<string> } - Promise used to return the description of the component.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 11
     * @test
     */
    getDescription(): Promise<string>;
    /**
     * Obtains the hint text of a component. This API uses a promise to return the result.
     *
     * @returns { Promise<string> } - Promise used to return the hint text of a component.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 18
     * @test
     */
    getHint(): Promise<string>;
    /**
     * Scrolls on this component to search for the target component. This API is applicable to components that support
     * scrolling. You can specify the scrolling direction and the offset between the scrolling start and end points and
     * the component border. This API uses a promise to return the result.
     *
     * @param { On } on - Attributes of the target component.
     * @param { boolean } [vertical] - Whether the search direction is vertical. The default value **true** indicates that the
     *     search direction is vertical. **false** indicates that the search direction is horizontal.
     * @param { number } [offset] - Offset from the scrolling start/end point to the component border, in pixels. The default
     *     value is **80**. The value is an integer greater than or equal to 0.
     *     <br>Default value: 80
     *     <br>Unit: px
     * @returns { Promise<Component> } - Promise used to return the target component.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 18
     * @test
     */
    scrollSearch(on: On, vertical?: boolean, offset?: number): Promise<Component>;
    /**
     * Obtains the text information of this component. This API uses a promise to return the result. If the
     * [accessibilityLevel]{@link ./@internal/component/ets/common:CommonMethod#accessibilityLevel}
     * attribute of the component is set to **no** or **no-hide-descendants**, this API can be used
     * to obtain the text information of the component, but [Component.getText()]{@link Component#getText} cannot.
     *
     * @returns { Promise<string> } - Promise used to return the text information of the component.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    getOriginalText(): Promise<string>;
}
/**
 * The **Driver** class is the main entry to the UiTest framework. It provides APIs for features such as component
 * matching/search, key injection, coordinate clicking/sliding, and screenshot.
 * All APIs provided by this class, except **Driver.create()**, use a promise to return the result and must be invoked
 * using **await**.
 *
 * @syscap SystemCapability.Test.UiTest
 * @crossplatform [since 12]
 * @atomicservice [since 11]
 * @since 9
 * @test
 */
declare class Driver {
    /**
     * Creates a **Driver** object and returns the object created. This API is a static API.
     *
     * @returns { Driver } - **{@link Driver}** object created.
     * @throws { BusinessError } 17000001 - Initialization failed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    static create(): Driver;
    /**
     * Delays execution for the specified duration. This API uses a promise to return the result.
     *
     * @param { number } duration - Specified time, in ms. The value is an integer greater than or equal to 0.
     *     <br>Unit: ms
     *     <br>Value range: The value should be >= 0
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    delayMs(duration: number): Promise<void>;
    /**
     * Searches for the target component based on the specified attributes. This API uses a promise to return the result.
     *
     * @param { On } on - Attributes of the target {@link Component}.
     * @returns { Promise<Component> } - Promise used to return the {@link Component} or undefined.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    findComponent(on: On): Promise<Component>;
    /**
     * Searches for a window based on the specified attributes. This API uses a promise to return the result.
     *
     * @param { WindowFilter } filter - Attributes of the target {@link UiWindow}.
     * @returns { Promise<UiWindow> } - Promise used to return the target {@link UiWindow}.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    findWindow(filter: WindowFilter): Promise<UiWindow>;
    /**
     * Searches for the target component based on the attributes within a specified time. This API uses a promise to
     * return the result.
     *
     * @param { On } on - Attributes of the target {@link Component}.
     * @param { number } time - Duration for searching for the target {@link Component}, in ms. The value is an integer greater than or
     *     equal to 0.
     *     <br>Unit: ms
     *     <br>Value range: The value should be >= 0
     * @returns { Promise<Component> } the first matched {@link Component} or undefined.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 26.0.0]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    waitForComponent(on: On, time: number): Promise<Component>;
    /**
     * Searches for all matched components based on the specified attributes and saves them in a list. This API uses a
     * promise to return the result.
     *
     * @param { On } on - Attributes of the target {@link Component}.
     * @returns { Promise<Array<Component>> } - Promise used to return the list of {@link Component}s.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    findComponents(on: On): Promise<Array<Component>>;
    /**
     * Asserts whether a component matches the specified attributes exists on the current page. This API uses a promise
     * to return the result.
     *
     * @param { On } on - Attributes of the target {@link Component}.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000003 - Assertion failed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    assertComponentExist(on: On): Promise<void>;
    /**
     * Presses the Back button. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    pressBack(): Promise<void>;
    /**
     * Presses the Back button on the specified screen. This API uses a promise to return the result.
     *
     * @param { number } displayId - Display ID. The value is an integer greater than or equal to 0.
     *     <br> **Note**: If the input **displayId** does not exist, the exception **17000007** is reported.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    pressBack(displayId: number): Promise<void>;
    /**
     * Triggers a key event by passing the key value. This API uses a promise to return the result.
     *
     * @param { number } keyCode - Key value. The value is an integer greater than or equal to 0.
     *     For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    triggerKey(keyCode: number): Promise<void>;
    /**
     * Triggers a key event by passing the key value on the specified screen. This API uses a promise to return the
     * result.
     *
     * @param { number } keyCode - Key value. The value is an integer greater than or equal to 0.
     *     For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
     * @param { number } displayId - Display ID. The value is an integer greater than or equal to 0.
     *     <br> **Note**: If the input **displayId** does not exist, the exception **401** is reported.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    triggerKey(keyCode: number, displayId: number): Promise<void>;
    /**
     * Triggers a combination key event based on the specified key values. This API uses a promise to return the result.
     * For example, if the value of **Key** is (2072, 2019), the combination key **Ctrl+C** that matches the value is
     * found and clicked.
     *
     * @param { number } key0 - First key value. The value is an integer greater than or equal to 0.
     *     For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
     * @param { number } key1 - Second key value. The value is an integer greater than or equal to 0.
     *     For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
     * @param { number } [key2] - Third key value. The value is an integer greater than or equal to 0.
     *     For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
     *     <br>Default value: 0
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    triggerCombineKeys(key0: number, key1: number, key2?: number): Promise<void>;
    /**
     * Triggers a combination key event based on the specified key values on the specified screen. This API uses a
     * promise to return the result. For example, if the value of **Key** is (2072, 2019), the combination key **Ctrl+C**
     *  that matches the value is found and clicked.
     *
     * @param { number } key0 - First key value. The value is an integer greater than or equal to 0.
     *     For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
     * @param { number } key1 - Second key value. The value is an integer greater than or equal to 0.
     *     For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
     * @param { number } [key2] - Third key value. The value is an integer greater than or equal to 0.
     *     For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
     *     <br>Default value: 0
     * @param { number } [displayId] - Display ID. The value is an integer greater than or equal to 0. The default value is the
     *     default display ID of the device.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    triggerCombineKeys(key0: number, key1: number, key2?: number, displayId?: number): Promise<void>;
    /**
     * Clicks the target coordinate point. This API uses a promise to return the result.
     *
     * @param { number } x - Number, which indicates the horizontal coordinate of the target point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @param { number } y - Number, which indicates the vertical coordinate of the target point. The value is an integer greater
     *     than or equal to 0.
     *     <br>Unit: px
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    click(x: number, y: number): Promise<void>;
    /**
     * Double-clicks the target coordinate point. This API uses a promise to return the result.
     *
     * @param { number } x - Number, which indicates the horizontal coordinate of the target point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @param { number } y - Number, which indicates the vertical coordinate of the target point. The value is an integer greater
     *     than or equal to 0.
     *     <br>Unit: px
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    doubleClick(x: number, y: number): Promise<void>;
    /**
     * Long-clicks the target coordinate point. This API uses a promise to return the result.
     *
     * @param { number } x - Number, which indicates the horizontal coordinate of the target point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @param { number } y - Number, which indicates the vertical coordinate of the target point. The value is an integer greater
     *     than or equal to 0.
     *     <br>Unit: px
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    longClick(x: number, y: number): Promise<void>;
    /**
     * Swipes from the start coordinate point to the target coordinate point. This API uses a promise to return the
     * result.
     *
     * @param { number } startx - Number, which indicates the horizontal coordinate of the start point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @param { number } starty - Number, which indicates the vertical coordinate of the start point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @param { number } endx - Number, which indicates the horizontal coordinate of the target point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @param { number } endy - Number, which indicates the vertical coordinate of the target point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @param { number } [speed] - Swipe speed, in px/s. The value ranges from 200 to 40000. If the set value is not in the range
     *     , the default value **600** is used.
     *     <br>Value range:[200, 40000]
     *     <br>Unit: px/s.
     *     <br>Throws error code 401 if negative.
     *     <br>Default value: 600
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    swipe(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>;
    /**
     * Drags from the start coordinate point to the target coordinate point. This API uses a promise to return the result
     * .
     *
     * @param { number } startx - Number, which indicates the horizontal coordinate of the start point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @param { number } starty - Number, which indicates the vertical coordinate of the start point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @param { number } endx - Number, which indicates the horizontal coordinate of the target point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @param { number } endy - Number, which indicates the vertical coordinate of the target point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @param { number } [speed] - Drag speed, in px/s. The value ranges from 200 to 40000. If the set value is not in the range
     *     , the default value **600** is used.
     *     <br>Value range:[200, 40000]
     *     <br>Unit: px/s.
     *     <br>Throws error code 401 if negative.
     *     <br>Default value: 600
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 26.0.0]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    drag(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>;
    /**
     * Clicks the target coordinate point. This API uses a promise to return the result.
     *
     * @param { Point } point - Point object, which is used to transfer the target point information.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    clickAt(point: Point): Promise<void>;
    /**
     * Click on the specified location on the screen, with optional touch options.
     *
     * @param { Point } point - the coordinate point where the finger touches the screen.
     * @param { TouchOptions } [options] - the options for the click operation.
     *                           Only the 'pressure' property is applicable for this method.
     *                           Setting other properties will result in a BusinessError 17000007.
     *                           Default value: Refer to the default value of TouchOptions.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    clickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>;
    /**
     * Double-clicks the target coordinate point. This API uses a promise to return the result.
     *
     * @param { Point } point - Point object, which is used to transfer the target point information.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    doubleClickAt(point: Point): Promise<void>;
    /**
     * Long-clicks the target coordinate point for a specified duration. This API uses a promise to return the result.
     *
     * @param { Point } point - Point object, which is used to transfer the target point information.
     * @param { number } [duration] - Long-click duration, in ms.
     *     <br>Value range: The value should be >= 1500
     *     <br>Unit: ms
     *     <br>Default value: 1500
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    longClickAt(point: Point, duration?: number): Promise<void>;
    /**
     * LongClick on the specified location on the screen, with optional touch settings.
     *
     * @param { Point } point - the coordinate point where the finger touches the screen.
     * @param { TouchOptions } [options] - the options for the long click operation.
     *                         Only the 'duration' and 'pressure' properties are applicable for this method.
     *                         Setting other properties will result in a BusinessError 17000007.
     *                         Default value: Refer to the default value of TouchOptions.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    longClickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>;
    /**
     * Swipes from the start coordinate point to the target coordinate point. This API uses a promise to return the
     * result.
     *
     * @param { Point } from - Point object, which transfers the coordinates of the start point and the ID of the display to
     *     which the start point belongs.
     * @param { Point } to - Point object, which transfers the coordinates of the target point and the ID of the display to
     *     which it belongs.
     *     <br> **Note**: The target point and the start point must be on the same screen. Otherwise, the **17000007**
     *     exception is thrown.
     * @param { number } [speed] - Swipe speed, in px/s. The value ranges from 200 to 40000. If the set value is not in the range
     *     , the default value **600** is used.
     *     <br>Value range:[200, 40000]
     *     <br>Unit: px/s.
     *     <br>Throws error code 17000007 if negative.
     *     <br>Default value: 600
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    swipeBetween(from: Point, to: Point, speed?: number): Promise<void>;
    /**
     * Swipe on the screen between the specified points with optional touch options.
     *
     * @param { Point } from - the coordinate point where the finger touches the screen.
     * @param { Point } to - the coordinate point where the finger leaves the screen.
     * @param { TouchOptions } [options] - the options for the swipe operation.
     *                                Only the 'speed' and 'pressure' properties are applicable for this method.
     *                                Setting other properties will result in a BusinessError 17000007.
     *                                Default value: Refer to the default value of TouchOptions.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    swipeBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>;
    /**
     * Drags from the start point to the target point. You can specify the drag speed and the click duration before
     * dragging. This API uses a promise to return the result.
     *
     * @param { Point } from - Point object, which transfers the coordinates of the start point and the ID of the display to
     *     which the start point belongs.
     * @param { Point } to - Point object, which transfers the coordinates of the target point and the ID of the display to
     *     which it belongs.
     *     <br> **Note**: The target point and the start point must be on the same screen. Otherwise, the **17000007**
     *     exception is thrown.
     * @param { number } [speed] - Drag speed, in px/s. The value ranges from 200 to 40000. If the set value is not in the range
     *     , the default value **600** is used.
     *     <br>Value range:[200, 40000]
     *     <br>Unit: px/s.
     *     <br>Throws error code 17000007 if negative.
     *     <br>Default value: 600
     * @param { number } [duration] - The duration of the long press before dragging.
     *     <br>Value range: The value should be >= 1500
     *     <br>Unit: ms
     *     <br>Default value: 1500
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    dragBetween(from: Point, to: Point, speed?: number, duration?: number): Promise<void>;
    /**
     * Drag on the screen between the specified points with optional settings.
     *
     * @param { Point } from - the coordinate point where the finger touches the screen.
     * @param { Point } to - the coordinate point where the finger leaves the screen.
     * @param { TouchOptions } [options] - the options for the drag operation.
     *                         Only the 'pressure', 'speed', and 'duration' properties are applicable for this method.
     *                         Setting other properties will result in a BusinessError 17000007.
     *                         Default value: Refer to the default value of TouchOptions.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    dragBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>;
    /**
     * Captures the current screen and saves it as a PNG image to the given save path. This API uses a promise to return
     * the result. This API can be used in scenarios where screenshots are supported.
     *
     * @param { string } savePath - File save path. The path must be the
     *     [sandbox path](docroot://file-management/app-sandbox-directory.md) of the current application.
     * @returns { Promise<boolean> } - Promise used to return whether the screenshot operation is successful.
     *     The value **true** indicates that the operation is successful, and **false** indicates the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    screenCap(savePath: string): Promise<boolean>;
    /**
     * Captures the specified screen and saves it as a PNG image to the given save path. This API uses a promise to
     * return the result. This API can be used in scenarios where screenshots are supported.
     *
     * @param { string } savePath - File save path. The path must be the
     *     [sandbox path](docroot://file-management/app-sandbox-directory.md) of the current application.
     * @param { number } displayId - Display ID. The value is an integer greater than or equal to 0.
     *     <br> **Note**: If the input **displayId** does not exist, the exception **401** is reported.
     * @returns { Promise<boolean> } Promise used to return whether the screenshot operation is successful. The value
     *     **true** indicates that the screen capture operation is successful, and **false** indicates the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    screenCap(savePath: string, displayId: number): Promise<boolean>;
    /**
     * Get the current layout information and save as file with json format.
     *
     * @param { string } savePath - the path where to store the json, must be in the application sandbox directory.
     *     The path must be the [sandbox path](docroot://file-management/app-sandbox-directory.md) of the current
     *     application.
     * @param { number } [displayId] - the Id of the specified display, default is the displayId of the main screen.
     * @returns { Promise<boolean> } true if dump layout and file-storing are completed successfully,false otherwise.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    dumpLayout(savePath: string, displayId?: number): Promise<boolean>;
    /**
     * Sets the display rotation of the current scene. This API uses a promise to return the result. It applies to
     * rotatable scenarios.
     *
     * @param { DisplayRotation } rotation - Display rotation of the device.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
     *      2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 26.0.0]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    setDisplayRotation(rotation: DisplayRotation): Promise<void>;
    /**
     * Obtains the display rotation of the current device. This API uses a promise to return the result.
     *
     * @returns { Promise<DisplayRotation> } - Promise used to return the display rotation of the current device.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    getDisplayRotation(): Promise<DisplayRotation>;
    /**
     * Obtains the display rotation of the specified device. This API uses a promise to return the result.
     *
     * @param { number } displayId - Display ID. The value is an integer greater than or equal to 0.
     *     <br> **Note**: If the input **displayId** does not exist, the exception **17000007** is reported.
     * @returns { Promise<DisplayRotation> } - Promise used to return the display rotation of the specified device.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    getDisplayRotation(displayId: number): Promise<DisplayRotation>;
    /**
     * Enables or disables display rotation. This API uses a promise to return the result.
     *
     * @param { boolean } enabled - Whether the screen can be rotated. The value **true** indicates that the screen can be
     *     rotated, and **false** indicates the opposite.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    setDisplayRotationEnabled(enabled: boolean): Promise<void>;
    /**
     * Obtains the display size of the current device. This API uses a promise to return the result.
     *
     * @returns { Promise<Point> } - Promise used to return the **Point** object.
     *     The size of the current device screen is **Point.x * Point.y**.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 26.0.0]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    getDisplaySize(): Promise<Point>;
    /**
     * Obtains the size of the specified display on the current device. This API uses a promise to return the result.
     *
     * @param { number } displayId - Display ID. The value is an integer greater than or equal to 0.
     *     <br> **Note**: If the input **displayId** does not exist, the exception **17000007** is reported.
     * @returns { Promise<Point> } Promise used to return the **Point** object. The size of the specified display is
     *     **Point.x * Point.y**.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 26.0.0]
     * @atomicservice
     * @since 20
     * @test
     */
    getDisplaySize(displayId: number): Promise<Point>;
    /**
     * Obtains the display density of the current device. This API uses a promise to return the result.
     *
     * @returns { Promise<Point> } Promise used to return the **Point** object. The density of the current device display
     *     is **Point.x*Point.y**.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    getDisplayDensity(): Promise<Point>;
    /**
     * Obtains the density of the specified display of the current device. This API uses a promise to return the result.
     *
     * @param { number } displayId - Display ID. The value is an integer greater than or equal to 0.
     *     <br> **Note**: If the input **displayId** does not exist, the exception **17000007** is reported.
     * @returns { Promise<Point> } Promise used to return the **Point** object. The density of the specified display is
     *     **Point.x*Point.y**.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    getDisplayDensity(displayId: number): Promise<Point>;
    /**
     * Wakes up the current display. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    wakeUpDisplay(): Promise<void>;
    /**
     * Injects an operation of returning to the home screen on the device. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    pressHome(): Promise<void>;
    /**
     * Injects an operation of returning to the home screen on the specified display. This API uses a promise to return
     * the result.
     *
     * @param { number } displayId - Display ID. The value is an integer greater than or equal to 0.
     *     <br> **Note**: If the input **displayId** does not exist, the exception **17000007** is reported.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    pressHome(displayId: number): Promise<void>;
    /**
     * Checks whether all components on the current UI are idle. This API uses a promise to return the result.
     *
     * @param { number } idleTime - Idle time threshold, in ms. If the duration for which a component remains inactive reaches
     *     this threshold, it is considered as idle. The value must be an integer greater than or equal to 0.
     *     <br>Unit: ms
     * @param { number } timeout - Maximum waiting time, in milliseconds. The value is an integer greater than or equal to 0.
     *     <br>Unit: ms
     * @returns { Promise<boolean> } - Promise used to return whether all components on the current UI are idle. The value true
     *     indicates that all components on the current UI are idle, and false indicates the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 26.0.0]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    waitForIdle(idleTime: number, timeout: number): Promise<boolean>;
    /**
     * Simulates a fling operation. This API uses a promise to return the result.
     *
     * @param { Point } from - Coordinates of the point where the finger touches the screen.
     * @param { Point } to - Coordinates of the point where the finger leaves the screen.
     * @param { number } stepLen - Step length, in pixels. The value is an integer greater than or equal to 0.
     *     <br>Unit: px
     * @param { number } speed - Fling speed, in px/s. The value ranges from 200 to 40000. If the set value is not in the range
     *     , the default value **600** is used.
     *     <br>Value range:[200, 40000]
     *     <br>Unit: px/s.
     *     <br>Throws error code 17000007 if negative.
     *     <br>Default value: 600
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    fling(from: Point, to: Point, stepLen: number, speed: number): Promise<void>;
    /**
     * Injects a multi-finger operation into a device. This API uses a promise to return the result.
     *
     * @param { PointerMatrix } pointers - Scroll trajectory, including the number of fingers and an array of coordinates along
     *     the trajectory.
     * @param { number } [speed] - Pointer action speed, in px/s.
     *     <br>Value range:[200, 40000]
     *     <br>Unit: px/s.
     *     <br>Throws error code 401 if negative.
     *     <br>Default value: 600
     * @returns { Promise<boolean> } - Promise used to return whether the operation is successful.
     *     The value **true** indicates that the operation is successful, and **false** indicates the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    injectMultiPointerAction(pointers: PointerMatrix, speed?: number): Promise<boolean>;
    /**
     * Simulates a fling operation with the specified direction and speed. This API uses a promise to return the result.
     *
     * @param { UiDirection } direction - Direction of the fling operation.
     * @param { number } speed - Scroll speed.
     *     <br>Value range:[200, 40000]
     *     <br>Unit: px/s.
     *     <br>Throws error code 401 if negative.
     *     <br>Default value: 600
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     * @test
     */
    fling(direction: UiDirection, speed: number): Promise<void>;
    /**
     * Simulates a fling operation on a specified display with the specified direction and speed. This API uses a promise
     *  to return the result.
     *
     * @param { UiDirection } direction - Direction of the fling operation.
     * @param { number } speed - Fling speed, in px/s. The value ranges from 200 to 40000. If the set value is not in the range,
     *     the default value **600** is used.
     *     <br>Value range:[200, 40000]
     *     <br>Unit: px/s.
     *     <br>Throws error code 401 if negative.
     *     <br>Default value: 600
     * @param { number } displayId - Display ID. The value is an integer greater than or equal to 0.
     *     <br> **Note**: If the input **displayId** does not exist, the exception **401** is reported.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    fling(direction: UiDirection, speed: number, displayId: number): Promise<void>;
    /**
     * Injects a mouse click action at the specified coordinates, with the optional key or key combination. This API uses
     *  a promise to return the result. For example, if the value of **key1** is **2072**, the **Ctrl** button is pressed
     *  with the mouse click.
     *
     * @param { Point } p - Coordinates of the mouse click.
     * @param { MouseButton } btnId - Mouse button pressed.
     * @param { number } [key1] - First key value. The value is an integer greater than or equal to 0.
     *     For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
     *     <br>Default value: 0
     * @param { number } [key2] - Second key value. The value is an integer greater than or equal to 0.
     *     For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
     *     <br>Default value: 0
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 10
     * @test
     */
    mouseClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>;
    /**
     * Moves the mouse cursor to the target point. This API uses a promise to return the result.
     *
     * @param { Point } p - Coordinates of the end point.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 10
     * @test
     */
    mouseMoveTo(p: Point): Promise<void>;
    /**
     * Injects a mouse scroll action at the specified coordinates, with the optional key or key combination. This API
     * uses a promise to return the result. For example, if the value of **key1** is **2072**, the **Ctrl** button is
     * pressed with mouse scrolling.
     *
     * @param { Point } p - Coordinates of the mouse click.
     * @param { boolean } down - Whether the mouse wheel scrolls downward. The value **true** indicates the mouse wheel scrolls
     *     downward, and **false** indicates the mouse wheel scrolls upward.
     * @param { number } d - Number of ticks scrolled by the mouse wheel. A tick indicates a 120 px shift to the target point.
     *     The value is an integer greater than or equal to 0.
     *     <br>Value range: The value should be >= 0
     *     <br>Unit: px
     * @param { number } [key1] - First key value. The value is an integer greater than or equal to 0.
     *     For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
     *     <br>Default value: 0
     * @param { number } [key2] - Second key value. The value is an integer greater than or equal to 0.
     *     For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
     *     <br>Default value: 0
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 10
     * @test
     */
    mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number): Promise<void>;
    /**
     * Injects a mouse scroll action at the specified coordinates, with the optional key or key combination and the
     * specified scroll speed. This API uses a promise to return the result.
     *
     * @param { Point } p - Coordinates of the mouse click.
     * @param { boolean } down - Whether the mouse wheel scrolls downward. The value **true** indicates the mouse wheel scrolls
     *     downward, and **false** indicates the mouse wheel scrolls upward.
     * @param { number } d - Number of ticks scrolled by the mouse wheel. A tick indicates a 120 px shift to the target point. The
     *     value is an integer greater than or equal to 0.
     *     <br>Unit: cell
     * @param { number } [key1] - First key value. The value is an integer greater than or equal to 0.
     *     For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
     *     <br>Default value: 0
     * @param { number } [key2] - Second key value. The value is an integer greater than or equal to 0.
     *     For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
     *     <br>Default value: 0
     * @param { number } [speed] - Scroll speed of the mouse wheel.
     *     <br>Value range:[1, 500]
     *     <br>Unit: ticks/s
     *     <br>Throws error code 401 if negative.
     *     <br>Default value: 20
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 11
     * @test
     */
    mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number, speed?: number): Promise<void>;
    /**
     * Captures the specified area of the current screen and saves the captured screenshot as a PNG image to the
     * specified path. This API uses a promise to return the result. This API can be used in scenarios where screenshots
     * are supported.
     *
     * @param { string } savePath - File save path. The path must be the
     *     [sandbox path](docroot://file-management/app-sandbox-directory.md) of the current application.
     * @param { Rect } [rect] - Area of the screen to capture. The default value is the entire screen.
     * @returns { Promise<boolean> } - Promise used to return whether the screenshot operation is successful.
     *     The value **true** indicates the screenshot operation is successful, and **false** indicates the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 26.0.0]
     * @atomicservice [since 11]
     * @since 10
     * @test
     */
    screenCapture(savePath: string, rect?: Rect): Promise<boolean>;
    /**
     * Creates a UI event listener {@link UIEventObserver}.
     *
     * @returns { UIEventObserver } - UI event listener {@link UIEventObserver}.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 10
     * @test
     */
    createUIEventObserver(): UIEventObserver;
    /**
     * Injects a double-click action at the specified coordinates, with the optional key or key combination. This API
     * uses a promise to return the result. For example, if the value of **key** is **2072**, the **Ctrl** button is
     * pressed with the double-click.
     *
     * @param { Point } p - Coordinates of the double-click.
     * @param { MouseButton } btnId - Mouse button pressed.
     * @param { number } [key1] - First key value. The value is an integer greater than or equal to 0.
     *     For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
     *     <br>Default value: 0
     * @param { number } [key2] - Second key value. The value is an integer greater than or equal to 0.
     *     For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
     *     <br>Default value: 0
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 11
     * @test
     */
    mouseDoubleClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>;
    /**
     * Injects a mouse long-click action at the specified coordinates, with the optional key or key combination. This API
     *  uses a promise to return the result. For example, if the value of **Key** is **2072**, the **Ctrl** button is
     * long-clicked with the mouse device.
     *
     * @param { Point } p - Coordinates of the long-click of the mouse device.
     * @param { MouseButton } btnId - Mouse button pressed.
     * @param { number } [key1] - First key value. The value is an integer greater than or equal to 0.
     *     For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
     *     <br>Default value: 0
     * @param { number } [key2] - Second key value. The value is an integer greater than or equal to 0.
     *     For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
     *     <br>Default value: 0
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 11
     * @test
     */
    mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>;
    /**
     * Injects a mouse long-click action at the specified coordinates, with the optional key or key combination and the
     * specified duration. This API uses a promise to return the result. For example, if the value of **Key** is **2072**
     * , the **Ctrl** button is long-clicked with the mouse device.
     *
     * @param { Point } p - Coordinates of the long-click of the mouse device.
     * @param { MouseButton } btnId - Mouse button pressed.
     * @param { number } [key1] - First key value. The value is an integer greater than or equal to 0.
     *     For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
     *     <br>Default value: 0
     * @param { number } [key2] - Second key value. The value is an integer greater than or equal to 0.
     *     For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
     *     <br>Default value: 0
     * @param { number } [duration] - Long-click duration.
     *     <br>Value range: The value should be >= 1500
     *     <br>Unit: ms
     *     <br>Default value: 1500
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number, duration?: number): Promise<void>;
    /**
     * Moves the mouse pointer from the start point to the end point. This API uses a promise to return the result.
     *
     * @param { Point } from - Coordinates of the start point.
     * @param { Point } to - Coordinates of the end point.
     * @param { number } [speed] - Mouse move speed.
     *     <br>Value range:[200, 40000]
     *     <br>Unit: px/s.
     *     <br>Throws error code 401 if negative.
     *     <br>Default value: 600
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 11
     * @test
     */
    mouseMoveWithTrack(from: Point, to: Point, speed?: number): Promise<void>;
    /**
     * Drags the mouse pointer from the start point to the end point. This API uses a promise to return the result.
     *
     * @param { Point } from - Coordinates of the start point.
     * @param { Point } to - Coordinates of the end point.
     * @param { number } [speed] - Mouse drag speed.
     *     <br>Value range:[200, 40000]
     *     <br>Unit: px/s.
     *     <br>Throws error code 401 if negative.
     *     <br>Default value: 600
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 11
     * @test
     */
    mouseDrag(from: Point, to: Point, speed?: number): Promise<void>;
    /**
     * Drags the mouse from the start point to the end point. You can specify the dragging speed and the duration before
     * dragging. This API uses a promise to return the result.
     *
     * @param { Point } from - Coordinates of the start point.
     * @param { Point } to - Coordinates of the end point.
     * @param { number } [speed] - Speed of mouse drag.
     *     <br>Value range:[200, 40000]
     *     <br>Unit: px/s.
     *     <br>Throws error code 401 if negative.
     *     <br>Default value: 600
     * @param { number } [duration] - The duration of the long press before dragging.
     *     <br>Value range: The value should be >= 1500
     *     <br>Unit: ms
     *     <br>Default value: 1500
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    mouseDrag(from: Point, to: Point, speed?: number, duration?: number): Promise<void>;
    /**
     * Hold down the left mouse button and drag on the screen between the specified points,
     * with optional touch and key settings.
     *
     * @param { Point } from - the starting point.
     * @param { Point } to - the ending point.
     * @param { TouchOptions } [touchOptions] - the touch options for speed and duration settings.
     *                                    Only 'speed' and 'duration' properties are valid in this method.
     *                                    Setting other properties will cause BusinessError 17000007.
     *                                    Default value: Refer to the default value of TouchOptions.
     * @param { KeyOptions } [keyOptions] - the key options for key codes to press during drag.
     *                                    Default value: Refer to the default value of keyOptions.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    mouseDragWithOptions(from: Point, to: Point, touchOptions?: TouchOptions, keyOptions?: KeyOptions): Promise<void>;
    /**
     * Inputs text at a specified coordinate without clearing the original text in the component. This API uses a promise
     *  to return the result.
     *
     * @param { Point } p - Coordinates of the end point.
     * @param { string } text - Input text. Currently, English, Chinese, and special characters are supported.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 11
     * @test
     */
    inputText(p: Point, text: string): Promise<void>;
    /**
     * Inputs text at a specified coordinate point in a specified input mode. This API uses a promise to return the
     * result.
     *
     * @param { Point } p - Coordinates of the end point.
     * @param { string } text - Input text. Currently, English, Chinese, and special characters are supported.
     * @param { InputTextMode } mode - Text input mode.
     *     For details, see [InputTextMode]{@link InputTextMode}.
     *      **NOTE**
     *
     *      If **InputTextMode.addition** is set to **true**, the cursor moves to the end of the text and the specified
     *     text is input. If the value is **false**, the specified text is input at the coordinate point.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 Capability not supported. function can not work correctly due to limited device
     *     capabilities.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    inputText(p: Point, text: string, mode: InputTextMode): Promise<void>;
    /**
     * Simulates a multi-finger swipe gesture on the touchpad. This API uses a promise to return the result.
     *
     * @param { number } fingers - Number of fingers. The value can be 3 or 4.
     * @param { UiDirection } direction - Swipe direction.
     * @param { TouchPadSwipeOptions } [options] - Additional options for the multi-finger swipe gesture on the touchpad. The
     *     default values of the attributes in **{@link TouchPadSwipeOptions }** are used by default.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000005 This operation is not supported.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 18
     * @test
     */
    touchPadMultiFingerSwipe(fingers: number, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>;
    /**
     * Simulates a pen click operation. This API uses a promise to return the result.
     *
     * @param { Point } point - Coordinates of the clicked point.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 18
     * @test
     */
    penClick(point: Point): Promise<void>;
    /**
     * Simulates a pen long-click operation. This API uses a promise to return the result.
     *
     * @param { Point } point - Coordinates of the long-clicked point.
     * @param { number } [pressure] - Swipe pressure of the pen. The value ranges from 0.0 to 1.0. The default value is **1.0**.
     *     <br>Value range:[0.0, 1.0]
     *     <br>Default value: 1.0
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 18
     * @test
     */
    penLongClick(point: Point, pressure?: number): Promise<void>;
    /**
     * Simulates a pen double-click operation. This API uses a promise to return the result.
     *
     * @param { Point } point - Coordinates of the double-clicked point.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 18
     * @test
     */
    penDoubleClick(point: Point): Promise<void>;
    /**
     * Simulates a pen swipe operation. This API uses a promise to return the result.
     *
     * @param { Point } startPoint - Coordinates of the start point.
     * @param { Point } endPoint - Coordinates of the end point.
     * @param { number } [speed] - Speed of pen swipe.
     *     <br>Value range:[200, 40000]
     *     <br>Unit: px/s.
     *     <br>Throws error code 401 if negative.
     *     <br>Default value: 600
     * @param { number } [pressure] - Swipe pressure of the pen.
     *     <br>Value range:[0.0, 1.0]
     *     <br>Default value: 1.0
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 18
     * @test
     */
    penSwipe(startPoint: Point, endPoint: Point, speed?: number, pressure?: number): Promise<void>;
    /**
     * Simulates a continuous multi-point pen injection operation. This API uses a promise to return the result.
     *
     * @param { PointerMatrix } pointers - Scroll trajectory, including the number of fingers and an array of coordinates along
     *     the trajectory.
     *     **Note**: Currently, only the single-finger operation is supported. The value of **fingers** in
     *     **PointerMatrix** must be set to **1**.
     * @param { number } [speed] - Pen pointer action speed.
     *     <br>Value range:[200, 40000]
     *     <br>Unit: px/s.
     *     <br>Throws error code 401 if negative.
     *     <br>Default value: 600
     * @param { number } [pressure] - Injection pressure.
     *     <br>Value range:[0.0, 1.0]
     *     <br>Default value: 1.0
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 18
     * @test
     */
    injectPenPointerAction(pointers: PointerMatrix, speed?: number, pressure?: number): Promise<void>;
    /**
     * Trigger pen key operation.
     *
     * Supported combinations:
     *
     * - HANDWRITING mode: HANDWRITING key with CLICK or DOUBLE_CLICK operation.
     * - AIR_MOUSE mode: AIR_MOUSE key with CLICK or DOUBLE_CLICK operation (requires point in options),
     *   HANDWRITING key with CLICK or DOUBLE_CLICK operation, SMART key with CLICK operation.
     * Other combinations will result in a BusinessError 17000007.
     *
     * @param { PenKey } key - the pen key to operate.
     * @param { PenMode } mode - the pen mode.
     * @param { PenKeyOperation } operation - the operation type.
     * @param { PenKeyOperationOptions } [options] - the operation options, including optional coordinate point.
     *                                   Default value: Refer to the default value of PenKeyOperationOption.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000005 - This operation is not supported.
     * @throws { BusinessError } 17000007 - Parameter verification failed. Unsupported key, mode, and operation combination.
     * @syscap SystemCapability.Test.UiTest
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     * @test
     */
    triggerPenKey(key: PenKey, mode: PenMode, operation: PenKeyOperation, options?: PenKeyOperationOptions): Promise<void>;
    /**
     * Injects a crown rotation event. You can specify the rotation speed. This API uses a promise to return the result.
     *
     * @param { number } d - Number of rotation ticks. A positive value indicates rotation, and a negative value indicates
     *     counterclockwise rotation. The value must be an integer.
     * @param { number } [speed] - Rotation speed.
     *     <br>Unit: ticks/s.
     *     <br>Value range: [1, 500]
     *     <br>Throws error code 17000007 if negative.
     *     <br>Default value: 20
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device capabilities.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    crownRotate(d: number, speed?: number): Promise<void>;
    /**
     * Long-clicks at the specified coordinates and checks whether the target component exists. This API uses a promise
     *  to return the result.
     *
     * @param { On } on - Attributes of the target {@link Component}.
     * @param { Point } point - Coordinates of the long-clicked point.
     * @param { number } [duration] - Long-click duration.
     *     <br>Value range: The value should be >= 1500
     *     <br>Default value: 1500
     * @returns { Promise<boolean> } - Promise used to return whether the target component exists during a long-click
     *     operation. The value **true** indicates that the target component exists, and **false** indicates the opposite.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 26.0.0]
     * @atomicservice
     * @since 22
     * @test
     */
    isComponentPresentWhenLongClick(on: On, point: Point, duration?: number): Promise<boolean>;
    /**
     * Drags from the start point to the end point and checks whether the target component exists. This API uses a
     * promise to return the result.
     *
     * @param { On } on - Attributes of the target {@link Component}.
     * @param { Point } from - Point object, which transfers the coordinates of the start point and the ID
     *      of the display to which the start point belongs.
     * @param { Point } to - Point object, which transfers the coordinates of the target point and the ID
     *     of the display to which it belongs.
     *     <br> **Note**: The target point and the start point must be on the same screen. Otherwise, the **17000007**
     *     exception is thrown.
     * @param { number } [speed] - Drag speed.
     *     <br>Value range:[200, 40000]
     *     <br>Throws error code 17000007 if negative.
     *     <br>Default value: 600
     * @param { number } [duration] - The duration of the long press before dragging.
     *     <br>Value range: The value should be >= 1500
     *     <br>Default value: 1500
     * @returns { Promise<boolean> } - Promise used to return whether the target component exists during the dragging
     *     operation. The value **true** indicates that the target component exists, and **false** indicates the opposite.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: number, duration?: number): Promise<boolean>;
    /**
     * Swipes from the start point to the end point and checks whether the target component exists. This API uses a
     * promise to return the result.
     *
     * @param { On } on - Attributes of the target component.
     * @param { Point } from - Point object, which transfers the coordinates of the start point and the ID of
     *     the display to which the start point belongs.
     * @param { Point } to - Point object, which transfers the coordinates of the target point and the ID
     *     of the display to
     *     which it belongs.
     *     <br> **Note**: The target point and the start point must be on the same screen. Otherwise, the **17000007**
     *     exception is thrown.
     * @param { number } [speed] - Scroll speed.
     *     <br>Value range:[200, 40000]
     *     <br>Throws error code 17000007 if negative.
     *     <br>Default value: 600
     * @returns { Promise<boolean> } - Promise used to return whether the target component exists during the swiping
     *     operation.The value **true** indicates that the target component exists, and **false** indicates the opposite.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: number): Promise<boolean>;
    /**
     * Simulates a two-finger scroll gesture on the touchpad. This API uses a promise to return the result.
     *
     * @param { Point } point - Point of the mouse cursor when the two-finger scrolling is performed on the touchpad.
     * @param { UiDirection } direction - Direction of two-finger scrolling on the touchpad.
     * @param { number } d - Number of grids scrolled by two fingers on the touchpad. A grid indicates a 120 px shift to the
     *     target point. The value is an integer greater than or equal to 0.
     * @param { number } [speed] - Speed of two-finger scrolling on the touchpad.
     *     <br>Unit: ticks/s.
     *     <br>Value range: [1, 500]
     *     <br>Throws error code 17000007 if negative.
     *     <br>Default value: 20
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000005 - This operation is not supported.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: number, speed?: number): Promise<void>;
    /**
     * Simulates a knuckle knock on the display. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > If the knuckle gesture is disabled on the device<!--RP4--><!--RP4End-->, 17000005 is returned.
     *
     * @param { Array<Point> } pointers - Array of knuckle knock coordinates on the display. The array length can be 1 or 2.
     * @param { number } times - Number of consecutive knocks on the display.
     *     <br>Value range:[1,2]
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000005 - This operation is not supported.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    knuckleKnock(pointers: Array<Point>, times: number): Promise<void>;
    /**
     * Simulates a multi-point knuckle scrolling operation. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > If the knuckle gesture is disabled on the device<!--RP4--><!--RP4End-->, 17000005 is returned.
     *
     * @param { PointerMatrix } pointers - Scroll trajectory, including the number of fingers and an array of
     *     coordinates along the trajectory.
     *
     *     **Note**: Currently, only the single-finger operation is supported. The value of **fingers** in
     *     **PointerMatrix** must be set to **1**.
     * @param { number } [speed] - Knuckle pointer action speed.
     *     <br>Value range:[200, 40000]
     *     <br>Unit: px/s.
     *     <br>Throws error code 17000007 if negative.
     *     <br>Default value: 600
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000005 - This operation is not supported.
     * @throws { BusinessError } 17000007 - Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 22
     * @test
     */
    injectKnucklePointerAction(pointers: PointerMatrix, speed?: number): Promise<void>;
}
/**
 * The **UiWindow** class represents a window on the UI and provides APIs for obtaining window attributes, dragging a
 * window, and adjusting the window size.
 * All APIs provided in this class use a promise to return the result and must be invoked using **await**.
 *
 * @syscap SystemCapability.Test.UiTest
 * @atomicservice [since 11]
 * @since 9
 * @test
 */
declare class UiWindow {
    /**
     * Obtains the bundle name of the application to which a window belongs. This API uses a promise to return the result.
     *
     * @returns { Promise<string> } - Promise used to return the bundle name of the application to which the window belongs.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    getBundleName(): Promise<string>;
    /**
     * Obtains the bounds information of a window. This API uses a promise to return the result.
     *
     * @returns { Promise<Rect> } - Promise used to return the window border information.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    getBounds(): Promise<Rect>;
    /**
     * Obtains the window title. This API uses a promise to return the result.
     *
     * @returns { Promise<string> } - Promise used to return the window title.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    getTitle(): Promise<string>;
    /**
     * Obtains the window mode. This API uses a promise to return the result.
     *
     * @returns { Promise<WindowMode> } - Promise used to return the window mode information.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    getWindowMode(): Promise<WindowMode>;
    /**
     * Checks whether a window is focused. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } - Promise used to return whether the window is focused. The value **true** indicates that
     *     the component is focused, and **false** indicates the opposite.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    isFocused(): Promise<boolean>;
    /**
     * Checks whether a window is active. This API uses a promise to return the result.
     *
     *
     * @returns { Promise<boolean> } - Promise used to return whether the window is active. The value **true** indicates that
     *     the window is active, and **false** indicates the opposite.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @since 9
     * @deprecated since 11
     * @useinstead UiWindow#isActive
     * @test
     */
    isActived(): Promise<boolean>;
    /**
     * Focuses a window. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    focus(): Promise<void>;
    /**
     * Moves a window to the target point. This API uses a promise to return the result. This API is applicable to
     * moveable windows.
     *
     * @param { number } x - Number, which indicates the horizontal coordinate of the target point. The value is an integer
     *     greater than or equal to 0.
     *     <br>Unit: px
     * @param { number } y - Number, which indicates the vertical coordinate of the target point. The value is an integer greater
     *     than or equal to 0.
     *     <br>Unit: px
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @throws { BusinessError } 17000005 - This operation is not supported.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    moveTo(x: number, y: number): Promise<void>;
    /**
     * Resizes a window based on the specified width, height, and direction. This API uses a promise to return the
     * result. This API is applicable to resizable windows.
     *
     * @param { number } wide - Width of the adjusted window, in number format.
     *     The value is an integer greater than or equal to 0.
     *     <br>Unit: px
     * @param { number } height - Height of the adjusted window, in number format.
     *     The value is an integer greater than or equal to 0.
     *     <br>Unit: px
     * @param { ResizeDirection } direction - Resize direction.
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @throws { BusinessError } 17000005 - This operation is not supported.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    resize(wide: number, height: number, direction: ResizeDirection): Promise<void>;
    /**
     * Switches to the split-screen mode. This API uses a promise to return the result. This API is applicable to
     * windows that support screen splitting.
     *
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @throws { BusinessError } 17000005 - This operation is not supported.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    split(): Promise<void>;
    /**
     * Maximizes a window. This API uses a promise to return the result. This API is applicable to windows that can be
     * maximized.
     *
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @throws { BusinessError } 17000005 - This operation is not supported.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    maximize(): Promise<void>;
    /**
     * Minimizes a window. This API uses a promise to return the result. This API is applicable to windows that can be
     * minimized.
     *
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @throws { BusinessError } 17000005 - This operation is not supported.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    minimize(): Promise<void>;
    /**
     * Resumes a window to its previous mode. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @throws { BusinessError } 17000005 - This operation is not supported.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    resume(): Promise<void>;
    /**
     * Closes a window. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } - Promise that returns no value.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @throws { BusinessError } 17000005 - This operation is not supported.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    close(): Promise<void>;
    /**
     * Checks whether a window is active. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } - Promise used to return whether the window is active. The value **true** indicates that
     *     the window is active, and **false** indicates the opposite.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 11
     * @test
     */
    isActive(): Promise<boolean>;
    /**
     * Obtains the ID of the display to which a window belongs. This API uses a promise to return the result.
     *
     * @returns { Promise<number> } - Promise used to return the ID of the display to which the window belongs.
     * @throws { BusinessError } 17000002 - The API does not support concurrent calls.
     * @throws { BusinessError } 17000004 - The window or component is invisible or destroyed.
     * @syscap SystemCapability.Test.UiTest
     * @atomicservice
     * @since 20
     * @test
     */
    getDisplayId(): Promise<number>;
}
/**
 * Represents a two-dimensional array of pointers on the device display, it's used to build a
 * multi-finger trace which can be injected with UiDriver.
 *
 * @syscap SystemCapability.Test.UiTest
 * @crossplatform [since 11]
 * @atomicservice [since 11]
 * @since 9
 * @test
 */
declare class PointerMatrix {
    /**
     * Creates a **PointerMatrix** object and returns the object created. This API is a static API.
     *
     * @param { number } fingers - Number of fingers injected during the multi-finger operation.
     *     <br>Value range:[1, 10]
     * @param { number } steps - Number of steps performed by a finger.
     *     <br>Value range:[1, 1000]
     * @returns { PointerMatrix } - **PointerMatrix** object created.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    static create(fingers: number, steps: number): PointerMatrix;
    /**
     * Sets the coordinates for the action corresponding to the specified finger and step in the **PointerMatrix**
     * object.
     *
     * @param { number } finger - Number of fingers. The value is an integer greater than or equal to 0 and cannot exceed the
     *     number of fingers set when the **PointerMatrix** object is constructed.
     * @param { number } step - Number of steps. The value is an integer greater than or equal to 0 and cannot exceed the number
     *     of steps set when the **PointerMatrix** object is constructed.
     * @param { Point } point - Coordinates of the action. It is recommended that the distance between adjacent coordinates be
     *     within the range of 10 px to 80 px.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Test.UiTest
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 9
     * @test
     */
    setPoint(finger: number, step: number, point: Point): void;
}
/**
 * The static builder for building {@link By}object conveniently,usage example:BY.text('txt').enabled(true).
 *
 * @syscap SystemCapability.Test.UiTest
 * @since 8
 * @deprecated since 9
 * @useinstead ohos.UiTest.ON
 * @test
 */
declare const BY: By;
/**
 * The static builder for building {@link On}object conveniently,usage example:ON.text('txt').enabled(true).
 *
 * @syscap SystemCapability.Test.UiTest
 * @crossplatform [since 11]
 * @atomicservice [since 11]
 * @since 9
 * @test
 */
declare const ON: On;
export { Component, Driver, UiWindow, ON, On, MatchPattern, DisplayRotation, ResizeDirection, WindowMode, Point, WindowFilter, Rect, PointerMatrix, UiDirection, MouseButton, UIElementInfo, UIEventObserver, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, KeyOptions, TouchOptions, PenKey, PenKeyOperation, PenMode, PenKeyOperationOptions };
export { UiComponent, UiDriver, BY, By };

```
