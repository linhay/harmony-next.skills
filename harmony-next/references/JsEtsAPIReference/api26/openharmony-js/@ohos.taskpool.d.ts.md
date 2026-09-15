# @ohos.taskpool.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022 Huawei Device Co., Ltd.
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
 * TaskPool provides a multi-thread running environment for applications. It helps reduce resource consumption and
 * improve system performance. It also frees you from caring about the thread lifecycle. You can use the TaskPool APIs
 * to create background tasks and perform operations on them, for example, executing or canceling a task. Theoretically,
 * you can create an unlimited number of tasks, but this is not recommended due to memory limitations. In addition, you
 * are not advised performing blocking operations in a task, especially indefinite blocking. Long-time blocking
 * operations occupy worker threads and may block other task scheduling, adversely affecting your application
 * performance.
 * You can determine the execution sequence of tasks with the same priority. They are executed in the same sequence as
 * you call the task execution APIs. The default task priority is MEDIUM.
 * If the number of tasks to be executed is greater than the number of worker threads in the task pool, the task pool
 * scales out based on load balancing to minimize the waiting duration. Similarly, when the number of tasks to be
 * executed falls below the number of worker threads, the task pool scales in to reduce the number of worker threads.
 * For details about the error codes returned by TaskPool APIs, see
 * [Utils Error Codes](docroot://reference/apis-arkts/errorcode-utils.md).
 * For details about the precautions for using TaskPool, see
 * [Precautions for TaskPool](docroot://arkts-utils/taskpool-introduction.md#precautions-for-taskpool).
 * The following concepts are used in this topic:
 *
 * - Task group task: task in a [TaskGroup]{@link taskpool.TaskGroup}.
 * - Serial queue task: task in a [SequenceRunner]{@link taskpool.SequenceRunner}.
 * - Asynchronous queue task: task in an [AsyncRunner]{@link taskpool.AsyncRunner}.
 * - Periodic task: task executed by calling
 * [executePeriodically]{@link taskpool.executePeriodically(period: number, task: Task, priority?: Priority)}.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare namespace taskpool {
    /**
     * Enumerates the priorities available for created tasks. The task priority applies during task execution. The worker
     * thread priority is updated with the task priority. For details about the mappings, see
     * [QoS Level](docroot://napi/qos-guidelines.md#qos-level).
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    enum Priority {
        /**
         * The task has a high priority.
         *
         * This API can be used in atomic services since API version 11.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        HIGH = 0,
        /**
         * The task has a medium priority.
         *
         * This API can be used in atomic services since API version 11.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        MEDIUM = 1,
        /**
         * The task has a low priority.
         *
         * This API can be used in atomic services since API version 11.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        LOW = 2,
        /**
         * The task is a background task.
         *
         * This API can be used in atomic services since API version 12.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        IDLE = 3
    }
    /**
     * Describes a callback function.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    type CallbackFunction = () => void;
    /**
     * Describes a callback function with an error message.
     *
     * @param { Error } e - Error message.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    type CallbackFunctionWithError = (e: Error) => void;
    /**
     * Enumerates tasks, which can be executed for multiple times, placed in a task group, serial queue, or asynchronous
     * queue for execution, or added with dependencies for execution.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    class Task {
        /**
         * A constructor used to create a **Task** instance.
         *
         * @param { Function } func - Function to be executed. The function must be decorated using
         *     [@Concurrent](docroot://arkts-utils/taskpool-introduction.md#concurrent-decorator). For details about the
         *     supported return value types of the function, see
         *     [Sequenceable Data Types](docroot://reference/apis-arkts/js-apis-taskpool.md#sequenceable-data-types).
         * @param { Object[] } args - Arguments of the function. For details about the supported parameter types, see
         *     [Sequenceable Data Types](docroot://reference/apis-arkts/js-apis-taskpool.md#sequenceable-data-types). The
         *     default value is **undefined**.
         * @throws { BusinessError } 10200014 - The function is not marked as concurrent.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        constructor(func: Function, ...args: Object[]);
        /**
         * A constructor used to create a **Task** instance, with the task name specified.
         *
         * @param { string } name - Task name.
         * @param { Function } func - Function to be executed. The function must be decorated using
         *     [@Concurrent](docroot://arkts-utils/taskpool-introduction.md#concurrent-decorator). For details about the
         *     supported return value types of the function, see
         *     [Sequenceable Data Types](docroot://reference/apis-arkts/js-apis-taskpool.md#sequenceable-data-types).
         * @param { Object[] } args - Arguments of the function. For details about the supported types, see
         *     [Sequenceable Data Types](docroot://reference/apis-arkts/js-apis-taskpool.md#sequenceable-data-types). The
         *     default value is **undefined**.
         * @throws { BusinessError } 10200014 - The function is not marked as concurrent.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        constructor(name: string, func: Function, ...args: Object[]);
        /**
         * Checks whether the running task is canceled. Before using this method, you need to create a **Task** object.
         *
         * @returns { boolean } If the task is canceled, **true** is returned. Otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        static isCanceled(): boolean;
        /**
         * Sends data to the host thread and triggers the registered callback. Before calling this method, you need to
         * construct a **Task** object.
         *
         * > **NOTE**
         * >
         * > - The API should be called in the TaskPool thread.
         * >
         * > - Do not use this API in a callback function. Otherwise, messages may fail to be passed to the host thread.
         * >
         * > - Do not use this API in an asynchronous function. Otherwise, messages may fail to be passed to the host
         * > thread. If this API is used in an asynchronous function, use **await** to ensure that the asynchronous function
         * > is executed synchronously in the task.
         * >
         * > - Before calling this API, ensure that the callback function for processing data has been registered in the
         * > host thread.
         *
         * @param { Object[] } args - Data to be used as the argument of the registered callback. For details about the
         *     supported parameter types, see
         *     [Sequenceable Data Types](docroot://reference/apis-arkts/js-apis-taskpool.md#sequenceable-data-types). The
         *     default value is **undefined**.
         * @throws { BusinessError } 10200006 - An exception occurred during serialization.
         * @throws { BusinessError } 10200022 - The function is not called in the TaskPool thread.
         * @throws { BusinessError } 10200023 - The function is not called in the concurrent function.
         * @throws { BusinessError } 10200024 - The callback is not registered on the host side.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        static sendData(...args: Object[]): void;
        /**
         * Sets the task transfer list. Before using this API, you must create a **Task** instance. If this API is not
         * called, the ArrayBuffer in the data is transferred by default.
         *
         * > **NOTE**
         * >
         * > This API is used to set the task transfer list in the form of **ArrayBuffer** in the task pool. The
         * > **ArrayBuffer** instance does not copy the content in the task to the worker thread during transfer. Instead,
         * > it transfers the buffer control right to the worker thread. After the transfer, the **ArrayBuffer** instance
         * > becomes invalid. An empty **ArrayBuffer** will not be transferred.
         *
         * @param { ArrayBuffer[] } [transfer] - **ArrayBuffer** instance holding the objects to transfer. The default value
         *     is an empty array.
         * @throws { BusinessError } 10200029 - An ArrayBuffer cannot be set as both a transfer list and a clone list.
         *     [since 11]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        setTransferList(transfer?: ArrayBuffer[]): void;
        /**
         * Sets the task clone list. Before using this method, you need to construct a **Task** object.
         *
         * > **NOTE**
         * >
         * > This API must be used together with the
         * > [@Sendable decorator](docroot://arkts-utils/arkts-sendable.md#sendable-decorator). Otherwise, an exception is
         * > thrown. You are advised to use this decorator to avoid exceptions.
         *
         * @param { Object[] | ArrayBuffer[] } cloneList - - The type of the passed-in array must be
         *     [sendable data types](docroot://arkts-utils/arkts-sendable.md#sendable-data-types) or ArrayBuffer.<br>- All
         *     [Sendable class](docroot://arkts-utils/arkts-sendable.md#sendable-class) instances or ArrayBuffer objects
         *     passed in to **cloneList** are transferred in copy mode between threads. This means that any modification to
         *     the destination objects does not affect the original objects.
         * @throws { BusinessError } 10200029 - An ArrayBuffer cannot be set as both a transfer list and a clone list.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        setCloneList(cloneList: Object[] | ArrayBuffer[]): void;
        /**
         * Registers a callback for a task to receive and process data from the worker thread. Before using this API, you
         * must create a Task instance.
         * NOTE:
         * If multiple callbacks are registered for the same task, only the last registration takes effect.
         *
         * @param { Function } [callback] - Callback function for processing the data received. The data sent to the host
         *     thread is transferred to the callback as an input parameter. If no value is passed in, all the registered
         *     callbacks are canceled.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        onReceiveData(callback?: Function): void;
        /**
         * Adds dependent tasks for this task. Before using this API, you must create a **Task** instance. The task and its
         * dependent tasks cannot be a task in a task group, serial queue, or asynchronous queue, a task that has been
         * executed, or a periodic task. A task with a dependency relationship (a task that depends on another task or a
         * task that is depended on) cannot be executed multiple times.
         *
         * @param { Task[] } tasks - Array of tasks on which the current task depends. The default value is **undefined**.
         * @throws { BusinessError } 10200026 - There is a circular dependency.
         * @throws { BusinessError } 10200052 - The periodic task cannot have a dependency. [since 12]
         * @throws { BusinessError } 10200056 - The task has been executed by the AsyncRunner. [since 18]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        addDependency(...tasks: Task[]): void;
        /**
         * Removes dependent tasks for this task. Before using this method, you need to construct a **Task** object.
         *
         * @param { Task[] } tasks - Array of tasks on which the current task depends. The default value is **undefined**.
         * @throws { BusinessError } 10200027 - The dependency does not exist.
         * @throws { BusinessError } 10200052 - The periodic task cannot have a dependency. [since 12]
         * @throws { BusinessError } 10200056 - The task has been executed by the AsyncRunner. [since 18]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        removeDependency(...tasks: Task[]): void;
        /**
         * Register a callback function and call it when a task is enqueued.
         * The registration must be carried out before the task is executed. Otherwise, an exception is thrown.
         *
         * @param { CallbackFunction } [callback] - Callback function to register.
         * @throws { BusinessError } 10200034 - The executed task does not support the registration of listeners.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        onEnqueued(callback: CallbackFunction): void;
        /**
         * Register a callback function and call it when the execution of a task starts.
         * The registration must be carried out before the task is executed. Otherwise, an exception is thrown.
         *
         * @param { CallbackFunction } [callback] - Callback function to register.
         * @throws { BusinessError } 10200034 - The executed task does not support the registration of listeners.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        onStartExecution(callback: CallbackFunction): void;
        /**
         * Register a callback function and call it when a task fails to be executed(Periodic tasks are not supported).
         * The registration must be carried out before the task is executed. Otherwise, an exception is thrown.
         *
         * @param { CallbackFunctionWithError } [callback] - Callback function to register.
         * @throws { BusinessError } 10200034 - The executed task does not support the registration of listeners.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        onExecutionFailed(callback: CallbackFunctionWithError): void;
        /**
         * Register a callback function and call it when a task is executed successfully.
         * The registration must be carried out before the task is executed. Otherwise, an exception is thrown.
         *
         * @param { CallbackFunction } [callback] - Callback function to register.
         * @throws { BusinessError } 10200034 - The executed task does not support the registration of listeners.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        onExecutionSucceeded(callback: CallbackFunction): void;
        /**
         * Checks whether the task is complete.
         *
         * @returns { boolean } Check result. The value **true** is returned if the task is complete; otherwise, **false**
         *     is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        isDone(): boolean;
        /**
         * Function to be passed in during task creation. For details about the supported return value types of the function
         * , see [Sequenceable Data Types](docroot://reference/apis-arkts/js-apis-taskpool.md#sequenceable-data-types).<br>
         * This API can be used in atomic services since API version 11.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        function: Function;
        /**
         * Arguments of the function. For details about the supported parameter types, see
         * [Sequenceable Data Types](docroot://reference/apis-arkts/js-apis-taskpool.md#sequenceable-data-types).<br>
         * This API can be used in atomic services since API version 11.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        arguments?: Object[];
        /**
         * Name of the task specified when the task is created. You are advised not to change the value.<br>
         * This API can be used in atomic services since API version 11.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        name: string;
        /**
         * Task ID, which is globally unique by default. You are advised not to change the value.<br>
         * This API can be used in atomic services since API version 18.
         *
         * @default 0
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 22]
         * @atomicservice
         * @since 18
         */
        taskId: number;
        /**
         * Total execution time of the task. in ms. You are advised not to change the value.<br>
         * This API can be used in atomic services since API version 11.
         *
         * @default 0
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        totalDuration: number;
        /**
         * Asynchronous I/O time of the task. in ms. You are advised not to change the value.<br>
         * This API can be used in atomic services since API version 11.
         *
         * @default 0
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        ioDuration: number;
        /**
         * CPU time of the task. in ms. You are advised not to change the value.<br>
         * This API can be used in atomic services since API version 11.
         *
         * @default 0
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        cpuDuration: number;
    }
    /**
     * Implements a task group, in which tasks are associated with each other and all tasks are executed at a time. If all
     * the tasks are executed normally, an array of task results is returned asynchronously, and the sequence of elements
     * in the array is the same as the sequence of tasks added by calling
     * [addTask]{@link taskpool.TaskGroup#addTask(task: Task)}. If any task fails, the corresponding exception is thrown.
     * If multiple tasks in the task group fail, the exception of the first failed task is thrown. A task group can be
     * executed for multiple times, but no task can be added after the task group is executed.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    class TaskGroup {
        /**
         * Constructor used to create a **TaskGroup** instance.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        constructor();
        /**
         * A constructor used to create a **TaskGroup** instance, with the task group name specified.
         *
         * @param { string } name - Task group name.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        constructor(name: string);
        /**
         * Adds the function to be executed to this task group. Before using this API, you must create a **TaskGroup**
         * instance.
         *
         * @param { Function } func - Function that must be decorated using
         *     [@Concurrent](docroot://arkts-utils/taskpool-introduction.md#concurrent-decorator). For details about the
         *     supported return value types, see
         *     [Sequenceable Data Types](docroot://reference/apis-arkts/js-apis-taskpool.md#sequenceable-data-types).
         * @param { Object[] } args - Arguments of the function. For details about the supported parameter types, see
         *     [Sequenceable Data Types](docroot://reference/apis-arkts/js-apis-taskpool.md#sequenceable-data-types). The
         *     default value is **undefined**.
         * @throws { BusinessError } 10200014 - The function is not marked as concurrent.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        addTask(func: Function, ...args: Object[]): void;
        /**
         * Adds a created task to this task group. Before using this API, you must create a **TaskGroup** instance. Tasks in
         * another task group, serial queue, or asynchronous queue, dependent tasks, continuous tasks, tasks that have been
         * executed, and periodic tasks cannot be added to the task group.
         *
         * @param { Task } task - Task to be added to the task group.
         * @throws { BusinessError } 10200014 - The function is not marked as concurrent.
         * @throws { BusinessError } 10200051 - The periodic task cannot be executed again. [since 12]
         * @throws { BusinessError } 10200057 - The task cannot be executed by two APIs. [since 18]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        addTask(task: Task): void;
        /**
         * Name of the task group specified when the task group is created.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        name: string;
    }
    /**
     * Implements a serial queue, in which all tasks are executed in sequence.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 11
     */
    class SequenceRunner {
        /**
         * A constructor used to create a **SequenceRunner** instance.
         *
         * @param { Priority } priority - Priority of the task. The default value is **taskpool.Priority.MEDIUM**.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        constructor(priority?: Priority);
        /**
         * A constructor used to create a **SequenceRunner** instance. This instance represents a global serial queue. If
         * the passed-in name is the same as an existing name, the same serial queue is returned.
         *
         * > **NOTE**
         * >
         * > - The bottom layer uses the singleton mode to ensure that the same instance is obtained when a serial queue
         * > with the same name is created.
         * >
         * > - The priority of a serial queue cannot be modified.
         *
         * @param { string } name - Name of a serial queue.
         * @param { Priority } priority - Priority of the task. The default value is **taskpool.Priority.MEDIUM**.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        constructor(name: string, priority?: Priority);
        /**
         * Adds a task to the serial queue for execution. Before using this API, you must create a **SequenceRunner**
         * instance. Tasks in another task group, serial queue, or asynchronous queue, dependent tasks, and tasks that have
         * been executed cannot be added to the serial queue. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > - Tasks that depend others cannot be added to the serial queue.
         * >
         * > - The failure or cancellation of a task does not affect the execution of subsequent tasks in the serial queue.
         *
         * @param { Task } task - Task to be added to the serial queue.
         * @returns { Promise<Object> } Promise used to return the task execution result.
         * @throws { BusinessError } 10200003 - Worker initialization failed. [since 11 - 17]
         * @throws { BusinessError } 10200006 - An exception occurred during serialization.
         * @throws { BusinessError } 10200025 - dependent task not allowed.
         * @throws { BusinessError } 10200051 - The periodic task cannot be executed again. [since 12]
         * @throws { BusinessError } 10200057 - The task cannot be executed by two APIs. [since 18]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        execute(task: Task): Promise<Object>;
    }
    /**
     * Describes a continuous task. **LongTask** inherits from
     * [Task]{@link taskpool.execute(func: Function, ...args: Object[])}.
     * No upper limit is set for the execution time of a continuous task, and no timeout exception is thrown if a
     * continuous task runs for a long period of time. However, a continuous task cannot be executed in a task group or
     * executed for multiple times.
     * The thread for executing a continuous task exists until [terminateTask]{@link taskpool.terminateTask} is called
     * after the execution is complete. The thread is reclaimed when it is idle.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    class LongTask extends Task {
    }
    /**
     * Implements a generic task. **GenericsTask** inherits from
     * [Task]{@link taskpool.execute(func: Function, ...args: Object[])}.
     * During the creation of a generic task, the passed-in parameter types and return value types of concurrent functions
     * are verified in the compilation phase. Other behaviors are the same as those during the creation of a task.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 18]
     * @atomicservice
     * @since 13
     */
    class GenericsTask<A extends Array<Object>, R> extends Task {
        /**
         * A constructor used to create a **GenericsTask** object.
         *
         * @param { (...args: A) => R | Promise<R> } func - Function to be executed. The function must be decorated using
         *     [@Concurrent](docroot://arkts-utils/taskpool-introduction.md#concurrent-decorator). For details about the
         *     supported return value types of the function, see
         *     [Sequenceable Data Types](docroot://reference/apis-arkts/js-apis-taskpool.md#sequenceable-data-types).
         * @param { A } args - Arguments of the function. For details about the supported parameter types, see
         *     [Sequenceable Data Types](docroot://reference/apis-arkts/js-apis-taskpool.md#sequenceable-data-types). The
         *     default value is **undefined**.
         * @throws { BusinessError } 10200014 - The function is not marked as concurrent.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 18]
         * @atomicservice
         * @since 13
         */
        constructor(func: (...args: A) => R | Promise<R>, ...args: A);
        /**
         * A constructor used to create a **GenericsTask** instance, with the task name specified.
         *
         * @param { string } name - Name of the generic task.
         * @param { (...args: A) => R | Promise<R> } func - Function to be executed. The function must be decorated using
         *     [@Concurrent](docroot://arkts-utils/taskpool-introduction.md#concurrent-decorator). For details about the
         *     supported return value types of the function, see
         *     [Sequenceable Data Types](docroot://reference/apis-arkts/js-apis-taskpool.md#sequenceable-data-types).
         * @param { A } args - Arguments of the function. For details about the supported parameter types, see
         *     [Sequenceable Data Types](docroot://reference/apis-arkts/js-apis-taskpool.md#sequenceable-data-types). The
         *     default value is **undefined**.
         * @throws { BusinessError } 10200014 - The function is not marked as concurrent.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 18]
         * @atomicservice
         * @since 13
         */
        constructor(name: string, func: (...args: A) => R | Promise<R>, ...args: A);
    }
    /**
     * Enumerates the task states. After a task is created and **execute()** is called, the task is placed in the internal
     * queue of the task pool and the state is **WAITING**. When the task is being executed by the worker thread of the
     * task pool, the state changes to **RUNNING**. After the task is executed and the result is returned, the state is
     * reset to **WAITING**. When the task is proactively canceled, the state changes to **CANCELED**.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    enum State {
        /**
         * The task is waiting.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        WAITING = 1,
        /**
         * The task is running.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        RUNNING = 2,
        /**
         * The task is canceled.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        CANCELED = 3
    }
    /**
     * Describes the internal information about a task.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    class TaskInfo {
        /**
         * Task ID, which is globally unique by default. You are advised not to change the value.<br>
         * This API can be used in atomic services since API version 11.
         *
         * @default 0
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        taskId: number;
        /**
         * Task state. You are advised not to change the value.<br>
         * This API can be used in atomic services since API version 11.
         *
         * @default State::WAITING
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        state: State;
        /**
         * Duration that the task has been executed, in ms. The default value is **0**. If the return value is **0**, the
         * task is not running. If the return value is empty, no task is running. You are advised not to change the value.<
         * br>
         * This API can be used in atomic services since API version 11.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        duration?: number;
        /**
         * Task name. You are advised not to change the value.<br>
         * This API can be used in atomic services since API version 12.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        name: string;
    }
    /**
     * Describes the internal information about a worker thread.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    class ThreadInfo {
        /**
         * ID of the worker thread. If the return value is empty, no task is running. You are advised not to change the
         * value.
         *
         * @default 0
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        tid: number;
        /**
         * IDs of tasks running on the calling thread. If the return value is empty, no task is running. You are advised not
         * to change the value.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        taskIds?: number[];
        /**
         * Priority of the calling thread. If the return value is empty, no task is running. You are advised not to change
         * the value.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        priority?: Priority;
    }
    /**
     * Describes the internal information about a task pool.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    class TaskPoolInfo {
        /**
         * Internal information about the worker threads. You are advised not to change the value.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        threadInfos: ThreadInfo[];
        /**
         * Internal information about the tasks. You are advised not to change the value.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        taskInfos: TaskInfo[];
    }
    /**
     * Places a function to be executed in the internal queue of the task pool. The function is not executed immediately.
     * It waits to be distributed to the worker thread for execution. In this mode, the function cannot be canceled. This
     * API uses a promise to return the result.
     *
     * @param { Function } func - Function to be executed. The function must be decorated using
     *     [@Concurrent](docroot://arkts-utils/taskpool-introduction.md#concurrent-decorator). For details about the
     *     supported return value types of the function, see
     *     [Sequenceable Data Types](docroot://reference/apis-arkts/js-apis-taskpool.md#sequenceable-data-types).
     * @param { Object[] } args - Arguments of the function. For details about the supported parameter types, see
     *     [Sequenceable Data Types](docroot://reference/apis-arkts/js-apis-taskpool.md#sequenceable-data-types). The
     *     default value is **undefined**.
     * @returns { Promise<unknown> } [since 9 - 11]
     * @returns { Promise<Object> } Promise used to return an object that carries the function execution result. [since 11]
     * @throws { BusinessError } 10200003 - Worker initialization failed. [since 9 - 11]
     * @throws { BusinessError } 10200006 - An exception occurred during serialization.
     * @throws { BusinessError } 10200014 - The function is not marked as concurrent.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function execute(func: Function, ...args: Object[]): Promise<Object>;
    /**
     * Verifies the passed-in parameter types and return value type of a concurrent function, and places the function in
     * the queue of the task pool. This API uses a promise to return the result.
     *
     * @param { (...args: A) => R | Promise<R> } func - Function to be executed. The function must be decorated using
     *     [@Concurrent](docroot://arkts-utils/taskpool-introduction.md#concurrent-decorator). For details about the
     *     supported return value types of the function, see
     *     [Sequenceable Data Types](docroot://reference/apis-arkts/js-apis-taskpool.md#sequenceable-data-types).
     * @param { A } args - Arguments of the function. For details about the supported parameter types, see
     *     [Sequenceable Data Types](docroot://reference/apis-arkts/js-apis-taskpool.md#sequenceable-data-types). The
     *     default value is **undefined**.
     * @returns { Promise<R> } Promise used to return an object that carries the function execution result.
     * @throws { BusinessError } 10200006 - An exception occurred during serialization.
     * @throws { BusinessError } 10200014 - The function is not marked as concurrent.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 18]
     * @atomicservice
     * @since 13
     */
    function execute<A extends Array<Object>, R>(func: (...args: A) => R | Promise<R>, ...args: A): Promise<R>;
    /**
     * Places a task in the internal queue of the task pool. The task will not be executed immediately; instead, it waits
     * to be distributed to a worker thread for execution. In the current mode, you can set the task priority and cancel
     * the task. Note that the task cannot belong to a task group, serial queue, or asynchronous queue. For non-continuous
     * tasks, this API can be called multiple times. This API uses a promise to return the result.
     *
     * @param { Task } task - Task to be executed.
     * @param { Priority } [priority] - Priority of the task to be executed. The default value is
     *     **taskpool.Priority.MEDIUM**.
     * @returns { Promise<unknown> } [since 9 - 17]
     * @returns { Promise<Object> } Promise used to return an object that carries the function execution result. [since 11]
     * @throws { BusinessError } 10200003 - Worker initialization failed. [since 9 - 17]
     * @throws { BusinessError } 10200006 - An exception occurred during serialization.
     * @throws { BusinessError } 10200014 - The function is not marked as concurrent.
     * @throws { BusinessError } 10200051 - The periodic task cannot be executed again. [since 12]
     * @throws { BusinessError } 10200057 - The task cannot be executed by two APIs. [since 18]
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function execute(task: Task, priority?: Priority): Promise<Object>;
    /**
     * Places the generic task in the internal queue of the task pool. The parameter type and return value type of the
     * task are not verified. This API uses a promise to return the result.
     * The verification of the **execute** task works in conjunction with **new GenericsTask**, requiring that the
     * parameter and return value types match those specified in **new GenericsTask**.
     *
     * @param { GenericsTask<A, R> } task - Generic task to be executed.
     * @param { Priority } [priority] - Priority of the task to be executed. The default value is
     *     **taskpool.Priority.MEDIUM**.
     * @returns { Promise<R> } Promise used to return an object that carries the function execution result.
     * @throws { BusinessError } 10200006 - An exception occurred during serialization.
     * @throws { BusinessError } 10200014 - The function is not marked as concurrent.
     * @throws { BusinessError } 10200051 - The periodic task cannot be executed again.
     * @throws { BusinessError } 10200057 - The task cannot be executed by two APIs. [since 18]
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 18]
     * @atomicservice
     * @since 13
     */
    function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, priority?: Priority): Promise<R>;
    /**
     * Places a task group in the internal queue of the task pool. The tasks in the task group are not executed
     * immediately. They wait to be distributed to the worker thread for execution. After all tasks in the task group are
     * executed, a result array is returned. This mode is applicable to the execution of associated tasks. This API uses a
     * promise to return the result.
     *
     * @param { TaskGroup } group - Task group to be executed.
     * @param { Priority } [priority] - Priority of the task group. The default value is **taskpool.Priority.MEDIUM**.
     * @returns { Promise<Object[]> } Promise used to return an object array that carries the function execution result.
     * @throws { BusinessError } 10200006 - An exception occurred during serialization.
     * @throws { BusinessError } 10200059 - TaskGroup cannot be re-executed. [since 24]
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    function execute(group: TaskGroup, priority?: Priority): Promise<Object[]>;
    /**
     * Executes a task after a given delay. In this execution mode, you can set the task priority and call **cancel()** to
     * cancel the execution. The task cannot be a task in a task group, serial queue, or asynchronous queue, or a periodic
     * task. This API can be called only once for a continuous task, but multiple times for a non-continuous task. This
     * API uses a promise to return the result.
     *
     * @param { number } delayTime - Delay, in ms. The value must be greater than or equal to 0.
     *     The value should be an integer.
     *     <br>Unit:milliseconds.
     * @param { Task } task - Task to be executed with a delay.
     * @param { Priority } [priority] - Priority of the task. The default value is **taskpool.Priority.MEDIUM**.
     * @returns { Promise<Object> } Promise used to return an object that carries the function execution result.
     * @throws { BusinessError } 10200028 - The delayTime is less than zero.
     * @throws { BusinessError } 10200006 - An exception occurred during serialization. [since 12]
     * @throws { BusinessError } 10200014 - The function is not marked as concurrent. [since 12]
     * @throws { BusinessError } 10200051 - The periodic task cannot be executed again. [since 12]
     * @throws { BusinessError } 10200057 - The task cannot be executed by two APIs. [since 18]
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 11
     */
    function executeDelayed(delayTime: number, task: Task, priority?: Priority): Promise<Object>;
    /**
     * Executes the generic task with a delay without verifying the parameter type and return value type of the task. This
     * API uses a promise to return the result.
     * The verification of the **executeDelayed** task works in conjunction with **new GenericsTask**, requiring that the
     * parameter and return value types match those specified in **new GenericsTask**.
     *
     * @param { number } delayTime - Delay, in ms. The value must be greater than or equal to 0.
     *     The value should be an integer.
     *     <br>Unit:milliseconds.
     * @param { GenericsTask<A, R> } task - Generic task to be executed with a delay.
     * @param { Priority } [priority] - Priority of the task. The default value is **taskpool.Priority.MEDIUM**.
     * @returns { Promise<R> } Promise used to return an object that carries the function execution result.
     * @throws { BusinessError } 10200028 - The delayTime is less than zero.
     * @throws { BusinessError } 10200051 - The periodic task cannot be executed again.
     * @throws { BusinessError } 10200057 - The task cannot be executed by two APIs. [since 18]
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 18]
     * @atomicservice
     * @since 13
     */
    function executeDelayed<A extends Array<Object>, R>(delayTime: number, task: GenericsTask<A, R>, priority?: Priority): Promise<R>;
    /**
     * Executes a task periodically. In this execution mode, you can set the task priority and call **cancel()** to cancel
     * the execution. A periodic task cannot be a task in a task group, serial queue, or asynchronous queue. It cannot
     * call **execute()** again or have a dependency relationship.
     *
     * @param { number } period - Execution period, in ms. The value must be greater than or equal to 0.
     *     The value should be an integer.
     *     <br>Unit:milliseconds.
     * @param { Task } task - Task to be executed.
     * @param { Priority } [priority] - Priority of the task. The default value is **taskpool.Priority.MEDIUM**.
     * @throws { BusinessError } 10200006 - An exception occurred during serialization.
     * @throws { BusinessError } 10200014 - The function is not marked as concurrent.
     * @throws { BusinessError } 10200028 - The period is less than zero.
     * @throws { BusinessError } 10200050 - The concurrent task has been executed and cannot be executed periodically.
     * @throws { BusinessError } 10200057 - The task cannot be executed by two APIs. [since 18]
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    function executePeriodically(period: number, task: Task, priority?: Priority): void;
    /**
     * Executes a generic task periodically, without verifying the parameter type and return value type of the task.
     * The verification of the **executePeriodically** task works in conjunction with **new GenericsTask**, requiring that
     * the parameter and return value types match those specified in **new GenericsTask**.
     *
     * @param { number } period - Execution period, in ms. The value must be greater than or equal to 0.
     *     The value should be an integer.
     *     <br>Unit:milliseconds.
     * @param { GenericsTask<A, R> } task - Generic task to be executed periodically.
     * @param { Priority } [priority] - Priority of the task. The default value is **taskpool.Priority.MEDIUM**.
     * @throws { BusinessError } 10200006 - An exception occurred during serialization.
     * @throws { BusinessError } 10200014 - The function is not marked as concurrent.
     * @throws { BusinessError } 10200028 - The period is less than zero.
     * @throws { BusinessError } 10200050 - The concurrent task has been executed and cannot be executed periodically.
     * @throws { BusinessError } 10200057 - The task cannot be executed by two APIs. [since 18]
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 18]
     * @atomicservice
     * @since 13
     */
    function executePeriodically<A extends Array<Object>, R>(period: number, task: GenericsTask<A, R>, priority?: Priority): void;
    /**
     * Cancels a task in the task pool. If the task is in the internal queue of the task pool, the task will not be
     * executed after being canceled, and an exception indicating task cancellation is returned. If the task has been
     * distributed to the worker thread of the task pool, canceling the task does not affect the task execution, and the
     * execution result is returned in the catch branch. You can use **isCanceled()** to check the task cancellation
     * status. In other words, **taskpool.cancel** takes effect for calls of **taskpool.execute**,
     * **taskpool.executeDelayed**, or **taskpool.executePeriodically**.
     * Starting from API version 20, after performing a cancel operation, you can use the generic type BusinessError<
     * [taskpool.TaskResult]{@link taskpool.TaskResult}> in the catch branch to obtain the exception information thrown by
     * the task or the final execution result.
     *
     * @param { Task } task - Task to cancel.
     * @throws { BusinessError } 10200015 - The task to cancel does not exist.
     * @throws { BusinessError } 10200016 - The task to cancel is being executed. [since 9 - 17]
     * @throws { BusinessError } 10200055 - The asyncRunner task has been canceled. [since 18]
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function cancel(task: Task): void;
    /**
     * Cancels a task group in the task pool. If a task group is canceled before all the tasks in it are finished,
     * **undefined** is returned.
     * Starting from API version 20, after performing a cancel operation, you can use the generic type BusinessError<
     * [taskpool.TaskResult]{@link taskpool.TaskResult}> in the catch branch to obtain the exception information thrown by
     * the task or the final execution result.
     *
     * @param { TaskGroup } group - Task group to cancel.
     * @throws { BusinessError } 10200018 - The task group to cancel does not exist.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    function cancel(group: TaskGroup): void;
    /**
     * Cancels a task in the task pool by task ID. If the task is in the internal queue of the task pool, the task will
     * not be executed after being canceled, and an exception indicating task cancellation is returned. If the task has
     * been distributed to the worker thread of the task pool, canceling the task does not affect the task execution, and
     * the execution result is returned in the catch branch. You can use **isCanceled()** to check the task cancellation
     * status. **taskpool.cancel** takes effect for the previous calls of **taskpool.execute** or
     * **taskpool.executeDelayed**. If **taskpool.cancel** is called by other threads, note that the cancel operation,
     * which is asynchronous, may take effect for later calls of **taskpool.execute** or **taskpool.executeDelayed**.
     * Starting from API version 20, after performing a cancel operation, you can use the generic type BusinessError<
     * [taskpool.TaskResult]{@link taskpool.TaskResult}> in the catch branch to obtain the exception information thrown by
     * the task or the final execution result.
     *
     * @param { number } taskId - ID of the task to cancel.
     * @throws { BusinessError } 10200015 - The task to cancel does not exist.
     * @throws { BusinessError } 10200055 - The asyncRunner task has been canceled.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 22]
     * @atomicservice
     * @since 18
     */
    function cancel(taskId: number): void;
    /**
     * Obtains the thread information and task information of the task pool.
     *
     * @returns { TaskPoolInfo } Internal information about the task pool.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    function getTaskPoolInfo(): TaskPoolInfo;
    /**
     * Terminates a continuous task in the task pool. It is called after the continuous task is complete. After the task
     * is terminated, the thread that executes the task may be reclaimed.
     *
     * @param { LongTask } longTask - Continuous task to terminate.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    function terminateTask(longTask: LongTask): void;
    /**
     * Checks whether a function is a concurrent function.
     *
     * @param { Function } func - Function to check.
     * @returns { boolean } Check result. The value **true** is returned if the function is a concurrent function, that is
     *     , a function decorated with [@Concurrent](docroot://arkts-utils/taskpool-introduction.md#concurrent-decorator);
     *     otherwise, **false** is returned.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    function isConcurrent(func: Function): boolean;
    /**
     * Implements an asynchronous queue, for which you can specify the task execution concurrency and queuing policy.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 22]
     * @atomicservice
     * @since 18
     */
    export class AsyncRunner {
        /**
         * A constructor used to create an **AsyncRunner** instance. It constructs a non-global asynchronous queue. Even
         * when the parameters passed are the same, it returns different asynchronous queues.
         *
         * @param { number } runningCapacity - Maximum number of tasks that can run concurrently. The value must be a
         *     positive integer. If a negative number is passed, an error is reported. If a non-integer is passed, the value
         *     is rounded down.
         * @param { ?number } waitingCapacity - Maximum number of tasks that can be queued. The value must be greater than
         *     or equal to 0. If a negative number is passed, an error is reported. If a non-integer is passed, the value is
         *     rounded down. The default value is **0**, indicating that there is no limit to the number of tasks that can
         *     wait. If a value greater than 0 is passed, tasks will be discarded from the front of the queue once the queue
         *     size exceeds this limit, implementing a discard policy.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 22]
         * @atomicservice
         * @since 18
         */
        constructor(runningCapacity: number, waitingCapacity?: number);
        /**
         * A constructor used to create an **AsyncRunner** instance. It constructs a global asynchronous queue. If the queue
         * name is the same as an existing name, the same asynchronous queue is returned.
         *
         * > **NOTE**
         * >
         * > - The bottom layer uses the singleton mode to ensure that the same instance is obtained when an asynchronous
         * > queue with the same name is created.
         * >
         * > - The task execution concurrency and waiting capacity cannot be modified.
         *
         * @param { string } name - Name of an asynchronous queue.
         * @param { number } runningCapacity - Maximum number of tasks that can run concurrently. The value must be a
         *     positive integer. If a negative number is passed, an error is reported. If a non-integer is passed, the value
         *     is rounded down.
         * @param { ?number } waitingCapacity - Maximum number of tasks that can be queued. The value must be greater than
         *     or equal to 0. If a negative number is passed, an error is reported. If a non-integer is passed, the value is
         *     rounded down. The default value is **0**, indicating that there is no limit to the number of tasks that can
         *     wait. If a value greater than 0 is passed, tasks will be discarded from the front of the queue once the queue
         *     size exceeds this limit, implementing a discard policy.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 22]
         * @atomicservice
         * @since 18
         */
        constructor(name: string, runningCapacity: number, waitingCapacity?: number);
        /**
         * Adds a task to the asynchronous queue for execution. Before using this API, you must create an **AsyncRunner**
         * instance. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > - Tasks in a task group cannot be added to the asynchronous queue.
         * >
         * > - Tasks in a serial queue cannot be added to the asynchronous queue.
         * >
         * > - Tasks in other asynchronous queues cannot be added to the asynchronous queue.
         * >
         * > - Periodic tasks cannot be added to the asynchronous queue.
         * >
         * > - Delayed tasks cannot be added to the asynchronous queue.
         * >
         * > - Tasks that depend others cannot be added to the asynchronous queue.
         * >
         * > - Tasks that have been executed cannot be added to the asynchronous queue.
         *
         * @param { Task } task - Task to be added to the asynchronous queue.
         * @param { ?Priority } [priority] - Priority of the task. The default value is **taskpool.Priority.MEDIUM**.
         * @returns { Promise<Object> } Promise used to return the task execution result.
         * @throws { BusinessError } 10200006 - An exception occurred during serialization.
         * @throws { BusinessError } 10200025 - dependent task not allowed.
         * @throws { BusinessError } 10200051 - The periodic task cannot be executed again.
         * @throws { BusinessError } 10200054 - The asyncRunner task is discarded.
         * @throws { BusinessError } 10200057 - The task cannot be executed by two APIs.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 22]
         * @atomicservice
         * @since 18
         */
        execute(task: Task, priority?: Priority): Promise<Object>;
    }
    /**
     * Describes the supplementary information captured in **BusinessError** in the catch branch after a task in the
     * waiting or execution phase is canceled. In other scenarios, the task result is **undefined**.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    interface TaskResult {
        /**
         * Task execution result. The default value is **undefined**. You are advised not to change the value.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        result?: Object;
        /**
         * Error message. By default, the value is the same as the **message** field of **BusinessError**. You are advised
         * not to change the value.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        error?: Error | Object;
    }
    /**
     * Obtains the corresponding task instance by task ID, or by task ID and task name.
     *
     * > **NOTE**
     * >
     * > - If no task instance is found based on the input task ID, **undefined** is returned.
     * >
     * > - If the corresponding task instance can be queried based on the input task ID but the thread that calls the
     * > **getTask** method is different from the thread that creates the task instance, **undefined** is returned.
     * >
     * > - If taskId and taskName are both passed, and the name of the task instance queried via task ID does not match
     * > the provided task name, **undefined** is returned.
     *
     * @param { number } taskId - Task ID.
     *     The value should be an integer.
     * @param { string } [taskName] - Task name. The default value is **undefined**.
     * @returns { Task | undefined } Task instance. If an exception occurs, **undefined** is returned. For details, see
     *     the preceding description.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 22
     */
    function getTask(taskId: number, taskName?: string): Task | undefined;
    /**
     * Defines the task configs interface
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 24
     */
    interface Configs {
        /**
         * The priority of the task. The default value is taskpool.Priority.MEDIUM.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 24
         */
        priority?: Priority;
        /**
         * The timeout for the task in ms. Suggest passing in integers. If decimals are passed in, they will be rounded down.
         * If this parameter is omitted, timeout will take the default value of 0 and no timeout logic will be executed.
         * **NOTE**
         * 1. The timeout period is not a precise time, and the actual timeout period may differ from the expected time.
         * 2. If the value is less than 1, it will be defaulted to **0**.
         * 3. The value is subject to system limitations. If it exceeds 2^31 �C 1, the value will be **0**.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 24
         */
        timeout?: number;
    }
    /**
     * Execute a concurrent task with Configs.
     *
     * @param { Task } task - Task to be executed.
     * @param { Configs } configs - Configs of the task.
     * @returns { Promise<Object> }
     * @throws { BusinessError } 10200006 - An exception occurred during serialization.
     * @throws { BusinessError } 10200014 - The function is not marked as concurrent.
     * @throws { BusinessError } 10200051 - The periodic task cannot be executed again.
     * @throws { BusinessError } 10200057 - The task cannot be executed by two APIs.
     * @throws { BusinessError } 10200058 - Task timed out.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 24
     */
    function execute(task: Task, configs: Configs): Promise<Object>;
    /**
     * Execute a concurrent generics task with Configs.
     *
     * @param { GenericsTask<A, R> } task - Generic task to be executed.
     * @param { Configs } configs - Configs of the task.
     * @returns { Promise<R> }
     * @throws { BusinessError } 10200006 - An exception occurred during serialization.
     * @throws { BusinessError } 10200014 - The function is not marked as concurrent.
     * @throws { BusinessError } 10200051 - The periodic task cannot be executed again.
     * @throws { BusinessError } 10200057 - The task cannot be executed by two APIs.
     * @throws { BusinessError } 10200058 - Task timed out.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 24
     */
    function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, configs: Configs): Promise<R>;
    /**
     * Execute a concurrent task group with Configs.
     *
     * @param { TaskGroup } group - Task group to be executed.
     * @param { Configs } configs - Configs of each task in the TaskGroup.
     * @returns { Promise<Object[]> }
     * @throws { BusinessError } 10200006 - An exception occurred during serialization.
     * @throws { BusinessError } 10200059 - TaskGroup cannot be re-executed.
     * @throws { BusinessError } 10200070 - TaskGroup timed out.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 24
     */
    function execute(group: TaskGroup, configs: Configs): Promise<Object[]>;
}
export default taskpool;

```
