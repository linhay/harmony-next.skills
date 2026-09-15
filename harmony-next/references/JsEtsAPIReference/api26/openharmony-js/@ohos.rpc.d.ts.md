# @ohos.rpc.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2021-2026 Huawei Device Co., Ltd.
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
 * @kit IPCKit
 */
import type { AsyncCallback } from './@ohos.base';
/**
 * The **RPC** module implements communication between processes, including inter-process communication (IPC) on a
 *     single device and remote procedure call (RPC) between processes on difference devices. IPC is implemented based
 *     on the Binder driver, and RPC is based on the DSoftBus driver.
 *
 * @syscap SystemCapability.Communication.IPC.Core
 * @atomicservice [since 26.0.0]
 * @since 7
 */
declare namespace rpc {
    /**
     * The APIs of this module return exceptions since API version 9. The following table lists the error codes.
     *
     * @syscap SystemCapability.Communication.IPC.Core
     * @since 9
     */
    enum ErrorCode {
        /**
         * Parameter check failed.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        CHECK_PARAM_ERROR = 401,
        /**
         * Failed to call mmap.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        OS_MMAP_ERROR = 1900001,
        /**
         * Failed to call **ioctl** with the shared memory file descriptor.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        OS_IOCTL_ERROR = 1900002,
        /**
         * Failed to write data to the shared memory.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        WRITE_TO_ASHMEM_ERROR = 1900003,
        /**
         * Failed to read data from the shared memory.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        READ_FROM_ASHMEM_ERROR = 1900004,
        /**
         * This operation is allowed only on the proxy object.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        ONLY_PROXY_OBJECT_PERMITTED_ERROR = 1900005,
        /**
         * This operation is allowed only on the remote object.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        ONLY_REMOTE_OBJECT_PERMITTED_ERROR = 1900006,
        /**
         * Failed to communicate with the remote object over IPC.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        COMMUNICATION_ERROR = 1900007,
        /**
         * Invalid proxy or remote object.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        PROXY_OR_REMOTE_OBJECT_INVALID_ERROR = 1900008,
        /**
         * Failed to write data to MessageSequence.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        WRITE_DATA_TO_MESSAGE_SEQUENCE_ERROR = 1900009,
        /**
         * Failed to read data from MessageSequence.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        READ_DATA_FROM_MESSAGE_SEQUENCE_ERROR = 1900010,
        /**
         * Failed to allocate memory during serialization.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        PARCEL_MEMORY_ALLOC_ERROR = 1900011,
        /**
         * Failed to invoke the JS callback.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        CALL_JS_METHOD_ERROR = 1900012,
        /**
         * Failed to call dup.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        OS_DUP_ERROR = 1900013
    }
    /**
     * Since API version 12,
     *     [writeArrayBuffer]{@link rpc.MessageSequence#writeArrayBuffer(buf: ArrayBuffer, typeCode: TypeCode)} and
     *     [readArrayBuffer]{@link rpc.MessageSequence#readArrayBuffer(typeCode: TypeCode)} are added to pass ArrayBuffer
     *     data. The specific TypedArray type is determined by the **TypeCode** defined as follows:
     *
     * @syscap SystemCapability.Communication.IPC.Core
     * @since 12
     */
    enum TypeCode {
        /**
         * The TypedArray type is **INT8_ARRAY**.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 12
         */
        INT8_ARRAY = 0,
        /**
         * The TypedArray type is **UINT8_ARRAY**.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 12
         */
        UINT8_ARRAY = 1,
        /**
         * The TypedArray type is **INT16_ARRAY**.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 12
         */
        INT16_ARRAY = 2,
        /**
         * The TypedArray type is **UINT16_ARRAY**.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 12
         */
        UINT16_ARRAY = 3,
        /**
         * The TypedArray type is **INT32_ARRAY**.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 12
         */
        INT32_ARRAY = 4,
        /**
         * The TypedArray type is **UINT32_ARRAY**.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 12
         */
        UINT32_ARRAY = 5,
        /**
         * The TypedArray type is **FLOAT32_ARRAY**.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 12
         */
        FLOAT32_ARRAY = 6,
        /**
         * The TypedArray type is **FLOAT64_ARRAY**.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 12
         */
        FLOAT64_ARRAY = 7,
        /**
         * The TypedArray type is **BIGINT64_ARRAY**.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 12
         */
        BIGINT64_ARRAY = 8,
        /**
         * The TypedArray type is **BIGUINT64_ARRAY**.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 12
         */
        BIGUINT64_ARRAY = 9
    }
    /**
     * Provides APIs for reading and writing data in specific format. During RPC, the sender can use the **write()**
     *     method provided by **MessageParcel** to write data in specific format to a **MessageParcel** object. The
     *     receiver can use the **read()** method provided by **MessageParcel** to read data in specific format from a
     *     **MessageParcel** object. The data formats include basic data types and arrays, IPC objects, interface tokens,
     *     and custom sequenceable objects.
     *
     * @syscap SystemCapability.Communication.IPC.Core
     * @since 7
     * @deprecated since 9
     * @useinstead rpc.MessageSequence
     */
    class MessageParcel {
        /**
         * Creates a **MessageParcel** object. This method is a static method.
         *
         * @returns { MessageParcel } **MessageParcel** object created.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence.create()
         */
        static create(): MessageParcel;
        /**
         * Reclaims the **MessageParcel** object that is no longer used.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#reclaim()
         */
        reclaim(): void;
        /**
         * Serializes a remote object and writes it to this **MessageParcel** object.
         *
         * @param { IRemoteObject } object - Remote object to serialize and write to the **MessageParcel** object.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeRemoteObject(obj: IRemoteObject)
         */
        writeRemoteObject(object: IRemoteObject): boolean;
        /**
         * Reads the remote object from this **MessageParcel** object. You can use this method to deserialize the
         *     **MessageParcel** object to generate an **IRemoteObject**. The remote objects are read in the order in which
         *     they are written to this **MessageParcel** object.
         *
         * @returns { IRemoteObject } Remote object obtained.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readRemoteObject()
         */
        readRemoteObject(): IRemoteObject;
        /**
         * Writes an interface token to this **MessageParcel** object. The remote object can use this interface token to
         *     verify the communication.
         *
         * @param { string } token - Interface token to write. The length of the string must be less than 40960.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeInterfaceToken(token: string)
         */
        writeInterfaceToken(token: string): boolean;
        /**
         * Reads the interface token from this **MessageParcel** object. The interface token is read in the sequence in
         *     which it is written to the **MessageParcel** object. The local object can use it to verify the communication.
         *
         * @returns { string } Interface token obtained.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readInterfaceToken()
         */
        readInterfaceToken(): string;
        /**
         * Obtains the data size of this **MessageParcel** object.
         *
         * @returns { number } Size of the **MessageParcel** object obtained, in bytes.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#getSize()
         */
        getSize(): number;
        /**
         * Obtains the capacity of this **MessageParcel** object.
         *
         * @returns { number } **MessageParcel** capacity obtained, in bytes.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#getCapacity()
         */
        getCapacity(): number;
        /**
         * Sets the size of data contained in this **MessageParcel** object.
         *
         * @param { number } size - Data size to set, in bytes.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#setSize(size: int)
         */
        setSize(size: number): boolean;
        /**
         * Sets the storage capacity of this **MessageParcel** object.
         *
         * @param { number } size - Storage capacity to set, in bytes.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#setCapacity(size: int)
         */
        setCapacity(size: number): boolean;
        /**
         * Obtains the writable capacity of this **MessageParcel** object.
         *
         * @returns { number } **MessageParcel** writable capacity obtained, in bytes.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#getWritableBytes()
         */
        getWritableBytes(): number;
        /**
         * Obtains the readable capacity of this **MessageParcel** object.
         *
         * @returns { number } **MessageParcel** object readable capacity, in bytes.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#getReadableBytes()
         */
        getReadableBytes(): number;
        /**
         * Obtains the read position of this **MessageParcel** object.
         *
         * @returns { number } Current read position of the **MessageParcel** object.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#getReadPosition()
         */
        getReadPosition(): number;
        /**
         * Obtains the write position of this **MessageParcel** object.
         *
         * @returns { number } Current write position of the **MessageParcel** object.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#getWritePosition()
         */
        getWritePosition(): number;
        /**
         * Moves the read pointer to the specified position.
         *
         * @param { number } pos - Position from which data is to read.
         * @returns { boolean } Returns **true** if the read position changes; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#rewindRead(pos: int)
         */
        rewindRead(pos: number): boolean;
        /**
         * Moves the write pointer to the specified position.
         *
         * @param { number } pos - Position from which data is to write.
         * @returns { boolean } Returns **true** if the write position changes; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#rewindWrite(pos: int)
         */
        rewindWrite(pos: number): boolean;
        /**
         * Writes information to this **MessageParcel** object indicating that no exception occurred.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeNoException()
         */
        writeNoException(): void;
        /**
         * Reads the exception information from this **MessageParcel** object.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readException()
         */
        readException(): void;
        /**
         * Writes a Byte value to this **MessageParcel** object.
         *
         * @param { number } val - Byte value to write.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeByte(val: int)
         */
        writeByte(val: number): boolean;
        /**
         * Writes a short int value to this **MessageParcel** object.
         *
         * @param { number } val - Short integer to write.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeShort(val: int)
         */
        writeShort(val: number): boolean;
        /**
         * Writes an int value to this **MessageParcel** object.
         *
         * @param { number } val - Integer to write.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeInt(val: int)
         */
        writeInt(val: number): boolean;
        /**
         * Writes a long int value to this **MessageParcel** object.
         *
         * @param { number } val - Long int value to write.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeLong(val: long)
         */
        writeLong(val: number): boolean;
        /**
         * Writes a double value to this **MessageParcel** object.
         *
         * @param { number } val - Double value to write.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeFloat(val: double)
         */
        writeFloat(val: number): boolean;
        /**
         * Writes a double value to this **MessageParcel** object.
         *
         * @param { number } val - Double value to write.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeDouble(val: double)
         */
        writeDouble(val: number): boolean;
        /**
         * Writes a Boolean value to this **MessageParcel** object.
         *
         * @param { boolean } val - Boolean value to write.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeBoolean(val: boolean)
         */
        writeBoolean(val: boolean): boolean;
        /**
         * Writes a single character value to this **MessageParcel** object.
         *
         * @param { number } val - **Char** value to write.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeChar(val: int)
         */
        writeChar(val: number): boolean;
        /**
         * Writes a string to this **MessageParcel** object.
         *
         * @param { string } val - String to write. The length of the string must be less than 40960.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeString(val: string)
         */
        writeString(val: string): boolean;
        /**
         * Writes a **Sequenceable** object to this **MessageParcel** object.
         *
         * @param { Sequenceable } val - **Sequenceable** object to write.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeParcelable(val: Parcelable)
         */
        writeSequenceable(val: Sequenceable): boolean;
        /**
         * Writes a byte array to this **MessageParcel** object.
         *
         * @param { number[] } byteArray - Byte array to write.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeByteArray(byteArray: int[])
         */
        writeByteArray(byteArray: number[]): boolean;
        /**
         * Writes a short array to this **MessageParcel** object.
         *
         * @param { number[] } shortArray - Short array to write.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeShortArray(shortArray: int[])
         */
        writeShortArray(shortArray: number[]): boolean;
        /**
         * Writes an integer array to this **MessageParcel** object.
         *
         * @param { number[] } intArray - Integer array to write.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeIntArray(intArray: int[])
         */
        writeIntArray(intArray: number[]): boolean;
        /**
         * Writes a long array to this **MessageParcel** object.
         *
         * @param { number[] } longArray - Long array to write.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeLongArray(longArray: long[])
         */
        writeLongArray(longArray: number[]): boolean;
        /**
         * Writes a double array to this **MessageParcel** object.
         *
         * @param { number[] } floatArray - Double array to write. The system processes float data as that of the double
         *     type. Therefore, the total number of bytes occupied by a float array must be calculated as the double type.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeFloatArray(floatArray: double[])
         */
        writeFloatArray(floatArray: number[]): boolean;
        /**
         * Writes a double array to this **MessageParcel** object.
         *
         * @param { number[] } doubleArray - Double array to write.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeDoubleArray(doubleArray: double[])
         */
        writeDoubleArray(doubleArray: number[]): boolean;
        /**
         * Writes a Boolean array to this **MessageParcel** object.
         *
         * @param { boolean[] } booleanArray - Boolean array to write.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeBooleanArray(booleanArray: boolean[])
         */
        writeBooleanArray(booleanArray: boolean[]): boolean;
        /**
         * Writes a single character array to this **MessageParcel** object.
         *
         * @param { number[] } charArray - Character array to write.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeCharArray(charArray: int[])
         */
        writeCharArray(charArray: number[]): boolean;
        /**
         * Writes a string array to this **MessageParcel** object.
         *
         * @param { string[] } stringArray - String array to write. The length of a single element in the array must be less
         *     than 40960.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeStringArray(stringArray: string[])
         */
        writeStringArray(stringArray: string[]): boolean;
        /**
         * Writes a **Sequenceable** array to this **MessageParcel** object.
         *
         * @param { Sequenceable[] } sequenceableArray - **Sequenceable** array to write.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeParcelableArray(parcelableArray: Parcelable[])
         */
        writeSequenceableArray(sequenceableArray: Sequenceable[]): boolean;
        /**
         * Writes an **IRemoteObject** array to this **MessageParcel** object.
         *
         * @param { IRemoteObject[] } objectArray - **IRemoteObject** array to write.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeRemoteObjectArray(objectArray: IRemoteObject[])
         */
        writeRemoteObjectArray(objectArray: IRemoteObject[]): boolean;
        /**
         * Reads the byte value from this **MessageParcel** object.
         *
         * @returns { number } Byte value read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readByte()
         */
        readByte(): number;
        /**
         * Reads the short integer from this **MessageParcel** object.
         *
         * @returns { number } Short integer read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readShort()
         */
        readShort(): number;
        /**
         * Reads the integer from this **MessageParcel** object.
         *
         * @returns { number } Integer read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readInt()
         */
        readInt(): number;
        /**
         * Reads the long int value from this **MessageParcel** object.
         *
         * @returns { number } Long integer read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readLong()
         */
        readLong(): number;
        /**
         * Reads the double value from this **MessageParcel** object.
         *
         * @returns { number } Double value read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readFloat()
         */
        readFloat(): number;
        /**
         * Reads the double value from this **MessageParcel** object.
         *
         * @returns { number } Double value read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readDouble()
         */
        readDouble(): number;
        /**
         * Reads the Boolean value from this **MessageParcel** object.
         *
         * @returns { boolean } Boolean value read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readBoolean()
         */
        readBoolean(): boolean;
        /**
         * Reads the single character value from this **MessageParcel** object.
         *
         * @returns { number } **Char** value read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readChar()
         */
        readChar(): number;
        /**
         * Reads the string from this **MessageParcel** object.
         *
         * @returns { string } String read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readString()
         */
        readString(): string;
        /**
         * Reads member variables from this **MessageParcel** object.
         *
         * @param { Sequenceable } dataIn - Object that reads member variables from the **MessageParcel** object.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readParcelable(dataIn: Parcelable)
         */
        readSequenceable(dataIn: Sequenceable): boolean;
        /**
         * Reads the byte array from this **MessageParcel** object and writes it to the created empty array.
         *
         * @param { number[] } dataIn - Byte array to read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readByteArray(dataIn: int[])
         */
        readByteArray(dataIn: number[]): void;
        /**
         * Reads the byte array from this **MessageParcel** object.
         *
         * @returns { number[] } Byte array read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readByteArray()
         */
        readByteArray(): number[];
        /**
         * Reads the short array from this **MessageParcel** object and writes it to the created empty array.
         *
         * @param { number[] } dataIn - Short array to read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readShortArray(dataIn: int[])
         */
        readShortArray(dataIn: number[]): void;
        /**
         * Reads the short array from this **MessageParcel** object.
         *
         * @returns { number[] } Short array read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readShortArray()
         */
        readShortArray(): number[];
        /**
         * Reads the integer array from this **MessageParcel** object and writes it to the created empty array.
         *
         * @param { number[] } dataIn - Integer array to read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readIntArray(dataIn: int[])
         */
        readIntArray(dataIn: number[]): void;
        /**
         * Reads the integer array from this **MessageParcel** object.
         *
         * @returns { number[] } Integer array read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readIntArray()
         */
        readIntArray(): number[];
        /**
         * Reads the long array from this **MessageParcel** object and writes it to the created empty array.
         *
         * @param { number[] } dataIn - Long array to read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readLongArray(dataIn: long[])
         */
        readLongArray(dataIn: number[]): void;
        /**
         * Reads the long array from this **MessageParcel** object.
         *
         * @returns { number[] } Long array read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readLongArray()
         */
        readLongArray(): number[];
        /**
         * Reads the double array from this **MessageParcel** object and writes it to the created empty array.
         *
         * @param { number[] } dataIn - Double array to read. The system processes float data as that of the double type.
         *     Therefore, the total number of bytes occupied by a float array must be calculated as the double type.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readFloatArray(dataIn: double[])
         */
        readFloatArray(dataIn: number[]): void;
        /**
         * Reads the double array from this **MessageParcel** object.
         *
         * @returns { number[] } Double array read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readFloatArray()
         */
        readFloatArray(): number[];
        /**
         * Reads the double array from this **MessageParcel** object and writes it to the created empty array.
         *
         * @param { number[] } dataIn - Double array to read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readDoubleArray(dataIn: double[])
         */
        readDoubleArray(dataIn: number[]): void;
        /**
         * Reads the double array from this **MessageParcel** object.
         *
         * @returns { number[] } Double array read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readDoubleArray()
         */
        readDoubleArray(): number[];
        /**
         * Reads the Boolean array from this **MessageParcel** object and writes it to the created empty array.
         *
         * @param { boolean[] } dataIn - Boolean array to read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readBooleanArray(dataIn: boolean[])
         */
        readBooleanArray(dataIn: boolean[]): void;
        /**
         * Reads the Boolean array from this **MessageParcel** object.
         *
         * @returns { boolean[] } Boolean array read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readBooleanArray()
         */
        readBooleanArray(): boolean[];
        /**
         * Reads the character array from this **MessageParcel** object and writes it to the created empty array.
         *
         * @param { number[] } dataIn - Character array to read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readCharArray(dataIn: int[])
         */
        readCharArray(dataIn: number[]): void;
        /**
         * Reads the single character array from this **MessageParcel** object.
         *
         * @returns { number[] } Character array read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readCharArray()
         */
        readCharArray(): number[];
        /**
         * Reads the string array from this **MessageParcel** object and writes it to the created empty array.
         *
         * @param { string[] } dataIn - String array to read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readStringArray(dataIn: string[])
         */
        readStringArray(dataIn: string[]): void;
        /**
         * Reads the string array from this **MessageParcel** object.
         *
         * @returns { string[] } String array read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readStringArray()
         */
        readStringArray(): string[];
        /**
         * Reads the **Sequenceable** array from this **MessageParcel** object.
         *
         * @param { Sequenceable[] } sequenceableArray - **Sequenceable** array to read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readParcelableArray(parcelableArray: Parcelable[])
         */
        readSequenceableArray(sequenceableArray: Sequenceable[]): void;
        /**
         * Reads the **IRemoteObject** array from this **MessageParcel** object and writes it to the created empty array.
         *
         * @param { IRemoteObject[] } objects - **IRemoteObject** array to read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readRemoteObjectArray(objects: IRemoteObject[])
         */
        readRemoteObjectArray(objects: IRemoteObject[]): void;
        /**
         * Reads the **IRemoteObject** array from this **MessageParcel** object.
         *
         * @returns { IRemoteObject[] } **IRemoteObject** object array obtained.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readRemoteObjectArray(objects: IRemoteObject[])
         */
        readRemoteObjectArray(): IRemoteObject[];
        /**
         * Closes a file descriptor. This API is a static method.
         *
         * @param { number } fd - File descriptor to close.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.MessageSequence.closeFileDescriptor(fd: int)
         */
        static closeFileDescriptor(fd: number): void;
        /**
         * Duplicates a file descriptor. This API is a static method.
         *
         * @param { number } fd - File descriptor to duplicate.
         * @returns { number } New file descriptor.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.MessageSequence.dupFileDescriptor(fd: int)
         */
        static dupFileDescriptor(fd: number): number;
        /**
         * Checks whether this **MessageParcel** object contains file descriptors.
         *
         * @returns { boolean } Returns **true** if the **MessageParcel** object contains file descriptors; returns
         *     **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#containFileDescriptors()
         */
        containFileDescriptors(): boolean;
        /**
         * Writes a file descriptor to this **MessageParcel** object.
         *
         * @param { number } fd - File descriptor to write.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeFileDescriptor(fd: int)
         */
        writeFileDescriptor(fd: number): boolean;
        /**
         * Reads the file descriptor from this **MessageParcel** object.
         *
         * @returns { number } File descriptor read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readFileDescriptor()
         */
        readFileDescriptor(): number;
        /**
         * Writes an anonymous shared object to this **MessageParcel** object.
         *
         * @param { Ashmem } ashmem - Anonymous shared object to write.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeAshmem(ashmem: Ashmem)
         */
        writeAshmem(ashmem: Ashmem): boolean;
        /**
         * Reads the anonymous shared object from this **MessageParcel** object.
         *
         * @returns { Ashmem } Anonymous share object obtained.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readAshmem()
         */
        readAshmem(): Ashmem;
        /**
         * Obtains the maximum amount of raw data that can be held by this **MessageParcel** object.
         *
         * @returns { number } Maximum amount of raw data that **MessageParcel** can hold, that is, 128 MB.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#getRawDataCapacity()
         */
        getRawDataCapacity(): number;
        /**
         * Writes raw data to this **MessageParcel** object.
         *
         * @param { number[] } rawData - Raw data to write. The size cannot exceed 128 MB.
         * @param { number } size - Size of the raw data, in bytes.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#writeRawDataBuffer(rawData: ArrayBuffer, size: int)
         */
        writeRawData(rawData: number[], size: number): boolean;
        /**
         * Reads raw data from this **MessageParcel** object.
         *
         * @param { number } size - Size of the raw data to read.
         * @returns { number[] } Raw data obtained, in bytes.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.MessageSequence#readRawDataBuffer(size: int)
         */
        readRawData(size: number): number[];
    }
    /**
     * Provides APIs for reading and writing data in specific format. During RPC or IPC, the sender can use the
     *     **write()** method provided by **MessageSequence** to write data in specific format to a **MessageSequence**
     *     object. The receiver can use the **read()** method provided by **MessageSequence** to read data in specific
     *     format from a **MessageSequence** object. The data formats include basic data types and arrays, IPC objects,
     *     interface tokens, and custom sequenceable objects.
     *
     * @syscap SystemCapability.Communication.IPC.Core
     * @atomicservice [since 26.0.0]
     * @since 9
     */
    class MessageSequence {
        /**
         * Creates a **MessageSequence** object. This API is a static method.
         *
         * @returns { MessageSequence } **MessageSequence** object created.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        static create(): MessageSequence;
        /**
         * Reclaims the **MessageSequence** object that is no longer used.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        reclaim(): void;
        /**
         * Serializes the remote object and writes it to the [MessageSequence]{@link rpc.MessageSequence} object.
         *
         * @param { IRemoteObject } obj - Remote object to serialize and write to the **MessageSequence** object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @throws { BusinessError } 1900008 - The proxy or remote object is invalid.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeRemoteObject(obj: IRemoteObject): void;
        /**
         * Reads the remote object from **MessageSequence**. You can use this API to deserialize the **MessageSequence**
         *     object to generate an **IRemoteObject**. The remote object is read in the order in which it is written to
         *     this **MessageSequence** object.
         *
         * @returns { IRemoteObject } Remote object obtained.
         * @throws { BusinessError } 1900008 - The proxy or remote object is invalid.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readRemoteObject(): IRemoteObject;
        /**
         * Writes an interface token to this **MessageSequence** object. The remote object can use this interface token to
         *     verify the communication.
         *
         * @param { string } token - Interface token to write. The length of the string must be less than 40960.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.The string length is greater than or equal to 40960;
         *     4.The number of bytes copied to the buffer is different from the length of the obtained string.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeInterfaceToken(token: string): void;
        /**
         * Reads the interface token from this **MessageSequence** object. The interface token is read in the sequence in
         *     which it is written to the **MessageSequence** object. The local object can use it to verify the
         *     communication.
         *
         * @returns { string } Interface token obtained.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readInterfaceToken(): string;
        /**
         * Obtains the data size of this **MessageSequence** object.
         *
         * @returns { number } Size of the **MessageSequence** instance obtained, in bytes.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        getSize(): number;
        /**
         * Obtains the capacity of this **MessageSequence** object.
         *
         * @returns { number } Capacity of the obtained **MessageSequence** object, in bytes.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        getCapacity(): number;
        /**
         * Sets the size of the data contained in this **MessageSequence** object.
         *
         * @param { number } size - Data size to set, in bytes.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        setSize(size: number): void;
        /**
         * Sets the storage capacity of this **MessageSequence** object.
         *
         * @param { number } size - Storage capacity of the **MessageSequence** object to set, in bytes.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @throws { BusinessError } 1900011 - Memory allocation failed.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        setCapacity(size: number): void;
        /**
         * Obtains the writable capacity (in bytes) of this **MessageSequence** object.
         *
         * @returns { number } Writable capacity of the **MessageSequence** instance, in bytes.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        getWritableBytes(): number;
        /**
         * Obtains the readable capacity of this **MessageSequence** object.
         *
         * @returns { number } Readable capacity of the **MessageSequence** instance, in bytes.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        getReadableBytes(): number;
        /**
         * Obtains the read position of this **MessageSequence** object.
         *
         * @returns { number } Read position obtained.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        getReadPosition(): number;
        /**
         * Obtains the write position of this **MessageSequence** object.
         *
         * @returns { number } Write position obtained.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        getWritePosition(): number;
        /**
         * Moves the read pointer to the specified position.
         *
         * @param { number } pos - Position from which data is to read.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        rewindRead(pos: number): void;
        /**
         * Moves the write pointer to the specified position.
         *
         * @param { number } pos - Position from which data is to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        rewindWrite(pos: number): void;
        /**
         * Writes information to this **MessageSequence** object indicating that no exception occurred.
         *
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeNoException(): void;
        /**
         * Reads the exception information from this **MessageSequence** object.
         *
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readException(): void;
        /**
         * Writes a byte value to this **MessageSequence** object.
         *
         * @param { number } val - Byte value to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeByte(val: number): void;
        /**
         * Writes a short integer to this **MessageSequence** object.
         *
         * @param { number } val - Short integer to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeShort(val: number): void;
        /**
         * Writes an integer to this **MessageSequence** object.
         *
         * @param { number } val - Integer to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @atomicservice [since 26.0.0]
         * @since 9
         */
        writeInt(val: number): void;
        /**
         * Writes a long integer to this **MessageSequence** object.
         *
         * @param { number } val - Long integer to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeLong(val: number): void;
        /**
         * Writes a double value to this **MessageSequence** object.
         *
         * @param { number } val - Double value to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeFloat(val: number): void;
        /**
         * Writes a double value to this **MessageSequence** object.
         *
         * @param { number } val - Double value to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeDouble(val: number): void;
        /**
         * Writes a Boolean value to this **MessageSequence** object.
         *
         * @param { boolean } val - Boolean value to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeBoolean(val: boolean): void;
        /**
         * Writes a character to this **MessageSequence** object.
         *
         * @param { number } val - **Char** value to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeChar(val: number): void;
        /**
         * Writes a string to this **MessageSequence** object.
         *
         * @param { string } val - String to write. The length of the string must be less than 40960.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.The string length is greater than or equal to 40960;
         *     4.The number of bytes copied to the buffer is different from the length of the obtained string.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @atomicservice [since 26.0.0]
         * @since 9
         */
        writeString(val: string): void;
        /**
         * Writes a **Parcelable** object to this **MessageSequence** object.
         *
         * @param { Parcelable } val - **Parcelable** object to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeParcelable(val: Parcelable): void;
        /**
         * Writes a byte array to this **MessageSequence** object.
         *
         * @param { number[] } byteArray - Byte array to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match;
         *     4.The element does not exist in the array.
         *     5.The type of the element in the array is incorrect.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeByteArray(byteArray: number[]): void;
        /**
         * Writes a short array to this **MessageSequence** object.
         *
         * @param { number[] } shortArray - Short array to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match;
         *     4.The element does not exist in the array;
         *     5.The type of the element in the array is incorrect.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeShortArray(shortArray: number[]): void;
        /**
         * Writes an integer array to this **MessageSequence** object.
         *
         * @param { number[] } intArray - Integer array to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match;
         *     4.The element does not exist in the array;
         *     5.The type of the element in the array is incorrect.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeIntArray(intArray: number[]): void;
        /**
         * Writes a long array to this **MessageSequence** object.
         *
         * @param { number[] } longArray - Long array to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match;
         *     4.The element does not exist in the array;
         *     5.The type of the element in the array is incorrect.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeLongArray(longArray: number[]): void;
        /**
         * Writes a double array to this **MessageSequence** object.
         *
         * @param { number[] } floatArray - Double array to write. The system processes float data as that of the double
         *     type. Therefore, the total number of bytes occupied by a float array must be calculated as the double type.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match;
         *     4.The element does not exist in the array;
         *     5.The type of the element in the array is incorrect.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeFloatArray(floatArray: number[]): void;
        /**
         * Writes a double array to this **MessageSequence** object.
         *
         * @param { number[] } doubleArray - Double array to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match;
         *     4.The element does not exist in the array;
         *     5.The type of the element in the array is incorrect.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeDoubleArray(doubleArray: number[]): void;
        /**
         * Writes a Boolean array to this **MessageSequence** object.
         *
         * @param { boolean[] } booleanArray - Boolean array to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match;
         *     4.The element does not exist in the array.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeBooleanArray(booleanArray: boolean[]): void;
        /**
         * Writes a character array to this **MessageSequence** object.
         *
         * @param { number[] } charArray - Character array to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match;
         *     4.The element does not exist in the array.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeCharArray(charArray: number[]): void;
        /**
         * Writes a string array to this **MessageSequence** object.
         *
         * @param { string[] } stringArray - String array to write. The length of a single element in the array must be less
         *     than 40960.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match;
         *     4.The string length is greater than or equal to 40960;
         *     5.The number of bytes copied to the buffer is different from the length of the obtained string.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeStringArray(stringArray: string[]): void;
        /**
         * Writes the **Parcelable** array to this **MessageSequence** object.
         *
         * @param { Parcelable[] } parcelableArray - **Parcelable** array to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match;
         *     4.The element does not exist in the array.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeParcelableArray(parcelableArray: Parcelable[]): void;
        /**
         * Writes an **IRemoteObject** array to this **MessageSequence** object.
         *
         * @param { IRemoteObject[] } objectArray - **IRemoteObject** array to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match;
         *     4.The element does not exist in the array;
         *     5.The obtained remoteObject is null.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeRemoteObjectArray(objectArray: IRemoteObject[]): void;
        /**
         * Reads the byte value from this **MessageSequence** object.
         *
         * @returns { number } Byte value read.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readByte(): number;
        /**
         * Reads the short integer from this **MessageSequence** object.
         *
         * @returns { number } Short integer read.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readShort(): number;
        /**
         * Reads the integer from this **MessageSequence** object.
         *
         * @returns { number } Integer read.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @atomicservice [since 26.0.0]
         * @since 9
         */
        readInt(): number;
        /**
         * Reads the long integer from this **MessageSequence** object.
         *
         * @returns { number } Long integer read.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readLong(): number;
        /**
         * Reads the double value from this **MessageSequence** object.
         *
         * @returns { number } Double value read.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readFloat(): number;
        /**
         * Reads the double value from this **MessageSequence** object.
         *
         * @returns { number } Double value read.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readDouble(): number;
        /**
         * Reads the Boolean value from this **MessageSequence** object.
         *
         * @returns { boolean } Boolean value read.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readBoolean(): boolean;
        /**
         * Reads the character from this **MessageSequence** object.
         *
         * @returns { number } **Char** value read.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readChar(): number;
        /**
         * Reads the string from this **MessageSequence** object.
         *
         * @returns { string } String read.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @atomicservice [since 26.0.0]
         * @since 9
         */
        readString(): string;
        /**
         * Reads the **Parcelable** object from this **MessageSequence** object to the specified object (**dataIn**).
         *
         * @param { Parcelable } dataIn - **Parcelable** object to read.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @throws { BusinessError } 1900012 - Failed to call the JS callback function.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readParcelable(dataIn: Parcelable): void;
        /**
         * Reads the byte array from this **MessageSequence** object and writes it to the created empty array.
         *
         * @param { number[] } dataIn - Byte array to read.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readByteArray(dataIn: number[]): void;
        /**
         * Reads the byte array from this **MessageSequence** object.
         *
         * @returns { number[] } Byte array read.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readByteArray(): number[];
        /**
         * Reads the short array from this **MessageSequence** object and writes it to the created empty array.
         *
         * @param { number[] } dataIn - Short array to read.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readShortArray(dataIn: number[]): void;
        /**
         * Reads the short array from this **MessageSequence** object.
         *
         * @returns { number[] } Short array read.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readShortArray(): number[];
        /**
         * Reads the integer array from this **MessageSequence** object and writes it to the created empty array.
         *
         * @param { number[] } dataIn - Integer array to read.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readIntArray(dataIn: number[]): void;
        /**
         * Reads the integer array from this **MessageSequence** object.
         *
         * @returns { number[] } Integer array read.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readIntArray(): number[];
        /**
         * Reads the long array from this **MessageSequence** object and writes it to the created empty array.
         *
         * @param { number[] } dataIn - Long array to read.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readLongArray(dataIn: number[]): void;
        /**
         * Reads the long integer array from this **MessageSequence** object.
         *
         * @returns { number[] } Long array read.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readLongArray(): number[];
        /**
         * Reads the double array from this **MessageSequence** object and writes it to the created empty array.
         *
         * @param { number[] } dataIn - Double array to read. The system processes float data as that of the double type.
         *     Therefore, the total number of bytes occupied by a float array must be calculated as the double type.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readFloatArray(dataIn: number[]): void;
        /**
         * Reads the double array from this **MessageSequence** object.
         *
         * @returns { number[] } Double array read.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readFloatArray(): number[];
        /**
         * Reads the double array from this **MessageSequence** object and writes it to the created empty array.
         *
         * @param { number[] } dataIn - Double array to read.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readDoubleArray(dataIn: number[]): void;
        /**
         * Reads the double array from this **MessageSequence** object.
         *
         * @returns { number[] } Double array read.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readDoubleArray(): number[];
        /**
         * Reads the Boolean array from this **MessageSequence** object and writes it to the created empty array.
         *
         * @param { boolean[] } dataIn - Boolean array to read.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readBooleanArray(dataIn: boolean[]): void;
        /**
         * Reads the Boolean array from this **MessageSequence** object.
         *
         * @returns { boolean[] } Boolean array read.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readBooleanArray(): boolean[];
        /**
         * Reads the character array from this **MessageSequence** object and writes it to the created empty array.
         *
         * @param { number[] } dataIn - Character array to read.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readCharArray(dataIn: number[]): void;
        /**
         * Reads the character array from this **MessageSequence** object.
         *
         * @returns { number[] } Character array read.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readCharArray(): number[];
        /**
         * Reads the string array from this **MessageSequence** object and writes it to the created empty array.
         *
         * @param { string[] } dataIn - String array to read.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readStringArray(dataIn: string[]): void;
        /**
         * Reads the string array from this **MessageSequence** object.
         *
         * @returns { string[] } String array read.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readStringArray(): string[];
        /**
         * Reads the **Parcelable** array from this **MessageSequence** object.
         *
         * @param { Parcelable[] } parcelableArray - **Parcelable** array to read.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match;
         *     4.The length of the array passed when reading is not equal to the length passed when writing to the array;
         *     5.The element does not exist in the array.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @throws { BusinessError } 1900012 - Failed to call the JS callback function.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readParcelableArray(parcelableArray: Parcelable[]): void;
        /**
         * Reads the **IRemoteObject** array from this **MessageSequence** object and writes it to the created empty array.
         *
         * @param { IRemoteObject[] } objects - **IRemoteObject** array to read.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match;
         *     4.The length of the array passed when reading is not equal to the length passed when writing to the array.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readRemoteObjectArray(objects: IRemoteObject[]): void;
        /**
         * Reads the **IRemoteObject** array from this **MessageSequence** object.
         *
         * @returns { IRemoteObject[] } The **IRemoteObject** array is returned. If an empty array is written, **null** is
         *     returned.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readRemoteObjectArray(): IRemoteObject[];
        /**
         * Closes a file descriptor. This API is a static method.
         *
         * @param { number } fd - File descriptor to close.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        static closeFileDescriptor(fd: number): void;
        /**
         * Duplicates a file descriptor. This API is a static method.
         *
         * @param { number } fd - File descriptor to duplicate.
         * @returns { number } New file descriptor.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @throws { BusinessError } 1900013 - Failed to call dup.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        static dupFileDescriptor(fd: number): number;
        /**
         * Checks whether this **MessageSequence** object contains file descriptors.
         *
         * @returns { boolean } Returns **true** if the **MessageSequence** object contains file descriptors; returns
         *     **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        containFileDescriptors(): boolean;
        /**
         * Writes a file descriptor to this **MessageSequence** object.
         *
         * @param { number } fd - File descriptor to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeFileDescriptor(fd: number): void;
        /**
         * Reads the file descriptor from this **MessageSequence** object.
         *
         * @returns { number } File descriptor read.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readFileDescriptor(): number;
        /**
         * Writes an anonymous shared object to this **MessageSequence** object.
         *
         * @param { Ashmem } ashmem - Anonymous shared object to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter is not an instance of the Ashmem object.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        writeAshmem(ashmem: Ashmem): void;
        /**
         * Reads the anonymous shared object from this **MessageSequence** object.
         *
         * @returns { Ashmem } Anonymous share object obtained.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        readAshmem(): Ashmem;
        /**
         * Obtains the maximum amount of raw data that can be held by this **MessageSequence** object.
         *
         * @returns { number } Maximum amount of raw data that **MessageSequence** can hold, that is, 128 MB.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        getRawDataCapacity(): number;
        /**
         * Writes raw data to this **MessageSequence** object.
         *
         * > **NOTE**
         * >
         * > - This API cannot be called for multiple times in one parcel communication.
         * >
         * > - When the data volume is large (greater than 32 KB), the shared memory is used to transmit data. In this case,
         * >  pay attention to the SELinux configuration.
         *
         * @param { number[] } rawData - Raw data to write. The size cannot exceed 128 MB.
         * @param { number } size - Size of the raw data, in bytes.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match;
         *     4.The transferred size cannot be obtained;
         *     5.The transferred size is less than or equal to 0;
         *     6.The element does not exist in the array;
         *     7.Failed to obtain typedArray information;
         *     8.The array is not of type int32;
         *     9.The length of typedarray is smaller than the size of the original data sent.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         * @deprecated since 11
         * @useinstead writeRawDataBuffer(rawData: ArrayBuffer, size: int)
         */
        writeRawData(rawData: number[], size: number): void;
        /**
         * Writes raw data to this **MessageSequence** object.
         *
         * > **NOTE**
         * >
         * > - This API cannot be called for multiple times in one parcel communication.
         * >
         * > - When the data volume is large (greater than 32 KB), the shared memory is used to transmit data. In this case,
         * >  pay attention to the SELinux configuration.
         *
         * @param { ArrayBuffer } rawData - Raw data to write. The size cannot exceed 128 MB.
         * @param { number } size - Size of the raw data, in bytes.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.Failed to obtain arrayBuffer information;
         *     4.The transferred size cannot be obtained;
         *     5.The transferred size is less than or equal to 0;
         *     6.The transferred size is greater than the byte length of ArrayBuffer.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 11
         */
        writeRawDataBuffer(rawData: ArrayBuffer, size: number): void;
        /**
         * Reads raw data from this **MessageSequence** object.
         *
         * @param { number } size - Size of the raw data to read.
         * @returns { number[] } Raw data obtained, in bytes.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         * @deprecated since 11
         * @useinstead readRawDataBuffer(size: int)
         */
        readRawData(size: number): number[];
        /**
         * Reads raw data from this **MessageSequence** object.
         *
         * @param { number } size - Size of the raw data to read.
         * @returns { ArrayBuffer } Raw data obtained, in bytes.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 11
         */
        readRawDataBuffer(size: number): ArrayBuffer;
        /**
         * Writes data of the ArrayBuffer type to this **MessageSequence** object.
         *
         * @param { ArrayBuffer } buf - Data to write.
         * @param { TypeCode } typeCode - TypedArray type of the ArrayBuffer data.<br>The underlying write mode is
         *     determined based on the enum value of **TypeCode** passed by the service.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The parameter is an empty array;
         *     2.The number of parameters is incorrect;
         *     3.The parameter type does not match;
         *     4.The obtained value of typeCode is incorrect;
         *     5.Failed to obtain arrayBuffer information.
         * @throws { BusinessError } 1900009 - Failed to write data to the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 12
         */
        writeArrayBuffer(buf: ArrayBuffer, typeCode: TypeCode): void;
        /**
         * Reads data of the ArrayBuffer type from this **MessageSequence**.
         *
         * @param { TypeCode } typeCode - TypedArray type of the ArrayBuffer data.<br>The underlying read mode is determined
         *     based on the enum value of **TypeCode** passed by the service.
         * @returns { ArrayBuffer } Data of the ArrayBuffer type read, in bytes.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.The obtained value of typeCode is incorrect;
         * @throws { BusinessError } 1900010 - Failed to read data from the message sequence.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 12
         */
        readArrayBuffer(typeCode: TypeCode): ArrayBuffer;
    }
    /**
     * Writes objects of classes to a **MessageParcel** and reads them from the **MessageParcel** during IPC.
     *
     * @syscap SystemCapability.Communication.IPC.Core
     * @since 7
     * @deprecated since 9
     * @useinstead rpc.Parcelable
     */
    interface Sequenceable {
        /**
         * Marshals the sequenceable object into a **MessageParcel** object.
         *
         * @param { MessageParcel } dataOut - **MessageParcel** object to which the sequenceable object is to be marshaled.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.Parcelable#marshalling(dataOut: MessageSequence)
         */
        marshalling(dataOut: MessageParcel): boolean;
        /**
         * Unmarshals this sequenceable object from a **MessageParcel** object.
         *
         * @param { MessageParcel } dataIn - **MessageParcel** object in which the sequenceable object is to be unmarshaled.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.Parcelable#unmarshalling(dataIn: MessageSequence)
         */
        unmarshalling(dataIn: MessageParcel): boolean;
    }
    /**
     * Writes an object to a **MessageSequence** and reads it from the **MessageSequence** during IPC.
     *
     * @syscap SystemCapability.Communication.IPC.Core
     * @since 9
     */
    interface Parcelable {
        /**
         * Marshals this **Parcelable** object into a **MessageSequence** object.
         *
         * @param { MessageSequence } dataOut - **MessageSequence** object to which the **Parcelable** object is to be
         *     marshaled.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        marshalling(dataOut: MessageSequence): boolean;
        /**
         * Unmarshals this **Parcelable** object from a **MessageSequence** object.
         *
         * @param { MessageSequence } dataIn - **MessageSequence** object from which the **Parcelable** object is to be
         *     unmarshaled.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        unmarshalling(dataIn: MessageSequence): boolean;
    }
    /**
     * Defines the response to the request.
     *
     * @syscap SystemCapability.Communication.IPC.Core
     * @since 8
     * @deprecated since 9
     * @useinstead rpc.RequestResult
     */
    interface SendRequestResult {
        /**
         * Error code.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.RequestResult#errCode
         */
        errCode: number;
        /**
         * Message code.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.RequestResult#code
         */
        code: number;
        /**
         * **MessageParcel** object sent to the remote process.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.RequestResult#data
         */
        data: MessageParcel;
        /**
         * **MessageParcel** object returned by the remote process.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.RequestResult#reply
         */
        reply: MessageParcel;
    }
    /**
     * Defines the response to the request.
     *
     * @syscap SystemCapability.Communication.IPC.Core
     * @since 9
     */
    interface RequestResult {
        /**
         * Error code.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        errCode: number;
        /**
         * Message code.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        code: number;
        /**
         * **MessageSequence** object sent to the remote process.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        data: MessageSequence;
        /**
         * **MessageSequence** object returned by the remote process.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        reply: MessageSequence;
    }
    /**
     * Provides methods to query of obtain interface descriptors, add or delete death notifications, dump object status to
     *     specific files, and send messages.
     *
     * @syscap SystemCapability.Communication.IPC.Core
     * @since 7
     */
    abstract class IRemoteObject {
        /**
         * Obtains the string of the interface descriptor.
         *
         * @param { string } descriptor - Interface descriptor.
         * @returns { IRemoteBroker } **IRemoteBroker** object bound to the specified interface token.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead getLocalInterface(descriptor: string)
         */
        queryLocalInterface(descriptor: string): IRemoteBroker;
        /**
         * Obtains the string of the interface descriptor.
         *
         * @param { string } descriptor - Interface descriptor.
         * @returns { IRemoteBroker } **IRemoteBroker** object bound to the specified interface token.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.The string length is greater than or equal to 40960;
         *     4.The number of bytes copied to the buffer is different from the length of the obtained string.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        getLocalInterface(descriptor: string): IRemoteBroker;
        /**
         * Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode
         *     is set in **options**, a promise will be fulfilled immediately and the reply message does not contain any
         *     content. If synchronous mode is set in **options**, a promise will be fulfilled when the response to
         *     **sendRequest** is returned, and the reply message contains the returned information.
         *
         * @param { number } code - Message code [1-16777215] called by the request, which is determined by the
         *     communication parties. If the method is generated by an IDL tool, the message code is automatically generated
         *     by the IDL tool.
         * @param { MessageParcel } data - **MessageParcel** object holding the data to send.
         * @param { MessageParcel } reply - **MessageParcel** object that receives the response.
         * @param { MessageOption } options - Request sending mode, which can be synchronous (default) or asynchronous.
         * @returns { boolean } Returns **true** if the message is sent successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead sendMessageRequest(code: int, data: MessageSequence, reply: MessageSequence, options: MessageOption)
         */
        sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean;
        /**
         * Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode
         *     is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The specific
         *     reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**,
         *     a promise will be fulfilled when the response to **sendRequest** is returned, and the reply message contains
         *     the returned information.
         *
         * @param { number } code - Message code [1-16777215] called by the request, which is determined by the
         *     communication parties. If the method is generated by an IDL tool, the message code is automatically generated
         *     by the IDL tool.
         * @param { MessageParcel } data - **MessageParcel** object holding the data to send.
         * @param { MessageParcel } reply - **MessageParcel** object that receives the response.
         * @param { MessageOption } options - Request sending mode, which can be synchronous (default) or asynchronous.
         * @returns { Promise<SendRequestResult> } Promise used to return a **sendRequestResult** instance.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead sendMessageRequest(code: int, data: MessageSequence, reply: MessageSequence, options: MessageOption)
         */
        sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): Promise<SendRequestResult>;
        /**
         * Sends a **MessageSequence** message to the remote process in synchronous or asynchronous mode. If asynchronous
         *     mode is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The
         *     specific reply needs to be obtained from the callback on the service side. If synchronous mode is set
         *     in **options**, a promise will be fulfilled when the response to **sendMessageRequest** is returned, and the
         *     reply message contains the returned information.
         *
         * @param { number } code - Message code [1-16777215] called by the request, which is determined by the communication
         *     parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL
         *     tool.
         * @param {MessageSequence } data - **MessageSequence** object holding the data to send.
         * @param {MessageSequence } reply - **MessageSequence** object that receives the response.
         * @param { MessageOption } options - Request sending mode, which can be synchronous (default) or asynchronous.
         * @returns { Promise<RequestResult> } Promise used to return a **requestResult** instance.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.Failed to obtain the passed object instance.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption): Promise<RequestResult>;
        /**
         * Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode
         *     is set in **options**, a callback will be called immediately, and the reply message is empty. The specific
         *     reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**,
         *     a callback will be invoked when the response to **sendRequest** is returned, and the reply message contains
         *     the returned information.
         *
         * @param { number } code - Message code [1-16777215] called by the request, which is determined by the
         *     communication parties. If the method is generated by an IDL tool, the message code is automatically generated
         *     by the IDL tool.
         * @param { MessageParcel } data - **MessageParcel** object holding the data to send.
         * @param { MessageParcel } reply - **MessageParcel** object that receives the response.
         * @param { MessageOption } options - Request sending mode, which can be synchronous (default) or asynchronous.
         * @param { AsyncCallback<SendRequestResult> } callback - Callback for receiving the sending result.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead sendMessageRequest(code: int, data: MessageSequence, reply: MessageSequence,
         *     options: MessageOption, callback: AsyncCallback<RequestResult>)
         */
        sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption, callback: AsyncCallback<SendRequestResult>): void;
        /**
         * Sends a **MessageSequence** message to the remote process in synchronous or asynchronous mode. If asynchronous
         *     mode is set in **options**, a callback will be called immediately, and the reply message is empty. The
         *     specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in
         *     **options**, a callback will be invoked when the response to **sendRequest** is returned, and the reply
         *     message contains the returned information.
         *
         * @param {number } code - Message code [1-16777215] called by the request, which is determined by the communication
         *     parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL
         *     tool.
         * @param { MessageSequence } data - **MessageSequence** object holding the data to send.
         * @param { MessageSequence } reply - **MessageSequence** object that receives the response.
         * @param { MessageOption } options - Request sending mode, which can be synchronous (default) or asynchronous.
         * @param { AsyncCallback<RequestResult> } callback - Callback for receiving the sending result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.Failed to obtain the passed object instance.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption, callback: AsyncCallback<RequestResult>): void;
        /**
         * Adds a callback for receiving death notifications of the remote object.
         *
         * @param { DeathRecipient } recipient - Callback to register.
         * @param { number } flags - Flag of the death notification.
         * @returns { boolean } Returns **true** if the callback is added successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead registerDeathRecipient(recipient: DeathRecipient, flags: int)
         */
        addDeathRecipient(recipient: DeathRecipient, flags: number): boolean;
        /**
         * Registers a callback for receiving death notifications of the remote object.
         *
         * @param { DeathRecipient } recipient - Callback to register.
         * @param { number } flags - Flag of the death notification.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.The callback used to receive remote object death notifications is empty.
         * @throws { BusinessError } 1900005 - Operation allowed only for the proxy object.
         * @throws { BusinessError } 1900008 - The proxy or remote object is invalid.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        registerDeathRecipient(recipient: DeathRecipient, flags: number): void;
        /**
         * Removes the callback used to receive death notifications of the remote object.
         *
         * @param { DeathRecipient } recipient - Callback to unregister.
         * @param { number } flags - Flag of the death notification.
         * @returns { boolean } Returns **true** if the callback is removed; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead unregisterDeathRecipient(recipient: DeathRecipient, flags: int)
         */
        removeDeathRecipient(recipient: DeathRecipient, flags: number): boolean;
        /**
         * Unregisters from the callback used to receive death notifications of the remote object.
         *
         * @param { DeathRecipient } recipient - Callback to unregister.
         * @param { number } flags - Flag of the death notification.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.The callback used to receive remote object death notifications is empty.
         * @throws { BusinessError } 1900005 - Operation allowed only for the proxy object.
         * @throws { BusinessError } 1900008 - The proxy or remote object is invalid.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        unregisterDeathRecipient(recipient: DeathRecipient, flags: number): void;
        /**
         * Obtains the interface descriptor (which is a string) of this object.
         *
         * @returns { string } Interface descriptor obtained.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead getDescriptor()
         */
        getInterfaceDescriptor(): string;
        /**
         * Obtains the interface descriptor (which is a string) of this object.
         *
         * @returns { string } Interface descriptor obtained.
         * @throws { BusinessError } 1900008 - The proxy or remote object is invalid.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        getDescriptor(): string;
        /**
         * Checks whether this object is dead.
         *
         * @returns { boolean } Returns **true** if the object is dead; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         */
        isObjectDead(): boolean;
    }
    /**
     * Represents the holder of a remote proxy object. It is used to obtain a proxy object.
     *
     * @syscap SystemCapability.Communication.IPC.Core
     * @since 7
     */
    interface IRemoteBroker {
        /**
         * Obtains a proxy or remote object. This API must be implemented by its derived classes.
         *
         * @returns { IRemoteObject } Returns the **RemoteObject** if it is the caller; returns the
         *     [IRemoteObject]{@link rpc.IRemoteObject}, the holder of this **RemoteProxy** object, if the caller is a
         *     [RemoteProxy]{@link rpc.RemoteProxy} object.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         */
        asObject(): IRemoteObject;
    }
    /**
     * Subscribes to death notifications of a remote object. When the remote object is dead, the local end will receive a
     *     notification and **[onRemoteDied]{@link rpc.DeathRecipient.onRemoteDied()}** will be called. A remote object is
     *     dead when the process holding the object is terminated or the device of the remote object is shut down or
     *     restarted. If the local and remote objects belong to different devices, the remote object is dead when the
     *     device holding the remote object is detached from the network.
     *
     * @syscap SystemCapability.Communication.IPC.Core
     * @since 7
     */
    interface DeathRecipient {
        /**
         * Called to perform subsequent operations when a death notification of the remote object is received.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         */
        onRemoteDied(): void;
    }
    /**
     * Defines the options used to construct the **MessageOption** object.
     *
     * @syscap SystemCapability.Communication.IPC.Core
     * @atomicservice [since 26.0.0]
     * @since 7
     */
    class MessageOption {
        /**
         * Synchronous call.
         *
         * @default 0
         * @syscap SystemCapability.Communication.IPC.Core
         * @atomicservice [since 26.0.0]
         * @since 7
         */
        static readonly TF_SYNC: number;
        /**
         * Asynchronous call.
         *
         * @default 1
         * @syscap SystemCapability.Communication.IPC.Core
         * @atomicservice [since 26.0.0]
         * @since 7
         */
        static readonly TF_ASYNC: number;
        /**
         * Indication to **sendMessageRequest** for passing the file descriptor.
         *
         * @default 16
         * @syscap SystemCapability.Communication.IPC.Core
         * @atomicservice [since 26.0.0]
         * @since 7
         */
        static readonly TF_ACCEPT_FDS: number;
        /**
         * RPC wait time, in seconds. This parameter cannot be used in IPC. The default waiting time is 8 seconds. You are
         *     advised not to change the waiting time.
         *
         * @default 4 [since 7 - 10]
         * @default 8 [since 11]
         * @syscap SystemCapability.Communication.IPC.Core
         * @atomicservice [since 26.0.0]
         * @since 7
         */
        static readonly TF_WAIT_TIME: number;
        /**
         * A constructor used to create a **MessageOption** object.
         *
         * @param { number } syncFlags - Call flag to set. The options are as follows: 0 (synchronous call) and 1
         *     (asynchronous call). The default value is **synchronous**.
         * @param { number } waitTime - Maximum wait time for an RPC call, in seconds. The default value is
         *     **TF_WAIT_TIME**.
         * @syscap SystemCapability.Communication.IPC.Core
         * @atomicservice [since 26.0.0]
         * @since 7
         */
        constructor(syncFlags?: number, waitTime?: number);
        /**
         * A constructor used to create a **MessageOption** object.
         *
         * @param { boolean } async - Whether to execute the call asynchronously. The value **true** means to execute the
         *     call asynchronously; the value **false** means to execute the call synchronously. The default value is
         *     **synchronous**.
         * @syscap SystemCapability.Communication.IPC.Core
         * @atomicservice [since 26.0.0]
         * @since 9
         */
        constructor(async?: boolean);
        /**
         * Obtains the call flag, which can be synchronous or asynchronous.
         *
         * @returns { number } Call flag obtained. **0**: synchronous call flag; **1**: asynchronous call flag.
         * @syscap SystemCapability.Communication.IPC.Core
         * @atomicservice [since 26.0.0]
         * @since 7
         */
        getFlags(): number;
        /**
         * Sets the call flag, which can be synchronous or asynchronous.
         *
         * @param { number } flags - Call flag to set. **0**: synchronous call flag; **1**: asynchronous call flag.
         * @syscap SystemCapability.Communication.IPC.Core
         * @atomicservice [since 26.0.0]
         * @since 7
         */
        setFlags(flags: number): void;
        /**
         * Checks whether **SendMessageRequest** is called synchronously or asynchronously.
         *
         * @returns { boolean } Returns **true** if **SendMessageRequest** is called asynchronously; returns **false** if it
         *     is called synchronously.
         * @syscap SystemCapability.Communication.IPC.Core
         * @atomicservice [since 26.0.0]
         * @since 9
         */
        isAsync(): boolean;
        /**
         * Sets whether **SendMessageRequest** is called synchronously or asynchronously.
         *
         * @param { boolean } isAsync - Whether to execute the call asynchronously. The value **true** means to execute the
         *     call asynchronously; the value **false** means to execute the call synchronously.
         * @syscap SystemCapability.Communication.IPC.Core
         * @atomicservice [since 26.0.0]
         * @since 9
         */
        setAsync(isAsync: boolean): void;
        /**
         * Obtains the maximum wait time for this RPC call.
         *
         * @returns { number } Return the maximum waiting time obtained by the RPC, in seconds. The default value is
         *     **TF_WAIT_TIME**.
         * @syscap SystemCapability.Communication.IPC.Core
         * @atomicservice [since 26.0.0]
         * @since 7
         */
        getWaitTime(): number;
        /**
         * Sets the maximum wait time for this RPC call.
         *
         * @param { number } waitTime - Indicates the maximum waiting time for RPC, in seconds. The upper limit is 3000
         *     seconds.
         * @syscap SystemCapability.Communication.IPC.Core
         * @atomicservice [since 26.0.0]
         * @since 7
         */
        setWaitTime(waitTime: number): void;
    }
    /**
     * Defines the IPC context, including the PID and UID, local and remote device IDs, and whether the API is invoked on
     *     the same device.
     *
     * @syscap SystemCapability.Communication.IPC.Core
     * @since 23
     */
    class CallingInfo {
        /**
         * PID of the caller.
         * callerPid is valid only when the {@link isLocalCalling} is true. Otherwise callerPid is invalid
         * @default -1
         * @syscap SystemCapability.Communication.IPC.Core
         * @FaAndStageModel
         * @since 23
         */
        readonly callerPid: number;
        /**
         * UID of the caller.
         * callerUid is valid only when the {@link isLocalCalling} is true. Otherwise callerUid is invalid.
         *
         * @default -1
         * @syscap SystemCapability.Communication.IPC.Core
         * @FaAndStageModel
         * @since 23
         */
        readonly callerUid: number;
        /**
         * Token ID of the caller.
         * callerTokenId is valid only when the {@link isLocalCalling} is true. Otherwise callerTokenId is invalid.
         *
         * @default -1
         * @syscap SystemCapability.Communication.IPC.Core
         * @FaAndStageModel
         * @since 23
         */
        readonly callerTokenId: number;
        /**
         * Remote device ID. This parameter is valid only in RPC scenarios.
         * remoteDeviceId is valid only when the {@link isLocalCalling} is false. Otherwise remoteDeviceId is invalid.
         *
         * @default
         * @syscap SystemCapability.Communication.IPC.Core
         * @FaAndStageModel
         * @since 23
         */
        readonly remoteDeviceId: string;
        /**
         * Local device ID. This parameter is valid only in RPC scenarios.
         * localDeviceId is valid only when the {@link isLocalCalling} is false. Otherwise localDeviceId is invalid.
         *
         * @default
         * @syscap SystemCapability.Communication.IPC.Core
         * @FaAndStageModel
         * @since 23
         */
        readonly localDeviceId: string;
        /**
         * Whether the peer end of the current communication is a process on the local device. Returns **true** if the local
         *     and peer processes are on the same device; returns **false** otherwise.
         *
         * @default true
         * @syscap SystemCapability.Communication.IPC.Core
         * @FaAndStageModel
         * @since 23
         */
        readonly isLocalCalling: boolean;
    }
    /**
     * Provides methods to implement **RemoteObject**. The service provider must inherit from this class.
     *
     * @syscap SystemCapability.Communication.IPC.Core
     * @atomicservice [since 26.0.0]
     * @since 7
     */
    class RemoteObject extends IRemoteObject {
        /**
         * A constructor used to create a **RemoteObject** object.
         *
         * @param { string } descriptor - Interface descriptor. The length of the string must be less than 40960.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         */
        constructor(descriptor: string);
        /**
         * Checks whether the remote object corresponding to the specified interface token exists.
         *
         * @param { string } descriptor - Interface descriptor.
         * @returns { IRemoteBroker } Returns the remote object if a match is found; returns **Null** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.IRemoteObject#getLocalInterface(descriptor: string)
         */
        queryLocalInterface(descriptor: string): IRemoteBroker;
        /**
         * Obtains the string of the interface descriptor.
         *
         * @param { string } descriptor - String of the interface descriptor. The length of the string must be less than
         *     40960.
         * @returns { IRemoteBroker } **IRemoteBroker** object bound to the specified interface token.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.The string length is greater than or equal to 40960;
         *     4.The number of bytes copied to the buffer is different from the length of the obtained string.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        getLocalInterface(descriptor: string): IRemoteBroker;
        /**
         * Obtains the interface descriptor.
         *
         * @returns { string } Interface descriptor obtained.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.IRemoteObject#getDescriptor()
         */
        getInterfaceDescriptor(): string;
        /**
         * Obtains the interface descriptor of this object. The interface descriptor is a string.
         *
         * @returns { string } Interface descriptor obtained.
         * @throws { BusinessError } 1900008 - The proxy or remote object is invalid.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        getDescriptor(): string;
        /**
         * Called to return a response to **sendMessageRequest()**. The server processes the request synchronously or
         *     asynchronously and returns the result in this API.
         *
         * > **NOTE**
         * >
         * > - You are advised to overload **onRemoteMessageRequest** preferentially, which implements synchronous and
         * > asynchronous message processing.
         * >
         * > - If both **onRemoteRequest()** and **onRemoteMessageRequest()** are overloaded, only
         * > **onRemoteMessageRequest()** takes effect.
         *
         * @param { number } code - Service request code sent by the remote end.
         * @param { MessageSequence } data - **MessageSequence** object that holds the parameters called by the client.
         * @param { MessageSequence } reply - **MessageSequence** object to which the result is written.
         * @param { MessageOption } options - Whether the operation is synchronous or asynchronous.
         * @returns { boolean | Promise<boolean> } - If the request is processed synchronously in
         *     **onRemoteMessageRequest**, a Boolean value is returned. The value **true** means that the operation is
         *     successful, and **false** means the opposite.<br>- If the request is processed asynchronously in
         *     **onRemoteMessageRequest**, a promise object is returned. The value **true** means that the operation is
         *     successful, and **false** means the opposite.
         * @syscap SystemCapability.Communication.IPC.Core
         * @atomicservice [since 26.0.0]
         * @since 9
         */
        onRemoteMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption): boolean | Promise<boolean>;
        /**
         * Provides a response to **sendMessageRequest()**. The server processes the request and returns a response in this
         *     API. The IPC context can be obtained from the input parameter **callingInfo**.
         *
         * > **NOTE**
         * >
         * > You are advised to overload the **onRemoteMessageRequest** method with the **CallingInfo** parameter to
         * > implement synchronous and asynchronous message processing.
         * > If both **onRemoteRequest()** and **onRemoteMessageRequest()** are overloaded, only
         * > **onRemoteMessageRequest()** takes effect.
         *
         * @param { number } code - Service request code sent by the remote end.
         * @param { MessageSequence } data - **MessageSequence** object that holds the parameters called by the client.
         * @param { MessageSequence } reply - **MessageSequence** object to which the result is written.
         * @param { MessageOption } options - Whether the operation is synchronous or asynchronous.
         * @param { CallingInfo } [callingInfo] - IPC context.
         * @returns { boolean | Promise<boolean> } - If the request is processed synchronously in
         *     **onRemoteMessageRequest**, a Boolean value is returned. The value **true** means that the operation is
         *     successful, and **false** means the opposite.<br>- If the request is processed asynchronously in
         *     **onRemoteMessageRequest**, a promise object is returned. The value **true** means that the operation is
         *     successful, and **false** means the opposite.
         * @syscap SystemCapability.Communication.IPC.Core
         * @FaAndStageModel
         * @since 23
         */
        onRemoteMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption, callingInfo?: CallingInfo): boolean | Promise<boolean>;
        /**
         * Called to return a response to **sendRequest()**. The server processes the request and returns a response in this
         *     function.
         *
         * @param { number } code - Service request code sent by the remote end.
         * @param { MessageParcel } data - **MessageParcel** object that holds the parameters called by the client.
         * @param { MessageParcel } reply - **MessageParcel** object carrying the result.
         * @param { MessageOption } options - Whether the operation is synchronous or asynchronous.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead onRemoteMessageRequest(code: int, data: MessageSequence, reply: MessageSequence,
         *     options: MessageOption)
         */
        onRemoteRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean;
        /**
         * Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode
         *     is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The specific
         *     reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**,
         *     a promise will be fulfilled when the response to **sendRequest** is returned, and the reply message contains
         *     the returned information.
         *
         * @param { number } code - Message code [1-16777215] called by the request, which is determined by the
         *     communication parties. If the method is generated by an IDL tool, the message code is automatically generated
         *     by the IDL tool.
         * @param { MessageParcel } data - **MessageParcel** object holding the data to send.
         * @param { MessageParcel } reply - **MessageParcel** object that receives the response.
         * @param { MessageOption } options - Request sending mode, which can be synchronous (default) or asynchronous.
         * @returns { boolean } Returns **true** if the message is sent successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 8
         * @useinstead rpc.IRemoteObject#sendMessageRequest(code: int, data: MessageSequence, reply: MessageSequence,
         *     options: MessageOption)
         */
        sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean;
        /**
         * Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode
         *     is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The specific
         *     reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**,
         *     a promise will be fulfilled when the response to **sendRequest** is returned, and the reply message contains
         *     the returned information.
         *
         * @param { number } code - Message code [1-16777215] called by the request, which is determined by the
         *     communication parties. If the method is generated by an IDL tool, the message code is automatically generated
         *     by the IDL tool.
         * @param { MessageParcel } data - **MessageParcel** object holding the data to send.
         * @param { MessageParcel } reply - **MessageParcel** object that receives the response.
         * @param { MessageOption } options - Request sending mode, which can be synchronous (default) or asynchronous.
         * @returns { Promise<SendRequestResult> } Promise used to return a **sendRequestResult** instance.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.IRemoteObject#sendMessageRequest(code: int, data: MessageSequence, reply: MessageSequence,
         *     options: MessageOption)
         */
        sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): Promise<SendRequestResult>;
        /**
         * Sends a **MessageSequence** message to the remote process in synchronous or asynchronous mode. If asynchronous
         *     mode is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The
         *     specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in
         *     **options**, a promise will be fulfilled when the response to **sendMessageRequest** is returned, and the
         *     reply message contains the returned information.
         *
         * @param { number } code - Message code [1-16777215] called by the request, which is determined by the communication
         *     parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL
         *     tool.
         * @param { MessageSequence } data - **MessageSequence** object holding the data to send.
         * @param { MessageSequence } reply - **MessageSequence** object that receives the response.
         * @param { MessageOption } options - Request sending mode, which can be synchronous (default) or asynchronous.
         * @returns { Promise<RequestResult> } Promise used to return a **requestResult** instance.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.Failed to obtain the passed object instance.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption): Promise<RequestResult>;
        /**
         * Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode
         *     is set in **options**, a callback will be called immediately, and the reply message is empty. The specific
         *     reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**,
         *     a callback will be invoked when the response to **sendRequest** is returned, and the reply message contains
         *     the returned information.
         *
         * @param { number } code - Message code [1-16777215] called by the request, which is determined by the
         *     communication parties. If the method is generated by an IDL tool, the message code is automatically generated
         *     by the IDL tool.
         * @param { MessageParcel } data - **MessageParcel** object holding the data to send.
         * @param { MessageParcel} reply - **MessageParcel** object that receives the response.
         * @param { MessageOption } options - Request sending mode, which can be synchronous (default) or asynchronous.
         * @param { AsyncCallback<SendRequestResult> } callback - Callback for receiving the sending result.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.IRemoteObject#sendMessageRequest(code: int, data: MessageSequence, reply: MessageSequence,
         *     options: MessageOption, callback: AsyncCallback<RequestResult>)
         */
        sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption, callback: AsyncCallback<SendRequestResult>): void;
        /**
         * Sends a **MessageSequence** message to the remote process in synchronous or asynchronous mode. If asynchronous
         *     mode is set in **options**, a callback will be called immediately, and the reply message is empty. The
         *     specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in
         *     **options**, a callback will be invoked when the response to **sendMessageRequest** is returned, and the
         *     reply message contains the returned information.
         *
         * @param { number } code - Message code [1-16777215] called by the request, which is determined by the communication
         *     parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL
         *     tool.
         * @param { MessageSequence } data - **MessageSequence** object holding the data to send.
         * @param { MessageSequence } reply - **MessageSequence** object that receives the response.
         * @param { MessageOption } options - Request sending mode, which can be synchronous (default) or asynchronous.
         * @param { AsyncCallback<RequestResult> } callback - Callback for receiving the sending result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.Failed to obtain the passed object instance.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption, callback: AsyncCallback<RequestResult>): void;
        /**
         * Obtains the PID of the remote process.
         *
         * @returns { number } PID of the remote process obtained.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         */
        getCallingPid(): number;
        /**
         * Obtains the UID of the remote process.
         *
         * @returns { number } Return the UID of the {@link RemoteProxy} object.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         */
        getCallingUid(): number;
        /**
         * Binds an interface descriptor to an **IRemoteBroker** object.
         *
         * @param { IRemoteBroker } localInterface - **IRemoteBroker** object.
         * @param { string } descriptor - Interface descriptor.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead modifyLocalInterface(localInterface: IRemoteBroker, descriptor: string)
         */
        attachLocalInterface(localInterface: IRemoteBroker, descriptor: string): void;
        /**
         * Binds an interface descriptor to an **IRemoteBroker** object.
         *
         * @param { IRemoteBroker } localInterface - **IRemoteBroker** object.
         * @param { string } descriptor - **IRemoteBroker** object bound to the interface descriptor. The length of the
         *     descriptor must be less than 40960.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.The string length is greater than or equal to 40960;
         *     4.The number of bytes copied to the buffer is different from the length of the obtained string.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        modifyLocalInterface(localInterface: IRemoteBroker, descriptor: string): void;
    }
    /**
     * Provides APIs to implement **IRemoteObject**.
     *
     * @syscap SystemCapability.Communication.IPC.Core
     * @since 7
     */
    class RemoteProxy extends IRemoteObject {
        /**
         * Internal instruction code used to test whether the IPC service is normal.
         *
         * @default 1599098439
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         */
        static readonly PING_TRANSACTION: number;
        /**
         * Internal instruction code used to obtain IPC service status information.
         *
         * @default 1598311760
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         */
        static readonly DUMP_TRANSACTION: number;
        /**
         * Internal instruction code used to obtain the remote interface token.
         *
         * @default 1598968902
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         */
        static readonly INTERFACE_TRANSACTION: number;
        /**
         * Minimum valid instruction code.
         *
         * @default 0x1
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         */
        static readonly MIN_TRANSACTION_ID: number;
        /**
         * Maximum valid instruction code.
         *
         * @default 0x00FFFFFF
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         */
        static readonly MAX_TRANSACTION_ID: number;
        /**
         * Obtains the **LocalInterface** object of an interface token.
         *
         * @param { string } interface - Interface descriptor.
         * @returns { IRemoteBroker } Returns **Null** by default, which indicates a proxy interface.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.IRemoteObject#getLocalInterface(descriptor: string)
         */
        queryLocalInterface(interface: string): IRemoteBroker;
        /**
         * Obtains the **LocalInterface** object of an interface token.
         *
         * @param { string } interfaceDes - Interface descriptor.
         * @returns { IRemoteBroker } Returns **Null** by default, which indicates a proxy interface.
         * @throws { BusinessError } 401 - check param failed
         * @throws { BusinessError } 1900006 - Operation allowed only for the remote object.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        getLocalInterface(interfaceDes: string): IRemoteBroker;
        /**
         * Adds a callback for receiving death notifications of the remote object.
         *
         * @param { DeathRecipient } recipient - Callback to add.
         * @param { number } flags - Flag of the death notification. This parameter is reserved. It is set to **0**.
         * @returns { boolean } Returns **true** if the callback is added successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.IRemoteObject#registerDeathRecipient(recipient: DeathRecipient, flags: int)
         */
        addDeathRecipient(recipient: DeathRecipient, flags: number): boolean;
        /**
         * Registers a callback for receiving death notifications of the remote object.
         *
         * @param { DeathRecipient } recipient - Callback to register.
         * @param { number } flags - Flag of the death notification.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.The callback used to receive remote object death notifications is empty.
         * @throws { BusinessError } 1900008 - The proxy or remote object is invalid.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        registerDeathRecipient(recipient: DeathRecipient, flags: number): void;
        /**
         * Removes the callback used to receive death notifications of the remote object.
         *
         * @param { DeathRecipient } recipient - Callback to remove.
         * @param { number } flags - Flag of the death notification. This parameter is reserved. It is set to **0**.
         * @returns { boolean } Returns **true** if the callback is removed; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.IRemoteObject#unregisterDeathRecipient(recipient: DeathRecipient, flags: int)
         */
        removeDeathRecipient(recipient: DeathRecipient, flags: number): boolean;
        /**
         * Unregisters from the callback used to receive death notifications of the remote object.
         *
         * @param { DeathRecipient } recipient - Callback to unregister.
         * @param { number } flags - Flag of the death notification.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.The callback used to receive remote object death notifications is empty.
         * @throws { BusinessError } 1900008 - The proxy or remote object is invalid.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        unregisterDeathRecipient(recipient: DeathRecipient, flags: number): void;
        /**
         * Obtains the interface descriptor of this proxy object.
         *
         * @returns { string } Interface descriptor obtained.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead rpc.IRemoteObject#getDescriptor()
         */
        getInterfaceDescriptor(): string;
        /**
         * Obtains the interface descriptor (which is a string) of this object.
         *
         * @returns { string } Interface descriptor obtained.
         * @throws { BusinessError } 1900007 - communication failed.
         * @throws { BusinessError } 1900008 - The proxy or remote object is invalid.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        getDescriptor(): string;
        /**
         * Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode
         *     is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The specific
         *     reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**,
         *     a promise will be fulfilled when the response to **sendRequest** is returned, and the reply message contains
         *     the returned information.
         *
         * @param { number } code - Message code [1-16777215] called by the request, which is determined by the
         *     communication parties. If the method is generated by an IDL tool, the message code is automatically generated
         *     by the IDL tool.
         * @param { MessageParcel } data - **MessageParcel** object holding the data to send.
         * @param { MessageParcel } reply - **MessageParcel** object that receives the response.
         * @param { MessageOption } options - Request sending mode, which can be synchronous (default) or asynchronous.
         * @returns { boolean } Returns **true** if the message is sent successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 8
         * @useinstead rpc.IRemoteObject#sendMessageRequest(code: int, data: MessageSequence, reply: MessageSequence,
         *     options: MessageOption)
         */
        sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean;
        /**
         * Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode
         *     is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The specific
         *     reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**,
         *     a promise will be fulfilled when the response to **sendRequest** is returned, and the reply message contains
         *     the returned information.
         *
         * @param { number } code - Message code [1-16777215] called by the request, which is determined by the
         *     communication parties. If the method is generated by an IDL tool, the message code is automatically generated
         *     by the IDL tool.
         * @param { MessageParcel } data - **MessageParcel** object holding the data to send.
         * @param { MessageParcel} reply - **MessageParcel** object that receives the response.
         * @param { MessageOption } options - Request sending mode, which can be synchronous (default) or asynchronous.
         * @returns { Promise<SendRequestResult> } Promise used to return a **sendRequestResult** instance.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.IRemoteObject#sendMessageRequest(code: int, data: MessageSequence, reply: MessageSequence,
         *     options: MessageOption)
         */
        sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): Promise<SendRequestResult>;
        /**
         * Sends a **MessageSequence** message to the remote process in synchronous or asynchronous mode. If asynchronous
         *     mode is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The
         *     specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in
         *     **options**, a promise will be fulfilled when the response to **sendMessageRequest** is returned, and the
         *     reply message contains the returned information.
         *
         * @param { number } code - Message code [1-16777215] called by the request, which is determined by the communication
         *     parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL
         *     tool.
         * @param { MessageSequence } data - **MessageSequence** object holding the data to send.
         * @param { MessageSequence } reply - **MessageSequence** object that receives the response.
         * @param { MessageOption } options - Request sending mode, which can be synchronous (default) or asynchronous.
         * @returns { Promise<RequestResult> } Promise used to return a **requestResult** instance.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.Failed to obtain the passed object instance.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption): Promise<RequestResult>;
        /**
         * Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode
         *     is set in **options**, a callback will be called immediately, and the reply message is empty. The specific
         *     reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**,
         *     a callback will be invoked when the response to **sendRequest** is returned, and the reply message contains
         *     the returned information.
         *
         * @param { number } code - Message code [1-16777215] called by the request, which is determined by the
         *     communication parties. If the method is generated by an IDL tool, the message code is automatically generated
         *     by the IDL tool.
         * @param { MessageParcel } data - **MessageParcel** object holding the data to send.
         * @param { MessageParcel } reply - **MessageParcel** object that receives the response.
         * @param { MessageOption } options - Request sending mode, which can be synchronous (default) or asynchronous.
         * @param { AsyncCallback<SendRequestResult> } callback - Callback for receiving the sending result.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead rpc.IRemoteObject#sendMessageRequest(code: int, data: MessageSequence, reply: MessageSequence,
         *     options: MessageOption, callback: AsyncCallback<RequestResult>)
         */
        sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption, callback: AsyncCallback<SendRequestResult>): void;
        /**
         * Sends a **MessageSequence** message to the remote process in synchronous or asynchronous mode. If asynchronous
         *     mode is set in **options**, a callback will be called immediately, and the reply message is empty. The
         *     specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in
         *     **options**, a callback will be invoked at certain time after the response to **RequestResult** is returned,
         *     and the reply contains the returned information.
         *
         * @param { number } code - Message code [1-16777215] called by the request, which is determined by the communication
         *     parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL
         *     tool.
         * @param { MessageSequence } data - **MessageSequence** object holding the data to send.
         * @param { MessageSequence } reply - **MessageSequence** object that receives the response.
         * @param { MessageOption } options - Request sending mode, which can be synchronous (default) or asynchronous.
         * @param { AsyncCallback<RequestResult> } callback - Callback for receiving the sending result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.Failed to obtain the passed object instance.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption, callback: AsyncCallback<RequestResult>): void;
        /**
         * Checks whether the **RemoteObject** is dead.
         *
         * @returns { boolean } Returns **true** if **RemoteObject** is dead; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         */
        isObjectDead(): boolean;
    }
    /**
     * Obtains IPC context, including the UID and PID, local and remote device IDs, and whether the method is invoked on
     *     the same device.
     *
     * @syscap SystemCapability.Communication.IPC.Core
     * @since 7
     */
    class IPCSkeleton {
        /**
         * Obtains the system capability manager. This API is a static method.
         *
         * @returns { IRemoteObject } System capability manager obtained.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         */
        static getContextObject(): IRemoteObject;
        /**
         * Obtains the PID of the caller. This API is a static method, which is invoked by the **RemoteObject** object in
         *     the **onRemoteRequest** method. If this method is not invoked in the IPC context (**onRemoteRequest**), the
         *     PID of the process will be returned.
         *
         * @returns { number } PID of the caller.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         */
        static getCallingPid(): number;
        /**
         * Obtains the UID of the caller. This API is a static method, which is invoked by the **RemoteObject** object in
         *     the **onRemoteRequest** method. If this method is not invoked in the IPC context (**onRemoteRequest**), the
         *     UID of the process will be returned.
         *
         * @returns { number } UID of the caller.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         */
        static getCallingUid(): number;
        /**
         * Obtains the caller's token ID, which is used to verify the caller identity.
         *
         * @returns { number } Token ID of the caller obtained.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         */
        static getCallingTokenId(): number;
        /**
         * Obtains the ID of the device hosting the caller's process. This API is a static method.
         *
         * @returns { string } Device ID obtained.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         */
        static getCallingDeviceID(): string;
        /**
         * Obtains the local device ID. This API is a static method.
         *
         * @returns { string } Local device ID obtained.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         */
        static getLocalDeviceID(): string;
        /**
         * Checks whether the peer process is a process of the local device. This API is a static method.
         *
         * @returns { boolean } Returns **true** if the local and peer processes are on the same device; returns **false**
         *     otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         */
        static isLocalCalling(): boolean;
        /**
         * Flushes all suspended commands from the specified **RemoteProxy** to the corresponding **RemoteObject**. This API
         *     is a static method. You are advised to call this API before performing any sensitive operation.
         *
         * @param { IRemoteObject } object - **RemoteProxy** specified.
         * @returns { number } Returns **0** if the operation is successful; returns an error code if the input object is
         *     null or a **RemoteObject**, or if the operation fails.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead static flushCmdBuffer(object: IRemoteObject)
         */
        static flushCommands(object: IRemoteObject): number;
        /**
         * Flushes all suspended commands from the specified **RemoteProxy** to the corresponding **RemoteObject**. This API
         *     is a static method. You are advised to call this API before performing any sensitive operation.
         *
         * @param { IRemoteObject } object - **RemoteProxy** specified.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        static flushCmdBuffer(object: IRemoteObject): void;
        /**
         * Resets the UID and PID of the remote user to those of the local user. This API is a static method and is used in
         *     scenarios such as identity authentication.
         *
         * @returns { string } String containing the UID and PID of the remote user.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         */
        static resetCallingIdentity(): string;
        /**
         * Sets the UID and PID of the remote user. This API is a static method. It is usually called after
         *    **resetCallingIdentity**, and the UID and PID of the remote user returned by **resetCallingIdentity** are
         *    required.
         *
         * @param { string } identity - String containing the remote user's UID and PID, which are returned by
         *     **resetCallingIdentity**.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 7
         * @deprecated since 9
         * @useinstead static restoreCallingIdentity(identity: string)
         */
        static setCallingIdentity(identity: string): boolean;
        /**
         * Restores the UID and PID of the remote user. This API is a static method. It is usually called after
         *     **resetCallingIdentity**, and the UID and PID of the remote user returned by **resetCallingIdentity** are
         *     required.
         *
         * @param { string } identity - A string containing the UID and PID of the remote user. The length of the string
         *     must be less than 40960. are returned by **resetCallingIdentity**.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.The string length is greater than or equal to 40960;
         *     4.The number of bytes copied to the buffer is different from the length of the obtained string.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        static restoreCallingIdentity(identity: string): void;
    }
    /**
     * Provides methods related to anonymous shared memory objects, including creating, closing, mapping, and unmapping an
     *     **Ashmem** object, reading data from and writing data to an **Ashmem** object, obtaining the **Ashmem** size,
     *     and setting **Ashmem** protection. The shared memory applies only to cross-process communication within the
     *     local device.
     *
     * @syscap SystemCapability.Communication.IPC.Core
     * @since 8
     */
    class Ashmem {
        /**
         * Mapped memory protection type, indicating that the mapped memory is executable.
         *
         * @default 4
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         */
        static readonly PROT_EXEC: number;
        /**
         * Mapped memory protection type, indicating that the mapped memory cannot be accessed.
         *
         * @default 0
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         */
        static readonly PROT_NONE: number;
        /**
         * Mapped memory protection type, indicating that the mapped memory is readable.
         *
         * @default 1
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         */
        static readonly PROT_READ: number;
        /**
         * Mapped memory protection type, indicating that the mapped memory is readable.
         *
         * @default 2
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         */
        static readonly PROT_WRITE: number;
        /**
         * Creates an **Ashmem** object with the specified name and size. This API is a static method.
         *
         * @param { string } name - Name of the **Ashmem** object to create.
         * @param { number } size - Size (in bytes) of the **Ashmem** object to create.
         * @returns { Ashmem } Returns the **Ashmem** object if it is created successfully; returns null otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead create()
         */
        static createAshmem(name: string, size: number): Ashmem;
        /**
         * Creates an **Ashmem** object with the specified name and size. This API is a static method.
         *
         * @param { string } name - Name of the **Ashmem** object to create. The length of the Ashmem name cannot be 0.
         * @param { number } size - Size of the **Ashmem** object, in bytes. The value must be greater than 0.
         * @returns { Ashmem } Returns the **Ashmem** object if it is created successfully; returns null otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.The Ashmem name passed is empty;
         *     4.The Ashmem size passed is less than or equal to 0.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        static create(name: string, size: number): Ashmem;
        /**
         * Creates an **Ashmem** object by copying the file descriptor of an existing **Ashmem** object. The two **Ashmem**
         *     objects point to the same shared memory region.
         *
         * @param { Ashmem } ashmem - Existing **Ashmem** object.
         * @returns { Ashmem } **Ashmem** object created.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead create()
         */
        static createAshmemFromExisting(ashmem: Ashmem): Ashmem;
        /**
         * Creates an **Ashmem** object by copying the file descriptor of an existing **Ashmem** object. The two **Ashmem**
         *     objects point to the same shared memory region.
         *
         * @param { Ashmem } ashmem - Existing **Ashmem** object.
         * @returns { Ashmem } **Ashmem** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The passed parameter is not an Ashmem object;
         *     3.The ashmem instance for obtaining packaging is empty.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        static create(ashmem: Ashmem): Ashmem;
        /**
         * Closes this **Ashmem** object.
         *
         * > **NOTE**
         * >
         * > Before closing the **Ashmem** object, you need to remove the address mapping.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         */
        closeAshmem(): void;
        /**
         * Deletes the mappings for the specified address range of this **Ashmem** object.
         *
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         */
        unmapAshmem(): void;
        /**
         * Obtains the memory size of this **Ashmem** object.
         *
         * @returns { number } **Ashmem** size obtained.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         */
        getAshmemSize(): number;
        /**
         * Creates the shared file mapping on the virtual address space of this process. The size of the mapping region is
         *     specified by this **Ashmem** object.
         *
         * @param { number } mapType - Protection level of the memory region to which the shared file is mapped.
         * @returns { boolean } Returns **true** if the mapping is created; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead mapTypedAshmem(mapType: int)
         */
        mapAshmem(mapType: number): boolean;
        /**
         * Creates the shared file mapping on the virtual address space of this process. The size of the mapping region is
         *     specified by this **Ashmem** object.
         *
         * @param { number } mapType - Protection level of the memory region to which the shared file is mapped.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.The passed mapType exceeds the maximum protection level.
         * @throws { BusinessError } 1900001 - Failed to call mmap.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        mapTypedAshmem(mapType: number): void;
        /**
         * Maps the shared file to the readable and writable virtual address space of the process.
         *
         * @returns { boolean } Returns **true** if the mapping is created; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead mapReadWriteAshmem()
         */
        mapReadAndWriteAshmem(): boolean;
        /**
         * Maps the shared file to the readable and writable virtual address space of the process.
         *
         * @throws { BusinessError } 1900001 - Failed to call mmap.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        mapReadWriteAshmem(): void;
        /**
         * Maps the shared file to the read-only virtual address space of the process.
         *
         * @returns { boolean } Returns **true** if the mapping is created; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead mapReadonlyAshmem()
         */
        mapReadOnlyAshmem(): boolean;
        /**
         * Maps the shared file to the read-only virtual address space of the process.
         *
         * @throws { BusinessError } 1900001 - Failed to call mmap.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        mapReadonlyAshmem(): void;
        /**
         * Sets the protection level of the memory region to which the shared file is mapped.
         *
         * @param { number } protectionType - Protection type to set.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead setProtectionType(protectionType: int)
         */
        setProtection(protectionType: number): boolean;
        /**
         * Sets the protection level of the memory region to which the shared file is mapped.
         *
         * @param { number } protectionType - Protection type to set.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @throws { BusinessError } 1900002 - Failed to call ioctl.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         */
        setProtectionType(protectionType: number): void;
        /**
         * Writes data to the shared file associated with this **Ashmem** object.
         *
         * > **NOTE**
         * >
         * > - Before writing an **Ashmem** object, you need to call
         * > [mapReadWriteAshmem]{@link rpc.Ashmem#mapReadWriteAshmem()} for mapping.
         *
         * @param { number[] } buf - Data to write.
         * @param { number } size - Size of the data to write.
         * @param { number } offset - Start position of the data to write in the memory region associated with this
         *     **Ashmem** object.
         * @returns { boolean } Returns **true** if the data is written successfully; returns **false** otherwise.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead writeDataToAshmem(buf: ArrayBuffer, size: int, offset: int)
         */
        writeToAshmem(buf: number[], size: number, offset: number): boolean;
        /**
         * Writes data to the shared file associated with this **Ashmem** object.
         *
         * > **NOTE**
         * >
         * > - Before writing an **Ashmem** object, you need to call
         * > [mapReadWriteAshmem]{@link rpc.Ashmem#mapReadWriteAshmem()} for mapping.
         *
         * @param { number[] } buf - Data to write.
         * @param { number } size - Size of the data to write.
         * @param { number } offset - Start position of the data to write in the memory region associated with this
         *     **Ashmem** object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.The element does not exist in the array.
         * @throws { BusinessError } 1900003 - Failed to write data to the shared memory.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         * @deprecated since 11
         * @useinstead writeDataToAshmem(buf: ArrayBuffer, size: int, offset: int)
         */
        writeAshmem(buf: number[], size: number, offset: number): void;
        /**
         * Writes data to the shared file associated with this **Ashmem** object.
         *
         * > **NOTE**
         * >
         * > Before writing an **Ashmem** object, you need to call
         * > [mapReadWriteAshmem]{@link rpc.Ashmem#mapReadWriteAshmem()} for mapping.
         *
         * @param { ArrayBuffer } buf - Data to write.
         * @param { number } size - Size of the data to write.
         * @param { number } offset - Start position of the data to write in the memory region associated with this **Ashmem**
         *     object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match;
         *     3.Failed to obtain arrayBuffer information.
         * @throws { BusinessError } 1900003 - Failed to write data to the shared memory.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 11
         */
        writeDataToAshmem(buf: ArrayBuffer, size: number, offset: number): void;
        /**
         * Reads data from the shared file associated with this **Ashmem** object.
         *
         * > **NOTE**
         * >
         * > - Before writing an **Ashmem** object, you need to call
         * > [mapReadWriteAshmem]{@link rpc.Ashmem#mapReadWriteAshmem()} for mapping.
         *
         * @param { number } size - Size of the data to read.
         * @param { number } offset - Start position of the data to read in the memory region associated with this
         *     **Ashmem** object.
         * @returns { number[] } Data read.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 8
         * @deprecated since 9
         * @useinstead readDataFromAshmem(size: int, offset: int)
         */
        readFromAshmem(size: number, offset: number): number[];
        /**
         * Reads data from the shared file associated with this **Ashmem** object.
         *
         * > **NOTE**
         * >
         * > - Before writing an **Ashmem** object, you need to call
         * > [mapReadWriteAshmem]{@link rpc.Ashmem#mapReadWriteAshmem()} for mapping.
         *
         * @param { number } size - Size of the data to read.
         * @param { number } offset - Start position of the data to read in the memory region associated with this
         *     **Ashmem** object.
         * @returns { number[] } Data read.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @throws { BusinessError } 1900004 - Failed to read data from the shared memory.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 9
         * @deprecated since 11
         * @useinstead readDataFromAshmem(size: int, offset: int)
         */
        readAshmem(size: number, offset: number): number[];
        /**
         * Reads data from the shared file associated with this **Ashmem** object.
         *
         * > **NOTE**
         * >
         * > Before writing an **Ashmem** object, you need to call
         * > [mapReadWriteAshmem]{@link rpc.Ashmem#mapReadWriteAshmem()} for mapping.
         *
         * @param { number } size - Size of the data to read.
         * @param { number } offset - Start position of the data to read in the memory region associated with this **Ashmem**
         *     object.
         * @returns { ArrayBuffer } Data read.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.The number of parameters is incorrect;
         *     2.The parameter type does not match.
         * @throws { BusinessError } 1900004 - Failed to read data from the shared memory.
         * @syscap SystemCapability.Communication.IPC.Core
         * @since 11
         */
        readDataFromAshmem(size: number, offset: number): ArrayBuffer;
    }
}
export default rpc;

```
