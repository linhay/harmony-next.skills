# @ohos.multimodalAwareness.metadataBinding.d.ts

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
 * @kit MultimodalAwarenessKit
 */
import type { Callback } from './@ohos.base';
/**
 * The **metadataBinding** module provides metadata binding–specific functions such as metadata transfer, event
 * subscription, and event unsubscription.
 *
 * @syscap SystemCapability.MultimodalAwareness.MetadataBinding
 * @atomicservice
 * @since 18
 */
declare namespace metadataBinding {
    /**
     * Transfers the metadata to be encoded to the MSDP. The MSDP determines whether to transfer the metadata to the
     * system application or service that calls the encoding API.
     *
     * @param { string } metadata - Metadata to be encoded.
     * @throws { BusinessError } 32100001 - Internal handling failed.
     * @syscap SystemCapability.MultimodalAwareness.MetadataBinding
     * @atomicservice
     * @since 18
     */
    function submitMetadata(metadata: string): void;
    /**
     * Subscribes to a system event to obtain the encoded metadata. The application needs to register a callback to return
     * the encoded metadata when the registered system event occurs.
     *
     * @param { 'operationSubmitMetadata' } type - Event type. This parameter has a fixed value of
     *     **operationSubmitMetadata**, indicating the system application's attempt to obtain the encoded metadata.
     * @param { string } bundleName - Application bundle name.
     * @param { Callback<number> } callback - Callback used to return the encoded metadata.
     * @throws { BusinessError } 32100001 - Internal handling failed.
     * @throws { BusinessError } 32100004 - Subscribe Failed. Possible causes:
     *     <br>1. Abnormal system capability.
     *     <br>2. IPC communication abnormality.
     *     <br>3. Algorithm loading exception.
     * @syscap SystemCapability.MultimodalAwareness.MetadataBinding
     * @atomicservice
     * @since 18
     */
    function on(type: 'operationSubmitMetadata', bundleName: string, callback: Callback<number>): void;
    /**
     * Unsubscribes from system events that are used to obtain the encoded metadata. The respective callback will be
     * unregistered.
     *
     * @param { 'operationSubmitMetadata' } type - Event type. This parameter has a fixed value of
     *     **operationSubmitMetadata**, indicating the system application's attempt to obtain the encoded metadata.
     * @param { string } bundleName - Application bundle name.
     * @param { Callback<number> } [callback] - Callback used to return the encoded metadata.
     * @throws { BusinessError } 32100001 - Internal handling failed.
     * @throws { BusinessError } 32100005 - Unsubscribe Failed. Possible causes:
     *     <br> 1. Abnormal system capability.
     *     <br> 2. IPC communication abnormality.
     * @syscap SystemCapability.MultimodalAwareness.MetadataBinding
     * @atomicservice
     * @since 18
     */
    function off(type: 'operationSubmitMetadata', bundleName: string, callback?: Callback<number>): void;
}
export default metadataBinding;

```
