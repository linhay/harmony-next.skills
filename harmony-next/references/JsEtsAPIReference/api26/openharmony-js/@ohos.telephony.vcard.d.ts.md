# @ohos.telephony.vcard.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2023-2024 Huawei Device Co., Ltd.
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
 * @kit TelephonyKit
 */
import type { AsyncCallback } from './@ohos.base';
import type dataSharePredicates from './@ohos.data.dataSharePredicates';
import type Context from './application/BaseContext';
/**
 * Provides applications with APIs for obtaining vcard.
 *
 * @namespace vcard
 * @syscap SystemCapability.Telephony.CoreService
 * @since 11
 */
declare namespace vcard {
    /**
     * Import contacts from the specified vcf file.
     *
     * @permission ohos.permission.WRITE_CONTACTS and
     *      ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or
     *     capability.
     * @param { string } filePath - Vcf file path.
     * @param { number } accountId - Contact account ID. When the app chooses to
     *      import the vcf file into a contact account,
     *     it needs to pass in the accountId. If the accountId is not passed, a new
     *      contact account will be added by default.
     * @param { AsyncCallback<void> } callback - The callback of the function.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.CoreService
     * @since 23
     */
    function importVCard(context: Context, filePath: string, accountId: number, callback: AsyncCallback<void>): void;
    /**
     * Import contacts from the specified vcf file.
     *
     * @permission ohos.permission.WRITE_CONTACTS and
     *      ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or
     *     capability.
     * @param { string } filePath - Vcf file path.
     * @param { number } accountId - Contact account ID.When the app chooses to
     *     import the vcf file into a contact account,
     *     it needs to pass in the accountId. If the accountId is not passed, a new
     *     contact account will be added by default.
     * @returns { Promise<void> } the promise returned by the function.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.CoreService
     * @since 23
     */
    function importVCard(context: Context, filePath: string, accountId?: number): Promise<void>;
    /**
     * Import contacts from the specified vcf file.
     *
     * @permission ohos.permission.WRITE_CONTACTS and
     *      ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or
     *     capability.
     * @param { string } filePath - Vcf file path.
     * @param { AsyncCallback<void> } callback - The callback of the function.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.CoreService
     * @since 23
     */
    function importVCard(context: Context, filePath: string, callback: AsyncCallback<void>): void;
    /**
     * Export contact data to a vcf file.
     *
     * @permission ohos.permission.WRITE_CONTACTS and ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { dataSharePredicates.DataSharePredicates } predicates - Execute statement.
     * @param { VCardBuilderOptions } options - Encoding and version.
     * @param { AsyncCallback<string> } callback - Represents the address of the generated vcf file.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.CoreService
     * @since 23
     */
    function exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, options: VCardBuilderOptions, callback: AsyncCallback<string>): void;
    /**
     * Export contact data to a vcf file.
     *
     * @permission ohos.permission.WRITE_CONTACTS and ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { dataSharePredicates.DataSharePredicates } predicates - Execute statement.
     * @param { VCardBuilderOptions } options - Encoding and version.
     * @returns { Promise<string> } the promise represents the address of the generated vcf file..
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.CoreService
     * @since 23
     */
    function exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, options?: VCardBuilderOptions): Promise<string>;
    /**
     * Export contact data to a vcf file.
     *
     * @permission ohos.permission.WRITE_CONTACTS and ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { dataSharePredicates.DataSharePredicates } predicates - Execute statement.
     * @param { AsyncCallback<string> } callback - Represents the address of the generated vcf file.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.CoreService
     * @since 23
     */
    function exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<string>): void;
    /**
     * Indicates the VCard types.
     *
     * @enum { string }
     * @syscap SystemCapability.Telephony.CoreService
     * @since 23
     */
    export enum VCardType {
        /**
         * Indicates the VCard version 2.1.
         *
         * @syscap SystemCapability.Telephony.CoreService
         * @since 23
         */
        VERSION_21 = 0,
        /**
         * Indicates the VCard version 3.0.
         *
         * @syscap SystemCapability.Telephony.CoreService
         * @since 23
         */
        VERSION_30 = 1,
        /**
         * Indicates the VCard version 4.0.
         *
         * @syscap SystemCapability.Telephony.CoreService
         * @since 23
         */
        VERSION_40 = 2
    }
    /**
     * Indicates the options for VCard export.
     *
     * @interface VCardBuilderOptions
     * @syscap SystemCapability.Telephony.CoreService
     * @since 23
     */
    export interface VCardBuilderOptions {
        /**
         * Indicates the VCard types.
         *
         * @type { ?VCardType }
         * @syscap SystemCapability.Telephony.CoreService
         * @since 23
         */
        cardType?: VCardType;
        /**
         * Indicates the Encoding format.
         *
         * @type { ?string }
         * @syscap SystemCapability.Telephony.CoreService
         * @since 23
         */
        charset?: string;
    }
}
export default vcard;

```
