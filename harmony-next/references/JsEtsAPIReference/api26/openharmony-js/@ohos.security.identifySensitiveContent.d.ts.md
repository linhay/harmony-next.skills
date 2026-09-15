# @ohos.security.identifySensitiveContent.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
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
 * @file Identify sensitive file
 * @kit DataProtectionKit
 */
/**
 * This module identifies sensitive information in a specified file based on the input [Policy]{@link identifySensitiveContent.policy}.
 * The system matches the file content against the provided [Policy]{@link identifySensitiveContent.policy} (including sensitive labels,
 * keyword sets, and regular expressions) and returns the matched sensitive content.
 *
 * @syscap SystemCapability.Security.DataLossPrevention
 * @since 21
 */
declare namespace identifySensitiveContent {
    /**
     * Defines the policy for sensitive content identification.
     * In a single policy, keywords and regular expressions are combined in sequence, and two-level matching is performed. First, keyword matching is performed.
     * If a keyword is matched, regular expression matching is performed within a scope of 100 bytes: from the position 50 bytes before the matched position of
     * the keyword to that 50 bytes after the matched position.
     * Multiple policies are independent of each other, and each policy is applied separately during scanning.
     * sensitiveLabel is used to mark the matching result to identify the specific policy matched.
     *
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 21
     */
    export interface Policy {
        /**
         * Label of an identification policy, which is used to identify and classify matching results. The value is a string of 1 to 30 bytes.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        sensitiveLabel: string;
        /**
         * Keyword set, which is used to match sensitive keywords in a file.
         * The system searches for these keywords in the file content and returns the identification result if a keyword is matched.
         * The keywords are case-sensitive.
         * The array can contain a maximum of 50 elements, and each element can contain a maximum of 30 bytes.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        keywords: Array<string>;
        /**
         * Regular expression used to match sensitive content.
         * The system performs pattern matching on the file content based on the regular expression.
         * The matched content is returned. The value contains 0 to 512 characters.
         * When entering a string, check whether some special characters (such as backslash (), double quotation marks ("),
         * and newline characters) are automatically escaped to ensure the input effect of the string.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        regex: string;
    }
    /**
     * Displays the identification result of sensitive content.
     *
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 21
     */
    export interface MatchResult {
        /**
         * Label of an identification policy,
         * which corresponds to sensitiveLabel in the input policy and is used to label the policy used to identify the matching result.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        readonly sensitiveLabel: string;
        /**
         * Matched sensitive content segment, that is, the text content matched by keyword or regular expression.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        readonly matchContent: string;
        /**
         * Total number of matched items.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        readonly matchNumber: number;
    }
    /**
     * Identifies sensitive content in a specified file based on the configured policy and returns the identified result array,
     * including the matched sensitivity labels, matched content, and number of matched items. This API uses a promise to return the result.
     *
     * @permission ohos.permission.ENTERPRISE_DATA_IDENTIFY_FILE
     * @param { string } filePath - File path identified. The path must be a physical path. The file to which the path points must exist and can be accessed.
     * @param { Array<Policy> } identifyPolicies - An array of policies used to identify sensitive content.
     * Each policy defines an identification rule (tags, keywords, and regular expressions).
     * The system scans file content based on these rules and returns the matching result.
     * @returns { Promise<Array<MatchResult>> } Promise used to return the identification result of sensitive content.
     * If the operation is successful, the matching result array is returned. If the operation fails, an error code is returned.
     * @throws { BusinessError } 201 - permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 19110001 - Parameter error. Possible causes:
     *     1. Incorrect policy format.
     *     2. Invalid parameter range.
     * @throws { BusinessError } 19110002 - Sensitive file content identification timed out.
     * @throws { BusinessError } 19110003 - The file is not supported. Possible causes:
     *     1. The file path does not exist.
     *     2. The file type is not supported.
     *     3. The file permission is not supported.
     * @throws { BusinessError } 19110004 - A system error has occurred.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 21
     */
    function scanFile(filePath: string, identifyPolicies: Array<Policy>): Promise<Array<MatchResult>>;
}
export default identifySensitiveContent;

```
