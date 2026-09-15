# @ohos.account.appAccount.d.ts

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
import type { AsyncCallback, Callback } from './@ohos.base';
import type Want from './@ohos.app.ability.Want';
import type rpc from './@ohos.rpc';
/**
 * The **appAccount** module provides APIs for adding, deleting, modifying, and querying application account information
 * , and supports inter-application authentication and distributed data synchronization.
 *
 * @syscap SystemCapability.Account.AppAccount
 * @since 7
 */
declare namespace appAccount {
    /**
     * Creates an **AppAccountManager** object.
     *
     * @returns { AppAccountManager } **AppAccountManager** object created.
     * @syscap SystemCapability.Account.AppAccount
     * @since 7
     */
    function createAppAccountManager(): AppAccountManager;
    /**
     * Defines the application account manager, which is used to manage account information of applications.
     *
     * @syscap SystemCapability.Account.AppAccount
     * @since 7
     */
    interface AppAccountManager {
        /**
         * Adds an application account with the given name. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [createAccount]{@link appAccount.AppAccountManager.createAccount(name: string, callback: AsyncCallback<void>)}
         * > instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.createAccount(name: string, callback: AsyncCallback<void>)
         */
        addAccount(name: string, callback: AsyncCallback<void>): void;
        /**
         * Adds an application account name and additional information. This API uses an asynchronous callback to return the
         *  result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [createAccount]{@link appAccount.AppAccountManager.createAccount(name: string, options: CreateAccountOptions, callback: AsyncCallback<void>)}
         * > instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } extraInfo - Additional information (information that can be converted to the string type).
         *     It cannot contain sensitive information, such as the application account password and token.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.createAccount(name: string, options: CreateAccountOptions, callback: AsyncCallback<void>)
         */
        addAccount(name: string, extraInfo: string, callback: AsyncCallback<void>): void;
        /**
         * Adds an application account name and additional information. This API uses a promise to return the result.
         *
         * > **NOTE**
         * > > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [createAccount]{@link appAccount.AppAccountManager.createAccount(name: string, options?: CreateAccountOptions)}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } [extraInfo] - Additional information (information that can be converted to the string type).
         *     <br>The additional information cannot be sensitive information (such as the password and token)
         *     of the application account. <br>By default, no value is passed, which means no additional information
         *     needs to be added for the account.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.createAccount(name: string, options?: CreateAccountOptions)
         */
        addAccount(name: string, extraInfo?: string): Promise<void>;
        /**
         * Creates an application account with the given name. This API uses an asynchronous callback to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name.
         * @throws { BusinessError } 12300004 - Account already exists.
         * @throws { BusinessError } 12300007 - The number of accounts reaches the upper limit.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        createAccount(name: string, callback: AsyncCallback<void>): void;
        /**
         * Creates an application account with custom data. This API uses an asynchronous callback to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { CreateAccountOptions } options - Options for creating the application account. You can customize
         *     data based on service requirements, but do not add sensitive data (such as passwords and tokens).
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name or options.
         * @throws { BusinessError } 12300004 - Account already exists.
         * @throws { BusinessError } 12300007 - The number of accounts reaches the upper limit.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        createAccount(name: string, options: CreateAccountOptions, callback: AsyncCallback<void>): void;
        /**
         * Creates an application account with custom data. This API uses a promise to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { CreateAccountOptions } [options] - Options for creating the application account.
         *     You can customize data based on service requirements, but do not add sensitive data
         *     (such as passwords and tokens).<br>By default, no value is passed in, which means no additional
         *     information needs to be added for the account.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name or options.
         * @throws { BusinessError } 12300004 - Account already exists.
         * @throws { BusinessError } 12300007 - The number of accounts reaches the upper limit.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        createAccount(name: string, options?: CreateAccountOptions): Promise<void>;
        /**
         * Adds an application account implicitly based on the specified owner. This API uses an asynchronous callback to
         * return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [createAccountImplicitly]{@link appAccount.AppAccountManager.createAccountImplicitly(owner: string, callback: AuthCallback)}
         * >  instead.
         *
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { object } options - Options for the authentication, which can be set as required.
         * @param { AuthenticatorCallback } callback - Authenticator callback used to return the result.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.createAccountImplicitly(owner: string, callback: AuthCallback)
         */
        addAccountImplicitly(owner: string, authType: string, options: {
            [key: string]: any;
        }, callback: AuthenticatorCallback): void;
        /**
         * Creates an application account implicitly based on the specified account owner. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { AuthCallback } callback - Authenticator callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid owner.
         * @throws { BusinessError } 12300007 - The number of accounts reaches the upper limit.
         * @throws { BusinessError } 12300010 - Account service busy.
         * @throws { BusinessError } 12300113 - Authenticator service not found.
         * @throws { BusinessError } 12300114 - Authenticator service exception.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        createAccountImplicitly(owner: string, callback: AuthCallback): void;
        /**
         * Creates an application account implicitly based on the specified account owner and options. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { CreateAccountImplicitlyOptions } options - Options for implicitly creating the account.
         * @param { AuthCallback } callback - Authenticator callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid owner or options.
         * @throws { BusinessError } 12300007 - The number of accounts reaches the upper limit.
         * @throws { BusinessError } 12300010 - Account service busy.
         * @throws { BusinessError } 12300113 - Authenticator service not found.
         * @throws { BusinessError } 12300114 - Authenticator service exception.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        createAccountImplicitly(owner: string, options: CreateAccountImplicitlyOptions, callback: AuthCallback): void;
        /**
         * Deletes an application account. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [removeAccount]{@link appAccount.AppAccountManager.removeAccount(name: string, callback: AsyncCallback<void>)}
         * > instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.removeAccount(name: string, callback: AsyncCallback<void>)
         */
        deleteAccount(name: string, callback: AsyncCallback<void>): void;
        /**
         * Deletes an application account. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [removeAccount]{@link appAccount.AppAccountManager.removeAccount(name: string)}
         * > instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.removeAccount(name: string)
         */
        deleteAccount(name: string): Promise<void>;
        /**
         * Removes an application account. This API uses an asynchronous callback to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        removeAccount(name: string, callback: AsyncCallback<void>): void;
        /**
         * Removes an application account. This API uses a promise to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        removeAccount(name: string): Promise<void>;
        /**
         * Disables an application account from accessing an application. This API uses an asynchronous callback to return
         * the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [setAppAccess]{@link appAccount.AppAccountManager.setAppAccess(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback<void>)}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } bundleName - Bundle name of the application. The value cannot exceed 512 characters.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.setAppAccess(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback<void>)
         */
        disableAppAccess(name: string, bundleName: string, callback: AsyncCallback<void>): void;
        /**
         * Disables an application account from accessing an application. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [setAppAccess]{@link appAccount.AppAccountManager.setAppAccess(name: string, bundleName: string, isAccessible: boolean)}
         * >  instead.
         *
         * @param { string } name - Name of the target application account. The value cannot exceed 512 characters.
         * @param { string } bundleName - Bundle name of the application. The value cannot exceed 512 characters.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.setAppAccess(name: string, bundleName: string, isAccessible: boolean)
         */
        disableAppAccess(name: string, bundleName: string): Promise<void>;
        /**
         * Enables an application account to access an application. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [setAppAccess]{@link appAccount.AppAccountManager.setAppAccess(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback<void>)}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } bundleName - Bundle name of the application. The value cannot exceed 512 characters.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.setAppAccess(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback<void>)
         */
        enableAppAccess(name: string, bundleName: string, callback: AsyncCallback<void>): void;
        /**
         * Enables an application account to access an application. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [setAppAccess]{@link appAccount.AppAccountManager.setAppAccess(name: string, bundleName: string, isAccessible: boolean)}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } bundleName - Bundle name of the application. The value cannot exceed 512 characters.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.setAppAccess(name: string, bundleName: string, isAccessible: boolean)
         */
        enableAppAccess(name: string, bundleName: string): Promise<void>;
        /**
         * Sets the access to the data of an account for an application. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } bundleName - Bundle name of the application. The value cannot exceed 512 characters.
         * @param { boolean } isAccessible - Whether the access is allowed. The value **true** means to allow the access;
         *     the value **false** means the opposite.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name or bundleName.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12400001 - Application not found. [since 9 - 13]
         * @throws { BusinessError } 12400005 - The size of authorization list reaches the upper limit. [since 14]
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        setAppAccess(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback<void>): void;
        /**
         * Sets the access to the data of an account for an application. This API uses a promise to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } bundleName - Bundle name of the application. The value cannot exceed 512 characters.
         * @param { boolean } isAccessible - Whether the access is allowed. The value **true** means to allow the access;
         *     the value **false** means the opposite.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name or bundleName.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12400001 - Application not found. [since 9 - 13]
         * @throws { BusinessError } 12400005 - The size of authorization list reaches the upper limit. [since 14]
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        setAppAccess(name: string, bundleName: string, isAccessible: boolean): Promise<void>;
        /**
         * Checks whether an application can access the data of an account. This API uses an asynchronous callback to return
         *  the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } bundleName - Bundle name of the application. The value cannot exceed 512 characters.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true** means the
         *     application can access the account data; the value **false** means the opposite.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name or bundleName.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        checkAppAccess(name: string, bundleName: string, callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether an application can access the data of an account. This API uses a promise to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } bundleName - Bundle name of the application. The value cannot exceed 512 characters.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means the application can
         *     access the account data; the value **false** means the opposite.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name or bundleName.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        checkAppAccess(name: string, bundleName: string): Promise<boolean>;
        /**
         * Checks whether data synchronization is enabled for an application account. This API uses an asynchronous callback
         *  to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [checkDataSyncEnabled]{@link appAccount.AppAccountManager.checkDataSyncEnabled(name: string, callback: AsyncCallback<boolean>)}
         * >  instead.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true** means data
         *     synchronization is enabled for the application account; the value **false** means the opposite.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.checkDataSyncEnabled(name: string, callback: AsyncCallback<boolean>)
         */
        checkAppAccountSyncEnable(name: string, callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether data synchronization is enabled for an application account. This API uses a promise to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [checkDataSyncEnabled]{@link appAccount.AppAccountManager.checkDataSyncEnabled(name: string)} instead.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means
         *     data synchronization is enabled for the application account; the value **false** means the opposite.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.checkDataSyncEnabled(name: string)
         */
        checkAppAccountSyncEnable(name: string): Promise<boolean>;
        /**
         * Checks whether data synchronization is enabled for an application account. This API uses an asynchronous callback
         *  to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true** means data
         *     synchronization is enabled for the application account; the value **false** means the opposite.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        checkDataSyncEnabled(name: string, callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether data synchronization is enabled for an application account. This API uses a promise to return the
         * result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means
         *     data synchronization is enabled for the application account; the value **false** means the opposite.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        checkDataSyncEnabled(name: string): Promise<boolean>;
        /**
         * Sets a credential for an application account. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [setCredential]{@link appAccount.AppAccountManager.setCredential(name: string, credentialType: string, credential: string, callback: AsyncCallback<void>)}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } credentialType - Credential type. The custom type, the value cannot exceed 1024 characters.
         * @param { string } credential - Credential value. The custom value, the value cannot exceed 1024 characters.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.setCredential(name: string, credentialType: string, credential: string, callback: AsyncCallback<void>)
         */
        setAccountCredential(name: string, credentialType: string, credential: string, callback: AsyncCallback<void>): void;
        /**
         * Sets a credential for an application account. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [setCredential]{@link appAccount.AppAccountManager.setCredential(name: string, credentialType: string, credential: string)}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } credentialType - Credential type. The custom type, the value cannot exceed 1024 characters.
         * @param { string } credential - Credential value. The custom value, the value cannot exceed 1024 characters.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.setCredential(name: string, credentialType: string, credential: string)
         */
        setAccountCredential(name: string, credentialType: string, credential: string): Promise<void>;
        /**
         * Sets a credential for an application account. This API uses an asynchronous callback to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } credentialType - Credential type. The custom type, the value cannot exceed 1024 characters.
         * @param { string } credential - Credential value. The custom value, the value cannot exceed 1024 characters.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the credential is set
         *     successfully, **err** is **null**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name, credentialType or credential.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        setCredential(name: string, credentialType: string, credential: string, callback: AsyncCallback<void>): void;
        /**
         * Sets a credential for an application account. This API uses a promise to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } credentialType - Credential type. The custom type, the value cannot exceed 1024 characters.
         * @param { string } credential - Credential value. The custom value, the value cannot exceed 1024 characters.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name, credentialType or credential.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        setCredential(name: string, credentialType: string, credential: string): Promise<void>;
        /**
         * Sets additional information for an application account. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [setCustomData]{@link appAccount.AppAccountManager.setCustomData(name: string, key: string, value: string, callback: AsyncCallback<void>)}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } extraInfo - Additional information (information that can be converted to the string type).
         *     It cannot contain sensitive information, such as the application account password and token.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.setCustomData(name: string, key: string, value: string, callback: AsyncCallback<void>)
         */
        setAccountExtraInfo(name: string, extraInfo: string, callback: AsyncCallback<void>): void;
        /**
         * Sets additional information for an application account. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [setCustomData]{@link appAccount.AppAccountManager.setCustomData(name: string, key: string, value: string)}
         * > instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } extraInfo - Additional information (information that can be converted to the string type).
         *     It cannot contain sensitive information, such as the application account password and token.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.setCustomData(name: string, key: string, value: string)
         */
        setAccountExtraInfo(name: string, extraInfo: string): Promise<void>;
        /**
         * Sets data synchronization for an application account. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [setDataSyncEnabled]{@link appAccount.AppAccountManager.setDataSyncEnabled(name: string, isEnabled: boolean, callback: AsyncCallback<void>)}
         * >  instead.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { boolean } isEnable - Whether to enable data synchronization. The value **true** means that
         *     data synchronization is enabled, and **false** means the opposite.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.setDataSyncEnabled(name: string, isEnabled: boolean, callback: AsyncCallback<void>)
         */
        setAppAccountSyncEnable(name: string, isEnable: boolean, callback: AsyncCallback<void>): void;
        /**
         * Sets data synchronization for an application account. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [setDataSyncEnabled]{@link appAccount.AppAccountManager.setDataSyncEnabled(name: string, isEnabled: boolean)}
         * > instead.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { boolean } isEnable - Whether to enable data synchronization. The value **true** means that
         *     data synchronization is enabled, and **false** means the opposite.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.setDataSyncEnabled(name: string, isEnabled: boolean)
         */
        setAppAccountSyncEnable(name: string, isEnable: boolean): Promise<void>;
        /**
         * Sets data synchronization for an application account. This API uses an asynchronous callback to return the
         * result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { boolean } isEnabled - Whether to enable data synchronization. The value **true** means that data
         *     synchronization is enabled, and **false** means the opposite.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        setDataSyncEnabled(name: string, isEnabled: boolean, callback: AsyncCallback<void>): void;
        /**
         * Sets data synchronization for an application account. This API uses a promise to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { boolean } isEnabled - Whether to enable data synchronization. The value **true** means that data
         *     synchronization is enabled, and **false** means the opposite.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        setDataSyncEnabled(name: string, isEnabled: boolean): Promise<void>;
        /**
         * Sets data to be associated with an application account. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [setCustomData]{@link appAccount.AppAccountManager.setCustomData(name: string, key: string, value: string, callback: AsyncCallback<void>)}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } key - Key of the associated data.
         * @param { string } value - Value of the data to set.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.setCustomData(name: string, key: string, value: string, callback: AsyncCallback<void>)
         */
        setAssociatedData(name: string, key: string, value: string, callback: AsyncCallback<void>): void;
        /**
         * Sets data to be associated with an application account. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [setCustomData]{@link appAccount.AppAccountManager.setCustomData(name: string, key: string, value: string)}
         * > instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } key - Key of the associated data.
         * @param { string } value - Value of the data to set.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.setCustomData(name: string, key: string, value: string)
         */
        setAssociatedData(name: string, key: string, value: string): Promise<void>;
        /**
         * Sets custom data for an application account. This API uses an asynchronous callback to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } key - Key of the custom data. The value cannot exceed 512 characters.
         * @param { string } value - Value of the custom data. The value cannot exceed 512 characters.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name, key or value.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12400003 - The number of custom data reaches the upper limit.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        setCustomData(name: string, key: string, value: string, callback: AsyncCallback<void>): void;
        /**
         * Sets custom data for an application account. This API uses a promise to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } key - Key of the custom data. The value cannot exceed 512 characters.
         * @param { string } value - Value of the custom data. The value cannot exceed 512 characters.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name, key or value.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12400003 - The number of custom data reaches the upper limit.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        setCustomData(name: string, key: string, value: string): Promise<void>;
        /**
         * Obtains information about all accessible application accounts. This API uses an asynchronous callback to return
         * the result.
         * This method applies to the following accounts:
         * <br> Accounts of this application.
         * <br> Accounts of third-party applications. To obtain such information,
         * <br> your application must have gained authorization from the third-party applications.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [getAllAccounts]{@link appAccount.AppAccountManager.getAllAccounts(callback: AsyncCallback<Array<AppAccountInfo>>)}
         * >  instead.
         *
         * @permission ohos.permission.GET_ALL_APP_ACCOUNTS
         * @param { AsyncCallback<Array<AppAccountInfo>> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is a list of accessible application
         *     accounts. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.getAllAccounts(callback: AsyncCallback<Array<AppAccountInfo>>)
         */
        getAllAccessibleAccounts(callback: AsyncCallback<Array<AppAccountInfo>>): void;
        /**
         * Obtains information about all accessible application accounts. This API uses a promise to return the result.
         * This method applies to the following accounts:
         * <br> Accounts of this application.
         * <br> Accounts of third-party applications. To obtain such information,
         * <br> your application must have gained authorization from the third-party applications.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [getAllAccounts]{@link appAccount.AppAccountManager.getAllAccounts()} instead.
         *
         * @permission ohos.permission.GET_ALL_APP_ACCOUNTS
         * @returns { Promise<Array<AppAccountInfo>> } Promise used to return information about all accessible accounts.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.getAllAccounts()
         */
        getAllAccessibleAccounts(): Promise<Array<AppAccountInfo>>;
        /**
         * Obtains information about all accessible application accounts. This API uses an asynchronous callback to return
         * the result.
         * This method applies to the following accounts:
         * <br> Accounts of this application.
         * <br> Accounts of third-party applications. To obtain such information,
         * <br> your application must have gained authorization from the third-party applications or
         * <br> have gained the ohos.permission.GET_ALL_APP_ACCOUNTS permission.
         *
         * @param { AsyncCallback<Array<AppAccountInfo>> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is a list of accessible application
         *     accounts. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        getAllAccounts(callback: AsyncCallback<Array<AppAccountInfo>>): void;
        /**
         * Obtains information about all accessible application accounts. This API uses a promise to return the result.
         * This method applies to the following accounts:
         * <br> Accounts of this application.
         * <br> Accounts of third-party applications. To obtain such information,
         * <br> your application must have gained authorization from the third-party applications or
         * <br> have gained the ohos.permission.GET_ALL_APP_ACCOUNTS permission.
         *
         * @returns { Promise<Array<AppAccountInfo>> } Promise used to return information about all accessible accounts.
         * @throws { BusinessError } 12300001 - System service exception.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        getAllAccounts(): Promise<Array<AppAccountInfo>>;
        /**
         * Obtains the application accounts that can be accessed by the invoker based on the application account owner. This
         *  API uses an asynchronous callback to return the result.
         * This method applies to the following accounts:
         * <br> Accounts of this application.
         * <br> Accounts of third-party applications. To obtain such information,
         * <br> your application must have gained authorization from the third-party applications.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [getAccountsByOwner]{@link appAccount.AppAccountManager.getAccountsByOwner(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>)}
         * >  instead.
         *
         * @permission ohos.permission.GET_ALL_APP_ACCOUNTS
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { AsyncCallback<Array<AppAccountInfo>> } callback - Callback used to return information about
         *     all accessible application accounts.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.getAccountsByOwner(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>)
         */
        getAllAccounts(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void;
        /**
         * Obtains the application accounts that can be accessed by the invoker based on the application account owner. This
         *  API uses a promise to return the result.
         * This method applies to the following accounts:
         * <br> Accounts of this application.
         * <br> Accounts of third-party applications. To obtain such information,
         * <br> your application must have gained authorization from the third-party applications.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [getAccountsByOwner]{@link appAccount.AppAccountManager.getAccountsByOwner(owner: string)} instead.
         *
         * @permission ohos.permission.GET_ALL_APP_ACCOUNTS
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @returns { Promise<Array<AppAccountInfo>> } Promise used to return the application accounts that can be
         *     accessed by the invoker.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.getAccountsByOwner(owner: string)
         */
        getAllAccounts(owner: string): Promise<Array<AppAccountInfo>>;
        /**
         * Obtains the application accounts that can be accessed by the invoker based on the application account owner. This
         *  API uses an asynchronous callback to return the result.
         * This method applies to the following accounts:
         * <br> Accounts of this application.
         * <br> Accounts of third-party applications. To obtain such information,
         * <br> your application must have gained authorization from the third-party applications or
         * <br> have gained the ohos.permission.GET_ALL_APP_ACCOUNTS permission.
         *
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { AsyncCallback<Array<AppAccountInfo>> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is null and **data** is the application account information
         *     obtained. Otherwise, **err** is an error object.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid owner.
         * @throws { BusinessError } 12400001 - Application not found. [since 9 - 13]
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        getAccountsByOwner(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void;
        /**
         * Obtains the application accounts that can be accessed by the invoker based on the application account owner. This
         *  API uses a promise to return the result.
         * This method applies to the following accounts:
         * <br> Accounts of this application.
         * <br> Accounts of third-party applications. To obtain such information,
         * <br> your application must have gained authorization from the third-party applications or
         * <br> have gained the ohos.permission.GET_ALL_APP_ACCOUNTS permission.
         *
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @returns { Promise<Array<AppAccountInfo>> } Promise used to return the application account information obtained.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid owner.
         * @throws { BusinessError } 12400001 - Application not found. [since 9 - 13]
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        getAccountsByOwner(owner: string): Promise<Array<AppAccountInfo>>;
        /**
         * Obtains the credential of an application account. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [getCredential]{@link appAccount.AppAccountManager.getCredential(name: string, credentialType: string, callback: AsyncCallback<string>)}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } credentialType - Credential type. The custom type, the value cannot exceed 1024 characters.
         * @param { AsyncCallback<string> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null** and **data** is the credential obtained. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.getCredential(name: string, credentialType: string, callback: AsyncCallback<string>)
         */
        getAccountCredential(name: string, credentialType: string, callback: AsyncCallback<string>): void;
        /**
         * Obtains the credential of an application account. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [getCredential]{@link appAccount.AppAccountManager.getCredential(name: string, credentialType: string)}
         * > instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } credentialType - Credential type. The custom type, the value cannot exceed 1024 characters.
         * @returns { Promise<string> } Promise used to return the credential obtained.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.getCredential(name: string, credentialType: string)
         */
        getAccountCredential(name: string, credentialType: string): Promise<string>;
        /**
         * Obtains the credential of an application account. This API uses an asynchronous callback to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } credentialType - Credential type. The custom type, the value cannot exceed 1024 characters.
         * @param { AsyncCallback<string> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null** and **data** is the credential obtained. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name or credentialType.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300102 - Credential not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        getCredential(name: string, credentialType: string, callback: AsyncCallback<string>): void;
        /**
         * Obtains the credential of an application account. This API uses a promise to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } credentialType - Credential type. The custom type, the value cannot exceed 1024 characters.
         * @returns { Promise<string> } Promise used to return the credential obtained.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name or credentialType.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300102 - Credential not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        getCredential(name: string, credentialType: string): Promise<string>;
        /**
         * Obtains additional information of an application account. Additional information refers to other information that
         *  can be converted to the string type. It cannot contain sensitive information, such as the application account
         * password and token. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [getCustomData]{@link appAccount.AppAccountManager.getCustomData(name: string, key: string, callback: AsyncCallback<string>)}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { AsyncCallback<string> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is the additional information
         *     obtained. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.getCustomData(name: string, key: string, callback: AsyncCallback<string>)
         */
        getAccountExtraInfo(name: string, callback: AsyncCallback<string>): void;
        /**
         * Obtains additional information of an application account. Additional information refers to other information that
         *  can be converted to the string type. It cannot contain sensitive information, such as the application account
         * password and token. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [getCustomData]{@link appAccount.AppAccountManager.getCustomData(name: string, key: string)} instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @returns { Promise<string> } Promise used to return the additional information obtained.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.getCustomData(name: string, key: string)
         */
        getAccountExtraInfo(name: string): Promise<string>;
        /**
         * Obtains the associated data of an application account based on the specified key. This API uses an asynchronous
         * callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [getCustomData]{@link appAccount.AppAccountManager.getCustomData(name: string, key: string, callback: AsyncCallback<string>)}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } key - Key of the associated data.
         * @param { AsyncCallback<string> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is the data obtained.
         *     Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.getCustomData(name: string, key: string, callback: AsyncCallback<string>)
         */
        getAssociatedData(name: string, key: string, callback: AsyncCallback<string>): void;
        /**
         * Obtains data associated with an application account. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [getCustomData]{@link appAccount.AppAccountManager.getCustomData(name: string, key: string)} instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } key - Key of the associated data.
         * @returns { Promise<string> } Promise used to return the data obtained.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.getCustomData(name: string, key: string)
         */
        getAssociatedData(name: string, key: string): Promise<string>;
        /**
         * Obtains the custom data of an application account based on the specified key. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } key - Key of the custom data. The value cannot exceed 512 characters.
         * @param { AsyncCallback<string> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is the custom data value
         *     obtained. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name or key.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12400002 - Custom data not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        getCustomData(name: string, key: string, callback: AsyncCallback<string>): void;
        /**
         * Obtains the custom data of an application account based on the specified key. This API uses a promise to return
         * the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } key - Key of the custom data. The value cannot exceed 512 characters.
         * @returns { Promise<string> } Promise used to return the custom data value obtained.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name or key.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12400002 - Custom data not found
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        getCustomData(name: string, key: string): Promise<string>;
        /**
         * Obtains the custom data of an application account based on the specified key. The API returns the result
         * synchronously.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } key - Key of the custom data. The value cannot exceed 512 characters.
         * @returns { string } Value of the custom data, by default, no value is passed in.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name or key.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12400002 - Custom data not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        getCustomDataSync(name: string, key: string): string;
        /**
         * Subscribes to account information changes of apps.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [on('accountChange')]{@link appAccount.AppAccountManager.on(type: 'accountChange', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>)}
         * >  instead.
         *
         * @param { 'change' } type - Event type to subscribe to. The value is **'change'**.
         *     An event will be reported when the account information changes.
         * @param { Array<string> } owners - Application bundle names of the account.
         * @param { Callback<Array<AppAccountInfo>> } callback - Callback registered to return the list of
         *     changed application accounts.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.on(type: 'accountChange', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>)
         */
        on(type: 'change', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void;
        /**
         * Subscribes to account information changes of apps.
         *
         * @param { 'accountChange' } type - Event type to subscribe to. The value is **'accountChange'**.
         *     An event will be reported when the account information of the target application changes.
         * @param { Array<string> } owners - Application bundle names of the account.
         * @param { Callback<Array<AppAccountInfo>> } callback - Callback registered to return the list
         *     of changed application accounts.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid type or owners.
         * @throws { BusinessError } 12400001 - Application not found. [since 9 - 13]
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        on(type: 'accountChange', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void;
        /**
         * Unsubscribes from account information changes.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 7 and deprecated since API version 9. You are advised to use
         * > [off('accountChange')]{@link appAccount.AppAccountManager.off(type: 'accountChange', callback?: Callback<Array<AppAccountInfo>>)}
         * >  instead.
         *
         * @param { 'change' } type - Event type to subscribe to. The value is **'change'**.
         *     An event will be reported when the account information changes.
         * @param { Callback<Array<AppAccountInfo>> } [callback] - Callback to unregister.
         *     By default, no value is passed, which means to unregister all callbacks for
         *     the specified event.
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.off(type: 'accountChange', callback?: Callback<Array<AppAccountInfo>>)
         */
        off(type: 'change', callback?: Callback<Array<AppAccountInfo>>): void;
        /**
         * Unsubscribes from account information changes.
         *
         * @param { 'accountChange' } type - Event type to unsubscribe from. The value is **'accountChange'**.
         * @param { Callback<Array<AppAccountInfo>> } [callback] - Callback to unregister. By default, no value is passed,
         *     which means to unregister all callbacks for the specified event.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid type.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        off(type: 'accountChange', callback?: Callback<Array<AppAccountInfo>>): void;
        /**
         * Authenticates an application account. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [auth]{@link appAccount.AppAccountManager.auth(name: string, owner: string, authType: string, callback: AuthCallback)}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { object } options - Options for the authentication.
         * @param { AuthenticatorCallback } callback - Authenticator callback used to return the result.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.auth(name: string, owner: string, authType: string, callback: AuthCallback)
         */
        authenticate(name: string, owner: string, authType: string, options: {
            [key: string]: any;
        }, callback: AuthenticatorCallback): void;
        /**
         * Authenticates an application account. This API uses an asynchronous callback to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { AuthCallback } callback - Authenticator callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name, owner or authType.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300010 - Account service busy.
         * @throws { BusinessError } 12300113 - Authenticator service not found.
         * @throws { BusinessError } 12300114 - Authenticator service exception.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        auth(name: string, owner: string, authType: string, callback: AuthCallback): void;
        /**
         * Authenticates an application account. This API uses an asynchronous callback to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { Record<string, Object> } options - Options for the authentication.
         * @param { AuthCallback } callback - Authenticator callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name, owner, authType or options.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300010 - Account service busy.
         * @throws { BusinessError } 12300113 - Authenticator service not found.
         * @throws { BusinessError } 12300114 - Authenticator service exception.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        auth(name: string, owner: string, authType: string, options: Record<string, Object>, callback: AuthCallback): void;
        /**
         * Obtains the authorization token of the specified authentication type for an application account. This API uses an
         *  asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [getAuthToken]{@link appAccount.AppAccountManager.getAuthToken(name: string, owner: string, authType: string, callback: AsyncCallback<string>)}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { AsyncCallback<string> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null** and **data** is the authorization token value obtained.
         *     Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.getAuthToken(name: string, owner: string, authType: string, callback: AsyncCallback<string>)
         */
        getOAuthToken(name: string, owner: string, authType: string, callback: AsyncCallback<string>): void;
        /**
         * Obtains the authorization token of the specified authentication type for an application account. This API uses a
         * promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [getAuthToken]{@link appAccount.AppAccountManager.getAuthToken(name: string, owner: string, authType: string)}
         * > instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @returns { Promise<string> } Promise used to return the authorization token obtained.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.getAuthToken(name: string, owner: string, authType: string)
         */
        getOAuthToken(name: string, owner: string, authType: string): Promise<string>;
        /**
         * Obtains the authorization token of the specified authentication type for an application account. This API uses an
         *  asynchronous callback to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { AsyncCallback<string> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is the
         *     authorization token value obtained. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name, owner or authType.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300107 - AuthType not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        getAuthToken(name: string, owner: string, authType: string, callback: AsyncCallback<string>): void;
        /**
         * Obtains the authorization token of the specified authentication type for an application account. This API uses a
         * promise to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @returns { Promise<string> } Promise used to return the authorization token obtained.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name, owner or authType.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300107 - AuthType not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        getAuthToken(name: string, owner: string, authType: string): Promise<string>;
        /**
         * Sets an authorization token of the specific authentication type for an application account. This API uses an
         * asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [setAuthToken]{@link appAccount.AppAccountManager.setAuthToken(name: string, authType: string, token: string, callback: AsyncCallback<void>)}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { string } token - Authorization token. The value cannot exceed 1024 characters.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.setAuthToken(name: string, authType: string, token: string, callback: AsyncCallback<void>)
         */
        setOAuthToken(name: string, authType: string, token: string, callback: AsyncCallback<void>): void;
        /**
         * Sets an authorization token of the specific authentication type for an application account. This API uses a
         * promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [setAuthToken]{@link appAccount.AppAccountManager.setAuthToken(name: string, authType: string, token: string)}
         * > instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { string } token - Authorization token. The value cannot exceed 1024 characters.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.setAuthToken(name: string, authType: string, token: string)
         */
        setOAuthToken(name: string, authType: string, token: string): Promise<void>;
        /**
         * Sets an authorization token of the specific authentication type for an application account. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { string } token - Authorization token. The value cannot exceed 1024 characters.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name, authType or token.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12400004 - The number of tokens reaches the upper limit.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        setAuthToken(name: string, authType: string, token: string, callback: AsyncCallback<void>): void;
        /**
         * Sets an authorization token of the specific authentication type for an application account. This API uses a
         * promise to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { string } token - Authorization token. The value cannot exceed 1024 characters.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name, authType or token.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12400004 - The number of tokens reaches the upper limit.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        setAuthToken(name: string, authType: string, token: string): Promise<void>;
        /**
         * Deletes the authorization token of the specified authentication type for an application account. This API uses an
         *  asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [deleteAuthToken]{@link appAccount.AppAccountManager.deleteAuthToken(name: string, owner: string, authType: string, token: string, callback: AsyncCallback<void>)}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { string } token - Authorization token. The value cannot exceed 1024 characters.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.deleteAuthToken(name: string, owner: string, authType: string, token: string, callback: AsyncCallback<void>)
         */
        deleteOAuthToken(name: string, owner: string, authType: string, token: string, callback: AsyncCallback<void>): void;
        /**
         * Deletes the authorization token of the specified authentication type for an application account. This API uses a
         * promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [deleteAuthToken]{@link appAccount.AppAccountManager.deleteAuthToken(name: string, owner: string, authType: string, token: string)}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { string } token - Authorization token. The value cannot exceed 1024 characters.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.deleteAuthToken(name: string, owner: string, authType: string, token: string)
         */
        deleteOAuthToken(name: string, owner: string, authType: string, token: string): Promise<void>;
        /**
         * Deletes the authorization token of the specified authentication type for an application account. This API uses an
         *  asynchronous callback to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { string } token - Authorization token. The value cannot exceed 1024 characters. If the token
         *     does not exist, no operation is performed.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name, owner, authType or token.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300107 - AuthType not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        deleteAuthToken(name: string, owner: string, authType: string, token: string, callback: AsyncCallback<void>): void;
        /**
         * Deletes the authorization token of the specified authentication type for an application account. This API uses a
         * promise to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { string } token - Authorization token. The value cannot exceed 1024 characters. If the token
         *     does not exist, no operation is performed.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name, owner, authType or token.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300107 - AuthType not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        deleteAuthToken(name: string, owner: string, authType: string, token: string): Promise<void>;
        /**
         * Sets the visibility of an authorization token to an application. This API uses an asynchronous callback to return
         *  the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [setAuthTokenVisibility]{@link appAccount.AppAccountManager.setAuthTokenVisibility( name: string, authType: string, bundleName: string, isVisible: boolean, callback: AsyncCallback<void> )}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { string } bundleName - Bundle name of the application. The value cannot exceed 512 characters.
         * @param { boolean } isVisible - Whether the authorization token is visible to the application.
         *     The value **true** means the authorization token is visible to the application;
         *     the value **false** means the opposite.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.setAuthTokenVisibility( name: string, authType: string, bundleName: string, isVisible: boolean, callback: AsyncCallback<void> )
         */
        setOAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean, callback: AsyncCallback<void>): void;
        /**
         * Sets the visibility of an authorization token to an application. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [setAuthTokenVisibility]{@link appAccount.AppAccountManager.setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean)}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { string } bundleName - Bundle name of the application. The value cannot exceed 512 characters.
         * @param { boolean } isVisible - Whether the authorization token is visible to the application. The value **true** means
         *     the authorization token is visible to the application; the value **false** means the opposite.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean)
         */
        setOAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>;
        /**
         * Sets the visibility of an authorization token to an application. This API uses an asynchronous callback to return
         *  the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { string } bundleName - Bundle name of the application. The value cannot exceed 512 characters.
         * @param { boolean } isVisible - Whether the authorization token is visible to the application.
         *     The value **true** means the authorization token is visible to the application;
         *     the value **false** means the opposite.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name, authType or bundleName.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300107 - AuthType not found.
         * @throws { BusinessError } 12400001 - Application not found. [since 9 - 13]
         * @throws { BusinessError } 12400005 - The size of authorization list reaches the upper limit.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean, callback: AsyncCallback<void>): void;
        /**
         * Sets the visibility of an authorization token to an application. This API uses a promise to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { string } bundleName - Bundle name of the application. The value cannot exceed 512 characters.
         * @param { boolean } isVisible - Whether the authorization token is visible to the application.
         *     The value **true** means the authorization token is visible to the application;
         *     the value **false** means the opposite.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name, authType or bundleName.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300107 - AuthType not found.
         * @throws { BusinessError } 12400001 - Application not found. [since 9 - 13]
         * @throws { BusinessError } 12400005 - The size of authorization list reaches the upper limit.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>;
        /**
         * Checks the visibility of an authorization token of the specified authentication type to an application. This API
         * uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [checkAuthTokenVisibility]{@link appAccount.AppAccountManager.checkAuthTokenVisibility(name: string, authType: string, bundleName: string, callback: AsyncCallback<boolean>)}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { string } bundleName - Bundle name of the application. The value cannot exceed 512 characters.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null** and **data** can be **true** (the authorization token is visible to the application)
         *     or **false** (the authorization token is not visible to the application).
         *     If the operation fails, **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.checkAuthTokenVisibility(name: string, authType: string, bundleName: string, callback: AsyncCallback<boolean>)
         */
        checkOAuthTokenVisibility(name: string, authType: string, bundleName: string, callback: AsyncCallback<boolean>): void;
        /**
         * Checks the visibility of an authorization token of the specified authentication type to an application. This API
         * uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [checkAuthTokenVisibility]{@link appAccount.AppAccountManager.checkAuthTokenVisibility(name: string, authType: string, bundleName: string)}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { string } bundleName - Bundle name of the application. The value cannot exceed 512 characters.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means
         *     the authorization token is visible to the application; the value **false** means the opposite.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.checkAuthTokenVisibility(name: string, authType: string, bundleName: string)
         */
        checkOAuthTokenVisibility(name: string, authType: string, bundleName: string): Promise<boolean>;
        /**
         * Checks the visibility of an authorization token of the specified authentication type to an application. This API
         * uses an asynchronous callback to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { string } bundleName - Bundle name of the application. The value cannot exceed 512 characters.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null** and **data** can be **true** (the authorization token is visible to the application)
         *     or **false** (the authorization token is not visible to the application). If the operation fails,
         *     **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name, authType or bundleName.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300107 - AuthType not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        checkAuthTokenVisibility(name: string, authType: string, bundleName: string, callback: AsyncCallback<boolean>): void;
        /**
         * Checks the visibility of an authorization token of the specified authentication type to an application. This API
         * uses a promise to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { string } bundleName - Bundle name of the application. The value cannot exceed 512 characters.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means the
         *     authorization token is visible to the application; the value **false** means the opposite.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name, authType or bundleName.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300107 - AuthType not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        checkAuthTokenVisibility(name: string, authType: string, bundleName: string): Promise<boolean>;
        /**
         * Obtains all tokens visible to the invoker for an application account. This API uses an asynchronous callback to
         * return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [getAllAuthTokens]{@link appAccount.AppAccountManager.getAllAuthTokens(name: string, owner: string, callback: AsyncCallback<Array<AuthTokenInfo>>)}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { AsyncCallback<Array<OAuthTokenInfo>> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is a list of all tokens visible to
         *     the invoker. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.getAllAuthTokens(name: string, owner: string, callback: AsyncCallback<Array<AuthTokenInfo>>)
         */
        getAllOAuthTokens(name: string, owner: string, callback: AsyncCallback<Array<OAuthTokenInfo>>): void;
        /**
         * Obtains all tokens visible to the invoker for an application account. This API uses a promise to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [getAllAuthTokens]{@link appAccount.AppAccountManager.getAllAuthTokens(name: string, owner: string)} instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @returns { Promise<Array<OAuthTokenInfo>> } Promise used to return the tokens obtained.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.getAllAuthTokens(name: string, owner: string)
         */
        getAllOAuthTokens(name: string, owner: string): Promise<Array<OAuthTokenInfo>>;
        /**
         * Obtains all tokens visible to the invoker for an application account. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { AsyncCallback<Array<AuthTokenInfo>> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is a list of all tokens visible
         *     to the invoker. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name or owner.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        getAllAuthTokens(name: string, owner: string, callback: AsyncCallback<Array<AuthTokenInfo>>): void;
        /**
         * Obtains all tokens visible to the invoker for an application account. This API uses a promise to return the
         * result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @returns { Promise<Array<AuthTokenInfo>> } Promise used to return the tokens obtained.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name or owner.
         * @throws { BusinessError } 12300003 - Account not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        getAllAuthTokens(name: string, owner: string): Promise<Array<AuthTokenInfo>>;
        /**
         * Obtains the authorization list of the specified authentication type for an application account. The authorization
         *  list contains all authorized bundles. The token authorization list is set by
         * [setOAuthTokenVisibility]{@link appAccount.AppAccountManager.setOAuthTokenVisibility( name: string, authType: string, bundleName: string, isVisible: boolean, callback: AsyncCallback<void> )}
         * . This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [getAuthList]{@link appAccount.AppAccountManager.getAuthList(name: string, authType: string, callback: AsyncCallback<Array<string>>)}
         * >  instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { AsyncCallback<Array<string>> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is a list of authorized
         *     bundles obtained. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.getAuthList(name: string, authType: string, callback: AsyncCallback<Array<string>>)
         */
        getOAuthList(name: string, authType: string, callback: AsyncCallback<Array<string>>): void;
        /**
         * Obtains the authorization list of the specified authentication type for an application account. The authorization
         *  list contains all authorized bundles. The token authorization list is set by
         * [setOAuthTokenVisibility]{@link appAccount.AppAccountManager.setOAuthTokenVisibility( name: string, authType: string, bundleName: string, isVisible: boolean, callback: AsyncCallback<void> )}
         * . This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [getAuthList]{@link appAccount.AppAccountManager.getAuthList(name: string, authType: string)} instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @returns { Promise<Array<string>> } Promise used to return a list of authorized bundles.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.getAuthList(name: string, authType: string)
         */
        getOAuthList(name: string, authType: string): Promise<Array<string>>;
        /**
         * Obtains the authorization list of the specified authentication type for an application account. The authorization
         *  list contains all authorized bundles. The token authorization list is set by
         * [setAuthTokenVisibility]{@link appAccount.AppAccountManager.setAuthTokenVisibility( name: string, authType: string, bundleName: string, isVisible: boolean, callback: AsyncCallback<void> )}
         * . This API uses an asynchronous callback to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { AsyncCallback<Array<string>> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is a list of authorized
         *     bundles obtained. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name or authType.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300107 - AuthType not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        getAuthList(name: string, authType: string, callback: AsyncCallback<Array<string>>): void;
        /**
         * Obtains the authorization list of the specified authentication type for an application account. The authorization
         *  list contains all authorized bundles. The token authorization list is set by
         * [setAuthTokenVisibility]{@link appAccount.AppAccountManager.setAuthTokenVisibility( name: string, authType: string, bundleName: string, isVisible: boolean, callback: AsyncCallback<void> )}
         * . This API uses a promise to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @returns { Promise<Array<string>> } Promise used to return a list of authorized bundles.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name or authType.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300107 - AuthType not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        getAuthList(name: string, authType: string): Promise<Array<string>>;
        /**
         * Obtains the authenticator callback for an authentication session. This API uses an asynchronous callback to
         * return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [getAuthCallback]{@link appAccount.AppAccountManager.getAuthCallback(sessionId: string, callback: AsyncCallback<AuthCallback>)}
         * >  instead.
         *
         * @param { string } sessionId - ID of the authentication session.
         * @param { AsyncCallback<AuthenticatorCallback> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is the authenticator callback
         *     obtained. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.getAuthCallback(sessionId: string, callback: AsyncCallback<AuthCallback>)
         */
        getAuthenticatorCallback(sessionId: string, callback: AsyncCallback<AuthenticatorCallback>): void;
        /**
         * Obtains the authenticator callback for an authentication session. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [getAuthCallback]{@link appAccount.AppAccountManager.getAuthCallback(sessionId: string)} instead.
         *
         * @param { string } sessionId - ID of the authentication session.
         * @returns { Promise<AuthenticatorCallback> } Promise used to return the authenticator callback obtained.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.getAuthCallback(sessionId: string)
         */
        getAuthenticatorCallback(sessionId: string): Promise<AuthenticatorCallback>;
        /**
         * Obtains the authenticator callback for an authentication session. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { string } sessionId - ID of the authentication session.
         * @param { AsyncCallback<AuthCallback> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is the authenticator
         *     callback object obtained. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid sessionId.
         * @throws { BusinessError } 12300108 - Session not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        getAuthCallback(sessionId: string, callback: AsyncCallback<AuthCallback>): void;
        /**
         * Obtains the authenticator callback for an authentication session. This API uses a promise to return the result.
         *
         * @param { string } sessionId - ID of the authentication session.
         * @returns { Promise<AuthCallback> } Promise used to return the authenticator callback obtained.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid sessionId.
         * @throws { BusinessError } 12300108 - Session not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        getAuthCallback(sessionId: string): Promise<AuthCallback>;
        /**
         * Obtains the authenticator information of an application. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [queryAuthenticatorInfo]{@link appAccount.AppAccountManager.queryAuthenticatorInfo(owner: string, callback: AsyncCallback<AuthenticatorInfo>)}
         * >  instead.
         *
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { AsyncCallback<AuthenticatorInfo> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **null** and **data** is the authenticator information obtained. Otherwise,
         *     **err** is an error object.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.queryAuthenticatorInfo(owner: string, callback: AsyncCallback<AuthenticatorInfo>)
         */
        getAuthenticatorInfo(owner: string, callback: AsyncCallback<AuthenticatorInfo>): void;
        /**
         * Obtains the authenticator information of an application. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [queryAuthenticatorInfo]{@link appAccount.AppAccountManager.queryAuthenticatorInfo(owner: string)} instead.
         *
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @returns { Promise<AuthenticatorInfo> } Promise used to return the authenticator information obtained.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AppAccountManager.queryAuthenticatorInfo(owner: string)
         */
        getAuthenticatorInfo(owner: string): Promise<AuthenticatorInfo>;
        /**
         * Obtains the authenticator information of an application. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { AsyncCallback<AuthenticatorInfo> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **null** and **data** is the authenticator information obtained.
         *     Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid owner.
         * @throws { BusinessError } 12300113 - Authenticator service not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        queryAuthenticatorInfo(owner: string, callback: AsyncCallback<AuthenticatorInfo>): void;
        /**
         * Obtains the authenticator information of an application. This API uses a promise to return the result.
         *
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @returns { Promise<AuthenticatorInfo> } Promise used to return the authenticator information obtained.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid owner.
         * @throws { BusinessError } 12300113 - Authenticator service not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        queryAuthenticatorInfo(owner: string): Promise<AuthenticatorInfo>;
        /**
         * Checks whether an application account has specific labels. This API uses an asynchronous callback to return the
         * result. The labels are checked by the authenticator of the target application.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { Array<string> } labels - Labels to check.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** can be **true** or **false**.
         *     The value **true** means the application account has the labels; the value **false** means the opposite.
         *     If the operation fails, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name, owner or labels.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300010 - Account service busy.
         * @throws { BusinessError } 12300113 - Authenticator service not found.
         * @throws { BusinessError } 12300114 - Authenticator service exception.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        checkAccountLabels(name: string, owner: string, labels: Array<string>, callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether an application account has specific labels. This API uses a promise to return the result. The
         * labels are checked by the authenticator of the target application.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { Array<string> } labels - Labels to check.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means the application
         *     account has the labels; the value **false** means the opposite.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name, owner or labels.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300010 - Account service busy.
         * @throws { BusinessError } 12300113 - Authenticator service not found.
         * @throws { BusinessError } 12300114 - Authenticator service exception.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        checkAccountLabels(name: string, owner: string, labels: Array<string>): Promise<boolean>;
        /**
         * Deletes the credential of the specified type from an application account. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } credentialType - Credential type. The custom type, the value cannot exceed 1024 characters.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **null**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name or credentialType.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300102 - Credential not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        deleteCredential(name: string, credentialType: string, callback: AsyncCallback<void>): void;
        /**
         * Deletes the credential of the specified type from an application account. This API uses a promise to return the
         * result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } credentialType - Credential type. The custom type, the value cannot exceed 1024 characters.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name or credentialType.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300102 - Credential not found.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        deleteCredential(name: string, credentialType: string): Promise<void>;
        /**
         * Selects the accounts that can be accessed by the invoker based on the options. This API uses an asynchronous
         * callback to return the result. If the options contain label constraints, the authenticator of the target
         * application provides the capability of checking the labels.
         *
         * @param { SelectAccountsOptions } options - Options for selecting accounts.
         * @param { AsyncCallback<Array<AppAccountInfo>> } callback - Callback used to return the result.
         *     If the operation is successful, **err** is **null** and **data** is a list of accounts selected.
         *     Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid options.
         * @throws { BusinessError } 12300010 - Account service busy.
         * @throws { BusinessError } 12300114 - Authenticator service exception.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        selectAccountsByOptions(options: SelectAccountsOptions, callback: AsyncCallback<Array<AppAccountInfo>>): void;
        /**
         * Selects the accounts that can be accessed by the invoker based on the options. This API uses a promise to return
         * the result. If the options contain label constraints, the authenticator of the target application provides the
         * capability of checking the labels.
         *
         * @param { SelectAccountsOptions } options - Options for selecting accounts.
         * @returns { Promise<Array<AppAccountInfo>> } Promise used to return the accounts selected.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid options.
         * @throws { BusinessError } 12300010 - Account service busy.
         * @throws { BusinessError } 12300114 - Authenticator service exception.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        selectAccountsByOptions(options: SelectAccountsOptions): Promise<Array<AppAccountInfo>>;
        /**
         * Verifies the credential of an application account. This API uses an asynchronous callback to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { AuthCallback } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name or owner.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300010 - Account service busy.
         * @throws { BusinessError } 12300113 - Authenticator service not found.
         * @throws { BusinessError } 12300114 - Authenticator service exception.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        verifyCredential(name: string, owner: string, callback: AuthCallback): void;
        /**
         * Verifies the user credential. This API uses an asynchronous callback to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } owner - Owner of the application account. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { VerifyCredentialOptions } options - Options for credential verification.
         * @param { AuthCallback } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid name, owner or options.
         * @throws { BusinessError } 12300003 - Account not found.
         * @throws { BusinessError } 12300010 - Account service busy.
         * @throws { BusinessError } 12300113 - Authenticator service not found.
         * @throws { BusinessError } 12300114 - Authenticator service exception.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        verifyCredential(name: string, owner: string, options: VerifyCredentialOptions, callback: AuthCallback): void;
        /**
         * Sets the authenticator attributes of an application. This API uses an asynchronous callback to return the result.
         *
         * @param { string } owner - Owner of the authenticator. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { AuthCallback } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid owner.
         * @throws { BusinessError } 12300010 - Account service busy.
         * @throws { BusinessError } 12300113 - Authenticator service not found.
         * @throws { BusinessError } 12300114 - Authenticator service exception.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        setAuthenticatorProperties(owner: string, callback: AuthCallback): void;
        /**
         * Sets the authenticator properties. This API uses an asynchronous callback to return the result.
         *
         * @param { string } owner - Owner of the authenticator. The value is the Bundle name of the application.
         *     The value cannot exceed 1024 characters.
         * @param { SetPropertiesOptions } options - Authenticator properties to set.
         * @param { AuthCallback } callback - Authenticator callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         * @throws { BusinessError } 12300001 - System service exception.
         * @throws { BusinessError } 12300002 - Invalid owner or options.
         * @throws { BusinessError } 12300010 - Account service busy.
         * @throws { BusinessError } 12300113 - Authenticator service not found.
         * @throws { BusinessError } 12300114 - Authenticator service exception.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        setAuthenticatorProperties(owner: string, options: SetPropertiesOptions, callback: AuthCallback): void;
    }
    /**
     * Defines application account information.
     *
     * @syscap SystemCapability.Account.AppAccount
     * @since 7
     */
    interface AppAccountInfo {
        /**
         * Owner of the application account. The value is the bundle name of the application.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         */
        owner: string;
        /**
         * Name of the application account.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 7
         */
        name: string;
    }
    /**
     * Defines authorization token information.
     *
     * > **NOTE**
     * >
     * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
     * > [AuthTokenInfo]{@link appAccount.AuthTokenInfo} instead.
     *
     * @syscap SystemCapability.Account.AppAccount
     * @since 8
     * @deprecated since 9
     * @useinstead appAccount.AuthTokenInfo
     */
    interface OAuthTokenInfo {
        /**
         * Authentication type.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AuthTokenInfo.authType
         */
        authType: string;
        /**
         * Value of the authorization token.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.AuthTokenInfo.token
         */
        token: string;
    }
    /**
     * Defines authorization token information.
     *
     * @syscap SystemCapability.Account.AppAccount
     * @since 9
     */
    interface AuthTokenInfo {
        /**
         * Authentication type.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        authType: string;
        /**
         * Value of the authorization token.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        token: string;
        /**
         * Information about the account to which the token belongs. By default, no value is passed in.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        account?: AppAccountInfo;
    }
    /**
     * Defines OAuth authenticator information.
     *
     * @syscap SystemCapability.Account.AppAccount
     * @since 8
     */
    interface AuthenticatorInfo {
        /**
         * Owner of the authenticator. The value is the Bundle name of the application.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         */
        owner: string;
        /**
         * ID of the authenticator icon.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         */
        iconId: number;
        /**
         * ID of the authenticator label.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         */
        labelId: number;
    }
    /**
     * Defines the authentication result.
     *
     * @syscap SystemCapability.Account.AppAccount
     * @since 9
     */
    interface AuthResult {
        /**
         * Information about the account to which the token belongs. By default, no value is passed in.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        account?: AppAccountInfo;
        /**
         * Token information. By default, no value is passed in.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        tokenInfo?: AuthTokenInfo;
    }
    /**
     * Defines the options for creating an application account.
     *
     * @syscap SystemCapability.Account.AppAccount
     * @since 9
     */
    interface CreateAccountOptions {
        /**
         * Custom data. By default, no value is passed in.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        customData?: Record<string, string>;
    }
    /**
     * Defines the options for implicitly creating an application account.
     *
     * @syscap SystemCapability.Account.AppAccount
     * @since 9
     */
    interface CreateAccountImplicitlyOptions {
        /**
         * Required labels. By default, no value is passed in.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        requiredLabels?: Array<string>;
        /**
         * Authentication type.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        authType?: string;
        /**
         * Custom parameter object. By default, no value is passed in.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        parameters?: Record<string, Object>;
    }
    /**
     * Defines the options for selecting accounts.
     *
     * @syscap SystemCapability.Account.AppAccount
     * @since 9
     */
    interface SelectAccountsOptions {
        /**
         * Array of allowed accounts. By default, no value is passed in.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        allowedAccounts?: Array<AppAccountInfo>;
        /**
         * Array of the owners of the allowed accounts. By default, no value is passed in.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        allowedOwners?: Array<string>;
        /**
         * Labels of the authenticator. By default, no value is passed in.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        requiredLabels?: Array<string>;
    }
    /**
     * Represents the options for verifying the user credential.
     *
     * @syscap SystemCapability.Account.AppAccount
     * @since 9
     */
    interface VerifyCredentialOptions {
        /**
         * Credential type. The custom type, the value cannot exceed 1024 characters. By default, no value is passed in.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        credentialType?: string;
        /**
         * Credential value. The custom value, the value cannot exceed 1024 characters. By default, no value is passed in.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        credential?: string;
        /**
         * Custom parameter object. By default, no value is passed in.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        parameters?: Record<string, Object>;
    }
    /**
     * Represents the options for setting authenticator properties.
     *
     * @syscap SystemCapability.Account.AppAccount
     * @since 9
     */
    interface SetPropertiesOptions {
        /**
         * Property object. By default, no value is passed in.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        properties?: Record<string, Object>;
        /**
         * Custom parameter object. By default, no value is passed in.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        parameters?: Record<string, Object>;
    }
    /**
     * Enumerates the constants.
     *
     * @syscap SystemCapability.Account.AppAccount
     * @since 8
     */
    enum Constants {
        /**
         * Operation of adding an account implicitly.
         *
         * Note: This API is supported since API version 8 and deprecated since API version 9. Use
         * **ACTION_CREATE_ACCOUNT_IMPLICITLY** instead.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.Constants.ACTION_CREATE_ACCOUNT_IMPLICITLY
         */
        ACTION_ADD_ACCOUNT_IMPLICITLY = 'addAccountImplicitly',
        /**
         * Authentication operation.
         *
         * Note: This API is supported since API version 8 and deprecated since API version 9. Use **ACTION_AUTH** instead.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.Constants.ACTION_AUTH
         */
        ACTION_AUTHENTICATE = 'authenticate',
        /**
         * Operation of creating an account implicitly.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        ACTION_CREATE_ACCOUNT_IMPLICITLY = "createAccountImplicitly",
        /**
         * Authentication operation.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        ACTION_AUTH = "auth",
        /**
         * Operation of verifying credentials.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        ACTION_VERIFY_CREDENTIAL = "verifyCredential",
        /**
         * Operation of setting authenticator properties.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        ACTION_SET_AUTHENTICATOR_PROPERTIES = "setAuthenticatorProperties",
        /**
         * Name of the application account.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         */
        KEY_NAME = "name",
        /**
         * Bundle name of the application account owner.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         */
        KEY_OWNER = "owner",
        /**
         * Token.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         */
        KEY_TOKEN = "token",
        /**
         * Operation.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         */
        KEY_ACTION = "action",
        /**
         * Authentication type.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         */
        KEY_AUTH_TYPE = "authType",
        /**
         * Session ID.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         */
        KEY_SESSION_ID = "sessionId",
        /**
         * PID of the caller.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         */
        KEY_CALLER_PID = "callerPid",
        /**
         * UID of the caller.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         */
        KEY_CALLER_UID = "callerUid",
        /**
         * Bundle name of the caller.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         */
        KEY_CALLER_BUNDLE_NAME = "callerBundleName",
        /**
         * Required labels.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        KEY_REQUIRED_LABELS = "requiredLabels",
        /**
         * Return value of the Boolean type.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        KEY_BOOLEAN_RESULT = "booleanResult"
    }
    /**
     * Enumerates the result codes.
     *
     * > **NOTE**<br>
     * > > This API is supported since API version 8 and deprecated since API version 9. For details, see
     * > [Account Management Error Codes](docroot://reference/apis-basic-services-kit/errorcode-account.md).
     *
     * @syscap SystemCapability.Account.AppAccount
     * @since 8
     * @deprecated since 9
     */
    enum ResultCode {
        /**
         * The operation is successful.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         */
        SUCCESS = 0,
        /**
         * The application account does not exist.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         */
        ERROR_ACCOUNT_NOT_EXIST = 10001,
        /**
         * The **AppAccountManager** service is abnormal.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         */
        ERROR_APP_ACCOUNT_SERVICE_EXCEPTION = 10002,
        /**
         * The password is invalid.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         */
        ERROR_INVALID_PASSWORD = 10003,
        /**
         * The request is invalid.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         */
        ERROR_INVALID_REQUEST = 10004,
        /**
         * The response is invalid.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         */
        ERROR_INVALID_RESPONSE = 10005,
        /**
         * The network is abnormal.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         */
        ERROR_NETWORK_EXCEPTION = 10006,
        /**
         * The authenticator does not exist.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         */
        ERROR_OAUTH_AUTHENTICATOR_NOT_EXIST = 10007,
        /**
         * The authentication is canceled.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         */
        ERROR_OAUTH_CANCELED = 10008,
        /**
         * The size of the OAuth list exceeds the limit.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         */
        ERROR_OAUTH_LIST_TOO_LARGE = 10009,
        /**
         * The OAuth service is busy.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         */
        ERROR_OAUTH_SERVICE_BUSY = 10010,
        /**
         * The OAuth service is abnormal.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         */
        ERROR_OAUTH_SERVICE_EXCEPTION = 10011,
        /**
         * The session to be authenticated does not exist.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         */
        ERROR_OAUTH_SESSION_NOT_EXIST = 10012,
        /**
         * The authentication timed out.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         */
        ERROR_OAUTH_TIMEOUT = 10013,
        /**
         * The authorization token does not exist.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         */
        ERROR_OAUTH_TOKEN_NOT_EXIST = 10014,
        /**
         * The number of OAuth tokens reaches the limit.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         */
        ERROR_OAUTH_TOKEN_TOO_MANY = 10015,
        /**
         * The authentication operation is not supported.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         */
        ERROR_OAUTH_UNSUPPORT_ACTION = 10016,
        /**
         * The authentication type is not supported.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         */
        ERROR_OAUTH_UNSUPPORT_AUTH_TYPE = 10017,
        /**
         * The required permission is missing.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         */
        ERROR_PERMISSION_DENIED = 10018
    }
    /**
     * Provides OAuth authenticator callbacks.
     *
     * > **NOTE**
     * >
     * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
     * > [AuthCallback]{@link appAccount.AuthCallback} instead.
     *
     * @syscap SystemCapability.Account.AppAccount
     * @since 8
     * @deprecated since 9
     * @useinstead appAccount.AuthCallback
     */
    interface AuthenticatorCallback {
        /**
         * Called to return the result of an authentication request.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. Use [onResult](#onresult9) instead.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead AppAccount.AuthCallback.onResult
         */
        onResult: (code: number, result: {
            [key: string]: any;
        }) => void;
        /**
         * Called to redirect a request.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. Use [onRequestRedirected](#onrequestredirected9) instead.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead AppAccount.AuthCallback.onRequestRedirected
         */
        onRequestRedirected: (request: Want) => void;
    }
    /**
     * Implements authenticator callbacks.
     *
     * @syscap SystemCapability.Account.AppAccount
     * @since 9
     */
    interface AuthCallback {
        /**
         *
         * Called to return the result of an authentication request.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        onResult: (code: number, result?: AuthResult) => void;
        /**
         * Called to redirect a request.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        onRequestRedirected: (request: Want) => void;
        /**
         * Called to continue to process the request.
         *
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        onRequestContinued?: () => void;
    }
    /**
     * Provides APIs to operate the authenticator.
     *
     * @syscap SystemCapability.Account.AppAccount
     * @name Authenticator
     * @since 8
     */
    class Authenticator {
        /**
         * Adds an application account implicitly based on the specified authentication type and options. This API uses an
         * asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [createAccountImplicitly](docroot://reference/apis-basic-services-kit/js-apis-appAccount.md#createaccountimplicitly9-2)
         * >  instead.
         *
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { string } callerBundleName - Bundle name of the authentication requester.
         * @param { object } options - Options for the authentication.
         * @param { AuthenticatorCallback } callback - Authenticator callback used to return the result.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.Authenticator.createAccountImplicitly(options: CreateAccountImplicitlyOptions, callback: AuthCallback)
         */
        addAccountImplicitly(authType: string, callerBundleName: string, options: {
            [key: string]: any;
        }, callback: AuthenticatorCallback): void;
        /**
         * Creates an application account implicitly based on the specified account owner. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { CreateAccountImplicitlyOptions } options - Options for implicitly creating the account.
         * @param { AuthCallback } callback - Authenticator callback used to return the result.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        createAccountImplicitly(options: CreateAccountImplicitlyOptions, callback: AuthCallback): void;
        /**
         * Authenticates an application account to obtain the OAuth token. This API uses an asynchronous callback to return
         * the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 9. You are advised to use
         * > [auth](docroot://reference/apis-basic-services-kit/js-apis-appAccount.md#auth9-2) instead.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { string } callerBundleName - Bundle name of the authentication requester.
         * @param { object } options - Options for the authentication.
         * @param { AuthenticatorCallback } callback - Authenticator callback used to return the result.
         * @syscap SystemCapability.Account.AppAccount
         * @since 8
         * @deprecated since 9
         * @useinstead appAccount.Authenticator.auth(name: string, authType: string, options: Record<string, Object>, callback: AuthCallback)
         */
        authenticate(name: string, authType: string, callerBundleName: string, options: {
            [key: string]: any;
        }, callback: AuthenticatorCallback): void;
        /**
         * Authenticates an application account. This API uses an asynchronous callback to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { string } authType - Authentication type. The custom type, The value cannot exceed 1024 characters.
         * @param { Record<string, Object> } options - Options for the authentication.
         * @param { AuthCallback } callback - Authenticator callback used to return the result.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        auth(name: string, authType: string, options: Record<string, Object>, callback: AuthCallback): void;
        /**
         * Verifies the credential of an application account. This API uses an asynchronous callback to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { VerifyCredentialOptions } options - Options for credential verification.
         * @param { AuthCallback } callback - Authenticator callback used to return the result.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        verifyCredential(name: string, options: VerifyCredentialOptions, callback: AuthCallback): void;
        /**
         * Sets the authenticator properties. This API uses an asynchronous callback to return the result.
         *
         * @param { SetPropertiesOptions } options - Authenticator properties to set.
         * @param { AuthCallback } callback - Authenticator callback used to return the result.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        setProperties(options: SetPropertiesOptions, callback: AuthCallback): void;
        /**
         * Checks the account labels. This API uses an asynchronous callback to return the result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { Array<string> } labels - Labels to check.
         * @param { AuthCallback } callback - Authenticator callback used to return the result.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        checkAccountLabels(name: string, labels: Array<string>, callback: AuthCallback): void;
        /**
         * Checks whether an application account can be deleted. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { string } name - Name of the application account. The value cannot exceed 512 characters.
         * @param { AuthCallback } callback - Authenticator callback used to return the result.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        checkAccountRemovable(name: string, callback: AuthCallback): void;
        /**
         * Obtains the remote object of an authenticator. This API cannot be overloaded.
         *
         * @returns { rpc.RemoteObject } Remote object of the authenticator, which is used for inter-process communication.
         * @syscap SystemCapability.Account.AppAccount
         * @since 9
         */
        getRemoteObject(): rpc.RemoteObject;
    }
}
export default appAccount;

```
