# @ohos.application.testRunner.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2023 Huawei Device Co., Ltd.
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
 * The **TestRunner** module provides a test framework. You can use the APIs of this module to prepare the unit test
 * environment and run test cases.
 * To implement your own unit test framework, extend this class and override its APIs.
 *
 * > **NOTE**
 * >
 * > The APIs of this module can be used only in [JsUnit](docroot://application-test/unittest-guidelines.md).
 *
 * @file
 * @kit TestKit
 */
/**
 * Stop all test cases.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 26.0.0
 */
type OnStopFn = () => void;
/**
 * Base class for the test framework.
 * If you want to implement your own unit test framework, you must inherit this class and overrides all its methods.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @atomicservice [since 11]
 * @since 8
 */
interface TestRunner {
    /**
     * Prepare the unit testing environment for running test cases.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 11]
     * @since 8
     */
    onPrepare(): void;
    /**
     * Run all test cases.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 11]
     * @since 8
     */
    onRun(): void;
    /**
     * Stop all test cases.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    onStop?: OnStopFn;
}
/*** if arkts 1.1 */
export { TestRunner };
/*** endif */
export default TestRunner;

```
