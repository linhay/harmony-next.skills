# @ohos.print.d.ts

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
 * @kit BasicServicesKit
 */
import type { AsyncCallback, Callback } from './@ohos.base';
import type Context from './application/Context';
/**
 * The **print** module provides APIs for basic print operations.
 *
 * @syscap SystemCapability.Print.PrintFramework
 * @since 10
 */
declare namespace print {
    /**
     * Implements event listeners for print jobs.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 10
     */
    interface PrintTask {
        /**
         * Subscribes to the block events of a print job. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.PRINT
         * @param { 'block' } type - Listening type.<br>The value is fixed at **'block'**.<br>It means that the print job is
         *     blocked.
         * @param { Callback<void> } callback - Callback used to notify the caller that the print job is blocked.
         * @throws { BusinessError } 201 - the application does not have permission to call this function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @syscap SystemCapability.Print.PrintFramework
         * @since 10
         */
        on(type: 'block', callback: Callback<void>): void;
        /**
         * Subscribes to the success events of a print job. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.PRINT
         * @param { 'succeed' } type - Listening type.<br>The value is fixed at **'succeed'**.<br>It means that the print
         *     job is successful.
         * @param { Callback<void> } callback - Callback used to notify the caller that the print job is successful.
         * @throws { BusinessError } 201 - the application does not have permission to call this function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @syscap SystemCapability.Print.PrintFramework
         * @since 10
         */
        on(type: 'succeed', callback: Callback<void>): void;
        /**
         * Subscribes to the failure events of a print job. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.PRINT
         * @param { 'fail' } type - Listening type.<br>The value is fixed at **'fail'**.<br>It means that the print job is
         *     failed.
         * @param { Callback<void> } callback - Callback used to notify the caller that the print job is failed.
         * @throws { BusinessError } 201 - the application does not have permission to call this function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @syscap SystemCapability.Print.PrintFramework
         * @since 10
         */
        on(type: 'fail', callback: Callback<void>): void;
        /**
         * Subscribes to the cancellation events of a print job. This API uses an asynchronous callback to return the
         * result.
         *
         * @permission ohos.permission.PRINT
         * @param { 'cancel' } type - Listening type.<br>The value is fixed at **'cancel'**.<br>It means that the print job
         *     is canceled.
         * @param { Callback<void> } callback - Callback used to notify the caller that the print job is canceled.
         * @throws { BusinessError } 201 - the application does not have permission to call this function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @syscap SystemCapability.Print.PrintFramework
         * @since 10
         */
        on(type: 'cancel', callback: Callback<void>): void;
        /**
         * Unsubscribes from the block events of a print job. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.PRINT
         * @param { 'block' } type - Listening type.<br>The value is fixed at **'block'**.<br>It means that the print job is
         *     blocked.
         * @param { Callback<void> } callback - Callback used to unsubscribe from the block events of a specified print job.
         * @throws { BusinessError } 201 - the application does not have permission to call this function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @syscap SystemCapability.Print.PrintFramework
         * @since 10
         */
        off(type: 'block', callback?: Callback<void>): void;
        /**
         * Unsubscribes from the success events of a print job. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.PRINT
         * @param { 'succeed' } type - Listening type.<br>The value is fixed at **'succeed'**.<br>It means that the print
         *     job is successful.
         * @param { Callback<void> } callback - Callback used to unsubscribe from the success events of a specified print
         *     job.
         * @throws { BusinessError } 201 - the application does not have permission to call this function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @syscap SystemCapability.Print.PrintFramework
         * @since 10
         */
        off(type: 'succeed', callback?: Callback<void>): void;
        /**
         * Unsubscribes from the failure events of a print job. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.PRINT
         * @param { 'fail' } type - Listening type.<br>The value is fixed at **'fail'**.<br>It means that the print job is
         *     failed.
         * @param { Callback<void> } callback - Callback used to unsubscribe from the failure events of a specified print
         *     job.
         * @throws { BusinessError } 201 - the application does not have permission to call this function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @syscap SystemCapability.Print.PrintFramework
         * @since 10
         */
        off(type: 'fail', callback?: Callback<void>): void;
        /**
         * Unsubscribes from the cancellation events of a print job. This API uses an asynchronous callback to return the
         * result.
         *
         * @permission ohos.permission.PRINT
         * @param { 'cancel' } type - Listening type.<br>The value is fixed at **'cancel'**.<br>It means that the print job
         *     is canceled.
         * @param { Callback<void> } callback - Callback used to unsubscribe from the cancellation events of a specified
         *     print job.
         * @throws { BusinessError } 201 - the application does not have permission to call this function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @syscap SystemCapability.Print.PrintFramework
         * @since 10
         */
        off(type: 'cancel', callback?: Callback<void>): void;
    }
    /**
     * Provides information about the document to print. This API must be implemented by a third-party application.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 11
     */
    interface PrintDocumentAdapter {
        /**
         * Sends an empty PDF file descriptor to a third-party application. The third-party application updates the file
         * with the new print attributes and then calls **writeResultCallback** to print the file.
         *
         * @permission ohos.permission.PRINT
         * @param { string } jobId - ID of the print job.
         * @param { PrintAttributes } oldAttrs - Old print attributes.
         * @param { PrintAttributes } newAttrs - New print attributes.
         * @param { number } fd - PDF file descriptor sent to the API caller.
         * @param { function } writeResultCallback - Callback used to print the updated file.
         * @throws { BusinessError } 201 - the application does not have permission to call this function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        onStartLayoutWrite(jobId: string, oldAttrs: PrintAttributes, newAttrs: PrintAttributes, fd: number, writeResultCallback: (jobId: string, writeResult: PrintFileCreationState) => void): void;
        /**
         * Registers a listener for print job state changes.
         *
         * @permission ohos.permission.PRINT
         * @param { string } jobId - ID of the print job.
         * @param { PrintDocumentAdapterState } state - New state of the print job.
         * @throws { BusinessError } 201 - the application does not have permission to call this function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        onJobStateChanged(jobId: string, state: PrintDocumentAdapterState): void;
    }
    /**
     * Prints files. This API uses an asynchronous callback to return the result. To start the system print preview page,
     * call the [print]{@link print.print(files: Array<string>, context: Context)} API and pass in context.
     *
     * @permission ohos.permission.PRINT
     * @param { Array<string> } files - List of files to print. Images (in .jpg, .png, .gif, .bmp, or .webp format) and
     *     PDF files are supported. You should save the files to the application sandbox, obtain the sandbox URI through
     *     **fileUri.getUriFromPath**, and then pass this URI as a parameter to this API.
     * @param { AsyncCallback<PrintTask> } callback - Callback to be invoked when the print job is finished.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 10
     * @deprecated since 26.0.0
     * @useinstead print#print
     */
    function print(files: Array<string>, callback: AsyncCallback<PrintTask>): void;
    /**
     * Prints files. This API uses a promise to return the result. To start the system print preview page, call the
     * [print]{@link print.print(files: Array<string>, context: Context)} API and pass in context.
     *
     * @permission ohos.permission.PRINT
     * @param { Array<string> } files - List of files to print. Images (in .jpg, .png, .gif, .bmp, or .webp format) and
     *     PDF files are supported. You should save the files to the application sandbox, obtain the sandbox URI through
     *     **fileUri.getUriFromPath**, and then pass this URI as a parameter to this API.
     * @returns { Promise<PrintTask> } Promise used to return a [PrintTask]{@link print.PrintTask} object.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 10
     * @deprecated since 26.0.0
     * @useinstead print#print
     */
    function print(files: Array<string>): Promise<PrintTask>;
    /**
     * Prints files. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.PRINT
     * @param { Array<string> } files - List of files to be printed. Currently, the following file types are supported: "
     *     .bm", ".bmp", ".doc", ".docm", ".docx", ".dot", ".dotm", ".dotx", ".gif", ".jfif", ".jpe", ".jpeg", ".jpg", "
     *     pdf", ".pot", ".potm", ".potx", ".pps", ".ppsm", ".ppsx", ".ppt", ".pptm", ".pptx", ".png", ".rtf", ".txt", "
     *     .webp", ".wps", ".xls", ".xlsb", ".xlsm", ".xlsx", ".xlt", ".xltx", and ".xml". You should save the files to
     *     the application sandbox, obtain the sandbox URI through **fileUri.getUriFromPath**, and then pass this URI as a
     *     parameter to this API.
     * @param { Context } context - UIAbilityContext used to start the system print UI.
     * @param { AsyncCallback<PrintTask> } callback - Callback to be invoked when the print job is finished.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 11
     */
    function print(files: Array<string>, context: Context, callback: AsyncCallback<PrintTask>): void;
    /**
     * Prints files. This API uses a promise to return the result.
     *
     * @permission ohos.permission.PRINT
     * @param { Array<string> } files - List of files to be printed. Currently, the following file types are supported: "
     *     .bm", ".bmp", ".doc", ".docm", ".docx", ".dot", ".dotm", ".dotx", ".gif", ".jfif", ".jpe", ".jpeg", ".jpg", "
     *     pdf", ".pot", ".potm", ".potx", ".pps", ".ppsm", ".ppsx", ".ppt", ".pptm", ".pptx", ".png", ".rtf", ".txt", "
     *     .webp", ".wps", ".xls", ".xlsb", ".xlsm", ".xlsx", ".xlt", ".xltx", and ".xml". You should save the files to
     *     the application sandbox, obtain the sandbox URI through **fileUri.getUriFromPath**, and then pass this URI as a
     *     parameter to this API.
     * @param { Context } context - UIAbilityContext used to start the system print UI.
     * @returns { Promise<PrintTask> } Promise used to return a [PrintTask]{@link print.PrintTask} object.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 11
     */
    function print(files: Array<string>, context: Context): Promise<PrintTask>;
    /**
     * Prints a file. This API uses a promise to return the result.
     *
     * @permission ohos.permission.PRINT
     * @param { string } jobName - Name of the file to print, for example, **test.pdf**. The printer uses the
     *     [onStartLayoutWrite]{@link print.PrintDocumentAdapter.onStartLayoutWrite} API to send the **fd** of the empty
     *     PDF file to the API caller. The API caller uses the new print attributes to update the file to print.
     * @param { PrintDocumentAdapter } printAdapter - [PrintDocumentAdapter]{@link print.PrintDocumentAdapter} API
     *     instance implemented by a third-party application.
     * @param { PrintAttributes } printAttributes - Print attributes.
     * @param { Context } context - UIAbilityContext used to start the system print UI.
     * @returns { Promise<PrintTask> } Promise used to return a [PrintTask]{@link print.PrintTask} object.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 11
     */
    function print(jobName: string, printAdapter: PrintDocumentAdapter, printAttributes: PrintAttributes, context: Context): Promise<PrintTask>;
    /**
     * Defines the print attributes.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 11
     */
    interface PrintAttributes {
        /**
         * Number of printed file copies. The default value is **1**.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        copyNumber?: number;
        /**
         * Page range of the file to print.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        pageRange?: PrintPageRange;
        /**
         * Page size of the file to print.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        pageSize?: PrintPageSize | PrintPageType;
        /**
         * Print direction mode.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        directionMode?: PrintDirectionMode;
        /**
         * Color mode of the files to print.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        colorMode?: PrintColorMode;
        /**
         * Duplex mode of the files to print.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        duplexMode?: PrintDuplexMode;
    }
    /**
     * Defines the print range.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 11
     */
    interface PrintPageRange {
        /**
         * Start page. The default value is **1**.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        startPage?: number;
        /**
         * End page. The default value is the maximum number of pages of the file to be printed.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        endPage?: number;
        /**
         * Page range set of the file to print. The default value is empty.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        pages?: Array<number>;
    }
    /**
     * Defines the page margins for printing.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 24
     */
    interface PrintMargin {
        /**
         * Top margin of the page, in millimeters. The default value is **0**.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        top?: number;
        /**
         * Bottom margin of the page, in millimeters. The default value is **0**.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        bottom?: number;
        /**
         * Left margin of the page, in millimeters. The default value is **0**.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        left?: number;
        /**
         * Right margin of the page, in millimeters. The default value is **0**.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        right?: number;
    }
    /**
     * Defines the print range.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 24
     */
    interface PrinterRange {
        /**
         * Start page. The default value is **1**.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        startPage?: number;
        /**
         * End page. The default value is the maximum number of pages of the file to be printed.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        endPage?: number;
        /**
         * Page range set of the file to print. The default value is empty.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        pages?: Array<number>;
    }
    /**
     * Defines the print preview attributes.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 24
     */
    interface PreviewAttribute {
        /**
         * Preview page range.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        previewRange: PrinterRange;
        /**
         * Print preview result. The default value is **-1**.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        result?: number;
    }
    /**
     * Defines the resolution for printing.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 24
     */
    interface PrintResolution {
        /**
         * Resolution ID.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        id: string;
        /**
         * Horizontal DPI.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        horizontalDpi: number;
        /**
         * Vertical DPI.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        verticalDpi: number;
    }
    /**
     * Defines the size of the printed page.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 11
     */
    interface PrintPageSize {
        /**
         * Paper size ID.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        id: string;
        /**
         * Paper size name.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        name: string;
        /**
         * Page width, in millimeters.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        width: number;
        /**
         * Page height, in millimeters.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        height: number;
    }
    /**
     * Defines the printer capabilities.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 24
     */
    interface PrinterCapability {
        /**
         * Color mode.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        colorMode: number;
        /**
         * Simplex or duplex mode.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        duplexMode: number;
        /**
         * List of page sizes supported by the printer.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        pageSize: Array<PrintPageSize>;
        /**
         * List of resolutions supported by the printer.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        resolution?: Array<PrintResolution>;
        /**
         * Minimum margin of the printer.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        minMargin?: PrintMargin;
        /**
         * Printer options. The value is a JSON object string.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        options?: Object;
    }
    /**
     * Provides the printer information.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 24
     */
    interface PrinterInfo {
        /**
         * Printer ID.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        printerId: string;
        /**
         * Printer name.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        printerName: string;
        /**
         * Printer state.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        printerState: PrinterState;
        /**
         * Resource ID of the printer icon. The default value is **-1**.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        printerIcon?: number;
        /**
         * Printer description.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        description?: string;
        /**
         * Printer capability.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        capability?: PrinterCapability;
        /**
         * Printer options. The value is a JSON object string.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        options?: Object;
    }
    /**
     * Defines a print job.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 24
     */
    interface PrintJob {
        /**
         * FD list of files to print.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        fdList: Array<number>;
        /**
         * ID of the print job.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        jobId: string;
        /**
         * ID of the printer used for printing.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        printerId: string;
        /**
         * State of the print job.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        jobState: PrintJobState;
        /**
         * Substate of the print job.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        jobSubstate: PrintJobSubState;
        /**
         * Copy of the file list.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        copyNumber: number;
        /**
         * Print range.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        pageRange: PrinterRange;
        /**
         * Whether the printing is sequential. The value **true** means that the printing is sequential, and **false** means
         * the opposite. The default value is **false**.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        isSequential: boolean;
        /**
         * Selected page size.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        pageSize: PrintPageSize;
        /**
         * Whether pages are printed in landscape mode. The value **true** indicates that pages are printed in landscape
         * mode, and **false** indicates that pages are printed in portrait mode. The default value is **false**.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        isLandscape: boolean;
        /**
         * Color mode.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        colorMode: number;
        /**
         * Simplex or duplex mode.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        duplexMode: number;
        /**
         * Current page margin.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        margin?: PrintMargin;
        /**
         * Preview settings.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        preview?: PreviewAttribute;
        /**
         * Printer options. The value is a JSON object string.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 24
         */
        options?: Object;
        /**
         * Vendor-specific job options in JSON format.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 26.0.0
         */
        vendorOptions?: string;
    }
    /**
     * Defines a print job.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 23
     */
    interface PrintJobData {
        /**
         * Printer ID.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        printerId: string;
        /**
         * Name of the print job.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        jobName: string;
        /**
         * Format of the print data.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        documentFormat: PrintDocumentFormat;
        /**
         * Data source type.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        docFlavor: DocFlavor;
        /**
         * Number of file list copies.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        copyNumber: number;
        /**
         * Whether pages are printed in landscape mode. The value **true** indicates that pages are printed in landscape
         * mode, and **false** indicates that pages are printed in portrait mode. The default value is **false**.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        isLandscape: boolean;
        /**
         * Color mode.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        colorMode: PrintColorMode;
        /**
         * Simplex or duplex mode.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        duplexMode: PrintDuplexMode;
        /**
         * Selected page size.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        pageSize: PrintPageSize;
        /**
         * Unique identifier of the print job.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        jobId?: string;
        /**
         * FD list of files to print.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        fdList?: number[];
        /**
         * Binary data to print.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        binaryData?: Uint8Array;
        /**
         * Print quality.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        printQuality?: PrintQuality;
        /**
         * Type of the paper to print.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        mediaType?: string;
        /**
         * Whether to print without margins. The value **true** means to print without margins, and **false** means the
         * opposite. Default value: **true**.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        isBorderless?: boolean;
        /**
         * Whether to automatically rotate the page. The value **true** means to automatically rotate the page, and
         * **false** means the opposite. Default value: **true**.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        isAutoRotate?: boolean;
        /**
         * Whether pages are printed in reverse order. The value **true** means that pages are printed in reverse order, and
         * **false** means that pages are printed in normal order. The default value is **false**.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        isReverse?: boolean;
        /**
         * Whether pages are printed uncollated. The value **true** means that pages are printed uncollated, and **false**
         * means the opposite. Default value: **true**.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        isCollate?: boolean;
        /**
         * Whether pages are printed in sequential order.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        isSequential?: boolean;
        /**
         * Object stringified in JSON format.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        options?: string;
        /**
         * Vendor-specific job options in JSON format.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 26.0.0
         */
        vendorOptions?: string;
    }
    /**
     * Enumerates the data formats.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 23
     */
    enum PrintDocumentFormat {
        /**
         * Auto-detected format.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        DOCUMENT_FORMAT_AUTO = 0,
        /**
         * JPEG.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        DOCUMENT_FORMAT_JPEG = 1,
        /**
         * PDF.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        DOCUMENT_FORMAT_PDF = 2,
        /**
         * PostScript.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        DOCUMENT_FORMAT_POSTSCRIPT = 3,
        /**
         * Text.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        DOCUMENT_FORMAT_TEXT = 4,
        /**
         * RAW.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        DOCUMENT_FORMAT_RAW = 5
    }
    /**
     * Enumerates the data source types for printing.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 23
     */
    enum DocFlavor {
        /**
         * File data.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        FILE_DESCRIPTOR = 0,
        /**
         * Binary data.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 23
         */
        BYTES = 1
    }
    /**
     * Prints a file or binary data. This API uses a promise to return the result.
     *
     * @permission ohos.permission.PRINT
     * @param { PrintJobData } job - Print job data.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 23
     */
    function startPrint(job: PrintJobData): Promise<void>;
    /**
     * Enumerates the print direction modes.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 11
     */
    enum PrintDirectionMode {
        /**
         * Automatic.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        DIRECTION_MODE_AUTO = 0,
        /**
         * Portrait mode.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        DIRECTION_MODE_PORTRAIT = 1,
        /**
         * Landscape mode.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        DIRECTION_MODE_LANDSCAPE = 2
    }
    /**
     * Enumerates the color modes.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 11
     */
    enum PrintColorMode {
        /**
         * Black and white.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        COLOR_MODE_MONOCHROME = 0,
        /**
         * Color.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        COLOR_MODE_COLOR = 1
    }
    /**
     * Enumerates the duplex modes.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 11
     */
    enum PrintDuplexMode {
        /**
         * Simplex (single-sided).
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        DUPLEX_MODE_NONE = 0,
        /**
         * Duplex (double-sided) with flipping on long edge.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        DUPLEX_MODE_LONG_EDGE = 1,
        /**
         * Duplex (double-sided) with flipping on short edge.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        DUPLEX_MODE_SHORT_EDGE = 2
    }
    /**
     * Enumerates the print page types.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 11
     */
    enum PrintPageType {
        /**
         * A3.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        PAGE_ISO_A3 = 0,
        /**
         * A4.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        PAGE_ISO_A4 = 1,
        /**
         * A5.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        PAGE_ISO_A5 = 2,
        /**
         * B5.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        PAGE_JIS_B5 = 3,
        /**
         * C5.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        PAGE_ISO_C5 = 4,
        /**
         * DL.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        PAGE_ISO_DL = 5,
        /**
         * Letter.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        PAGE_LETTER = 6,
        /**
         * Legal.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        PAGE_LEGAL = 7,
        /**
         * 4 x 6 photo paper.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        PAGE_PHOTO_4X6 = 8,
        /**
         * 5 x 7 photo paper.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        PAGE_PHOTO_5X7 = 9,
        /**
         * International envelope DL.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        PAGE_INT_DL_ENVELOPE = 10,
        /**
         * B Tabloid.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        PAGE_B_TABLOID = 11
    }
    /**
     * Enumerates the print job states.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 11
     */
    enum PrintDocumentAdapterState {
        /**
         * The preview fails.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        PREVIEW_DESTROY = 0,
        /**
         * The print job is successful.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        PRINT_TASK_SUCCEED = 1,
        /**
         * The print job is failed.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        PRINT_TASK_FAIL = 2,
        /**
         * The print job is canceled.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        PRINT_TASK_CANCEL = 3,
        /**
         * The print job is blocked.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        PRINT_TASK_BLOCK = 4
    }
    /**
     * Enumerates the print file creation status.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 11
     */
    enum PrintFileCreationState {
        /**
         * The print file is created successfully.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        PRINT_FILE_CREATED = 0,
        /**
         * The print file fails to be created.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        PRINT_FILE_CREATION_FAILED = 1,
        /**
         * The print file is successfully created but not rendered.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 11
         */
        PRINT_FILE_CREATED_UNRENDERED = 2
    }
    /**
     * Enumerates the printer states.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 14
     */
    enum PrinterState {
        /**
         * A new printer is added.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINTER_ADDED = 0,
        /**
         * The printer is removed.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINTER_REMOVED = 1,
        /**
         * The printer is updated.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINTER_CAPABILITY_UPDATED = 2,
        /**
         * The printer is connected.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINTER_CONNECTED = 3,
        /**
         * The printer is disconnected.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINTER_DISCONNECTED = 4,
        /**
         * The printer is running.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINTER_RUNNING = 5
    }
    /**
     * Enumerates the print job states.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 14
     */
    enum PrintJobState {
        /**
         * The printer is prepared for the print job.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_PREPARE = 0,
        /**
         * The print job is on the print queue of the printer.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_QUEUED = 1,
        /**
         * The print job is being executed.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_RUNNING = 2,
        /**
         * The print job is blocked.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCKED = 3,
        /**
         * The print job is complete.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_COMPLETED = 4
    }
    /**
     * Enumerates the print job substates.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 14
     */
    enum PrintJobSubState {
        /**
         * The print job is successful.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_COMPLETED_SUCCESS = 0,
        /**
         * The print job is failed.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_COMPLETED_FAILED = 1,
        /**
         * The print job is canceled by user.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_COMPLETED_CANCELLED = 2,
        /**
         * The print file is corrupted.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_COMPLETED_FILE_CORRUPTED = 3,
        /**
         * The printer is offline.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_OFFLINE = 4,
        /**
         * The printer is occupied by another process.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_BUSY = 5,
        /**
         * The print job is canceled due to a block.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_CANCELLED = 6,
        /**
         * The printer is out of paper.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_OUT_OF_PAPER = 7,
        /**
         * The printer is out of ink.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_OUT_OF_INK = 8,
        /**
         * The printer is out of toner.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_OUT_OF_TONER = 9,
        /**
         * The printer is in a paper jam.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_JAMMED = 10,
        /**
         * The printer door is open.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_DOOR_OPEN = 11,
        /**
         * Print service request.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_SERVICE_REQUEST = 12,
        /**
         * The printer is low on ink.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_LOW_ON_INK = 13,
        /**
         * The printer is low on toner.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_LOW_ON_TONER = 14,
        /**
         * The printer is extremely low on ink.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_REALLY_LOW_ON_INK = 15,
        /**
         * The print certificate is incorrect.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_BAD_CERTIFICATE = 16,
        /**
         * The print driver is abnormal.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 20
         */
        PRINT_JOB_BLOCK_DRIVER_EXCEPTION = 17,
        /**
         * There is an error with the printer account.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_ACCOUNT_ERROR = 18,
        /**
         * There is an error with the printer permission.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_PRINT_PERMISSION_ERROR = 19,
        /**
         * There is an error with the color printing permission.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_PRINT_COLOR_PERMISSION_ERROR = 20,
        /**
         * The printer fails to connect to the network.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_NETWORK_ERROR = 21,
        /**
         * The printer fails to connect to the server.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_SERVER_CONNECTION_ERROR = 22,
        /**
         * There is an error with a large file printing.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_LARGE_FILE_ERROR = 23,
        /**
         * There is an error with file parsing.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_FILE_PARSING_ERROR = 24,
        /**
         * The file conversion is slow.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_SLOW_FILE_CONVERSION = 25,
        /**
         * The file is uploading.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_RUNNING_UPLOADING_FILES = 26,
        /**
         * The file is converting.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_RUNNING_CONVERTING_FILES = 27,
        /**
         * The file fails to be uploaded.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 18
         */
        PRINT_JOB_BLOCK_FILE_UPLOADING_ERROR = 30,
        /**
         * The print driver is missing.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 20
         */
        PRINT_JOB_BLOCK_DRIVER_MISSING = 34,
        /**
         * The print job is interrupted.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 20
         */
        PRINT_JOB_BLOCK_INTERRUPT = 35,
        /**
         * The printer is unavailable.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 20
         */
        PRINT_JOB_BLOCK_PRINTER_UNAVAILABLE = 98,
        /**
         * There is an unknown error with the printer.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINT_JOB_BLOCK_UNKNOWN = 99
    }
    /**
     * Enumerates the print error codes.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 14
     */
    enum PrintErrorCode {
        /**
         * No error.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        E_PRINT_NONE = 0,
        /**
         * No permission.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        E_PRINT_NO_PERMISSION = 201,
        /**
         * Invalid parameters.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        E_PRINT_INVALID_PARAMETER = 401,
        /**
         * Printing failure.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        E_PRINT_GENERIC_FAILURE = 13100001,
        /**
         * RPC failure.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        E_PRINT_RPC_FAILURE = 13100002,
        /**
         * Print service failure.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        E_PRINT_SERVER_FAILURE = 13100003,
        /**
         * Invalid printer extension.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        E_PRINT_INVALID_EXTENSION = 13100004,
        /**
         * Invalid printer.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        E_PRINT_INVALID_PRINTER = 13100005,
        /**
         * Invalid print job.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        E_PRINT_INVALID_PRINT_JOB = 13100006,
        /**
         * Incorrect file input/output.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        E_PRINT_FILE_IO = 13100007,
        /**
         * Excessive files. Maximum number: 99.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 18
         */
        E_PRINT_TOO_MANY_FILES = 13100010,
        /**
         * The SMB account is locked due to multiple failed login attempts.
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 24
         */
        E_PRINT_SMB_LOGIN_LOCKOUT = 13100012,
        /**
         * SMB Connection Failure (A network error occurs, the host is unreachable, or the port is blocked.)
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 24
         */
        E_PRINT_SMB_CONNECTION_FAILURE = 13100013,
        /**
         * The login account or password is invalid.
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 24
         */
        E_PRINT_SMB_INVALID_CREDENTIALS = 13100014
    }
    /**
     * Enumerates print application events.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 14
     */
    enum ApplicationEvent {
        /**
         * Starts the print application.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        APPLICATION_CREATED = 0,
        /**
         * Closes the print application by clicking **Start**.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        APPLICATION_CLOSED_FOR_STARTED = 1,
        /**
         * Closes the print application by clicking **Cancel**.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        APPLICATION_CLOSED_FOR_CANCELED = 2
    }
    /**
     * Discovers printers by specifying the extension list. The discovered printers contain the specified print extension
     * abilities. If an empty extension list is specified, all extension abilities are loaded. This API uses an
     * asynchronous callback to return the result.
     *
     * @permission ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINT
     * @param { Array<string> } extensionList - List of
     *     [PrintExtensionAbilities]{@link @ohos.app.ability.PrintExtensionAbility:PrintExtensionAbility} to be loaded.
     *     The list members are the bundle names of the applications with print extension abilities. An empty list
     *     indicates that all extension abilities are loaded.
     * @param { AsyncCallback<void> } callback - Callback to be invoked when a printer is discovered.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 20
     */
    function startDiscoverPrinter(extensionList: Array<string>, callback: AsyncCallback<void>): void;
    /**
     * Discovers printers by specifying the extension list. The discovered printers contain the specified print extension
     * abilities. If an empty extension list is specified, all extension abilities are loaded. This API uses a promise to
     * return the result.
     *
     * @permission ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINT
     * @param { Array<string> } extensionList - List of
     *     [PrintExtensionAbilities]{@link @ohos.app.ability.PrintExtensionAbility:PrintExtensionAbility} to be loaded.
     *     The list members are the bundle names of the applications with print extension abilities. An empty list
     *     indicates that all extension abilities are loaded.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 20
     */
    function startDiscoverPrinter(extensionList: Array<string>): Promise<void>;
    /**
     * Stops discovering printers. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINT
     * @param { AsyncCallback<void> } callback - Callback to be invoked when printer discovery is stopped.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 20
     */
    function stopDiscoverPrinter(callback: AsyncCallback<void>): void;
    /**
     * Stops discovering printers. This API uses a promise to return the result.
     *
     * @permission ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINT
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 20
     */
    function stopDiscoverPrinter(): Promise<void>;
    /**
     * Connects to a printer by printer ID. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINT
     * @param { string } printerId - Printer ID.
     * @param { AsyncCallback<void> } callback - Callback to be invoked when a printer is connected.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 20
     */
    function connectPrinter(printerId: string, callback: AsyncCallback<void>): void;
    /**
     * Connects to a printer by printer ID. This API uses a promise to return the result.
     *
     * @permission ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINT
     * @param { string } printerId - Printer ID.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 20
     */
    function connectPrinter(printerId: string): Promise<void>;
    /**
     * Updates the print job state. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.MANAGE_PRINT_JOB or ohos.permission.ENTERPRISE_MANAGE_PRINT
     * @param { string} jobId - ID of the print job.
     * @param { PrintJobState } state - Print job state.
     * @param { PrintJobSubState } subState - Substate of the print job.
     * @param { AsyncCallback<void> } callback - Callback to be invoked when the print job state is updated.
     * @throws { BusinessError } 201 - The application does not have permission to call this function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 24
     */
    function updatePrintJobState(jobId: string, state: PrintJobState, subState: PrintJobSubState, callback: AsyncCallback<void>): void;
    /**
     * Updates the print job state. This API uses a promise to return the result.
     *
     * @permission ohos.permission.MANAGE_PRINT_JOB or ohos.permission.ENTERPRISE_MANAGE_PRINT
     * @param { string} jobId - ID of the print job.
     * @param { PrintJobState } state - Print job state.
     * @param { PrintJobSubState } subState - Substate of the print job.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 24
     */
    function updatePrintJobState(jobId: string, state: PrintJobState, subState: PrintJobSubState): Promise<void>;
    /**
     * Obtains the list of printers added to the system. This API uses a promise to return the result.
     *
     * @permission ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINT
     * @returns { Promise<Array<string>> } Promise used to return a list of all added printers.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 18
     */
    function getAddedPrinters(): Promise<Array<string>>;
    /**
     * Adds a printer to the printer discovery list. This API uses a promise to return the result.
     *
     * @permission ohos.permission.PRINT
     * @param { PrinterInformation } printerInformation - The added printer.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 14
     */
    function addPrinterToDiscovery(printerInformation: PrinterInformation): Promise<void>;
    /**
     * Updates the printer capabilities to the printer discovery list. This API uses a promise to return the result.
     *
     * @permission ohos.permission.PRINT
     * @param { PrinterInformation } printerInformation - Printer whose capability is to be updated.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 14
     */
    function updatePrinterInDiscovery(printerInformation: PrinterInformation): Promise<void>;
    /**
     * Removes a printer from the printer discovery list. This API uses a promise to return the result.
     *
     * @permission ohos.permission.PRINT
     * @param { string } printerId - Printer to remove.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 14
     */
    function removePrinterFromDiscovery(printerId: string): Promise<void>;
    /**
     * Obtains printer information based on the printer ID. This API uses a promise to return the result.
     *
     * @permission ohos.permission.PRINT
     * @param { string } printerId - Printer ID used to obtain information.
     * @returns { Promise<PrinterInformation> } Promise used to return the printer information.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 14
     */
    function getPrinterInformationById(printerId: string): Promise<PrinterInformation>;
    /**
     * Defines the printer information.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 14
     */
    interface PrinterInformation {
        /**
         * Printer ID.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        printerId: string;
        /**
         * Printer name.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        printerName: string;
        /**
         * Printer state.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        printerStatus: PrinterStatus;
        /**
         * Printer description.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        description?: string;
        /**
         * Printer capabilities.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        capability?: PrinterCapabilities;
        /**
         * Printer URI.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        uri?: string;
        /**
         * Printer model.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        printerMake?: string;
        /**
         * Printer preferences.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 18
         */
        preferences?: PrinterPreferences;
        /**
         * Printer alias.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 18
         */
        alias?: string;
        /**
         * Information about the selected driver when adding the printer.
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 24
         */
        selectedDriver?: PpdInfo;
        /**
         * Protocol used when adding the printer.
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 24
         */
        selectedProtocol?: string;
        /**
         * Printer details.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        options?: string;
    }
    /**
     * Defines the printer capabilities.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 14
     */
    interface PrinterCapabilities {
        /**
         * List of paper sizes supported by the printer.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        supportedPageSizes: Array<PrintPageSize>;
        /**
         * List of color modes supported by the printer.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        supportedColorModes: Array<PrintColorMode>;
        /**
         * List of single- and double-sided modes supported by the printer.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        supportedDuplexModes: Array<PrintDuplexMode>;
        /**
         * List of paper types supported by the printer.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        supportedMediaTypes?: Array<string>;
        /**
         * List of print quality supported by the printer.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        supportedQualities?: Array<PrintQuality>;
        /**
         * List of print directions supported by the printer.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        supportedOrientations?: Array<PrintOrientationMode>;
        /**
         * Printer capability details.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        options?: string;
        /**
         * Ability to configure printer vendor-specific preferences.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 26.0.0
         */
        vendorPrinterPrefAbility?: string;
        /**
         * Ability to configure job vendor-specific attributes.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 26.0.0
         */
        vendorJobAttrAbility?: string;
    }
    /**
     * Enumerates the print qualities.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 14
     */
    enum PrintQuality {
        /**
         * Draft
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        QUALITY_DRAFT = 3,
        /**
         * Standard
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        QUALITY_NORMAL = 4,
        /**
         * High
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        QUALITY_HIGH = 5
    }
    /**
     * Enumerates the print directions.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 14
     */
    enum PrintOrientationMode {
        /**
         * Portrait mode.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        ORIENTATION_MODE_PORTRAIT = 0,
        /**
         * Landscape mode.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        ORIENTATION_MODE_LANDSCAPE = 1,
        /**
         * Reverse landscape mode.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        ORIENTATION_MODE_REVERSE_LANDSCAPE = 2,
        /**
         * Reverse portrait mode.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        ORIENTATION_MODE_REVERSE_PORTRAIT = 3,
        /**
         * Adaptive mode.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        ORIENTATION_MODE_NONE = 4
    }
    /**
     * Enumerates the printer states.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 14
     */
    enum PrinterStatus {
        /**
         * The printer is idle.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINTER_IDLE = 0,
        /**
         * The printer is busy.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINTER_BUSY = 1,
        /**
         * The printer is unavailable.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 14
         */
        PRINTER_UNAVAILABLE = 2
    }
    /**
     * Defines the printer preferences.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 18
     */
    interface PrinterPreferences {
        /**
         * Default duplex mode.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 18
         */
        defaultDuplexMode?: PrintDuplexMode;
        /**
         * Default print quality.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 18
         */
        defaultPrintQuality?: PrintQuality;
        /**
         * Default paper type.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 18
         */
        defaultMediaType?: string;
        /**
         * ID of the default paper size. The value can be a standard paper size defined by the International Organization
         * for Standardization (ISO), for example, ISO_A4, or a non-standard paper size defined in the system, for example,
         * Custom.178 × 254 mm.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 18
         */
        defaultPageSizeId?: string;
        /**
         * Default print orientation.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 18
         */
        defaultOrientation?: PrintOrientationMode;
        /**
         * Whether to print without margins. The value **true** means to print without margins, and **false** means the
         * opposite. The default value is **false**.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 18
         */
        borderless?: boolean;
        /**
         * Default color mode.
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 24
         */
        defaultColorMode?: PrintColorMode;
        /**
         * Default collate.
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 24
         */
        defaultCollate?: boolean;
        /**
         * Default reverse.
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 24
         */
        defaultReverse?: boolean;
        /**
         * Other fields in the printer preferences. The fields are queried from the printer or obtained from the printer
         * driver and stored in the string in JSON format.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 18
         */
        options?: string;
        /**
         * Vendor-specific printer preferences in JSON format.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 26.0.0
         */
        vendorOptions?: string;
    }
    /**
     * Enumerates printer-related events.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 18
     */
    enum PrinterEvent {
        /**
         * Printer added.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 18
         */
        PRINTER_EVENT_ADDED = 0,
        /**
         * Printer deleted.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 18
         */
        PRINTER_EVENT_DELETED = 1,
        /**
         * Printer state changed.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 18
         */
        PRINTER_EVENT_STATE_CHANGED = 2,
        /**
         * Printer information changed.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 18
         */
        PRINTER_EVENT_INFO_CHANGED = 3,
        /**
         * Printer preferences changed.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 18
         */
        PRINTER_EVENT_PREFERENCE_CHANGED = 4,
        /**
         * The last used printer changed.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 18
         */
        PRINTER_EVENT_LAST_USED_PRINTER_CHANGED = 5
    }
    /**
     * Enumerates default printer types.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @since 18
     */
    enum DefaultPrinterType {
        /**
         * The printer set by the user serves as the default printer.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 18
         */
        DEFAULT_PRINTER_TYPE_SET_BY_USER = 0,
        /**
         * The printer used last time serves as the default printer.
         *
         * @syscap SystemCapability.Print.PrintFramework
         * @since 18
         */
        DEFAULT_PRINTER_TYPE_LAST_USED_PRINTER = 1
    }
    /**
     * Updates the information of a printer in the system. This API uses a promise to return the result. Currently, only
     * the **alias** and **options** fields of [PrinterInformation]{@link print.PrinterInformation} can be updated.
     *
     * @permission ohos.permission.MANAGE_PRINT_JOB or ohos.permission.ENTERPRISE_MANAGE_PRINT
     * @param { PrinterInformation } printerInformation - Printer information to be updated.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 24
     */
    function updatePrinterInformation(printerInformation: PrinterInformation): Promise<void>;
    /**
     * Defines a callback that takes the printer event and printer information as parameters.
     *
     * @param { PrinterEvent } event - Printer event.
     * @param { PrinterInformation } printerInformation - Printer information.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 18
     */
    type PrinterChangeCallback = (event: PrinterEvent, printerInformation: PrinterInformation) => void;
    /**
     * Registers a listener for the printer change events. This API uses a callback to return the result.
     *
     * @permission ohos.permission.PRINT
     * @param { 'printerChange' } type - Printer change event.
     * @param { PrinterChangeCallback } callback - Callback to be invoked when the printer changes.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 18
     */
    function on(type: 'printerChange', callback: PrinterChangeCallback): void;
    /**
     * Unregisters the listener for printer state change events. This API uses a callback to return the result.
     *
     * @permission ohos.permission.PRINT
     * @param { 'printerChange' } type - Printer change event.
     * @param { PrinterChangeCallback } [callback] - Callback to unregister.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
     * @syscap SystemCapability.Print.PrintFramework
     * @since 18
     */
    function off(type: 'printerChange', callback?: PrinterChangeCallback): void;
    /**
     * Interface defining shared device information
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 24
     */
    interface SharedHost {
        /**
         * IP address of the shared device.
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 24
         */
        ip: string;
        /**
         * Share name of the shared device.
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 24
         */
        shareName: string;
        /**
         * Workgroup name of the shared device.
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 24
         */
        workgroupName: string;
    }
    /**
     * defines ppd info.
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 24
     */
    interface PpdInfo {
        /**
         * Manufacturer.
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 24
         */
        manufacturer: string;
        /**
         * Nick name.
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 24
         */
        nickName: string;
        /**
         * Ppd name.
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 24
         */
        ppdName: string;
    }
    /**
     * Add a printer to system.
     * @permission ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINTER_DRIVER
     * @param { string } printerName - Indicates the printer name.
     *     <br>Name of the printer to be added.
     * @param { string } uri - Indicates the printer uri.
     *     <br>Uri of the printer to be added.
     * @param { string } [ppdName] - Indicates the ppd name.
     *     <br>Ppd name of the printer to be added.
     * @param { string } [options] - Indicates the options.
     *     <br>Optional parameters when adding a printer.
     * @returns { Promise<boolean> } the promise returned by the function.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @throws { BusinessError } 13100003 - Add the printer to system failed.
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 24
     */
    function addPrinter(printerName: string, uri: string, ppdName?: string, options?: string): Promise<boolean>;
    /**
     * Watermark handling result.
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 24
     */
    enum WatermarkHandleResult {
        /**
         * Watermark handling success.
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 24
         */
        WATERMARK_HANDLE_SUCCESS = 0,
        /**
         * Watermark handling failure.
         * @syscap SystemCapability.Print.PrintFramework
         * @stagemodelonly
         * @since 24
         */
        WATERMARK_HANDLE_FAILURE = 1
    }
    /**
     * Defines the callback type used in registering to listen for watermark handling.
     * The value of jobId indicates the print job ID.
     * The value of fd indicates the fd.
     *
     * @param { string } jobId - the print job ID
     *     <br>Print job ID in preview.
     * @param { number } fd - File Descriptor
     *     <br>File descriptor in preview.
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 24
     */
    type WatermarkCallback = (jobId: string, fd: number) => void;
    /**
     * Register to listen for watermark handling.
     * @permission ohos.permission.ENTERPRISE_MANAGE_PRINT
     * @param { WatermarkCallback } callback - Indicates the callback type used in registering to
     *     listen for watermark handling.
     *     <br>Indicates the callback type used in registering to listen for watermark handling.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 24
     */
    function registerWatermarkCallback(callback: WatermarkCallback): void;
    /**
     * Unregister to listen for watermark handling.
     * @permission ohos.permission.ENTERPRISE_MANAGE_PRINT
     * @param { WatermarkCallback } [callback] - Indicates the callback type used in registering to
     *     listen for watermark handling.
     *     <br>Indicates the callback type used in registering to listen for watermark handling.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 24
     */
    function unregisterWatermarkCallback(callback?: WatermarkCallback): void;
    /**
     * Notify watermark complete.
     * @permission ohos.permission.ENTERPRISE_MANAGE_PRINT
     * @param { string } jobId - Indicates the job ID.
     *     <br>Print job ID in preview.
     * @param { WatermarkHandleResult } result - Indicates the result.
     *     <br>Watermark processing results.
     * @throws { BusinessError } 201 - the application does not have permission to call this function.
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 24
     */
    function notifyWatermarkComplete(jobId: string, result: WatermarkHandleResult): void;
}
export default print;

```
