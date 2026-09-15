# @ohos.arkui.StateManagement.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2024-2025 Huawei Device Co., Ltd.
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
 * The state management module provides data storage, persistent data management, UIAbility data storage, and
 * environment state and tools required by applications.
 *
 * T and S in this topic represent the types as described below.
 *
 * | Type  | Description                                    |
 * | ---- | -------------------------------------- |
 * | T    | Class, number, boolean, string, and arrays of these types.|
 * | S    | number, boolean, string.                |
 *
 * @file State Management
 * @kit ArkUI
 */
import contextConstant from '@ohos.app.ability.contextConstant';
import collections from '@arkts.collections';
/**
 * Obtains the default constructor.
 *
 * @returns { T } Default constructor.
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 12
 */
export declare type StorageDefaultCreator<T> = () => T;
/**
 * Represents a class constructor that accepts arbitrary arguments.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 12
 */
export interface TypeConstructorWithArgs<T> {
    /**
     * Creates and returns an instance of the specified type T.
     *
     * @param { any } args - Function arguments.
     * @returns { T } Instance of the T type.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    new (...args: any): T;
}
/**
 * Defines the parameter type for **globalConnect**.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @atomicservice
 * @since 18
 */
export class ConnectOptions<T extends object> {
    /**
     * Specified type.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @atomicservice
     * @since 18
     */
    type: TypeConstructorWithArgs<T>;
    /**
     * Input key. If no value is passed in, the type name is used as the key.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @atomicservice
     * @since 18
     */
    key?: string;
    /**
     * Default constructor. You are advised to pass this parameter. If **globalConnect** is connected to the key for the
     * first time, an error is reported if this parameter is not passed in.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @atomicservice
     * @since 18
     */
    defaultCreator?: StorageDefaultCreator<T>;
    /**
     * Encryption level, ranging from EL1 to EL5 (corresponding to the value from 0 to 4). For details, see
     * [Encryption Levels](docroot://application-models/application-context-stage.md#obtaining-and-modifying-encryption-levels).
     * If no value is passed in, EL2 is used by default. Storage paths vary based on the encryption levels. If the input
     * value of encryption level is not in the range of **0** to **4**, a crash occurs.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @atomicservice
     * @since 18
     */
    areaMode?: contextConstant.AreaMode;
}
/**
 * For details about how to use AppStorageV2, see
 * [AppStorageV2: Storing Application-wide UI State](docroot://ui/state-management/arkts-new-appstoragev2.md).
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 12
 */
export declare class AppStorageV2 {
    /**
     * Stores key-value pair data in the application memory. If the given key already exists in
     * [AppStorageV2](docroot://ui/state-management/arkts-new-appstoragev2.md), the corresponding value is returned.
     * Otherwise, a default value is constructed using the default value constructor and returned.
     *
     * @param { TypeConstructorWithArgs<T> } type - Type. If no key is specified, the name of the type is used as the key.
     * @param { string | StorageDefaultCreator<T> } [keyOrDefaultCreator] - Key, or constructor for obtaining the default
     *     value. The default value is **undefined**.
     * @param { StorageDefaultCreator<T> } [defaultCreator] - Constructor for obtaining the default value. The default
     *     value is **undefined**.
     * @returns { T | undefined } Returns data if the creation or data acquisition from AppStorageV2 is successful;
     *     returns **undefined** otherwise.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    static connect<T extends object>(type: TypeConstructorWithArgs<T>, keyOrDefaultCreator?: string | StorageDefaultCreator<T>, defaultCreator?: StorageDefaultCreator<T>): T | undefined;
    /**
     * Removes the specified key-value pair from [AppStorageV2](docroot://ui/state-management/arkts-new-appstoragev2.md).
     * If the specified key does not exist in AppStorageV2, the removal will fail.
     *
     * @param { string | TypeConstructorWithArgs<T> } keyOrType - Key to be removed. If a type is specified, the key to be
     *     removed is the name of that type.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    static remove<T>(keyOrType: string | TypeConstructorWithArgs<T>): void;
    /**
     * Obtains all keys in [AppStorageV2](docroot://ui/state-management/arkts-new-appstoragev2.md).
     *
     * @returns { Array<string> } All keys stored in AppStorageV2.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    static keys(): Array<string>;
}
/**
 * Defines a callback used to return the cause of the persistence failure.
 *
 * @param { string } key - Key of the error.
 * @param { 'quota' | 'serialization' | 'unknown' } reason - Reason of the error.
 * @param { string } message - Extra information about the error.
 * @param { string } [oldValue] - Old serialized data stored on the disk when deserialization fails. [since 26.0.0]
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 12
 */
export declare type PersistenceErrorCallback = (key: string, reason: 'quota' | 'serialization' | 'unknown', message: string, oldValue?: string) => void;
/**
 * Defines the types of persistent collection data supported by **globalConnect** using the generic type of the input
 * parameter of **globalConnect**.
 *
 * @unionmember { Array<S> } The value is of the array type.
 * @unionmember { Map<string | number, S> } The value is of the Map type.
 * @unionmember { Set<S> } The value is of the Set type.
 * @unionmember { collections.Array<S> } The value is of the collections.Array type.
 * @unionmember { collections.Map<string | number, S> } The value is of the collections.Map type.
 * @unionmember { collections.Set<S> } The value is of the collections.Set type.
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @atomicservice
 * @since 23
 */
export declare type CollectionType<S> = Array<S> | Map<string | number, S> | Set<S> | collections.Array<S> | collections.Map<string | number, S> | collections.Set<S>;
/**
 * Defines the parameter type for the
 * [globalConnect]{@link PersistenceV2.globalConnect<T extends CollectionType<S>, S extends object>( type: ConnectOptionsCollections<T, S> | ConnectOptions<T> )}
 * API. **ConnectOptionsCollections** is inherited from [ConnectOptions\<T\>]{@link ConnectOptions}. You can use the
 * **ConnectOptionsCollections** input parameter to persist container data (such as **Array\<S>**).
 *
 * The following shows the examples of **StorageDefaultCreator\<T>** and **StorageDefaultCreator\<S>**:
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @atomicservice
 * @since 23
 */
export class ConnectOptionsCollections<T extends CollectionType<S>, S extends object> extends ConnectOptions<T> {
    /**
     * Persists container data. **defaultSubCreator** should be provided together with **defaultCreator**; otherwise, the
     * container data cannot be persisted. The collection item type **S** must be the same as the return type of
     * **defaultSubCreator**. If **defaultSubCreator** is provided but **defaultCreator** is not, the persistence fails.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    defaultCreator?: StorageDefaultCreator<T>;
    /**
     * Persists container data. If the return value of **defaultSubCreator** is **undefined** or **null**, the persistence
     * fails. When a user-defined class collection (such as **Array<ClassA>**) is persisted, the generic type **T** in
     * **defaultCreator** is **Array<ClassA>**, and **S** in **defaultSubCreator** is **ClassA**.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    defaultSubCreator?: StorageDefaultCreator<S>;
}
/**
 * Inherits from [AppStorageV2]{@link AppStorageV2}. For details, see
 * [PersistenceV2: Persisting Application State](docroot://ui/state-management/arkts-new-persistencev2.md).
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 12
 */
export declare class PersistenceV2 extends AppStorageV2 {
    /**
     * Stores key-value pair data on the application disk. If the given key already exists in
     * [PersistenceV2](docroot://ui/state-management/arkts-new-persistencev2.md), the corresponding value is returned.
     * Otherwise, a default value is constructed using the default value constructor and returned. If **globalConnect** is
     * used for an [\@ObservedV2](docroot://ui/state-management/arkts-new-observedV2-and-trace.md) decorated object,
     * changes to the object's [\@Trace](docroot://ui/state-management/arkts-new-observedV2-and-trace.md) properties will
     * trigger automatic refresh of the associated object, while changes to non-@Trace properties will not. If necessary,
     * the [PersistenceV2.save]{@link PersistenceV2#save} API can be called to store the data manually.
     *
     * @param { ConnectOptions<T> } type - Connection settings.
     * @returns { T | undefined } Returns the data if creation or acquisition is successful; otherwise, returns
     *     **undefined**.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @atomicservice
     * @since 18
     */
    static globalConnect<T extends object>(type: ConnectOptions<T>): T | undefined;
    /**
     * Stores key-value pair data on the application disk. Supports the persistence of the following collection types:
     * [Array, Map, Set, Date, collections.Array, collections.Map, and collections.Set](docroot://ui/state-management/arkts-new-persistencev2.md#types-supported-by-globalconnect).
     * Note that when persisting data of the **Array\<ClassA>** type, you need to call
     * [makeObserved]{@link UIUtils#makeObserved} to make the returned object observed. Multi-level nested sets are not
     * supported. For example, **Array<Array\<ClassA>>** persistence is not supported.
     *
     * @param { ConnectOptionsCollections<T, S> | ConnectOptions<T> } type - Passed **globalConnect** parameters. For
     *     details, see the description of **ConnectOptions** and **ConnectOptionsCollections**.
     *     <br>If **defaultSubCreator** is provided in **ConnectOptionsCollections**, **defaultCreator** must be provided.
     *     Otherwise, the persistence fails. The collection item type S must be the same as the return type of
     *     **defaultSubCreator**. If the return types are inconsistent, an error will be reported during compilation.
     * @returns { T | undefined } Returns the data if creation or acquisition is successful; otherwise, returns
     *     **undefined**.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    static globalConnect<T extends CollectionType<S>, S extends object>(type: ConnectOptionsCollections<T, S> | ConnectOptions<T>): T | undefined;
    /**
     * Persists the specified key-value pair data once.
     *
     * @param { string | TypeConstructorWithArgs<T> } keyOrType - Key to be persisted. If a type is specified, the key for
     *     persistence is the name of the type.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    static save<T>(keyOrType: string | TypeConstructorWithArgs<T>): void;
    /**
     * Called when persistence fails.
     *
     * @param { PersistenceErrorCallback | undefined } callback - Callback called when persistence fails.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    static notifyOnError(callback: PersistenceErrorCallback | undefined): void;
}
/**
 * Represents a class constructor.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 12
 */
export interface TypeConstructor<T> {
    /**
     * Creates and returns an instance of the specified type T.
     *
     * @returns { T } Instance of the T type.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    new (): T;
}
/**
 * Defines the attribute decorator, which is used to decorate attributes of the custom class in a nested class.
 *
 * @param { TypeConstructor<T> } type - Type of the class property.
 * @returns { PropertyDecorator } Property decorator.
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 12
 */
export declare type TypeDecorator = <T>(type: TypeConstructor<T>) => PropertyDecorator;
/**
 * Define Type PropertyDecorator, adds type information to an object.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 12
 * @noninterop
 */
export declare const Type: TypeDecorator;
/**
 * Provides APIs for handling data transformations related to state management.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 12
 */
export declare class UIUtils {
    /**
     * Obtains the original object from a proxy object wrapped by the state management framework. For details, see
     * [getTarget API: Obtaining Original Objects](docroot://ui/state-management/arkts-new-getTarget.md).
     *
     * @param { T } source - Source object.
     * @returns { T } Original object of the source after the proxy added by the state management framework is removed.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    static getTarget<T extends object>(source: T): T;
    /**
     * Converts ordinary unobservable data into observable data. For details, see
     * [makeObserved API: Changing Unobservable Data to Observable Data](docroot://ui/state-management/arkts-new-makeObserved.md).
     *
     * @param { T } source - Source object. It supports classes not decorated by @Observed or @ObservedV2, objects
     *     returned by **JSON.parse**, and classes decorated by @Sendable.
     *     <br>Array, Map, Set, and Date types are supported.
     *     <br>collections.Array, collections.Set, and collections.Map are supported.
     *     <br>For details, see
     *     [makeObserved API: Changing Unobservable Data to Observable Data](docroot://ui/state-management/arkts-new-makeObserved.md).
     * @returns { T } Observable data.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    static makeObserved<T extends object>(source: T): T;
    /**
     * Wraps an unobservable object into an object that is observable by V1 state management. This API is equivalent to @
     * Observed and can be used to initialize @ObjectLink.
     *
     * This API can be used together with [enableV2Compatibility]{@link UIUtils#enableV2Compatibility} in scenarios where
     * state management V1 and V2 are used together. For details, see
     * [Mixed Use of State Management V1 and V2 (API Version 19 and Later)](docroot://ui/state-management/arkts-v1-v2-mixusage.md).
     *
     * @param { T } source - Data source. Common classes, Array, Map, Set, and Date types are supported.
     *     <br>[@arkts.collections]{@link @arkts.collections:collections} (ArkTS containers) and
     *     classes decorated with [@Sendable](docroot://arkts-utils/arkts-sendable.md) are not supported.
     *     <br>**undefined** and **null** are not supported. V2 state management data and
     *     the return value of [makeObserved]{@link UIUtils#makeObserved} are not supported.
     * @returns { T } For supported input parameter types, returns data observable by V1 state management. For unsupported
     *     input parameter types, returns the data source object itself.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 19
     */
    static makeV1Observed<T extends object>(source: T): T;
    /**
     * Enables V1 state variables to be observable in @ComponentV2. This API is primarily used in scenarios where V1 and V
     * 2 state management are mixed. For details, see
     * [Mixed Use of State Management V1 and V2 (API Version 19 and Later)](docroot://ui/state-management/arkts-v1-v2-mixusage.md).
     *
     * @param { T } source - Data source, which must be V1 state data.
     * @returns { T } If the data source is V1 state data, returns data that can be observed in @ComponentV2; otherwise,
     *     returns the data source itself.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 19
     */
    static enableV2Compatibility<T extends object>(source: T): T;
    /**
     * Dynamically adds a listener to the state variable of state management V2. For details, see
     * [addMonitor and clearMonitor APIs: Dynamically Adding and Removing Listeners](docroot://ui/state-management/arkts-new-addMonitor-clearMonitor.md).
     *
     * @param { object } target - Target object. Only
     *     [@ComponentV2](docroot://ui/state-management/arkts-create-custom-components.md#componentv2) and
     *     [@ObservedV2](docroot://ui/state-management/arkts-new-observedV2-and-trace.md) instances are supported.
     *     <br>If an unsupported type is provided, a runtime error is thrown.
     * @param { string | string[] } path - Name path of the variable to be listened for. You can specify a path or pass a
     *     string array to specify multiple variable paths to be listened for at a time.
     *     <br>Only string and string array are supported. If an unsupported type is provided, a runtime error is thrown.
     * @param { MonitorCallback } monitorCallback - Listener function registered with the corresponding state variable.
     *     That is, when the state variable corresponding to the path changes, a specific function is called.
     *     <br>If an unsupported type is provided, a runtime error is thrown.
     * @param { MonitorOptions} [options] - Configuration item of the listener. For details, see
     *     [MonitorOptions]{@link MonitorOptions}. By default, the asynchronous callback is used.
     * @throws { BusinessError } 130000 - The target is not a custom component instance or V2 class instance.
     * @throws { BusinessError } 130001 - The path is invalid.
     * @throws { BusinessError } 130002 - monitorCallback is not a function or an anonymous function.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    static addMonitor(target: object, path: string | string[], monitorCallback: MonitorCallback, options?: MonitorOptions): void;
    /**
     * Deletes the listener added to the state variable of the state management V2 by calling the
     * [addMonitor]{@link UIUtils#addMonitor} API. For details, see
     * [addMonitor and clearMonitor APIs: Dynamically Adding and Removing Listeners](docroot://ui/state-management/arkts-new-addMonitor-clearMonitor.md).
     *
     * @param { object } target - Target object. Only
     *     [@ComponentV2](docroot://ui/state-management/arkts-create-custom-components.md#componentv2) and
     *     [@ObservedV2](docroot://ui/state-management/arkts-new-observedV2-and-trace.md) instances are supported.
     *     <br>If an unsupported type is provided, a runtime error is thrown.
     * @param { string | string[] } path - Name path of the variable to be deleted. You can specify a path or pass a
     *     string array to delete the listener functions of multiple state variables at a time.
     *     <br>Only string and string array are supported. If an unsupported type is provided, a runtime error is thrown.
     * @param { MonitorCallback } [monitorCallback] - Listener function to be deleted.
     *     <br>If this parameter is not specified, all listener functions registered with the variable corresponding to
     *     the path will be deleted.
     *     <br>If an unsupported type is provided, a runtime error is thrown.
     * @throws { BusinessError } 130000 - The target is not a custom component instance or V2 class instance.
     * @throws { BusinessError } 130001 - The path is invalid.
     * @throws { BusinessError } 130002 - monitorCallback is not a function or an anonymous function.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    static clearMonitor(target: object, path: string | string[], monitorCallback?: MonitorCallback): void;
    /**
     * Creates a read-only one-way data binding instance, which is used to construct the arguments of the **Binding** type
     * in the [\@Builder](docroot://ui/state-management/arkts-builder.md) function.
     *
     * @param { GetterCallback<T> } getter - Callback used to obtain the value. Each value access triggers this function
     *     to obtain the latest value.
     * @returns { Binding<T> } Returns a read-only one-way data binding instance with a **value** attribute, which is used
     *     to obtain the currently bound value. The value can only be read and cannot be directly modified.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    static makeBinding<T>(getter: GetterCallback<T>): Binding<T>;
    /**
     * Creates a mutable two-way data binding instance, which is used to construct the argument of the **MutableBinding**
     * type in the \@Builder function.
     *
     * @param { GetterCallback<T> } getter - Callback used to obtain the value. Each value access triggers this function
     *     to obtain the latest value.
     * @param { SetterCallback<T> } [setter] - Callback used to update the value. Each modification to **.value** triggers
     *     this function.
     * @returns { MutableBinding<T> } Returns a two-way data binding instance with a **value** attribute, which allows you
     *     to read and modify data. If the value is set, the system checks whether the value type matches the generic type
     *     **T**.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    static makeBinding<T>(getter: GetterCallback<T>, setter: SetterCallback<T>): MutableBinding<T>;
    /**
     * Synchronously updates a specified state variable. This API receives a closure function and updates only the
     * internal modifications, including the updates of [@Computed](docroot://ui/state-management/arkts-new-computed.md)
     * and [@Monitor](docroot://ui/state-management/arkts-new-monitor.md) decorators, and re-rendering of the UI nodes.
     * For details, see
     * [applySync/flushUpdates/flushUIUpdates APIs: Synchronous Update](docroot://ui/state-management/arkts-new-applySync-flushUpdates-flushUIUpdates.md).
     *
     * @param { TaskCallback } task - Closure function. The state variable modification generated in the closure will be
     *     executed synchronously.
     * @returns { T } Return value obtained by executing the closure function.
     * @throws { BusinessError } 140001 - The function is not allowed to be called in @Computed
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 22
     */
    static applySync<T>(task: TaskCallback): T;
    /**
     * Synchronously updates all state variable modifications before this API call, including the updates
     * of @Computed and @Monitor decorators, and re-rendering of the UI nodes. For details, see
     * [applySync/flushUpdates/flushUIUpdates APIs: Synchronous Update](docroot://ui/state-management/arkts-new-applySync-flushUpdates-flushUIUpdates.md).
     *
     * @throws { BusinessError } 140001 - The function is not allowed to be called in @Computed
     * @throws { BusinessError } 140002 - The function is not allowed to be called in @Monitor
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 22
     */
    static flushUpdates(): void;
    /**
     * Processes all state variable modifications before this API call and synchronizes the
     * [dirty](docroot://ui/state-management/arkts-state-management-introduce.md#triggering-updates) UI nodes. However, it
     * does not synchronize the execution of @Computed and @Monitor decorators. For details, see
     * [applySync/flushUpdates/flushUIUpdates APIs: Synchronous Update](docroot://ui/state-management/arkts-new-applySync-flushUpdates-flushUIUpdates.md).
     *
     * @throws { BusinessError } 140001 - The function is not allowed to be called in @Computed
     * @throws { BusinessError } 140002 - The function is not allowed to be called in @Monitor
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 22
     */
    static flushUIUpdates(): void;
    /**
     * Determines whether a data object can be observed and returns the observation result. For details, see
     * [canBeObserved API: Determining Whether an Object Can Be Observed](docroot://ui/state-management/arkts-new-canBeObserved.md).
     *
     * @param { T } source - Data object to be determined. Array, Map, Set, and Date types are supported.
     *     <br>For details, see
     *     [canBeObserved API: Determining Whether an Object Can Be Observed](docroot://ui/state-management/arkts-new-canBeObserved.md).
     * @returns { ObservedResult } Returns a result about whether the object can be observed.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    static canBeObserved<T extends object>(source: T): ObservedResult;
    /**
     * Obtains the [lifecycle of a custom component]{@link ComponentInit}.
     *
     * @param { T } customComponent - Custom component instance.
     * @returns { CustomComponentLifecycle } Lifecycle instance of a custom component obtained.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    static getLifecycle<T extends BaseCustomComponent>(customComponent: T): CustomComponentLifecycle;
    /**
     * Obtains [CustomComponentContext]{@link CustomComponentContext} of the given @Component(V1) or @ComponentV2.
     * **CustomComponentContext** can be used to access the reuse pool of the component. For details about the reuse pool,
     * see
     * [Global Reuse: Centralized Component Recycling and Reuse](docroot://ui/state-management/arkts-global-reuse-pool.md).
     *
     * @param { T } customComponent - @Component or @ComponentV2 whose context is to be obtained.
     * @returns { CustomComponentContext } Context object of the given component instance.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    static getCustomComponentContext<T extends BaseCustomComponent>(customComponent: T): CustomComponentContext;
}
/**
 * Defines a synchronous callback.
 *
 * @returns { T } Return value obtained by executing the closure function.
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 22
 */
declare type TaskCallback = () => T;
/**
 * Listener callback function of the [IMonitor]{@link IMonitor} type.
 *
 * @param { IMonitor} monitorValue - Change information passed by the callback.
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 20
 */
export declare type MonitorCallback = (monitorValue: IMonitor) => void;
/**
 * Defines the optional parameters for [addMonitor]{@link UIUtils#addMonitor}, which are used to configure the callback
 * type and whether to enable the wildcard capability.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 20
 */
export interface MonitorOptions {
    /**
     * Whether the current callback is a synchronous callback. **true**: The current callback is a synchronous callback.
     * **false** (default value): The current callback is an asynchronous callback.
     *
     * @default false
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    isSynchronous?: boolean;
    /**
     * Whether to enable the wildcard capability for this **addMonitor**. **true** to enable the wildcard capability, and
     * **false** means the opposite. The default value is **false**. If the wildcard capability is disabled but the path
     * contains wildcards, the path is considered invalid.
     *
     * @default false
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    enableWildcard?: boolean;
}
/**
 * Defines a callback used to obtain a value.
 *
 * @returns { T } Value of the T type.
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 20
 */
export declare type GetterCallback<T> = () => T;
/**
 * Defines a callback used to set a value.
 *
 * @param { T } newValue - Parameter of the T type.
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 20
 */
export declare type SetterCallback<T> = (newValue: T) => void;
/**
 * Represents the generic class for read-only data binding, which can bind data of any type.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 20
 */
export declare class Binding<T> {
    /**
     * Obtains a bound value.
     *
     * @returns { T } Returns a value whose type is the generic parameter T, which is the same as the type defined by
     *     **Binding<T>**.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    get value(): T;
}
/**
 * Represents a generic class for mutable data binding, which allows the read and write operations on the bound value
 * and provides complete **get** and **set** accessors.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 20
 */
export declare class MutableBinding<T> {
    /**
     * Obtains a bound value.
     *
     * @returns { T } Returns a value whose type is the generic parameter T, which is the same as the type defined by
     *     **Binding<T>**.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    get value(): T;
    /**
     * Provides the **set** accessor to set a new value for the current bound value. The **set** accessor must be provided
     * when the **MutableBinding** class instance is constructed. Otherwise, a runtime error will be thrown when the
     * **set** accessor is triggered.
     *
     * @param { T } newValue - New value, whose type is the generic parameter T, which is the same as the type defined in
     *     **MutableBinding<T>**.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    set value(newValue: T);
}
/**
 * Provides the result of whether the object can be observed.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 23
 */
export interface ObservedResult {
    /**
     * Whether an object can be observed.
     *
     * **true**: The object can be observed.
     *
     * **false**: The object cannot be observed.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    isObserved: boolean;
    /**
     * Reason for the object's observability.
     *
     * For the object that cannot be observed: The object itself cannot be observed.
     *
     * For the object that can be observed:
     *
     * 1. The V1 object is decorated by the [@Observed](docroot://ui/state-management/arkts-observed-and-objectlink.md)
     *     decorator or the object is converted by the [makeV1Observed]{@link UIUtils#makeV1Observed} method.
     * 2. The V1 object is decorated by the [@Observed](docroot://ui/state-management/arkts-observed-and-objectlink.md)
     *     decorator or the object is converted by the [makeV1Observed]{@link UIUtils#makeV1Observed} method, but the object is not used by the UI component.
     * 3. The V1 object is converted by the [enableV2Compatibility]{@link UIUtils#enableV2Compatibility} method
     *     and then passed to the V2 component.
     * 4. The V1 object is converted by the [enableV2Compatibility]{@link UIUtils#enableV2Compatibility} method
     *     and then passed to the V2 component, but is not used by the V2 component.
     * 5. The V2 object is decorated by the
     *     [@ObservedV2 or @Trace](docroot://ui/state-management/arkts-new-observedV2-and-trace.md) decorator.
     * 6. The V2 object is converted by the [makeObserved]{@link UIUtils#makeObserved} method.
     * 7. The V2 object is of the Array, Map, Set, or Date type.
     * 8. The V2 object is decorated by the
     *     [@ObservedV2 or @Trace](docroot://ui/state-management/arkts-new-observedV2-and-trace.md) decorator,
     *     but is not used by the UI component.
     * 9. The V2 object is converted by the [makeObserved]{@link UIUtils#makeObserved} method, but the object is not
     *     used by the UI component.
     * 10. The V2 object is of the Array, Map, Set, or Date type, but is not used by the UI component.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    reason: string;
    /**
     * Decorator and component information associated with the observable object. If the object cannot be observed, the
     * array is empty.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    decoratorInfo: Array<DecoratorInfo>;
}
/**
 * Defines the decorator and component information associated with the observable object.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 23
 */
export interface DecoratorInfo {
    /**
     * Decorator name.
     *
     * For a V1 object, the value is the name of the decorator associated with the object.
     *
     * If the V1 object uses [@Track](docroot://ui/state-management/arkts-track.md), the value is **'@Track'**.
     *
     * If the V2 object uses [@Trace](docroot://ui/state-management/arkts-new-observedV2-and-trace.md), the value is
     * **'@Trace'**.
     *
     * If the V2 object uses [makeObserved]{@link UIUtils#makeObserved}, the value is **'MakeObserved'**.
     *
     * If the V2 object uses [enableV2Compatibility]{@link UIUtils#enableV2Compatibility}, the value is
     * **'EnableV2Compatible'**.
     *
     * If the V2 object uses built-in data, the value is **'ProxyObservedV2'**.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    decoratorName: string;
    /**
     * Name of the attribute decorated by the decorator.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    stateVariableName: string;
    /**
     * Component or object name.
     *
     * For a V1 object, the component name is returned.
     *
     * For a V1 object whose properties are decorated by the [@Track](docroot://ui/state-management/arkts-track.md)
     * decorator, the object name is returned.
     *
     * For a V2 object, the object name is returned.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    owningComponentOrClassName: string;
    /**
     * Component ID.
     *
     * For a V1 object, the component ID is returned.
     *
     * For the V1 object whose properties are decorated by the [@Track](docroot://ui/state-management/arkts-track.md)
     * decorator or for the V2 object, **-1** is returned instead of the component ID.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    owningComponentId: number;
    /**
     * Information about the component that uses the observable object. If the object is not used in any UI, an empty
     * array is returned.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    dependentInfo: Array<ElementInfo>;
}
/**
 * Defines information about the components associated with the observable object, including system components and
 * custom components.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 23
 */
export interface ElementInfo {
    /**
     * Component name.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    elementName: string;
    /**
     * Component ID.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    elementId: number;
}
/**
 * **CustomComponentLifecycle** monitors the lifecycle changes of a custom component.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 23
 */
export declare interface CustomComponentLifecycle {
    /**
     * getCurrentState(): CustomComponentLifecycleState
     *
     * @returns { CustomComponentLifecycleState } - Current lifecycle status of a custom component.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    getCurrentState(): CustomComponentLifecycleState;
    /**
     * Registers a listener for the lifecycle of a custom component. Lifecycle changes will trigger the lifecycle callback in the listener.
     *
     * @param { CustomComponentLifecycleObserver } observer - Listener for a custom component.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    addObserver(observer: CustomComponentLifecycleObserver): void;
    /**
     * Removes a listener for the lifecycle of a custom component. After the listener is removed,
     * the lifecycle callback in the listener is not triggered even if the component status changes.
     *
     * @param { CustomComponentLifecycleObserver } observer - Listener for a custom component.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    removeObserver(observer: CustomComponentLifecycleObserver): void;
}
/**
 * Observes lifecycle status changes of a custom component,
 * and triggers the lifecycle callback in the listener when detecting lifecycle status changes.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 23
 */
export declare interface CustomComponentLifecycleObserver {
    /**
     * Called after a new instance of the custom component is created and before its **build()** function is executed.
     * You can modify the status variables in this phase.
     * Its function is similar to that of [aboutToAppear]{@link BaseCustomComponent.aboutToAppear},
     * but it is triggered under the constraints of the custom component state machine.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    aboutToAppear?(): void;
    /**
     * Called after a new instance of the custom component is created and its **build()** function is executed.
     * You can use this callback for actions that do not affect the UI, such as event data reporting.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    onDidBuild?(): void;
    /**
     * Called before the custom component is destroyed. You are advised not to change state variables
     * in the **aboutToDisappear** function. Modifying the **@Link** decorated variable may lead to unstable
     * application behavior. This function is similar to the earlier **aboutToDisappear** function, which is triggered
     * under the constraints of the custom component state machine. Therefore, this function is added for compatibility.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    aboutToDisappear?(): void;
    /**
     * Called when a reusable custom component is re-added to the node tree from the cache to receive the component
     * constructors. The value of **params** is not **undefined** in the reuse callback of the V1 component. The value
     * of **params** is **undefined** in the reuse callback of the V2 component.
     *
     * @param { Record<string, Object | undefined |null> } [params] - The value is not **undefined** in the reuse
     *     callback of the V1 component and is **undefined** in the reuse callback of the V2 component.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    aboutToReuse?(params?: Record<string, Object | undefined | null>): void;
    /**
     * Called after necessary component recycling operations defined in the application are performed.
     * Then, the component is frozen to prevent UI updates when the component is in the recycling pool.
     * At last, the **aboutToRecycle** function recursively traverses all child components,
     * and the **aboutToRecycle** function in each recycled child component will be called.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    aboutToRecycle?(): void;
}
/**
 * Current lifecycle status of a custom component.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 23
 */
export declare enum CustomComponentLifecycleState {
    /**
     * Initial.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    INIT = 0,
    /**
     * To build.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    APPEARED = 1,
    /**
     * Built.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    BUILT = 2,
    /**
     * Recycled.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    RECYCLED = 3,
    /**
     * Deleted.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    DISAPPEARED = 4
}
/**
 * Decorates a function that is called when the initialization of a custom component is about to complete.
 * You can register a listener at this time.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 23
 */
export declare const ComponentInit: MethodDecorator;
/**
 * Decorates a function that is called after a new instance of the custom component is created and
 * before the **build()** function is executed. This callback is similar to **aboutToAppear**. The difference is that
 * the **@ComponentAppear** callback is triggered only when the custom component is in the
 * **[CustomComponentLifecycleState]{@link CustomComponentLifecycleState}.INIT** state. The state variable can be
 * changed in **@ComponentAppear**. The change will take effect in the subsequent **build()** function execution.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 23
 */
export declare const ComponentAppear: MethodDecorator;
/**
 * Decorates a function that is called after the **build()** function of the custom component is executed
 * for the first time, that is, when the component status changes from **CustomComponentLifecycleState.APPEARED**
 * to **CustomComponentLifecycleState.BUILT**. You can use this callback for actions that do not affect the UI,
 * such as tracking data reporting.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 23
 */
export declare const ComponentBuilt: MethodDecorator;
/**
 * Decorates a function that is called when a reusable custom component is re-added to the node tree from the cache,
 * that is, when the component status changes from the **CustomComponentLifecycleState.RECYCLED** to
 * **CustomComponentLifecycleState.BUILT** phase, to receive the constructor parameters. At last, the function
 * decorated by **@ComponentReuse** recursively traverses all child components, and the **@ComponentReuse**
 * decorated function in each reused child component will be called.
 *
 * > **NOTE**
 * >
 * > -  The value of **params** is not **undefined** in the callback of the reused state management V1 component.
 * >
 * > -  The value of **params** is **undefined** in the callback of the reused state management V2 component.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 23
 */
export declare const ComponentReuse: MethodDecorator;
/**
 * Decorates a function that is called when the necessary recycling operations defined in the application
 * are performed. That is, this function is triggered when the component status changes
 * from **CustomComponentLifecycleState.BUILT** to **CustomComponentLifecycleState.RECYCLED**.
 * At last, the function decorated by **@ComponentRecycle** recursively traverses all child components,
 * and the **@ComponentRecycle** decorated function in each recycled child component will be called.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 23
 */
export declare const ComponentRecycle: MethodDecorator;
/**
 * The function decorated is invoked before a custom component becomes active.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export declare const ComponentActive: MethodDecorator;
/**
 * The function decorated is invoked before a custom component becomes inactive.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export declare const ComponentInactive: MethodDecorator;
/**
 * Decorates a function that is called when the custom component is destructed. You are advised not to
 * change state variables in this function. Modifying the **@Link** decorated variable may lead to
 * unstable application behavior.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 23
 */
export declare const ComponentDisappear: MethodDecorator;
/**
 * The **CustomComponentContext** class provides access to component-level services, including the reuse pool. You can
 * obtain an instance through [UIUtils.getCustomComponentContext]{@link UIUtils#getCustomComponentContext}.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export declare interface CustomComponentContext {
    /**
     * Obtains the global reuse pool of the custom component. If the component does not configure the reuse pool through
     * **reusePool** and **poolAccepts**, **undefined** is returned. For details about how to configure the global reuse
     * pool, see
     * [Global Reuse: Centralized Component Recycling and Reuse](docroot://ui/state-management/arkts-global-reuse-pool.md).
     *
     * @returns { IReusePool | undefined } If a global reuse pool is configured for the current component, the reuse pool
     *     information is returned. Otherwise, **undefined** is returned.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    getReusePool(): IReusePool | undefined;
}
/**
 * The **IReusePool** API provides the features related to the global reuse pool of a custom component.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export declare interface IReusePool {
    /**
     * Obtains the information about the recycling instance of a given reusable component type in this reuse pool.
     *
     * @param { ReusableComponentConstructor } constructor - Name of the reusable custom component to be queried.
     * @param { string } [reuseId] - Reuse ID for filtering. If specified, only the information about the reuse pool with
     *     the reuse ID is returned. The default value is **undefined**, indicating that information about all reuse pools
     *     is returned.
     * @returns { IReusableInfo[] | IReusableInfo | undefined } If the reuse pool is not configured to accept the given
     *     component type, **undefined** is returned.
     *     <br>If **reuseId** is specified, a single **IReusableInfo** is returned (even if **count** is set to **0** and
     *     **maxCount** is set to the default value).
     *     <br>If **reuseId** is not specified and the reusable component does not use **reuseId**, a single **IReusableInfo**
     *     is returned.
     *     <br>If **reuseId** is not specified but the reusable component uses **reuseId**, an **Array<IReusableInfo>** is
     *     returned, providing a separate entry for each **reuseId** that has a positive value of **count** or a non-
     *     default value of **maxCount** as well as an entry of **reuseId: undefined**.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    getReusableInfo(constructor: ReusableComponentConstructor, reuseId?: string): IReusableInfo[] | IReusableInfo | undefined;
    /**
     * Pre-creates @Reusable/@ReusableV2 decorated components and places them in this reuse pool.
     *
     * @param { WrappedBuilder<[]> } builder - **WrappedBuilder** that contains the @Builder decorated function to be
     *     executed *n* times. Each execution should create one or more @Reusable/@ReusableV2 decorated components.
     * @param { number } times - Number of times the @Builder decorated function is executed.
     * @returns { Promise<void> } Promise parsed when the idle task is successfully completed. This promise returns no
     *     value.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    preRender(builder: WrappedBuilder<[
    ]>, times: number): Promise<void>;
}
/**
 * The **IReusableInfo** API provides information about the current number and maximum number of reusable components
 * managed by the reuse pool.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export declare interface IReusableInfo {
    /**
     * Current number of @Reuseable/V2 component instances in pool.
     * count is usually <= maxCount. It is allowed to be larger for short time
     * because pool clean happens asynchronously.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    readonly count: number;
    /**
     * Maximum number of permissible @Reusable/V2 component instances.
     * The default value is 100, the maximum value is 200.
     * Setting to a negative number will be treated as setting to 0.
     * Setting to a number greater than maximum will be treated as setting to 200.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    maxCount: number;
    /**
     * reuse id.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    readonly reuseId?: string;
}
/**
 * Function for initializing the reusable custom component.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
declare type ReusableComponentConstructor = Function;

```
