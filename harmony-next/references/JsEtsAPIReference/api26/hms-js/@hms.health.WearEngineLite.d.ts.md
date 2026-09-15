# @hms.health.WearEngineLite.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
 */
/**
 * @file This module provides the capability of wear engine in lite wearable.
 * @kit WearEngine
 */
/**
 * 1. Callback for event changes.
 * 2. This callback is used for event listener registration.
 *
 * @typedef MonitorEventCallback
 * @syscap SystemCapability.Health.WearEngine.Lite
 * @famodelonly
 * @since 6.1.1(24)
 */
export interface MonitorEventCallback {
    /**
     * 1. Callback triggered upon an event change.
     * 2. This callback is used to notify developers when an event changes.
     *
     * @param { MonitorEventData } data  - 1. Event-related data.
     *     2. This parameter is used to notify developers of related data when an event changes.
     * @syscap SystemCapability.Health.WearEngine.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    eventChange(data: MonitorEventData): void;
    /**
     * 1. Callback triggered when the listening API is called successfully.
     * 2. This callback is triggered when the listening API is called successfully.
     *
     * @param { number } code  - 1. Success return code.
     *     2. This callback is triggered when the listening API is called successfully.
     * @param { string } [data]  - 1. Message returned upon a success.
     *     2. This parameter is used to return related information when calling the listening API succeeds.
     * @syscap SystemCapability.Health.WearEngine.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    success(code: number, data?: string): void;
    /**
     * 1. Callback triggered when calling the event listening API fails.
     * 2. This callback is used to notify developers when calling the listening API fails.
     *
     * @param { number } code  - 1. Error code.
     *     2. Error code returned when calling the listening API fails.
     * @param { string } [data]  - 1. Error message returned upon a failure.
     *     2. This parameter is used to return error information when calling the listening API fails.
     * @syscap SystemCapability.Health.WearEngine.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    fail(code: number, data?: string): void;
}
/**
 * 1. Data returned when an event changes.
 * 2. This API is used to return related data when the listened event changes.
 *
 * @typedef MonitorEventData
 * @syscap SystemCapability.Health.WearEngine.Lite
 * @famodelonly
 * @since 6.1.1(24)
 */
export interface MonitorEventData {
    /**
     * 1. Type of the event that changes.
     * 2. When the listened event changes, this API is used to return the event type.
     *
     *
     *
     * @syscap SystemCapability.Health.WearEngine.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    event: string;
    /**
     * 1. Data returned when an event change occurs.
     * 2. This parameter is used to return related data when an event change occurs.
     *
     * @type { MonitorData }
     * @syscap SystemCapability.Health.WearEngine.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    data: MonitorData;
}
/**
 * 1. Data returned when an event change occurs.
 * 2. This API is used to return data when the listened event changes.
 *
 * @typedef MonitorData
 * @syscap SystemCapability.Health.WearEngine.Lite
 * @famodelonly
 * @since 6.1.1(24)
 */
interface MonitorData {
    /**
     * 1. Numeric data returned when an event change occurs.
     * 2. This API is used to return numeric data when the listened event changes.
     *
     * @type { number }
     * @syscap SystemCapability.Health.WearEngine.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    code: number;
    /**
     * 1. Character string data returned when an event change occurs.
     * 2. This API is used to return character string data when the listened event changes.
     *
     *
     *
     * @type { ?string }
     * @syscap SystemCapability.Health.WearEngine.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    data?: string;
}
/**
 * 1. App information.
 * 2. App information is required when the file transfer progress is obtained.
 *
 * @syscap SystemCapability.Health.WearEngine.Lite
 * @famodelonly
 * @since 26.0.0
 */
export interface AppInfo {
    /**
     * 1. Package name.
     * 2. Package information is required when the file transfer progress is obtained.
     *
     * @syscap SystemCapability.Health.WearEngine.Lite
     * @famodelonly
     * @since 26.0.0
     */
    bundleName: string;
    /**
     * 1. App fingerprint.
     * 2. App fingerprint information is required when the file transfer progress is obtained.
     *
     * @syscap SystemCapability.Health.WearEngine.Lite
     * @famodelonly
     * @since 26.0.0
     */
    fingerprint: string;
}
/**
 * 1. Callback for file receiving.
 * 2. This callback is required when the file transfer progress is obtained.
 *
 * @syscap SystemCapability.Health.WearEngine.Lite
 * @famodelonly
 * @since 26.0.0
 */
export interface FileReceiverCallback {
    /**
     * 1. Receiver of the progress and file information during file transfer.
     * 2. This method is used to obtain related information during file transfer.
     *
     * @param { string } fileName  - 1. File name.
     *     2. This parameter is used when the file transfer progress is obtained.
     * @param { string } filePath  - 1. File path.
     *     2. This parameter is used when the file transfer progress is obtained.
     * @param { number } progress  - 1. File receiving progress.
     *     2. This parameter is used for file receiving.
     *     <br>Value range: [0,100]
     * @syscap SystemCapability.Health.WearEngine.Lite
     * @famodelonly
     * @since 26.0.0
     */
    onReceive(fileName: string, filePath: string, progress: number): void;
    /**
     * 1. Callback triggered when the API is called successfully.
     * 2. The callback is used when the file transfer progress is obtained.
     *
     * @param { number } code  - 1. Result code of the API call.
     *     2. This parameter is used when the file transfer progress is obtained.
     * @param { string } [data]  - 1. Detailed description of the result code.
     *     2. This parameter is used when the file transfer progress is obtained.
     * @syscap SystemCapability.Health.WearEngine.Lite
     * @famodelonly
     * @since 26.0.0
     */
    success(code: number, data?: string): void;
    /**
     * 1. Callback triggered when the API fails to be called.
     * 2. The callback is used when the file transfer progress is obtained.
     *
     * @param { number } code  - 1. Error code of the API call failure.
     *     2. This parameter is used when the file transfer progress is obtained.
     * @param { string } [data]  - 1. Detailed description of the error code.
     *     2. This parameter is used when the file transfer progress is obtained.
     * @syscap SystemCapability.Health.WearEngine.Lite
     * @famodelonly
     * @since 26.0.0
     */
    fail(code: number, data?: string): void;
}
/**
 * 1. Provides an API for developers.
 * 2. Used when the API needs to be called.
 *
 * @syscap SystemCapability.Health.WearEngine.Lite
 * @famodelonly
 * @since 6.1.1(24)
 */
export default class WearEngineLite {
    /**
     * 1. Subscribes to the device connection status.
     * 2. This method is used to subscribe to the device connection status.
     *
     * @param { MonitorEventCallback } callback  - 1. Event callback.
     *     2. This callback is used to notify developers when the listened event changes.
     * @syscap SystemCapability.Health.WearEngine.Lite
     * @famodelonly
     * @since 6.1.1(24)
     * @see [offConnectionStateChange]{@link WearEngineLite.offConnectionStateChange} which cancels the listening to the connection service.
     */
    static onConnectionStateChange(callback: MonitorEventCallback): void;
    /**
     * 1. Cancels the listening to the connection service.
     * 2. This method is used to cancel the listening to the connection service.
     *
     * @param { MonitorEventCallback } [callback] - 1. Connection status event.
     *     2. Represents the connection status event for which the listening needs to be canceled.
     * @syscap SystemCapability.Health.WearEngine.Lite
     * @famodelonly
     * @since 6.1.1(24)
     * @see [onConnectionStateChange]{@link WearEngineLite.onConnectionStateChange} which subscribes to the device connection status.
     */
    static offConnectionStateChange(callback?: MonitorEventCallback): void;
    /**
     * 1. Registers a file receiver.
     * 2. This method is used for receiving files.
     *
     * @param { AppInfo } remoteAppInfo  - 1. App information on the peer device.
     *     2. This parameter is used to obtain the file transfer progress.
     * @param { FileReceiverCallback } callback  - 1. Callback function of the file receiver.
     *     2. The callback is used for registering a file receiver.
     * @syscap SystemCapability.Health.WearEngine.Lite
     * @famodelonly
     * @since 26.0.0
     * @see [offFileReceive]{@link WearEngineLite.offFileReceive} which unregisters a file receiver.
     */
    static onFileReceive(remoteAppInfo: AppInfo, callback: FileReceiverCallback): void;
    /**
     * 1. Unregisters a file receiver.
     * 2. This method is used for unregistering a file receiver.
     *
     * @param { AppInfo } remoteAppInfo  - 1. App information on the peer device.
     *     2. This parameter is used to obtain the file transfer progress.
     * @param { FileReceiverCallback } [callback] - 1. The specific file‑reception listener to unregister.
     *     2. Represents file reception progress event for which the listening needs to be canceled.
     * @syscap SystemCapability.Health.WearEngine.Lite
     * @famodelonly
     * @since 26.0.0
     * @see [onFileReceive]{@link WearEngineLite.onFileReceive} which registers a file receiver.
     */
    static offFileReceive(remoteAppInfo: AppInfo, callback?: FileReceiverCallback): void;
}

```
