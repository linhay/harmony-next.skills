# @ohos.busManager.serial.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2026 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License"),
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
import { Callback } from './@ohos.base';
/**
 * Serial port management.
 *
 * @syscap SystemCapability.BusManager.Serial
 * @stagemodelonly
 * @since 26.0.0
 */
declare namespace serial {
    /**
     * Obtains the serial port list. This API returns the result asynchronously through a promise.
     *
     * @returns { Promise<SerialPort[]> } - Promise used to return the list of serial port devices.
     * @throws { BusinessError } 203 - This function is prohibited by enterprise management policies.
     * @throws { BusinessError } 35700001 - Service error.
     * @syscap SystemCapability.BusManager.Serial
     * @stagemodelonly
     * @since 26.0.0
     */
    function getSerialPortList(): Promise<SerialPort[]>;
    /**
     * Serial port object, which provides information and communication capabilities of the serial port device.
     *
     * @syscap SystemCapability.BusManager.Serial
     * @stagemodelonly
     * @since 26.0.0
     */
    interface SerialPort {
        /**
         * Serial port information.
         *
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly portInfo: SerialPortInfo;
        /**
         * Enables the port. This API returns the result asynchronously through a promise.
         *
         * @param { SerialConfigs } [config] - Serial port communication parameter.
         *     <br>Default value: Refer to the default value of SerialConfigs.
         *
         * @returns { Promise<void> } - Promise that returns no value.
         * @throws { BusinessError } 35700001 - Service error.
         * @throws { BusinessError } 35700002 - Invalid parameter.
         * @throws { BusinessError } 35700003 - Virtual serial port disconnected.
         * @throws { BusinessError } 35700004 - Port already in use.
         * @throws { BusinessError } 35700007 - User authorization required.
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        open(config?: SerialConfigs): Promise<void>;
        /**
         * Closes the serial port device. This API returns the result asynchronously through a promise.
         *
         * @returns { Promise<void> } - Promise that returns no value.
         * @throws { BusinessError } 35700001 - Service error.
         * @throws { BusinessError } 35700005 - Port not open.
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        close(): Promise<void>;
        /**
         * Sends data. This API returns the result asynchronously through a promise.
         *
         * @param { Uint8Array } data - Data to be sent.
         *     <br>Length range: (0, 4096]
         * @param { number } [timeout] - Timeout interval.
         *     <br>Length range: [0, 300000]. The value must be an integer, in milliseconds. The default value is 0,
         *     indicating that when data cannot be written to the port, the API does not wait and directly returns 0.
         * @returns { Promise<number> } - Promise used to return the length of the data written.
         * @throws { BusinessError } 35700001 - Service error.
         * @throws { BusinessError } 35700002 - Invalid parameter.
         * @throws { BusinessError } 35700003 - Virtual serial port disconnected.
         * @throws { BusinessError } 35700005 - Port not open.
         * @throws { BusinessError } 35700006 - Transmission timeout.
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        write(data: Uint8Array, timeout?: number): Promise<number>;
        /**
         * Listens for data received by the serial port. This API uses an asynchronous callback to return the result.
         * When {@link close} is called, all callbacks are cleared.
         *
         * @param { Callback<Uint8Array> } callback - Callback used to return the data received by the serial port.
         * @throws { BusinessError } 35700001 - Service error.
         * @throws { BusinessError } 35700003 - Virtual serial port disconnected.
         * @throws { BusinessError } 35700005 - Port not open.
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        onDataRead(callback: Callback<Uint8Array>): void;
        /**
         * Cancels listening for data receiving events on the serial port.
         *
         * @param { Callback<Uint8Array> } [callback] - Callback used to return the data received by the serial port.
         *     <br>Default value: Clear all listeners for data receiving events on the serial port.
         * @throws { BusinessError } 35700001 - Service error.
         * @throws { BusinessError } 35700005 - Port not open.
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        offDataRead(callback?: Callback<Uint8Array>): void;
        /**
         * Flushes the serial port buffer. This API returns the result asynchronously through a promise.
         *
         * @returns { Promise<void> } - Promise that returns no value.
         * @throws { BusinessError } 35700001 - Service error.
         * @throws { BusinessError } 35700003 - Virtual serial port disconnected.
         * @throws { BusinessError } 35700005 - Port not open.
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        flush(): Promise<void>;
        /**
         * Waits until all write requests are complete. This API returns the result asynchronously through a promise.
         *
         * @returns { Promise<void> } - Promise that returns no value.
         * @throws { BusinessError } 35700001 - Service error.
         * @throws { BusinessError } 35700003 - Virtual serial port disconnected.
         * @throws { BusinessError } 35700005 - Port not open.
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        drain(): Promise<void>;
        /**
         * Sets the RTS signal. This API returns the result asynchronously through a promise.
         *
         * @param { boolean } enable - RTS signal status, indicating whether to request sending data.
         * @returns { Promise<void> } - Promise that returns no value.
         * @throws { BusinessError } 35700001 - Service error.
         * @throws { BusinessError } 35700003 - Virtual serial port disconnected.
         * @throws { BusinessError } 35700005 - Port not open.
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        setRts(enable: boolean): Promise<void>;
        /**
         * Obtains the CTS signal status. This API returns the result asynchronously through a promise.
         *
         * @returns { Promise<boolean> } - Promise used to return the CTS signal status, indicating whether data can be
         *     sent.
         * @throws { BusinessError } 35700001 - Service error.
         * @throws { BusinessError } 35700003 - Virtual serial port disconnected.
         * @throws { BusinessError } 35700005 - Port not open.
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        getCts(): Promise<boolean>;
        /**
         * Sends a BRK signal. This API returns the result asynchronously through a promise.
         *
         * @returns { Promise<void> } - Promise that returns no value.
         * @throws { BusinessError } 35700001 - Service error.
         * @throws { BusinessError } 35700003 - Virtual serial port disconnected.
         * @throws { BusinessError } 35700005 - Port not open.
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        sendBrk(): Promise<void>;
        /**
         * This interface is used to listen to the disconnection event of the USB virtual serial port. Use Callback
         * asynchronous callback.
         * When the {@link close} interface is invoked, all callbacks are cleared.
         *
         * @param { Callback<void> } callback - Callback of the USB virtual serial port disconnection event.
         * @throws { BusinessError } 35700001 - Service error.
         * @throws { BusinessError } 35700005 - Port not open.
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        onDisconnect(callback: Callback<void>): void;
        /**
         * This command is used to cancel the monitoring of the USB virtual serial port disconnection event.
         *
         * @param { Callback<void> } [callback] - Callback of the USB virtual serial port disconnection event.
         *     <br>Default value: Clears all callbacks for USB virtual serial port disconnection events.
         * @throws { BusinessError } 35700001 - Service error.
         * @throws { BusinessError } 35700005 - Port not open.
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        offDisconnect(callback?: Callback<void>): void;
        /**
         * Sets the DTR signal status. Use Promise asynchronous callbacks.
         *
         * @param { boolean } enable - DTR signal status, indicating whether the local end is ready.
         * @returns { Promise<void> } - Promise that returns no value.
         * @throws { BusinessError } 35700001 - Service error.
         * @throws { BusinessError } 35700003 - Virtual serial port disconnected.
         * @throws { BusinessError } 35700005 - Port not open.
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        setDtr(enable: boolean): Promise<void>;
        /**
         * Obtains the DSR signal status. This API returns the result asynchronously through a promise.
         *
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** indicates the remote end
         *     is ready, and **false** indicates the remote end is not ready.
         * @throws { BusinessError } 35700001 - Service error.
         * @throws { BusinessError } 35700003 - Virtual serial port disconnected.
         * @throws { BusinessError } 35700005 - Port not open.
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        getDsr(): Promise<boolean>;
    }
    /**
     * Serial port device information.
     *
     * @syscap SystemCapability.BusManager.Serial
     * @stagemodelonly
     * @since 26.0.0
     */
    interface SerialPortInfo {
        /**
         * Port name.
         *
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        portName: string;
        /**
         * Vendor ID of the USB virtual serial port.
         *
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        vendorId?: number;
        /**
         * Product ID of the USB virtual serial port device.
         *
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        productId?: number;
        /**
         * Manufacturer name of the USB virtual serial port device.
         *
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        manufacturer?: string;
    }
    /**
     * Data bits in serial port communication.
     *
     * @syscap SystemCapability.BusManager.Serial
     * @stagemodelonly
     * @since 26.0.0
     */
    enum DataBits {
        /**
         * Five data bits.
         *
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        FIVE = 5,
        /**
         * Six data bits.
         *
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        SIX = 6,
        /**
         * 7 data bits.
         *
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        SEVEN = 7,
        /**
         * Eight data bits.
         *
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        EIGHT = 8
    }
    /**
     * Stop bits in serial port communication.
     *
     * @syscap SystemCapability.BusManager.Serial
     * @stagemodelonly
     * @since 26.0.0
     */
    enum StopBits {
        /**
         * One stop bit.
         *
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        ONE = 1,
        /**
         * 2 stop bits.
         *
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        TWO = 2
    }
    /**
     * Parity bits in serial port communication.
     *
     * @syscap SystemCapability.BusManager.Serial
     * @stagemodelonly
     * @since 26.0.0
     */
    enum Parity {
        /**
         * No parity bit.
         *
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        NONE = 'none',
        /**
         * Even parity.
         *
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        EVEN = 'even',
        /**
         * Odd parity.
         *
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        ODD = 'odd',
        /**
         * Mark parity. The parity bit is always 1.
         *
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        MARK = 'mark',
        /**
         * Space parity. The parity bit is always 0.
         *
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        SPACE = 'space'
    }
    /**
     * Serial port communication configuration.
     *
     * @syscap SystemCapability.BusManager.Serial
     * @stagemodelonly
     * @since 26.0.0
     */
    interface SerialConfigs {
        /**
         * Baud rate.
         * The value must be an integer.
         * Value constraint: standard baud rates.
         * <br>Unit: bit/s
         * <br>Default value: 115200
         *
         * @default 115200
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        baudRate?: number;
        /**
         * Data bits.
         * <br>Default value: EIGHT
         *
         * @default EIGHT
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        dataBits?: DataBits;
        /**
         * Stop bits.
         *
         * Default value: ONE
         *
         * @default ONE
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        stopBits?: StopBits;
        /**
         * Parity bit.
         * <br>Default value: NONE
         *
         * @default NONE
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        parity?: Parity;
        /**
         * Whether to enable hardware-based automatic flow control.
         * <br>Default value: false.
         *
         * @default false
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        rtscts?: boolean;
        /**
         * Whether to enable XON to control the sending of flows.
         * <br>Default value: false
         *
         * @default false
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        xon?: boolean;
        /**
         * Whether to enable XOFF to control the reception of flows.
         * <br>Default value: false
         *
         * @default false
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        xoff?: boolean;
        /**
         * Whether to enable XANY to control the flow.
         * <br>Default value: false
         *
         * @default false
         * @syscap SystemCapability.BusManager.Serial
         * @stagemodelonly
         * @since 26.0.0
         */
        xany?: boolean;
    }
}
export default serial;

```
