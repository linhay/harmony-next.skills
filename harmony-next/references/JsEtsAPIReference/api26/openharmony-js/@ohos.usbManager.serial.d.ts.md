# @ohos.usbManager.serial.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
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
/**
 * This module provides the serial port management functions, including enabling and disabling the serial port of the
 * device, writing and reading data, setting and obtaining the configuration parameters of the serial port, and managing
 * permissions.
 *
 * @syscap SystemCapability.USB.USBManager.Serial
 * @since 19
 */
declare namespace serialManager {
    /**
     * Obtains the serial port device list, including the device name and port number.
     *
     * @returns { Readonly<SerialPort>[]} Serial port information list.
     * @syscap SystemCapability.USB.USBManager.Serial
     * @since 19
     */
    function getPortList(): Readonly<SerialPort>[];
    /**
     * Checks whether the application has the permission to access the serial port device. When an application is
     * restarted after exits, you need to request the permission from the user again.
     *
     * @param { number} portId - Port number, which is the value of the **SerialPort** parameter obtained
     *     by [getPortList]{@link serialManager.getPortList()}.
     * @returns {boolean} The value **true** indicates that the permission is authorized, and **false** indicates the opposite.
     * @throws { BusinessError } 401 Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14400005 Database operation exception.
     * @throws { BusinessError } 31400001 Serial port management exception.
     * @throws { BusinessError } 31400003 PortId does not exist.
     * @syscap SystemCapability.USB.USBManager.Serial
     * @since 19
     */
    function hasSerialRight(portId: number): boolean;
    /**
     * Requests the permission for the application to access the serial port device. After the application exits, the
     * access permission on the serial port device is automatically removed. After the application is restarted, you need
     * to request the permission again. This API uses a promise to return the result.
     *
     * @param { number} portId - Port number, which is the value of the **SerialPort** parameter obtained
     *     by [getPortList]{@link serialManager.getPortList()}.
     * @returns { Promise<boolean>} Promise used to return the result. The value **true** indicates that the permission is
     *     successfully requested, and **false** indicates the opposite.
     * @throws { BusinessError } 401 Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14400005 Database operation exception.
     * @throws { BusinessError } 31400001 Serial port management exception.
     * @throws { BusinessError } 31400003 PortId does not exist.
     * @syscap SystemCapability.USB.USBManager.Serial
     * @since 19
     */
    function requestSerialRight(portId: number): Promise<boolean>;
    /**
     * Cancels the permission to access the serial port device when the application is running. This API is used to close
     * the enabled serial port device.
     *
     * @param { number} portId - Port number, which is the value of the **SerialPort** parameter obtained
     *     by [getPortList]{@link serialManager.getPortList()}.
     * @throws { BusinessError } 401 Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14400005 Database operation exception.
     * @throws { BusinessError } 31400001 Serial port management exception.
     * @throws { BusinessError } 31400002 Access denied. Call requestSerialRight to request user authorization first.
     * @throws { BusinessError } 31400003 PortId does not exist.
     * @syscap SystemCapability.USB.USBManager.Serial
     * @since 19
     */
    function cancelSerialRight(portId: number): void;
    /**
     * Opens a serial port device.
     *
     * @param { number} portId - Port number, which is the value of the **SerialPort** parameter obtained
     *     by [getPortList]{@link serialManager.getPortList()}.
     * @throws { BusinessError } 401 Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 31400001 Serial port management exception.
     * @throws { BusinessError } 31400002 Access denied. Call requestSerialRight to request user authorization first.
     * @throws { BusinessError } 31400003 PortId does not exist.
     * @throws { BusinessError } 31400004 The serial port device is occupied.
     * @syscap SystemCapability.USB.USBManager.Serial
     * @since 19
     */
    function open(portId: number): void;
    /**
     * Closes the serial port device.
     *
     * @param { number} portId - Port number, which is the value of the **SerialPort** parameter obtained
     *     by [getPortList]{@link serialManager.getPortList()}.
     * @throws { BusinessError } 401 Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 31400001 Serial port management exception.
     * @throws { BusinessError } 31400003 PortId does not exist.
     * @throws { BusinessError } 31400005 The serial port device is not opened. Call the open API first.
     * @syscap SystemCapability.USB.USBManager.Serial
     * @since 19
     */
    function close(portId: number): void;
    /**
     * Obtains the configuration parameters of a specified serial port.
     *
     * @param { number} portId - Port number, which is the value of the **SerialPort** parameter obtained
     *     by [getPortList]{@link serialManager.getPortList()}.
     * @returns { Readonly<SerialAttribute>} Configuration parameters of the serial port.
     * @throws { BusinessError } 401 Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 31400001 Serial port management exception.
     * @throws { BusinessError } 31400003 PortId does not exist.
     * @throws { BusinessError } 31400005 The serial port device is not opened. Call the open API first.
     * @syscap SystemCapability.USB.USBManager.Serial
     * @since 19
     */
    function getAttribute(portId: number): Readonly<SerialAttribute>;
    /**
     * Sets the parameters of the serial port. If this method is not called, the default configuration parameters are used
     *  (baud rate: 9600 bit/s; data bit: 8; parity bit: 0; stop bit: 1).
     *
     * @param { number} portId - Port number, which is the value of the **SerialPort** parameter obtained
     *     by [getPortList]{@link serialManager.getPortList()}.
     * @param { SerialAttribute} attribute - Configuration parameters of the serial port.
     * @throws { BusinessError } 401 Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 31400001 Serial port management exception.
     * @throws { BusinessError } 31400003 PortId does not exist.
     * @throws { BusinessError } 31400005 The serial port device is not opened. Call the open API first.
     * @syscap SystemCapability.USB.USBManager.Serial
     * @since 19
     */
    function setAttribute(portId: number, attribute: SerialAttribute): void;
    /**
     * Reads data from the serial port device asynchronously. This API uses a promise to return the result.
     *
     * @param { number} portId - Port number, which is the value of the **SerialPort** parameter obtained
     *     by [getPortList]{@link serialManager.getPortList()}.
     * @param { Uint8Array } buffer - Buffer for reading data, with a maximum length of 8192 bytes.
     * @param { number } timeout - Timeout interval.Unit: milliseconds. If the API has no data in the buffer of the target port, it
     *     returns the result after waiting for the specified time. The default value **0** indicates that the API returns the
     *     result without waiting.
     * @returns { Promise<number> } Promise used to return the length of the data read.
     * @throws { BusinessError } 401 Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 31400001 Serial port management exception.
     * @throws { BusinessError } 31400003 PortId does not exist.
     * @throws { BusinessError } 31400005 The serial port device is not opened. Call the open API first.
     * @throws { BusinessError } 31400006 Data transfer timed out.
     * @throws { BusinessError } 31400007 I/O exception. Possible causes:
     *
     *     <br>1. The transfer was canceled.
     *
     *     <br>2. The device offered more data than allowed.
     * @syscap SystemCapability.USB.USBManager.Serial
     * @since 19
     */
    function read(portId: number, buffer: Uint8Array, timeout?: number): Promise<number>;
    /**
     * Reads data from the serial port device synchronously.
     *
     * @param { number} portId - Port number, which is the value of the **SerialPort** parameter obtained
     *     by [getPortList]{@link serialManager.getPortList()}.
     * @param { Uint8Array } buffer - Buffer for reading data, with a maximum length of 8192 bytes.
     * @param { number } timeout - Timeout interval.Unit: milliseconds. If the API has no data in the buffer of the target port, it
     *     returns the result after waiting for the specified time. The default value **0** indicates that the API returns the
     *     result without waiting.
     * @returns {number} Length of the data read.
     * @throws { BusinessError } 401 Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 31400001 Serial port management exception.
     * @throws { BusinessError } 31400003 PortId does not exist.
     * @throws { BusinessError } 31400005 The serial port device is not opened. Call the open API first.
     * @throws { BusinessError } 31400006 Data transfer timed out.
     * @throws { BusinessError } 31400007 I/O exception. Possible causes:
     *
     *     <br>1. The transfer was canceled.
     *
     *     <br>2. The device offered more data than allowed.
     * @syscap SystemCapability.USB.USBManager.Serial
     * @since 19
     */
    function readSync(portId: number, buffer: Uint8Array, timeout?: number): number;
    /**
     * Writes data to the serial port device asynchronously. The length of data written each time cannot exceed 4 KB;
     * otherwise, data loss may occur. You are advised to write long data in multiple packets. This API uses a promise to
     * return the result.
     *
     * @param { number} portId - Port number, which is the value of the **SerialPort** parameter obtained
     *     by [getPortList]{@link serialManager.getPortList()}.
     * @param { Uint8Array } buffer - Buffer for writing data, with a maximum length of 4 KB.
     * @param { number } timeout - Timeout interval for checking whether the buffer is writable, Unit: milliseconds.
     *     If not, **0** is returned after the interval. The default value **0** is returned
     *     when data cannot be written into the target port.
     * @returns { Promise<number> } Promise used to return the length of the data written.
     * @throws { BusinessError } 401 Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 31400001 Serial port management exception.
     * @throws { BusinessError } 31400003 PortId does not exist.
     * @throws { BusinessError } 31400005 The serial port device is not opened. Call the open API first.
     * @throws { BusinessError } 31400006 Data transfer timed out.
     * @throws { BusinessError } 31400007 I/O exception. Possible causes:
     *
     *     <br>1. The transfer was canceled.
     *
     *     <br>2. The device offered more data than allowed.
     * @syscap SystemCapability.USB.USBManager.Serial
     * @since 19
     */
    function write(portId: number, buffer: Uint8Array, timeout?: number): Promise<number>;
    /**
     * Writes data to the serial port device synchronously. The length of data written each time cannot exceed 4 KB;
     * otherwise, data loss may occur. You are advised to write long data in multiple packets.
     *
     * @param { number} portId - Port number, which is the value of the **SerialPort** parameter obtained
     *     by [getPortList]{@link serialManager.getPortList()}.
     * @param { Uint8Array } buffer - Destination buffer for writing data, with a maximum length of 4 KB.
     * @param { number } timeout - Timeout interval for checking whether the buffer is writable, Unit: milliseconds.
     *     If not, **0** is returned after the interval. The default value **0** is returned
     *     when data cannot be written into the target port.
     * @returns { number } Length of the data written.
     * @throws { BusinessError } 401 Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 31400001 Serial port management exception.
     * @throws { BusinessError } 31400003 PortId does not exist.
     * @throws { BusinessError } 31400005 The serial port device is not opened. Call the open API first.
     * @throws { BusinessError } 31400006 Data transfer timed out.
     * @throws { BusinessError } 31400007 I/O exception. Possible causes:
     *
     *     <br>1. The transfer was canceled.
     *
     *     <br>2. The device offered more data than allowed.
     * @syscap SystemCapability.USB.USBManager.Serial
     * @since 19
     */
    function writeSync(portId: number, buffer: Uint8Array, timeout?: number): number;
    /**
     * Represents the parameters of a serial port.
     *
     * @syscap SystemCapability.USB.USBManager.Serial
     * @since 19
     */
    interface SerialPort {
        /**
         * Port number.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        portId: number;
        /**
         * Serial port device name.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        deviceName: string;
    }
    /**
     * Represents the configuration parameters of a serial port.
     *
     * @syscap SystemCapability.USB.USBManager.Serial
     * @since 19
     */
    interface SerialAttribute {
        /**
         * Baud rate. Unit: bit/s
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        baudRate: BaudRates;
        /**
         * Data bits. The default value is **8**. Unit: bit
         *
         * @default DATABIT_8
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        dataBits?: DataBits;
        /**
         * Parity check. The default value is **None**, indicating that no parity check is performed.
         *
         * @default NONE
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        parity?: Parity;
        /**
         * Stop bits. The default value is **1**. Unit: bit
         *
         * @default STOPBIT_1
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        stopBits?: StopBits;
    }
    /**
     * Enumerates the baud rates. Unit: bit/s
     *
     * @syscap SystemCapability.USB.USBManager.Serial
     * @since 19
     */
    enum BaudRates {
        /**
         * The baud rate is 50 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_50 = 50,
        /**
         * The baud rate is 75 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_75 = 75,
        /**
         * The baud rate is 110 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_110 = 110,
        /**
         * The baud rate is 134 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_134 = 134,
        /**
         * The baud rate is 150 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_150 = 150,
        /**
         * The baud rate is 200 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_200 = 200,
        /**
         * The baud rate is 300 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_300 = 300,
        /**
         * The baud rate is 600 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_600 = 600,
        /**
         * The baud rate is 1200 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_1200 = 1200,
        /**
         * The baud rate is 1800 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_1800 = 1800,
        /**
         * The baud rate is 2400 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_2400 = 2400,
        /**
         * The baud rate is 4800 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_4800 = 4800,
        /**
         * The baud rate is 9600 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_9600 = 9600,
        /**
         * The baud rate is 19200 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_19200 = 19200,
        /**
         * The baud rate is 38400 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_38400 = 38400,
        /**
         * The baud rate is 57600 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_57600 = 57600,
        /**
         * The baud rate is 115200 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_115200 = 115200,
        /**
         * The baud rate is 230400 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_230400 = 230400,
        /**
         * The baud rate is 460800 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_460800 = 460800,
        /**
         * The baud rate is 500000 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_500000 = 500000,
        /**
         * The baud rate is 576000 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_576000 = 576000,
        /**
         * The baud rate is 921600 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_921600 = 921600,
        /**
         * The baud rate is 1000000 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_1000000 = 1000000,
        /**
         * The baud rate is 1152000 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_1152000 = 1152000,
        /**
         * The baud rate is 1500000 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_1500000 = 1500000,
        /**
         * The baud rate is 2000000 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_2000000 = 2000000,
        /**
         * The baud rate is 2500000 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_2500000 = 2500000,
        /**
         * The baud rate is 3000000 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_3000000 = 3000000,
        /**
         * The baud rate is 3500000 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_3500000 = 3500000,
        /**
         * The baud rate is 4000000 bit/s.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        BAUDRATE_4000000 = 4000000
    }
    /**
     * Enumerates the number of data bits. Unit: bit
     *
     * @syscap SystemCapability.USB.USBManager.Serial
     * @since 19
     */
    enum DataBits {
        /**
         * The number of data bits is 8.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        DATABIT_8 = 8,
        /**
         * The number of data bits is 7.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        DATABIT_7 = 7,
        /**
         * The number of data bits is 6.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        DATABIT_6 = 6,
        /**
         * The number of data bits is 5.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        DATABIT_5 = 5
    }
    /**
     * Enumerates the parity check modes.
     *
     * @syscap SystemCapability.USB.USBManager.Serial
     * @since 19
     */
    enum Parity {
        /**
         * No parity.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        PARITY_NONE = 0,
        /**
         * Odd parity.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        PARITY_ODD = 1,
        /**
         * Even parity.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        PARITY_EVEN = 2,
        /**
         * Mark parity, whose parity bit is fixed at **1**.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        PARITY_MARK = 3,
        /**
         * Space parity, whose parity bit is fixed at **0**.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        PARITY_SPACE = 4
    }
    /**
     * Enumerates of the number of stop bits. Unit: bit
     *
     * @syscap SystemCapability.USB.USBManager.Serial
     * @since 19
     */
    enum StopBits {
        /**
         * The number of stop bits is 1.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        STOPBIT_1 = 0,
        /**
         * The number of stop bits is 2.
         *
         * @syscap SystemCapability.USB.USBManager.Serial
         * @since 19
         */
        STOPBIT_2 = 1
    }
}
export default serialManager;

```
