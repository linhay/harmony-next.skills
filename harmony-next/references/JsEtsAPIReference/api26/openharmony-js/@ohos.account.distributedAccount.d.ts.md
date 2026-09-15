# @ohos.account.distributedAccount.d.ts

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
import type { AsyncCallback } from './@ohos.base';
/**
 * The **distributedAccount** module provides APIs for managing distributed accounts, including querying and updating
 * account login states.
 *
 * @syscap SystemCapability.Account.OsAccount
 * @since 7
 */
declare namespace distributedAccount {
    /**
     * Obtains a **DistributedAccountAbility** instance.
     *
     * @returns { DistributedAccountAbility } **DistributedAccountAbility** instance obtained.
     *     This instance provides APIs for querying and updating the login state of a distributed account.
     * @syscap SystemCapability.Account.OsAccount
     * @since 7
     */
    function getDistributedAccountAbility(): DistributedAccountAbility;
    /**
     * Provides APIs for querying and updating the login state of a distributed account. You must obtain a
     * **DistributedAccountAbility** instance first.
     *
     * @syscap SystemCapability.Account.OsAccount
     * @since 7
     */
    interface DistributedAccountAbility {
        /**
         * Queries the distributed account information. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [getOsAccountDistributedInfo]{@link distributedAccount.DistributedAccountAbility.getOsAccountDistributedInfo(callback: AsyncCallback<DistributedInfo>)}
         * >  instead.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.DISTRIBUTED_DATASYNC
         * @param { AsyncCallback<DistributedInfo> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined** and **data** is the distributed account information obtained.
         *     Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead distributedAccount.DistributedAccountAbility.getOsAccountDistributedInfo(callback: AsyncCallback<DistributedInfo>)
         */
        queryOsAccountDistributedInfo(callback: AsyncCallback<DistributedInfo>): void;
        /**
         * Queries the distributed account information. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [getOsAccountDistributedInfo]{@link distributedAccount.DistributedAccountAbility.getOsAccountDistributedInfo()}
         * >  instead.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.DISTRIBUTED_DATASYNC
         * @returns { Promise<DistributedInfo> } Promise used to return the distributed account information obtained.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead distributedAccount.DistributedAccountAbility.getOsAccountDistributedInfo()
         */
        queryOsAccountDistributedInfo(): Promise<DistributedInfo>;
        /**
         * Obtains the distributed account information. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS or ohos.permission.GET_DISTRIBUTED_ACCOUNTS or
         *     ohos.permission.DISTRIBUTED_DATASYNC
         * @param { AsyncCallback<DistributedInfo> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined** and **data** is the distributed account information obtained.
         *     Otherwise, **err** is an error object.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        getOsAccountDistributedInfo(callback: AsyncCallback<DistributedInfo>): void;
        /**
         * Obtains the distributed account information. This API uses a promise to return the result.
         *
         * @permission ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS or ohos.permission.GET_DISTRIBUTED_ACCOUNTS or
         *     ohos.permission.DISTRIBUTED_DATASYNC
         * @returns { Promise<DistributedInfo> } Promise used to return the distributed account information obtained.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 12300001 - System service exception.
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        getOsAccountDistributedInfo(): Promise<DistributedInfo>;
        /**
         * Updates the distributed account information. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [setOsAccountDistributedInfo]{@link distributedAccount.DistributedAccountAbility.setOsAccountDistributedInfo(accountInfo: DistributedInfo, callback: AsyncCallback<void>)}
         * >  instead.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @param { DistributedInfo } accountInfo - Distributed account information to update.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the distributed account
         *     information is updated successfully, **err** is **undefined**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead distributedAccount.DistributedAccountAbility.setOsAccountDistributedInfo(accountInfo: DistributedInfo, callback: AsyncCallback<void>)
         */
        updateOsAccountDistributedInfo(accountInfo: DistributedInfo, callback: AsyncCallback<void>): void;
        /**
         * Updates the distributed account information. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [setOsAccountDistributedInfo]{@link distributedAccount.DistributedAccountAbility.setOsAccountDistributedInfo(accountInfo: DistributedInfo)}
         * >  instead.
         *
         * @permission ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * @param { DistributedInfo } accountInfo - Distributed account information to update.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         * @deprecated since 9
         * @useinstead distributedAccount.DistributedAccountAbility.setOsAccountDistributedInfo(accountInfo: DistributedInfo)
         */
        updateOsAccountDistributedInfo(accountInfo: DistributedInfo): Promise<void>;
        /**
         * Sets the distributed account information. This API uses an asynchronous callback to return the result.
         * This API can be called only by system applications.
         *
         * @permission ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS
         * @param { DistributedInfo } accountInfo - Distributed account information to set.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the distributed account
         *     information is set successfully, **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid accountInfo.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300406 - The distributed account information has already been bound to
         *     a sub-profile of the same OS account. [since 26.0.0]
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        setOsAccountDistributedInfo(accountInfo: DistributedInfo, callback: AsyncCallback<void>): void;
        /**
         * Sets the distributed account information. This API uses a promise to return the result.
         * This API can be called only by system applications.
         *
         * @permission ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS
         * @param { DistributedInfo } accountInfo - Distributed account information to set.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid accountInfo.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300406 - The distributed account information has already been bound to
         *     a sub-profile of the same OS account. [since 26.0.0]
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        setOsAccountDistributedInfo(accountInfo: DistributedInfo): Promise<void>;
    }
    /**
     * Enumerates the statuses of a distributed account.
     *
     * @syscap SystemCapability.Account.OsAccount
     * @since 10
     */
    enum DistributedAccountStatus {
        /**
         * The account has not logged in.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 10
         */
        NOT_LOGGED_IN = 0,
        /**
         * The account has logged in.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 10
         */
        LOGGED_IN = 1
    }
    /**
     * Represents the distributed information about an OS account.
     *
     * @syscap SystemCapability.Account.OsAccount
     * @since 7
     */
    interface DistributedInfo {
        /**
         * Name of the distributed account. It must be a non-null string.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         */
        name: string;
        /**
         * UID of the distributed account. It must be a non-null string.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         */
        id: string;
        /**
         * Login state of the distributed account. The state can be login, logout, token invalid, or logoff, which
         * correspond to the following strings respectively:
         *
         * - Ohos.account.event.LOGIN
         *
         * - Ohos.account.event.LOGOUT
         *
         * - Ohos.account.event.TOKEN_INVALID
         *
         * - Ohos.account.event.LOGOFF
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 7
         */
        event: string;
        /**
         * Nickname of the distributed account. By default, no value is passed in.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        nickname?: string;
        /**
         * Avatar of the distributed account. By default, no value is passed in.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 9
         */
        avatar?: string;
        /**
         * Status of the distributed account. The value is of the enumerated type. The default status is unlogged.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 10
         */
        readonly status?: DistributedAccountStatus;
        /**
         * Additional information about the distributed account, in the form of KV pairs. This parameter is left empty by
         * default.
         *
         * @syscap SystemCapability.Account.OsAccount
         * @since 8
         */
        scalableData?: object;
    }
}
export default distributedAccount;

```
