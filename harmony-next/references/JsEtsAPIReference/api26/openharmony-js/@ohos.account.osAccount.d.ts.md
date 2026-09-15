# @ohos.account.osAccount.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2026 Huawei Device Co., Ltd.
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
 * @kit BasicServicesKit
 */
import type distributedAccount from './@ohos.account.distributedAccount';
import type { AsyncCallback } from './@ohos.base';
/**
 * The **osAccount** module provides basic capabilities for managing system (OS) accounts, including adding, deleting,
 * querying, setting, subscribing to, and enabling an OS account.
 *
 * @syscap SystemCapability.Account.OsAccount
 * @since 7
 */
declare namespace osAccount {
    /**
     * Obtains an **AccountManager** instance.
     *
     * @returns { AccountManager } **AccountManager** instance obtained.
     * @syscap SystemCapability.Account.OsAccount
     * @since 7
     */
    function getAccountManager(): AccountManager;
    /**
     * Checks whether this domain account is supported. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } Promise used to return the result. The value **true** means this domain account is
     *     supported; the value **false** means the opposite.
     * @throws { BusinessError } 12300001 - The system service works abnormally.
     * @syscap SystemCapability.Account.OsAccount
     * @stagemodelonly
     * @since 26.0.0
     */
    function isDomainAccountSupported(): Promise<boolean>;
    /**
     * Provides APIs for managing OS accounts.
     *
     * @syscap SystemCapability.Account.OsAccount
     * @since 7
     */
    interface AccountManager {
        /**
         * Checks whether multiple OS accounts are supported. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [checkMultiOsAccountEnabled]{@link osAccount.AccountManager.checkMultiOsAccountEnabled(callback: AsyncCallback<boolean>)}
         * >  instead.
         *
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result.
         *     The value **true** means multiple OS accounts are supported;
         *     the value **false** means the opposite.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.checkMultiOsAccountEnabled(callback: AsyncCallback<boolean>)
         */
        isMultiOsAccountEnable(callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether multiple OS accounts are supported. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [checkMultiOsAccountEnabled]{@link osAccount.AccountManager.checkMultiOsAccountEnabled()} instead.
         *
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means
         *     multiple OS accounts are supported; the value **false** means the opposite.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.checkMultiOsAccountEnabled()
         */
        isMultiOsAccountEnable(): Promise<boolean>;
        /**
         * Checks whether multiple OS accounts are supported. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value
         *     **true** means multiple OS accounts are supported;
         *     the value **false** means the opposite.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        checkMultiOsAccountEnabled(callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether multiple OS accounts are supported. This API uses a promise to return the result.
         *
         * @returns { Promise<boolean> } Promise used to return the result. The value
         *     **true** means multiple OS accounts are supported;
         *     the value **false** means the opposite.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        checkMultiOsAccountEnabled(): Promise<boolean>;
        /**
         * Checks whether an OS account is activated. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. The substitute API is available
         * > only to system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
         * @param { number } localId - ID of the target OS account.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value
         *     **true** means the account is activated; the value **false** means the opposite.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.checkOsAccountActivated(localId: number, callback: AsyncCallback<boolean>)
         */
        isOsAccountActived(localId: number, callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether an OS account is activated. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. The substitute API is available
         * > only to system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
         * @param { number } localId - ID of the target OS account.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means
         *     the account is activated; the value **false** means the opposite.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.checkOsAccountActivated(localId: number)
         */
        isOsAccountActived(localId: number): Promise<boolean>;
        /**
         * Checks whether an OS account is activated. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. The substitute API is available
         * > only to system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
         * @param { number } localId - ID of the target OS account.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true**
         *     means the account is activated; the value **false** means the opposite.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300002 - Invalid localId.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         * @deprecated since 11
         */
        checkOsAccountActivated(localId: number, callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether an OS account is activated. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. The substitute API is available
         * > only to system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
         * @param { number } localId - ID of the target OS account.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means
         *     the account is activated; the value **false** means the opposite.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300002 - Invalid localId.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         * @deprecated since 11
         */
        checkOsAccountActivated(localId: number): Promise<boolean>;
        /**
         * Checks whether the specified constraint is enabled for an OS account. This API uses an asynchronous callback
         * to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. The substitute API is available
         * > only to system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @param { number } localId - ID of the target OS account.
         * @param { string } constraint -
         *     [Constraint](docroot://reference/apis-basic-services-kit/js-apis-osAccount.md#constraints) to check.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true**
         *     means the specified constraint is enabled; the value **false** means the opposite.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.checkOsAccountConstraintEnabled(localId: number, constraint: string, callback: AsyncCallback<boolean>)
         */
        isOsAccountConstraintEnable(localId: number, constraint: string, callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether the specified constraint is enabled for an OS account. This API uses a promise to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. The substitute API is available
         * > only to system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @param { number } localId - ID of the target OS account.
         * @param { string } constraint -
         *     [Constraint](docroot://reference/apis-basic-services-kit/js-apis-osAccount.md#constraints) to check.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means
         *     the specified constraint is enabled; the value **false** means the opposite.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.checkOsAccountConstraintEnabled(localId: number, constraint: string)
         */
        isOsAccountConstraintEnable(localId: number, constraint: string): Promise<boolean>;
        /**
         * Checks whether the specified constraint is enabled for an OS account. This API uses an asynchronous callback
         * to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. The substitute API is available
         * > only to system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
         * @param { number } localId - ID of the target OS account.
         * @param { string } constraint -
         *     [Constraint](docroot://reference/apis-basic-services-kit/js-apis-osAccount.md#constraints) to check.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value
         *     **true** means the specified constraint is enabled; the value **false** means the opposite.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300002 - Invalid localId or constraint.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         * @deprecated since 11
         */
        checkOsAccountConstraintEnabled(localId: number, constraint: string, callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether the specified constraint is enabled for an OS account. This API uses a promise to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. The substitute API is available
         * > only to system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
         * @param { number } localId - ID of the target OS account.
         * @param { string } constraint -
         *     [Constraint](docroot://reference/apis-basic-services-kit/js-apis-osAccount.md#constraints) to check.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means
         *     the specified constraint is enabled; the value **false** means the opposite.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300002 - Invalid localId or constraint.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         * @deprecated since 11
         */
        checkOsAccountConstraintEnabled(localId: number, constraint: string): Promise<boolean>;
        /**
         * Checks whether a constraint is enabled for this OS account. This API uses a promise to return the result.
         *
         * @param { string } constraint -
         *     [Constraint](docroot://reference/apis-basic-services-kit/js-apis-osAccount.md#constraints) to check.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means
         *     the specified constraint is enabled; the value **false** means the opposite.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 11
         */
        isOsAccountConstraintEnabled(constraint: string): Promise<boolean>;
        /**
         * Checks whether this OS account is a test account. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [checkOsAccountTestable]{@link osAccount.AccountManager.checkOsAccountTestable(callback: AsyncCallback<boolean>)}
         * >  instead.
         *
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value
         *     **true** means the account is a test account; the value **false** means the opposite.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.checkOsAccountTestable(callback: AsyncCallback<boolean>)
         */
        isTestOsAccount(callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether this OS account is a test account. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [checkOsAccountTestable]{@link osAccount.AccountManager.checkOsAccountTestable()} instead.
         *
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means
         *     the account is a test account; the value **false** means the opposite.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.checkOsAccountTestable()
         */
        isTestOsAccount(): Promise<boolean>;
        /**
         * Checks whether this OS account is a test account. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value
         *     **true** means the account is a test account; the value **false** means the opposite;
         *     the default value is **false**.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        checkOsAccountTestable(callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether this OS account is a test account. This API uses a promise to return the result.
         *
         * @returns { Promise<boolean> } Promise used to return the result. The value **true**
         *     means the account is a test account; the value **false** means the opposite;
         *     the default value is **false**.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        checkOsAccountTestable(): Promise<boolean>;
        /**
         * Checks whether an OS account has been verified. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [checkOsAccountVerified]{@link osAccount.AccountManager.checkOsAccountVerified(callback: AsyncCallback<boolean>)}
         * >  instead.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value
         *     **true** means the OS account has been verified; the value **false** means the opposite.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.checkOsAccountVerified(callback: AsyncCallback<boolean>)
         */
        isOsAccountVerified(callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether an OS account has been verified. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. The substitute API is available
         * > only to system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
         * @param { number } localId - ID of the target OS account.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value
         *     **true** means the OS account has been verified; the value **false** means the opposite.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.checkOsAccountVerified(localId: number, callback: AsyncCallback<boolean>)
         */
        isOsAccountVerified(localId: number, callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether an OS account has been verified. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. The substitute API is available
         * > only to system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
         * @param { number } localId - ID of the target OS account. If this parameter is not specified,
         *     this API checks whether the current OS account has been verified. The default value is **-1**.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means the
         *     OS account has been verified; the value **false** means the opposite.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.checkOsAccountVerified(localId: number)
         */
        isOsAccountVerified(localId?: number): Promise<boolean>;
        /**
         * Checks whether this OS account is unlocked. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. You are advised to use
         * > [isOsAccountUnlocked]{@link osAccount.AccountManager.isOsAccountUnlocked()} instead.
         *
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true**
         *     means the OS account has been verified; the value **false** means the opposite.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         * @deprecated since 11
         * @useinstead osAccount.AccountManager.isOsAccountUnlocked()
         */
        checkOsAccountVerified(callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether this OS account has been verified. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. You are advised to use
         * > [isOsAccountUnlocked]{@link osAccount.AccountManager.isOsAccountUnlocked()} instead.
         *
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means the
         *     OS account has been verified; the value **false** means the opposite.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         * @deprecated since 11
         * @useinstead osAccount.AccountManager.isOsAccountUnlocked()
         */
        checkOsAccountVerified(): Promise<boolean>;
        /**
         * Checks whether an OS account has been verified. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. The substitute API is available
         * > only to system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
         * @param { number } localId - ID of the target OS account.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true**
         *     means the OS account has been verified; the value **false** means the opposite.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300002 - Invalid localId.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         * @deprecated since 11
         */
        checkOsAccountVerified(localId: number, callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether an OS account has been verified. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. The substitute API is available
         * > only to system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
         * @param { number } localId - ID of the target OS account. If this parameter is not specified,
         *     this API checks whether the current OS account has been verified.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means the
         *     OS account has been verified; the value **false** means the opposite.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300002 - Invalid localId.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         * @deprecated since 11
         */
        checkOsAccountVerified(localId: number): Promise<boolean>;
        /**
         * Checks whether this OS account is unlocked. This API uses a promise to return the result.
         *
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means
         *     the OS account has been verified; the value **false** means the opposite.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 11
         */
        isOsAccountUnlocked(): Promise<boolean>;
        /**
         * Obtains the name of the OS account of the caller. This API uses a promise to return the result.
         *
         * @returns { Promise<string> } Promise used to return the OS account name obtained.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 12
         */
        getOsAccountName(): Promise<string>;
        /**
         * Obtains the name of an OS account based on its local ID. This API uses a promise to return the result.
         *
         * @permission ohos.permission.GET_LOCAL_ACCOUNT_IDENTIFIERS
         * @param { number } localId - Local ID of the target OS account.
         * @returns { Promise<string> } Promise used to return the name of the target OS account.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300008 - Restricted Account.
         * @syscap SystemCapability.Account.OsAccount
         * @stagemodelonly
         * @since 26.0.0
         */
        getOsAccountNameByLocalId(localId: number): Promise<string>;
        /**
         * Obtains the number of OS accounts created. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [getOsAccountCount]{@link osAccount.AccountManager.getOsAccountCount(callback: AsyncCallback<number>)} instead.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **null** and **data** is the number of created OS accounts.
         *     If the operation fails, **err** is an error object.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.getOsAccountCount(callback: AsyncCallback<int>)
         */
        getCreatedOsAccountsCount(callback: AsyncCallback<number>): void;
        /**
         * Obtains the number of OS accounts created. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [getOsAccountCount]{@link osAccount.AccountManager.getOsAccountCount()} instead.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @returns { Promise<number> } Promise used to return the number of created OS accounts.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.getOsAccountCount()
         */
        getCreatedOsAccountsCount(): Promise<number>;
        /**
         * Obtains the number of OS accounts created. This API uses an asynchronous callback to return the result.
         * This API can be called only by system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **null** and **data** is the number of created OS accounts.
         *     If the operation fails, **err** is an error object.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        getOsAccountCount(callback: AsyncCallback<number>): void;
        /**
         * Obtains the number of OS accounts created. This API uses a promise to return the result.
         * This API can be called only by system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @returns { Promise<number> } Promise used to return the number of created OS accounts.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        getOsAccountCount(): Promise<number>;
        /**
         * Obtains the ID of the OS account to which the current process belongs. This API uses an asynchronous callback
         *  to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [getOsAccountLocalId]{@link osAccount.AccountManager.getOsAccountLocalId(callback: AsyncCallback<number>)}
         * > instead.
         *
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **null** and **data** is the OS account ID obtained.
         *     Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.getOsAccountLocalId(callback: AsyncCallback<int>)
         */
        getOsAccountLocalIdFromProcess(callback: AsyncCallback<number>): void;
        /**
         * Obtains the ID of the OS account to which the current process belongs. This API uses a promise to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [getOsAccountLocalId]{@link osAccount.AccountManager.getOsAccountLocalId()} instead.
         *
         * @returns { Promise<number> } Promise used to return the OS account ID obtained.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.getOsAccountLocalId()
         */
        getOsAccountLocalIdFromProcess(): Promise<number>;
        /**
         * Obtains the ID of the OS account to which the current process belongs. This API uses an asynchronous callback
         *  to return the result.
         *
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **null** and **data** is the OS account ID obtained.
         *     Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        getOsAccountLocalId(callback: AsyncCallback<number>): void;
        /**
         * Obtains the ID of the OS account to which the current process belongs. This API uses a promise to return the
         * result.
         *
         * @returns { Promise<number> } Promise used to return the OS account ID obtained.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        getOsAccountLocalId(): Promise<number>;
        /**
         * Obtains the local IDs of all non-system-level OS accounts. Non-system-level OS accounts are visible to
         * users and are usually used for operations such as login. This API uses a promise to return the result.
         *
         * @permission ohos.permission.GET_LOCAL_ACCOUNT_IDENTIFIERS
         * @returns { Promise<number[]> } Promise used to return the local IDs of all non-system-level OS accounts.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @stagemodelonly
         * @since 26.0.0
         */
        getOsAccountLocalIds(): Promise<number[]>;
        /**
         * Obtains the OS account ID based on the process UID. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [getOsAccountLocalIdForUid]{@link osAccount.AccountManager.getOsAccountLocalIdForUid(uid: number, callback: AsyncCallback<number>)}
         * >  instead.
         *
         * @param { number } uid - Process UID.
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **null** and **data** is the OS account ID obtained.
         *     Otherwise, **data** is an error object.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.getOsAccountLocalIdForUid(uid: int, callback: AsyncCallback<int>)
         */
        getOsAccountLocalIdFromUid(uid: number, callback: AsyncCallback<number>): void;
        /**
         * Obtains the OS account ID based on the process UID. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [getOsAccountLocalIdForUid]{@link osAccount.AccountManager.getOsAccountLocalIdForUid(uid: number)} instead.
         *
         * @param { number } uid - Process UID.
         * @returns { Promise<number> } Promise used to return the OS account ID obtained.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.getOsAccountLocalIdForUid(uid: int)
         */
        getOsAccountLocalIdFromUid(uid: number): Promise<number>;
        /**
         * Obtains the OS account ID based on the process UID. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { number } uid - Process UID.
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **null** and **data** is the OS account ID obtained.
         *     Otherwise, **data** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300002 - Invalid uid.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        getOsAccountLocalIdForUid(uid: number, callback: AsyncCallback<number>): void;
        /**
         * Obtains the OS account ID based on the process UID. This API uses a promise to return the result.
         *
         * @param { number } uid - Process UID.
         * @returns { Promise<number> } Promise used to return the OS account ID obtained.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300002 - Invalid uid.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        getOsAccountLocalIdForUid(uid: number): Promise<number>;
        /**
         * Obtains the OS account ID based on the process UID. The API returns the result synchronously.
         *
         * @param { number } uid - Process UID.
         * @returns { number } OS account ID obtained.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300002 - Invalid uid.
         * @syscap SystemCapability.Account.OsAccount
         * @since 10
         */
        getOsAccountLocalIdForUidSync(uid: number): number;
        /**
         * Obtains the OS account ID based on the domain account information. This API uses an asynchronous callback to
         * return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [getOsAccountLocalIdForDomain]{@link osAccount.AccountManager.getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<number>)}
         * >  instead.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @param { DomainAccountInfo } domainInfo - Domain account information.
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **null** and **data** is the OS account ID obtained.
         *     Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.OsAccount
         * @since 8
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<int>)
         */
        getOsAccountLocalIdFromDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<number>): void;
        /**
         * Obtains the OS account ID based on the domain account information. This API uses a promise to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [getOsAccountLocalIdForDomain]{@link osAccount.AccountManager.getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo)}
         * >  instead.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @param { DomainAccountInfo } domainInfo - Domain account information.
         * @returns { Promise<number> } Promise used to return the ID of the OS account associated
         *     with the domain account.
         * @syscap SystemCapability.Account.OsAccount
         * @since 8
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo)
         */
        getOsAccountLocalIdFromDomain(domainInfo: DomainAccountInfo): Promise<number>;
        /**
         * Obtains the OS account ID based on the domain account information. This API uses an asynchronous callback to
         * return the result.
         * This API can be called only by system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @param { DomainAccountInfo } domainInfo - Domain account information.
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **null** and **data** is the ID of the OS account associated with
         *     the domain account. Otherwise, **err** is an error object.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300002 - Invalid domainInfo.
         * @throws { BusinessError } 12300003 - Domain account not found.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<number>): void;
        /**
         * Obtains the OS account ID based on the domain account information. This API uses a promise to return the
         * result.
         * This API can be called only by system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @param { DomainAccountInfo } domainInfo - Domain account information.
         * @returns { Promise<number> } Promise used to return the ID of the OS account associated with the domain account.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300002 - Invalid domainInfo.
         * @throws { BusinessError } 12300003 - Domain account not found.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo): Promise<number>;
        /**
         * Obtains all constraints enabled for an OS account. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. The substitute API is available
         * > only to system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @param { number } localId - ID of the target OS account.
         * @param { AsyncCallback<Array<string>> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **null** and **data** is a list of all
         *     [constraints](docroot://reference/apis-basic-services-kit/js-apis-osAccount.md#constraints) enabled
         *     for the OS account. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.getOsAccountConstraints(localId: number, callback: AsyncCallback<Array<string>>)
         */
        getOsAccountAllConstraints(localId: number, callback: AsyncCallback<Array<string>>): void;
        /**
         * Obtains all constraints enabled for an OS account. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. The substitute API is available
         * > only to system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @param { number } localId - ID of the target OS account.
         * @returns { Promise<Array<string>> } Promise used to return all the
         *     [constraints](docroot://reference/apis-basic-services-kit/js-apis-osAccount.md#constraints) enabled
         *     for the OS account.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.getOsAccountConstraints(localId: number)
         */
        getOsAccountAllConstraints(localId: number): Promise<Array<string>>;
        /**
         * Obtains all constraints enabled for an OS account. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. The substitute API is available
         * > only to system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @param { number } localId - ID of the target OS account.
         * @param { AsyncCallback<Array<string>> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is all
         *     [constraints](docroot://reference/apis-basic-services-kit/js-apis-osAccount.md#constraints) obtained.
         *     Otherwise, **err** is an error object.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300002 - Invalid localId.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         * @deprecated since 11
         */
        getOsAccountConstraints(localId: number, callback: AsyncCallback<Array<string>>): void;
        /**
         * Obtains all constraints enabled for an OS account. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. The substitute API is available
         * > only to system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @param { number } localId - ID of the target OS account.
         * @returns { Promise<Array<string>> } Promise used to return all the
         *     [constraints](docroot://reference/apis-basic-services-kit/js-apis-osAccount.md#constraints) enabled
         *     for the OS account.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300002 - Invalid localId.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         * @deprecated since 11
         */
        getOsAccountConstraints(localId: number): Promise<Array<string>>;
        /**
         * Obtains information about all activated OS accounts. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [getActivatedOsAccountLocalIds]{@link osAccount.AccountManager.getActivatedOsAccountLocalIds(callback: AsyncCallback<Array<number>>)}
         * >  instead.
         *
         * @param { AsyncCallback<Array<number>> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is a list of activated OS accounts.
         *     Otherwise, **data** is an error object.
         * @syscap SystemCapability.Account.OsAccount
         * @since 8
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.getActivatedOsAccountLocalIds(callback: AsyncCallback<Array<int>>)
         */
        queryActivatedOsAccountIds(callback: AsyncCallback<Array<number>>): void;
        /**
         * Obtains information about all activated OS accounts. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [getActivatedOsAccountLocalIds]{@link osAccount.AccountManager.getActivatedOsAccountLocalIds()} instead.
         *
         * @returns { Promise<Array<number>> } Promise used to return the information about all activated OS accounts.
         * @syscap SystemCapability.Account.OsAccount
         * @since 8
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.getActivatedOsAccountLocalIds()
         */
        queryActivatedOsAccountIds(): Promise<Array<number>>;
        /**
         * Obtains information about all activated OS accounts. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { AsyncCallback<Array<number>> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is a list of activated OS accounts.
         *     Otherwise, **data** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        getActivatedOsAccountLocalIds(callback: AsyncCallback<Array<number>>): void;
        /**
         * Obtains information about all activated OS accounts. This API uses a promise to return the result.
         *
         * @returns { Promise<Array<number>> } Promise used to return the information about all activated OS accounts.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        getActivatedOsAccountLocalIds(): Promise<Array<number>>;
        /**
         * Obtains the ID of the foreground OS account. This API uses a promise to return the result.
         *
         * @returns { Promise<number> } Promise used to return the ID of the foreground OS account.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 15
         */
        getForegroundOsAccountLocalId(): Promise<number>;
        /**
         * Obtains information about the OS account to which the current process belongs. This API uses an asynchronous
         * callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. The substitute API is available
         * > only to system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @param { AsyncCallback<OsAccountInfo> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is the OS account information obtained.
         *     Otherwise, **data** is an error object.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.getCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>)
         */
        queryCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void;
        /**
         * Obtains information about the OS account to which the current process belongs. This API uses a promise to
         * return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. The substitute API is available
         * > only to system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @returns { Promise<OsAccountInfo> } Promise used to return the OS account information obtained.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.getCurrentOsAccount()
         */
        queryCurrentOsAccount(): Promise<OsAccountInfo>;
        /**
         * Obtains information about the OS account to which the current process belongs. This API uses an asynchronous
         * callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. The substitute API is available
         * > only to system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS [since 9 - 9]
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.GET_LOCAL_ACCOUNTS [since 10]
         * @param { AsyncCallback<OsAccountInfo> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is the OS account information obtained.
         *     Otherwise, **data** is an error object.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         * @deprecated since 11
         */
        getCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void;
        /**
         * Obtains information about the OS account to which the current process belongs. This API uses a promise to
         * return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. The substitute API is available
         * > only to system applications.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS [since 9 - 9]
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.GET_LOCAL_ACCOUNTS [since 10]
         * @returns { Promise<OsAccountInfo> } Promise used to return the OS account information obtained.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         * @deprecated since 11
         */
        getCurrentOsAccount(): Promise<OsAccountInfo>;
        /**
         * Obtains the domain account information associated with a specified OS account. This API uses a promise to
         * return the result.
         *
         * @permission ohos.permission.GET_DOMAIN_ACCOUNTS and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
         * @param { number } localId - ID of the target OS account.
         * @returns { Promise<DomainAccountInfo> } Promise used to return the domain account information obtained.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300003 - OS account not found.
         * @syscap SystemCapability.Account.OsAccount
         * @since 15
         */
        getOsAccountDomainInfo(localId: number): Promise<DomainAccountInfo>;
        /**
         * Obtains the type of the account to which the current process belongs. This API uses an asynchronous callback to
         * return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [getOsAccountType]{@link osAccount.AccountManager.getOsAccountType(callback: AsyncCallback<OsAccountType>)}
         * > instead.
         *
         * @param { AsyncCallback<OsAccountType> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is the OS account type obtained.
         *     Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.getOsAccountType(callback: AsyncCallback<OsAccountType>)
         */
        getOsAccountTypeFromProcess(callback: AsyncCallback<OsAccountType>): void;
        /**
         * Obtains the type of the account to which the current process belongs. This API uses a promise to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [getOsAccountType]{@link osAccount.AccountManager.getOsAccountType()} instead.
         *
         * @returns { Promise<OsAccountType> } Promise used to return the OS account type obtained.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.getOsAccountType()
         */
        getOsAccountTypeFromProcess(): Promise<OsAccountType>;
        /**
         * Obtains the type of the account to which the current process belongs. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { AsyncCallback<OsAccountType> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is the OS account type obtained.
         *     Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        getOsAccountType(callback: AsyncCallback<OsAccountType>): void;
        /**
         * Obtains the type of the account to which the current process belongs. This API uses a promise to return the
         * result.
         *
         * @returns { Promise<OsAccountType> } Promise used to return the OS account type obtained.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        getOsAccountType(): Promise<OsAccountType>;
        /**
         * Obtains the ID of a distributed virtual device. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [queryDistributedVirtualDeviceId]{@link osAccount.AccountManager.queryDistributedVirtualDeviceId(callback: AsyncCallback<string>)}
         * >  instead.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC or ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @param { AsyncCallback<string> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is the distributed virtual
         *     device ID obtained. Otherwise, **data** is an error object.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.queryDistributedVirtualDeviceId(callback: AsyncCallback<string>)
         */
        getDistributedVirtualDeviceId(callback: AsyncCallback<string>): void;
        /**
         * Obtains the ID of this distributed virtual device. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [queryDistributedVirtualDeviceId]{@link osAccount.AccountManager.queryDistributedVirtualDeviceId()} instead.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC or ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @returns { Promise<string> } Promise used to return the distributed virtual device ID obtained.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.queryDistributedVirtualDeviceId()
         */
        getDistributedVirtualDeviceId(): Promise<string>;
        /**
         * Queries the ID of a distributed virtual device. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC or ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @param { AsyncCallback<string> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is the distributed virtual device ID
         *     obtained. Otherwise, **data** is an error object.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        queryDistributedVirtualDeviceId(callback: AsyncCallback<string>): void;
        /**
         * Queries the ID of this distributed virtual device. This API uses a promise to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC or ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @returns { Promise<string> } Promise used to return the distributed virtual device ID obtained.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        queryDistributedVirtualDeviceId(): Promise<string>;
        /**
         * Obtains the OS account ID based on the SN. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [getOsAccountLocalIdForSerialNumber]{@link osAccount.AccountManager.getOsAccountLocalIdForSerialNumber(serialNumber: number, callback: AsyncCallback<number>)}
         * >  instead.
         *
         * @param { number } serialNumber - Account SN.
         * @param { AsyncCallback<number> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is the OS account ID obtained.
         *     Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.OsAccount
         * @since 8
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.getOsAccountLocalIdForSerialNumber(serialNumber: long, callback: AsyncCallback<int>)
         */
        getOsAccountLocalIdBySerialNumber(serialNumber: number, callback: AsyncCallback<number>): void;
        /**
         * Obtains the OS account ID based on the SN. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [getOsAccountLocalIdForSerialNumber]{@link osAccount.AccountManager.getOsAccountLocalIdForSerialNumber(serialNumber: number)}
         * >  instead.
         *
         * @param { number } serialNumber - Account SN.
         * @returns { Promise<number> } Promise used to return the OS account ID obtained.
         * @syscap SystemCapability.Account.OsAccount
         * @since 8
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.getOsAccountLocalIdForSerialNumber(serialNumber: long)
         */
        getOsAccountLocalIdBySerialNumber(serialNumber: number): Promise<number>;
        /**
         * Obtains the OS account ID based on the SN. This API uses an asynchronous callback to return the result.
         *
         * @param { number } serialNumber - Account SN.
         * @param { AsyncCallback<number> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is the OS account ID obtained.
         *     Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300002 - Invalid serialNumber.
         * @throws { BusinessError } 12300003 - The account indicated by serialNumber does not exist.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        getOsAccountLocalIdForSerialNumber(serialNumber: number, callback: AsyncCallback<number>): void;
        /**
         * Obtains the OS account ID based on the SN. This API uses a promise to return the result.
         *
         * @param { number } serialNumber - Account SN.
         * @returns { Promise<number> } Promise used to return the OS account ID obtained.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300002 - Invalid serialNumber.
         * @throws { BusinessError } 12300003 - The account indicated by serialNumber does not exist.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        getOsAccountLocalIdForSerialNumber(serialNumber: number): Promise<number>;
        /**
         * Obtains the SN of an OS account based on the account ID. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [getSerialNumberForOsAccountLocalId]{@link osAccount.AccountManager.getSerialNumberForOsAccountLocalId(localId: number, callback: AsyncCallback<number>)}
         * >  instead.
         *
         * @param { number } localId - ID of the target OS account.
         * @param { AsyncCallback<number> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is the SN obtained.
         *     Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.OsAccount
         * @since 8
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.getSerialNumberForOsAccountLocalId(localId: int, callback: AsyncCallback<long>)
         */
        getSerialNumberByOsAccountLocalId(localId: number, callback: AsyncCallback<number>): void;
        /**
         * Obtains the SN of an OS account based on the account ID. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [getSerialNumberForOsAccountLocalId]{@link osAccount.AccountManager.getSerialNumberForOsAccountLocalId(localId: number)}
         * >  instead.
         *
         * @param { number } localId - ID of the target OS account.
         * @returns { Promise<number> } Promise used to return the SN obtained.
         * @syscap SystemCapability.Account.OsAccount
         * @since 8
         * @deprecated since 9
         * @useinstead osAccount.AccountManager.getSerialNumberForOsAccountLocalId(localId: int)
         */
        getSerialNumberByOsAccountLocalId(localId: number): Promise<number>;
        /**
         * Obtains the SN of an OS account based on the account ID. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { number } localId - ID of the target OS account.
         * @param { AsyncCallback<number> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is the SN obtained.
         *     Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300002 - Invalid localId.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        getSerialNumberForOsAccountLocalId(localId: number, callback: AsyncCallback<number>): void;
        /**
         * Obtains the SN of an OS account based on the account ID. This API uses a promise to return the result.
         *
         * @param { number } localId - ID of the target OS account.
         * @returns { Promise<number> } Promise used to return the SN obtained.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300002 - Invalid localId.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        getSerialNumberForOsAccountLocalId(localId: number): Promise<number>;
    }
    /**
     * Represents information about an OS account.
     *
     * @syscap SystemCapability.Account.OsAccount
     * @since 7
     */
    interface OsAccountInfo {
        /**
         * ID of the target OS account.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         */
        localId: number;
        /**
         * Name of the OS account.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         */
        localName: string;
        /**
         * Type of the OS account.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         */
        type: OsAccountType;
        /**
         * [Constraints](docroot://reference/apis-basic-services-kit/js-apis-osAccount.md#constraints) of the system
         * account. By default, no value is passed in.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         */
        constraints: Array<string>;
        /**
         * Whether the account has been verified. The value **true** means the specified account has been verified; the
         * value **false** means the opposite.
         *
         * Note: This parameter is supported since API version 7 and deprecated since API version 11. You are advised to use
         *  **isUnlocked** instead.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 8
         * @deprecated since 11
         * @useinstead osAccount.OsAccountInfo.isUnlocked
         */
        isVerified: boolean;
        /**
         * Whether the account is unlocked (whether the **el2/** directory is decrypted). The value **true** means the
         * specified account is unlocked; the value **false** means the opposite.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 11
         */
        isUnlocked: boolean;
        /**
         * Avatar of the OS account. By default, no value is passed in.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 8
         */
        photo: string;
        /**
         * OS account creation time. The value is a Unix timestamp (in seconds).
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 8
         */
        createTime: number;
        /**
         * Last login time of the OS account. The value is a Unix timestamp (in seconds).
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 8
         */
        lastLoginTime: number;
        /**
         * SN of the OS account.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 8
         */
        serialNumber: number;
        /**
         * Whether the OS account is activated. The value **true** means the specified account is activated; the value
         * **false** means the opposite.
         *
         * Note: This parameter is supported since API version 7 and deprecated since API version 11. You are advised to use
         *  **isActivated** instead.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 8
         * @deprecated since 11
         * @useinstead osAccount.OsAccountInfo.isActivated
         */
        isActived: boolean;
        /**
         * Whether the OS account is activated. The value **true** means the specified account is activated; the value
         * **false** means the opposite.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 11
         */
        isActivated: boolean;
        /**
         * Whether the OS account information is complete. The value **true** means the specified account is complete;
         * the value **false** means the opposite.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 8
         */
        isCreateCompleted: boolean;
        /**
         * Distributed account information. By default, no value is passed in.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         */
        distributedInfo: distributedAccount.DistributedInfo;
        /**
         * Domain account information. By default, no value is passed in.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 8
         */
        domainInfo: DomainAccountInfo;
    }
    /**
     * Represents the domain account information.
     *
     * @syscap SystemCapability.Account.OsAccount
     * @since 8
     */
    interface DomainAccountInfo {
        /**
         * Domain name.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 8
         */
        domain: string;
        /**
         * Domain account name.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 8
         */
        accountName: string;
        /**
         * Domain account configuration ID, which is an empty string by default.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 18
         */
        serverConfigId?: string;
        /**
         * Additional information about the domain account.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @stagemodelonly
         * @since 26.0.0
         */
        additionalInfo?: Record<string, Object>;
    }
    /**
     * Enumerates the OS account types.
     *
     * @syscap SystemCapability.Account.OsAccount
     * @since 7
     */
    enum OsAccountType {
        /**
         * Administrator account.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         */
        ADMIN = 0,
        /**
         * Normal account.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         */
        NORMAL = 1,
        /**
         * Guest account.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         */
        GUEST = 2
    }
    /**
     * Provides APIs for domain account management.
     *
     * @syscap SystemCapability.Account.OsAccount
     * @since 18
     */
    class DomainAccountManager {
        /**
         * Updates information of a domain account. This API uses a promise to return the result.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.MANAGE_DOMAIN_ACCOUNTS
         * @param { DomainAccountInfo } oldAccountInfo - Domain account information.
         * @param { DomainAccountInfo } newAccountInfo - New domain account information.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300002 - The new account info is invalid.
         * @throws { BusinessError } 12300003 - The old account not found.
         * @throws { BusinessError } 12300004 - The new account already exists.
         * @syscap SystemCapability.Account.OsAccount
         * @since 18
         */
        static updateAccountInfo(oldAccountInfo: DomainAccountInfo, newAccountInfo: DomainAccountInfo): Promise<void>;
    }
    /**
     * Represents the configuration of a domain server.
     *
     * @syscap SystemCapability.Account.OsAccount
     * @since 18
     */
    interface DomainServerConfig {
        /**
         * Server configuration parameters.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 18
         */
        parameters: Record<string, Object>;
        /**
         * Server configuration ID.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 18
         */
        id: string;
        /**
         * Domain to which the server belongs.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 18
         */
        domain: string;
    }
    /**
     * Provides APIs for domain server configuration and management.
     *
     * @syscap SystemCapability.Account.OsAccount
     * @since 18
     */
    class DomainServerConfigManager {
        /**
         * Adds domain server configuration. This API uses a promise to return the result.
         *
         * @permission ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS
         * @param { Record<string, Object> } parameters - Configuration parameters of the domain server.
         * @returns { Promise<DomainServerConfig> } Promise used to return the configuration of
         *     the newly added domain server.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300002 - Invalid server config parameters.
         * @throws { BusinessError } 12300211 - Server unreachable.
         * @throws { BusinessError } 12300213 - Server config already exists.
         * @throws { BusinessError } 12300215 - The number of server config reaches the upper limit.
         * @syscap SystemCapability.Account.OsAccount
         * @since 18
         */
        static addServerConfig(parameters: Record<string, Object>): Promise<DomainServerConfig>;
        /**
         * Removes domain server configuration. This API uses a promise to return the result.
         *
         * @permission ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS
         * @param { string } configId - Server configuration ID.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300212 - Server config not found.
         * @throws { BusinessError } 12300214 - Server config has been associated with an account.
         * @syscap SystemCapability.Account.OsAccount
         * @since 18
         */
        static removeServerConfig(configId: string): Promise<void>;
        /**
         * Updates the domain server configuration. This API uses a promise to return the result.
         *
         * @permission ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS
         * @param { string } configId - Server configuration ID.
         * @param { Record<string, Object> } parameters - Configuration parameters of the domain server.
         * @returns { Promise<DomainServerConfig> } Promise used to return the updated domain server configuration.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300002 - Invalid server config parameters.
         * @throws { BusinessError } 12300211 - Server unreachable.
         * @throws { BusinessError } 12300212 - Server config not found.
         * @throws { BusinessError } 12300213 - Server config already exists.
         * @throws { BusinessError } 12300214 - Server config has been associated with an account.
         * @syscap SystemCapability.Account.OsAccount
         * @since 18
         */
        static updateServerConfig(configId: string, parameters: Record<string, Object>): Promise<DomainServerConfig>;
        /**
         * Obtains the domain server configuration. This API uses a promise to return the result.
         *
         * @permission ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS
         * @param { string } configId - Server configuration ID.
         * @returns { Promise<DomainServerConfig> } Promise used to return the domain server configuration obtained.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300212 - Server config not found.
         * @syscap SystemCapability.Account.OsAccount
         * @since 18
         */
        static getServerConfig(configId: string): Promise<DomainServerConfig>;
        /**
         * Obtains the configurations of all domain servers. This API uses a promise to return the result.
         *
         * @permission ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS
         * @returns { Promise<Array<DomainServerConfig>> } Promise used to return the domain server configuration obtained.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @syscap SystemCapability.Account.OsAccount
         * @since 18
         */
        static getAllServerConfigs(): Promise<Array<DomainServerConfig>>;
        /**
         * Obtains the server configuration of a domain account. This API uses a promise to return the result.
         *
         * @permission ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS
         * @param { DomainAccountInfo } domainAccountInfo - Information of the domain account.
         * @returns { Promise<DomainServerConfig> } Promise used to return the domain server configuration of the account.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 12300001 - The system service works abnormally.
         * @throws { BusinessError } 12300003 - Domain account not found.
         * @syscap SystemCapability.Account.OsAccount
         * @since 18
         */
        static getAccountServerConfig(domainAccountInfo: DomainAccountInfo): Promise<DomainServerConfig>;
    }
}
export default osAccount;

```
