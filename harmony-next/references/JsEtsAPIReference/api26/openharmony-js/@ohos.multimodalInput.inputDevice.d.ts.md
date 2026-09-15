# @ohos.multimodalInput.inputDevice.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2023 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * @file Input Device
 * @kit InputKit
 */
import type { Callback, AsyncCallback } from './@ohos.base';
import type { KeyCode } from './@ohos.multimodalInput.keyCode';
/**
 * The inputDevice module implements input device management functions such as listening for the connection and
 * disconnection of input devices and querying input device information such as the device name.
 *
 * @syscap SystemCapability.MultimodalInput.Input.InputDevice
 * @since 8
 */
declare namespace inputDevice {
    /**
     * Enumerates hot swap events.
     *
     * @unionmember { 'add' } Device insertion.
     * @unionmember { 'remove' } Device removal.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 9
     */
    type ChangedType = 'add' | 'remove';
    /**
     * Input sources supported by the input device, including the keyboard, mouse, touchscreen, trackball, touchpad, and
     * joystick.
     *
     * @unionmember { 'keyboard' } The input device is a keyboard.
     * @unionmember { 'mouse' } The input device is a mouse.
     * @unionmember { 'touchpad' } The input device is a touchpad.
     * @unionmember { 'touchscreen' } The input device is a touchscreen.
     * @unionmember { 'joystick' } The input device is a joystick.
     * @unionmember { 'trackball' } The input device is a trackball.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 9
     */
    type SourceType = 'keyboard' | 'mouse' | 'touchpad' | 'touchscreen' | 'joystick' | 'trackball';
    /**
     * Defines the axis type of an input device.
     *
     * @unionmember { 'touchmajor' } Major axis of the elliptical touching area.
     * @unionmember { 'touchminor' } Minor axis of the elliptical touching area.
     * @unionmember { 'orientation' } Orientation axis.
     * @unionmember { 'x' } Horizontal axis.
     * @unionmember { 'y' } Vertical axis.
     * @unionmember { 'pressure' } Pressure axis.
     * @unionmember { 'toolminor' } Minor axis of the tool area.
     * @unionmember { 'toolmajor' } Major axis of the tool area.
     * @unionmember { 'null' } None.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 9
     */
    type AxisType = 'touchmajor' | 'touchminor' | 'orientation' | 'x' | 'y' | 'pressure' | 'toolminor' | 'toolmajor' | 'null';
    /**
     * Enumerates keyboard types.
     *
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 9
     */
    enum KeyboardType {
        /**
         * Keyboard without keys.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 9
         */
        NONE = 0,
        /**
         * Keyboard with unknown keys.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 9
         */
        UNKNOWN = 1,
        /**
         * Full keyboard.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 9
         */
        ALPHABETIC_KEYBOARD = 2,
        /**
         * Keypad.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 9
         */
        DIGITAL_KEYBOARD = 3,
        /**
         * Stylus.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 9
         */
        HANDWRITING_PEN = 4,
        /**
         * Remote control.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 9
         */
        REMOTE_CONTROL = 5
    }
    /**
     * Enumerates function key types.
     *
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 15
     */
    enum FunctionKey {
        /**
         * CapsLock key. This key can be enabled or disabled only for the input keyboard extension.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 15
         */
        CAPS_LOCK = 1
    }
    /**
     * Provides hot swap information about an input device.
     *
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 9
     */
    interface DeviceListener {
        /**
         * Device change type, which indicates whether an input device is inserted or removed.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 9
         */
        type: ChangedType;
        /**
         * Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 9
         */
        deviceId: number;
    }
    /**
     * Enables listening for device hot swap events. When performing this operation, you need to connect to external
     * devices such as a mouse, keyboard, and touchscreen. This API uses an asynchronous callback to return the result.
     *
     * @param { 'change' } type - Event type. This field has a fixed value of **change**.
     * @param { Callback<DeviceListener> } listener - Callback used to return the input device hot swap events.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 9
     */
    function on(type: 'change', listener: Callback<DeviceListener>): void;
    /**
     * Disables listening for device hot swap events. This API is called before the application exits. This API uses an
     * asynchronous callback to return the result.
     *
     * @param { 'change' } type - Event type. This field has a fixed value of **change**.
     * @param { Callback<DeviceListener> } listener - Callback to unregister. If this parameter is left unspecified,
     *     listening for hot swap events of all input devices will be canceled.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 9
     */
    function off(type: 'change', listener?: Callback<DeviceListener>): void;
    /**
     * Defines the axis range of an input device.
     *
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 8
     */
    interface AxisRange {
        /**
         * Input sources supported by the input device, including the keyboard, mouse, touchscreen, trackball, touchpad, and
         * joystick.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 8
         */
        source: SourceType;
        /**
         * Axis type of an input device.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 8
         */
        axis: AxisType;
        /**
         * Maximum value of the axis.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 8
         */
        max: number;
        /**
         * Minimum value of the axis.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 8
         */
        min: number;
        /**
         * Fuzzy value of the axis.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 9
         */
        fuzz: number;
        /**
         * Benchmark value of the axis.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 9
         */
        flat: number;
        /**
         * Resolution of the axis.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 9
         */
        resolution: number;
    }
    /**
     * Provides information about an input device.
     *
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 8
     */
    interface InputDeviceData {
        /**
         * Unique ID of the input device. If a physical device is repeatedly plugged and unplugged, its ID may change.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 8
         */
        id: number;
        /**
         * Name of the input device.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 8
         */
        name: string;
        /**
         * Input sources supported by the input device, including the keyboard, mouse, touchscreen, trackball, touchpad, and
         * joystick.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 8
         */
        sources: Array<SourceType>;
        /**
         * Axis information of the input device.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 8
         */
        axisRanges: Array<AxisRange>;
        /**
         * Bus type of the input device. By default, the bus type reported by the input device prevails.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 9
         */
        bus: number;
        /**
         * Product information of the input device.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 9
         */
        product: number;
        /**
         * Vendor information of the input device.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 9
         */
        vendor: number;
        /**
         * Version information of the input device.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 9
         */
        version: number;
        /**
         * Physical address of the input device.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 9
         */
        phys: string;
        /**
         * Unique ID of the input device.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 9
         */
        uniq: string;
        /**
         * Whether the input device is a virtual device.
         *
         * The value **true** indicates that the device is a virtual device, and the value **false** indicates that the
         * device is a non-virtual device.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 23
         */
        isVirtual?: boolean;
        /**
         * Whether the input device is a local device.
         *
         * The value **true** indicates that the device is a local device, and the value **false** indicates that the device
         * is a non-local device.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputDevice
         * @since 23
         */
        isLocal?: boolean;
    }
    /**
     * Obtains the IDs of all input devices. This API uses an asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > This API is supported since API version 8 and deprecated since API version 9. Use
     * > [inputDevice.getDeviceList]{@link inputDevice.getDeviceList} instead.
     *
     * @param { AsyncCallback<Array<number>> } callback - Callback function. If the operation is successful, **err** is
     *     **undefined**, and **data** is the ID list of all input devices. Otherwise, **err** is an error object.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.multimodalInput.inputDevice#getDeviceList
     */
    function getDeviceIds(callback: AsyncCallback<Array<number>>): void;
    /**
     * Obtains the IDs of all input devices. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > This API is supported since API version 8 and deprecated since API version 9. Use
     * > [inputDevice.getDeviceList]{@link inputDevice.getDeviceList} instead.
     *
     * @returns { Promise<Array<number>> } Promise used to return the IDs of all input devices. **id** is the unique ID of
     *     an input device.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.multimodalInput.inputDevice#getDeviceList
     */
    function getDeviceIds(): Promise<Array<number>>;
    /**
     * Obtains the information about the input device with the specified ID. This API uses an asynchronous callback to
     * return the result.
     *
     * > **NOTE**
     * >
     * > This API is supported since API version 8 and deprecated since API version 9. Use
     * > [inputDevice.getDeviceInfo]{@link inputDevice.getDeviceInfo} instead.
     *
     * @param { number } deviceId - Unique ID of the input device. If a physical device is repeatedly reinstalled or
     *     restarted, its ID may change.
     * @param { AsyncCallback<InputDeviceData> } callback - Callback function. If the retrieval is successful, **err** is
     *     **undefined**, and **data** is the input device information. Otherwise, **err** is an error object.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.multimodalInput.inputDevice#getDeviceInfo
     */
    function getDevice(deviceId: number, callback: AsyncCallback<InputDeviceData>): void;
    /**
     * Obtains the information about the input device with the specified ID. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > This API is supported since API version 8 and deprecated since API version 9. Use
     * > [inputDevice.getDeviceInfo]{@link inputDevice.getDeviceInfo} instead.
     *
     * @param { number } deviceId - Unique ID of the input device. If a physical device is repeatedly reinstalled or
     *     restarted, its ID may change.
     * @returns { Promise<InputDeviceData> } Promise used to return information about the input device, including device
     *     ID, name, supported source, physical address, version information, and product information.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.multimodalInput.inputDevice#getDeviceInfo
     */
    function getDevice(deviceId: number): Promise<InputDeviceData>;
    /**
     * Obtains the IDs of all input devices. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<Array<number>> } callback - Callback function. If the operation is successful, **err** is
     *     **undefined**, and **data** is the ID list of all input devices (the ID is the unique identifier of an input
     *     device). Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 9
     */
    function getDeviceList(callback: AsyncCallback<Array<number>>): void;
    /**
     * Obtains the IDs of all input devices. This API uses a promise to return the result.
     *
     * @returns { Promise<Array<number>> } Promise used to return the IDs of all input devices. The ID is the unique ID of an
     *     input device.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 9
     */
    function getDeviceList(): Promise<Array<number>>;
    /**
     * Obtains information about the specified input device. This API uses an asynchronous callback to return the result.
     *
     * @param { number } deviceId - Unique ID of the input device. If a physical device is repeatedly reinstalled or
     *     restarted, its ID may change.
     * @param { AsyncCallback<InputDeviceData> } callback - Callback function. If the retrieval is successful, **err** is
     *     **undefined**, and **data** is the input device information (including the device ID, name, supported input
     *     capabilities). Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 9
     */
    function getDeviceInfo(deviceId: number, callback: AsyncCallback<InputDeviceData>): void;
    /**
     * Obtains the information about the input device with the specified ID. This API uses a promise to return the result.
     *
     * @param { number } deviceId - Unique ID of the input device. If a physical device is repeatedly reinstalled or
     *     restarted, its ID may change.
     * @returns { Promise<InputDeviceData> } Promise used to return information about the input device, including device
     *     ID, name, supported source, physical address, version information, and product information.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 9
     */
    function getDeviceInfo(deviceId: number): Promise<InputDeviceData>;
    /**
     * Obtains information about the specified input device.
     *
     * @param { number } deviceId - Unique ID of the input device. If a physical device is repeatedly reinstalled or
     *     restarted, its ID may change.
     * @returns { InputDeviceData } Information about the input device, including the device ID, name, supported source,
     *     physical address, version information, and product information.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 10
     */
    function getDeviceInfoSync(deviceId: number): InputDeviceData;
    /**
     * Queries whether a specified input device supports specified keys. This API uses an asynchronous callback to return
     * the result.
     *
     * @param { number } deviceId - Unique ID of the input device. If a physical device is repeatedly reinstalled or
     *     restarted, its ID may change.
     * @param { Array<KeyCode> } keys - Keys to be queried. A maximum of five keys can be specified.
     * @param { AsyncCallback<Array<boolean>> } callback - Callback function. If the query is successful, **err** is
     *     **undefined**, and **data** is the key support query result (elements in the array correspond one-to-one to
     *     those in **keys**; **true** indicates supported, and **false** indicates not supported). Otherwise, **err** is
     *     an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 9
     */
    function supportKeys(deviceId: number, keys: Array<KeyCode>, callback: AsyncCallback<Array<boolean>>): void;
    /**
     * Checks whether the input device supports the specified keys. This API uses a promise to return the result.
     *
     * @param { number } deviceId - Unique ID of the input device. If a physical device is repeatedly reinstalled or
     *     restarted, its ID may change.
     * @param { Array<KeyCode> } keys - Keys to be queried. A maximum of five keys can be specified.
     * @returns { Promise<Array<boolean>> } Promise object, returning the query result. true indicates supported, false
     *     indicates not supported.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 9
     */
    function supportKeys(deviceId: number, keys: Array<KeyCode>): Promise<Array<boolean>>;
    /**
     * Checks whether the input device supports the specified keys.
     *
     * @param { number } deviceId - Unique ID of the input device. If a physical device is repeatedly reinstalled or
     *     restarted, its ID may change.
     * @param { Array<KeyCode> } keys - Keys to be queried. A maximum of five keys can be specified.
     * @returns { Array<boolean> } Result indicating whether the input device supports the keycode value. The value
     *     **true** indicates yes, and the value **false** indicates no.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 10
     */
    function supportKeysSync(deviceId: number, keys: Array<KeyCode>): Array<boolean>;
    /**
     * Obtains the keyboard type of the input device, such as full keyboard and numeric keypad. The keyboard type of the
     * input device is subject to the result returned by this API. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { number } deviceId - Unique ID of the input device. If a physical device is repeatedly reinstalled or
     *     restarted, its ID may change.
     * @param { AsyncCallback<KeyboardType> } callback - Callback function. If the query is successful, **err** is
     *     **undefined**, and **data** is the keyboard type of the input device. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 9
     */
    function getKeyboardType(deviceId: number, callback: AsyncCallback<KeyboardType>): void;
    /**
     * Obtains the keyboard type of an input device. This API uses a promise to return the result.
     *
     * @param { number } deviceId - Unique ID of the input device. If a physical device is repeatedly reinstalled or
     *     restarted, its ID may change.
     * @returns { Promise<KeyboardType> } Promise used to return the keyboard type of the input device.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 9
     */
    function getKeyboardType(deviceId: number): Promise<KeyboardType>;
    /**
     * Obtains the keyboard type of the input device.
     *
     * @param { number } deviceId - Unique ID of the input device. If a physical device is repeatedly reinstalled or
     *     restarted, its ID may change.
     * @returns { KeyboardType } Keyboard type.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 10
     */
    function getKeyboardTypeSync(deviceId: number): KeyboardType;
    /**
     * Obtains the interval (including the device sleep time) elapsed since the last system input event. This API uses a
     * promise to return the result.
     *
     * @returns { Promise<number> } Promise used to return the time elapsed since the last system input event, in
     *     microseconds (μs).
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 14
     */
    function getIntervalSinceLastInput(): Promise<number>;
    /**
     * Specifies whether to enable a function key (for example, **CapsLock**). This API uses a promise to return the
     * result.
     *
     * @permission ohos.permission.INPUT_KEYBOARD_CONTROLLER
     * @param { FunctionKey } functionKey - Type of the function key.
     * @param { boolean } enabled - Status of the function key. The value **true** indicates that the function key is
     *     enabled, and the value **false** indicates the opposite.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 3900002 - There is currently no keyboard device connected.
     * @throws { BusinessError } 3900003 - It is prohibited for non-input applications.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 15
     */
    function setFunctionKeyEnabled(functionKey: FunctionKey, enabled: boolean): Promise<void>;
    /**
     * Checks whether the specified function key (for example, **CapsLock**) is enabled. This API uses a promise to return
     * the result.
     *
     * @param { FunctionKey } functionKey - Type of the function key.
     * @returns { Promise<boolean> } Promise used to return the result. The value **true** indicates that the function key
     *     is enabled, and the value **false** indicates the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 3900002 - There is currently no keyboard device connected.
     * @syscap SystemCapability.MultimodalInput.Input.InputDevice
     * @since 15
     */
    function isFunctionKeyEnabled(functionKey: FunctionKey): Promise<boolean>;
}
export default inputDevice;

```
