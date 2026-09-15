# @ohos.app.ability.PrintExtensionAbility.d.ts

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
import type PrintExtensionContext from './application/PrintExtensionContext';
import type Want from './@ohos.app.ability.Want';
import type print from './@ohos.print';
/**
 * class of print extensionAbility.
 *
 * @syscap SystemCapability.Print.PrintFramework
 * @stagemodelonly
 * @since 14
 */
declare class PrintExtensionAbility {
    /**
     * Indicates print service extension ability context.
     *
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 26.0.0
     */
    context: PrintExtensionContext;
    /**
     * Called once to initialize the extensionAbility.
     * @param { Want } want - call print page want params.
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 14
     */
    onCreate(want: Want): void;
    /**
     * Called once to start to discover the printers connected with the device.
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 14
     */
    onStartDiscoverPrinter(): void;
    /**
     * Called once to stop discovering the printer.
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 14
     */
    onStopDiscoverPrinter(): void;
    /**
     * Called once to connect to the specific printer.
     * @param { number } printerId - connect the printerId.
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 14
     */
    onConnectPrinter(printerId: number): void;
    /**
     * Called once to disconnect to the specific printer.
     * @param { number } printerId - connect the printerId.
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 14
     */
    onDisconnectPrinter(printerId: number): void;
    /**
     * Called once to start print job.
     * @param { print.PrintJob } jobInfo - Indicates the information of print job.
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 24
     */
    public onStartPrintJob(jobInfo: print.PrintJob): void;
    /**
     * Called once to remove the print job has been started.
     * @param { print.PrintJob } jobInfo - Indicates the information of print job.
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 24
     */
    public onCancelPrintJob(jobInfo: print.PrintJob): void;
    /**
     * Called once to request the printer's capabilities.
     * @param { number } printerId - Indicates the information of printer.
     * @returns { print.PrinterCapability } printer capability.
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 24
     */
    public onRequestPrinterCapability(printerId: number): print.PrinterCapability;
    /**
     * Called once to finalize the extensionAbility.
     * @syscap SystemCapability.Print.PrintFramework
     * @stagemodelonly
     * @since 14
     */
    onDestroy(): void;
}
export default PrintExtensionAbility;

```
