# @ohos.arkui.observer.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023 Huawei Device Co., Ltd.
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
import type { Callback } from './@ohos.base';
import type UIAbilityContext from './application/UIAbilityContext';
import type { NavigationOperation, NavBar } from '../component/navigation';
import type { Size } from './@ohos.arkui.node';
/**
 * Provides APIs for listening for UI component behavior changes.
 *
 * > **NOTE**
 * >
 * > - UIObserver can only listen for relevant information within the current process and does not support obtaining
 * > information in cross-process scenarios<!--Del--> such as [UIExtensionComponent]{@link ui_extension_component}<!--
 * > DelEnd-->.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice [since 12]
 * @since 11
 */
declare namespace uiObserver {
    /**
     * Describes the state of the **NavDestination** component.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    export enum NavDestinationState {
        /**
         * The **NavDestination** component is displayed.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        ON_SHOWN = 0,
        /**
         * The **NavDestination** component is hidden.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        ON_HIDDEN = 1,
        /**
         * The **NavDestination** component is attached to the component tree.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        ON_APPEAR = 2,
        /**
         * The **NavDestination** component is detached from the component tree.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        ON_DISAPPEAR = 3,
        /**
         * The **NavDestination** component is about to be displayed.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        ON_WILL_SHOW = 4,
        /**
         * The **NavDestination** component is about to be hidden.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        ON_WILL_HIDE = 5,
        /**
         * The **NavDestination** component is about to be mounted to the component tree.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        ON_WILL_APPEAR = 6,
        /**
         * The **NavDestination** component is about to be unmounted from the component tree.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        ON_WILL_DISAPPEAR = 7,
        /**
         * The **NavDestination** component is active.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 17
         */
        ON_ACTIVE = 8,
        /**
         * The **NavDestination** component is inactive.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 17
         */
        ON_INACTIVE = 9,
        /**
         * The back button is pressed on the **NavDestination** component.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        ON_BACKPRESS = 100
    }
    /**
     * Enumerates the states of a page during routing. **RouterPageState** is used in
     * [RouterPageInfo]{@link uiObserver.RouterPageInfo} as the callback parameter for passive observation via
     * [routerPageUpdate]{@link uiObserver.on(type: 'routerPageUpdate', context: UIAbilityContext | UIContext, callback: Callback<RouterPageInfo>)}.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    export enum RouterPageState {
        /**
         * The page is about to be displayed.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        ABOUT_TO_APPEAR = 0,
        /**
         * The page is about to be destroyed.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        ABOUT_TO_DISAPPEAR = 1,
        /**
         * The page is displayed.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        ON_PAGE_SHOW = 2,
        /**
         * The page is hidden.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        ON_PAGE_HIDE = 3,
        /**
         * The page is returned.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        ON_BACK_PRESS = 4
    }
    /**
     * ScrollEvent type.
     *
     * @enum { number }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export enum ScrollEventType {
        /**
         * When the ScrollEvent starts.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        SCROLL_START = 0,
        /**
         * When the ScrollEvent stops.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        SCROLL_STOP = 1
    }
    /**
     * TabContent state.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export enum TabContentState {
        /**
         * When the TabContent is shown.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        ON_SHOW = 0,
        /**
         * When the TabContent is hidden.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        ON_HIDE = 1
    }
    /**
     * Information about the **NavDestination** component, returned by the system to developers.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    export interface NavDestinationInfo {
        /**
         * ID of the **Navigation** component that contains the target **NavDestination** component.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        navigationId: ResourceStr;
        /**
         * Name of the **NavDestination** component.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        name: ResourceStr;
        /**
         * State of the **NavDestination** component.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        state: NavDestinationState;
        /**
         * Index of the **NavDestination** component in the navigation stack.
         * The value must be greater than or equal to 0.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        index: number;
        /**
         * Parameters of the **NavDestination** component.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        param?: Object;
        /**
         * Unique ID of the **NavDestination** component.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        navDestinationId: string;
        /**
         * Mode of the **NavDestination** component.
         * Default value: NavDestinationMode.Standard.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 15
         */
        mode?: NavDestinationMode;
        /**
         * Unique ID of the **NavDestination** component.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 15
         */
        uniqueId?: number;
        /**
         * Size of the **NavDestination** component, in vp.
         *
         * @type { ?Size }
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 23
         */
        size?: Size;
    }
    /**
     * Provides information about the **Navigation** component.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export interface NavigationInfo {
        /**
         * ID of the **Navigation** component.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        navigationId: string;
        /**
         * Navigation controller of the **Navigation** component.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        pathStack: NavPathStack;
        /**
         * Unique ID of the **Navigation** component, which can be obtained through
         * [queryNavigationInfo]{@link BaseCustomComponent#queryNavigationInfo}.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        uniqueId?: number;
    }
    /**
     * ScrollEvent info.
     *
     * @interface ScrollEventInfo
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export interface ScrollEventInfo {
        /**
         * Scroll id.
         *
         * @type { string }
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        id: string;
        /**
         * The uniqueId of the scrollable component.
         *
         * @type { number }
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        uniqueId: number;
        /**
         * Changed ScrollEvent type.
         *
         * @type { ScrollEventType }
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        scrollEvent: ScrollEventType;
        /**
         * Changed ScrollEvent offset.
         *
         * @type { number }
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        offset: number;
        /**
         * Scroll axis.
         *
         * @type { ?Axis }
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        axis?: Axis;
    }
    /**
     * Provides the **TabContent** switching information.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export interface TabContentInfo {
        /**
         * ID of the **TabContent** component.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        tabContentId: string;
        /**
         * Unique ID of the **TabContent** component.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        tabContentUniqueId: number;
        /**
         * Enumerates the **TabContent** component states.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        state: TabContentState;
        /**
         * Index of the **TabContent** component. The index is zero-based.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        index: number;
        /**
         * ID of the **Tabs** component.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        id: string;
        /**
         * Unique ID of the **Tabs** component.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        uniqueId: number;
        /**
         * Index of the previously focused **TabContent** component. The index is zero-based. This parameter is available
         * only in the callback of [on('tabChange')]{@link @ohos.arkui.UIContext:UIObserver#on(type: 'tabChange', callback:
         * Callback<observer.TabContentInfo>)}.
         *
         * @type { ?number }
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        lastIndex?: number;
    }
    /**
     * Describes the observer options.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export interface ObserverOptions {
        /**
         * Component ID.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        id: string;
    }
    /**
     * Provides the information contained in **RouterPageInfo**, returned by the system to developers.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    export class RouterPageInfo {
        /**
         * Context of the router page that invokes the lifecycle callback.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        context: UIAbilityContext | UIContext;
        /**
         * Position of the router page that invokes the lifecycle callback, in the navigation stack.
         * The value must be greater than or equal to 0.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        index: number;
        /**
         * Name of the page that invokes the lifecycle callback.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        name: string;
        /**
         * Path of the page that invokes the lifecycle callback.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        path: string;
        /**
         * State of the router page that invokes the lifecycle callback.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        state: RouterPageState;
        /**
         * Unique ID of the router page that invokes the lifecycle callback.
         *
         * @type { string }
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        pageId: string;
        /**
         * Size of the router page, in vp.
         *
         * @type { ?Size }
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 23
         */
        size?: Size;
    }
    /**
     * Provides the information contained in the callback when the screen pixel density changes.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export class DensityInfo {
        /**
         * Context corresponding to the page when the screen pixel density changes.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        context: UIContext;
        /**
         * Screen pixel density after the change.
         *
         * Value range: [0, +∞)
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        density: number;
    }
    /**
     * Provides information about window size layout breakpoint changes.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 26.0.0]
     * @atomicservice
     * @since 22
     */
    export class WindowSizeLayoutBreakpointInfo {
        /**
         * Layout breakpoint for window width.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 26.0.0]
         * @atomicservice
         * @since 22
         */
        readonly widthBreakpoint: WidthBreakpoint;
        /**
         * Layout breakpoint for window height.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 26.0.0]
         * @atomicservice
         * @since 22
         */
        readonly heightBreakpoint: HeightBreakpoint;
    }
    /**
     * Provides the information about page switching of the **Navigation** component.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export interface NavDestinationSwitchInfo {
        /**
         * Context information corresponding to **Navigation** component that triggers page switching.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        context: UIAbilityContext | UIContext;
        /**
         * Source page for page switching.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        from: NavDestinationInfo | NavBar;
        /**
         * Destination page for page switching.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        to: NavDestinationInfo | NavBar;
        /**
         * Page switching operation type.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        operation: NavigationOperation;
    }
    /**
    * Text change event info
    *
    * @interface TextChangeEventInfo
    * @syscap SystemCapability.ArkUI.ArkUI.Full
    * @stagemodelonly
    * @crossplatform
    * @atomicservice
    * @since 22
    */
    export interface TextChangeEventInfo {
        /**
        * The id of text input component.
        *
        * @type { string }
        * @syscap SystemCapability.ArkUI.ArkUI.Full
        * @stagemodelonly
        * @crossplatform
        * @atomicservice
        * @since 22
        */
        id: string;
        /**
        * The uniqueId of the text input component.
        *
        * @type { number }
        * @syscap SystemCapability.ArkUI.ArkUI.Full
        * @stagemodelonly
        * @crossplatform
        * @atomicservice
        * @since 22
        */
        uniqueId: number;
        /**
        * Current content of text field component .
        *
        * @type { string }
        * @syscap SystemCapability.ArkUI.ArkUI.Full
        * @stagemodelonly
        * @crossplatform
        * @atomicservice
        * @since 22
        */
        content: string;
    }
    /**
     * Provides the observer options for the page switching event of the **Navigation** component.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export interface NavDestinationSwitchObserverOptions {
        /**
         * ID of the target **Navigation** component.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        navigationId: ResourceStr;
    }
    /**
     * Subscribes to status changes of the **NavDestination** component. Compared with
     * [uiObserver.on]{@link uiObserver.on(type: 'navDestinationUpdate', callback: Callback<NavDestinationInfo>)}, this
     * API supports the **options** parameter, which enables you to specify the ID of the target **Navigation** component
     * to observe.
     *
     * @param { 'navDestinationUpdate' } type - Event type. Set to **'navDestinationUpdate'** for **NavDestination**
     *     component status change events.
     * @param { object } options - ID of the target **Navigation** component.
     * @param { Callback<NavDestinationInfo> } callback - Callback used to return the result. It provides the current
     *     state of the **NavDestination** component.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    export function on(type: 'navDestinationUpdate', options: {
        navigationId: ResourceStr;
    }, callback: Callback<NavDestinationInfo>): void;
    /**
     * Unsubscribes from status changes of the **NavDestination** component. Compared with
     * [uiObserver.off]{@link uiObserver.off(type: 'navDestinationUpdate', callback?: Callback<NavDestinationInfo>)}, this
     * API supports the **options** parameter, which enables you to specify the ID of the target **Navigation** component
     * to observe.
     *
     * @param { 'navDestinationUpdate' } type - Event type. Set to **'navDestinationUpdate'** for **NavDestination**
     *     component status change events.
     * @param { object } options - ID of the target **Navigation** component.
     * @param { Callback<NavDestinationInfo> } callback - Callback used to return the result. It provides the current
     *     state of the **NavDestination** component.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    export function off(type: 'navDestinationUpdate', options: {
        navigationId: ResourceStr;
    }, callback?: Callback<NavDestinationInfo>): void;
    /**
     * Subscribes to status changes of the **NavDestination** component.
     *
     * @param { 'navDestinationUpdate' } type - Event type. Set to **'navDestinationUpdate'** for **NavDestination**
     *     component status change events.
     * @param { Callback<NavDestinationInfo> } callback - Callback used to return the result. It provides the current
     *     state of the **NavDestination** component.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    export function on(type: 'navDestinationUpdate', callback: Callback<NavDestinationInfo>): void;
    /**
     * Unsubscribes from status changes of the **NavDestination** component.
     *
     * @param { 'navDestinationUpdate' } type - Event type. Set to **'navDestinationUpdate'** for **NavDestination**
     *     component status change events.
     * @param { Callback<NavDestinationInfo> } [callback] - Callback used to return the result. It provides the current
     *     state of the **NavDestination** component.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    export function off(type: 'navDestinationUpdate', callback?: Callback<NavDestinationInfo>): void;
    /**
     * Registers a callback function to be called when the scroll event start or stop.
     *
     * @param { 'scrollEvent' } type - The type of event to listen for. Must be 'scrollEvent'.
     * @param { ObserverOptions } options - The options object.
     * @param { Callback<ScrollEventInfo> } callback - The callback function to be called when the scroll event start or stop.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export function on(type: 'scrollEvent', options: ObserverOptions, callback: Callback<ScrollEventInfo>): void;
    /**
     * Removes a callback function that was previously registered with `on()`.
     *
     * @param { 'scrollEvent' } type - The type of event to remove the listener for. Must be 'scrollEvent'.
     * @param { ObserverOptions } options - The options object.
     * @param { Callback<ScrollEventInfo> } callback - The callback function to remove. If not provided, all callbacks for the given event type and
     *                                                    scroll ID will be removed.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export function off(type: 'scrollEvent', options: ObserverOptions, callback?: Callback<ScrollEventInfo>): void;
    /**
     * Registers a callback function to be called when the scroll event start or stop.
     *
     * @param { 'scrollEvent' } type - The type of event to listen for. Must be 'scrollEvent'.
     * @param { Callback<ScrollEventInfo> } callback - The callback function to be called when the scroll event start or stop.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export function on(type: 'scrollEvent', callback: Callback<ScrollEventInfo>): void;
    /**
     * Removes a callback function that was previously registered with `on()`.
     *
     * @param { 'scrollEvent'} type - The type of event to remove the listener for. Must be 'scrollEvent'.
     * @param { Callback<ScrollEventInfo> } [callback] - The callback function to remove. If not provided, all callbacks for the given event type
     *                                                      will be removed.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export function off(type: 'scrollEvent', callback?: Callback<ScrollEventInfo>): void;
    /**
     * Subscribes to state changes of the page during routing.
     *
     * @param { 'routerPageUpdate' } type - Event type. The value is fixed at **'routerPageUpdate'**, which indicates the
     *     state change event of the page during routing.
     * @param { UIAbilityContext | UIContext } context - Context information, which is used to specify the target page
     *     scope.
     * @param { Callback<RouterPageInfo> } callback - Callback used to return the result. If **pageInfo** is passed, the
     *     current page state is returned.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    export function on(type: 'routerPageUpdate', context: UIAbilityContext | UIContext, callback: Callback<RouterPageInfo>): void;
    /**
     * Unsubscribes from state changes of the page during routing.
     *
     * @param { 'routerPageUpdate' } type - Event type. The value is fixed at **'routerPageUpdate'**, which indicates the
     *     state change event of the page during routing.
     * @param { UIAbilityContext | UIContext } context - Context information, which is used to specify the target page
     *     scope.
     * @param { Callback<RouterPageInfo> } [callback] - Target listener to unregister.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    export function off(type: 'routerPageUpdate', context: UIAbilityContext | UIContext, callback?: Callback<RouterPageInfo>): void;
    /**
     * Listens for screen pixel density changes.
     *
     * @param { 'densityUpdate' } type - Event type. Set to **'densityUpdate'** for screen pixel density change events.
     * @param { UIContext } context - Context information, which is used to specify the target page scope.
     * @param { Callback<DensityInfo> } callback - Callback used to return the result. It provides information about the
     *     changed screen pixel density.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export function on(type: 'densityUpdate', context: UIContext, callback: Callback<DensityInfo>): void;
    /**
     * Unregisters the listener for screen pixel density changes.
     *
     * @param { 'densityUpdate' } type - Event type. Set to **'densityUpdate'** for screen pixel density change events.
     * @param { UIContext } context - Context information, which is used to specify the target page scope.
     * @param { Callback<DensityInfo> } [callback] - Target listener to unregister. If no parameter is provided, all
     *     listeners for the **densityUpdate** event under the current UI context are unregistered.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export function off(type: 'densityUpdate', context: UIContext, callback?: Callback<DensityInfo>): void;
    /**
     * Listens for drawing instruction dispatch in each frame.
     *
     * @param { 'willDraw' } type - Event event. The value **'willDraw'** indicates whether drawing is about to occur.
     * @param { UIContext } context - Context information, which is used to specify the target page scope.
     * @param { Callback<void> } callback - Callback used to return the result.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export function on(type: 'willDraw', context: UIContext, callback: Callback<void>): void;
    /**
     * Unregisters the listener for drawing instruction dispatch in each frame.
     *
     * @param { 'willDraw' } type - Event event. The value **'willDraw'** indicates whether drawing is about to occur.
     * @param { UIContext } context - Context information, which is used to specify the target page scope.
     * @param { Callback<void> } [callback] - Target listener to unregister.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export function off(type: 'willDraw', context: UIContext, callback?: Callback<void>): void;
    /**
     * Listens for layout completion status in each frame.
     *
     * @param { 'didLayout' } type - Event type. The value **'didLayout'** indicates whether the layout has been
     *     completed.
     * @param { UIContext } context - Context information, which is used to specify the target page scope.
     * @param { Callback<void> } callback - Callback used to return the result.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export function on(type: 'didLayout', context: UIContext, callback: Callback<void>): void;
    /**
     * Unregisters the listener for layout completion status in each frame.
     *
     * @param { 'didLayout' } type - Event type. The value **'didLayout'** indicates whether the layout has been
     *     completed.
     * @param { UIContext } context - Context information, which is used to specify the target page scope.
     * @param { Callback<void> } [callback] - Target listener to unregister.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export function off(type: 'didLayout', context: UIContext, callback?: Callback<void>): void;
    /**
     * Subscribes to **TabContent** page switching events for the specified **Tabs** component identified by its ID.
     * Unlike
     * [on('tabChange')]{@link @ohos.arkui.UIContext:UIObserver#on(type: 'tabChange', callback: Callback<observer.TabContentInfo>)},
     * this API does not support listening for the initial tab display event when the **Tabs** component is initialized.
     *
     * @param { 'tabContentUpdate' } type - Event type. Set to **'tabContentUpdate'** for **TabContent** page switching
     *     events.
     * @param { ObserverOptions } options - ID of the target **Tabs** component.
     * @param { Callback<TabContentInfo> } callback - Callback used to return the result. It provides information about
     *     **TabContent** switch events through **TabContentInfo**.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export function on(type: 'tabContentUpdate', options: ObserverOptions, callback: Callback<TabContentInfo>): void;
    /**
     * Unsubscribes from **TabContent** page switching events for the specified **Tabs** component identified by its ID.
     *
     * @param { 'tabContentUpdate' } type - Event type. Set to **'tabContentUpdate'** for **TabContent** page switching
     *     events.
     * @param { ObserverOptions } options - ID of the target **Tabs** component.
     * @param { Callback<TabContentInfo> } callback - Target listener to unregister.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export function off(type: 'tabContentUpdate', options: ObserverOptions, callback?: Callback<TabContentInfo>): void;
    /**
     * Subscribes to **TabContent** switch events. Unlike
     * [on('tabChange')]{@link @ohos.arkui.UIContext:UIObserver#on(type: 'tabChange', callback: Callback<observer.TabContentInfo>)},
     * this API does not support listening for the initial tab display event when the **Tabs** component is initialized.
     *
     * @param { 'tabContentUpdate' } type - Event type. Set to **'tabContentUpdate'** for **TabContent** page switching
     *     events.
     * @param { Callback<TabContentInfo> } callback - Callback used to return the result. It provides information about
     *     **TabContent** switch events through **TabContentInfo**.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export function on(type: 'tabContentUpdate', callback: Callback<TabContentInfo>): void;
    /**
     * Unsubscribes from the **TabContent** switching event.
     *
     * @param { 'tabContentUpdate' } type - Event type. Set to **'tabContentUpdate'** for **TabContent** page switching
     *     events.
     * @param { Callback<TabContentInfo> } [callback] - Target listener to unregister.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export function off(type: 'tabContentUpdate', callback?: Callback<TabContentInfo>): void;
    /**
     * Subscribes to **Navigation** component page switching events.
     *
     * @param { 'navDestinationSwitch' } type - Event type. Set to **'navDestinationSwitch'** for **Navigation** component
     *     page switching events.
     * @param { UIAbilityContext | UIContext } context - Context information, which is used to specify the target scope
     *     for page switching events.
     * @param { Callback<NavDestinationSwitchInfo> } callback - Callback used to return the result. It provides page
     *     switching event information through **NavDestinationSwitchInfo**.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export function on(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, callback: Callback<NavDestinationSwitchInfo>): void;
    /**
     * Unsubscribes from **Navigation** component page switching events.
     *
     * @param { 'navDestinationSwitch' } type - Event type. Set to **'navDestinationSwitch'** for **Navigation** component
     *     page switching events.
     * @param { UIAbilityContext | UIContext } context - Context information, which is used to specify the target scope
     *     for page switching events.
     * @param { Callback<NavDestinationSwitchInfo> } [callback] - Target listener to unregister.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export function off(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, callback?: Callback<NavDestinationSwitchInfo>): void;
    /**
     * Subscribes to **Navigation** component page switching events. Compared with
     * [uiObserver.on]{@link uiObserver.on( type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, callback: Callback<NavDestinationSwitchInfo> )},
     * this API supports the **observerOptions** parameter, which enables you to configure observation options.
     *
     * @param { 'navDestinationSwitch' } type - Event type. Set to **'navDestinationSwitch'** for **Navigation** component
     *     page switching events.
     * @param { UIAbilityContext | UIContext } context - Context information, which is used to specify the target scope
     *     for page switching events.
     * @param { NavDestinationSwitchObserverOptions } observerOptions - Observer configuration options.
     * @param { Callback<NavDestinationSwitchInfo> } callback - Callback used to return the result. It provides page
     *     switching event information through **NavDestinationSwitchInfo**.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export function on(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, observerOptions: NavDestinationSwitchObserverOptions, callback: Callback<NavDestinationSwitchInfo>): void;
    /**
     * Unsubscribes from **Navigation** component page switching events. Compared with
     * [uiObserver.off]{@link uiObserver.off( type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, callback?: Callback<NavDestinationSwitchInfo> )},
     * this API supports the **observerOptions** parameter, which enables you to configure observation options.
     *
     * @param { 'navDestinationSwitch' } type - Event type. Set to **'navDestinationSwitch'** for **Navigation** component
     *     page switching events.
     * @param { UIAbilityContext | UIContext } context - Context information, which is used to specify the target scope
     *     for page switching events.
     * @param { NavDestinationSwitchObserverOptions } observerOptions - Observer configuration options.
     * @param { Callback<NavDestinationSwitchInfo> } [callback] - Target listener to unregister.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export function off(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, observerOptions: NavDestinationSwitchObserverOptions, callback?: Callback<NavDestinationSwitchInfo>): void;
}
export default uiObserver;

```
