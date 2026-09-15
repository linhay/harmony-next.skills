# @ohos.userIAM.userAuth.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023-2026 Huawei Device Co., Ltd.
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
 * @file User Authentication
 * @kit UserAuthenticationKit
 */
import type { AsyncCallback } from './@ohos.base';
/**
 * The **userAuth** module is the core module for user authentication in OpenHarmony. It provides authentication
 * capabilities in scenarios such as device unlocking, payment verification, and application login.
 *
 * This module supports multiple biometric authentication methods (face, fingerprint) and password authentication (PIN),
 * and provides various security trust levels. Since API version 26.0.0, the companion device authentication mode is
 * added.
 *
 * This module applies to the following scenarios:
 *
 * - Device unlocking authentication.
 * - Financial payment verification.
 * - Application login protection.
 * - Confirmation for sensitive operations.
 *
 * @syscap SystemCapability.UserIAM.UserAuth.Core
 * @atomicservice [since 12]
 * @since 6
 */
declare namespace userAuth {
    /**
     * Maximum reuse duration of the authentication result, in milliseconds. The value is **300000** (5 minutes). This
     * constant is used to limit the maximum duration for reusing an authentication result, preventing security risks
     * caused by reusing expired authentication results for a long time. It can be used as the maximum value of the
     * **reuseDuration** parameter in [ReuseUnlockResult]{@link userAuth.ReuseUnlockResult}.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @atomicservice
     * @since 12
     */
    const MAX_ALLOWABLE_REUSE_DURATION: 300000;
    /**
     * Permanent lockout duration, in milliseconds. The value is **0x7fffffff**. When the number of failed authentication
     * attempts reaches the upper limit, the authenticator enters the permanent lockout status. In this case, PIN
     * authentication is required for unlocking. This value is used to identify the permanent lockout status of the
     * authenticator, which can be returned by the **lockoutDuration** field in
     * [AuthLockState]{@link userAuth.AuthLockState}.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @atomicservice
     * @since 22
     */
    const PERMANENT_LOCKOUT_DURATION: number = 0x7fffffff;
    /**
     * Enumerates the authentication results.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @since 6
     * @deprecated since 8
     * @useinstead userAuth.UserAuthResultCode
     */
    export enum AuthenticationResult {
        /**
         * The device does not support the current authentication mode.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 6
         * @deprecated since 8
         * @useinstead userAuth.ResultCode.TYPE_NOT_SUPPORT
         */
        NO_SUPPORT = -1,
        /**
         * The authentication is successful.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 6
         * @deprecated since 8
         * @useinstead userAuth.ResultCode.SUCCESS
         */
        SUCCESS = 0,
        /**
         * The feature comparison failed.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 6
         * @deprecated since 8
         * @useinstead userAuth.ResultCode.FAIL
         */
        COMPARE_FAILURE = 1,
        /**
         * The authentication was canceled by the user.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 6
         * @deprecated since 8
         * @useinstead userAuth.ResultCode.CANCELED
         */
        CANCELED = 2,
        /**
         * The authentication has timed out.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 6
         * @deprecated since 8
         * @useinstead userAuth.ResultCode.TIMEOUT
         */
        TIMEOUT = 3,
        /**
         * The camera failed to start.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 6
         * @deprecated since 8
         */
        CAMERA_FAIL = 4,
        /**
         * The authentication service is not available. Try again later.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 6
         * @deprecated since 8
         * @useinstead userAuth.ResultCode.BUSY
         */
        BUSY = 5,
        /**
         * The authentication parameters are invalid.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 6
         * @deprecated since 8
         * @useinstead userAuth.ResultCode.INVALID_PARAMETERS
         */
        INVALID_PARAMETERS = 6,
        /**
         * The user account is locked because the number of authentication failures has reached the threshold.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 6
         * @deprecated since 8
         * @useinstead userAuth.ResultCode.LOCKED
         */
        LOCKED = 7,
        /**
         * No authentication credential is registered.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 6
         * @deprecated since 8
         * @useinstead userAuth.ResultCode.NOT_ENROLLED
         */
        NOT_ENROLLED = 8,
        /**
         * Other errors.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 6
         * @deprecated since 8
         * @useinstead userAuth.ResultCode.GENERAL_ERROR
         */
        GENERAL_ERROR = 100
    }
    /**
     * Enumerates the authentication types.
     *
     * @unionmember { 'ALL' } reserved and not supported by the current version.
     * @unionmember { 'FACE_ONLY' } facial authentication.
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @since 6
     * @deprecated since 8
     * @useinstead userAuth.UserAuthType
     */
    type AuthType = 'ALL' | 'FACE_ONLY';
    /**
     * Enumerates the authentication security levels.
     *
     * @unionmember { 'S1' } authentication trust level 1. The authentication of this level can identify individual users
     *     and provides limited liveness detection capabilities. It is usually used in service risk control and query of
     *     general personal data.
     * @unionmember { 'S2' } authentication trust level 2. The authentication of this level can accurately identify
     *     individual users and provides regular liveness detection capabilities. It is usually used in scenarios such as
     *     application logins and keeping the unlocking state of a device.
     * @unionmember { 'S3' } authentication trust level 3. The authentication of this level can accurately identify
     *     individual users and provides strong liveness detection capabilities. It is usually used in scenarios such as
     *     unlocking a device.
     * @unionmember { 'S4' } authentication trust level 4. The authentication of this level can accurately identify
     *     individual users and provides powerful liveness detection capabilities. It is usually used in scenarios such as
     *     small-amount payment.
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @since 6
     * @deprecated since 8
     * @useinstead userAuth.AuthTrustLevel
     */
    type SecureLevel = 'S1' | 'S2' | 'S3' | 'S4';
    /**
     * Provides APIs for managing the **Authenticator** object.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @since 6
     * @deprecated since 8
     * @useinstead userAuth.AuthInstance
     */
    interface Authenticator {
        /**
         * Starts user authentication. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.ACCESS_BIOMETRIC
         * @param { AuthType } type - Authentication type. Currently, only **FACE_ONLY** is supported.
         *     <br>**ALL** is reserved and not supported by the current version.
         * @param { SecureLevel } level - Security level of the authentication. It can be **S1** (lowest), **S2**, **S3**,
         *     or **S4** (highest).
         *     <br>Devices capable of 3D facial recognition support S3 and lower-level authentication.
         *     <br>Devices capable of 2D facial recognition support S2 and lower-level authentication.
         * @param { AsyncCallback<number> } callback - Callback used to return the result. **number** indicates the
         *     [AuthenticationResult]{@link userAuth.AuthenticationResult}.
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 6
         * @deprecated since 8
         * @useinstead userAuth.AuthInstance.start
         */
        execute(type: AuthType, level: SecureLevel, callback: AsyncCallback<number>): void;
        /**
         * Starts user authentication. This API uses a promise to return the result.
         *
         * @permission ohos.permission.ACCESS_BIOMETRIC
         * @param { AuthType } type - Authentication type. Currently, only **FACE_ONLY** is supported.
         *     <br>**ALL** is reserved and not supported by the current version.
         * @param { SecureLevel } level - Security level of the authentication. It can be **S1** (lowest), **S2**, **S3**,
         *     or **S4** (highest).
         *     <br>Devices capable of 3D facial recognition support S3 and lower-level authentication.
         *     <br>Devices capable of 2D facial recognition support S2 and lower-level authentication.
         * @returns { Promise<number> } Promise used to return the authentication result, which is a number. For details,
         *     see [AuthenticationResult]{@link userAuth.AuthenticationResult}.
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 6
         * @deprecated since 8
         * @useinstead userAuth.AuthInstance.start
         */
        execute(type: AuthType, level: SecureLevel): Promise<number>;
    }
    /**
     * Obtains an **Authenticator** instance for user authentication.
     *
     * @returns { Authenticator } **Authenticator** instance obtained.
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @since 6
     * @deprecated since 8
     * @useinstead userAuth.getAuthInstance
     */
    function getAuthenticator(): Authenticator;
    /**
     * Provides APIs for managing the **UserAuth** object.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @since 8
     * @deprecated since 9
     * @useinstead userAuth.AuthInstance
     */
    class UserAuth {
        /**
         * A constructor used to create a **UserAuth** instance.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 9
         * @useinstead userAuth.getAuthInstance
         */
        constructor();
        /**
         * Obtains the version of this authenticator.
         *
         * @permission ohos.permission.ACCESS_BIOMETRIC
         * @returns { number } Authenticator version obtained.
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 9
         */
        getVersion(): number;
        /**
         * Checks whether the specified authentication capability is supported.
         *
         * @permission ohos.permission.ACCESS_BIOMETRIC
         * @param { UserAuthType } authType - Authentication type. Currently, **FACE** and **FINGERPRINT** are supported.
         * @param { AuthTrustLevel } authTrustLevel - Authentication trust level.
         * @returns { number } Query result. If the authentication capability is supported, **SUCCESS** is returned.
         *     Otherwise, a [ResultCode]{@link userAuth.ResultCode} is returned.
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 9
         * @useinstead userAuth.getAvailableStatus
         */
        getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): number;
        /**
         * Starts user authentication. This API uses a callback to return the result.
         *
         * @permission ohos.permission.ACCESS_BIOMETRIC
         * @param { Uint8Array } challenge - Challenge value, which can be passed in Uint8Array([]) format.
         * @param { UserAuthType } authType - Authentication type. Currently, **FACE** and **FINGERPRINT** are supported.
         * @param { AuthTrustLevel } authTrustLevel - Authentication trust level.
         * @param { IUserAuthCallback } callback - Callback used to return the result.
         * @returns { Uint8Array } Context ID, which is used as the input parameter of
         *     [cancelAuth]{@link userAuth.UserAuth#cancelAuth}.
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 9
         * @useinstead userAuth.AuthInstance.start
         */
        auth(challenge: Uint8Array, authType: UserAuthType, authTrustLevel: AuthTrustLevel, callback: IUserAuthCallback): Uint8Array;
        /**
         * Cancels the authentication based on the context ID.
         *
         * @permission ohos.permission.ACCESS_BIOMETRIC
         * @param { Uint8Array } contextID - Context ID, which is obtained by [auth]{@link userAuth.UserAuth#auth}.
         * @returns { number } Returns **SUCCESS** if the cancellation is successful. Returns a
         *     [ResultCode]{@link userAuth.ResultCode} otherwise.
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 9
         * @useinstead userAuth.AuthInstance.cancel
         */
        cancelAuth(contextID: Uint8Array): number;
    }
    /**
     * Provides callbacks to return the authentication result.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @since 8
     * @deprecated since 9
     * @useinstead userAuth.AuthEvent
     */
    interface IUserAuthCallback {
        /**
         * Called to return the authentication result.
         *
         * - **result**: Authentication result. For details, see [ResultCode]{@link userAuth.ResultCode}.
         * - **extraInfo**: Extended information, which varies depending on the authentication result. If the authentication
         * is successful, the user authentication token will be returned in **extraInfo**. If the authentication fails, the
         * remaining number of authentication times will be returned in **extraInfo**. If the authentication executor is
         * locked, the freeze time will be returned in **extraInfo**.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 9
         * @useinstead userAuth.AuthEvent.callback
         */
        onResult: (result: number, extraInfo: AuthResult) => void;
        /**
         * Called to acquire authentication tip information. This API is optional.
         *
         * - **module**: ID of the module that sends the tip information.
         * - **acquire**: Authentication tip information.
         * - **extraInfo**: Reserved field.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 9
         * @useinstead userAuth.AuthEvent.callback
         */
        onAcquireInfo?: (module: number, acquire: number, extraInfo: any) => void;
    }
    /**
     * Represents the authentication result object.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @since 8
     * @deprecated since 9
     * @useinstead userAuth.AuthResultInfo
     */
    interface AuthResult {
        /**
         * Authentication token information.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 9
         * @useinstead userAuth.AuthResultInfo.token
         */
        token?: Uint8Array;
        /**
         * Number of remaining authentication operations.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 9
         * @useinstead userAuth.AuthResultInfo.remainAttempts
         */
        remainTimes?: number;
        /**
         * Time for which the authentication operation is frozen. The unit is milliseconds.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 9
         * @useinstead userAuth.AuthResultInfo.lockoutDuration
         */
        freezingTime?: number;
    }
    /**
     * Enumerates the authentication result codes.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @since 8
     * @deprecated since 9
     * @useinstead userAuth.UserAuthResultCode
     */
    enum ResultCode {
        /**
         * The operation is successful.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 9
         * @useinstead userAuth.UserAuthResultCode.SUCCESS
         */
        SUCCESS = 0,
        /**
         * The authentication failed.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 9
         * @useinstead userAuth.UserAuthResultCode.FAIL
         */
        FAIL = 1,
        /**
         * A general operation error occurred.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 9
         * @useinstead userAuth.UserAuthResultCode.GENERAL_ERROR
         */
        GENERAL_ERROR = 2,
        /**
         * The authentication is canceled.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 9
         * @useinstead userAuth.UserAuthResultCode.CANCELED
         */
        CANCELED = 3,
        /**
         * The authentication timed out.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 9
         * @useinstead userAuth.UserAuthResultCode.TIMEOUT
         */
        TIMEOUT = 4,
        /**
         * The authentication type is not supported.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 9
         * @useinstead userAuth.UserAuthResultCode.TYPE_NOT_SUPPORT
         */
        TYPE_NOT_SUPPORT = 5,
        /**
         * The authentication trust level is not supported.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 9
         * @useinstead userAuth.UserAuthResultCode.TRUST_LEVEL_NOT_SUPPORT
         */
        TRUST_LEVEL_NOT_SUPPORT = 6,
        /**
         * Indicates the busy state.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 9
         * @useinstead userAuth.UserAuthResultCode.BUSY
         */
        BUSY = 7,
        /**
         * Invalid parameters are detected.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 9
         * @useinstead userAuth.UserAuthResultCode.INVALID_PARAMETERS
         */
        INVALID_PARAMETERS = 8,
        /**
         * The authentication executor is locked.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 9
         * @useinstead userAuth.UserAuthResultCode.LOCKED
         */
        LOCKED = 9,
        /**
         * The user has not enrolled the authentication information.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 9
         * @useinstead userAuth.UserAuthResultCode.NOT_ENROLLED
         */
        NOT_ENROLLED = 10
    }
    /**
     * Enumerates the tip codes used during the facial authentication process.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @since 8
     * @deprecated since 11
     */
    enum FaceTips {
        /**
         * The obtained facial image is too bright due to high illumination.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 11
         */
        FACE_AUTH_TIP_TOO_BRIGHT = 1,
        /**
         * The obtained facial image is too dark due to low illumination.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 11
         */
        FACE_AUTH_TIP_TOO_DARK = 2,
        /**
         * The face is too close to the device.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 11
         */
        FACE_AUTH_TIP_TOO_CLOSE = 3,
        /**
         * The face is too far away from the device.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 11
         */
        FACE_AUTH_TIP_TOO_FAR = 4,
        /**
         * Only the upper part of the face is captured because the device is angled too high.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 11
         */
        FACE_AUTH_TIP_TOO_HIGH = 5,
        /**
         * Only the lower part of the face is captured because the device is angled too low.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 11
         */
        FACE_AUTH_TIP_TOO_LOW = 6,
        /**
         * Only the right part of the face is captured because the device is deviated to the right.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 11
         */
        FACE_AUTH_TIP_TOO_RIGHT = 7,
        /**
         * Only the left part of the face is captured because the device is deviated to the left.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 11
         */
        FACE_AUTH_TIP_TOO_LEFT = 8,
        /**
         * The face moves too fast during facial information collection.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 11
         */
        FACE_AUTH_TIP_TOO_MUCH_MOTION = 9,
        /**
         * The face is not facing the camera.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 11
         */
        FACE_AUTH_TIP_POOR_GAZE = 10,
        /**
         * No face is detected.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 11
         */
        FACE_AUTH_TIP_NOT_DETECTED = 11
    }
    /**
     * Enumerates the tip codes used during the fingerprint authentication process.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @since 8
     * @deprecated since 11
     */
    enum FingerprintTips {
        /**
         * The obtained fingerprint image is in good condition.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 11
         */
        FINGERPRINT_AUTH_TIP_GOOD = 0,
        /**
         * Large fingerprint image noise is detected due to suspicious or detected dirt on the sensor.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 11
         */
        FINGERPRINT_AUTH_TIP_DIRTY = 1,
        /**
         * The noise of the fingerprint image is too large to be processed.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 11
         */
        FINGERPRINT_AUTH_TIP_INSUFFICIENT = 2,
        /**
         * Incomplete fingerprint image is detected.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 11
         */
        FINGERPRINT_AUTH_TIP_PARTIAL = 3,
        /**
         * The fingerprint image is incomplete due to fast movement.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 11
         */
        FINGERPRINT_AUTH_TIP_TOO_FAST = 4,
        /**
         * Failed to obtain the fingerprint image because the finger seldom moves.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 8
         * @deprecated since 11
         */
        FINGERPRINT_AUTH_TIP_TOO_SLOW = 5
    }
    /**
     * Enumerates the identity authentication types. This enum defines the authentication types supported by the system,
     * including PIN authentication and biometric authentication (face and fingerprint). When initiating authentication,
     * an application needs to specify the authentication type list, and the user can select any of the authentication
     * types to complete the authentication. The security strength and user experience vary depending on authentication
     * types. The application needs to select a proper authentication type based on service scenarios.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @atomicservice [since 12]
     * @since 8
     */
    enum UserAuthType {
        /**
         * PIN authentication. It indicates that the user enters the PIN to complete authentication. PIN authentication has
         * a high security level of ATL4. It is applicable to scenarios requiring high security, such as payment and
         * confirmation of important operations. However, users need to manually enter information, which is not as
         * convenient as biometric authentication.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 10
         */
        PIN = 1,
        /**
         * Face authentication. It indicates that the system checks whether the facial features of a user match the enrolled
         * face. Face authentication supports different levels of liveness detection. For details about the classification
         * principles, see
         * [Principles for Classifying Biometric Authentication Trust Levels](docroot://security/UserAuthenticationKit/user-authentication-overview.md#principles-for-classifying-biometric-authentication-trust-levels).
         * The advantage is convenient user experience, but the disadvantage is that there are certain requirements on the
         * device and lighting conditions.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 8
         */
        FACE = 2,
        /**
         * Fingerprint authentication. It indicates that the user is authenticated through the fingerprint sensor. The
         * system checks whether the user fingerprint matches the enrolled fingerprint. Fingerprint authentication supports
         * multiple trust levels. For details about the classification principles, see
         * [Principles for Classifying Biometric Authentication Trust Levels](docroot://security/UserAuthenticationKit/user-authentication-overview.md#principles-for-classifying-biometric-authentication-trust-levels).
         * It is applicable to medium-security scenarios. The advantage is that the operation is simple and quick. The
         * disadvantage is that the device must be equipped with a fingerprint sensor, and wet hands or fingerprint abrasion
         * may affect the recognition effect.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 8
         */
        FINGERPRINT = 4,
        /**
         * Companion device authentication. It indicates that the user completes the authentication through the companion
         * device. Companion device authentication supports multiple trust levels. For details about the classification
         * principles, see
         * [Principles for Classifying Biometric Authentication Trust Levels](docroot://security/UserAuthenticationKit/user-authentication-overview.md#principles-for-classifying-biometric-authentication-trust-levels).
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        COMPANION_DEVICE = 64
    }
    /**
     * Enumerates the trust levels of the authentication result. This enum defines four trust levels of the authentication
     * result, which are used to describe the security strength of the authentication result. A higher trust level
     * indicates a stronger liveness detection capability and more accurate user identity recognition of the
     * authentication solution, and is applicable to service scenarios that require higher security. The application
     * should select a proper authentication trust level based on the security requirements of service scenarios.
     *
     * For typical use cases, see
     * [Principles for Classifying Biometric Authentication Trust Levels](docroot://security/UserAuthenticationKit/user-authentication-overview.md#principles-for-classifying-biometric-authentication-trust-levels).
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @atomicservice [since 12]
     * @since 8
     */
    enum AuthTrustLevel {
        /**
         * Authentication trust level 1. It can identify individual users and provides basic liveness detection capabilities
         * (such as simple action detection). The security strength is low, and the authentication result may be risky. It
         * is applicable to low-security scenarios such as service risk control, common personal data query, and access to
         * non-sensitive information. It is recommended that this level be used together with other security measures.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 8
         */
        ATL1 = 10000,
        /**
         * Authentication trust level 2. It can accurately identify individual users and provides standard liveness
         * detection capabilities (such as blinking and nodding detection). It features medium security strength and can
         * effectively defend against simple forgery attacks. It is applicable to medium-security scenarios such as
         * maintaining the screen-unlocked state of a device, application login, and confirmation of general sensitive
         * operations.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 8
         */
        ATL2 = 20000,
        /**
         * Authentication trust level 3. It can accurately identify individual users and provides strong liveness detection
         * capabilities (such as 3D face recognition and multi-frame analysis). It features high security strength and can
         * effectively defend against common forgery attacks such as photos and videos. It is applicable to high-security
         * scenarios such as device unlocking, confirmation of important sensitive operations, and enterprise-level
         * application login. 3D face recognition devices support this level.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 8
         */
        ATL3 = 30000,
        /**
         * Authentication trust level 4. It can accurately identify individual users and provides strong liveness detection
         * capabilities (such as in-depth analysis and multi-dimensional verification). It features the highest security
         * strength and can effectively defend against various advanced forgery attacks. It is applicable to high-security
         * scenarios, such as small-amount payment, financial transactions, and access to highly sensitive data. Only a few
         * high-security authentication solutions support this level.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 8
         */
        ATL4 = 40000
    }
    /**
     * Defines the keyword of the authentication event type. It is used as a parameter of
     * [on]{@link userAuth.AuthInstance.on}.
     *
     * It consists of the fields in **Type** in the following table.
     *
     * @unionmember { 'result' } If the first parameter of
     *     [on]{@link userAuth.AuthInstance.on} is **result**,
     *     the [callback]{@link userAuth.AuthEvent.callback } If the first parameter of
     *     [on]{@link userAuth.AuthInstance.on} is **result**, the [callback]{@link userAuth.AuthEvent.callback} returns
     *     the authentication result.
     * @unionmember { 'tip' } If the first parameter of
     *     [on]{@link userAuth.AuthInstance.on} is **tip**, the
     *     [callback]{@link userAuth.AuthEvent.callback } If the first parameter of [on]{@link userAuth.AuthInstance.on}
     *     is **tip**, the [callback]{@link userAuth.AuthEvent.callback} returns the authentication tip information.
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @since 9
     * @deprecated since 11
     */
    type AuthEventKey = 'result' | 'tip';
    /**
     * Enumerates the authentication event information types.
     *
     * It consists of the fields in **Type** in the following table.
     *
     * @unionmember { AuthResultInfo } Authentication result.
     * @unionmember { TipInfo } Authentication tip information.
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @since 9
     * @deprecated since 11
     * @useinstead userAuth.UserAuthResult
     */
    type EventInfo = AuthResultInfo | TipInfo;
    /**
     * Provides an asynchronous callback to return the authentication event information.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @since 9
     * @deprecated since 11
     * @useinstead userAuth.IAuthCallback
     */
    interface AuthEvent {
        /**
         * Called to return the authentication result or authentication tip information.
         *
         * @param { EventInfo } result - Authentication result or tip information.
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 9
         * @deprecated since 11
         * @useinstead userAuth.IAuthCallback.onResult(result: UserAuthResult)
         */
        callback(result: EventInfo): void;
    }
    /**
     * Represents the authentication result.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @since 9
     * @deprecated since 11
     * @useinstead userAuth.UserAuthResult
     */
    interface AuthResultInfo {
        /**
         * Authentication result.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 9
         * @deprecated since 11
         * @useinstead userAuth.UserAuthResult.result
         */
        result: number;
        /**
         * Token that has passed the user identity authentication.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 9
         * @deprecated since 11
         * @useinstead userAuth.UserAuthResult.token
         */
        token?: Uint8Array;
        /**
         * Number of remaining authentication attempts.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 9
         * @deprecated since 11
         * @useinstead userAuth.AuthLockState.remainingAuthAttempts
         */
        remainAttempts?: number;
        /**
         * Lock duration of the authentication operation, in ms.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 9
         * @deprecated since 11
         * @useinstead userAuth.AuthLockState.lockoutDuration
         */
        lockoutDuration?: number;
    }
    /**
     * Represents the tip information displayed during the authentication, which is used to provide feedback during the
     * authentication process.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @since 9
     * @deprecated since 11
     * @useinstead userAuth.AuthTipInfo
     */
    interface TipInfo {
        /**
         * ID of the module that sends the tip information.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 9
         * @deprecated since 11
         * @useinstead userAuth.AuthTipInfo.tipType
         */
        module: number;
        /**
         * Tip to be given during the authentication process.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 9
         * @deprecated since 11
         * @useinstead userAuth.AuthTipInfo.tipCode
         */
        tip: number;
    }
    /**
     * Implements user authentication.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @since 9
     * @deprecated since 10
     * @useinstead userAuth.UserAuthInstance
     */
    interface AuthInstance {
        /**
         * Subscribes to the user authentication events of the specified type.
         *
         * - **name**: indicates the authentication event type. The value **result** means that the callback returns the
         * authentication result, and the value **tip** means that the callback returns the authentication tip information.
         * For details, see [AuthEventKey]{@link userAuth.AuthEventKey}.
         * - **callback**: callback used to return the authentication result or tip information. For details, see
         * [AuthEvent]{@link userAuth.AuthEvent}.
         *
         * > **NOTE**
         * >
         * > Use the [AuthInstance]{@link userAuth.AuthInstance} instance obtained to call this API.
         *
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 12500002 - General operation error.
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 9
         * @deprecated since 10
         * @useinstead userAuth.UserAuthInstance.on
         */
        on: (name: AuthEventKey, callback: AuthEvent) => void;
        /**
         * Unsubscribes from the user authentication events of the specified type.
         *
         * - **name**: indicates the authentication event type. The value **result** means to unsubscribe from the
         * authentication result, and the value **tip** means to unsubscribe from the authentication tip information. For
         * details, see [AuthEventKey]{@link userAuth.AuthEventKey}.
         *
         * > **NOTE**
         * >
         * > The [AuthInstance]{@link userAuth.AuthInstance} instance used to invoke this API must be the one used to
         * > subscribe to the event.
         *
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 12500002 - General operation error.
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 9
         * @deprecated since 10
         * @useinstead userAuth.UserAuthInstance.off
         */
        off: (name: AuthEventKey) => void;
        /**
         * Starts authentication.
         *
         * > **NOTE**
         * >
         * > Use the [AuthInstance]{@link userAuth.AuthInstance} instance obtained to call this API.
         *
         * @permission ohos.permission.ACCESS_BIOMETRIC
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 12500001 - Authentication failed.
         * @throws { BusinessError } 12500002 - General operation error.
         * @throws { BusinessError } 12500003 - The operation is canceled.
         * @throws { BusinessError } 12500004 - The operation is time-out.
         * @throws { BusinessError } 12500005 - The authentication type is not supported.
         * @throws { BusinessError } 12500006 - The authentication trust level is not supported.
         * @throws { BusinessError } 12500007 - The authentication task is busy.
         * @throws { BusinessError } 12500009 - The authenticator is locked.
         * @throws { BusinessError } 12500010 - The type of credential has not been enrolled.
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 9
         * @deprecated since 10
         * @useinstead userAuth.UserAuthInstance.start
         */
        start: () => void;
        /**
         * Cancels this authentication.
         *
         * > **NOTE**
         * >
         * > Use the [AuthInstance]{@link userAuth.AuthInstance} instance obtained to call this API. The
         * > [AuthInstance]{@link userAuth.AuthInstance} instance must be the instance being authenticated.
         *
         * @permission ohos.permission.ACCESS_BIOMETRIC
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 12500002 - General operation error.
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @since 9
         * @deprecated since 10
         * @useinstead userAuth.UserAuthInstance.cancel
         */
        cancel: () => void;
    }
    /**
     * Checks whether the specified authentication capability is supported. This API is used to check whether the current
     * device supports the specified authentication type and authentication trust level. It helps an application determine
     * whether the authentication capability is available before initiating authentication, thereby avoiding unnecessary
     * authentication failures. If the query is successful (no error is thrown), the authentication capability is
     * available. If an error is thrown, the application should determine the cause based on the error code and take
     * appropriate measures.
     *
     * @permission ohos.permission.ACCESS_BIOMETRIC
     * @param { UserAuthType } authType - Authentication type. This parameter specifies the authentication type to be
     *     queried. The options are **FACE**, **FINGERPRINT**, **PIN**, and **COMPANION_DEVICE**.
     *     <br>Note:
     *     <br>PIN is supported since API version 11.
     *     <br>COMPANION_DEVICE query is supported since API version 26.0.0.
     * @param { AuthTrustLevel } authTrustLevel - Authentication trust level. This parameter specifies the authentication
     *     trust level to be queried. The valid values are **ATL1(10000)**, **ATL2(20000)**, **ATL3(30000)**, and
     *     **ATL4(40000)**. A higher level indicates a higher requirement on the liveness detection capability of the
     *     authentication solution.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified.
     * @throws { BusinessError } 12500002 - General operation error.
     * @throws { BusinessError } 12500005 - The authentication type is not supported.
     * @throws { BusinessError } 12500006 - The authentication trust level is not supported.
     * @throws { BusinessError } 12500010 - The type of credential has not been enrolled.
     * @throws { BusinessError } 12500013 - Operation failed because of PIN expired. [since 12]
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @atomicservice [since 12]
     * @since 9
     */
    function getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): void;
    /**
     * Represents the state of a credential enrolled. This API is used to describe the current state of enrolled
     * authentication credentials (such as face, fingerprint, and companion device), including the credential digest and
     * quantity. The application can call the [getEnrolledState]{@link userAuth.getEnrolledState} API to query the
     * credential status, and check whether the user's credentials have changed (for example, whether a fingerprint, face,
     * or companion device is added or deleted) to perform corresponding service processing.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @atomicservice
     * @since 12
     */
    interface EnrolledState {
        /**
         * Credential digest, which is randomly generated when a credential is added. This value is used to identify the
         * version of the currently registered credential. It changes when a credential is added or deleted. The application
         * can save this value and compare it with the value obtained in subsequent queries to determine whether the
         * credential has changed.
         *
         * **Note**: When the authentication result is reused, if the credential used for the previous authentication has
         * been deleted, the return value of **credentialDigest** may be **0**.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 12
         */
        credentialDigest: number;
        /**
         * Number of enrolled credentials. This parameter indicates the number of credentials of a specified type enrolled
         * by the current user, for example, the number of fingerprints or faces.
         *
         * **Note**: When an authentication result is reused, if the credential used for the previous authentication has
         * been deleted, the returned value of **credentialCount** may be **0**.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 12
         */
        credentialCount: number;
    }
    /**
     * Obtains the credential state. This API is used to obtain the credential enrollment information of a specified
     * authentication type, including the credential digest and quantity. The application can compare the current query
     * result with the previously saved result to determine whether the user has added or deleted credentials, and then
     * perform corresponding service processing.
     *
     * @permission ohos.permission.ACCESS_BIOMETRIC
     * @param { UserAuthType } authType - Authentication type. This parameter specifies the credential type to be queried.
     *     The options are **FACE**, **FINGERPRINT**, **PIN**, and **COMPANION_DEVICE**. When a PIN is queried, the
     *     overall status of the PIN instead of the number of PINs is returned.
     * @returns { EnrolledState } Credential state obtained if the operation is successful. The value contains
     *     **credentialDigest** (credential digest) and **credentialCount** (credential count). The application can save
     *     the **credentialDigest** value and compare it with the value obtained in subsequent queries to detect
     *     credential changes.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified.
     * @throws { BusinessError } 12500002 - General operation error.
     * @throws { BusinessError } 12500005 - The authentication type is not supported.
     * @throws { BusinessError } 12500010 - The type of credential has not been enrolled.
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @atomicservice
     * @since 12
     */
    function getEnrolledState(authType: UserAuthType): EnrolledState;
    /**
     * Enumerates the lockout status of an identity authentication type. This API is used to query the lockout status of a
     * specified authentication type (such as face, fingerprint, or PIN), including whether the authentication type is
     * locked out, the number of remaining attempts, and the lockout duration. If a user fails to be authenticated for
     * multiple times, the authenticator may enter a temporary or permanent lockout state. The application can notify the
     * user based on the lockout information.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @atomicservice
     * @since 22
     */
    interface AuthLockState {
        /**
         * Whether the authentication is locked. The value **true** indicates that the authentication type is locked and
         * cannot be used for authentication, and **false** indicates the opposite. The lockout status is usually triggered
         * by multiple consecutive authentication failures.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 22
         */
        isLocked: boolean;
        /**
         * Number of remaining attempts before the authentication is locked. The maximum value is **5**. The value decreases
         * by 1 each time the authentication fails. When the value decreases to 0, the authenticator is locked. This
         * parameter is valid only when **isLocked** is set to **false**.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 22
         */
        remainingAuthAttempts: number;
        /**
         * Remaining lockout duration, in milliseconds. This parameter is valid only when **isLocked** is set to **true**.
         *
         * If the authenticator is permanently locked, the value is
         * [PERMANENT_LOCKOUT_DURATION]{@link userAuth.PERMANENT_LOCKOUT_DURATION},
         * indicating that the authenticator has been permanently locked. The user needs to perform PIN authentication
         * before using the authentication type again. If the authenticator is temporarily locked, the value is the actual
         * remaining lockout duration. After the lockout period ends, the user can continue to attempt authentication.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 22
         */
        lockoutDuration: number;
    }
    /**
     * Queries the lockout state of the specified authentication type. This API uses a promise to return the result.
     *
     * @permission ohos.permission.ACCESS_BIOMETRIC
     * @param { UserAuthType } authType - Authentication type.
     * @returns { Promise<AuthLockState> } Promise used to return the result. An error is reported when the operation
     *     fails.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 12500002 - General operation error.
     * @throws { BusinessError } 12500005 - The authentication type is not supported.
     * @throws { BusinessError } 12500008 - The parameter is out of range.
     * @throws { BusinessError } 12500010 - The type of credential has not been enrolled.
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @atomicservice
     * @since 22
     */
    function getAuthLockState(authType: UserAuthType): Promise<AuthLockState>;
    /**
     * Obtains an **AuthInstance** instance for user authentication.
     *
     * > **NOTE**
     *
     * > An **AuthInstance** instance can be used for authentication only once.
     *
     * @param { Uint8Array } challenge - Challenge value. It cannot exceed 32 bytes and can be passed in Uint8Array([])
     *     format.
     * @param { UserAuthType } authType - Authentication type. Currently, **FACE** and **FINGERPRINT** are supported.
     * @param { AuthTrustLevel } authTrustLevel - Authentication trust level.
     * @returns { AuthInstance } **AuthInstance** instance obtained.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 12500002 - General operation error.
     * @throws { BusinessError } 12500005 - The authentication type is not supported.
     * @throws { BusinessError } 12500006 - The authentication trust level is not supported.
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @since 9
     * @deprecated since 10
     * @useinstead userAuth.getUserAuthInstance
     */
    function getAuthInstance(challenge: Uint8Array, authType: UserAuthType, authTrustLevel: AuthTrustLevel): AuthInstance;
    /**
     * Enumerates the modes for reusing authentication results. This enum defines four modes for reusing authentication
     * results and is used to control which authentication results can be reused under what conditions. The application
     * can select a proper reuse mode based on the service scenario to balance security and user experience.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @atomicservice
     * @since 12
     */
    enum ReuseMode {
        /**
         * The device unlock authentication result can be reused within the validity period if the authentication type
         * matches any of the authentication types specified for this authentication.
         *
         * For example, after a user uses face authentication to unlock device, the authentication result can be reused
         * within the validity period if the user initiates a service operation that requires face authentication. However,
         * if the user initiates a service operation that requires fingerprint authentication, the authentication result
         * cannot be reused.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 12
         */
        AUTH_TYPE_RELEVANT = 1,
        /**
         * The device unlock authentication result can be reused within the validity period regardless of the authentication
         * type.
         *
         * For example, after a user uses face authentication to unlock the device, the authentication result can be reused
         * within the validity period if the user initiates a service operation that requires fingerprint or PIN
         * authentication.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 12
         */
        AUTH_TYPE_IRRELEVANT = 2,
        /**
         * Any identity authentication result (including device unlock authentication result) can be reused within the
         * validity period if the authentication type matches any of the authentication types specified for this
         * authentication.
         *
         * For example, after a user uses face authentication to complete payment in an application, the authentication
         * result can be reused within the validity period if the user initiates an operation that requires face
         * authentication in another application. However, if the user initiates an operation that requires fingerprint
         * authentication, the authentication result cannot be reused.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 14
         */
        CALLER_IRRELEVANT_AUTH_TYPE_RELEVANT = 3,
        /**
         * Any identity authentication result (including device unlock authentication result) can be reused within the
         * validity period regardless of the authentication type.
         *
         * For example, after a user uses face authentication to complete an operation in an application, the authentication
         * result can be reused within the validity period if the user initiates an authentication operation of any type in
         * another application.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 14
         */
        CALLER_IRRELEVANT_AUTH_TYPE_IRRELEVANT = 4
    }
    /**
     * Represents information about the authentication result reuse. This API is used to configure parameters related to
     * authentication result reuse, including the reuse mode and validity period. By properly configuring authentication
     * result reuse, you can ensure security while avoid repeated authentication, improving user experience.
     *
     * > **NOTE**
     *
     * > If the credential changes within the reuse duration after a successful identity authentication (including device
     * > unlock authentication), the authentication result can still be reused and the actual **EnrolledState** is
     * > returned in the authentication result. When the authentication credential used in the previous authentication has
     * > been deleted when the authentication result is reused:
     * >
     * > - If the face or fingerprint credential is deleted, the authentication result can still be reused, but the values
     * > of **credentialCount** and **credentialDigest** in the returned **EnrolledState** are both **0**.
     * >
     * > - If the screen lock password is deleted, the reuse will fail.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @atomicservice
     * @since 12
     */
    interface ReuseUnlockResult {
        /**
         * Authentication result reuse mode. Select a proper reuse mode based on the security requirements of the service
         * scenario:
         *
         * - **AUTH_TYPE_RELEVANT(1)**: Only the device unlock result that matches the authentication type is reused,
         * providing the highest security.
         * - **AUTH_TYPE_IRRELEVANT(2)**: Any type of device unlock result is reused, which is applicable to medium-security
         * scenarios.
         * - **CALLER_IRRELEVANT_AUTH_TYPE_RELEVANT(3)**: Any authentication result that matches the authentication type is
         * reused, which is applicable to cross-application scenarios.
         * - **CALLER_IRRELEVANT_AUTH_TYPE_IRRELEVANT(4)**: Any authentication result is reused, which provides the lowest
         * security but the best user experience.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 12
         */
        reuseMode: ReuseMode;
        /**
         * Reuse duration of the authentication result, in milliseconds. The value must be greater than 0 and the maximum
         * value is
         * [MAX_ALLOWABLE_REUSE_DURATION]{@link userAuth.MAX_ALLOWABLE_REUSE_DURATION}
         * (300,000 milliseconds, that is, 5 minutes). You are advised to set a proper duration based on the service
         * scenario:
         *
         * - Advanced security scenarios (such as payment): A short duration (for example, 30 seconds to 1 minute) is
         * recommended.
         * - Medium security scenarios (such as application login): A medium duration (for example, 2 to 3 minutes) is
         * recommended.
         * - Low security scenarios (such as data query): The maximum duration can be used.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 12
         */
        reuseDuration: number;
    }
    /**
     * Defines the user authentication parameters. This API is used to configure user authentication parameters, including
     * the challenge value, authentication type list, authentication trust level, and authentication result reuse
     * configuration. By properly configuring these parameters, you can meet authentication requirements in different
     * service scenarios.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @atomicservice [since 12]
     * @since 10
     */
    interface AuthParam {
        /**
         * Random challenge value, which can be used to prevent replay attacks. It cannot exceed 32 bytes and can be passed
         * in **Uint8Array([])** format. You are advised to use the random number generated by the
         * [crypto framework]{@link @ohos.security.cryptoFramework:cryptoFramework} as the challenge value to enhance
         * security. After the authentication is successful, the challenge value is included in the authentication token.
         * The service can verify the validity of the authentication result based on the challenge value in the
         * authentication token.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 10
         */
        challenge: Uint8Array;
        /**
         * Authentication type list, which specifies the types of authentication provided on the user authentication page.
         * Multiple authentication types can be specified at the same time, for example, **UserAuthType.PIN**,
         * **UserAuthType.FACE**, and **UserAuthType.FINGERPRINT**. Users can select any authentication type. The selection
         * of authentication types affects the matching conditions for authentication result reuse. Currently, companion
         * device authentication and other authentication types cannot be initiated at the same time.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 10
         */
        authType: UserAuthType[];
        /**
         * Authentication trust level. The authentication trust level determines the security strength of authentication.
         * Select a proper level based on the security requirements of the service scenario:
         *
         * - **ATL1**: Applies to low-security scenarios such as service risk control and common personal data query.
         * - **ATL2**: Applies to medium-security scenarios such as application login and maintaining the screen-unlocked
         * state of a device.
         * - **ATL3**: Applies to high-security scenarios such as device unlocking.
         * - **ATL4**: Applies to high-security scenarios such as small-amount payment.
         *
         * For details, see
         * [Principles for Classifying Biometric Authentication Trust Levels](docroot://security/UserAuthenticationKit/user-authentication-overview.md#principles-for-classifying-biometric-authentication-trust-levels).
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 10
         */
        authTrustLevel: AuthTrustLevel;
        /**
         * Information about the authentication result reuse. After this parameter is set, if the reuse conditions are met,
         * the system directly returns the previous authentication result, and the user does not need to perform
         * authentication interaction again. By default, the result cannot be reused. Enabling authentication result reuse
         * can improve user experience. However, you should properly configure the reuse mode and validity period based on
         * the security requirements of the service scenario.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 12
         */
        reuseUnlockResult?: ReuseUnlockResult;
        /**
         * Whether to skip the authentication mode that has been locked and automatically switch to another authentication
         * mode. If no authentication mode can be switched to, the component is disabled and an authentication freezing
         * error code is returned.
         *
         * - **true**: When biometric authentication is locked, the system skips the countdown screen and directly switches
         * to another authentication type (for example, from the locked fingerprint to the PIN). This is applicable
         * to scenarios where quick authentication is required.
         * - **false** (default): The system does not skip the countdown screen. The user needs to wait until the countdown
         * ends before attempting the authentication method again or manually switching to another method.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 20
         */
        skipLockedBiometricAuth?: boolean;
    }
    /**
     * Represents the information presented on the user authentication page. This API is used to configure the display
     * style and interaction mode of the authentication screen, including the title, navigation button text, and window
     * mode. By properly setting these parameters, you can provide clear authentication guidance and good interaction
     * experience for users.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @atomicservice [since 12]
     * @since 10
     */
    interface WidgetParam {
        /**
         * Title of the user authentication page, which cannot be empty or exceed 500 characters. You are advised to set it
         * to the authentication purpose, such as payment or application login. The title is displayed on the authentication
         * screen to help users understand the purpose of the current authentication, improving user trust and cooperation.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 10
         */
        title: string;
        /**
         * Text on the navigation button. It cannot exceed 60 characters. Tapping this button triggers a custom application
         * operation, such as jumping to the custom authentication page or canceling authentication. It is supported in
         * single fingerprint or face authentication before API version 18. Since API version 18, it is also supported in
         * combined face and fingerprint authentication. By default, the custom navigation button is not displayed.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 10
         */
        navigationButtonText?: string;
        /**
         * Used to display an application modal dialog for authentication. This parameter can be used only on 2-in-1
         * devices. After a valid uiContext is passed, the authentication dialog box is displayed as an application modal
         * dialog. After the authentication result is returned, the application needs to obtain the widget release message (
         * subscribe to [on('authTip')]{@link userAuth.UserAuthInstance.on(type: 'authTip', callback: AuthTipCallback)} and
         * wait for the **WIDGET_RELEASED** state) before displaying other windows. If this parameter is not specified or
         * the device is of another type, the authentication dialog box is displayed as a system modal dialog. In this case,
         * the application can directly perform the follow-up procedure after the widget is released.
         *
         * **Default value**: The authentication dialog box is displayed as a system modal dialog.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 18
         */
        uiContext?: Context;
    }
    /**
     * Represents the user authentication result. If the authentication is successful, the authentication type and token
     * information are returned. If the authentication fails, the corresponding error code is returned. This API is used
     * to describe the result information after the authentication is complete. The application can obtain the result
     * through the **onResult** callback of [IAuthCallback]{@link userAuth.IAuthCallback}.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @atomicservice [since 12]
     * @since 10
     */
    interface UserAuthResult {
        /**
         * User authentication result. If the operation is successful, **SUCCESS(12500000)** is returned. If the operation
         * fails, the corresponding error code is returned. The error codes are as follows:
         *
         * - **FAIL(12500001)**: The authentication fails.
         * - **CANCELED(12500003)**: The authentication is canceled.
         * - **TIMEOUT(12500004)**: The authentication times out.
         * - **LOCKED(12500009)**: The authenticator is locked.
         * - **NOT_ENROLLED(12500010)**: The credential is not registered.
         * - **PIN_EXPIRED(12500013)**: The screen lock PIN has expired.
         *
         * For details about the complete error code list, see [UserAuthResultCode]{@link userAuth.UserAuthResultCode}.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 10
         */
        result: number;
        /**
         * Token information returned when the authentication is successful. The token contains the credentials for user
         * authentication and can be used for subsequent security operation verification (such as payment confirmation and
         * sensitive data access). The maximum length of a token is 1024 bytes. The token contains the challenge value used
         * during authentication. The service can verify the challenge value to prevent replay attacks.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 10
         */
        token?: Uint8Array;
        /**
         * Authentication type that is actually used when the authentication is successful. If multiple authentication types
         * are specified in the **authType** field of [AuthParam]{@link userAuth.AuthParam}, this field identifies the
         * authentication type that the user selects and completes.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 10
         */
        authType?: UserAuthType;
        /**
         * Enrolled credential status returned when the authentication is successful. It contains the digest and quantity of
         * the current authentication types. The application can compare this value with the previously saved value to
         * determine whether the user credential has changed. If authentication result reuse is enabled and the credential (
         * face or fingerprint) used for the previous authentication has been deleted, the values of **credentialCount** and
         * **credentialDigest** in the returned **enrolledState** are both **0**.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 12
         */
        enrolledState?: EnrolledState;
    }
    /**
     * Provides callbacks to return the authentication result. This API defines the authentication result callback method,
     * which is used to obtain the authentication result after the authentication is complete. By implementing the
     * **onResult** method, the application can obtain the authentication token when the authentication is successful, or
     * obtain the error code and related information when the authentication fails.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @atomicservice [since 12]
     * @since 10
     */
    interface IAuthCallback {
        /**
         * Called to return the authentication result. If the authentication is successful, you can obtain the token
         * information through **UserAuthResult** for subsequent security operation verification. If the authentication
         * fails, you can obtain the error code through the **result** field and take corresponding measures (for example,
         * prompting the user to perform authentication again or guiding the user to register a credential).
         *
         * @param { UserAuthResult } result - Authentication result. It contains information such as the authentication
         *     result code, authentication token (when the authentication is successful), authentication type, and
         *     credential status. The application needs to check the **result.result** field to determine whether the
         *     authentication is successful.
         *     <br>- If the value of **result.result** is **SUCCESS(12500000)**, the authentication is successful. In this
         *     case, you can use **result.token** to perform the subsequent operations.
         *     <br>- If the value of **result.result** is another value, the authentication fails. In this case, you need to
         *     handle the error based on the specific error code.
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 10
         */
        onResult(result: UserAuthResult): void;
    }
    /**
     * Enumerates the intermediate states of identity authentication. This enum is used to describe various intermediate
     * states during authentication, including authentication failure, timeout, lockout, and loading and release of the
     * authentication screen. Applications can subscribe to these intermediate states through the
     * [on('authTip')]{@link userAuth.UserAuthInstance.on(type: 'authTip', callback: AuthTipCallback)} API to provide more
     * refined user feedback and status awareness during authentication.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @atomicservice
     * @since 20
     */
    enum UserAuthTipCode {
        /**
         * The authentication fails. This state occurs because the user's biometric features do not match the registered
         * credential. It is triggered each time the authentication fails. Your application can prompt the user to try again
         * based on this state.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 20
         */
        COMPARE_FAILURE = 1,
        /**
         * The authentication has timed out. This state usually occurs because the user has not completed the authentication
         * interaction within the specified time (for example, the user has not entered the password in time or has not
         * looked straight at the camera lens).
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 20
         */
        TIMEOUT = 2,
        /**
         * The authentication is temporarily locked. When this state occurs, users can attempt to perform authentication
         * only after the lockout duration expires. The temporary lockout status is usually triggered by multiple
         * consecutive authentication failures.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 20
         */
        TEMPORARILY_LOCKED = 3,
        /**
         * The authentication is permanently locked. When this state occurs, automatic unlocking is unavailable. Users must
         * use PIN authentication to unlock the authenticator before using the authentication type. The permanent lockout
         * status is usually triggered by failed authentication attempts during the temporary lockout period.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 20
         */
        PERMANENTLY_LOCKED = 4,
        /**
         * The identity authentication page is loaded. This state indicates that the authentication widget is successfully
         * loaded and displayed, and the user can start authentication interaction. The application can perform UI-related
         * initialization operations after this state is triggered.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 20
         */
        WIDGET_LOADED = 5,
        /**
         * The current identity authentication page is switched to another authentication page or the identity
         * authentication component is closed. This state indicates that the authentication widget has been released. The
         * application can perform follow-up operations, such as displaying another window, after this state is triggered.
         * When using the application modal dialog for authentication on a PC/2-in-1 device, you are advised to subscribe to
         * this status to ensure that the widget is completely released before performing other operations.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 20
         */
        WIDGET_RELEASED = 6,
        /**
         * The authentication fails and authentication freezing is triggered. This state indicates that the number of
         * authentication failures reaches the threshold and the authenticator is locked. This state contains both
         * authentication failure and freezing information. Your application can prompt the user with the corresponding
         * unlock method based on the lockout type (temporary or permanent).
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 20
         */
        COMPARE_FAILURE_WITH_FROZEN = 7
    }
    /**
     * Represents the intermediate authentication status. This API is used to describe various intermediate states
     * generated during authentication, including the authentication type and specific status code corresponding to each
     * state. The application can obtain these intermediate states through
     * [AuthTipCallback]{@link userAuth.AuthTipCallback} to provide more refined user feedback and status awareness during
     * authentication.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @atomicservice
     * @since 20
     */
    interface AuthTipInfo {
        /**
         * Authentication type of the intermediate status. It indicates the authentication type that generates the current
         * intermediate state, such as face authentication (**FACE**), fingerprint authentication (**FINGERPRINT**), or PIN
         * authentication (**PIN**). The application can provide specific prompts for the user based on the authentication
         * type.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 20
         */
        tipType: UserAuthType;
        /**
         * Intermediate status. It indicates the specific intermediate status type, such as authentication failure, timeout,
         * lockout, and UI loading/release. The application should provide feedback or execute the corresponding processing
         * logic based on the value of **tipCode**.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 20
         */
        tipCode: UserAuthTipCode;
    }
    /**
     * Defines the callback to return the intermediate authentication status. This callback is used to obtain various
     * intermediate status information during authentication, including authentication failure, lockout, and loading and
     * release of the authentication screen. By subscribing to these intermediate statuses, the application can provide
     * more refined user interaction and status management during the authentication process.
     *
     * @param { AuthTipInfo } authTipInfo - Intermediate authentication status. It contains the authentication type (
     *     **tipType**) and status code (**tipCode**). The application should perform the corresponding processing based
     *     on the value of **tipCode**:
     *     <br>- **COMPARE_FAILURE(1)**: Prompt the user to try again.
     *     <br>- **TIMEOUT(2)**: Prompt the user that the operation has timed out.
     *     <br>- **TEMPORARILY_LOCKED(3)**: Prompt the user to wait for unlocking.
     *     <br>- **PERMANENTLY_LOCKED(4)**: Prompt the user to use PIN authentication.
     *     <br>- **WIDGET_LOADED(5)**: The authentication screen has been loaded and initialization can be performed.
     *     <br>- **WIDGET_RELEASED(6)**: The authentication screen has been released, and the subsequent operations can be
     *     performed.
     *     <br>- **COMPARE_FAILURE_WITH_FROZEN(7)**: Prompt the user that the authentication fails and the authenticator
     *     is locked.
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @atomicservice
     * @since 20
     */
    type AuthTipCallback = (authTipInfo: AuthTipInfo) => void;
    /**
     * Provides APIs for user authentication. The user authentication widget is supported. This API provides complete user
     * authentication capabilities, including subscribing to authentication results and intermediate states, and starting
     * and canceling authentication. The unified authentication widget provides users with a standardized authentication
     * UI and consistent authentication experience.
     *
     * Before using the APIs of **UserAuthInstance**, you must obtain a **UserAuthInstance** instance by using
     * [getUserAuthInstance]{@link userAuth.getUserAuthInstance}.
     *
     * > **NOTE**
     *
     * > Each **UserAuthInstance** can be used for only one authentication process. To perform authentication again, you
     * > must obtain a new **UserAuthInstance** instance.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @atomicservice [since 12]
     * @since 10
     */
    interface UserAuthInstance {
        /**
         * Subscribes to the user authentication result. This API is used to obtain the final identity authentication result
         * after the user completes identity authentication interaction with the authentication component. Before the
         * authentication widget disappears, the intermediate authentication failures will not be returned through this API.
         * Only the final authentication result (success or failure) is returned through this API. To perceive each
         * authentication failure and intermediate status during the entire authentication process, use the
         * [on('authTip')]{@link userAuth.UserAuthInstance.on(type: 'authTip', callback: AuthTipCallback)} API for
         * subscription.
         *
         * > **NOTE**
         *
         * > On PCs/2-in-1 devices, if an application initiates authentication in an application modal dialog (that is, a
         * > valid **uiContext** is passed when the user API parameter [widgetParam]{@link userAuth.WidgetParam} is
         * > configured) and receives the authentication result, and if other windows need to be displayed, the application
         * > needs to obtain the flag message released by the component pop-up window and subscribe to the component release
         * > message (**authTipInfo.tipCode = UserAuthTipCode.WIDGET_RELEASED**) through the
         * > [on('authTip')]{@link userAuth.UserAuthInstance.on(type: 'authTip', callback: AuthTipCallback)} API.
         *
         * @param { 'result' } type - Event type. The value is **result**, which indicates the authentication result.
         * @param { IAuthCallback } callback - Callback used to return the user authentication result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 12500002 - General operation error.
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'result', callback: IAuthCallback): void;
        /**
         * Unsubscribes from the user authentication result.
         *
         * > **NOTE**
         *
         * > The [UserAuthInstance]{@link userAuth.UserAuthInstance} instance used to invoke this API must be the one used
         * > to subscribe to the event.
         *
         * @param { 'result' } type - Event type. The value is **result**, which indicates the authentication result.
         * @param { IAuthCallback } [callback] - Callback used to return the user authentication result. If this parameter is
         *     not passed, the value passed when the
         *     [on('result')]{@link userAuth.UserAuthInstance.on(type: 'result', callback: IAuthCallback)} API is called is
         *     used by default.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 12500002 - General operation error.
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'result', callback?: IAuthCallback): void;
        /**
         * Starts authentication.
         *
         * > **NOTE**
         *
         * > Each **UserAuthInstance** can be used for authentication only once.
         *
         * @permission ohos.permission.ACCESS_BIOMETRIC [since 10 - 19]
         * @permission ohos.permission.ACCESS_BIOMETRIC or ohos.permission.USER_AUTH_FROM_BACKGROUND [since 20]
         * @throws { BusinessError } 201 - Permission denied. Possible causes:
         *     <br>1. No permission to access biometric.
         *     <br>2. No permission to start authentication from background.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Incorrect parameter types.
         * @throws { BusinessError } 12500001 - Authentication failed. [since 10 - 19]
         * @throws { BusinessError } 12500002 - General operation error.
         * @throws { BusinessError } 12500003 - Authentication canceled.
         * @throws { BusinessError } 12500004 - Authentication timeout. [since 10 - 19]
         * @throws { BusinessError } 12500005 - The authentication type is not supported.
         * @throws { BusinessError } 12500006 - The authentication trust level is not supported.
         * @throws { BusinessError } 12500007 - Authentication service is busy. [since 10 - 19]
         * @throws { BusinessError } 12500009 - Authentication is locked out.
         * @throws { BusinessError } 12500010 - The type of credential has not been enrolled.
         * @throws { BusinessError } 12500011 - Switched to the customized authentication process.
         * @throws { BusinessError } 12500013 - Operation failed because of PIN expired. [since 12]
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 10
         */
        start(): void;
        /**
         * Cancels this authentication.
         *
         * > **NOTE**
         *
         * > **UserAuthInstance** must be the instance being authenticated.
         *
         * @permission ohos.permission.ACCESS_BIOMETRIC
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Incorrect parameter types.
         * @throws { BusinessError } 12500002 - General operation error.
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 10
         */
        cancel(): void;
        /**
         * Subscribes to authentication tip information. This API is used to obtain the widget startup and exit messages and
         * each authentication failure. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         *
         * > On PCs/2-in-1 devices, if an application initiates authentication in an application modal dialog (that is, a
         * > valid **uiContext** is passed when the user API parameter [widgetParam]{@link userAuth.WidgetParam} is
         * > configured) and receives the authentication result, and if other windows need to be displayed, the application
         * > needs to obtain the flag message released by the component pop-up window and subscribe to the component release
         * > message (**authTipInfo.tipCode = UserAuthTipCode.WIDGET_RELEASED**) through the
         * > [on('authTip')]{@link userAuth.UserAuthInstance.on(type: 'authTip', callback: AuthTipCallback)} API.
         *
         * @param { 'authTip' } type - Event type. The supported event is **'authTip'**. This event is triggered when
         *     [start()]{@link userAuth.UserAuthInstance.start} is called and authentication is initiated.
         * @param { AuthTipCallback } callback - Callback used to return the intermediate authentication status.
         * @throws { BusinessError } 12500002 - General operation error.
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 20
         */
        on(type: 'authTip', callback: AuthTipCallback): void;
        /**
         * Unsubscribes from the event for intermediate authentication status.
         *
         * > **NOTE**
         *
         * > The [UserAuthInstance]{@link userAuth.UserAuthInstance} instance used to invoke this API must be the one used
         * > to subscribe to the event.
         *
         * @param { 'authTip' } type - Event type. The supported event is **'authTip'**. This API unsubscribes from the
         *     event triggered by [on('authtip')]{@link userAuth.UserAuthInstance.on_authTip} after the
         *     [start()]{@link userAuth.UserAuthInstance.start} call and the initiation of authentication.
         * @param { AuthTipCallback } [callback] - Callback used to return the intermediate authentication status. If this
         *     parameter is not passed, the value passed when the
         *     [on('authtip')]{@link userAuth.UserAuthInstance.on_authTip} API is called is used by default.
         * @throws { BusinessError } 12500002 - General operation error.
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 20
         */
        off(type: 'authTip', callback?: AuthTipCallback): void;
    }
    /**
     * Obtains a [UserAuthInstance]{@link userAuth.UserAuthInstance} instance for user authentication. The user
     * authentication widget is also supported. This API is used to create a user authentication instance. After
     * authentication parameters and UI parameters are configured, you can use the returned instance object to start
     * authentication and subscribe to the authentication result.
     *
     * > **NOTE**
     *
     * > Each **UserAuthInstance** can be used for authentication only once. After the authentication is complete (
     * > regardless of whether it is successful or fails), the instance cannot be used again.
     *
     * @param { AuthParam } authParam - User authentication parameters. The parameters include the challenge value,
     *     authentication type list, authentication trust level, and authentication result reuse configuration. It is
     *     recommended that the challenge value be a random number generated by the crypto framework. Multiple
     *     authentication types can be specified for users to choose from. The authentication trust level should be
     *     selected based on the security requirements of the service scenario.
     * @param { WidgetParam } widgetParam - Parameters on the user authentication page. The parameters include the page
     *     title, navigation button text, window mode (for system API), and application modal dialog context. It is
     *     recommended that the title be set to the authentication purpose, and the navigation button text be used for
     *     custom authentication redirection.
     * @returns { UserAuthInstance } **UserAuthInstance** instance that supports UI. After obtaining the instance, call
     *     [on('result')]{@link userAuth.UserAuthInstance.on(type: 'result', callback: IAuthCallback)} to subscribe to the
     *     authentication result, and then call [start]{@link userAuth.UserAuthInstance.start} to start authentication.
     *     After the authentication is complete, you can obtain the authentication result through a callback.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified.
     *     <br>2. Incorrect parameter types.
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 12500002 - General operation error.
     * @throws { BusinessError } 12500005 - The authentication type is not supported.
     * @throws { BusinessError } 12500006 - The authentication trust level is not supported.
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @atomicservice [since 12]
     * @since 10
     */
    function getUserAuthInstance(authParam: AuthParam, widgetParam: WidgetParam): UserAuthInstance;
    /**
     * Enumerates the authentication result codes. They include all success codes and error codes for user authentication
     * operations. The application can determine the authentication result based on the return code and take corresponding
     * measures.
     *
     * @syscap SystemCapability.UserIAM.UserAuth.Core
     * @atomicservice [since 12]
     * @since 9
     */
    enum UserAuthResultCode {
        /**
         * The operation is successful. It indicates that the user authentication is successful and the authentication token
         * is valid. The application can use the returned token to perform subsequent security operations.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 9
         */
        SUCCESS = 12500000,
        /**
         * The authentication fails. It indicates that the user characteristics do not match the enrolled credentials. The
         * possible cause is that the user input is incorrect or an unenrolled credential is used. It is recommended that
         * the user be prompted to try again.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 9
         */
        FAIL = 12500001,
        /**
         * A general operation error occurred. It indicates that an unknown error occurs during authentication. It is
         * recommended that the user be prompted to try again later or contact the system administrator.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 9
         */
        GENERAL_ERROR = 12500002,
        /**
         * The authentication is canceled. It indicates that the user or the system cancels the authentication. The
         * application can determine whether to initiate the authentication again based on the service logic.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 9
         */
        CANCELED = 12500003,
        /**
         * The authentication has timed out. It indicates that the user does not complete the authentication interaction
         * within the specified time (for example, the user does not enter the password in time or does not look at the
         * camera). You are advised to prompt the user to try again and pay attention to the operation time limit.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 9
         */
        TIMEOUT = 12500004,
        /**
         * The authentication type is not supported. It indicates that the current device does not support the specified
         * authentication type. For example, the device does not have a fingerprint sensor but the fingerprint
         * authentication is requested. You are advised to check the device capability or change the authentication type.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 9
         */
        TYPE_NOT_SUPPORT = 12500005,
        /**
         * The authentication trust level is not supported. It indicates that the specified authentication trust level is
         * higher than the highest level supported by the current authentication type. You are advised to lower the
         * authentication trust level or use a more secure authentication type.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 9
         */
        TRUST_LEVEL_NOT_SUPPORT = 12500006,
        /**
         * The system does not respond. It indicates that the authentication service is busy processing other requests. You
         * are advised to try again later.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 9
         */
        BUSY = 12500007,
        /**
         * Parameter verification failed. It indicates that the input parameter does not meet the requirements, for example,
         * the parameter type is incorrect or the parameter value is out of range. You are advised to check the parameter
         * and call the API again.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 20
         */
        INVALID_PARAMETERS = 12500008,
        /**
         * The authentication executor is locked. It indicates that the authenticator is locked due to consecutive
         * authentication failures. The user can continue the authentication only after waiting for unlocking or using the
         * PIN. You can call [getAuthLockState]{@link userAuth.getAuthLockState} to query the lock status.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 9
         */
        LOCKED = 12500009,
        /**
         * The user has not enrolled the specified system identity authentication credential. It indicates that the user has
         * not enrolled the requested authentication type. For example, the fingerprint authentication is requested but the
         * user has not enrolled the fingerprint. You are advised to guide the user to register the corresponding credential
         * first.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 9
         */
        NOT_ENROLLED = 12500010,
        /**
         * The user cancels the system authentication and selects a custom authentication of the application. It indicates
         * that the user taps the navigation button on the authentication screen and chooses to use the custom
         * authentication type provided by the application. The application needs to launch the custom authentication page.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice [since 12]
         * @since 10
         */
        CANCELED_FROM_WIDGET = 12500011,
        /**
         * The PIN has expired. It indicates that the system PIN has expired. For example, the enterprise policy requires
         * that the PIN be changed periodically. In this case, the user needs to change the PIN before using the
         * authentication function.
         *
         * @syscap SystemCapability.UserIAM.UserAuth.Core
         * @atomicservice
         * @since 12
         */
        PIN_EXPIRED = 12500013
    }
}
export default userAuth;

```
