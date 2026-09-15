# @ohos.bundle.skillManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2026 Huawei Device Co., Ltd.
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
 * @kit AbilityKit
 */
import { SkillInfo as _SkillInfo, SkillType as _SkillType } from './bundleManager/SkillInfo';
/**
 * This module provides skill query capabilities for applications.
 *
 * @namespace skillManager
 * @syscap SystemCapability.BundleManager.BundleFramework.Core
 * @stagemodelonly
 * @atomicservice
 * @since 26.0.0
 */
declare namespace skillManager {
    /**
     * Enumeration of flags used to control what content is populated in a SkillInfo.
     * Multiple flags can be combined using bitwise OR, for example GET_SKILL_INFO_WITH_SRC_ENTRIES | GET_SKILL_INFO_WITH_DESCRIPTION.
     *
     * @enum { number }
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export enum SkillInfoFlag {
        /**
         * Used to obtain the default SkillInfo.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        GET_SKILL_INFO_DEFAULT = 0x00000000,
        /**
         * Used to obtain the SkillInfo containing description.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        GET_SKILL_INFO_WITH_DESCRIPTION = 0x00000001,
        /**
         * Used to obtain the SkillInfo containing srcEntries.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        GET_SKILL_INFO_WITH_SRC_ENTRIES = 0x00000002,
        /**
         * Used to obtain the SkillInfo containing permissions.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        GET_SKILL_INFO_WITH_PERMISSIONS = 0x00000004,
        /**
         * Used to obtain the permissions declared under requestPermissions in the module manifest.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        GET_SKILL_INFO_WITH_REQUEST_PERMISSIONS = 0x00000008
    }
    /**
     * Obtains SkillInfo of the calling application based on moduleName and skillName.
     *
     * @param { string } moduleName - Indicates the module name of the skill.
     * @param { string } skillName - Indicates the name of the skill.
     * @param { number } flags {@link SkillInfoFlag} - Indicates the flag used to specify information
     *     contained in the SkillInfo object that will be returned.
     * @returns { Promise<SkillInfo> } Returns the SkillInfo object of the specified skill.
     * @throws { BusinessError } 17700002 - The specified module is not found.
     * @throws { BusinessError } 17700093 - The specified skillName is not found.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    function getSkillInfoForSelf(moduleName: string, skillName: string, flags: number): Promise<SkillInfo>;
    /**
     * Obtains all SkillInfo objects of the calling application.
     *
     * @param { number } flags {@link SkillInfoFlag} - Indicates the flag used to specify information
     *     contained in the SkillInfo objects that will be returned.
     * @returns { Promise<Array<SkillInfo>> } Returns the list of SkillInfo objects.
     * @throws { BusinessError } 17700101 - Bundle manager service is exception. Possible causes:
     *     1. Failed to connect to the system service.
     *     2. IPC data transmission failed.
     *     3. Failed to obtain the object constructor.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    function getSkillInfosForSelf(flags: number): Promise<Array<SkillInfo>>;
    /**
     * Obtains SkillInfo of a specified application based on bundleName, moduleName and skillName.
     * To query information for other local accounts, the permission
     * ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS must additionally be granted.
     *
     * @permission ohos.permission.MANAGE_SKILL_PRIVILEGE or ohos.permission.MANAGE_SKILL
     * @param { string } bundleName - Indicates the bundle name of the application.
     * @param { string } moduleName - Indicates the module name of the skill.
     * @param { string } skillName - Indicates the name of the skill.
     * @param { number } flags {@link SkillInfoFlag} - Indicates the flag used to specify information
     *     contained in the SkillInfo object that will be returned.
     * @param { number } [userId] - Indicates the user ID. If not provided, the user ID of the caller is used.
     * @returns { Promise<SkillInfo> } Returns the SkillInfo object of the specified skill.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 17700001 - The specified bundleName is not found.
     * @throws { BusinessError } 17700002 - The specified module is not found.
     * @throws { BusinessError } 17700004 - The specified user ID is not found.
     * @throws { BusinessError } 17700093 - The specified skillName is not found.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    function getSkillInfo(bundleName: string, moduleName: string, skillName: string, flags: number, userId?: number): Promise<SkillInfo>;
    /**
     * Obtains all SkillInfo of a specified application based on bundleName.
     * To query information for other local accounts, the permission
     * ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS must additionally be granted.
     *
     * @permission ohos.permission.MANAGE_SKILL_PRIVILEGE or ohos.permission.MANAGE_SKILL
     * @param { string } bundleName - Indicates the bundle name of the application.
     * @param { number } flags {@link SkillInfoFlag} - Indicates the flag used to specify information
     *     contained in the SkillInfo objects that will be returned.
     * @param { number } [userId] - Indicates the user ID. If not provided, the user ID of the caller is used.
     * @returns { Promise<Array<SkillInfo>> } Returns the list of SkillInfo objects.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 17700001 - The specified bundleName is not found.
     * @throws { BusinessError } 17700004 - The specified user ID is not found.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    function getSkillInfos(bundleName: string, flags: number, userId?: number): Promise<Array<SkillInfo>>;
    /**
     * Obtains all SkillInfo objects installed on the device.
     * To query information for other local accounts, the permission
     * ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS must additionally be granted.
     *
     * @permission ohos.permission.MANAGE_SKILL_PRIVILEGE or ohos.permission.MANAGE_SKILL
     * @param { number } flags {@link SkillInfoFlag} - Indicates the flag used to specify information
     *     contained in the SkillInfo objects that will be returned.
     * @param { number } [userId] - Indicates the user ID. If not provided, the user ID of the caller is used.
     * @returns { Promise<Array<SkillInfo>> } Returns the list of SkillInfo objects.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 17700004 - The specified user ID is not found.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    function getAllSkillInfos(flags: number, userId?: number): Promise<Array<SkillInfo>>;
    /**
     * Provides information about a skill, including skill name, type, and associated metadata.
     *
     * @typedef { _SkillInfo }
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export type SkillInfo = _SkillInfo;
    /**
     * Enumerates the skill types.
     *
     * @typedef { _SkillType }
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export type SkillType = _SkillType;
}
export default skillManager;

```
