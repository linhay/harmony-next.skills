# @ohos.app.ability.appMemoryOptimizer.d.ts

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
/**
 * appMemoryOptimizer provides application memory optimization capabilities, including performing file page cache
 * eviction on specified files, performing file page cache eviction on specified modules.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @since 26.0.0
 */
declare namespace appMemoryOptimizer {
    /**
     * Sends a request to the system to release file page cache of specified files. The system determines
     * whether to actually perform the release based on the current memory status, and success is not guaranteed.
     *
     * @param { Array<string> } fileNames - Array of file names for which file page cache needs to be released.
     *     File names must end with .so, .hap, or .hsp.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 16000163 - File type error. File name does not end with .so, .hap, or .hsp.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    function evictFilePages(fileNames: Array<string>): Promise<void>;
    /**
     * Sends a request to the system to release file page cache of specified modules. The system determines
     * whether to actually perform the release based on the current memory status, and success is not guaranteed.
     * The system reads the memory_optimizer.json configuration file of the corresponding module, obtains the
     * evictFilePages array, and performs file page cache eviction on the files in the array.
     *
     * Configuration file path: {Module directory}/src/main/resources/rawfile/memory_optimizer.json
     * File names in the evictFilePages array of the configuration file must end with .so, .hap, or .hsp.
     *
     * @param { Array<string> } moduleNames - Array of module names for which file page cache needs to be released.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 16000163 - File type error. File names in the evictFilePages array of the configuration
     *     file do not end with .so, .hap, or .hsp.
     * @throws { BusinessError } 16000164 - Failed to parse configuration file.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    function evictModuleFilePages(moduleNames: Array<string>): Promise<void>;
}
export default appMemoryOptimizer;

```
