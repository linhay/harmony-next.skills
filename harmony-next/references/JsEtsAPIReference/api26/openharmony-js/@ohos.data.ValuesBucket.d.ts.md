# @ohos.data.ValuesBucket.d.ts

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
 * **ValuesBucket** is a dataset in the form of key-value (KV) pairs that can be inserted in the database.
 *
 * @file
 * @kit ArkData
 */
/**
 * Defines the value types allowed in a **ValuesBucket** instance.
 *
 * @unionmember { number } The value is a number. [since 12 - 19]
 * @unionmember { long } [since 20]
 * @unionmember { double } [since 20]
 * @unionmember { string } The value is a string. [since 12]
 * @unionmember { boolean } The value is **true** or **false**. [since 12]
 * @syscap SystemCapability.DistributedDataManager.DataShare.Core
 * @stagemodelonly
 * @crossplatform [since 12]
 * @atomicservice [since 20]
 * @since 10
 */
export type ValueType = number | string | boolean;
/**
 * Defines the types of the key and value in a KV pair. This type is not multi-thread safe. If a **ValuesBucket**
 * instance is operated by multiple threads at the same time in an application, use a lock for it.
 *
 * @syscap SystemCapability.DistributedDataManager.DataShare.Core
 * @stagemodelonly
 * @since 10
 */
export type ValuesBucket = Record<string, ValueType | Uint8Array | null>;

```
