# @ohos.enterprise.telephonyManager.d.ts

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
 * @file Telephony Management
 * @kit MDMKit
 */
import type Want from './@ohos.app.ability.Want';
import adminManager from './@ohos.enterprise.adminManager';
/**
 * The **telephonyManager** module provides the telephony management capability.
 *
 * > **NOTE**
 * >
 * > The APIs of this module can be called only by a device administrator application that is enabled. For details, see
 * > [MDM Kit Development](docroot://mdm/mdm-kit-guide.md).
 * >
 * > The global restriction policy is provided by **restrictions**. To disable telephony globally, see
 * > [@ohos.enterprise.restrictions (Restrictions)]{@link @ohos.enterprise.restrictions:restrictions}.
 *
 * @syscap SystemCapability.Customization.EnterpriseDeviceManager
 * @stagemodelonly
 * @since 20
 */
declare namespace telephonyManager {
    /**
     * Disables the SIM card in the specified slot. After being disabled, the SIM card in the specified slot cannot be
     * used for making or receiving calls, sending or receiving SMSs, or accessing the internet. For example, an
     * enterprise device administrator can disable the SIM card when an employee leaves the company or a device is lost,
     * preventing unauthorized use. This is applicable in scenarios where enterprises need to restrict employee devices'
     * communication capabilities, such as preventing SIM card misuse after employee departure or device loss, thereby
     * ensuring enterprise communication security and cost control.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_TELEPHONY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { number } slotId - Slot ID. Currently, only single-slot and dual-slot devices are supported. The value can
     *     be **0** or **1**, where **0** indicates slot 1 and **1** indicates slot 2.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function setSimDisabled(admin: Want, slotId: number): void;
    /**
     * Enables the SIM card in a specified slot. After it has been disabled with **setSimDisabled**, the card must be
     * turned back on manually in **Settings** > **Mobile network** > **SIM management**, as this **setSimEnabled** API
     * cannot re-enable it directly.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_TELEPHONY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { number } slotId - Slot ID. Currently, only single-slot and dual-slot devices are supported. The value can
     *     be **0** or **1**, where **0** indicates slot 1 and **1** indicates slot 2.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function setSimEnabled(admin: Want, slotId: number): void;
    /**
     * Checks whether the SIM card in a specified slot is disabled. This API is applicable in scenarios where enterprise
     * administrators need to check whether the SIM card disablement policy has taken effect. It helps administrators
     * confirm the policy enforcement status and ensure that call control policies are correctly implemented.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_TELEPHONY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { number } slotId - Slot ID. Currently, only single-slot and dual-slot devices are supported. The value can
     *     be **0** or **1**, where **0** indicates slot 1 and **1** indicates slot 2.
     * @returns { boolean } A Boolean value indicating the SIM card status in the specified slot. The value **true** means
     *     the SIM card in the specified slot is disabled; the value **false** means the opposite.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function isSimDisabled(admin: Want, slotId: number): boolean;
    /**
     * Adds the trustlist or blocklist for outgoing calls. If no list is set, all numbers can make outgoing calls. Once a
     * list is added, only numbers on the list are allowed (or blocked) from making outgoing calls. For example, an
     * enterprise can restrict employees to calling only customer service hotlines, or prohibit them from calling specific
     * numbers.
     *
     * A policy conflict is reported when this API is called in the following scenarios:
     *
     * 1. The device's call capability has been disabled via [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy},
     * using this API to add an outgoing call trustlist or blocklist will return error code 203. To resolve the conflict,
     * enable the call capability via [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy}.
     * 2. If an outgoing call blocklist has been set via this API, using this API again to add an outgoing call trustlist
     * will return error code 9200010. To resolve the conflict, remove the previously set blocklist via the [removeOutgoingCallPolicyNumbers]{@link telephonyManager.removeOutgoingCallPolicyNumbers} API.
     * 3. If an outgoing call trustlist has been set via this API, using this API again to add an outgoing call blocklist
     * will return error code 9200010. To resolve the conflict, remove the previously set trustlist via the [removeOutgoingCallPolicyNumbers]{@link telephonyManager.removeOutgoingCallPolicyNumbers} API.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_TELEPHONY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { adminManager.Policy } policy - Policy for trustlist or blocklist. **BLOCK_LIST** indicates a blocklist,
     *     and **TRUST_LIST** indicates a trustlist.
     * @param { Array<string> } numbers - List of phone numbers. Currently, only full number matching is supported. The
     *     total length of the array must not exceed 1,000. For example, if there are already 100 numbers in the current
     *     trustlist array, this API supports adding up to 900 more numbers.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200010 - A conflict policy has been configured.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 203 - This function is prohibited by enterprise management policies.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
     *     capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function addOutgoingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void;
    /**
     * Removes the trustlist or blocklist for outgoing calls. If the list is not set, the removal fails. For example, an
     * enterprise can use this API when removing call restrictions and restoring normal call permissions for employees.
     *
     * A policy conflict is reported when this API is called in the following scenario:
     *
     * If the device's call capability has been disabled via the
     * [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy} API, using this API to
     * remove an outgoing call trustlist or blocklist will return error code 203. To resolve the conflict, enable the call
     * capability via [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy}.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_TELEPHONY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { adminManager.Policy } policy - Policy for trustlist or blocklist. **BLOCK_LIST** indicates a blocklist,
     *     and **TRUST_LIST** indicates a trustlist.
     * @param { Array<string> } numbers - List of call numbers to remove. The total length of the array must not exceed 1,
     *     000.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 203 - This function is prohibited by enterprise management policies.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
     *     capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function removeOutgoingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void;
    /**
     * Obtains the trustlist or blocklist for outgoing calls.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_TELEPHONY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { adminManager.Policy } policy - Policy for trustlist or blocklist. **BLOCK_LIST** indicates a blocklist,
     *     and **TRUST_LIST** indicates a trustlist.
     * @returns { Array<string> } An array of numbers in the outgoing call blocklist or trustlist.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
     *     capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function getOutgoingCallPolicyNumbers(admin: Want, policy: adminManager.Policy): Array<string>;
    /**
     * Obtains the trustlist or blocklist for outgoing calls.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_TELEPHONY
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @param { adminManager.Policy } policy - Policy for trustlist or blocklist. **BLOCK_LIST** indicates a blocklist,
     *     and **TRUST_LIST** indicates a trustlist.
     * @returns { Array<string> } An array of numbers in the outgoing call blocklist or trustlist.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
     *     capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getOutgoingCallPolicyNumbers(admin: Want | null, policy: adminManager.Policy): Array<string>;
    /**
     * Adds the trustlist or blocklist for incoming calls. If no list is set, all numbers can make incoming calls. Once a
     * list is added, only numbers on the list are allowed (or blocked) from making incoming calls. For example, an
     * enterprise can restrict employees to answering only calls from customers, or prohibit them from answering
     * harassment calls.
     *
     * A policy conflict is reported when this API is called in the following scenarios:
     *
     * 1. The device's call capability has been disabled via [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy},
     * using this API to add an incoming call trustlist or blocklist will return error code 203. To resolve the conflict,
     * enable the call capability via [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy}.
     * 2. If an incoming call blocklist has been set via this API, using this API again to add an incoming call trustlist
     * will return error code 9200010. To resolve the conflict, remove the previously set blocklist via the [removeIncomingCallPolicyNumbers]{@link telephonyManager.removeIncomingCallPolicyNumbers} API.
     * 3. If an incoming call trustlist has been set via this API, using this API again to add an incoming call blocklist
     * will return error code 9200010. To resolve the conflict, remove the previously set trustlist via the [removeIncomingCallPolicyNumbers]{@link telephonyManager.removeIncomingCallPolicyNumbers} API.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_TELEPHONY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { adminManager.Policy } policy - Policy for trustlist or blocklist. **BLOCK_LIST** indicates a blocklist,
     *     and **TRUST_LIST** indicates a trustlist.
     * @param { Array<string> } numbers - List of phone numbers. Currently, only full number matching is supported. The
     *     total length of the array must not exceed 1,000. For example, if there are already 100 numbers in the current
     *     trustlist array, this API supports adding up to 900 more numbers.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200010 - A conflict policy has been configured.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 203 - This function is prohibited by enterprise management policies.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
     *     capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function addIncomingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void;
    /**
     * Removes the trustlist or blocklist for incoming calls. If the list is not set, the removal fails. For example, an
     * enterprise can use this API when lifting incoming call restrictions and restoring employees' normal answering
     * permissions.
     *
     * A policy conflict is reported when this API is called in the following scenario:
     *
     * 1. If the device's call capability has been disabled via the [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy}
     * API, using this API to remove an incoming call trustlist or blocklist will return error code 203. To resolve the
     * conflict, enable the call capability via [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy}.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_TELEPHONY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { adminManager.Policy } policy - Policy for trustlist or blocklist. **BLOCK_LIST** indicates a blocklist,
     *     and **TRUST_LIST** indicates a trustlist.
     * @param { Array<string> } numbers - List of call numbers to remove. The total length of the array must not exceed 1,
     *     000.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 203 - This function is prohibited by enterprise management policies.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
     *     capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function removeIncomingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void;
    /**
     * Obtains the trustlist or blocklist for incoming calls.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_TELEPHONY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { adminManager.Policy } policy - Policy for trustlist or blocklist. **BLOCK_LIST** indicates a blocklist,
     *     and **TRUST_LIST** indicates a trustlist.
     * @returns { Array<string> } An array of numbers in the incoming call blocklist or trustlist.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
     *     capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function getIncomingCallPolicyNumbers(admin: Want, policy: adminManager.Policy): Array<string>;
    /**
     * Obtains the trustlist or blocklist for incoming calls.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_TELEPHONY
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @param { adminManager.Policy } policy - Policy for trustlist or blocklist. **BLOCK_LIST** indicates a blocklist,
     *     and **TRUST_LIST** indicates a trustlist.
     * @returns { Array<string> } An array of numbers in the incoming call blocklist or trustlist.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
     *     capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getIncomingCallPolicyNumbers(admin: Want | null, policy: adminManager.Policy): Array<string>;
    /**
     * Ends the current call. Only carrier calls are supported, excluding MeeTime calls. For example, an enterprise device
     * administrator can forcibly hang up a non-compliant call that an employee is currently on in enterprise security
     * management scenarios.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_TELEPHONY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 23
     */
    function hangupCalling(admin: Want): void;
    /**
     * Activates the SIM card in the specified slot. In scenarios where a SIM card is inserted but not yet activated, this
     * API can be used to activate the SIM card without requiring manual user action. After the SIM card is activated, it
     * can be used for communication. To successfully call this API, the SIM card must be inserted and airplane mode must
     * be turned off.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_TELEPHONY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { number } slotId - Slot ID. Currently, only single-slot and dual-slot devices are supported. The value can
     *     be **0** or **1**, where **0** indicates slot 1 and **1** indicates slot 2.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 9201017 - SIM card activation or deactivation failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 203 - This function is prohibited by enterprise management policies.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function activeSim(admin: Want, slotId: number): void;
    /**
     * Deactivates the SIM card in the specified slot. After deactivation, the SIM card in that slot cannot be used for
     * making or receiving calls, sending or receiving SMSs, or accessing the internet. For example, an enterprise can
     * temporarily deactivate a SIM card during employee leave or device maintenance. To successfully call this API, the
     * SIM card must be inserted and airplane mode must be turned off.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_TELEPHONY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { number } slotId - Slot ID. Currently, only single-slot and dual-slot devices are supported. The value can
     *     be **0** or **1**, where **0** indicates slot 1 and **1** indicates slot 2.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 9201017 - SIM card activation or deactivation failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 203 - This function is prohibited by enterprise management policies.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function deactiveSim(admin: Want, slotId: number): void;
    /**
     * Sets the SIM card in the specified slot as the default data SIM card. The device will use the data connection from
     * the SIM card in that slot for internet access. For example, in dual-SIM device management scenarios, an enterprise
     * can specify a default data SIM card for employee devices to centrally manage data usage. To successfully call this
     * API, the SIM card must be inserted and airplane mode must be turned off.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_TELEPHONY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { number } slotId - Slot ID. Currently, only single-slot and dual-slot devices are supported. The value can
     *     be **0** or **1**, where **0** indicates slot 1 and **1** indicates slot 2.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 9201020 - Failed to set the default data SIM card.
     *     The airplane mode is enabled or no SIM card is inserted.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 203 - This function is prohibited by enterprise management policies.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function setDefaultData(admin: Want, slotId: number): void;
    /**
     * Obtains the slot ID of the SIM card currently used as the default data SIM card on the device. For example, an
     * enterprise device administrator can query the current default data SIM during device management for data usage
     * control or data card configuration switching. If no SIM card is inserted or the device is in airplane mode, the API
     * returns the slot ID of the last used data SIM card. If the device has never had a default data SIM set, the API
     * returns **0**, indicating slot 1.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_TELEPHONY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { number } Slot ID. Currently, only single-slot and dual-slot devices are supported. The value can be
     *     **0** or **1**, where **0** indicates slot 1 and **1** indicates slot 2.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 203 - This function is prohibited by enterprise management policies.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getDefaultData(admin: Want): number;
}
export default telephonyManager;

```
