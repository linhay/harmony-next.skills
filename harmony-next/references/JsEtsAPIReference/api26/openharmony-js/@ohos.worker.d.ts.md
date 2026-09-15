# @ohos.worker.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021 Huawei Device Co., Ltd.
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
 * @kit ArkTS
 */
/**
 * Provides options that can be set for the Worker instance to create.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 7
 */
export interface WorkerOptions {
    /**
     * Mode in which the Worker instance executes the script. The module type is not supported yet. The default value is
     * classic.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    type?: 'classic' | 'module';
    /**
     * Name of the Worker thread. The default value is undefined.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    name?: string;
    /**
     * Whether sharing of the Worker instance is enabled. Currently, sharing is not supported.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 7
     */
    shared?: boolean;
    /**
     * Priority of the Worker thread.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 22]
     * @atomicservice
     * @since 18
     */
    priority?: ThreadWorkerPriority;
}
/**
 * Enumerates the priorities available for Worker threads.
 * For details about the mappings between priorities and QoS levels, see QoS Level.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 22]
 * @atomicservice
 * @since 18
 */
export enum ThreadWorkerPriority {
    /**
     * High priority, corresponding to QOS_USER_INITIATED.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 22]
     * @atomicservice
     * @since 18
     */
    HIGH = 0,
    /**
     * Medium priority, corresponding to QOS_DEFAULT.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 22]
     * @atomicservice
     * @since 18
     */
    MEDIUM = 1,
    /**
     * Low priority, corresponding to QOS_UTILITY.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 22]
     * @atomicservice
     * @since 18
     */
    LOW = 2,
    /**
     * Background priority, corresponding to QOS_BACKGROUND.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 22]
     * @atomicservice
     * @since 18
     */
    IDLE = 3,
    /**
     * Deadline priority, corresponding to QOS_DEADLINE_REQUEST.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 22]
     * @atomicservice
     * @since 20
     */
    DEADLINE = 4,
    /**
     * Vip priority, corresponding to QOS_USER_INTERACTIVE.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 22]
     * @atomicservice
     * @since 20
     */
    VIP = 5
}
/**
 * Enumerates the priorities available for EventHandler.
 * For details about the mappings between priorities and EventHandler levels, see EventHandler Level.
 *
 * @syscap SystemCapability.Utils.Lang
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export enum Priority {
    /**
     * IMMEDIATE priority, corresponding to EventHandler IMMEDIATE priority.
     *
     * @syscap SystemCapability.Utils.Lang
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    IMMEDIATE = 1,
    /**
     * HIGH priority, corresponding to EventHandler HIGH priority.
     *
     * @syscap SystemCapability.Utils.Lang
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    HIGH = 2,
    /**
     * Low priority, corresponding to EventHandler LOW priority.
     *
     * @syscap SystemCapability.Utils.Lang
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    LOW = 3,
    /**
     * IDLE priority, corresponding to EventHandler IDLE priority.
     *
     * @syscap SystemCapability.Utils.Lang
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    IDLE = 4
}
/**
 * Defines the event.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 7
 */
export interface Event {
    /**
     * Type of the Event.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 7
     */
    readonly type: string;
    /**
     * Timestamp (accurate to millisecond) when the event is created. This parameter is not supported yet.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 7
     */
    readonly timeStamp: number;
}
/**
 * Provides detailed information about the exception that occurs during worker execution. The ErrorEvent class inherits
 * from Event.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 7
 */
export interface ErrorEvent extends Event {
    /**
     * Information about the exception.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    readonly message: string;
    /**
     * File where the exception is located.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    readonly filename: string;
    /**
     * Serial number of the line where the exception is located.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    readonly lineno: number;
    /**
     * Serial number of the column where the exception is located.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    readonly colno: number;
    /**
     * Type of the exception.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    readonly error: Object;
}
/**
 * Holds the data transferred between worker threads.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 12]
 * @since 7
 */
export interface MessageEvent<T> extends Event {
    /**
     * Data transferred when an exception occurs.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 7
     */
    readonly data: T;
}
/**
 * Holds the data transferred between Worker threads.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
export interface MessageEvents extends Event {
    /**
     * Data transferred when an exception occurs.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    readonly data: any;
}
/**
 * Defines the object for which the ownership is to be transferred during data transfer. The object must be an
 * ArrayBuffer instance.
 * After the ownership is transferred, the object becomes unavailable in the sender and can be used only in the
 * receiver.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 7
 */
export interface PostMessageOptions {
    /**
     * ArrayBuffer array used to transfer the ownership. The array cannot be null.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    transfer?: Object[];
}
/**
 * Implements event listening.
 *
 * @syscap SystemCapability.Utils.Lang
 * @since 7
 * @deprecated since 9
 * @useinstead ohos.worker.WorkerEventListener
 */
export interface EventListener {
    /**
     * Specifies the callback to invoke.
     *
     * @param { Event } evt - evt evt Event class for the callback to invoke.
     * @returns { void | Promise<void> }
     * @syscap SystemCapability.Utils.Lang
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.worker.WorkerEventListener.(event: Event)
     */
    (evt: Event): void | Promise<void>;
}
/**
 * Implements event listening.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 12]
 * @since 9
 */
export interface WorkerEventListener {
    /**
     * Specifies the callback function to be invoked.
     *
     * @param { Event } event - Event class for the callback to invoke.
     * @returns { void | Promise<void> }
     * @throws { BusinessError } 10200004 - The Worker instance is not running.
     * @throws { BusinessError } 10200005 - The called API is not supported in the worker thread.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 9
     */
    (event: Event): void | Promise<void>;
}
/**
 * Type of message, only "message" and "messageerror".
 *
 * @unionmember { 'message' }
 * @unionmember { 'messageerror' }
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 12]
 * @since 7
 */
type MessageType = 'message' | 'messageerror';
/**
 * Specific event features.
 *
 * @syscap SystemCapability.Utils.Lang
 * @since 7
 * @deprecated since 9
 * @useinstead ohos.worker.WorkerEventTarget
 */
export interface EventTarget {
    /**
     * Adds an event listener to the worker.
     *
     * @param { string } type - type Type of the event to listen for.
     * @param { EventListener } listener - listener Callback to invoke when an event of the specified type occurs.
     * @syscap SystemCapability.Utils.Lang
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.worker.WorkerEventTarget.addEventListener
     */
    addEventListener(type: string, listener: EventListener): void;
    /**
     * Dispatches the event defined for the worker.
     *
     * @param { Event } event - event Event to dispatch.
     * @returns { boolean }
     * @syscap SystemCapability.Utils.Lang
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.worker.WorkerEventTarget.dispatchEvent
     */
    dispatchEvent(event: Event): boolean;
    /**
     * Removes an event defined for the worker.
     *
     * @param { string } type - type Type of the event for which the event listener is removed.
     * @param { EventListener } callback - callback Callback of the event listener to remove.
     * @syscap SystemCapability.Utils.Lang
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.worker.WorkerEventTarget.removeEventListener
     */
    removeEventListener(type: string, callback?: EventListener): void;
    /**
     * Removes all event listeners for the worker.
     *
     * @syscap SystemCapability.Utils.Lang
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.worker.WorkerEventTarget.removeAllListener
     */
    removeAllListener(): void;
}
/**
 * Processes worker listening events.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
export interface WorkerEventTarget {
    /**
     * Adds an event listener for the Worker thread. This API provides the same functionality as on9+.
     *
     * @param { string } type - type Type of the event to listen for.
     * @param { WorkerEventListener } listener - listener Callback to invoke when an event of the specified type occurs.
  
     * @throws { BusinessError } 10200004 - The Worker instance is not running.
     * @throws { BusinessError } 10200005 - The called API is not supported in the worker thread.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 9
     */
    addEventListener(type: string, listener: WorkerEventListener): void;
    /**
     * Dispatches the event defined for the Worker thread.
     *
     * @param { Event } event - event Event to dispatch.
     * @returns { boolean }
  
     * @throws { BusinessError } 10200004 - The Worker instance is not running.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 9
     */
    dispatchEvent(event: Event): boolean;
    /**
     * Removes an event listener for the Worker thread. This API provides the same functionality as off9+.
     *
     * @param { string } type - type Type of the event for which the event listener is to be removed.
     * @param { WorkerEventListener } [callback] - callback Callback to invoke when the listener is removed.
  
     * @throws { BusinessError } 10200004 - The Worker instance is not running.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 9
     */
    removeEventListener(type: string, callback?: WorkerEventListener): void;
    /**
     * Removes all event listeners for the Worker thread.
     *
     * @throws { BusinessError } 10200004 - The Worker instance is not running.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 9
     */
    removeAllListener(): void;
}
/**
 * Specifies the worker thread running environment, which is isolated from the host thread environment.
 *
 * @syscap SystemCapability.Utils.Lang
 * @since 7
 * @deprecated since 9
 * @useinstead ohos.worker.GlobalScope
 */
declare interface WorkerGlobalScope extends EventTarget {
    /**
     * Worker name specified when there is a new worker.
     *
     * @syscap SystemCapability.Utils.Lang
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.worker.GlobalScope.name
     */
    readonly name: string;
    /**
     * The onerror attribute of parentPort specifies
     * the event handler to be called when an exception occurs during worker execution.
     * The event handler is executed in the worker thread.
     *
     * @syscap SystemCapability.Utils.Lang
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.worker.GlobalScope.onerror
     */
    onerror?: (ev: ErrorEvent) => void;
    /**
     * Specify the type attribute for self.
     *
     * @syscap SystemCapability.Utils.Lang
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.worker.GlobalScope.self
     */
    readonly self: WorkerGlobalScope & typeof globalThis;
}
/**
 * Implements the running environment of the Worker thread. The GlobalScope class inherits from WorkerEventTarget.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare interface GlobalScope extends WorkerEventTarget {
    /**
     * Worker instance specified when there is a new Worker instance.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    readonly name: string;
    /**
     * Called when an exception occurs during worker execution. The event handler is executed in the Worker thread.
     * In the callback function, the ev type is ErrorEvent, indicating the received abnormal data.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    onerror?: (ev: ErrorEvent) => void;
    /**
     * GlobalScope itself.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    readonly self: GlobalScope & typeof globalThis;
}
/**
 * Specifies the worker thread running environment, which is isolated from the host thread environment
 *
 * @syscap SystemCapability.Utils.Lang
 * @since 7
 * @deprecated since 9
 * @useinstead ohos.worker.ThreadWorkerGlobalScope
 */
export interface DedicatedWorkerGlobalScope extends WorkerGlobalScope {
    /**
     * The onmessage attribute of parentPort specifies the event handler
     * to be called then the worker thread receives a message sent by
     * the host thread through worker postMessage.
     * The event handler is executed in the worker thread.
     *
     * @syscap SystemCapability.Utils.Lang
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.worker.ThreadWorkerGlobalScope.onmessage
     */
    onmessage?: (this: DedicatedWorkerGlobalScope, ev: MessageEvent) => void;
    /**
     * The onmessage attribute of parentPort specifies the event handler
     * to be called then the worker receives a message that cannot be deserialized.
     * The event handler is executed in the worker thread.
     *
     * @syscap SystemCapability.Utils.Lang
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.worker.ThreadWorkerGlobalScope.onmessageerror
     */
    onmessageerror?: (this: DedicatedWorkerGlobalScope, ev: MessageEvent) => void;
    /**
     * Close the worker thread to stop the worker from receiving messages
     *
     * @syscap SystemCapability.Utils.Lang
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.worker.ThreadWorkerGlobalScope.close
     */
    close(): void;
    /**
     * Send a message to be host thread from the worker
     *
     * @param { Object } messageObject - messageObject Data to be sent to the worker
     * @param { Transferable[] } transfer - transfer array cannot contain null.
     * @syscap SystemCapability.Utils.Lang
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.worker.ThreadWorkerGlobalScope.postMessage
     */
    postMessage(messageObject: Object, transfer: Transferable[]): void;
    /**
     * Send a message to be host thread from the worker
     *
     * @param { Object } messageObject - messageObject Data to be sent to the worker
     * @param { PostMessageOptions } [options] - options Option can be set for postmessage.
     * @syscap SystemCapability.Utils.Lang
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.worker.ThreadWorkerGlobalScope.postMessage
     */
    postMessage(messageObject: Object, options?: PostMessageOptions): void;
    /**
     * Send a message to host thread from the worker
     *
     * @param { Object } messageObject - messageObject Data to be sent to the worker
     * @param { ArrayBuffer[] } transfer - transfer array cannot contain null.
     * @syscap SystemCapability.Utils.Lang
     * @since 9
     * @deprecated since 9
     * @useinstead ohos.worker.ThreadWorkerGlobalScope.postMessage
     */
    postMessage(messageObject: Object, transfer: ArrayBuffer[]): void;
}
/**
 * Implements communication between the Worker thread and the host thread. The postMessage API is used to send messages
 * to the host thread, and the close API is used to terminate the Worker thread. The ThreadWorkerGlobalScope class
 * inherits from GlobalScope9+.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
export interface ThreadWorkerGlobalScope extends GlobalScope {
    /**
     * Called when the Worker thread receives a message sent by the host thread through postMessage.
     * The event handler is executed in the Worker thread. In the callback function, this indicates the caller's
     * ThreadWorkerGlobalScope, and the ev type is MessageEvents, indicating the received message data.
     *
     * @throws { BusinessError } 10200004 - The Worker instance is not running.
     * @throws { BusinessError } 10200005 - The called API is not supported in the worker thread.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    onmessage?: (this: ThreadWorkerGlobalScope, ev: MessageEvents) => void;
    /**
     * Called when the Worker thread receives a message that cannot be deserialized. The event handler is executed
     * in the Worker thread. In the callback function, this indicates the caller's ThreadWorkerGlobalScope,
     * and the ev type is MessageEvents, indicating the received message data.
     *
     * @throws { BusinessError } 10200004 - The Worker instance is not running.
     * @throws { BusinessError } 10200005 - The called API is not supported in the worker thread.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    onmessageerror?: (this: ThreadWorkerGlobalScope, ev: MessageEvents) => void;
    /**
     * Terminates the Worker thread to stop it from receiving messages.
     *
     * @throws { BusinessError } 10200004 - The Worker instance is not running.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    close(): void;
    /**
     * Sends a message from the Worker thread to the host thread by transferring object ownership.
     *
     * @param { Object } messageObject - Data to be sent to the host thread. The data object must be sequenceable.
     *     For details about the supported parameter types, see Sequenceable Data Types.
     * @param { ArrayBuffer[] } transfer - ArrayBuffer instance holding an array of objects for which the ownership
     *     is transferred to the host thread. After the transfer, the objects are available only in the host thread. The
     *     array cannot be null.
     * @throws { BusinessError } 10200004 - The Worker instance is not running.
     * @throws { BusinessError } 10200006 - An exception occurred during serialization.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    postMessage(messageObject: Object, transfer: ArrayBuffer[]): void;
    /**
     * Sends a message from the Worker thread to the host thread by transferring object ownership or copying data.
     *
     * @param { Object } messageObject - Data to be sent to the host thread. The data object must be sequenceable.
     *     For details about the supported parameter types, see Sequenceable Data Types.
     * @param { PostMessageOptions } [options] - If this parameter is specified, it functions the same as ArrayBuffer[].
     *     Specifically, the ownership of the objects in the array is transferred to the host thread and becomes
     *     unavailable in the Worker thread.
     *     The objects are available only in the host thread. If this parameter is not specified, the default value
     *     undefined is used,
     *     and information is transferred to the host thread by copying data.
     * @throws { BusinessError } 10200004 - The Worker instance is not running.
     * @throws { BusinessError } 10200006 - An exception occurred during serialization.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    postMessage(messageObject: Object, options?: PostMessageOptions): void;
    /**
     * Sends a message from the Worker thread to the host thread. In the message, a sendable object is passed by reference
     * ,
     * and a non-sendable object is passed by serialization.
     *
     * @param { Object } message - Data to be sent to the host thread. The data object must be sequenceable or sendable.
     *     For details about the supported sequenceable types, see Sequenceable Data Types.
     *     For details about the supported sendable types, see Sendable Data Types.
     * @param { ArrayBuffer[] } [transfer] - ArrayBuffer instance holding an array of objects for which the ownership is
     *     transferred to the host thread. After the transfer, the objects are available only in the host thread.
     *     The array cannot be null. The default value is an empty array.
     * @throws { BusinessError } 10200004 - The Worker instance is not running.
     * @throws { BusinessError } 10200006 - An exception occurred during serialization.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    postMessageWithSharedSendable(message: Object, transfer?: ArrayBuffer[]): void;
    /**
     * Calls a method of an object registered with the host thread. This API is called by the Worker thread.
     * The invoking is synchronous for the Worker thread and asynchronous for the host thread. The return value is
     * transferred through serialization.
     *
     * @param { string } instanceName - Key used for registration. It is used to search for the object in the host thread.
     * @param { string } methodName - Name of the method to call. Note that the method cannot be modified by async or
     *     generator,
     *     or return results asynchronously by using the asynchronous mechanism at the bottom layer. Otherwise, an
     *     exception is thrown.
     * @param { number } timeout - Maximum duration that the current synchronous invoking waits, in ms.
     *     The value is an integer ranging from 1 to 5000. The value 0 means that the 5000 ms duration is used.
     *     The value should be an integer.
     *     <br>Unit:ms.
     * @param { Object[] } args - the method argument called on registered globalCallObject.
     * @returns { Object } Return the result of method if it has a return value, otherwise return void.
     * @throws { BusinessError } 10200004 - The Worker instance is not running.
     * @throws { BusinessError } 10200006 - An exception occurred during serialization.
     * @throws { BusinessError } 10200019 - The globalCallObject is not registered.
     * @throws { BusinessError } 10200020 - The method to be called is not callable or is an async method or a generator.
     * @throws { BusinessError } 10200021 - The global call exceeds the timeout.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    callGlobalCallObjectMethod(instanceName: string, methodName: string, timeout: number, ...args: Object[]): Object;
    /**
     * Sends a message from the Worker thread to the main thread by transferring object ownership,
     * and inserted into the head of the corresponding priority queue.Except for the worker thread to the main thread,
     * this interface has the same function as postMessage.
     *
     * @param { Object } message - Data to be sent to the main thread. The data object must be sequenceable or sendable.
     *     For details about the supported sequenceable types, see Sequenceable Data Types.
     *     For details about the supported sendable types, see Sendable Data Types.
     * @param { Priority } priority - Priority of the Worker EventHandler.
     * @param { ArrayBuffer[] } [transfer] - ArrayBuffer instance holding an array of objects for which the ownership
     *     is transferred to the main thread. After the transfer, the objects are available only in the main thread.
     *     The array cannot be null.
     * @throws { BusinessError } 10200004 - The Worker instance is not running.
     * @throws { BusinessError } 10200006 - An exception occurred during serialization.
     * @syscap SystemCapability.Utils.Lang
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    postMessageAtFront?(message: Object, priority: Priority, transfer?: ArrayBuffer[]): void;
}
/**
 * The event handler to be called when an exception occurs during worker execution.
 *
 * @param { ErrorEvent } err - Error event class,
 *     which provides detailed information about the exception occurred during Worker execution.
 * @returns { void }
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 22]
 * @atomicservice
 * @since 18
 */
type ErrorCallback = (err: ErrorEvent) => void;
/**
 * JS cross-thread communication tool
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 7
 */
declare namespace worker {
    /**
     * Before using the following APIs, you must create a ThreadWorker instance. The ThreadWorker class inherits from
     * WorkerEventTarget.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    class ThreadWorker implements WorkerEventTarget {
        /**
         * A constructor used to create a ThreadWorker instance.
         *
         * @param { string } scriptURL - URL of the Worker thread file. For details about the rules, see Precautions for
         *     File URLs.
         * @param { WorkerOptions } [options] - Options that can be set for the Worker instance.
         * @throws { BusinessError } 10200003 - Worker initialization failed.
         * @throws { BusinessError } 10200007 - The worker file path is invalid.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        constructor(scriptURL: string, options?: WorkerOptions);
        /**
         * Called when the Worker thread exits. The event handler is executed in the host thread. In the callback function,
         * the code value is of the number type, where the value 1 indicates abnormal exit and 0 indicates normal exit.The default value is undefined.
         *
         * @throws { BusinessError } 10200004 - The Worker instance is not running.
         * @throws { BusinessError } 10200005 - The called API is not supported in the worker thread.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        onexit?: (code: number) => void;
        /**
         * Called when an exception occurs during worker execution. The event handler is executed in the host thread.
         * In the callback function, the err type is ErrorEvent, indicating the received abnormal data.
         *
         * @throws { BusinessError } 10200004 - The Worker instance is not running.
         * @throws { BusinessError } 10200005 - The called API is not supported in the worker thread.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        onerror?: (err: ErrorEvent) => void;
        /**
         * Called when an exception occurs within the lifecycle of the Worker thread.
         * The event handler is executed in the host thread.
         *
         * onerror can capture only exceptions generated by synchronous methods within the onmessage callback.
         * It cannot capture exceptions from multithreaded callbacks or modularization-related exceptions.
         * Once an exception is captured, the Worker thread will proceed to the destruction process and cannot be used.
         *
         * onAllErrors can capture global exceptions generated during the onmessage callback, timer callback,
         * and file execution of the Worker thread. After an exception is captured by onAllErrors,
         * the Worker thread remains alive and can continue to be used.
         * You are advised to use onAllErrors instead of onerror.
         *
         * @throws { BusinessError } 10200004 - The Worker instance is not running.
         * @throws { BusinessError } 10200005 - The called API is not supported in the worker thread.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 22]
         * @atomicservice
         * @since 18
         */
        onAllErrors?: ErrorCallback;
        /**
         * Called when the host thread receives a message sent by the Worker thread through workerPort.postMessage.
         * The event handler is executed in the host thread. In the callback function, the event type is MessageEvents,
         * indicating the received message data.
         *
         * @throws { BusinessError } 10200004 - The Worker instance is not running.
         * @throws { BusinessError } 10200005 - The called API is not supported in the worker thread.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        onmessage?: (event: MessageEvents) => void;
        /**
         * Called when the Worker thread receives a message that cannot be serialized. The event handler is executed in the
         * host thread.
         * In the callback function, the event type is MessageEvents, indicating the received message data.
         *
         * @throws { BusinessError } 10200004 - The Worker instance is not running.
         * @throws { BusinessError } 10200005 - The called API is not supported in the worker thread.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        onmessageerror?: (event: MessageEvents) => void;
        /**
         * Sends a message from the host thread to the Worker thread by transferring object ownership.
         *
         * @param { Object } message - Data to be sent to the Worker thread. The data object must be sequenceable.
         *     For details about the supported parameter types, see Sequenceable Data Types.
         * @param { ArrayBuffer[] } transfer - ArrayBuffer instance holding an array of objects for which the ownership
         *     is transferred to the Worker thread. After the transfer, the objects are available only in the Worker thread.
         *     The array cannot be null.
         * @throws { BusinessError } 10200004 - The Worker instance is not running.
         * @throws { BusinessError } 10200006 - An exception occurred during serialization.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        postMessage(message: Object, transfer: ArrayBuffer[]): void;
        /**
         * Sends a message from the host thread to the Worker thread by transferring object ownership or copying data.
         *
         * @param { Object } message - Data to be sent to the Worker thread. The data object must be sequenceable.
         *     For details about the supported parameter types, see Sequenceable Data Types.
         * @param { PostMessageOptions } [options] - If this parameter is specified, it functions the same as ArrayBuffer[].
         *     Specifically, the ownership of the objects in the array is transferred to the Worker thread and becomes
         *     unavailable in the host thread.
         *     The objects are available only in the Worker thread. If this parameter is not specified, the default value
         *     undefined is used,
         *     and information is transferred to the Worker thread by copying data.
         * @throws { BusinessError } 10200004 - The Worker instance is not running.
         * @throws { BusinessError } 10200006 - An exception occurred during serialization.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        postMessage(message: Object, options?: PostMessageOptions): void;
        /**
         * Sends a message from the host thread to the Worker thread. In the message, a sendable object is passed by
         * reference,
         * and a non-sendable object is passed by serialization.
         *
         * @param { Object } message - Data to be sent to the Worker thread. The data object must be sequenceable or
         *     sendable.
         *     For details about the supported sequenceable types, see Sequenceable Data Types.
         *     For details about the supported sendable types, see Sendable Data Types.
         * @param { ArrayBuffer[] } [transfer] - ArrayBuffer instance holding an array of objects for which the ownership
         *     is transferred to the Worker thread. After the transfer, the objects are available only in the Worker thread.
         *     The array cannot be null. The default value is an empty array.
         * @throws { BusinessError } 10200004 - The Worker instance is not running.
         * @throws { BusinessError } 10200006 - An exception occurred during serialization.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        postMessageWithSharedSendable(message: Object, transfer?: ArrayBuffer[]): void;
        /**
         * Adds an event listener for the Worker thread. This API provides the same functionality as addEventListener9+.
         *
         * @param { string } type - Type of the event to listen for.
         * @param { WorkerEventListener } listener - Callback to invoke when an event of the specified type occurs.
         * @throws { BusinessError } 10200004 - The Worker instance is not running.
         * @throws { BusinessError } 10200005 - The called API is not supported in the worker thread.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        on(type: string, listener: WorkerEventListener): void;
        /**
         * Adds an event listener for the Worker thread and removes the event listener after it is invoked once.
         *
         * @param { string } type - type Type of the event to listen for
         * @param { WorkerEventListener } listener - listener Callback to invoke when an event of the specified type occurs
         * @throws { BusinessError } 10200004 - The Worker instance is not running.
         * @throws { BusinessError } 10200005 - The called API is not supported in the worker thread.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        once(type: string, listener: WorkerEventListener): void;
        /**
         * Removes an event listener for the Worker thread. This API provides the same functionality as removeEventListener9
         * +.
         *
         * @param { string } type - type Type of the event for which the event listener is removed.
         * @param { WorkerEventListener } [listener] - listener Callback of the event listener to remove.
         * @throws { BusinessError } 10200004 - The Worker instance is not running.
         * @throws { BusinessError } 10200005 - The called API is not supported in the worker thread.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        off(type: string, listener?: WorkerEventListener): void;
        /**
         * Terminates the Worker thread to stop it from receiving messages.
         *
         * @throws { BusinessError } 10200004 - The Worker instance is not running.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        terminate(): void;
        /**
         * Adds an event listener for the Worker thread. This API provides the same functionality as on9+.
         *
         * @param { string } type - type Type of the event to listen for.
         * @param { WorkerEventListener } listener Callback to invoke when an event of the specified type occurs.
         * @throws { BusinessError } 10200004 - The Worker instance is not running.
         * @throws { BusinessError } 10200005 - The called API is not supported in the worker thread.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        addEventListener(type: string, listener: WorkerEventListener): void;
        /**
         * Dispatches the event defined for the Worker thread.
         *
         * @param { Event } event - event Event to dispatch.
         * @returns { boolean }
         * @throws { BusinessError } 10200004 - The Worker instance is not running.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        dispatchEvent(event: Event): boolean;
        /**
         * Removes an event listener for the Worker thread. This API provides the same functionality as off9+.
         *
         * @param { string } type - Type of the event for which the event listener is to be removed.
         * @param { WorkerEventListener } [callback] - Callback to invoke when the listener is removed.
         * @throws { BusinessError } 10200004 - The Worker instance is not running.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        removeEventListener(type: string, callback?: WorkerEventListener): void;
        /**
         * Removes all event listeners for the Worker thread.
         *
         * @throws { BusinessError } 10200004 - The Worker instance is not running.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        removeAllListener(): void;
        /**
         * Registers an object with the ThreadWorker instance of the host thread.
         * In this way, the methods of the object can be called in the Worker thread through callGlobalCallObjectMethod.
         *
         * @param { string } instanceName - Key used for registration, based on which the registered object is identified
         *     during method calling.
         * @param { Object } globalCallObject - Object to register. The ThreadWorker instance holds a strong reference to
         *     the object.
         * @throws { BusinessError } 10200004 - The Worker instance is not running.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        registerGlobalCallObject(instanceName: string, globalCallObject: Object): void;
        /**
         * Unregisters an object with the ThreadWorker instance of the host thread. This API releases the strong reference
         * between the ThreadWorker instance and the target object. No error is reported if no object is matched.
         *
         * @param { string } [instanceName] - Key used for registration. If this parameter is left blank,
         *     all registered objects registered in the ThreadWorker instance are unregistered.
         * @throws { BusinessError } 10200004 - The Worker instance is not running.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        unregisterGlobalCallObject(instanceName?: string): void;
    }
    /**
     * The Worker class contains all Worker functions.
     *
     * @syscap SystemCapability.Utils.Lang
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.worker.ThreadWorker
     */
    class Worker implements EventTarget {
        /**
         * Creates a worker instance
         *
         * @param { string } scriptURL - scriptURL URL of the script to be executed by the worker
         * @param { WorkerOptions } options - options Options that can be set for the worker
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.worker.ThreadWorker.constructor
         */
        constructor(scriptURL: string, options?: WorkerOptions);
        /**
         * Called when the Worker thread exits. The event handler is executed in the host thread. In the callback function,
         * the code value is of the number type, where the value 1 indicates abnormal exit and 0 indicates normal exit.The default value is undefined.
         *
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.worker.ThreadWorker.onexit
         */
        onexit?: (code: number) => void;
        /**
         * The onerror attribute of the worker specifies the event handler to be called
         * when an exception occurs during worker execution.
         * The event handler is executed in the host thread.
         *
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.worker.ThreadWorker.onerror
         */
        onerror?: (err: ErrorEvent) => void;
        /**
         * The onmessage attribute of the worker specifies the event handler
         * to be called then the host thread receives a message created by itself
         * and sent by the worker through the parentPort.postMessage.
         * The event handler is executed in the host thread.
         *
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.worker.ThreadWorker.onmessage
         */
        onmessage?: (event: MessageEvent) => void;
        /**
         * The onmessage attribute of the worker specifies the event handler
         * when the worker receives a message that cannot be serialized.
         * The event handler is executed in the host thread.
         *
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.worker.ThreadWorker.onmessageerror
         */
        onmessageerror?: (event: MessageEvent) => void;
        /**
         * Sends a message to the worker thread.
         * The data is transferred using the structured clone algorithm.
         *
         * @param { Object } message - message - message Data to be sent to the worker
         * @param { ArrayBuffer[] } transfer - transfer ArrayBuffer instance that can be transferred.
         *     The transferList array cannot contain null.
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.worker.ThreadWorker.postMessage
         */
        postMessage(message: Object, transfer: ArrayBuffer[]): void;
        /**
         * Sends a message to the worker thread.
         * The data is transferred using the structured clone algorithm.
         *
         * @param { Object } message - message - message Data to be sent to the worker
         * @param { PostMessageOptions } [options] - options Option can be set for postmessage.
         *     The transferList array cannot contain null.
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.worker.ThreadWorker.postMessage
         */
        postMessage(message: Object, options?: PostMessageOptions): void;
        /**
         * Adds an event listener to the worker.
         *
         * @param { string } type - type Adds an event listener to the worker.
         * @param { EventListener } listener - listener Callback to invoke when an event of the specified type occurs.
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.worker.ThreadWorker.on
         */
        on(type: string, listener: EventListener): void;
        /**
         * Adds an event listener to the worker
         * and removes the event listener automatically after it is invoked once.
         *
         * @param { string } type - type Type of the event to listen for
         * @param { EventListener } listener - listener Callback to invoke when an event of the specified type occurs
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.worker.ThreadWorker.once
         */
        once(type: string, listener: EventListener): void;
        /**
         * Removes an event listener to the worker.
         *
         * @param { string } type - type Type of the event for which the event listener is removed.
         * @param { EventListener } listener - listener Callback of the event listener to remove.
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.worker.ThreadWorker.off
         */
        off(type: string, listener?: EventListener): void;
        /**
         * Terminates the worker thread to stop the worker from receiving messages
         *
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.worker.ThreadWorker.terminate
         */
        terminate(): void;
    }
    /**
     * The object used by the worker thread to communicate with the host thread.
     *
     * @syscap SystemCapability.Utils.Lang
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.worker.workerPort
     */
    const parentPort: DedicatedWorkerGlobalScope;
    /**
     * The object used by the worker thread to communicate with the host thread.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    const workerPort: ThreadWorkerGlobalScope;
}
export default worker;

```
