# @ohos.multimedia.avMusicTemplate.d.ts

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
 * @file
 * @kit AVSessionKit
 */
import type { Callback } from './@ohos.base';
import image from './@ohos.multimedia.image';
import { WantAgent } from './@ohos.app.ability.wantAgent';
/**
 * This module provides the capability to media enhancement
 *
 * @namespace avMusicTemplate
 * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
 * @stagemodelonly
 * @since 23
 */
declare namespace avMusicTemplate {
    /**
     * Create an AVMusicTemplate instance.
     *
     * @param { AVMusicTemplateType } accessType - type of access, default is 'smartCar'
     * @returns { AVMusicTemplate } an AVMusicTemplate instance
     * @throws { BusinessError } 801 - Capability not supported.function createAVMusicTemplate
     *     can not work correctly due to limited device capabilities.
     * @throws { BusinessError } 35000001 - Failed to create the AVMusicTemplate.
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    function createAVMusicTemplate(accessType: AVMusicTemplateType): AVMusicTemplate;
    /**
     * Defines the basic callback.
     *
     * @typedef { function } NoParamAsyncCallback
     * @returns { Promise<void> } (void) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type NoParamAsyncCallback = () => Promise<void>;
    /**
     * The query main tabs event.
     *
     * @typedef { function } QueryMainTabsEvent
     * @returns { Promise<MediaTab[]> } (MediaTab[]) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type QueryMainTabsEvent = () => Promise<MediaTab[]>;
    /**
     * The query media tab content event.
     *
     * @typedef { function } QueryMediaTabContentEvent
     * @param { string } tabId - tab id
     * @returns { Promise<MediaTabContent> } (MediaTabContent) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type QueryMediaTabContentEvent = (tabId: string) => Promise<MediaTabContent>;
    /**
     * The query media entity event.
     *
     * @typedef { function } QueryMediaEntityEvent
     * @param { QueryMediaEntityParam } params - query params
     * @returns { Promise<PageMediaEntity> } (PageMediaEntity) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type QueryMediaEntityEvent = (params: QueryMediaEntityParam) => Promise<PageMediaEntity>;
    /**
     * The query compilation event.
     *
     * @typedef { function } QueryCompilationEvent
     * @param { string } compilationId - compilation id
     * @param { number } pageIndex - page index
     * @returns { Promise<PageMediaEntity> } (PageMediaEntity) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type QueryCompilationEvent = (compilationId: string, pageIndex: number) => Promise<PageMediaEntity>;
    /**
     * The query play list event.
     *
     * @typedef { function } QueryPlaylistEvent
     * @param { number } pageIndex - page index
     * @param { Sort } sort - sort
     * @returns { Promise<PageMediaEntity> } (PageMediaEntity) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type QueryPlaylistEvent = (pageIndex: number, sort: Sort) => Promise<PageMediaEntity>;
    /**
     * The query current single event.
     *
     * @typedef { function } QueryCurrentSingleEvent
     * @returns { Promise<Single> } (Single) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type QueryCurrentSingleEvent = () => Promise<Single>;
    /**
     * The query compilation by keyword event.
     *
     * @typedef { function } QueryCompilationByKeywordEvent
     * @param { string } keyword - keyword
     * @returns { Promise<Compilation[]> } (Compilation[]) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type QueryCompilationByKeywordEvent = (keyword: string) => Promise<Compilation[]>;
    /**
     * The query media entity by keyword event.
     *
     * @typedef { function } QueryMediaEntityByKeywordEvent
     * @param { string } keyword - keyword
     * @param { EntityType } searchType - search type
     * @param { number } pageIndex - page index
     * @returns { Promise<PageMediaEntity> } (PageMediaEntity) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type QueryMediaEntityByKeywordEvent = (keyword: string, searchType: EntityType, pageIndex: number) => Promise<PageMediaEntity>;
    /**
     * The query recommend media entity list event.
     *
     * @typedef { function } QueryRecommendMediaEntityListEvent
     * @returns { Promise<MediaEntity[]> } (MediaEntity[]) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type QueryRecommendMediaEntityListEvent = () => Promise<MediaEntity[]>;
    /**
     * The query hot words event.
     *
     * @typedef { function } QueryHotWordsEvent
     * @returns { Promise<string[]> } (string[]) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type QueryHotWordsEvent = () => Promise<string[]>;
    /**
     * The query search history event.
     *
     * @typedef { function } QuerySearchHistoryEvent
     * @returns { Promise<string[]> } (string[]) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type QuerySearchHistoryEvent = () => Promise<string[]>;
    /**
     * The clear search history event.
     *
     * @typedef { function } ClearSearchHistoryEvent
     * @returns { Promise<OperResult> } (OperResult) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type ClearSearchHistoryEvent = () => Promise<OperResult>;
    /**
     * The login event.
     *
     * @typedef { function } LoginEvent
     * @param { LoginType } controlType - control type
     * @param { string } [id] - id
     * @returns { Promise<QrCodeInfo[]> } (QrCodeInfo[]) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type LoginEvent = (controlType: LoginType, id?: string) => Promise<QrCodeInfo[]>;
    /**
     * The request dialog info event.
     *
     * @typedef { function } RequestDialogInfoEvent
     * @param { DialogActionType } actionType - action type
     * @param { DialogActionInfo } [actionInfo] - action info
     * @returns { Promise<DialogInfo> } (DialogInfo) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type RequestDialogInfoEvent = (actionType: DialogActionType, actionInfo?: DialogActionInfo) => Promise<DialogInfo>;
    /**
     * The handle member purchase event.
     *
     * @typedef { function } HandleMemberPurchaseEvent
     * @param { MemberPurchaseInfo } info - info
     * @returns { Promise<DialogInfo> } (DialogInfo) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type HandleMemberPurchaseEvent = (info: MemberPurchaseInfo) => Promise<DialogInfo>;
    /**
     * The query member purchase event.
     *
     * @typedef { function } QueryMemberPurchaseEvent
     * @param { MemberPurchaseType } memberPurchaseType - memberPurchaseType
     * @returns { Promise<MemberPurchaseInfo[]> } (MemberPurchaseInfo[]) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type QueryMemberPurchaseEvent = (memberPurchaseType: MemberPurchaseType) => Promise<MemberPurchaseInfo[]>;
    /**
     * The query custom content event.
     *
     * @typedef { function } QueryCustomContentEvent
     * @param { CustomType[] } queryType - query type
     * @returns { Promise<CustomElement> } (CustomElement) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type QueryCustomContentEvent = (queryType: CustomType[]) => Promise<CustomElement>;
    /**
     * The download media entity event.
     *
     * @typedef { function } DownloadMediaEntityEvent
     * @param { DownloadControlType } controlType - control type
     * @param { MediaEntity } mediaEntity - media entity
     * @returns { Promise<OperResult> } (OperResult) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type DownloadMediaEntityEvent = (controlType: DownloadControlType, mediaEntity: MediaEntity) => Promise<OperResult>;
    /**
     * The settings change event.
     *
     * @typedef { function } SettingsChangeEvent
     * @param { SettingItem } settingItem - setting item
     * @returns { Promise<SettingItem> } (SettingItem) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type SettingsChangeEvent = (settingItem: SettingItem) => Promise<SettingItem>;
    /**
     * The problem and advice event.
     *
     * @typedef { function } ProblemAndAdviceEvent
     * @param { string } advice - advice
     * @returns { Promise<OperResult> } (OperResult) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type ProblemAndAdviceEvent = (advice: string) => Promise<OperResult>;
    /**
     * The play for search event.
     *
     * @typedef { function } ExecuteActionEvent
     * @param { SearchPlayInfoType } command - command
     * @param { SearchPlayInfo } args - args
     * @returns { Promise<OperResult> } (OperResult) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type PlayForSearchEvent = (command: SearchPlayInfoType, args: SearchPlayInfo) => Promise<OperResult>;
    /**
     * The execute action event.
     *
     * @typedef { function } ExecuteActionEvent
     * @param { string } actionType - action type
     * @param { string } params - params
     * @returns { Promise<string> } (string) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type ExecuteActionEvent = (actionType: string, params: string) => Promise<string>;
    /**
     * The play media entity event.
     *
     * @typedef { function } PlayMediaEntityEvent
     * @param { MediaEntity } mediaEntity - media entity
     * @returns { Promise<void> } (void) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type PlayMediaEntityEvent = (mediaEntity: MediaEntity) => Promise<void>;
    /**
     * The favorite media entity event.
     *
     * @typedef { function } FavoriteMediaEntityEvent
     * @param { MediaFavoriteType } actionType - action type
     * @param { MediaEntity } mediaEntity - media entity
     * @returns { Promise<OperResult> } (OperResult) returned through promise
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type FavoriteMediaEntityEvent = (actionType: MediaFavoriteType, mediaEntity: MediaEntity) => Promise<OperResult>;
    /**
     * AVMusicTemplate interface
     *
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    class AVMusicTemplate {
        /**
         * Unique AVMusicTemplate descriptor.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        sessionId: string;
        /**
         * AVMusicTemplate tag.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        sessionTag: string;
        /**
         * Start media center template interface.
         *
         * @returns { Promise<OperResult> } (OperResult) returned through promise
         * @throws { BusinessError } 801 - capability not supported.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        startTemplate(): Promise<OperResult>;
        /**
         * Register query main tabs callback.
         *
         * @param { QueryMainTabsEvent } callback - The callback used to handle ('queryMainTabs') event.
         * @throws { BusinessError } 801 - Capability not supported.function onQueryMainTabs
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onQueryMainTabs(callback: QueryMainTabsEvent): void;
        /**
         * Unregister query main tabs callback.
         *
         * @param { QueryMainTabsEvent } [callback] - The callback used to handle ('queryMainTabs') event.
         * @throws { BusinessError } 801 - Capability not supported.function offQueryMainTabs
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offQueryMainTabs(callback?: QueryMainTabsEvent): void;
        /**
         * Register query media tab content callback.
         *
         * @param { QueryMediaTabContentEvent } callback - The callback used to handle ('queryMediaTabContent') event.
         * @throws { BusinessError } 801 - Capability not supported.function onQueryMediaTabContent
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onQueryMediaTabContent(callback: QueryMediaTabContentEvent): void;
        /**
         * Unregister query media tab content callback.
         *
         * @param { QueryMediaTabContentEvent } [callback] - The callback used to handle ('queryMediaTabContent') event.
         * @throws { BusinessError } 801 - Capability not supported.function offQueryMediaTabContent
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offQueryMediaTabContent(callback?: QueryMediaTabContentEvent): void;
        /**
         * Register query media entity callback.
         *
         * @param { QueryMediaEntityEvent } callback - The callback used to handle ('queryMediaEntity') event.
         * @throws { BusinessError } 801 - Capability not supported.function onQueryMediaEntity
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onQueryMediaEntity(callback: QueryMediaEntityEvent): void;
        /**
         * Unregister query media entity callback.
         *
         * @param { QueryMediaEntityEvent } [callback] - The callback used to handle ('queryMediaEntity') event.
         * @throws { BusinessError } 801 - Capability not supported.function offQueryMediaEntity
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offQueryMediaEntity(callback?: QueryMediaEntityEvent): void;
        /**
         * Register query compilation callback.
         *
         * @param { QueryCompilationEvent } callback - The callback used to handle ('queryCompilation') event.
         * @throws { BusinessError } 801 - Capability not supported.function onQueryCompilation
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onQueryCompilation(callback: QueryCompilationEvent): void;
        /**
         * Unregister query compilation callback.
         *
         * @param { QueryCompilationEvent } [callback] - The callback used to handle ('queryCompilation') event.
         * @throws { BusinessError } 801 - Capability not supported.function offQueryCompilation
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offQueryCompilation(callback?: QueryCompilationEvent): void;
        /**
         * Register query playlist callback.
         *
         * @param { QueryPlaylistEvent } callback - The callback used to handle ('queryPlaylist') event.
         * @throws { BusinessError } 801 - Capability not supported.function onQueryPlaylist
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onQueryPlaylist(callback: QueryPlaylistEvent): void;
        /**
         * Unregister query playlist callback.
         *
         * @param { QueryPlaylistEvent } [callback] - The callback used to handle ('queryPlaylist') event.
         * @throws { BusinessError } 801 - Capability not supported.function offQueryPlaylist
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offQueryPlaylist(callback?: QueryPlaylistEvent): void;
        /**
         * Register query current single callback.
         *
         * @param { QueryCurrentSingleEvent } callback - The callback used to handle ('queryCurrentSingle') event.
         * @throws { BusinessError } 801 - Capability not supported.function onQueryCurrentSingle
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onQueryCurrentSingle(callback: QueryCurrentSingleEvent): void;
        /**
         * Unregister query current single callback.
         *
         * @param { QueryCurrentSingleEvent } [callback] - The callback used to handle ('queryCurrentSingle') event.
         * @throws { BusinessError } 801 - Capability not supported.function offQueryCurrentSingle
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offQueryCurrentSingle(callback?: QueryCurrentSingleEvent): void;
        /**
         * Register query compilation by keyword callback.
         *
         * @param { QueryCompilationByKeywordEvent } callback - The callback used to handle ('queryCompilationByKeyword') event.
         * @throws { BusinessError } 801 - Capability not supported.function onQueryCompilationByKeyword
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onQueryCompilationByKeyword(callback: QueryCompilationByKeywordEvent): void;
        /**
         * Unregister query compilation by keyword callback.
         *
         * @param { QueryCompilationByKeywordEvent } [callback] - The callback used to
         *     handle ('queryCompilationByKeyword') event.
         * @throws { BusinessError } 801 - Capability not supported.function offQueryCompilationByKeyword
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offQueryCompilationByKeyword(callback?: QueryCompilationByKeywordEvent): void;
        /**
         * Register query media entity by keyword callback.
         *
         * @param { QueryMediaEntityByKeywordEvent } callback - The callback used to handle ('queryMediaEntityByKeyword') event.
         * @throws { BusinessError } 801 - Capability not supported.function onQueryMediaEntityByKeyword
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onQueryMediaEntityByKeyword(callback: QueryMediaEntityByKeywordEvent): void;
        /**
         * Unregister query media entity by keyword callback.
         *
         * @param { QueryMediaEntityByKeywordEvent } [callback] - The callback used to
         *     handle ('queryMediaEntityByKeyword') event.
         * @throws { BusinessError } 801 - Capability not supported.function offQueryMediaEntityByKeyword
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offQueryMediaEntityByKeyword(callback?: QueryMediaEntityByKeywordEvent): void;
        /**
         * Register query recommend media entity list callback.
         *
         * @param { QueryRecommendMediaEntityListEvent } callback - The callback used to
         *     handle ('queryRecommendMediaEntityList') event.
         * @throws { BusinessError } 801 - Capability not supported.function onQueryRecommendMediaEntityList
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onQueryRecommendMediaEntityList(callback: QueryRecommendMediaEntityListEvent): void;
        /**
         * Unregister query recommend media entity list callback.
         *
         * @param { QueryRecommendMediaEntityListEvent } [callback]
         *     - The callback used to handle ('queryRecommendMediaEntityList') event.
         * @throws { BusinessError } 801 - Capability not supported.function offQueryRecommendMediaEntityList
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offQueryRecommendMediaEntityList(callback?: QueryRecommendMediaEntityListEvent): void;
        /**
         * Register query hot words callback.
         *
         * @param { QueryHotWordsEvent } callback - The callback used to handle ('queryHotWords') event.
         * @throws { BusinessError } 801 - Capability not supported.function onQueryHotWords
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onQueryHotWords(callback: QueryHotWordsEvent): void;
        /**
         * Unregister query hot words callback.
         *
         * @param { QueryHotWordsEvent } [callback] - The callback used to handle ('queryHotWords') event.
         * @throws { BusinessError } 801 - Capability not supported.function offQueryHotWords
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offQueryHotWords(callback?: QueryHotWordsEvent): void;
        /**
         * Register query search history callback.
         *
         * @param { QuerySearchHistoryEvent } callback - The callback used to handle ('querySearchHistory') event.
         * @throws { BusinessError } 801 - Capability not supported.function onQuerySearchHistory
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onQuerySearchHistory(callback: QuerySearchHistoryEvent): void;
        /**
         * Unregister query search history callback.
         *
         * @param { QuerySearchHistoryEvent } [callback] - The callback used to handle ('querySearchHistory') event.
         * @throws { BusinessError } 801 - Capability not supported.function offQuerySearchHistory
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offQuerySearchHistory(callback?: QuerySearchHistoryEvent): void;
        /**
         * Register clear search history callback.
         *
         * @param { ClearSearchHistoryEvent } callback - The callback used to handle ('clearSearchHistory') event.
         * @throws { BusinessError } 801 - Capability not supported.function onClearSearchHistory
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onClearSearchHistory(callback: ClearSearchHistoryEvent): void;
        /**
         * Unregister clear search history callback.
         *
         * @param { ClearSearchHistoryEvent } [callback] - The callback used to handle ('clearSearchHistory') event.
         * @throws { BusinessError } 801 - Capability not supported.function offClearSearchHistory
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offClearSearchHistory(callback?: ClearSearchHistoryEvent): void;
        /**
         * Register login callback.
         *
         * @param { LoginEvent } callback - The callback used to handle ('login') event.
         * @throws { BusinessError } 801 - Capability not supported.function onLogin
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onLogin(callback: LoginEvent): void;
        /**
         * Unregister login callback.
         *
         * @param { LoginEvent } [callback] - The callback used to handle ('login') event.
         * @throws { BusinessError } 801 - Capability not supported.function offLogin
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offLogin(callback?: LoginEvent): void;
        /**
         * Register request dialog info callback.
         *
         * @param { RequestDialogInfoEvent } callback - The callback used to handle ('requestDialogInfo') event.
         * @throws { BusinessError } 801 - Capability not supported.function onRequestDialogInfo
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onRequestDialogInfo(callback: RequestDialogInfoEvent): void;
        /**
         * Unregister request dialog info callback.
         *
         * @param { RequestDialogInfoEvent } [callback] - The callback used to handle ('requestDialogInfo') event.
         * @throws { BusinessError } 801 - Capability not supported.function offRequestDialogInfo
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offRequestDialogInfo(callback?: RequestDialogInfoEvent): void;
        /**
         * Register handle member purchase callback.
         *
         * @param { HandleMemberPurchaseEvent } callback - The callback used to handle ('handleMemberPurchase') event.
         * @throws { BusinessError } 801 - Capability not supported.function onHandleMemberPurchase
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onHandleMemberPurchase(callback: HandleMemberPurchaseEvent): void;
        /**
         * Unregister handle member purchase callback.
         *
         * @param { HandleMemberPurchaseEvent } [callback] - The callback used to handle ('handleMemberPurchase') event.
         * @throws { BusinessError } 801 - Capability not supported.function offHandleMemberPurchase
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offHandleMemberPurchase(callback?: HandleMemberPurchaseEvent): void;
        /**
         * Register query member purchase callback.
         *
         * @param { QueryMemberPurchaseEvent } callback - The callback used to handle ('queryMemberPurchase') event.
         * @throws { BusinessError } 801 - Capability not supported.function onQueryMemberPurchase
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onQueryMemberPurchase(callback: QueryMemberPurchaseEvent): void;
        /**
         * Unregister query member purchase callback.
         *
         * @param { QueryMemberPurchaseEvent } [callback] - The callback used to handle ('queryMemberPurchase') event.
         * @throws { BusinessError } 801 - Capability not supported.function offQueryMemberPurchase
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offQueryMemberPurchase(callback?: QueryMemberPurchaseEvent): void;
        /**
         * Register query custom content callback.
         *
         * @param { QueryCustomContentEvent } callback - The callback used to handle ('queryCustomContent') event.
         * @throws { BusinessError } 801 - Capability not supported.function onQueryCustomContent
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onQueryCustomContent(callback: QueryCustomContentEvent): void;
        /**
         * Unregister query custom content callback.
         *
         * @param { QueryCustomContentEvent } [callback] - The callback used to handle ('queryCustomContent') event.
         * @throws { BusinessError } 801 - Capability not supported.function offQueryCustomContent
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offQueryCustomContent(callback?: QueryCustomContentEvent): void;
        /**
         * Register download media entity callback.
         *
         * @param { DownloadMediaEntityEvent } callback - The callback used to handle ('downloadMediaEntity') event.
         * @throws { BusinessError } 801 - Capability not supported.function onDownloadMediaEntity
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onDownloadMediaEntity(callback: DownloadMediaEntityEvent): void;
        /**
         * Unregister download media entity callback.
         *
         * @param { DownloadMediaEntityEvent } [callback] - The callback used to handle ('downloadMediaEntity') event.
         * @throws { BusinessError } 801 - Capability not supported.function offDownloadMediaEntity
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offDownloadMediaEntity(callback?: DownloadMediaEntityEvent): void;
        /**
         * Register settings change callback.
         *
         * @param { SettingsChangeEvent } callback - The callback used to handle ('settingsChange') event.
         * @throws { BusinessError } 801 - Capability not supported.function onSettingsChange
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onSettingsChange(callback: SettingsChangeEvent): void;
        /**
         * Unregister settings change callback.
         *
         * @param { SettingsChangeEvent } [callback] - The callback used to handle ('settingsChange') event.
         * @throws { BusinessError } 801 - Capability not supported.function offSettingsChange
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offSettingsChange(callback?: SettingsChangeEvent): void;
        /**
         * Register problem and advice callback.
         *
         * @param { ProblemAndAdviceEvent } callback - The callback used to handle ('problemAndAdvice') event.
         * @throws { BusinessError } 801 - Capability not supported.function onProblemAndAdvice
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onProblemAndAdvice(callback: ProblemAndAdviceEvent): void;
        /**
         * Unregister problem and advice callback.
         *
         * @param { ProblemAndAdviceEvent } [callback] - The callback used to handle ('problemAndAdvice') event.
         * @throws { BusinessError } 801 - Capability not supported.function offProblemAndAdvice
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offProblemAndAdvice(callback?: ProblemAndAdviceEvent): void;
        /**
         * Register play for search callback.
         *
         * @param { PlayForSearchEvent } callback - The callback used to handle ('playForSearch') event.
         * @throws { BusinessError } 801 - Capability not supported.function onPlayForSearch
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onPlayForSearch(callback: PlayForSearchEvent): void;
        /**
         * Unregister play for search callback.
         *
         * @param { PlayForSearchEvent } [callback] - The callback used to handle ('playForSearch') event.
         * @throws { BusinessError } 801 - Capability not supported.function offPlayForSearch
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offPlayForSearch(callback?: PlayForSearchEvent): void;
        /**
         * Register execute action callback.
         *
         * @param { ExecuteActionEvent } callback - The callback used to handle ('executeAction') event.
         * @throws { BusinessError } 801 - Capability not supported.function onExecuteAction
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onExecuteAction(callback: ExecuteActionEvent): void;
        /**
         * Unregister execute action callback.
         *
         * @param { ExecuteActionEvent } [callback] - The callback used to handle ('executeAction') event.
         * @throws { BusinessError } 801 - Capability not supported.function offExecuteAction
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offExecuteAction(callback?: ExecuteActionEvent): void;
        /**
         * Register play media entity callback.
         *
         * @param { PlayMediaEntityEvent } callback - The callback used to handle ('playMediaEntity') event.
         * @throws { BusinessError } 801 - Capability not supported.function onPlayMediaEntity
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onPlayMediaEntity(callback: PlayMediaEntityEvent): void;
        /**
         * Unregister play media entity callback.
         *
         * @param { PlayMediaEntityEvent } [callback] - The callback used to handle ('playMediaEntity') event.
         * @throws { BusinessError } 801 - Capability not supported.function offPlayMediaEntity
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offPlayMediaEntity(callback?: PlayMediaEntityEvent): void;
        /**
         * Register favorite media entity callback.
         *
         * @param { FavoriteMediaEntityEvent } callback - The callback used to handle ('favoriteMediaEntity') event.
         * @throws { BusinessError } 801 - Capability not supported.function onFavoriteMediaEntity
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onFavoriteMediaEntity(callback: FavoriteMediaEntityEvent): void;
        /**
         * Unregister favorite media entity callback.
         *
         * @param { FavoriteMediaEntityEvent } [callback] - The callback used to handle ('favoriteMediaEntity') event.
         * @throws { BusinessError } 801 - Capability not supported.function offFavoriteMediaEntity
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offFavoriteMediaEntity(callback?: FavoriteMediaEntityEvent): void;
        /**
         * Report user infomation to MediaUI.
         *
         * @param { UserInfo } userInfo - user information
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 801 - Capability not supported.function setUserInfo
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000011 - The data write error, data is invalid.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        setUserInfo(userInfo: UserInfo): Promise<void>;
        /**
         * Report dialog command to MediaUI.
         *
         * @param { DialogControlType } type - dialog control type
         * @param { DialogInfo } dialogInfo - dialog information
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 801 - Capability not supported.function setDialogCommand
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000011 - The data write error, data is invalid.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        setDialogCommand(type: DialogControlType, dialogInfo: DialogInfo): Promise<void>;
        /**
         * Report current single song to MediaUI.
         *
         * @param { Single } single - single information
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 801 - Capability not supported.function setCurrentSingle
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000011 - The data write error, data is invalid.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        setCurrentSingle(single: Single): Promise<void>;
        /**
         * Report media resource change information to MediaUI.
         *
         * @param { MediaEntity[] } entities - media resource information
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 801 - Capability not supported.function setMediaEntities
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000011 - The data write error, data is invalid.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        setMediaEntities(entities: MediaEntity[]): Promise<void>;
        /**
         * Report tab page content information to MediaUI.
         *
         * @param { string } tabId - tab page id
         * @param { MediaTabContent } tabContent - tab page content
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 801 - Capability not supported.function setTabContent
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000011 - The data write error, data is invalid.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        setTabContent(tabId: string, tabContent: MediaTabContent): Promise<void>;
        /**
         * Report play list information to MediaUI.
         *
         * @param { PageMediaEntity } playlist - play list information
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 801 - Capability not supported.function setPlaylist
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000011 - The data write error, data is invalid.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        setPlaylist(playlist: PageMediaEntity): Promise<void>;
        /**
         * Report single download status information to MediaUI.
         *
         * @param { MediaEntity } single - single information
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 801 - Capability not supported.function setDownloadMediaEntityStatus
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000011 - The data write error, data is invalid.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        setDownloadMediaEntityStatus(single: MediaEntity): Promise<void>;
        /**
         * Report custom elements change information to MediaUI.
         *
         * @param { ActionType } actionType - action type
         * @param { CustomType } customType - custom type
         * @param { CustomElement } customElement - custom element
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 801 - Capability not supported.function setCustomElements
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000011 - The data write error, data is invalid.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        setCustomElements(actionType: ActionType, customType: CustomType, customElement: CustomElement): Promise<void>;
        /**
         * Report settings information to MediaUI.
         *
         * @param { SettingItem[] } settingItems - setting items
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 801 - Capability not supported.function setSettings
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000011 - The data write error, data is invalid.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        setSettings(settingItems: SettingItem[]): Promise<void>;
        /**
         * Report execute action information to MediaUI.
         *
         * @param { string } actionType - action type
         * @param { string } params - params value
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 801 - Capability not supported.function reportExecuteAction
         *     can not work correctly due to limited device capabilities.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000011 - The data write error, data is invalid.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        reportExecuteAction(actionType: string, params: string): Promise<void>;
        /**
         * Report execute extension ability to MediaUI.
         *
         * @param { WantAgent } want - ability info
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000011 - The data write error, data is invalid.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        setExtensionAbility(want: WantAgent): Promise<void>;
        /**
         * Destroy the AVMusicTemplate instance.
         *
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 801 - Capability not supported.function destroy
         *     can not work correctly due to limited device capabilities.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        destroy(): Promise<void>;
    }
    /**
     * The definition of the AVMusicTemplateController.
     *
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    class AVMusicTemplateController {
        /**
         * Unique id of the AVMusicTemplateController.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        sessionId: string;
        /**
         * Mark the controller is or not destroy.
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        isDestroy: boolean;
        /**
         * Query main tabs.
         *
         * @returns { Promise<MediaTab[]> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        queryMainTabs(): Promise<MediaTab[]>;
        /**
         * Query media tab content.
         *
         * @param { string } tabId - tab id
         * @returns { Promise<MediaTabContent> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        queryMediaTabContent(tabId: string): Promise<MediaTabContent>;
        /**
         * Query media entity.
         *
         * @param { QueryMediaEntityParam } params - query params
         * @returns { Promise<PageMediaEntity> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        queryMediaEntity(params: QueryMediaEntityParam): Promise<PageMediaEntity>;
        /**
         * Query compilation.
         *
         * @param { string } compilationId - compilation id
         * @param { number } pageIndex - page index
         * @returns { Promise<PageMediaEntity> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        queryCompilation(compilationId: string, pageIndex: number): Promise<PageMediaEntity>;
        /**
         * Query playlist.
         *
         * @param { number } pageIndex - page index
         * @param { Sort } sort - sort type
         * @returns { Promise<PageMediaEntity> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        queryPlaylist(pageIndex: number, sort: Sort): Promise<PageMediaEntity>;
        /**
         * Query current single.
         *
         * @returns { Promise<Single> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        queryCurrentSingle(): Promise<Single>;
        /**
         * Query compilation by keyword.
         *
         * @param { string } keyword - keyword
         * @returns { Promise<Compilation[]> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        queryCompilationByKeyword(keyword: string): Promise<Compilation[]>;
        /**
         * Query media entity by keyword.
         *
         * @param { string } keyword - keyword
         * @param { EntityType } searchType - search type
         * @param { number } pageIndex - page index
         * @returns { Promise<PageMediaEntity> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        queryMediaEntityByKeyword(keyword: string, searchType: EntityType, pageIndex: number): Promise<PageMediaEntity>;
        /**
         * Query recommend media entity list.
         *
         * @returns { Promise<MediaEntity[]> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        queryRecommendMediaEntityList(): Promise<MediaEntity[]>;
        /**
         * Query hot words.
         *
         * @returns { Promise<string[]> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        queryHotWords(): Promise<string[]>;
        /**
         * Query search history.
         *
         * @returns { Promise<string[]> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        querySearchHistory(): Promise<string[]>;
        /**
         * Clear search history.
         *
         * @returns { Promise<OperResult> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        clearSearchHistory(): Promise<OperResult>;
        /**
         * Report settings change.
         *
         * @param { SettingItem } settingItem - setting item
         * @returns { Promise<SettingItem> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        updateSettings(settingItem: SettingItem): Promise<SettingItem>;
        /**
         * Report problem and advice.
         *
         * @param { string } advice - advice
         * @returns { Promise<OperResult> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        reportProblemAndAdvice(advice: string): Promise<OperResult>;
        /**
         * Login.
         *
         * @param { LoginType } controlType - control type
         * @param { string } [id] - id
         * @returns { Promise<QrCodeInfo[]> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        login(controlType: LoginType, id?: string): Promise<QrCodeInfo[]>;
        /**
         * Request dialog info.
         *
         * @param { DialogActionType } actionType - action type
         * @param { DialogActionInfo } [actionInfo] - action info
         * @returns { Promise<DialogInfo> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        requestDialogInfo(actionType: DialogActionType, actionInfo?: DialogActionInfo): Promise<DialogInfo>;
        /**
         * Handle member purchase.
         *
         * @param { MemberPurchaseInfo } info - info
         * @returns { Promise<DialogInfo> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        handleMemberPurchase(info: MemberPurchaseInfo): Promise<DialogInfo>;
        /**
         * Query member purchase.
         *
         * @param { MemberPurchaseType } memberPurchaseType - memberPurchase type
         * @returns { Promise<MemberPurchaseInfo[]> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        queryMemberPurchase(memberPurchaseType: MemberPurchaseType): Promise<MemberPurchaseInfo[]>;
        /**
         * Query custom content.
         *
         * @param { CustomType[] } queryType - query type
         * @returns { Promise<CustomElement> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        queryCustomContent(queryType: CustomType[]): Promise<CustomElement>;
        /**
         * Download media entity.
         *
         * @param { DownloadControlType } controlType - control type
         * @param { MediaEntity } mediaEntity - media entity
         * @returns { Promise<OperResult> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        downloadMediaEntity(controlType: DownloadControlType, mediaEntity: MediaEntity): Promise<OperResult>;
        /**
         * Play for search.
         *
         * @param { SearchPlayInfoType } command - command
         * @param { SearchPlayInfo } args - args
         * @returns { Promise<OperResult> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        playForSearch(command: SearchPlayInfoType, args: SearchPlayInfo): Promise<OperResult>;
        /**
         * Execute action.
         *
         * @param { string } actionType - action type
         * @param { string } params - params
         * @returns { Promise<string> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        executeAction(actionType: string, params: string): Promise<string>;
        /**
         * Play media entity.
         *
         * @param { MediaEntity } mediaEntity - media entity
         * @returns { Promise<void> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        playMediaEntity(mediaEntity: MediaEntity): Promise<void>;
        /**
         * Favorite media entity.
         *
         * @param { MediaFavoriteType } actionType - action type
         * @param { MediaEntity } mediaEntity - media entity
         * @returns { Promise<OperResult> } Promise for the result
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000003 - Template listener not registered.
         * @throws { BusinessError } 35000005 - AVMusicTemplate does not exist.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        favoriteMediaEntity(actionType: MediaFavoriteType, mediaEntity: MediaEntity): Promise<OperResult>;
        /**
         * Register report user info callback.
         *
         * @param { Callback<UserInfo> } callback - The callback used to handle ('reportUserInfo') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onUserInfoChange(callback: Callback<UserInfo>): void;
        /**
         * Unregister report user info callback.
         *
         * @param { Callback<UserInfo> } [callback] - The callback used to handle ('reportUserInfo') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offUserInfoChange(callback?: Callback<UserInfo>): void;
        /**
         * Register report dialog command callback.
         *
         * @param { ReportDialogCommandEvent } callback - The callback used to handle ('reportDialogCommand') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onDialogCommandChange(callback: ReportDialogCommandEvent): void;
        /**
         * Unregister report dialog command callback.
         *
         * @param { ReportDialogCommandEvent } [callback] - The callback used to handle ('reportDialogCommand') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offDialogCommandChange(callback?: ReportDialogCommandEvent): void;
        /**
         * Register report current single callback.
         *
         * @param { Callback<Single> } callback - The callback used to handle ('reportCurrentSingle') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onCurrentSingleChange(callback: Callback<Single>): void;
        /**
         * Unregister report current single callback.
         *
         * @param { Callback<Single> } [callback] - The callback used to handle ('reportCurrentSingle') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offCurrentSingleChange(callback?: Callback<Single>): void;
        /**
         * Register report media entities change callback.
         *
         * @param { Callback<MediaEntity[]> } callback - The callback used to handle ('reportMediaEntitiesChange') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onMediaEntitiesChange(callback: Callback<MediaEntity[]>): void;
        /**
         * Unregister report media entities change callback.
         *
         * @param { Callback<MediaEntity[]> } [callback] - The callback used to handle ('reportMediaEntitiesChange') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offMediaEntitiesChange(callback?: Callback<MediaEntity[]>): void;
        /**
         * Register report tab content callback.
         *
         * @param { ReportTabContentEvent } callback - The callback used to handle ('reportTabContent') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onTabContentChange(callback: ReportTabContentEvent): void;
        /**
         * Unregister report tab content callback.
         *
         * @param { ReportTabContentEvent } [callback] - The callback used to handle ('reportTabContent') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offTabContentChange(callback?: ReportTabContentEvent): void;
        /**
         * Register report playlist callback.
         *
         * @param { Callback<PageMediaEntity> } callback - The callback used to handle ('reportPlaylist') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onPlaylistChange(callback: Callback<PageMediaEntity>): void;
        /**
         * Unregister report playlist callback.
         *
         * @param { Callback<PageMediaEntity> } [callback] - The callback used to handle ('reportPlaylist') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offPlaylistChange(callback?: Callback<PageMediaEntity>): void;
        /**
         * Register report download media entity status callback.
         *
         * @param { Callback<MediaEntity> } callback - The callback
         *     used to handle ('reportDownloadMediaEntityStatus') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onDownloadMediaEntityStatusChange(callback: Callback<MediaEntity>): void;
        /**
         * Unregister report download media entity status callback.
         *
         * @param { Callback<MediaEntity> } [callback] - The callback
         *     used to handle ('reportDownloadMediaEntityStatus') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offDownloadMediaEntityStatusChange(callback?: Callback<MediaEntity>): void;
        /**
         * Register report custom elements change callback.
         *
         * @param { ReportCustomElementsChangeEvent } callback - The callback
         *     used to handle ('reportCustomElementsChange') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onCustomElementsChange(callback: ReportCustomElementsChangeEvent): void;
        /**
         * Unregister report custom elements change callback.
         *
         * @param { ReportCustomElementsChangeEvent } [callback] - The callback
         *     used to handle ('reportCustomElementsChange') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offCustomElementsChange(callback?: ReportCustomElementsChangeEvent): void;
        /**
         * Register report settings callback.
         *
         * @param { Callback<SettingItem[]> } callback - The callback used to handle ('reportSettings') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onSettingsChange(callback: Callback<SettingItem[]>): void;
        /**
         * Unregister report settings callback.
         *
         * @param { Callback<SettingItem[]> } [callback] - The callback used to handle ('reportSettings') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offSettingsChange(callback?: Callback<SettingItem[]>): void;
        /**
         * Register report execute action callback.
         *
         * @param { ReportExecuteActionEvent } callback - The callback used to handle ('reportExecuteAction') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onReportExecuteAction(callback: ReportExecuteActionEvent): void;
        /**
         * Unregister report execute action callback.
         *
         * @param { ReportExecuteActionEvent } [callback] - The callback used to handle ('reportExecuteAction') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offReportExecuteAction(callback?: ReportExecuteActionEvent): void;
        /**
         * Register report extension ability callback.
         *
         * @param { ReportExecuteAbilityEvent } callback - The callback used to handle ('setExtensionAbility') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        onExtensionAbilityChange(callback: ReportExecuteAbilityEvent): void;
        /**
         * Unregister report extension ability callback.
         *
         * @param { ReportExecuteAbilityEvent } [callback] - The callback used to handle ('setExtensionAbility') event.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 35000006 - AVMusicTemplateController does not exist.
         * @throws { BusinessError } 35000012 - AVMusicTemplate error.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        offExtensionAbilityChange(callback?: ReportExecuteAbilityEvent): void;
        /**
         * Destroy the controller.
         *
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 801 - capability not supported.
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        destroy(): Promise<void>;
    }
    /**
     * The report dialog command event.
     *
     * @typedef { function } ReportDialogCommandEvent
     * @param { DialogControlType } type - type
     * @param { DialogInfo } buttonInfo - button info
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type ReportDialogCommandEvent = (type: DialogControlType, buttonInfo: DialogInfo) => void;
    /**
     * The report tab content event.
     *
     * @typedef { function } ReportTabContentEvent
     * @param { string } tabId - tab id
     * @param { MediaTabContent } tabContent - tab content
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type ReportTabContentEvent = (tabId: string, tabContent: MediaTabContent) => void;
    /**
     * The report custom elements change event.
     *
     * @typedef { function } ReportCustomElementsChangeEvent
     * @param { ActionType } actionType - action type
     * @param { CustomType } customType - custom type
     * @param { CustomElement } customElement - custom element
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type ReportCustomElementsChangeEvent = (actionType: ActionType, customType: CustomType, customElement: CustomElement) => void;
    /**
     * The report execute action event.
     *
     * @typedef { function } ReportExecuteActionEvent
     * @param { string } actionType - action type
     * @param { string } params - params
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type ReportExecuteActionEvent = (actionType: string, params: string) => void;
    /**
     * The report extension ability event.
     *
     * @typedef { function } ReportExecuteActionEvent
     * @param { WantAgent } want - ability info
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type ReportExecuteAbilityEvent = (want: WantAgent) => void;
    /**
     * Media favorite type addFavorite & removeFavorite.
     *
     * @typedef { 'addFavorite' | 'removeFavorite' } MediaFavoriteType
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type MediaFavoriteType = 'addFavorite' | 'removeFavorite';
    /**
     * Action type add & remove.
     *
     * @typedef { 'add' | 'remove' } ActionType
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type ActionType = 'add' | 'remove';
    /**
     * Custom tab type USER_INFO & TAB, COMPILATION, SETTINGS.
     *
     * @typedef { 'USER_INFO' | 'TAB' | 'COMPILATION' | 'SETTINGS' } CustomType
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type CustomType = 'USER_INFO' | 'TAB' | 'COMPILATION' | 'SETTINGS';
    /**
     * Download control type startDownload & deleteDownload, resumeDownload, pauseDownload.
     *
     * @typedef { 'startDownload' | 'deleteDownload' | 'resumeDownload' | 'pauseDownload' } DownloadControlType
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type DownloadControlType = 'startDownload' | 'deleteDownload' | 'resumeDownload' | 'pauseDownload';
    /**
     * Login type queryLoginInfo & refreshLoginInfo, logout.
     *
     * @typedef { 'queryLoginInfo' | 'refreshLoginInfo' | 'cancel' | 'logout' } LoginType
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type LoginType = 'queryLoginInfo' | 'refreshLoginInfo' | 'cancel' | 'logout';
    /**
     * Dialog action type open & close, refresh.
     *
     * @typedef { 'open' | 'close' | 'refresh' } DialogActionType
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type DialogActionType = 'open' | 'close' | 'refresh';
    /**
     * Dialog control type open & close, refresh, toast.
     *
     * @typedef { 'open' | 'close' | 'refresh' | 'toast' } DialogControlType
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    type DialogControlType = 'open' | 'close' | 'refresh' | 'toast';
    /**
     * The definition of the operate result.
     *
     * @interface OperResult
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface OperResult {
        /**
         * error code.
         *
         * @type { number }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        errorCode: number;
        /**
         * error message.
         *
         * @type { ?string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        errorMsg?: string;
    }
    /**
     * The definition of the tab page.
     *
     * @interface MediaTab
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface MediaTab {
        /**
         * Unique ID of the tab page.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        tabId: string;
        /**
         * The tab page name.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        tabName: string;
        /**
         * The tab page icon, main page required.
         *
         * @type { ?image.PixelMap }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        tabIcon?: image.PixelMap;
        /**
         * Additional content on tab page.
         *
         * @type { ?string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        extraDataJson?: string;
    }
    /**
     * The definition of the tab page content.
     *
     * @extends OperResult
     * @interface MediaTabContent
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface MediaTabContent extends OperResult {
        /**
         * Tab id corresponding to the content.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        tabId: string;
        /**
         * Compilations content of the tab page.
         *
         * @type { Compilation[] }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        compilations: Compilation[];
    }
    /**
     * Custom elements of mine page.
     *
     * @extends OperResult
     * @interface CustomElement
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface CustomElement extends OperResult {
        /**
         * User information
         *
         * @type { ?UserInfo }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        userInfo?: UserInfo;
        /**
         * Tab pages information
         *
         * @type { ?MediaTab[] }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        tabs?: MediaTab[];
        /**
         * Compilations of categories
         *
         * @type { ?Compilation[] }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        customCompilations?: Compilation[];
        /**
         * Settings information
         *
         * @type { ?SettingItem[] }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        settings?: SettingItem[];
    }
    /**
     * The definition of compilation.
     *
     * @extends OperResult
     * @interface Compilation
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface Compilation extends OperResult {
        /**
         * Unique ID of the compilation
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        id: string;
        /**
         * Title of the compilation
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        title: string;
        /**
         * Having more compilation data
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        hasMoreData: boolean;
        /**
         * Total size of the compilation
         *
         * @type { number }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        totalSize: number;
        /**
         * Media type of the compilation
         *
         * @type { EntityType }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        memberMediaType: EntityType;
        /**
         * Content of the compilation
         *
         * @type { MediaEntity[] }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        topElements: MediaEntity[];
    }
    /**
     * The definition of pagination object.
     *
     * @extends OperResult
     * @interface PageMediaEntity
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface PageMediaEntity extends OperResult {
        /**
         * Pagination query page number.
         *
         * @type { number }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        pageIndex: number;
        /**
         * Size of per page.
         *
         * @type { number }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        pageSize: number;
        /**
         * Have next page data.
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        hasMoreData: boolean;
        /**
         * Total size of data.
         *
         * @type { number }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        totalSize: number;
        /**
         * Media type.
         *
         * @type { EntityType }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        memberMediaType: EntityType;
        /**
         * Query data content (pass corresponding structure data according to the type).
         *
         * @type { MediaEntity[] }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        elements: MediaEntity[];
        /**
         * Data Sorting
         *
         * @type { ?Sort }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        sort?: Sort;
        /**
         * Episode Range
         *
         * @type { ?EpisodeRange }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        episodeRange?: EpisodeRange;
    }
    /**
     * The definition of MediaEntity.
     *
     * @interface MediaEntity
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface MediaEntity {
        /**
         * Unique ID of the media resource.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        mediaId: string;
        /**
         * Type of the media resource.
         *
         * @type { EntityType }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        mediaType: EntityType;
        /**
         * Parent id of the media resource.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        parentId: string;
        /**
         * Parent media type of the media resource.
         *
         * @type { EntityType }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        parentMediaType: EntityType;
        /**
         * Title of the media resource.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        title: string;
        /**
         * Description of the media resource.
         *
         * @type { ?string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        desc?: string;
        /**
         * Cover image url of the media resource.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        imageUrl: string;
        /**
         * Play state of the media resource.
         *
         * @type { PlaybackState }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        playState: PlaybackState;
    }
    /**
     * The definition of Singer/Radio/Banner.
     *
     * @extends MediaEntity
     * @interface MediaElement
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface MediaElement extends MediaEntity {
    }
    /**
     * The definition of Banner.
     *
     * @extends MediaEntity
     * @interface Banner
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface Banner extends MediaEntity {
        /**
         * Is support one play
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        isSupportOnePlay: boolean;
    }
    /**
     * The definition of Album.
     *
     * @extends MediaEntity
     * @interface Album
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface Album extends MediaEntity {
        /**
         * Singer name.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        singer: string;
        /**
         * Play counts.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        playCounts: string;
        /**
         * Favorite/Subscribe information.
         *
         * @type { FavoriteData }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        favSubscribeData: FavoriteData;
        /**
         * Total number of episodes in the program
         *
         * @type { ?string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        episodeCounts?: string;
    }
    /**
     * The definition of Single song.
     *
     * @extends MediaEntity
     * @interface Single
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface Single extends MediaEntity {
        /**
         * Is vip song.
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        isVip: boolean;
        /**
         * Singer name.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        singer: string;
        /**
         * Play information.
         *
         * @type { PlayInfo }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        playInfo: PlayInfo;
        /**
         * Favorite/Subscribe information.
         *
         * @type { FavoriteData }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        favSubscribeData: FavoriteData;
        /**
         * Tags of the song.
         *
         * @type { ?string[] }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        tags?: string[];
        /**
         * Settings of the song.
         *
         * @type { ?SettingItem[] }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        settings?: SettingItem[];
        /**
         * DownloadStatus of the song.
         *
         * @type { ?DownloadStatus }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        downloadStatus?: DownloadStatus;
        /**
         * DownloadProgress of the song.
         *
         * @type { ?number }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        downloadProgress?: number;
    }
    /**
     * Enumeration of DownloadStatus.
     *
     * @enum { number }
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    enum DownloadStatus {
        /**
         * DOWNLOAD_SUCCESS
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        DOWNLOAD_SUCCESS = 0,
        /**
         * DOWNLOADING
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        DOWNLOADING = 1,
        /**
         * DOWNLOAD_FAIL
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        DOWNLOAD_FAIL = 2
    }
    /**
     * The definition of Ranking.
     *
     * @extends MediaEntity
     * @interface Ranking
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface Ranking extends MediaEntity {
        /**
         * Recommended songs under the chart.
         *
         * @type { MediaEntity[] }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        topElements: MediaEntity[];
    }
    /**
     * The definition of play information.
     *
     * @interface PlayInfo
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface PlayInfo {
        /**
         * Play counts.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        playCounts: string;
        /**
         * Is support next.
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        isSupportNext: boolean;
        /**
         * Is support prev.
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        isSupportPrev: boolean;
        /**
         * Is support quick forward.
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        isSupportQuickForward: boolean;
        /**
         * Is support quick backward.
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        isSupportQuickBackward: boolean;
        /**
         * The step of quick forward.
         *
         * @type { number }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        quickForwardStep: number;
        /**
         * The step of quick backward.
         *
         * @type { number }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        quickBackwardStep: number;
        /**
         * Is support skip opening credits.
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        isSupportSkipHead: boolean;
        /**
         * Is support skip closing credits.
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        isSupportSkipTail: boolean;
        /**
         * Is support switch play mode.
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        isSupportPlayMode: boolean;
        /**
         * Is support change play rate.
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        isSupportPlayRate: boolean;
        /**
         * Supported play rate.
         *
         * @type { string[] }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        supportedPlayRate: string[];
        /**
         * Current play rate.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        currentPlayRate: string;
        /**
         * Is supported sound quality.
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        isSupportSoundQuality: boolean;
        /**
         * Is supported sound effect.
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        isSupportSoundEffect: boolean;
        /**
         * Total duration.
         *
         * @type { number }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        totalDuration: number;
        /**
         * Current duration.
         *
         * @type { number }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        currentPlayDuration: number;
        /**
         * Is supported progress, default true.
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        isSupportProgress: boolean;
    }
    /**
     * The definition of Favorite/Subscribe.
     *
     * @interface FavoriteData
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface FavoriteData {
        /**
         * Is supported favorite.
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        isSupportFav: boolean;
        /**
         * Is favorite.
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        isFavorite: boolean;
        /**
         * Favorite counts.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        favCounts: string;
    }
    /**
     * The definition of User information.
     *
     * @interface UserInfo
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface UserInfo {
        /**
         * Unique id of the user.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        userInfoId: string;
        /**
         * Nick name of the user.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        nickName: string;
        /**
         * Profile pic url of the user.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        profilePicUrl: string;
        /**
         * Other descriptions of the user.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        tips: string;
        /**
         * User is login.
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        isLogin: boolean;
        /**
         * User is vip.
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        isVip: boolean;
    }
    /**
     * The definition of member purchase information.
     *
     * @interface MemberPurchaseInfo
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface MemberPurchaseInfo {
        /**
         * Unique id of the member purchase information.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        id: string;
        /**
         * The URL for the member purchase illustration must be in 21:9 aspect ratio.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        diagramUrl: string;
        /**
         * Member purchase diagram.
         *
         * @type { ?image.PixelMap }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        diagramData?: image.PixelMap;
        /**
         * Member purchase diagram content.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        diagramContent: string;
        /**
         * Member purchase type
         *
         * @type { MemberPurchaseType }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        memberPurchaseType: MemberPurchaseType;
    }
    /**
     * The definition of QR code Information.
     *
     * @interface QrCodeInfo
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface QrCodeInfo {
        /**
         * A QR code session used to uniquely identify a user login.
         * When the QR code expires,
         * MediaUI will use this ID to query and update a new QR code from the third party.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        id: string;
        /**
         * Purchase price.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        price: string;
        /**
         * Title name.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        titleName: string;
        /**
         * Detail name.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        detailName: string;
        /**
         * Tips message.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        tips: string;
        /**
         * The icon of the app associated with the QR code,
         * such as a QR code for logging in via WeChat, should be the WeChat icon.
         *
         * @type { ?image.PixelMap }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        icon?: image.PixelMap;
        /**
         * QR code content.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        content: string;
        /**
         * QR code image.
         *
         * @type { ?image.PixelMap }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        codeData?: image.PixelMap;
        /**
         * QR code validity period (unit: seconds).
         * When the QR code expires,
         * the QR code ID will be used to query and obtain a new QR code again.
         *
         * @type { number }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        validPeriod: number;
    }
    /**
     * The definition of setting Information.
     *
     * @interface SettingItem
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface SettingItem {
        /**
         * Unique ID of the setting item.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        id: string;
        /**
         * Title of the setting item.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        title: string;
        /**
         * Description of the setting item.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        desc: string;
        /**
         * Type of the setting item.
         *
         * @type { ?SettingType }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        settingType?: SettingType;
        /**
         * Value of the setting item.
         * SWITCH: bool, LIST: SettingContent, JUMP: string.
         *
         * @type { ?(string | boolean | SettingContent[] | WantAgent) }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        settingValue?: string | boolean | SettingContent[] | WantAgent;
        /**
         * Media id associated with the current settings.
         * If the settings are associated with the current media information,
         * you need to set the mediaId; otherwise,
         * it is not required to set the mediaId.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        mediaId: string;
    }
    /**
     * The definition of setting content
     *
     * @interface SettingContent
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface SettingContent {
        /**
         * Value of the setting content.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        value: string;
        /**
         * Is selected the setting content.
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        isSelected: boolean;
        /**
         * Text descriptions of the setting content.
         *
         * @type { ?string[] }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        textTags?: string[];
        /**
         * Tag descriptions of the setting content.
         *
         * @type { ?image.PixelMap[] }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        imageTags?: image.PixelMap[];
    }
    /**
     * The definition of dialog action result.
     *
     * @interface DialogActionInfo
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface DialogActionInfo {
        /**
         * Unique ID of the dialog action.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        dialogId: string;
        /**
         * Is the checkbox in the pop-up window selected.
         *
         * @type { boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        isChecked: boolean;
        /**
         * Id of the button clicked by the user.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        clickedBtnId: string;
    }
    /**
     * The definition of dialog information.
     *
     * @interface DialogInfo
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface DialogInfo {
        /**
         * Unique id of the dialog.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        dialogId: string;
        /**
         * Type of the dialog.
         *
         * @type { DialogType }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        dialogType: DialogType;
        /**
         * Title of the dialog.
         *
         * @type { ?string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        title?: string;
        /**
         * Text content of the dialog.
         *
         * @type { ?string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        text?: string;
        /**
         * Buttons of the dialog.
         *
         * @type { ?DialogButtonInfo[] }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        buttons?: DialogButtonInfo[];
        /**
         * QR code of the dialog.
         * Once the QR code information is set,
         * this pop-up will be recognized as a QR code pop-up and will display the QR code information with priority.
         * A maximum of two can be set.
         *
         * @type { ?QrCodeInfo[] }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        qrCodes?: QrCodeInfo[];
        /**
         * Other message of the dialog.
         *
         * @type { ?string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        description?: string;
    }
    /**
     * The definition of dialog button information.
     *
     * @interface DialogButtonInfo
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface DialogButtonInfo {
        /**
         * Button id.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        buttonId: string;
        /**
         * Button text.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        buttonText: string;
        /**
         * Button type.
         *
         * @type { ButtonType }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        buttonType: ButtonType;
    }
    /**
     * The definition of SearchPlayMusicItem.
     *
     * @interface SearchPlayMusicItem
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface SearchPlayMusicItem {
        /**
         * Unique id of the Media.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        entityId: string;
        /**
         * Name of the Media.
         *
         * @type { ?string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        entityName?: string;
    }
    /**
     * The definition of SearchPlayMusicInfo.
     *
     * @interface SearchPlayMusicInfo
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface SearchPlayMusicInfo {
        /**
         * list of music
         *
         * @type { SearchPlayMusicItem[] }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        items: SearchPlayMusicItem[];
        /**
         * displayName of the Media.
         *
         * @type { ?string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        displayName?: string;
        /**
         * Other descriptions of the Media.
         *
         * @type { ?string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        description?: string;
        /**
         * playMusicOnly of the Media.
         *
         * @type { ?boolean }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        playMusicOnly?: boolean;
        /**
         * playMode of the Media.
         *
         * @type { ?string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        playMode?: string;
    }
    /**
     * The definition of SearchPlayVideoInfo.
     *
     * @interface SearchPlayVideoInfo
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface SearchPlayVideoInfo {
        /**
         * Unique id of the Media.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        entityId: string;
        /**
         * The episodeId of the video.
         *
         * @type { ?string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        episodeId?: string;
        /**
         * The episodeNumber of the video.
         *
         * @type { ?number }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        episodeNumber?: number;
        /**
         * The extras of the video.
         *
         * @type { ?string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        extras?: string;
    }
    /**
     * The definition of SearchPlayInfo.
     *
     * @interface SearchPlayInfo
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface SearchPlayInfo {
        /**
         * The musicInfo of SearchPlayInfo.
         *
         * @type { ?SearchPlayMusicInfo }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        musicInfo?: SearchPlayMusicInfo;
        /**
         * The videoInfo of SearchPlayInfo.
         *
         * @type { ?SearchPlayVideoInfo }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        videoInfo?: SearchPlayVideoInfo;
    }
    /**
     * The definition of EpisodeRange.
     *
     * @interface EpisodeRange
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface EpisodeRange {
        /**
         * Start Index.
         *
         * @type { number }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        start: number;
        /**
         * End Index.
         *
         * @type { number }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        end: number;
    }
    /**
     * The definition of QueryMediaEntityParam.
     *
     * @interface QueryMediaEntityParam
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    interface QueryMediaEntityParam {
        /**
         * entityId.
         *
         * @type { string }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        entityId: string;
        /**
         * pageIndex.
         *
         * @type { number }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        pageIndex: number;
        /**
         * type.
         *
         * @type { EntityType }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        type: EntityType;
        /**
         * subEntityType.
         *
         * @type { ?EntityType }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        subEntityType?: EntityType;
        /**
         * sort.
         *
         * @type { ?Sort }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        sort?: Sort;
        /**
         * episodeRange.
         *
         * @type { ?EpisodeRange }
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        episodeRange?: EpisodeRange;
    }
    /**
     * Enumeration of setting type.
     *
     * @enum { number }
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    enum SettingType {
        /**
         * Switch, the type of setting is used to control the on/off status of a function.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        SWITCH = 0,
        /**
         * List, this type of setting is used for selecting one option from multiple choices.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        LIST = 1,
        /**
         * Jump, this type of setting is used to jump to another interface.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        JUMP = 2
    }
    /**
     * Enumeration of dialog type.
     *
     * @enum { number }
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    enum DialogType {
        /**
         * Normal dialog box.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        NORMAL = 0,
        /**
         * Internet dialog box.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        INTERNET = 1,
        /**
         * Flow dialog box.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        FLOW = 2,
        /**
         * Paid dialog box.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        PAID = 3,
        /**
         * Vip dialog box.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        VIP = 4,
        /**
         * Login dialog box.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        LOGIN = 5,
        /**
         * Error dialog box.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        ERROR = 6,
        /**
         * Unknown dialog box.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        UNKNOWN = 7
    }
    /**
     * Enumeration of button type.
     *
     * @enum { number }
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    enum ButtonType {
        /**
         * Normal button.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        NORMAL = 0,
        /**
         * Emphasize button.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        EMPHASIZE = 1
    }
    /**
     * Enumeration of media resource type.
     *
     * @enum { number }
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    enum EntityType {
        /**
         * Unknown type.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        UNKNOWN = 0,
        /**
         * Single song type.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        SINGLE = 1,
        /**
         * Singer type.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        SINGER = 2,
        /**
         * Album type.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        ALBUM = 3,
        /**
         * Ranking type.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        RANKING = 4,
        /**
         * Banner type.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        BANNER = 5,
        /**
         * Radio station type.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        RADIO_STATION = 6
    }
    /**
     * Enumeration of play state.
     *
     * @enum { number }
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    enum PlaybackState {
        /**
         * Preparing state. Indicates that the media file is not ready to play,
         * the media is loading or buffering
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        PLAYBACK_STATE_PREPARE = 0,
        /**
         * Playing state.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        PLAYBACK_STATE_PLAY = 1,
        /**
         * Paused state.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        PLAYBACK_STATE_PAUSE = 2,
        /**
         * Stopped state.
         * The server will clear the media playback position and other information.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        PLAYBACK_STATE_STOP = 3,
        /**
         * Completed state.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        PLAYBACK_STATE_COMPLETED = 4,
        /**
         * error state.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        PLAYBACK_STATE_ERROR = 5,
        /**
         * Buffering state.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        PLAYBACK_STATE_BUFFERING = 6
    }
    /**
     * Enumeration of MemberPurchaseType.
     *
     * @enum { string }
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    enum MemberPurchaseType {
        /**
         * normal.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        NORMAL = 'normal',
        /**
         * banner.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        BANNER = 'banner'
    }
    /**
     * Enumeration of AVMusicTemplate type.
     *
     * @enum { string }
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    enum AVMusicTemplateType {
        /**
         * Smart_car.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        DEFAULT = 'smartCar'
    }
    /**
     * Enumeration of SearchPlayInfoType.
     *
     * @enum { string }
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    enum SearchPlayInfoType {
        /**
         * playMusic.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        PLAY_MUSIC = 'playMusic',
        /**
         * playVideo.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        PLAY_VIDEO = 'playVideo'
    }
    /**
     * Enumeration of Sort type.
     *
     * @enum { number }
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    enum Sort {
        /**
         * NONE.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        NONE = 0,
        /**
         * ORDER.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        ORDER = 1,
        /**
         * REVERSE_ORDER.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        REVERSE_ORDER = 2
    }
    /**
     * Enumeration ErrorCode types, returns in BusinessError.code.
     *
     * @enum { number }
     * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
     * @stagemodelonly
     * @since 23
     */
    enum AVMusicTemplateErrorCode {
        /**
         * Failed to create the AVMusicTemplate.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        ERR_CODE_CREATE_AV_MUSIC_TEMPLATE_FAILED = 35000001,
        /**
         * Failed to create the AVMusicTemplate controller.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        ERR_CODE_CREATE_AV_MUSIC_TEMPLATE_CONTROLLER_FAILED = 35000002,
        /**
         * Template listener not registered.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        ERR_CODE_TEMPLATE_LISTENER_NO_EXIT = 35000003,
        /**
         * Controller callback not registered.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        ERR_CODE_CONTROLLER_CALLBACK_NO_EXIT = 35000004,
        /**
         * AVMusicTemplate does not exist.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        ERR_CODE_AV_MUSIC_TEMPLATE_NOT_EXIST = 35000005,
        /**
         * AVMusicTemplateController does not exist.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        ERR_CODE_CONTROLLER_NOT_EXIST = 35000006,
        /**
         * AVMusicTemplateController already exists.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        ERR_CODE_CONTROLLER_IS_EXIST = 35000007,
        /**
         * AVMusicTemplate Manager services do not exist.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        ERR_CODE_SERVICE_NOT_EXIST = 35000008,
        /**
         * AVMusicTemplate Manager services exception.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        ERR_CODE_SERVICE_EXCEPTION = 35000009,
        /**
         * The data exceeds the maximum allowable transmission capacity.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        ERR_CODE_EXCEED_MAX_DATA_SIZE = 35000010,
        /**
         * The data write error, data is invalid.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        ERR_CODE_WRITE_RESULT_EXCEPTION = 35000011,
        /**
         * AVMusicTemplate error.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVMusicTemplate
         * @stagemodelonly
         * @since 23
         */
        ERR_CODE_AV_MUSIC_TEMPLATE_ERROR = 35000012
    }
}
export default avMusicTemplate;

```
