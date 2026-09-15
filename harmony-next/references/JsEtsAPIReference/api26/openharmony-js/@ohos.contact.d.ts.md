# @ohos.contact.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2021-2023 Huawei Device Co., Ltd.
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
 * @kit ContactsKit
 */
import { AsyncCallback } from './@ohos.base';
import type Context from './application/BaseContext';
import type image from './@ohos.multimedia.image';
/**
* The **contact** module provides contact management functions, such as adding, deleting, and updating contacts.
 *
 * @syscap SystemCapability.Applications.ContactsData
 * @atomicservice [since 11]
 * @since 7
 */
declare namespace contact {
    /**
     * Adds a contact. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.WRITE_CONTACTS
     * @param { Contact } contact - Indicates the contact information.
     * @param { AsyncCallback<number> } callback - Indicates the callback for getting the result of the call. If the operation is successful, the
     *     ID of the added contact is returned. If the operation fails, an error code is returned.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.addContact(context: Context, contact: Contact, callback: AsyncCallback<number>)
     */
    function addContact(contact: Contact, callback: AsyncCallback<number>): void;
    /**
     * Adds a contact. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.WRITE_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { Contact } contact - Indicates the contact information.
     * @param { AsyncCallback<number> } callback - Indicates the callback for getting the result of the call. If the operation is successful, the
     *     ID of the added contact is returned. If the operation fails, an error code is returned.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - 1.Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * 2.Failed to open contact portrait file. 3.Internal error. Invalid contact id. Failed to generate contact profile.
     * 4.Internal error. Failed to save contact portrait.
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice [since 12]
     * @since 10
     */
    function addContact(context: Context, contact: Contact, callback: AsyncCallback<number>): void;
    /**
     * Adds a contact. This API uses a promise to return the result.
     *
     *
     * @permission ohos.permission.WRITE_CONTACTS
     * @param { Contact } contact - Indicates the contact information.
     * @returns { Promise<number> } Promise used to return the result, which is the ID of the added contact.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.addContact(context: Context, contact: Contact)
     */
    function addContact(contact: Contact): Promise<number>;
    /**
     * Adds a contact. This API uses a promise to return the result.
     *
     * @permission ohos.permission.WRITE_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { Contact } contact - Indicates the contact information.
     * @returns { Promise<number> } Promise used to return the result, which is the ID of the added contact.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - 1.Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * 2.Failed to open contact portrait file. 3.Internal error. Invalid contact id. Failed to generate contact profile.
     * 4.Internal error. Failed to save contact portrait.
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice [since 12]
     * @since 10
     */
    function addContact(context: Context, contact: Contact): Promise<number>;
    /**
     * Selects a contact. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call. If the operation is
     *     successful, an array of selected contacts is returned. If the operation fails, an error code is returned.
     * @syscap SystemCapability.Applications.Contacts
     * @since 7
     * @deprecated since 10
     * @useinstead contact.selectContacts(callback: AsyncCallback<Array<Contact>>)
     */
    function selectContact(callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Selects a contact. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call. If the operation is
     *     successful, an array of selected contacts is returned. If the operation fails, an error code is returned.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.Contacts
     * @atomicservice [since 11]
     * @since 10
     */
    function selectContacts(callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Selects a contact. This API uses a promise to return the result.
     *
     * @returns { Promise<Array<Contact>> } Promise used to return the result, which is an array of selected contacts.
     * @syscap SystemCapability.Applications.Contacts
     * @since 7
     * @deprecated since 10
     * @useinstead contact.selectContacts()
     */
    function selectContact(): Promise<Array<Contact>>;
    /**
     * Selects a contact. This API uses a promise to return the result.
     *
     * @returns { Promise<Array<Contact>> } Promise used to return the result, which is an array of selected contacts.
     * @syscap SystemCapability.Applications.Contacts
     * @atomicservice [since 11]
     * @since 10
     */
    function selectContacts(): Promise<Array<Contact>>;
    /**
     * Selects a contact. (Filter criteria can be transferred during contact selection.) This API uses an asynchronous
     * callback to return the result.
     *
     * @param { ContactSelectionOptions } options - Contact selection options, which specifies whether one contact or
     *     multiple contacts can be selected.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call. If the operation is
     *     successful, an array of selected contacts is returned. If the operation fails, an error code is returned.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.Contacts
     * @atomicservice [since 11]
     * @since 10
     */
    function selectContacts(options: ContactSelectionOptions, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Selects a contact. (Filter criteria can be transferred during contact selection.) This API uses a promise to return
     * the result.
     *
     * @param { ContactSelectionOptions } options - Contact selection options, which specifies whether one contact or
     *     multiple contacts can be selected.
     * @returns { Promise<Array<Contact>> } Promise used to return the result, which is an array of selected contacts.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.Contacts
     * @atomicservice [since 11]
     * @since 10
     */
    function selectContacts(options: ContactSelectionOptions): Promise<Array<Contact>>;
    /**
     * Deletes a contact. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.WRITE_CONTACTS
     * @param { string } key - Unique query key of a contact. One contact corresponds to one key, which can be obtained
     *     through [queryKey]{@link contact.queryKey(context: Context, id: number, callback: AsyncCallback<string>)}.
     * @param { AsyncCallback<void> } callback - Indicates the callback for getting the result of the call. If the operation is successful, the
     *     ID of the deleted contact is returned. If the operation fails, an error code is returned.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.deleteContact(context: Context, key: string, callback: AsyncCallback<void>)
     */
    function deleteContact(key: string, callback: AsyncCallback<void>): void;
    /**
     * Deletes a contact. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.WRITE_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { string } key - Unique query key of a contact. One contact corresponds to one key, which can be obtained
     *     through [queryKey]{@link contact.queryKey(context: Context, id: number, callback: AsyncCallback<string>)}.
     * @param { AsyncCallback<void> } callback - Indicates the callback for getting the result of the call. If the operation is successful, the
     *     ID of the deleted contact is returned. If the operation fails, an error code is returned.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function deleteContact(context: Context, key: string, callback: AsyncCallback<void>): void;
    /**
     * Deletes a contact. This API uses a promise to return the result.
     *
     * @permission ohos.permission.WRITE_CONTACTS
     * @param { string } key - Unique query key of a contact. One contact corresponds to one key, which can be obtained
     *     through [queryKey]{@link contact.queryKey(context: Context, id: number, callback: AsyncCallback<string>)}.
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.deleteContact(context: Context, key: string)
     */
    function deleteContact(key: string): Promise<void>;
    /**
     * Deletes a contact. This API uses a promise to return the result.
     *
     * @permission ohos.permission.WRITE_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { string } key - Unique query key of a contact. One contact corresponds to one key, which can be obtained
     *     through [queryKey]{@link contact.queryKey(context: Context, id: number, callback: AsyncCallback<string>)}.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function deleteContact(context: Context, key: string): Promise<void>;
    /**
     * Queries a contact based on the specified key. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { string } key - Unique query key of a contact, which is the unique identifier automatically generated by
     *     the system when a contact is created. Each contact corresponds to one key, which can be obtained through
     *     [queryKey]{@link contact.queryKey(context: Context, id: number, callback: AsyncCallback<string>)}.
     * @param { AsyncCallback<Contact> } callback - Indicates the callback for getting the result of the call. If the operation is successful, an
     *     array of queried contacts is returned. If the operation fails, an error code is returned.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryContact(context: Context, key: string, callback: AsyncCallback<Contact>)
     */
    function queryContact(key: string, callback: AsyncCallback<Contact>): void;
    /**
     * Queries a contact based on the specified key. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { string } key - Unique query key of a contact, which is the unique identifier automatically generated by
     *     the system when a contact is created. Each contact corresponds to one key, which can be obtained through
     *     [queryKey]{@link contact.queryKey(context: Context, id: number, callback: AsyncCallback<string>)}.
     * @param { AsyncCallback<Contact> } callback - Indicates the callback for getting the result of the call. If the operation is successful, an
     *     array of queried contacts is returned. If the operation fails, an error code is returned.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryContact(context: Context, key: string, callback: AsyncCallback<Contact>): void;
    /**
     * Queries a contact based on the specified key and holder. This API uses an asynchronous callback to return the
     * result.
     *
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { string } key - Unique query key of a contact, which is the unique identifier automatically generated by
     *     the system when a contact is created. Each contact corresponds to one key, which can be obtained through
     *     [queryKey]{@link contact.queryKey(context: Context, id: number, callback: AsyncCallback<string>)}.
     * @param { Holder } holder - Application that creates the contacts.If the passed parameter is empty, the system
     *     contact application is used by default.
     * @param { AsyncCallback<Contact> } callback - Indicates the callback for getting the result of the call. If the operation is successful, an
     *     array of queried contacts is returned. If the operation fails, an error code is returned.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryContact(context: Context, key: string, holder: Holder, callback: AsyncCallback<Contact>)
     */
    function queryContact(key: string, holder: Holder, callback: AsyncCallback<Contact>): void;
    /**
     * Queries a contact based on the specified key and holder. This API uses an asynchronous callback to return the
     * result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { string } key - Unique query key of a contact, which is the unique identifier automatically generated by
     *     the system when a contact is created. Each contact corresponds to one key, which can be obtained through
     *     [queryKey]{@link contact.queryKey(context: Context, id: number, callback: AsyncCallback<string>)}.
     * @param { Holder } holder - Application that creates the contacts.If the passed parameter is empty, the system
     *     contact application is used by default.
     * @param { AsyncCallback<Contact> } callback - Indicates the callback for getting the result of the call. If the operation is successful, an
     *     array of queried contacts is returned. If the operation fails, an error code is returned.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryContact(context: Context, key: string, holder: Holder, callback: AsyncCallback<Contact>): void;
    /**
     * Queries a contact based on the specified key and attributes. This API uses an asynchronous callback to return the
     * result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { string } key - Unique query key of a contact, which is the unique identifier automatically generated by
     *     the system when a contact is created. Each contact corresponds to one key, which can be obtained through
     *     [queryKey]{@link contact.queryKey(context: Context, id: number, callback: AsyncCallback<string>)}.
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @param { AsyncCallback<Contact> } callback - Indicates the callback for getting the result of the call. If the operation is successful, an
     *     array of queried contacts is returned. If the operation fails, an error code is returned.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryContact(context: Context, key: string, attrs: ContactAttributes, callback: AsyncCallback<Contact>)
     */
    function queryContact(key: string, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void;
    /**
     * Queries a contact based on the specified key and attributes. This API uses an asynchronous callback to return the
     * result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { string } key - Unique query key of a contact, which is the unique identifier automatically generated by
     *     the system when a contact is created. Each contact corresponds to one key, which can be obtained through
     *     [queryKey]{@link contact.queryKey(context: Context, id: number, callback: AsyncCallback<string>)}.
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @param { AsyncCallback<Contact> } callback - Indicates the callback for getting the result of the call. If the operation is successful, an
     *     array of queried contacts is returned. If the operation fails, an error code is returned.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryContact(context: Context, key: string, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void;
    /**
     * Queries a contact based on the specified key, holder, and attributes. This API uses an asynchronous callback to
     * return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { string } key - Unique query key of a contact, which is the unique identifier automatically generated by
     *     the system when a contact is created. Each contact corresponds to one key, which can be obtained through
     *     [queryKey]{@link contact.queryKey(context: Context, id: number, callback: AsyncCallback<string>)}.
     * @param { Holder } holder - Application that creates the contacts.If the passed parameter is empty, the system
     *     contact application is used by default.
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @param { AsyncCallback<Contact> } callback - Indicates the callback for getting the result of the call. If the operation is successful, an
     *     array of queried contacts is returned. If the operation fails, an error code is returned.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>)
     */
    function queryContact(key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void;
    /**
     * Queries a contact based on the specified key, holder, and attributes. This API uses an asynchronous callback to
     * return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { string } key - Unique query key of a contact, which is the unique identifier automatically generated by
     *     the system when a contact is created. Each contact corresponds to one key, which can be obtained through
     *     [queryKey]{@link contact.queryKey(context: Context, id: number, callback: AsyncCallback<string>)}.
     * @param { Holder } holder - Application that creates the contacts.If the passed parameter is empty, the system
     *     contact application is used by default.
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @param { AsyncCallback<Contact> } callback - Indicates the callback for getting the result of the call. If the operation is successful, an
     *     array of queried contacts is returned. If the operation fails, an error code is returned.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void;
    /**
     * Queries a contact based on the specified key, holder, and attributes. This API uses a promise to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { string } key - Unique query key of a contact, which is the unique identifier automatically generated by
     *     the system when a contact is created. Each contact corresponds to one key, which can be obtained through
     *     [queryKey]{@link contact.queryKey(context: Context, id: number, callback: AsyncCallback<string>)}.
     * @param { Holder } holder - Application information for a contact. If this parameter is not specified, the system
     *     contact application is used by default.
     * @param { ContactAttributes } attrs - Contact attribute list. If this parameter is not specified, all contact
     *     attributes are queried by default.
     * @returns { Promise<Contact> } Promise used to return the result, which is the queried contact.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryContact(context: Context, key: string, holder?: Holder, attrs?: ContactAttributes)
     */
    function queryContact(key: string, holder?: Holder, attrs?: ContactAttributes): Promise<Contact>;
    /**
     * Queries a contact based on the specified key, holder, and attributes. This API uses a promise to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { string } key - Unique query key of a contact, which is the unique identifier automatically generated by
     *     the system when a contact is created. Each contact corresponds to one key, which can be obtained through
     *     [queryKey]{@link contact.queryKey(context: Context, id: number, callback: AsyncCallback<string>)}.
     * @param { Holder } holder - Application information for a contact. If this parameter is not specified, the system
     *     contact application is used by default.
     * @param { ContactAttributes } attrs - Contact attribute list. If this parameter is not specified, all contact
     *     attributes are queried by default.
     * @returns { Promise<Contact> } Promise used to return the result, which is the queried contact.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryContact(context: Context, key: string, holder?: Holder, attrs?: ContactAttributes): Promise<Contact>;
    /**
     * Queries all contacts. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryContacts(context: Context, callback: AsyncCallback<Array<Contact>>)
     */
    function queryContacts(callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries all contacts. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryContacts(context: Context, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries all contacts based on the specified holder. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Holder } holder - Application that creates the contacts.If the passed parameter is empty, the system
     *     contact application is used by default.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryContacts(context: Context, holder: Holder, callback: AsyncCallback<Array<Contact>>)
     */
    function queryContacts(holder: Holder, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries all contacts based on the specified holder. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { Holder } holder - Application that creates the contacts.If the passed parameter is empty, the system
     *     contact application is used by default.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryContacts(context: Context, holder: Holder, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries all contacts based on the specified attributes. This API uses an asynchronous callback to return the
     * result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryContacts(context: Context, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>)
     */
    function queryContacts(attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries all contacts based on the specified attributes. This API uses an asynchronous callback to return the
     * result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryContacts(context: Context, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries all contacts based on the specified holder and attributes. This API uses an asynchronous callback to return
     * the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Holder } holder - Application that creates the contacts.If the passed parameter is empty, the system
     *     contact application is used by default.
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryContacts(context: Context, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>)
     */
    function queryContacts(holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries all contacts based on the specified holder and attributes. This API uses an asynchronous callback to return
     * the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { Holder } holder - Application that creates the contacts.If the passed parameter is empty, the system
     *     contact application is used by default.
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryContacts(context: Context, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries all contacts based on the specified holder and attributes. This API uses a promise to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Holder } holder - Application information for a contact. If this parameter is not specified, the system
     *     contact application is used by default.
     * @param { ContactAttributes } attrs - Contact attribute list. If this parameter is not specified, all contact
     *     attributes are queried by default.
     * @returns { Promise<Array<Contact>> } Promise used to return the result, which is an array of queried contacts.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryContacts(context: Context, holder?: Holder, attrs?: ContactAttributes)
     */
    function queryContacts(holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>;
    /**
     * Queries all contacts based on the specified holder and attributes. This API uses a promise to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { Holder } holder - Application information for a contact. If this parameter is not specified, the system
     *     contact application is used by default.
     * @param { ContactAttributes } attrs - Contact attribute list. If this parameter is not specified, all contact
     *     attributes are queried by default.
     * @returns { Promise<Array<Contact>> } Promise used to return the result, which is an array of queried contacts.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryContacts(context: Context, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>;
    /**
     * Queries a contact based on the specified email. This API uses an asynchronous callback to return the result. The
     * return result of this API includes only the **id**, **key**, and **Emails** attributes. If you want to query all
     * information about a contact, you are advised to call
     * [queryContact]{@link contact.queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>)}
     * to query the contact based on the specified key.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { string } email - Email address of the contact.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryContactsByEmail(context: Context, email: string, callback: AsyncCallback<Array<Contact>>)
     */
    function queryContactsByEmail(email: string, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries a contact based on the specified email. This API uses an asynchronous callback to return the result. The
     * return result of this API includes only the **id**, **key**, and **Emails** attributes. If you want to query all
     * information about a contact, you are advised to call
     * [queryContact]{@link contact.queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>)}
     * to query the contact based on the specified key.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { string } email - Email address of the contact.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryContactsByEmail(context: Context, email: string, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries a contact based on the specified email and holder. This API uses an asynchronous callback to return the
     * result. The return result of this API includes only the **id**, **key**, and **Emails** attributes. If you want to
     * query all information about a contact, you are advised to call
     * [queryContact]{@link contact.queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>)}
     * to query the contact based on the specified key.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { string } email - Email address of the contact.
     * @param { Holder } holder - Application that creates the contacts.If the passed parameter is empty, the system
     *     contact application is used by default.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryContactsByEmail(context: Context, email: string, holder: Holder, callback: AsyncCallback<Array<Contact>>)
     */
    function queryContactsByEmail(email: string, holder: Holder, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries a contact based on the specified email and holder. This API uses an asynchronous callback to return the
     * result. The return result of this API includes only the **id**, **key**, and **Emails** attributes. If you want to
     * query all information about a contact, you are advised to call
     * [queryContact]{@link contact.queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>)}
     * to query the contact based on the specified key.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { string } email - Email address of the contact.
     * @param { Holder } holder - Application that creates the contacts.If the passed parameter is empty, the system
     *     contact application is used by default.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryContactsByEmail(context: Context, email: string, holder: Holder, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries a contact based on the specified email and attributes. This API uses an asynchronous callback to return the
     * result. The return result of this API includes only the **id**, **key**, and **Emails** attributes. If you want to
     * query all information about a contact, you are advised to call
     * [queryContact]{@link contact.queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>)}
     * to query the contact based on the specified key.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { string } email - Email address of the contact.
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryContactsByEmail(context: Context, email: string, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>)
     */
    function queryContactsByEmail(email: string, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries a contact based on the specified email and attributes. This API uses an asynchronous callback to return the
     * result. The return result of this API includes only the **id**, **key**, and **Emails** attributes. If you want to
     * query all information about a contact, you are advised to call
     * [queryContact]{@link contact.queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>)}
     * to query the contact based on the specified key.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { string } email - Email address of the contact.
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryContactsByEmail(context: Context, email: string, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries a contact based on the specified email, holder, and attributes. This API uses an asynchronous callback to
     * return the result. The return result of this API includes only the **id**, **key**, and **Emails** attributes. If
     * you want to query all information about a contact, you are advised to call
     * [queryContact]{@link contact.queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>)}
     * to query the contact based on the specified key.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { string } email - Email address of the contact.
     * @param { Holder } holder - Application that creates the contacts.If the passed parameter is empty, the system
     *     contact application is used by default.
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryContactsByEmail(context: Context, email: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>)
     */
    function queryContactsByEmail(email: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries a contact based on the specified email, holder, and attributes. This API uses an asynchronous callback to
     * return the result. The return result of this API includes only the **id**, **key**, and **Emails** attributes. If
     * you want to query all information about a contact, you are advised to call
     * [queryContact]{@link contact.queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>)}
     * to query the contact based on the specified key.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { string } email - Email address of the contact.
     * @param { Holder } holder - Application that creates the contacts.If the passed parameter is empty, the system
     *     contact application is used by default.
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryContactsByEmail(context: Context, email: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries a contact based on the specified email, holder, and attributes. This API uses a promise to return the
     * result. The return result of this API includes only the **id**, **key**, and **Emails** attributes. If you want to
     * query all information about a contact, you are advised to call
     * [queryContact]{@link contact.queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>)}
     * to query the contact based on the specified key.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { string } email - Email address of the contact.
     * @param { Holder } holder - Application information for a contact. If this parameter is not specified, it is not
     *     used for contact filtering by default.
     * @param { ContactAttributes } attrs - Contact attribute list. If this parameter is not specified, all contact
     *     attributes are queried by default.
     * @returns { Promise<Array<Contact>> } Promise used to return the result, which is an array of queried contacts.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryContactsByEmail(context: Context, email: string, holder?: Holder, attrs?: ContactAttributes)
     */
    function queryContactsByEmail(email: string, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>;
    /**
     * Queries a contact based on the specified email, holder, and attributes. This API uses a promise to return the
     * result. The return result of this API includes only the **id**, **key**, and **Emails** attributes. If you want to
     * query all information about a contact, you are advised to call
     * [queryContact]{@link contact.queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>)}
     * to query the contact based on the specified key.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { string } email - Email address of the contact.
     * @param { Holder } holder - Application information for a contact. If this parameter is not specified, it is not
     *     used for contact filtering by default.
     * @param { ContactAttributes } attrs - Contact attribute list. If this parameter is not specified, all contact
     *     attributes are queried by default.
     * @returns { Promise<Array<Contact>> } Promise used to return the result, which is an array of queried contacts.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryContactsByEmail(context: Context, email: string, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>;
    /**
     * Queries a contact based on the specified phone number. This API uses an asynchronous callback to return the result.
     * The return result of this API includes only the **id**, **key**, and **phoneNumbers** attributes. If you want to
     * query all information about a contact, you are advised to call
     * [queryContact]{@link contact.queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>)}
     * to query the contact based on the specified key. If an application calls this API in the background to obtain
     * contact information, the application must request the corresponding continuous task.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { string } phoneNumber - Phone number of a contact. Only full match is supported, and wildcards are not
     *     supported.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryContactsByPhoneNumber(context: Context, phoneNumber: string, callback: AsyncCallback<Array<Contact>>)
     */
    function queryContactsByPhoneNumber(phoneNumber: string, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries a contact based on the specified phone number. This API uses an asynchronous callback to return the result.
     * The return result of this API includes only the **id**, **key**, and **phoneNumbers** attributes. If you want to
     * query all information about a contact, you are advised to call
     * [queryContact]{@link contact.queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>)}
     * to query the contact based on the specified key. If an application calls this API in the background to obtain
     * contact information, the application must request the corresponding continuous task.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { string } phoneNumber - Phone number of a contact. Only full match is supported, and wildcards are not
     *     supported.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - 1.Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * 2.Internal error. The query resultSet is nullptr. 3.Internal error. The query resultSet is empty.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryContactsByPhoneNumber(context: Context, phoneNumber: string, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries a contact based on the specified phone number and holder. This API uses an asynchronous callback to return
     * the result. The return result of this API includes only the **id**, **key**, and **phoneNumbers** attributes. If
     * you want to query all information about a contact, you are advised to call
     * [queryContact]{@link contact.queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>)}
     * to query the contact based on the specified key. If an application calls this API in the background to obtain
     * contact information, the application must request the corresponding continuous task.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { string } phoneNumber - Phone number of a contact. Only full match is supported, and wildcards are not
     *     supported.
     * @param { Holder } holder - Application that creates the contacts.If the passed parameter is empty, the system
     *     contact application is used by default.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryContactsByPhoneNumber(context: Context, phoneNumber: string, holder: Holder, callback: AsyncCallback<Array<Contact>>)
     */
    function queryContactsByPhoneNumber(phoneNumber: string, holder: Holder, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries a contact based on the specified phone number and holder. This API uses an asynchronous callback to return
     * the result. The return result of this API includes only the **id**, **key**, and **phoneNumbers** attributes. If
     * you want to query all information about a contact, you are advised to call
     * [queryContact]{@link contact.queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>)}
     * to query the contact based on the specified key. If an application calls this API in the background to obtain
     * contact information, the application must request the corresponding continuous task.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { string } phoneNumber - Phone number of a contact. Only full match is supported, and wildcards are not
     *     supported.
     * @param { Holder } holder - Application that creates the contacts.If the passed parameter is empty, the system
     *     contact application is used by default.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - 1.Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * 2.Internal error. The query resultSet is nullptr. 3.Internal error. The query resultSet is empty.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryContactsByPhoneNumber(context: Context, phoneNumber: string, holder: Holder, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries a contact based on the specified phone number and attributes. This API uses an asynchronous callback to
     * return the result. The return result of this API includes only the **id**, **key**, and **phoneNumbers**
     * attributes. If you want to query all information about a contact, you are advised to call
     * [queryContact]{@link contact.queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>)}
     * to query the contact based on the specified key. If an application calls this API in the background to obtain
     * contact information, the application must request the corresponding continuous task.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { string } phoneNumber - Phone number of a contact. Only full match is supported, and wildcards are not
     *     supported.
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryContactsByPhoneNumber(context: Context, phoneNumber: string, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>)
     */
    function queryContactsByPhoneNumber(phoneNumber: string, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries a contact based on the specified phone number and attributes. This API uses an asynchronous callback to
     * return the result. The return result of this API includes only the **id**, **key**, and **phoneNumbers**
     * attributes. If you want to query all information about a contact, you are advised to call
     * [queryContact]{@link contact.queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>)}
     * to query the contact based on the specified key. If an application calls this API in the background to obtain
     * contact information, the application must request the corresponding continuous task.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { string } phoneNumber - Phone number of a contact. Only full match is supported, and wildcards are not
     *     supported.
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - 1.Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * 2.Internal error. The query resultSet is nullptr. 3.Internal error. The query resultSet is empty.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryContactsByPhoneNumber(context: Context, phoneNumber: string, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries a contact based on the specified phone number, holder, and attributes. This API uses an asynchronous
     * callback to return the result. The return result of this API includes only the **id**, **key**, and
     * **phoneNumbers** attributes. If you want to query all information about a contact, you are advised to call
     * [queryContact]{@link contact.queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>)}
     * to query the contact based on the specified key. If an application calls this API in the background to obtain
     * contact information, the application must request the corresponding continuous task.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { string } phoneNumber - Phone number of a contact. Only full match is supported, and wildcards are not
     *     supported.
     * @param { Holder } holder - Application that creates the contacts.If the passed parameter is empty, the system
     *     contact application is used by default.
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryContactsByPhoneNumber(context: Context, phoneNumber: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>)
     */
    function queryContactsByPhoneNumber(phoneNumber: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries a contact based on the specified phone number, holder, and attributes. This API uses an asynchronous
     * callback to return the result. The return result of this API includes only the **id**, **key**, and
     * **phoneNumbers** attributes. If you want to query all information about a contact, you are advised to call
     * [queryContact]{@link contact.queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>)}
     * to query the contact based on the specified key. If an application calls this API in the background to obtain
     * contact information, the application must request the corresponding continuous task.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { string } phoneNumber - Phone number of a contact. Only full match is supported, and wildcards are not
     *     supported.
     * @param { Holder } holder - Application that creates the contacts.If the passed parameter is empty, the system
     *     contact application is used by default.
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @param { AsyncCallback<Array<Contact>> } callback - Indicates the callback for getting the result of the call.
     *     Returns the contact list which user select; returns empty contact list if user not select.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - 1.Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * 2.Internal error. The query resultSet is nullptr. 3.Internal error. The query resultSet is empty.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryContactsByPhoneNumber(context: Context, phoneNumber: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void;
    /**
     * Queries a contact based on the specified phone number, holder, and attributes. This API uses a promise to return
     * the result. The return result of this API includes only the **id**, **key**, and **phoneNumbers** attributes. If
     * you want to query all information about a contact, you are advised to call
     * [queryContact]{@link contact.queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>)}
     * to query the contact based on the specified key. If an application calls this API in the background to obtain
     * contact information, the application must request the corresponding continuous task.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { string } phoneNumber - Phone number of a contact. Only full match is supported, and wildcards are not
     *     supported.
     * @param { Holder } holder - Application information for a contact. If this parameter is not specified, the system
     *     contact application is used by default.
     * @param { ContactAttributes } attrs - Contact attribute list. If this parameter is not specified, all contact
     *     attributes are queried by default.
     * @returns { Promise<Array<Contact>> } Promise used to return the result, which is an array of queried contacts.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryContactsByPhoneNumber(context: Context, phoneNumber: string, holder?: Holder, attrs?: ContactAttributes)
     */
    function queryContactsByPhoneNumber(phoneNumber: string, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>;
    /**
     * Queries a contact based on the specified phone number, holder, and attributes. This API uses a promise to return
     * the result. The return result of this API includes only the **id**, **key**, and **phoneNumbers** attributes. If
     * you want to query all information about a contact, you are advised to call
     * [queryContact]{@link contact.queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>)}
     * to query the contact based on the specified key. If an application calls this API in the background to obtain
     * contact information, the application must request the corresponding continuous task.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { string } phoneNumber - Phone number of a contact. Only full match is supported, and wildcards are not
     *     supported.
     * @param { Holder } holder - Application information for a contact. If this parameter is not specified, the system
     *     contact application is used by default.
     * @param { ContactAttributes } attrs - Contact attribute list. If this parameter is not specified, all contact
     *     attributes are queried by default.
     * @returns { Promise<Array<Contact>> } Promise used to return the result, which is an array of queried contacts.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - 1.Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * 2.Internal error. The query resultSet is nullptr. 3.Internal error. The query resultSet is empty.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryContactsByPhoneNumber(context: Context, phoneNumber: string, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>;
    /**
     * Queries all groups of a contact. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { AsyncCallback<Array<Group>> } callback - Indicates the callback for getting the result of the call. If the operation is
     *     successful, an array of queried groups is returned. If the operation fails, an error code is returned.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryGroups(context: Context, callback: AsyncCallback<Array<Group>>)
     */
    function queryGroups(callback: AsyncCallback<Array<Group>>): void;
    /**
     * Queries all groups of a contact. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { AsyncCallback<Array<Group>> } callback - Indicates the callback for getting the result of the call. If the operation is
     *     successful, an array of queried groups is returned. If the operation fails, an error code is returned.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryGroups(context: Context, callback: AsyncCallback<Array<Group>>): void;
    /**
     * Queries all groups of a contact based on the specified holder. This API uses an asynchronous callback to return the
     * result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Holder } holder - Application that creates the contacts.If the passed parameter is empty, the system
     *     contact application is used by default.
     * @param { AsyncCallback<Array<Group>> } callback - Indicates the callback for getting the result of the call. If the operation is
     *     successful, an array of queried groups is returned. If the operation fails, an error code is returned.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryGroups(context: Context, holder: Holder, callback: AsyncCallback<Array<Group>>)
     */
    function queryGroups(holder: Holder, callback: AsyncCallback<Array<Group>>): void;
    /**
     * Queries all groups of a contact based on the specified holder. This API uses an asynchronous callback to return the
     * result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { Holder } holder - Application that creates the contacts.If the passed parameter is empty, the system
     *     contact application is used by default.
     * @param { AsyncCallback<Array<Group>> } callback - Indicates the callback for getting the result of the call. If the operation is
     *     successful, an array of queried groups is returned. If the operation fails, an error code is returned.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryGroups(context: Context, holder: Holder, callback: AsyncCallback<Array<Group>>): void;
    /**
     * Queries all groups of a contact based on the specified holder. This API uses a promise to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Holder } holder - Application information for a contact. If this parameter is not specified, the system
     *     contact application is used by default.
     * @returns { Promise<Array<Group>> } Promise used to return the result, which is an array of groups.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryGroups(context: Context, holder?: Holder)
     */
    function queryGroups(holder?: Holder): Promise<Array<Group>>;
    /**
     * Queries all groups of a contact based on the specified holder. This API uses a promise to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { Holder } holder - Application information for a contact. If this parameter is not specified, the system
     *     contact application is used by default.
     * @returns { Promise<Array<Group>> } Promise used to return the result, which is an array of groups.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryGroups(context: Context, holder?: Holder): Promise<Array<Group>>;
    /**
     * Queries all applications that have created contacts. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { AsyncCallback<Array<Holder>> } callback - Indicates the callback for getting the result of the call. If the operation is
     *     successful, an array of the queried applications is returned. If the operation fails, an error code is
     *     returned.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryHolders(context: Context, callback: AsyncCallback<Array<Holder>>)
     */
    function queryHolders(callback: AsyncCallback<Array<Holder>>): void;
    /**
     * Queries all applications that have created contacts. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { AsyncCallback<Array<Holder>> } callback - Indicates the callback for getting the result of the call. If the operation is
     *     successful, an array of the queried applications is returned. If the operation fails, an error code is
     *     returned.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryHolders(context: Context, callback: AsyncCallback<Array<Holder>>): void;
    /**
     * Queries all applications that have created contacts. This API uses a promise to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @returns { Promise<Array<Holder>> } Promise used to return the result, which is an array of queried applications.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryHolders(context: Context)
     */
    function queryHolders(): Promise<Array<Holder>>;
    /**
     * Queries all applications that have created contacts. This API uses a promise to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @returns { Promise<Array<Holder>> } Promise used to return the result, which is an array of queried applications.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryHolders(context: Context): Promise<Array<Holder>>;
    /**
     * Queries the key of a contact based on the specified contact ID. This API uses an asynchronous callback to return
     * the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { number } id - Contact ID.
     * @param { AsyncCallback<string> } callback - Indicates the callback for getting the result of the call. If the operation is successful, the
     *     key of the queried contact is returned. If the operation fails, an error code is returned.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryKey(context: Context, id: number, callback: AsyncCallback<string>)
     */
    function queryKey(id: number, callback: AsyncCallback<string>): void;
    /**
     * Queries the key of a contact based on the specified contact ID. This API uses an asynchronous callback to return
     * the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { number } id - Contact ID.
     * @param { AsyncCallback<string> } callback - Indicates the callback for getting the result of the call. If the operation is successful, the
     *     key of the queried contact is returned. If the operation fails, an error code is returned.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified. 2.Parameter verification failed.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryKey(context: Context, id: number, callback: AsyncCallback<string>): void;
    /**
     * Queries the key of a contact based on the specified contact ID and holder. This API uses an asynchronous callback
     * to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { number } id - Contact ID.
     * @param { Holder } holder - Application that creates the contacts.If the passed parameter is empty, the system
     *     contact application is used by default.
     * @param { AsyncCallback<string> } callback - Indicates the callback for getting the result of the call. If the operation is successful, the
     *     key of the queried contact is returned. If the operation fails, an error code is returned.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryKey(context: Context, id: number, holder: Holder, callback: AsyncCallback<string>)
     */
    function queryKey(id: number, holder: Holder, callback: AsyncCallback<string>): void;
    /**
     * Queries the key of a contact based on the specified contact ID and holder. This API uses an asynchronous callback
     * to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { number } id - Contact ID.
     * @param { Holder } holder - Application that creates the contacts.If the passed parameter is empty, the system
     *     contact application is used by default.
     * @param { AsyncCallback<string> } callback - Indicates the callback for getting the result of the call. If the operation is successful, the
     *     key of the queried contact is returned. If the operation fails, an error code is returned.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified. 2.Parameter verification failed.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryKey(context: Context, id: number, holder: Holder, callback: AsyncCallback<string>): void;
    /**
     * Queries the key of a contact based on the specified contact ID and holder. This API uses a promise to return the
     * result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { number } id - Contact ID.
     * @param { Holder } holder - Application information for a contact. If this parameter is not specified, the system
     *     contact application is used by default.
     * @returns { Promise<string> } Promise used to return the result, which is the key of the queried contact.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryKey(context: Context, id: number, holder?: Holder)
     */
    function queryKey(id: number, holder?: Holder): Promise<string>;
    /**
     * Queries the key of a contact based on the specified contact ID and holder. This API uses a promise to return the
     * result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { number } id - Contact ID.
     * @param { Holder } holder - Application information for a contact. If this parameter is not specified, the system
     *     contact application is used by default.
     * @returns { Promise<string> } Promise used to return the result, which is the key of the queried contact.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified. 2.Parameter verification failed.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryKey(context: Context, id: number, holder?: Holder): Promise<string>;
    /**
     * Queries my card. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { AsyncCallback<Contact> } callback - Indicates the callback for getting the result of the call. If the operation is successful,
     *     information about my card is returned. If the operation fails, an error code is returned.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryMyCard(context: Context, callback: AsyncCallback<Contact>)
     */
    function queryMyCard(callback: AsyncCallback<Contact>): void;
    /**
     * Queries my card. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { AsyncCallback<Contact> } callback - Indicates the callback for getting the result of the call. If the operation is successful,
     *     information about my card is returned. If the operation fails, an error code is returned.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryMyCard(context: Context, callback: AsyncCallback<Contact>): void;
    /**
     * Queries my card. (The contact attribute list can be imported.) This API uses an asynchronous callback to return the
     * result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @param { AsyncCallback<Contact> } callback - Indicates the callback for getting the result of the call. If the operation is successful,
     *     information about my card is returned. If the operation fails, an error code is returned.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryMyCard(context: Context, attrs: ContactAttributes, callback: AsyncCallback<Contact>)
     */
    function queryMyCard(attrs: ContactAttributes, callback: AsyncCallback<Contact>): void;
    /**
     * Queries my card. (The contact attribute list can be imported.) This API uses an asynchronous callback to return the
     * result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @param { AsyncCallback<Contact> } callback - Indicates the callback for getting the result of the call. If the operation is successful,
     *     information about my card is returned. If the operation fails, an error code is returned.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryMyCard(context: Context, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void;
    /**
     * Queries my card. (The contact attribute list can be imported.) This API uses a promise to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @returns { Promise<Contact> } Promise used to return the result, which is a contact in my card.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.queryMyCard(context: Context, attrs?: ContactAttributes)
     */
    function queryMyCard(attrs?: ContactAttributes): Promise<Contact>;
    /**
     * Queries my card. (The contact attribute list can be imported.) This API uses a promise to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @returns { Promise<Contact> } Promise used to return the result, which is a contact in my card.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function queryMyCard(context: Context, attrs?: ContactAttributes): Promise<Contact>;
    /**
     * Updates a contact. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.WRITE_CONTACTS
     * @param { Contact } contact - Indicates the contact information. The ID is mandatory and can be obtained through
     *     [selectContacts]{@link contact.selectContacts()}.
     * @param { AsyncCallback<void> } callback - Indicates the callback for getting the result of the call. If the operation is successful, the
     *     ID of the updated contact is returned. If the operation fails, an error code is returned.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.updateContact(context: Context, contact: Contact, callback: AsyncCallback<void>)
     */
    function updateContact(contact: Contact, callback: AsyncCallback<void>): void;
    /**
     * Updates a contact. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.WRITE_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { Contact } contact - Indicates the contact information. The ID is mandatory and can be obtained through
     *     [selectContacts]{@link contact.selectContacts()}.
     * @param { AsyncCallback<void> } callback - Indicates the callback for getting the result of the call. If the operation is successful, the
     *     ID of the updated contact is returned. If the operation fails, an error code is returned.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - 1.Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * 2.Failed to open contact portrait file. 3.Internal error. Invalid contact id. Failed to generate contact profile.
     * 4.Internal error. Failed to save contact portrait. 5.Internal error. Invalid contact rawId.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function updateContact(context: Context, contact: Contact, callback: AsyncCallback<void>): void;
    /**
     * Updates a contact. (The contact attribute list can be imported.) This API uses an asynchronous callback to return
     * the result.
     *
     * @permission ohos.permission.WRITE_CONTACTS
     * @param { Contact } contact - Indicates the contact information. The ID is mandatory and can be obtained through
     *     [selectContacts]{@link contact.selectContacts()}.
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @param { AsyncCallback<void> } callback - Indicates the callback for getting the result of the call. If the operation is successful, the
     *     ID of the updated contact is returned. If the operation fails, an error code is returned.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.updateContact(context: Context, contact: Contact, attrs: ContactAttributes, callback: AsyncCallback<void>)
     */
    function updateContact(contact: Contact, attrs: ContactAttributes, callback: AsyncCallback<void>): void;
    /**
     * Updates a contact. (The contact attribute list can be imported.) This API uses an asynchronous callback to return
     * the result.
     *
     * @permission ohos.permission.WRITE_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { Contact } contact - Indicates the contact information. The ID is mandatory and can be obtained through
     *     [selectContacts]{@link contact.selectContacts()}.
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @param { AsyncCallback<void> } callback - Indicates the callback for getting the result of the call. If the operation is successful, the
     *     ID of the updated contact is returned. If the operation fails, an error code is returned.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - 1.Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * 2.Failed to open contact portrait file. 3.Internal error. Invalid contact id. Failed to generate contact profile.
     * 4.Internal error. Failed to save contact portrait. 5.Internal error. Invalid contact rawId.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function updateContact(context: Context, contact: Contact, attrs: ContactAttributes, callback: AsyncCallback<void>): void;
    /**
     * Updates a contact. (The contact attribute list can be imported.) This API uses a promise to return the result.
     *
     * @permission ohos.permission.WRITE_CONTACTS
     * @param { Contact } contact - Indicates the contact information. The ID is mandatory and can be obtained through
     *     [selectContacts]{@link contact.selectContacts()}.
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.updateContact(context: Context, contact: Contact, attrs?: ContactAttributes)
     */
    function updateContact(contact: Contact, attrs?: ContactAttributes): Promise<void>;
    /**
     * Updates a contact. (The contact attribute list can be imported.) This API uses a promise to return the result.
     *
     * @permission ohos.permission.WRITE_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { Contact } contact - Indicates the contact information. The ID is mandatory and can be obtained through
     *     [selectContacts]{@link contact.selectContacts()}.
     * @param { ContactAttributes } attrs - List of contact attributes. If this parameter is empty, all attribute fields (
     *     including the name, phone number, and email address) of the contact are queried.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - 1.Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * 2.Failed to open contact portrait file. 3.Internal error. Invalid contact id. Failed to generate contact profile.
     * 4.Internal error. Failed to save contact portrait. 5.Internal error. Invalid contact rawId.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function updateContact(context: Context, contact: Contact, attrs?: ContactAttributes): Promise<void>;
    /**
     * Checks whether the ID of this contact is in the local address book. This API uses an asynchronous callback to
     * return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { number } id - Contact ID. Each contact corresponds to one ID.
     * @param { AsyncCallback<boolean> } callback - Indicates the callback for getting the result of the call. If the operation is successful, a
     *     Boolean value is returned. The value **true** indicates that the contact ID is in the local phonebook, and the
     *     value **false** indicates the opposite. If the operation fails, an error code is returned.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.isLocalContact(context: Context, id: number, callback: AsyncCallback<boolean>)
     */
    function isLocalContact(id: number, callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether the ID of this contact is in the local address book. This API uses an asynchronous callback to
     * return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { number } id - Contact ID. Each contact corresponds to one ID.
     * @param { AsyncCallback<boolean> } callback - Indicates the callback for getting the result of the call. If the operation is successful, a
     *     Boolean value is returned. The value **true** indicates that the contact ID is in the local phonebook, and the
     *     value **false** indicates the opposite. If the operation fails, an error code is returned.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified. 2.Parameter verification failed.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function isLocalContact(context: Context, id: number, callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether the ID of this contact is in the local address book. This API uses a promise to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { number } id - Contact ID. Each contact corresponds to one ID.
     * @returns { Promise<boolean> } Promise used to return the result. The value **true** indicates that the contact ID
     *     is in the local phonebook, and the value **false** indicates the opposite.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.isLocalContact(context: Context, id: number)
     */
    function isLocalContact(id: number): Promise<boolean>;
    /**
     * Checks whether the ID of this contact is in the local address book. This API uses a promise to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { number } id - Contact ID. Each contact corresponds to one ID.
     * @returns { Promise<boolean> } Promise used to return the result. The value **true** indicates that the contact ID
     *     is in the local phonebook, and the value **false** indicates the opposite.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified. 2.Parameter verification failed.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function isLocalContact(context: Context, id: number): Promise<boolean>;
    /**
     * Checks whether a contact is included in my card. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { number } id - Contact ID.
     * @param { AsyncCallback<boolean> } callback - Indicates the callback for getting the result of the call. If the operation is successful, a
     *     Boolean value is returned. The value **true** indicates that the contact is included in my card, and the value
     *     **false** indicates the opposite. If the operation fails, an error code is returned.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.isMyCard(context: Context, id: number, callback: AsyncCallback<boolean>)
     */
    function isMyCard(id: number, callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether a contact is included in my card. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { number } id - Contact ID.
     * @param { AsyncCallback<boolean> } callback - Indicates the callback for getting the result of the call. If the operation is successful, a
     *     Boolean value is returned. The value **true** indicates that the contact is included in my card, and the value
     *     **false** indicates the opposite. If the operation fails, an error code is returned.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified. 2.Parameter verification failed.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function isMyCard(context: Context, id: number, callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether a contact is included in my card. This API uses a promise to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { number } id - Contact ID.
     * @returns { Promise<boolean> } Promise used to return the result. The value **true** indicates that the contact is
     *     included in my card, and the value **false** indicates the opposite.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     * @deprecated since 10
     * @useinstead contact.isMyCard(context: Context, id: number)
     */
    function isMyCard(id: number): Promise<boolean>;
    /**
     * Checks whether a contact is included in my card. This API uses a promise to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { number } id - Contact ID.
     * @returns { Promise<boolean> } Promise used to return the result. The value **true** indicates that the contact is
     *     included in my card, and the value **false** indicates the opposite.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified. 2.Parameter verification failed.
     * @syscap SystemCapability.Applications.ContactsData
     * @since 10
     */
    function isMyCard(context: Context, id: number): Promise<boolean>;
    /**
     * Defines the Contact selection options, which specifies whether one contact or
     *     multiple contacts can be selected.
     *
     * @syscap SystemCapability.Applications.Contacts
     * @atomicservice [since 11]
     * @since 10
     */
    interface ContactSelectionOptions {
        /**
         * Whether multiple contacts can be selected. The value **true** indicates that multiple contacts can be selected,
         * and the value **false** indicates that only one contact can be selected. The default value is **false**.
     
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice [since 11]
         * @since 10
         */
        isMultiSelect?: boolean;
        /**
         * Contact selection filter.
         * This API can be used in atomic services since API version 15.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        filter?: ContactSelectionFilter;
        /**
         * Maximum number of contacts. The default value is **10000**. If the value exceeds the maximum number, the default
         * value is used.
         * This API can be used in atomic services since API version 15.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        maxSelectable?: number;
        /**
         * Whether to display contacts by name. The value **true** indicates that contacts are displayed by name, and the
         * value **false** indicates that contacts are displayed by number. The default value is **false**.
         * This API can be used in atomic services since API version 15.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        isDisplayedByName?: boolean;
        /**
         * Indicates whether the contact picker is automatically closed when page routing is performed,
         * for example, when the application is in the background.
         *
         * The default value is false.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        isAutoDismissOnNavigation?: boolean;
    }
    /**
     * Defines a contact.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice [since 11]
     * @since 7
     */
    class Contact {
        /**
         * Default contact ID, value is -1.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly INVALID_CONTACT_ID: -1;
        /**
         * Contact ID, which is automatically generated by the system.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        readonly id?: number;
        /**
         * Contact key, which is automatically generated by the system.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        readonly key?: string;
        /**
         * List of contact attributes.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        contactAttributes?: ContactAttributes;
        /**
         * List of email addresses of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        emails?: Email[];
        /**
         * List of important dates such as birthdays and anniversaries of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        events?: Event[];
        /**
         * List of groups of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        groups?: Group[];
        /**
         * List of instant message addresses of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        imAddresses?: ImAddress[];
        /**
         * List of phone numbers of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        phoneNumbers?: PhoneNumber[];
        /**
         * Contact portrait.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        portrait?: Portrait;
        /**
         * List of postal addresses of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        postalAddresses?: PostalAddress[];
        /**
         * List of relationships with the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        relations?: Relation[];
        /**
         * List of Session Initiation Protocol (SIP) addresses of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        sipAddresses?: SipAddress[];
        /**
         * List of websites of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        websites?: Website[];
        /**
         * Contact name.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        name?: Name;
        /**
         * Contact nickname.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        nickName?: NickName;
        /**
         * Contact notes.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        note?: Note;
        /**
         * Organization of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        organization?: Organization;
    }
    /**
     * Provides a list of contact attributes, which are generally used as arguments.
     * If **null** is passed, all attributes are queried by default.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice [since 11]
     * @since 7
     */
    class ContactAttributes {
        /**
         * Indicates the contact attributes.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        attributes: Attribute[];
    }
    /**
     * Enumerates contact attributes. The enumerated value is of the number type.
     * Create contact data in JSON format:
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice [since 11]
     * @since 7
     */
    enum Attribute {
        /**
         * Important dates such as birthday and anniversaries of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        ATTR_CONTACT_EVENT = 0,
        /**
         * Email address of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        ATTR_EMAIL = 1,
        /**
         * Groups of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        ATTR_GROUP_MEMBERSHIP = 2,
        /**
         * IM addresses of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        ATTR_IM = 3,
        /**
         * Contact name.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        ATTR_NAME = 4,
        /**
         * Contact nickname.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        ATTR_NICKNAME = 5,
        /**
         * Contact notes.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        ATTR_NOTE = 6,
        /**
         * Organization of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        ATTR_ORGANIZATION = 7,
        /**
         * Phone number of a contact. Only full match is supported, and wildcards are not
       *     supported.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        ATTR_PHONE = 8,
        /**
         * Contact portrait.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        ATTR_PORTRAIT = 9,
        /**
         * Postal address of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        ATTR_POSTAL_ADDRESS = 10,
        /**
         * Relationship with the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        ATTR_RELATION = 11,
        /**
         * SIP addresses of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        ATTR_SIP_ADDRESS = 12,
        /**
         * Website that stores the contact information.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        ATTR_WEBSITE = 13
    }
    /**
     * Defines a contact's email.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice [since 11]
     * @since 7
     */
    class Email {
        /**
         * Custom mailbox type, the default value is **0**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly CUSTOM_LABEL: 0;
        /**
         * Home mailbox, the default value is **1**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly EMAIL_HOME: 1;
        /**
         * Work mailbox, the default value is **2**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly EMAIL_WORK: 2;
        /**
         * Other mailbox, the default value is **3**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly EMAIL_OTHER: 3;
        /**
         * Invalid mailbox, the default value is **-1**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly INVALID_LABEL_ID: -1;
        /**
         * Email address of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        email: string;
        /**
         * Name of the mailbox type.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        labelName?: string;
        /**
         * Displayed name of the mailbox.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        displayName?: string;
        /**
         * Mailbox type.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        labelId?: number;
    }
    /**
     * Defines a contact's event.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice [since 11]
     * @since 7
     */
    class Event {
        /**
         * Custom mailbox type, the default value is **0**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly CUSTOM_LABEL: 0;
        /**
         * Custom mailbox type, the default value is **0**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly EVENT_ANNIVERSARY: 1;
        /**
         * Custom mailbox type, the default value is **0**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly EVENT_OTHER: 2;
        /**
         * Birthday event, the default value is **3**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly EVENT_BIRTHDAY: 3;
        /**
         * Invalid mailbox, the default value is **-1**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly INVALID_LABEL_ID: -1;
        /**
         * Event date.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        eventDate: string;
        /**
         * Name of the mailbox type.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        labelName?: string;
        /**
         * Mailbox type.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        labelId?: number;
    }
    /**
     * Defines a contact group.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice [since 11]
     * @since 7
     */
    class Group {
        /**
         * ID of a contact group.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        groupId?: number;
        /**
         * Name of a contact group.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        title: string;
    }
    /**
     * Defines an application that creates the contact.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @since 7
     */
    class Holder {
        /**
         * Bundle name. The default value is **com.ohos.contacts**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @since 7
         */
        readonly bundleName: string;
        /**
         * Application name.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @since 7
         */
        readonly displayName?: string;
        /**
         * Application ID.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @since 7
         */
        holderId?: number;
    }
    /**
     * Enumerates IM addresses.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice [since 11]
     * @since 7
     */
    class ImAddress {
        /**
         * Custom mailbox type, the default value is **0**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly CUSTOM_LABEL: -1;
        /**
         * AIM, the default value is **0**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly IM_AIM: 0;
        /**
         * MSN, the default value is **1**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly IM_MSN: 1;
        /**
         * Yahoo, the default value is **2**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly IM_YAHOO: 2;
        /**
         * Skype, the default value is **3**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly IM_SKYPE: 3;
        /**
         * QQ, the default value is **4**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly IM_QQ: 4;
        /**
         * ICQ, the default value is **6**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly IM_ICQ: 6;
        /**
         * JABBER, the default value is **7**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly IM_JABBER: 7;
        /**
         * Invalid mailbox, the default value is **-1**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly INVALID_LABEL_ID: -2;
        /**
         * IM address.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        imAddress: string;
        /**
         * Name of the mailbox type.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        labelName?: string;
        /**
         * Mailbox type.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        labelId?: number;
    }
    /**
     * Defines a contact's name.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice [since 11]
     * @since 7
     */
    class Name {
        /**
         * Family name.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        familyName?: string;
        /**
         * Family name in pinyin.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        familyNamePhonetic?: string;
        /**
         * Full name of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        fullName: string;
        /**
         * Given name of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        givenName?: string;
        /**
         * Given name of the contact in pinyin.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        givenNamePhonetic?: string;
        /**
         * Middle name of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        middleName?: string;
        /**
         * Middle name of the contact in pinyin.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        middleNamePhonetic?: string;
        /**
         * Prefix of the contact name.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        namePrefix?: string;
        /**
         * Suffix of the contact name.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        nameSuffix?: string;
        /**
         * Whether the contact information contains the name. The value **true** indicates that the contact information
         * contains the name, and the value **false** indicates the opposite.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice
         * @since 22
         */
        hasName?: boolean;
    }
    /**
     * Defines a contact's nickname.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice [since 11]
     * @since 7
     */
    class NickName {
        /**
         * Contact nickname.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        nickName: string;
    }
    /**
     * Defines a contact's note.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice [since 11]
     * @since 7
     */
    class Note {
        /**
         * Notes of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        noteContent: string;
    }
    /**
     * Defines a contact's organization.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice [since 11]
     * @since 7
     */
    class Organization {
        /**
         * Organization name.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        name: string;
        /**
         * Job title.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        title?: string;
    }
    /**
     * Defines a contact's phone number.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice [since 11]
     * @since 7
     */
    class PhoneNumber {
        /**
         * Custom mailbox type, the default value is **0**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly CUSTOM_LABEL: 0;
        /**
         * Home phone, the default value is **1**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly NUM_HOME: 1;
        /**
         * Mobile phone, the default value is **2**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly NUM_MOBILE: 2;
        /**
         * Work phone, the default value is **3**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly NUM_WORK: 3;
        /**
         * Work fax, the default value is **4**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly NUM_FAX_WORK: 4;
        /**
         * Family fax, the default value is **5**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly NUM_FAX_HOME: 5;
        /**
         * Pager, the default value is **6**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly NUM_PAGER: 6;
        /**
         * Other phone type, the default value is **7**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly NUM_OTHER: 7;
        /**
         * Callback phone, the default value is **8**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly NUM_CALLBACK: 8;
        /**
         * Car phone, the default value is **9**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly NUM_CAR: 9;
        /**
         * Company phone, the default value is **10**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly NUM_COMPANY_MAIN: 10;
        /**
         * Integrated Services Digital Network (ISDN) phone, the default value is **11**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly NUM_ISDN: 11;
        /**
         * Main phone, the default value is **12**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly NUM_MAIN: 12;
        /**
         * Other fax phone, the default value is **13**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly NUM_OTHER_FAX: 13;
        /**
         * Wireless phone, the default value is **14**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly NUM_RADIO: 14;
        /**
         * Telex phone, the default value is **15**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly NUM_TELEX: 15;
        /**
         * Teletypewriter (TTY) or Test Driven Development (TDD) phone, the default value is **16**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly NUM_TTY_TDD: 16;
        /**
         * Work mobile phone, the default value is **17**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly NUM_WORK_MOBILE: 17;
        /**
         * Work pager, the default value is **18**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly NUM_WORK_PAGER: 18;
        /**
         * Assistant phone, the default value is **19**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly NUM_ASSISTANT: 19;
        /**
         * MMS phone, the default value is **20**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly NUM_MMS: 20;
        /**
         * Invalid mailbox, the default value is **-1**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly INVALID_LABEL_ID: -1;
        /**
         * Name of the mailbox type.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        labelName?: string;
        /**
         * Phone number.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        phoneNumber: string;
        /**
         * Mailbox type.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        labelId?: number;
    }
    /**
     * Defines a contact's portrait.
     *
     * > **NOTE**
     * >
     * > Since API version 22, contact portraits can be set in URI or [PixelMap]{@link @ohos.multimedia.image:image.PixelMap}
     * > format. (Currently, contact avatars cannot be set through the [addContactViaUI]{@link contact.addContactViaUI} or
     * > [saveToExistingContactViaUI]{@link contact.saveToExistingContactViaUI} API.)
     * >
     * > URI indicates the address of the contact portrait file that can be accessed, and
     * > [PixelMap]{@link @ohos.multimedia.image:image.PixelMap} indicates the [PixelMap]{@link @ohos.multimedia.image:image.PixelMap}
     * > object generated based on the contact portrait resource.
     * >
     * > Since API version 22, the profile picture resource can be read through URI. The resource can be opened only in
     * > [fs.open]{@link @ohos.file.fs:open(path: string, mode?: number)} mode and cannot be directly displayed in the **Image** component using a URI. You need to read
     * > the resource and display it in [PixelMap]{@link @ohos.multimedia.image:image.PixelMap} format.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice [since 11]
     * @since 7
     */
    class Portrait {
        /**
         * Contact portrait in URI format.
     
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        uri: string;
        /**
         * Contact portrait in PixelMap format.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice
         * @since 22
         */
        photo?: image.PixelMap;
    }
    /**
     * Defines a contact's postal address.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice [since 11]
     * @since 7
     */
    class PostalAddress {
        /**
         * Custom mailbox type, the default value is **0**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly CUSTOM_LABEL: 0;
        /**
         * Home address, the default value is **1**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly ADDR_HOME: 1;
        /**
         * Work address, the default value is **2**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly ADDR_WORK: 2;
        /**
         * Other addresses, the default value is **3**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly ADDR_OTHER: 3;
        /**
         * Invalid mailbox, the default value is **-1**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly INVALID_LABEL_ID: -1;
        /**
         * City where the contact is located.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        city?: string;
        /**
         * Country/Region where the contact is located.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        country?: string;
        /**
         * Name of the mailbox type.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        labelName?: string;
        /**
         * Neighbor of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        neighborhood?: string;
        /**
         * Email of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        pobox?: string;
        /**
         * Postal address of the contact.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        postalAddress: string;
        /**
         * Postal code of the region where the contact is located.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        postcode?: string;
        /**
         * Area where the contact is located.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        region?: string;
        /**
         * Street where the contact resides.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        street?: string;
        /**
         * Mailbox type.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        labelId?: number;
    }
    /**
     * Defines a contact's relationship.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice [since 11]
     * @since 7
     */
    class Relation {
        /**
         * Custom relationship, the default value is **0**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly CUSTOM_LABEL: 0;
        /**
         * Assistant, the default value is **1**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly RELATION_ASSISTANT: 1;
        /**
         * Sibling, the default value is **2**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly RELATION_BROTHER: 2;
        /**
         * Child, the default value is **3**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly RELATION_CHILD: 3;
        /**
         * Domestic partner, the default value is **4**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly RELATION_DOMESTIC_PARTNER: 4;
        /**
         * Father, the default value is **5**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly RELATION_FATHER: 5;
        /**
         * Friend, the default value is **6**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly RELATION_FRIEND: 6;
        /**
         * Manager, the default value is **7**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly RELATION_MANAGER: 7;
        /**
         * Mother, the default value is **8**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly RELATION_MOTHER: 8;
        /**
         * Parent, the default value is **9**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly RELATION_PARENT: 9;
        /**
         * Parent, the default value is **9**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly RELATION_PARTNER: 10;
        /**
         * Referrer, the default value is **11**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly RELATION_REFERRED_BY: 11;
        /**
         * Relative, the default value is **12**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly RELATION_RELATIVE: 12;
        /**
         * Relative, the default value is **12**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly RELATION_SISTER: 13;
        /**
         * Spouse, the default value is **14**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly RELATION_SPOUSE: 14;
        /**
         * Invalid relationship, the default value is **-1**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly INVALID_LABEL_ID: -1;
        /**
         * Name of the mailbox type.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        labelName?: string;
        /**
         * Relationship name.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        relationName: string;
        /**
         * Mailbox type.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        labelId?: number;
    }
    /**
     * Defines a contact's SIP address.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice [since 11]
     * @since 7
     */
    class SipAddress {
        /**
         * Custom mailbox type, the default value is **0**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly CUSTOM_LABEL: 0;
        /**
         * Home SIP address, the default value is **1**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly SIP_HOME: 1;
        /**
         * Work SIP address, the default value is **2**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly SIP_WORK: 2;
        /**
         * Other SIP address, the default value is **3**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly SIP_OTHER: 3;
        /**
         * Invalid mailbox, the default value is **-1**.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        static readonly INVALID_LABEL_ID: -1;
        /**
         * Name of the mailbox type.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        labelName?: string;
        /**
         * SIP address.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        sipAddress: string;
        /**
         * Mailbox type.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        labelId?: number;
    }
    /**
     * Defines a contact's website.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice [since 11]
     * @since 7
     */
    class Website {
        /**
         * Website that stores the contact information.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @atomicservice [since 11]
         * @since 7
         */
        website: string;
    }
    /**
     * Defines contact filter options.
     *
     * @syscap SystemCapability.Applications.Contacts
     * @atomicservice
     * @since 15
     */
    interface FilterOptions {
        /**
         * Filter criteria.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        filterCondition: FilterCondition;
        /**
         * Filter value. The default value is **undefined**.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        value?: string | ValueType[];
    }
    /**
     * Defines the contact data filter item.
     *
     * @syscap SystemCapability.Applications.Contacts
     * @atomicservice
     * @since 15
     */
    interface DataFilter {
        /**
         * Contact filtering parameter. Multiple filter options in the array are ORed. The maximum length of the array is 3.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        options: Array<FilterOptions>;
        /**
         * Contact data field.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        field: DataField;
    }
    /**
     * Defines the contact filter criteria. Multiple filter criteria are ORed. If the parameter is an array, the array can
     * contain a maximum of three elements.
     *
     * @syscap SystemCapability.Applications.Contacts
     * @atomicservice
     * @since 15
     */
    interface FilterClause {
        /**
         * Contact data filter item.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        dataItem?: DataFilter;
        /**
         * Contact name.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        name?: Array<FilterOptions>;
        /**
         * Contact ID.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        id?: Array<FilterOptions>;
        /**
         * Focus mode list.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        focusModeList?: Array<FilterOptions>;
    }
    /**
     * Saves the information to an existing contact through UI interaction.. This API uses a promise to return the
     * result.
     *
     * @param { Context } context - Indicates the context of application or capability.
     * @param { Contact } contact - Indicates the contact information.
     * @returns { Promise<number> } Promise used to return the result, which is the contact ID.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @throws { BusinessError } 801 - The specified SystemCapability name was not found.
     * @throws { BusinessError } 16700001 - General error.
     * @throws { BusinessError } 16700101 - Failed to get value from contacts data.
     * @throws { BusinessError } 16700102 - Failed to set value to contacts data.
     * @throws { BusinessError } 16700103 - User cancel.
     * @syscap SystemCapability.Applications.Contacts
     * @atomicservice
     * @since 15
     */
    function saveToExistingContactViaUI(context: Context, contact: Contact): Promise<number>;
    /**
     * Defines the contact selection filter.
     *
     * @syscap SystemCapability.Applications.Contacts
     * @atomicservice
     * @since 15
     */
    interface ContactSelectionFilter {
        /**
         * Filter criteria.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        filterClause: FilterClause;
        /**
         * Filter type.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        filterType: FilterType;
    }
    /**
     * Enumerates contact filter types.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice
     * @since 15
     */
    enum FilterType {
        /**
         * Shows only contacts that meet the filter criteria.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        SHOW_FILTER = 0,
        /**
         * Selects contacts that meet the filter criteria by default.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        DEFAULT_SELECT = 1,
        /**
         * Shows only contacts that meet the filter criteria and selects these contacts by default.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        SHOW_FILTER_AND_DEFAULT_SELECT = 2
    }
    /**
     * Enumerates filter criteria.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice
     * @since 15
     */
    enum FilterCondition {
        /**
         * The corresponding field is equal to a value.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        EQUAL_TO = 1,
        /**
         * The corresponding field is not equal to a value.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        NOT_EQUAL_TO = 2,
        /**
         * The value of the corresponding field is in an array.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        IN = 3,
        /**
         * The corresponding field is not empty.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        IS_NOT_NULL = 0,
        /**
         * The value of the corresponding field is not in an array.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        NOT_IN = 4,
        /**
         * The value of the corresponding field contains a certain value.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        CONTAINS = 5
    }
    /**
     * Enumerates contact data fields.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice
     * @since 15
     */
    enum DataField {
        /**
         * Phone number of the contact.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        PHONE = 1,
        /**
         * Organization of the contact.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        ORGANIZATION = 2,
        /**
         * Email of the contact.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @atomicservice
         * @since 15
         */
        EMAIL = 0
    }
    /**
     * Creates a contact through UI interaction. This API uses a promise to return the result.
     *
     * @param { Context } context - Indicates the context of application or capability.
     * @param { Contact } contact - Indicates the contact information.
     * @returns { Promise<number> } Promise used to return the result, which is the contact ID.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Mandatory parameters are left unspecified.
     * @throws { BusinessError } 801 - The specified SystemCapability name was not found.
     * @throws { BusinessError } 16700001 - General error.
     * @throws { BusinessError } 16700102 - Failed to set value to contacts data.
     * @throws { BusinessError } 16700103 - User cancel.
     * @syscap SystemCapability.Applications.Contacts
     * @atomicservice
     * @since 15
     */
    function addContactViaUI(context: Context, contact: Contact): Promise<number>;
    /**
     * Queries the number of all contacts. This API uses a promise to return the result.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @returns { Promise<number> } Promise used to return the result, which is the number of queried contacts.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 16700001 - General error.
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice
     * @since 22
     */
    function queryContactsCount(context: Context): Promise<number>;
    /**
     * Adds contacts in batches. This API uses a promise to return the result.
     *
     * @permission ohos.permission.WRITE_CONTACTS
     * @param { Context } context - Indicates the context of application or capability.
     * @param { Array<Contact> } contacts - Indicates the contact information. array.
     * @returns { Promise<Array<number>> } Promise used to return the result, which is the ID array of the contacts added in
     *     batches.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 16700001 - General error.
     * @throws { BusinessError } 16700002 - Invalid parameter value.
     * @syscap SystemCapability.Applications.ContactsData
     * @atomicservice
     * @since 23
     */
    function addContacts(context: Context, contacts: Array<Contact>): Promise<Array<number>>;
    /**
     * Checks whether there are call records that meet the specified conditions. By default, call records within the last
     * 6 hours are queried. This API applies only to carrier calls. This API uses a promise to return the result.
     *
     * @permission ohos.permission.CHECK_CALL_LOG
     * @param { Context } context - Indicates the context of the application or capability.
     * @param { string } phoneNumber - Phone number of the contacts.
     * @param { number } minDuration - Minimum call duration, in seconds. The value must be greater than 0.
     * @returns { Promise<boolean> }Promise used to return the result of whether there are call records that meet the
     *     specified conditions. The value **true** indicates that there are such records, and the value **false**
     *     indicates the opposite.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 16700001 - General error.
     * @throws { BusinessError } 16700002 - Invalid parameter value.
     * @syscap SystemCapability.Applications.ContactsData
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    function hasMatchedCallLog(context: Context, phoneNumber: string, minDuration: number): Promise<boolean>;
    /**
     * Checks whether there are call records that meet the specified conditions. This API applies only to carrier calls.
     * This API uses a promise to return the result.
     *
     * @permission ohos.permission.CHECK_CALL_LOG
     * @param { Context } context - Indicates the context of the application or capability.
     * @param { string } phoneNumber - Phone number of the contacts.
     * @param { number } minDuration - Minimum call duration, in seconds. The value must be greater than 0.
     * @param { number } withinTime - Period of time that the start time and end time of calls should be within, in seconds.
     *     This period starts from the current time. A maximum of six hours can be set. If the query duration exceeds six
     *     hours, the query duration is six hours by default.
     * @returns { Promise<boolean> }Promise used to return the result of whether there are call records that meet the
     *     specified conditions. The value **true** indicates that there are such records, and the value **false**
     *     indicates the opposite.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 16700001 - General error.
     * @throws { BusinessError } 16700002 - Invalid parameter value.
     * @syscap SystemCapability.Applications.ContactsData
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    function hasMatchedCallLog(context: Context, phoneNumber: string, minDuration: number, withinTime: number): Promise<boolean>;
    /**
     * Sync multiple contacts in batches into contacts database.
     *
     * A maximum of 400 contacts can be synchronized in batches. The invoking party must be in the foreground.
     *
     * @permission ohos.permission.WRITE_CONTACTS
     * @param { Context } context - Indicates the context of the application or capability.
     * @param { ContactSyncMode } mode - Indicates the type of contact synchronization mode.
     * @param { ContactSyncProgress } progress - Indicates the information about the contact synchronization progress.
     * @param { Array<Contact> } contacts - Indicates the array of contact information to be synchronized into the database.
     * @returns { Promise<Array<number>> } Returns the array of contacts creation results. Valid contact ID (which can be
     * obtained by {@link Contact#getId()}) indicates that the creation was successful.
     * {@link Contact#INVALID_CONTACT_ID} indicates the creation failed.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 16700001 - General error.
     * @throws { BusinessError } 16700002 - Invalid parameter value.
     * @throws { BusinessError } 16700003 - Background usage is prohibited.
     * @throws { BusinessError } 16700004 - The number of contacts exceeds the limit.
     * @throws { BusinessError } 16700103 - User cancel.
     * @syscap SystemCapability.Applications.ContactsData
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    function syncContacts(context: Context, mode: ContactSyncMode, progress: ContactSyncProgress, contacts: Array<Contact>): Promise<Array<number>>;
    /**
     * Queries information about ongoing contact synchronization for the calling application.
     *
     * If the returned contact synchronization information is empty, the invoking party does not synchronize contacts or
     * the contact synchronization is complete.
     *
     * @permission ohos.permission.READ_CONTACTS
     * @param { Context } context - Indicates the context of the application or capability.
     * @returns { Promise<Array<ContactSyncInfo>> } Returns the array of contacts synchronization information for the
     * calling application. Returns null if no contacts are being synchronized.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 16700001 - General error.
     * @syscap SystemCapability.Applications.ContactsData
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    function queryContactSyncInfo(context: Context): Promise<Array<ContactSyncInfo>>;
    /**
     * Imports multiple contacts through UI interaction.
     *
     *  A maximum of 100 contacts can be imported at a time.
     *
     * @param { Context } context - Indicates the context of the application or capability.
     * @param { Array<Contact> } contacts - Indicates the array of contact information to be imported into the database.
     * @returns { Promise<Array<number>> } Returns the array of contacts creation results. Valid contact ID (which can be
     *  obtained by [getId]{@link Contact#getId()}) indicates that the creation was successful.
     * [INVALID_CONTACT_ID]{@link Contact.INVALID_CONTACT_ID} indicates the creation failed.
     * -2 indicates that the user has not selected this contact.
     * @throws { BusinessError } 801 - The specified SystemCapability name was not found.
     * @throws { BusinessError } 16700001 - General error.
     * @throws { BusinessError } 16700002 - Invalid parameter value.
     * @throws { BusinessError } 16700004 - The number of contacts exceeds the limit.
     * @throws { BusinessError } 16700103 - User cancel.
     * @syscap SystemCapability.Applications.Contacts
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    function importContactsViaUI(context: Context, contacts: Array<Contact>): Promise<Array<number>>;
    /**
     * The type of contact synchronization mode.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    enum ContactSyncMode {
        /**
         * Indicates that contacts differing between cloud and local will be inserted or updated in the database.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        MODE_INCREMENTAL = 1,
        /**
         * Indicates that all local contacts will be replaced by cloud contacts.
         *
         * When the cloud overwrite local mode is used for batch synchronization, all local contacts
         *  (excluding third-party contacts) are deleted during the first batch synchronization.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        MODE_CLOUD_BASED = 2
    }
    /**
     * Information about the contact synchronization progress.
     *
     * Contains the sync ID, current batch, and total batch.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    interface ContactSyncProgress {
        /**
         * Indicates the sync identifier used for synchronizing all contacts.
         *
         * The value should start from 0.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        syncId: number;
        /**
         * Indicates the identifier of the current batch of contacts to be synchronized.
         *
         * The range of values is from 1 to totalBatches.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        currentBatch: number;
        /**
         * Indicates the total number of batches of contacts to be synchronized.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        totalBatches: number;
    }
    /**
     * Information about contact synchronization for the calling application.
     *
     * @syscap SystemCapability.Applications.ContactsData
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    interface ContactSyncInfo {
        /**
         * The contact synchronization mode.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        mode: ContactSyncMode;
        /**
         * Indicates the sync identifier used for synchronizing all contacts.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        syncId: number;
        /**
         * Indicates the array of batch identifiers for contacts that have been synchronized successfully.
         *
         * The range of values is from 1 to totalBatches.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        completedBatches: Array<number>;
        /**
         * Indicates the total number of batches of contacts to be synchronized.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        totalBatches: number;
        /**
         * Indicates the latest timestamp the contacts were synchronized in milliseconds.
         *
         * @syscap SystemCapability.Applications.ContactsData
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        lastSyncTime: number;
    }
}
export default contact;

```
