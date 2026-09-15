# permissions.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2025 Huawei Device Co., Ltd.
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
 * @file Defines all permissions.
 * @kit AbilityKit
 */
/**
* Indicates permissions.
*
* @typedef Permissions
* @syscap SystemCapability.Security.AccessToken
* @since 9
*/
/**
* Indicates permissions.
*
* @typedef Permissions
* @syscap SystemCapability.Security.AccessToken
* @atomicservice
* @since 11
*/
export type Permissions = 
/**
 * @since 26.0.0
 */
'ohos.permission.CAMERA_SHARED'
/**
 * @since 22
 */
 | 'ohos.permission.CRYPTO_EXTENSION_REGISTER'
/**
 * @since 6
 */
 | 'ohos.permission.ACCESS_BIOMETRIC'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_BBOX_DIR'
/**
 * @since 12
 */
 | 'ohos.permission.SUBSCRIBE_SWING_ABILITY'
/**
 * @since 12
 */
 | 'ohos.permission.MANAGER_SWING_MOTION'
/**
 * @since 7
 */
 | 'ohos.permission.GET_ALL_APP_ACCOUNTS'
/**
 * @since 7
 */
 | 'ohos.permission.MANAGE_SECURE_SETTINGS'
/**
 * @since 7
 */
 | 'ohos.permission.NFC_TAG'
/**
 * @since 12
 */
 | 'ohos.permission.SHORT_TERM_WRITE_IMAGEVIDEO'
/**
 * @since 7
 */
 | 'ohos.permission.GET_RUNNING_INFO'
/**
 * @since 7
 */
 | 'ohos.permission.CLEAN_APPLICATION_DATA'
/**
 * @since 7
 */
 | 'ohos.permission.RUNNING_STATE_OBSERVER'
/**
 * @since 7
 */
 | 'ohos.permission.CAPTURE_SCREEN'
/**
 * @since 7
 * @deprecated since 9
 */
 | 'ohos.permission.START_ABILIIES_FROM_BACKGROUND'
/**
 * @since 7
 */
 | 'ohos.permission.BUNDLE_ACTIVE_INFO'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.BUNDLE_ACTIVE_INFO'
/**
 * @since 7
 */
 | 'ohos.permission.sec.ACCESS_UDID'
/**
 * @since 7
 */
 | 'ohos.permission.LAUNCH_DATA_PRIVACY_CENTER'
/**
 * @since 7
 */
 | 'ohos.permission.PUBLISH_AGENT_REMINDER'
/**
 * @since 7
 */
 | 'ohos.permission.CONTROL_TASK_SYNC_ANIMATOR'
/**
 * @since 7
 */
 | 'ohos.permission.INPUT_MONITORING'
/**
 * @since 7
 */
 | 'ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_EXTENSION'
/**
 * @since 7
 */
 | 'ohos.permission.LISTEN_BUNDLE_CHANGE'
/**
 * @since 7
 */
 | 'ohos.permission.GET_BUNDLE_INFO'
/**
 * @since 7
 */
 | 'ohos.permission.ACCELEROMETER'
/**
 * @since 7
 */
 | 'ohos.permission.GYROSCOPE'
/**
 * @since 7
 */
 | 'ohos.permission.GET_BUNDLE_INFO_PRIVILEGED'
/**
 * @since 23
 */
 | 'ohos.permission.INSTALL_ALLOW_DOWNGRADE'
/**
 * @since 7
 */
 | 'ohos.permission.INSTALL_BUNDLE'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ALLOW_USE_BM'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.INSTALL_BUNDLE'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.UNINSTALL_BUNDLE'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.GET_BUNDLE_INFO_PRIVILEGED'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.REMOVE_BUNDLE_DATA_AND_CACHE_FILES'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.MANAGE_DISPOSED_APP_STATUS'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.MANAGE_CLONE_BUNDLE_PREFERENCES'
/**
 * @since 7
 */
 | 'ohos.permission.MANAGE_SHORTCUTS'
/**
 * @since 7
 */
 | 'ohos.permission.radio.ACCESS_FM_AM'
/**
 * @since 7
 */
 | 'ohos.permission.MANAGE_BLUETOOTH'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.MANAGE_RECENT_SNAPSHOT'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.SET_WINDOW_ALPHA'
/**
 * @since 7
 */
 | 'ohos.permission.ACCESS_NOTIFICATION_POLICY'
/**
 * @since 7
 */
 | 'ohos.permission.REQUIRE_FORM'
/**
 * @since 18
 */
 | 'ohos.permission.START_DESKTOP_UI_COMPONENT'
/**
 * @since 7
 */
 | 'ohos.permission.REMOVE_CACHE_FILES'
/**
 * @since 7
 */
 | 'ohos.permission.REBOOT'
/**
 * @since 7
 */
 | 'ohos.permission.RUNNING_LOCK'
/**
 * @since 7
 */
 | 'ohos.permission.SET_TIME'
/**
 * @since 7
 */
 | 'ohos.permission.SET_TIME_ZONE'
/**
 * @since 7
 */
 | 'ohos.permission.DOWNLOAD_SESSION_MANAGER'
/**
 * @since 7
 */
 | 'ohos.permission.COMMONEVENT_STICKY'
/**
 * @since 7
 */
 | 'ohos.permission.SYSTEM_FLOAT_WINDOW'
/**
 * @since 7
 */
 | 'ohos.permission.POWER_MANAGER'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.POWER_MANAGER'
/**
 * @since 7
 */
 | 'ohos.permission.REFRESH_USER_ACTION'
/**
 * @since 7
 */
 | 'ohos.permission.POWER_OPTIMIZATION'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.POWER_OPTIMIZATION'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.BATTERY_INFO'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.BRIGHTNESS_MANAGER'
/**
 * @since 7
 */
 | 'ohos.permission.REBOOT_RECOVERY'
/**
 * @since 7
 */
 | 'ohos.permission.MANAGE_LOCAL_ACCOUNTS'
/**
 * @since 7
 */
 | 'ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS'
/**
 * @since 7
 */
 | 'ohos.permission.VIBRATE'
/**
 * @since 7
 */
 | 'ohos.permission.CONNECT_IME_ABILITY'
/**
 * @since 7
 */
 | 'ohos.permission.CONNECT_SCREEN_SAVER_ABILITY'
/**
 * @since 7
 */
 | 'ohos.permission.READ_SCREEN_SAVER'
/**
 * @since 7
 */
 | 'ohos.permission.WRITE_SCREEN_SAVER'
/**
 * @since 7
 */
 | 'ohos.permission.SET_WALLPAPER'
/**
 * @since 7
 */
 | 'ohos.permission.GET_WALLPAPER'
/**
 * @since 7
 */
 | 'ohos.permission.CHANGE_ABILITY_ENABLED_STATE'
/**
 * @since 7
 * @deprecated since 9
 */
 | 'ohos.permission.ACCESS_MISSIONS'
/**
 * @since 7
 */
 | 'ohos.permission.CLEAN_BACKGROUND_PROCESSES'
/**
 * @since 7
 */
 | 'ohos.permission.UPDATE_CONFIGURATION'
/**
 * @since 8
 */
 | 'ohos.permission.GET_WIFI_INFO_INTERNAL'
/**
 * @since 8
 */
 | 'ohos.permission.USE_BLUETOOTH'
/**
 * @since 8
 */
 | 'ohos.permission.DISCOVER_BLUETOOTH'
/**
 * @since 8
 */
 | 'ohos.permission.MODIFY_AUDIO_SETTINGS'
/**
 * @since 8
 */
 | 'ohos.permission.GET_TELEPHONY_STATE'
/**
 * @since 8
 */
 | 'ohos.permission.GET_NETWORK_INFO'
/**
 * @since 8
 */
 | 'ohos.permission.PLACE_CALL'
/**
 * @since 8
 */
 | 'ohos.permission.SET_NETWORK_INFO'
/**
 * @since 8
 */
 | 'ohos.permission.KEEP_BACKGROUND_RUNNING'
/**
 * @since 8
 */
 | 'ohos.permission.UPDATE_SYSTEM'
/**
 * @since 8
 */
 | 'ohos.permission.FACTORY_RESET'
/**
 * @since 23
 */
 | 'ohos.permission.FORCE_FACTORY_RESET'
/**
 * @since 12
 */
 | 'ohos.permission.ASSIST_DEVICE_UPDATE'
/**
 * @since 18
 */
 | 'ohos.permission.PLUGIN_UPDATE'
/**
 * @since 12
 */
 | 'ohos.permission.RECEIVE_UPDATE_MESSAGE'
/**
 * @since 8
 */
 | 'ohos.permission.GRANT_SENSITIVE_PERMISSIONS'
/**
 * @since 8
 */
 | 'ohos.permission.REVOKE_SENSITIVE_PERMISSIONS'
/**
 * @since 8
 */
 | 'ohos.permission.GET_SENSITIVE_PERMISSIONS'
/**
 * @since 8
 */
 | 'ohos.permission.SET_TELEPHONY_STATE'
/**
 * @since 8
 */
 | 'ohos.permission.NOTIFICATION_CONTROLLER'
/**
 * @since 8
 */
 | 'ohos.permission.CONNECTIVITY_INTERNAL'
/**
 * @since 8
 */
 | 'ohos.permission.USE_USER_IDM'
/**
 * @since 8
 */
 | 'ohos.permission.MANAGE_USER_IDM'
/**
 * @since 8
 */
 | 'ohos.permission.ACCESS_USER_AUTH_INTERNAL'
/**
 * @since 8
 */
 | 'ohos.permission.ACCESS_PIN_AUTH'
/**
 * @since 8
 */
 | 'ohos.permission.GET_WIFI_INFO'
/**
 * @since 8
 */
 | 'ohos.permission.SET_WIFI_INFO'
/**
 * @since 8
 */
 | 'ohos.permission.GET_WIFI_PEERS_MAC'
/**
 * @since 8
 */
 | 'ohos.permission.GET_WIFI_LOCAL_MAC'
/**
 * @since 8
 */
 | 'ohos.permission.GET_WIFI_CONFIG'
/**
 * @since 8
 */
 | 'ohos.permission.SET_WIFI_CONFIG'
/**
 * @since 15
 */
 | 'ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION'
/**
 * @since 8
 */
 | 'ohos.permission.MANAGE_WIFI_CONNECTION'
/**
 * @since 8
 */
 | 'ohos.permission.MANAGE_WIFI_HOTSPOT'
/**
 * @since 8
 */
 | 'ohos.permission.READ_DFX_SYSEVENT'
/**
 * @since 12
 */
 | 'ohos.permission.READ_DFX_XPOWER'
/**
 * @since 8
 */
 | 'ohos.permission.NFC_CARD_EMULATION'
/**
 * @since 20
 */
 | 'ohos.permission.NFC_NOTIFICATION'
/**
 * @since 9
 */
 | 'ohos.permission.PERMISSION_USED_STATS'
/**
 * @since 18
 */
 | 'ohos.permission.PERMISSION_RECORD_TOGGLE'
/**
 * @since 9
 */
 | 'ohos.permission.NOTIFICATION_AGENT_CONTROLLER'
/**
 * @since 9
 */
 | 'ohos.permission.MOUNT_UNMOUNT_MANAGER'
/**
 * @since 9
 */
 | 'ohos.permission.MOUNT_FORMAT_MANAGER'
/**
 * @since 9
 */
 | 'ohos.permission.STORAGE_MANAGER'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.GET_STORAGE_MANAGER'
/**
 * @since 9
 */
 | 'ohos.permission.BACKUP'
/**
 * @since 9
 */
 | 'ohos.permission.FILE_ACCESS_MANAGER'
/**
 * @since 9
 */
 | 'ohos.permission.GET_DEFAULT_APPLICATION'
/**
 * @since 9
 */
 | 'ohos.permission.SET_DEFAULT_APPLICATION'
/**
 * @since 9
 */
 | 'ohos.permission.ACCESS_IDS'
/**
 * @since 9
 */
 | 'ohos.permission.MANAGE_DISPOSED_APP_STATUS'
/**
 * @since 12
 */
 | 'ohos.permission.GET_DISPOSED_APP_STATUS'
/**
 * @since 9
 */
 | 'ohos.permission.ACCESS_DLP_FILE'
/**
 * @since 9
 */
 | 'ohos.permission.PROVISIONING_MESSAGE'
/**
 * @since 9
 */
 | 'ohos.permission.ACCESS_SYSTEM_SETTINGS'
/**
 * @since 9
 */
 | 'ohos.permission.ABILITY_BACKGROUND_COMMUNICATION'
/**
 * @since 9
 */
 | 'ohos.permission.securityguard.REPORT_SECURITY_INFO'
/**
 * @since 9
 */
 | 'ohos.permission.securityguard.REQUEST_SECURITY_MODEL_RESULT'
/**
 * @since 9
 */
 | 'ohos.permission.securityguard.REQUEST_SECURITY_EVENT_INFO'
/**
 * @since 9
 */
 | 'ohos.permission.ACCESS_CERT_MANAGER_INTERNAL'
/**
 * @since 9
 */
 | 'ohos.permission.ACCESS_CERT_MANAGER'
/**
 * @since 9
 */
 | 'ohos.permission.GET_LOCAL_ACCOUNTS'
/**
 * @since 9
 */
 | 'ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS'
/**
 * @since 9
 */
 | 'ohos.permission.GET_DISTRIBUTED_ACCOUNTS'
/**
 * @since 9
 */
 | 'ohos.permission.READ_ACCESSIBILITY_CONFIG'
/**
 * @since 9
 */
 | 'ohos.permission.WRITE_ACCESSIBILITY_CONFIG'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.WRITE_ACCESSIBILITY_CONFIG_VISION'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.READ_ACCESSIBILITY_CONFIG_VISION'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.WRITE_ACCESSIBILITY_CONFIG_HEARING'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.READ_ACCESSIBILITY_CONFIG_HEARING'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.WRITE_ACCESSIBILITY_CONFIG_ACTION'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.READ_ACCESSIBILITY_CONFIG_ACTION'
/**
 * @since 9
 */
 | 'ohos.permission.ACCESS_PUSH_SERVICE'
/**
 * @since 9
 */
 | 'ohos.permission.MANAGE_AUDIO_CONFIG'
/**
 * @since 9
 */
 | 'ohos.permission.MANAGE_CAMERA_CONFIG'
/**
 * @since 12
 */
 | 'ohos.permission.CAMERA_CONTROL'
/**
 * @since 9
 */
 | 'ohos.permission.RECEIVER_STARTUP_COMPLETED'
/**
 * @since 9
 */
 | 'ohos.permission.START_INVISIBLE_ABILITY'
/**
 * @since 9
 */
 | 'ohos.permission.START_ABILITIES_FROM_BACKGROUND'
/**
 * @since 9
 */
 | 'ohos.permission.INTERNET'
/**
 * @since 12
 */
 | 'ohos.permission.GET_APP_DOMAIN_BUNDLE_INFO'
/**
 * @since 9
 */
 | 'ohos.permission.DISTRIBUTED_SOFTBUS_CENTER'
/**
 * @since 9
 */
 | 'ohos.permission.PRIVACY_WINDOW'
/**
 * @since 9
 */
 | 'ohos.permission.MANAGE_ENTERPRISE_DEVICE_ADMIN'
/**
 * @since 24
 */
 | 'ohos.permission.ENTERPRISE_ACTIVATE_DEVICE_ADMIN'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ENTERPRISE_MANAGE_LOCAL_ACCOUNTS'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ENTERPRISE_INTERACT_ACROSS_LOCAL_ACCOUNTS'
/**
 * @since 9
 */
 | 'ohos.permission.SET_ENTERPRISE_INFO'
/**
 * @since 9
 */
 | 'ohos.permission.ACCESS_BUNDLE_DIR'
/**
 * @since 9
 */
 | 'ohos.permission.ENTERPRISE_SUBSCRIBE_MANAGED_EVENT'
/**
 * @since 9
 */
 | 'ohos.permission.ENTERPRISE_SET_DATETIME'
/**
 * @since 12
 */
 | 'ohos.permission.ENTERPRISE_OPERATE_DEVICE'
/**
 * @since 12
 */
 | 'ohos.permission.ENTERPRISE_ADMIN_MANAGE'
/**
 * @since 12
 */
 | 'ohos.permission.ENTERPRISE_CONFIG'
/**
 * @since 9
 */
 | 'ohos.permission.DUMP'
/**
 * @since 9
 */
 | 'ohos.permission.ACCESS_AUTH_RESPOOL'
/**
 * @since 9
 */
 | 'ohos.permission.ENFORCE_USER_IDM'
/**
 * @since 9
 */
 | 'ohos.permission.MANAGE_MEDIA_RESOURCES'
/**
 * @since 9
 */
 | 'ohos.permission.SET_ABILITY_CONTROLLER'
/**
 * @since 9
 */
 | 'ohos.permission.MANAGE_MISSIONS'
/**
 * @since 10
 */
 | 'ohos.permission.GET_PHONE_NUMBERS'
/**
 * @since 10
 */
 | 'ohos.permission.UPDATE_MIGRATE'
/**
 * @since 10
 */
 | 'ohos.permission.CLOUDFILE_SYNC_MANAGER'
/**
 * @since 10
 */
 | 'ohos.permission.CLOUDFILE_SYNC'
/**
 * @since 10
 */
 | 'ohos.permission.MANAGE_NET_STRATEGY'
/**
 * @since 10
 */
 | 'ohos.permission.GET_NETWORK_STATS'
/**
 * @since 10
 */
 | 'ohos.permission.MANAGE_VPN'
/**
 * @since 10
 */
 | 'ohos.permission.NETSYS_INTERNAL'
/**
 * @since 10
 */
 | 'ohos.permission.READ_HIVIEW_SYSTEM'
/**
 * @since 10
 */
 | 'ohos.permission.WRITE_HIVIEW_SYSTEM'
/**
 * @since 10
 */
 | 'ohos.permission.ENTERPRISE_GET_DEVICE_INFO'
/**
 * @since 10
 */
 | 'ohos.permission.ENTERPRISE_RESET_DEVICE'
/**
 * @since 10
 */
 | 'ohos.permission.ENTERPRISE_SET_WIFI'
/**
 * @since 10
 */
 | 'ohos.permission.ENTERPRISE_GET_NETWORK_INFO'
/**
 * @since 10
 */
 | 'ohos.permission.ENTERPRISE_SET_ACCOUNT_POLICY'
/**
 * @since 10
 */
 | 'ohos.permission.ENTERPRISE_SET_BUNDLE_INSTALL_POLICY'
/**
 * @since 10
 */
 | 'ohos.permission.ENTERPRISE_SET_NETWORK'
/**
 * @since 10
 */
 | 'ohos.permission.ENTERPRISE_MANAGE_SET_APP_RUNNING_POLICY'
/**
 * @since 10
 */
 | 'ohos.permission.ENTERPRISE_SET_SCREENOFF_TIME'
/**
 * @since 10
 */
 | 'ohos.permission.ENTERPRISE_GET_SETTINGS'
/**
 * @since 10
 */
 | 'ohos.permission.ENTERPRISE_INSTALL_BUNDLE'
/**
 * @since 10
 */
 | 'ohos.permission.ENTERPRISE_MANAGE_CERTIFICATE'
/**
 * @since 10
 */
 | 'ohos.permission.ENTERPRISE_RESTRICT_POLICY'
/**
 * @since 10
 */
 | 'ohos.permission.ENTERPRISE_MANAGE_USB'
/**
 * @since 10
 */
 | 'ohos.permission.ENTERPRISE_MANAGE_NETWORK'
/**
 * @since 10
 */
 | 'ohos.permission.ENTERPRISE_SET_BROWSER_POLICY'
/**
 * @since 10
 */
 | 'ohos.permission.READ_APP_PUSH_DATA'
/**
 * @since 10
 */
 | 'ohos.permission.WRITE_APP_PUSH_DATA'
/**
 * @since 10
 */
 | 'ohos.permission.ACCESS_SERVICE_DM'
/**
 * @since 10
 */
 | 'ohos.permission.RUN_ANY_CODE'
/**
 * @since 10
 */
 | 'ohos.permission.PUBLISH_SYSTEM_COMMON_EVENT'
/**
 * @since 10
 */
 | 'ohos.permission.ACCESS_SCREEN_LOCK_INNER'
/**
 * @since 10
 */
 | 'ohos.permission.PRINT'
/**
 * @since 10
 */
 | 'ohos.permission.MANAGE_PRINT_JOB'
/**
 * @since 24
 */
 | 'ohos.permission.ENTERPRISE_MANAGE_PRINT'
/**
 * @since 24
 */
 | 'ohos.permission.PRINTER_DRIVER'
/**
 * @since 10
 */
 | 'ohos.permission.CHANGE_OVERLAY_ENABLED_STATE'
/**
 * @since 10
 */
 | 'ohos.permission.CONNECT_CELLULAR_CALL_SERVICE'
/**
 * @since 10
 */
 | 'ohos.permission.CONNECT_IMS_SERVICE'
/**
 * @since 10
 */
 | 'ohos.permission.ACCESS_SENSING_WITH_ULTRASOUND'
/**
 * @since 10
 */
 | 'ohos.permission.PROXY_AUTHORIZATION_URI'
/**
 * @since 10
 */
 | 'ohos.permission.INSTALL_ENTERPRISE_BUNDLE'
/**
 * @since 10
 */
 | 'ohos.permission.ACCESS_CAST_ENGINE_MIRROR'
/**
 * @since 10
 */
 | 'ohos.permission.ACCESS_CAST_ENGINE_STREAM'
/**
 * @since 10
 */
 | 'ohos.permission.CLOUDDATA_CONFIG'
/**
 * @since 10
 */
 | 'ohos.permission.DEVICE_STANDBY_EXEMPTION'
/**
 * @since 12
 */
 | 'ohos.permission.PERCEIVE_SMART_POWER_SCENARIO'
/**
 * @since 10
 */
 | 'ohos.permission.RESTRICT_APPLICATION_ACTIVE'
/**
 * @since 10
 */
 | 'ohos.permission.MANAGE_SENSOR'
/**
 * @since 10
 */
 | 'ohos.permission.UPLOAD_SESSION_MANAGER'
/**
 * @since 10
 */
 | 'ohos.permission.PREPARE_APP_TERMINATE'
/**
 * @since 10
 */
 | 'ohos.permission.MANAGE_ECOLOGICAL_RULE'
/**
 * @since 10
 */
 | 'ohos.permission.GET_SCENE_CODE'
/**
 * @since 10
 */
 | 'ohos.permission.FILE_GUARD_MANAGER'
/**
 * @since 10
 */
 | 'ohos.permission.SET_FILE_GUARD_POLICY'
/**
 * @since 20
 */
 | 'ohos.permission.FILE_GUARD_FILE_WRITE'
/**
 * @since 13
 */
 | 'ohos.permission.ENTERPRISE_RECOVERY_KEY'
/**
 * @since 14
 */
 | 'ohos.permission.MANAGE_RECOVERY_KEY'
/**
 * @since 14
 */
 | 'ohos.permission.UTILIZE_RECOVERY_KEY'
/**
 * @since 14
 */
 | 'ohos.permission.GET_RECOVERY_KEY_BRIEF_INFORMATION'
/**
 * @since 20
 */
 | 'ohos.permission.MANAGE_FILE_ENCRYPTION'
/**
 * @since 10
 */
 | 'ohos.permission.securityguard.SET_MODEL_STATE'
/**
 * @since 10
 */
 | 'ohos.permission.hsdr.HSDR_ACCESS'
/**
 * @since 10
 */
 | 'ohos.permission.SUPPORT_USER_AUTH'
/**
 * @since 10
 */
 | 'ohos.permission.CAPTURE_VOICE_DOWNLINK_AUDIO'
/**
 * @since 10
 */
 | 'ohos.permission.MANAGE_INTELLIGENT_VOICE'
/**
 * @since 10
 */
 | 'ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE'
/**
 * @since 10
 */
 | 'ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE'
/**
 * @since 10
 */
 | 'ohos.permission.INSTALL_SELF_BUNDLE'
/**
 * @since 10
 */
 | 'ohos.permission.OBSERVE_FORM_RUNNING'
/**
 * @since 10
 */
 | 'ohos.permission.MANAGE_DEVICE_AUTH_CRED'
/**
 * @since 10
 */
 | 'ohos.permission.UNINSTALL_BUNDLE'
/**
 * @since 10
 */
 | 'ohos.permission.RECOVER_BUNDLE'
/**
 * @since 10
 */
 | 'ohos.permission.GET_DOMAIN_ACCOUNTS'
/**
 * @since 11
 */
 | 'ohos.permission.ACCESS_DDK_USB'
/**
 * @since 18
 */
 | 'ohos.permission.ACCESS_DDK_USB_SERIAL'
/**
 * @since 18
 */
 | 'ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL'
/**
 * @since 11
 */
 | 'ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER'
/**
 * @since 18
 */
 | 'ohos.permission.ACCESS_DDK_DRIVERS'
/**
 * @since 11
 */
 | 'ohos.permission.AGENT_REQUIRE_FORM'
/**
 * @since 11
 */
 | 'ohos.permission.SYSTEM_LIGHT_CONTROL'
/**
 * @since 11
 */
 | 'ohos.permission.MANAGE_FINGERPRINT_AUTH'
/**
 * @since 11
 */
 | 'ohos.permission.ENTERPRISE_MANAGE_SYSTEM'
/**
 * @since 11
 */
 | 'ohos.permission.ENTERPRISE_MANAGE_SETTINGS'
/**
 * @since 11
 */
 | 'ohos.permission.ENTERPRISE_MANAGE_SECURITY'
/**
 * @since 11
 */
 | 'ohos.permission.ENTERPRISE_MANAGE_BLUETOOTH'
/**
 * @since 11
 */
 | 'ohos.permission.ENTERPRISE_MANAGE_WIFI'
/**
 * @since 11
 */
 | 'ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS'
/**
 * @since 11
 */
 | 'ohos.permission.ENTERPRISE_MANAGE_APPLICATION'
/**
 * @since 11
 */
 | 'ohos.permission.ENTERPRISE_MANAGE_LOCATION'
/**
 * @since 11
 */
 | 'ohos.permission.ENTERPRISE_REBOOT'
/**
 * @since 11
 */
 | 'ohos.permission.ENTERPRISE_LOCK_DEVICE'
/**
 * @since 14
 */
 | 'ohos.permission.ENTERPRISE_MANAGE_DELEGATED_POLICY'
/**
 * @since 20
 */
 | 'ohos.permission.ENTERPRISE_GET_ALL_BUNDLE_INFO'
/**
 * @since 20
 */
 | 'ohos.permission.ENTERPRISE_SET_USER_RESTRICTION'
/**
 * @since 20
 */
 | 'ohos.permission.ENTERPRISE_MANAGE_APN'
/**
 * @since 20
 */
 | 'ohos.permission.ENTERPRISE_MANAGE_TELEPHONY'
/**
 * @since 20
 */
 | 'ohos.permission.ENTERPRISE_SET_KIOSK'
/**
 * @since 20
 */
 | 'ohos.permission.ENTERPRISE_SET_WALLPAPER'
/**
 * @since 14
 */
 | 'ohos.permission.RECEIVE_ENTERPRISE_POLICY_EVENT'
/**
 * @since 15
 */
 | 'ohos.permission.PERSONAL_MANAGE_RESTRICTIONS'
/**
 * @since 15
 */
 | 'ohos.permission.START_PROVISIONING_MESSAGE'
/**
 * @since 11
 */
 | 'ohos.permission.SET_UNREMOVABLE_NOTIFICATION'
/**
 * @since 11
 */
 | 'ohos.permission.QUERY_ACCESSIBILITY_ELEMENT'
/**
 * @since 11
 */
 | 'ohos.permission.ACTIVATE_THEME_PACKAGE'
/**
 * @since 11
 */
 | 'ohos.permission.ATTEST_KEY'
/**
 * @since 11
 */
 | 'ohos.permission.WAKEUP_VOICE'
/**
 * @since 11
 */
 | 'ohos.permission.WAKEUP_VISION'
/**
 * @since 11
 */
 | 'ohos.permission.ENABLE_DISTRIBUTED_HARDWARE'
/**
 * @since 11
 */
 | 'ohos.permission.ACCESS_DISTRIBUTED_HARDWARE'
/**
 * @since 11
 */
 | 'ohos.permission.INSTANTSHARE_SWITCH_CONTROL'
/**
 * @since 11
 */
 | 'ohos.permission.ACCESS_INSTANTSHARE_SERVICE'
/**
 * @since 11
 */
 | 'ohos.permission.ACCESS_INSTANTSHARE_PRIVATE_ABILITY'
/**
 * @since 11
 */
 | 'ohos.permission.SECURE_PASTE'
/**
 * @since 11
 */
 | 'ohos.permission.ACCESS_MCP_AUTHORIZATION'
/**
 * @since 11
 */
 | 'ohos.permission.GET_BUNDLE_RESOURCES'
/**
 * @since 11
 */
 | 'ohos.permission.SET_CODE_PROTECT_INFO'
/**
 * @since 11
 */
 | 'ohos.permission.SET_ADVANCED_SECURITY_MODE'
/**
 * @since 11
 */
 | 'ohos.permission.SET_DEVELOPER_MODE'
/**
 * @since 11
 */
 | 'ohos.permission.RUN_DYN_CODE'
/**
 * @since 11
 */
 | 'ohos.permission.COOPERATE_MANAGER'
/**
 * @since 11
 */
 | 'ohos.permission.PERCEIVE_TRAIL'
/**
 * @since 11
 */
 | 'ohos.permission.DISABLE_PERMISSION_DIALOG'
/**
 * @since 11
 */
 | 'ohos.permission.EXECUTE_INSIGHT_INTENT'
/**
 * @since 11
 */
 | 'ohos.permission.MANAGE_ACTIVATION_LOCK'
/**
 * @since 11
 */
 | 'ohos.permission.VERIFY_ACTIVATION_LOCK'
/**
 * @since 11
 */
 | 'ohos.permission.MANAGE_PRIVATE_PHOTOS'
/**
 * @since 11
 */
 | 'ohos.permission.ACCESS_OUC'
/**
 * @since 11
 */
 | 'ohos.permission.TRUSTED_RING_HASH_DATA_PERMISSION'
/**
 * @since 11
 */
 | 'ohos.permission.MANAGE_TRUSTED_RING'
/**
 * @since 11
 */
 | 'ohos.permission.USE_TRUSTED_RING'
/**
 * @since 11
 */
 | 'ohos.permission.INPUT_CONTROL_DISPATCHING'
/**
 * @since 11
 */
 | 'ohos.permission.INTERCEPT_INPUT_EVENT'
/**
 * @since 12
 */
 | 'ohos.permission.LAUNCH_SPAMSHIELD_PAGE'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_SPAMSHIELD_SERVICE'
/**
 * @since 11
 */
 | 'ohos.permission.ACCESS_SECURITY_PRIVACY_CENTER'
/**
 * @since 11
 */
 | 'ohos.permission.GET_SECURITY_PRIVACY_ADVICE'
/**
 * @since 11
 */
 | 'ohos.permission.SET_SECURITY_PRIVACY_ADVICE'
/**
 * @since 11
 */
 | 'ohos.permission.USE_SECURITY_PRIVACY_MESSAGER'
/**
 * @since 12
 */
 | 'ohos.permission.EXEMPT_PRIVACY_INDICATOR'
/**
 * @since 12
 */
 | 'ohos.permission.EXEMPT_CAMERA_PRIVACY_INDICATOR'
/**
 * @since 18
 */
 | 'ohos.permission.ACCESS_CONFIDENTIAL_COMPUTING_ZONE'
/**
 * @since 18
 */
 | 'ohos.permission.SYNC_ASSET_BETWEEN_TRUSTED_ACCOUNT'
/**
 * @since 12
 */
 | 'ohos.permission.EXEMPT_MICROPHONE_PRIVACY_INDICATOR'
/**
 * @since 12
 */
 | 'ohos.permission.EXEMPT_LOCATION_PRIVACY_INDICATOR'
/**
 * @since 12
 */
 | 'ohos.permission.GET_SUPER_PRIVACY'
/**
 * @since 12
 */
 | 'ohos.permission.SET_SUPER_PRIVACY'
/**
 * @since 11
 */
 | 'ohos.permission.RECORD_VOICE_CALL'
/**
 * @since 11
 */
 | 'ohos.permission.MANAGE_APP_INSTALL_INFO'
/**
 * @since 19
 */
 | 'ohos.permission.MANAGE_APP_UNINSTALL'
/**
 * @since 11
 */
 | 'ohos.permission.RECEIVE_APP_INSTALL_INFO_CHANGE'
/**
 * @since 11
 */
 | 'ohos.permission.ACCESS_ADVANCED_SECURITY_MODE'
/**
 * @since 11
 */
 | 'ohos.permission.STORE_PERSISTENT_DATA'
/**
 * @since 11
 */
 | 'ohos.permission.ACCESS_HIVIEWX'
/**
 * @since 11
 */
 | 'ohos.permission.ACCESS_PASSWORDVAULT_ABILITY'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_TEXTAUTOFILL_ABILITY'
/**
 * @since 11
 */
 | 'ohos.permission.ACCESS_LOWPOWER_MANAGER'
/**
 * @since 11
 */
 | 'ohos.permission.ACCESS_DDK_HID'
/**
 * @since 11
 */
 | 'ohos.permission.MANAGE_APP_BOOT'
/**
 * @since 11
 */
 | 'ohos.permission.ACCESS_HIVIEWCARE'
/**
 * @since 11
 */
 | 'ohos.permission.FILE_ACCESS_PERSIST'
/**
 * @since 11
 */
 | 'ohos.permission.SET_SANDBOX_POLICY'
/**
 * @since 15
 */
 | 'ohos.permission.CHECK_SANDBOX_POLICY'
/**
 * @since 11
 */
 | 'ohos.permission.ACCESS_ACCOUNT_KIT_SERVICE'
/**
 * @since 11
 */
 | 'ohos.permission.REQUEST_ANONYMOUS_ATTEST'
/**
 * @since 11
 */
 | 'ohos.permission.ACCESS_ACCOUNT_KIT_UI'
/**
 * @since 11
 */
 | 'ohos.permission.START_RECENT_ABILITY'
/**
 * @since 11
 */
 | 'ohos.permission.READ_CLOUD_SYNC_CONFIG'
/**
 * @since 11
 */
 | 'ohos.permission.MANAGE_CLOUD_SYNC_CONFIG'
/**
 * @since 11
 */
 | 'ohos.permission.ACCESS_FINDDEVICE'
/**
 * @since 11
 */
 | 'ohos.permission.MANAGE_FINDSERVICE'
/**
 * @since 11
 */
 | 'ohos.permission.TRIGGER_ACTIVATIONLOCK'
/**
 * @since 11
 */
 | 'ohos.permission.MANAGE_USB_CONFIG'
/**
 * @since 11
 */
 | 'ohos.permission.WRITE_PRIVACY_PUSH_DATA'
/**
 * @since 12
 */
 | 'ohos.permission.READ_PRIVACY_PUSH_DATA'
/**
 * @since 11
 */
 | 'ohos.permission.ACCESS_STATUSBAR_ICON'
/**
 * @since 11
 */
 | 'ohos.permission.START_SYSTEM_DIALOG'
/**
 * @since 11
 */
 | 'ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS'
/**
 * @since 11
 */
 | 'ohos.permission.GET_BLUETOOTH_LOCAL_MAC'
/**
 * @since 24
 */
 | 'ohos.permission.ACQUIRE_LOCAL_ACCOUNT_AUTHORIZATION'
/**
 * @since 12
 */
 | 'ohos.permission.MANAGE_NEARLINK'
/**
 * @since 12
 */
 | 'ohos.permission.GET_NEARLINK_LOCAL_MAC'
/**
 * @since 12
 */
 | 'ohos.permission.MANAGE_UWB'
/**
 * @since 12
 */
 | 'ohos.permission.USE_UWB_RANGING'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_PROTOCOL_DFX_DATA'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_PROTOCOL_DFX_STATE'
/**
 * @since 14
 */
 | 'ohos.permission.ACCESS_CMAP_SERVICE'
/**
 * @since 12
 */
 | 'ohos.permission.MANAGE_RGM'
/**
 * @since 12
 */
 | 'ohos.permission.ALLOW_UPGRADE_GUIDE_ACCESS'
/**
 * @since 12
 */
 | 'ohos.permission.MANAGE_USER_ACCOUNT_INFO'
/**
 * @since 12
 */
 | 'ohos.permission.NOTIFY_DEBUG_ASSERT_RESULT'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_AI_ABILITY'
/**
 * @since 12
 */
 | 'ohos.permission.READ_HEALTH_MOTION'
/**
 * @since 12
 */
 | 'ohos.permission.hsdr.REQUEST_HSDR'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_PRIVATE_SPACE_MANAGER'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_PRIVATE_SPACE_PASSWORD_PROTECT'
/**
 * @since 12
 */
 | 'ohos.permission.QUERY_PASSWORD_VAULT_DATA'
/**
 * @since 12
 */
 | 'ohos.permission.SUBSCRIBE_NOTIFICATION_WINDOW_STATE'
/**
 * @since 12
 */
 | 'ohos.permission.STORAGE_MANAGER_CRYPT'
/**
 * @since 12
 */
 | 'ohos.permission.CHANGE_DISPLAYMODE'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_MEDIALIB_THUMB_DB'
/**
 * @since 12
 */
 | 'ohos.permission.MIGRATE_DATA'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_DYNAMIC_ICON'
/**
 * @since 12
 */
 | 'ohos.permission.CHANGE_BUNDLE_UNINSTALL_STATE'
/**
 * @since 12
 */
 | 'ohos.permission.MANAGE_STYLUS_EVENT'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.STYLUS_FRAME_BOOST'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_SERVICE_NAVIGATION_INFO'
/**
 * @since 12
 */
 | 'ohos.permission.READ_ACCOUNT_LOGIN_STATE'
/**
 * @since 12
 */
 | 'ohos.permission.WRITE_ACCOUNT_LOGIN_STATE'
/**
 * @since 12
 */
 | 'ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_AS_USER'
/**
 * @since 12
 */
 | 'ohos.permission.READ_FINDSERVICE'
/**
 * @since 12
 */
 | 'ohos.permission.GET_NEARLINK_PEER_MAC'
/**
 * @since 12
 */
 | 'ohos.permission.GET_PRIVACY_INDICATOR'
/**
 * @since 12
 */
 | 'ohos.permission.SET_PRIVACY_INDICATOR'
/**
 * @since 13
 */
 | 'ohos.permission.EXEMPT_PRIVACY_SECURITY_CENTER'
/**
 * @since 13
 */
 | 'ohos.permission.ACCESS_LEARN_MORE_DIALOG'
/**
 * @since 17
 */
 | 'ohos.permission.WRITE_PROTECTION_ADVICE_POLICY'
/**
 * @since 17
 */
 | 'ohos.permission.READ_PROTECTION_ADVICE_POLICY'
/**
 * @since 15
 */
 | 'ohos.permission.USE_FRAUD_MESSAGES_PICKER'
/**
 * @since 15
 */
 | 'ohos.permission.USE_FRAUD_CALL_LOG_PICKER'
/**
 * @since 18
 */
 | 'ohos.permission.USE_FRAUD_APP_PICKER'
/**
 * @since 18
 */
 | 'ohos.permission.PROXY_MESSAGE_AUTH'
/**
 * @since 12
 */
 | 'ohos.permission.GET_BLUETOOTH_PEERS_MAC'
/**
 * @since 16
 */
 | 'ohos.permission.PERSISTENT_BLUETOOTH_PEERS_MAC'
/**
 * @since 12
 */
 | 'ohos.permission.WRITE_GTOKEN_POLICY'
/**
 * @since 12
 */
 | 'ohos.permission.READ_GTOKEN_POLICY'
/**
 * @since 12
 */
 | 'ohos.permission.ENABLE_PROFILER'
/**
 * @since 12
 */
 | 'ohos.permission.USE_CLOUD_DRIVE_SERVICE'
/**
 * @since 12
 */
 | 'ohos.permission.USE_CLOUD_BACKUP_SERVICE'
/**
 * @since 12
 */
 | 'ohos.permission.USE_CLOUD_COMMON_SERVICE'
/**
 * @since 12
 */
 | 'ohos.permission.START_DLP_CRED'
/**
 * @since 12
 */
 | 'ohos.permission.START_SHORTCUT'
/**
 * @since 12
 */
 | 'ohos.permission.GET_ACCOUNT_MINORS_INFO'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_SHADER_CACHE_DIR'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_LOCAL_THEME'
/**
 * @since 12
 */
 | 'ohos.permission.INSTALL_CLONE_BUNDLE'
/**
 * @since 12
 */
 | 'ohos.permission.UNINSTALL_CLONE_BUNDLE'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_SEARCH_SERVICE'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_SCREEN_LOCK'
/**
 * @since 12
 */
 | 'ohos.permission.SET_PROCESS_CACHE_STATE'
/**
 * @since 12
 */
 | 'ohos.permission.CONTROL_LOCATION_SWITCH'
/**
 * @since 12
 */
 | 'ohos.permission.MOCK_LOCATION'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_SCAN_SERVICE'
/**
 * @since 12
 */
 | 'ohos.permission.MICROPHONE_CONTROL'
/**
 * @since 18
 */
 | 'ohos.permission.MICROPHONE_BACKGROUND'
/**
 * @since 12
 */
 | 'ohos.permission.RECEIVE_FUSION_MESSAGES'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_FUSION_MANAGER'
/**
 * @since 12
 */
 | 'ohos.permission.PUBLISH_LOCATION_EVENT'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_MULTICORE_HYBRID_ABILITY'
/**
 * @since 18
 */
 | 'ohos.permission.RECEIVE_BMS_BROKER_MESSAGES'
/**
 * @since 13
 */
 | 'ohos.permission.START_RESTORE_NOTIFICATION'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.CONTROL_LOCATION_SWITCH'
/**
 * @since 23
 */
 | 'ohos.permission.RESTORE_END_NOTIFICATION'
/**
 * @since 13
 */
 | 'ohos.permission.ACCESS_ANALYTICS'
/**
 * @since 13
 */
 | 'ohos.permission.GET_TELEPHONY_ESIM_STATE'
/**
 * @since 13
 */
 | 'ohos.permission.SET_TELEPHONY_ESIM_STATE'
/**
 * @since 13
 */
 | 'ohos.permission.SET_TELEPHONY_ESIM_STATE_OPEN'
/**
 * @since 12
 */
 | 'ohos.permission.INSTALL_INTERNALTESTING_BUNDLE'
/**
 * @since 13
 */
 | 'ohos.permission.CAMERA_BACKGROUND'
/**
 * @since 14
 */
 | 'ohos.permission.ACCESS_VIRTUAL_KEYBOARD'
/**
 * @since 14
 */
 | 'ohos.permission.ACCESS_APP_INSTALL_DIR'
/**
 * @since 14
 */
 | 'ohos.permission.MANAGE_UDMF_APP_SHARE_OPTION'
/**
 * @since 14
 */
 | 'ohos.permission.MANAGE_PASTEBOARD_APP_SHARE_OPTION'
/**
 * @since 15
 */
 | 'ohos.permission.EXEMPT_CAPTURE_SCREEN_AUTHORIZE'
/**
 * @since 15
 */
 | 'ohos.permission.INPUT_KEYBOARD_CONTROLLER'
/**
 * @since 15
 */
 | 'ohos.permission.SET_ABILITY_INSTANCE_INFO'
/**
 * @since 15
 */
 | 'ohos.permission.VIRTUAL_KEYBOARD_WINDOW'
/**
 * @since 18
 */
 | 'ohos.permission.GET_FAMILY_INFO'
/**
 * @since 15
 */
 | 'ohos.permission.PRELOAD_FILE'
/**
 * @since 16
 */
 | 'ohos.permission.ACCESS_VIRTUAL_SCREEN'
/**
 * @since 18
 */
 | 'ohos.permission.ACCESS_ACCOUNT_RECOMMENDATION_DATA'
/**
 * @since 18
 */
 | 'ohos.permission.GET_PAGE_INFO'
/**
 * @since 18
 */
 | 'ohos.permission.ACCESS_DEVAUTH_CRED_MGR'
/**
 * @since 18
 */
 | 'ohos.permission.ACCESS_DEVAUTH_CRED_PRIVILEGE'
/**
 * @since 16
 */
 | 'ohos.permission.FOWNER'
/**
 * @since 18
 */
 | 'ohos.permission.ACCESS_TRUST_LIST_OOBE_MANAGER'
/**
 * @since 18
 */
 | 'ohos.permission.ACCESS_DEVAUTH_CRED_AUTH'
/**
 * @since 19
 */
 | 'ohos.permission.CHANGE_DEFAULT_APPLICATION'
/**
 * @since 18
 */
 | 'ohos.permission.CUSTOM_SANDBOX'
/**
 * @since 19
 */
 | 'ohos.permission.INSTALL_PLUGIN_BUNDLE'
/**
 * @since 19
 */
 | 'ohos.permission.UNINSTALL_PLUGIN_BUNDLE'
/**
 * @since 19
 */
 | 'ohos.permission.kernel.SUPPORT_PLUGIN'
/**
 * @since 20
 */
 | 'ohos.permission.FILE_TRANSFER_OPERATION'
/**
 * @since 20
 */
 | 'ohos.permission.FILE_TRANSFER_INFO_QUERY'
/**
 * @since 20
 */
 | 'ohos.permission.ENTERPRISE_MANAGE_LOCAL_PUBLICSPACES'
/**
 * @since 20
 */
 | 'ohos.permission.ENTERPRISE_FILE_TRANSFER_AUDIT_POLICY_MANAGEMENT'
/**
 * @since 20
 */
 | 'ohos.permission.MANAGE_LOCAL_WORKSPACES'
/**
 * @since 20
 */
 | 'ohos.permission.QUERY_LOCAL_WORKSPACES'
/**
 * @since 23
 */
 | 'ohos.permission.MANAGE_LOCAL_EDUCATION_SPACES'
/**
 * @since 23
 */
 | 'ohos.permission.QUERY_LOCAL_EDUCATION_SPACES'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ACCESS_DLP_SERVICE'
/**
 * @since 14
 */
 | 'ohos.permission.CUSTOM_SCREEN_CAPTURE'
/**
 * @since 7
 */
 | 'ohos.permission.READ_HEALTH_DATA'
/**
 * @since 7
 */
 | 'ohos.permission.MEDIA_LOCATION'
/**
 * @since 7
 */
 | 'ohos.permission.ACTIVITY_MOTION'
/**
 * @since 7
 * @deprecated since 22
 */
 | 'ohos.permission.WRITE_MEDIA'
/**
 * @since 7
 */
 | 'ohos.permission.DISTRIBUTED_DATASYNC'
/**
 * @since 7
 */
 | 'ohos.permission.LOCATION_IN_BACKGROUND'
/**
 * @since 7
 */
 | 'ohos.permission.LOCATION'
/**
 * @since 7
 * @deprecated since 22
 */
 | 'ohos.permission.READ_MEDIA'
/**
 * @since 8
 */
 | 'ohos.permission.RECEIVE_MMS'
/**
 * @since 8
 */
 | 'ohos.permission.RECEIVE_SMS'
/**
 * @since 8
 */
 | 'ohos.permission.MANAGE_VOICEMAIL'
/**
 * @since 8
 */
 | 'ohos.permission.RECEIVE_WAP_MESSAGES'
/**
 * @since 8
 */
 | 'ohos.permission.MICROPHONE'
/**
 * @since 8
 */
 | 'ohos.permission.SEND_MESSAGES'
/**
 * @since 8
 */
 | 'ohos.permission.WRITE_CALENDAR'
/**
 * @since 8
 */
 | 'ohos.permission.WRITE_CALL_LOG'
/**
 * @since 8
 */
 | 'ohos.permission.WRITE_CONTACTS'
/**
 * @since 8
 */
 | 'ohos.permission.READ_MESSAGES'
/**
 * @since 8
 */
 | 'ohos.permission.READ_CELL_MESSAGES'
/**
 * @since 8
 */
 | 'ohos.permission.READ_CONTACTS'
/**
 * @since 8
 */
 | 'ohos.permission.READ_CALL_LOG'
/**
 * @since 24
 */
 | 'ohos.permission.CHECK_CALL_LOG'
/**
 * @since 8
 */
 | 'ohos.permission.READ_CALENDAR'
/**
 * @since 9
 */
 | 'ohos.permission.ANSWER_CALL'
/**
 * @since 9
 */
 | 'ohos.permission.APPROXIMATELY_LOCATION'
/**
 * @since 9
 */
 | 'ohos.permission.CAMERA'
/**
 * @since 9
 */
 | 'ohos.permission.READ_IMAGEVIDEO'
/**
 * @since 9
 */
 | 'ohos.permission.WRITE_IMAGEVIDEO'
/**
 * @since 9
 */
 | 'ohos.permission.WRITE_AUDIO'
/**
 * @since 9
 */
 | 'ohos.permission.WRITE_DOCUMENT'
/**
 * @since 9
 */
 | 'ohos.permission.READ_WHOLE_CALENDAR'
/**
 * @since 9
 */
 | 'ohos.permission.WRITE_WHOLE_CALENDAR'
/**
 * @since 9
 */
 | 'ohos.permission.APP_TRACKING_CONSENT'
/**
 * @since 9
 */
 | 'ohos.permission.READ_AUDIO'
/**
 * @since 9
 */
 | 'ohos.permission.READ_DOCUMENT'
/**
 * @since 10
 */
 | 'ohos.permission.ACCESS_BLUETOOTH'
/**
 * @since 10
 */
 | 'ohos.permission.GET_INSTALLED_BUNDLE_LIST'
/**
 * @since 11
 */
 | 'ohos.permission.READ_PASTEBOARD'
/**
 * @since 11
 */
 | 'ohos.permission.READ_WRITE_DOWNLOAD_DIRECTORY'
/**
 * @since 11
 */
 | 'ohos.permission.READ_WRITE_DOCUMENTS_DIRECTORY'
/**
 * @since 11
 */
 | 'ohos.permission.READ_WRITE_DESKTOP_DIRECTORY'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_NEARLINK'
/**
 * @since 12
 */
 | 'ohos.permission.PRELOAD_APPLICATION'
/**
 * @since 12
 */
 | 'ohos.permission.CAST_AUDIO_OUTPUT'
/**
 * @since 12
 */
 | 'ohos.permission.MANAGE_INPUT_INFRARED_EMITTER'
/**
 * @since 12
 */
 | 'ohos.permission.KILL_APP_PROCESSES'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.START_ABILITY'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.KILL_APP_PROCESSES'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_LOCAL_BACKUP'
/**
 * @since 12
 */
 | 'ohos.permission.PRELOAD_UI_EXTENSION_ABILITY'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_SYSTEM_APP_CERT'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_USER_TRUSTED_CERT'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_SCREEN_LOCK_MEDIA_DATA'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_BOOSTER_SERVICE'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_SCREEN_LOCK_ALL_DATA'
/**
 * @since 12
 */
 | 'ohos.permission.CHECK_QUICKFIX_RESULT'
/**
 * @since 12
 */
 | 'ohos.permission.PROTECT_SCREEN_LOCK_DATA'
/**
 * @since 12
 */
 | 'ohos.permission.WRITE_RINGTONE'
/**
 * @since 12
 */
 | 'ohos.permission.MANAGE_SETTINGS'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_DEVICE_COLLABORATION_PRIVATE_ABILITY'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_DEVICE_COLLABORATION_SERVICE'
/**
 * @since 18
 */
 | 'ohos.permission.ACCESS_FUSION_AWARENESS_DATA'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_FILE_CONTENT_SHARE'
/**
 * @since 12
 */
 | 'ohos.permission.MANAGE_FINDNETWORK'
/**
 * @since 12
 */
 | 'ohos.permission.OPERATE_FINDNETWORK'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_SUBSCRIPTION_CAPSULE_DATA'
/**
 * @since 12
 */
 | 'ohos.permission.QUERY_FINDNETWORK_LOCATION'
/**
 * @since 13
 */
 | 'ohos.permission.REGISTER_FINDNETWORK_ACCESSORY'
/**
 * @since 15
 */
 | 'ohos.permission.MANAGE_SHUTDOWN_FINDNETWORK'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_RINGTONE_RESOURCE'
/**
 * @since 12
 */
 | 'ohos.permission.INJECT_INPUT_EVENT'
/**
 * @since 12
 */
 | 'ohos.permission.QUERY_SECURITY_EVENT'
/**
 * @since 12
 */
 | 'ohos.permission.REPORT_SECURITY_EVENT'
/**
 * @since 12
 */
 | 'ohos.permission.QUERY_SECURITY_MODEL_RESULT'
/**
 * @since 12
 */
 | 'ohos.permission.MANAGE_SECURITY_GUARD_CONFIG'
/**
 * @since 12
 */
 | 'ohos.permission.ALLOW_TIPS_ACCESS'
/**
 * @since 12
 */
 | 'ohos.permission.COLLECT_SECURITY_EVENT'
/**
 * @since 12
 */
 | 'ohos.permission.QUERY_AUDIT_EVENT'
/**
 * @since 12
 */
 | 'ohos.permission.QUERY_SECURITY_POLICY_FROM_CLOUD'
/**
 * @since 12
 */
 | 'ohos.permission.REPORT_SECURITY_EVENT_TO_CLOUD'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_FACTORY_OTA_DIR'
/**
 * @since 12
 */
 | 'ohos.permission.PRE_START_ATOMIC_SERVICE'
/**
 * @since 12
 */
 | 'ohos.permission.FILTER_INPUT_EVENT'
/**
 * @since 12
 */
 | 'ohos.permission.MANAGE_MOUSE_CURSOR'
/**
 * @since 18
 */
 | 'ohos.permission.INPUT_DEVICE_CONTROLLER'
/**
 * @since 12
 */
 | 'ohos.permission.DUMP_AUDIO'
/**
 * @since 12
 */
 | 'ohos.permission.OPEN_FILE'
/**
 * @since 12
 */
 | 'ohos.permission.PROCESS_FILE_COPY_PASTE'
/**
 * @since 12
 */
 | 'ohos.permission.CLEAR_RECYCLEBIN'
/**
 * @since 12
 */
 | 'ohos.permission.GET_FILE_THUMBNAIL'
/**
 * @since 12
 */
 | 'ohos.permission.PUBLISH_DISPLAY_ROTATION_EVENT'
/**
 * @since 12
 */
 | 'ohos.permission.PUBLISH_CAST_PLUGGED_EVENT'
/**
 * @since 12
 */
 | 'ohos.permission.NETWORK_DHCP'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_CAR_DISTRIBUTED_ENGINE'
/**
 * @since 12
 */
 | 'ohos.permission.ALLOW_CONNECT_CAR'
/**
 * @since 12
 */
 | 'ohos.permission.MANAGE_NET_FIREWALL'
/**
 * @since 12
 */
 | 'ohos.permission.GET_NET_FIREWALL'
/**
 * @since 12
 */
 | 'ohos.permission.GET_ALL_PROCESSES'
/**
 * @since 12
 */
 | 'ohos.permission.ACTIVATE_DEVICE_PSI'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_IDM_WIDGET'
/**
 * @since 12
 */
 | 'ohos.permission.MANAGE_ACCESSORY'
/**
 * @since 12
 */
 | 'ohos.permission.COLLECT_ACCESSORY_LOG'
/**
 * @since 13
 */
 | 'ohos.permission.ACCESS_DISTRIBUTED_MODEM'
/**
 * @since 13
 */
 | 'ohos.permission.GET_ETHERNET_LOCAL_MAC'
/**
 * @since 12
 */
 | 'ohos.permission.ALLOW_SHOW_NON_SECURE_WINDOWS'
/**
 * @since 12
 */
 | 'ohos.permission.GRANT_SHORT_TERM_WRITE_MEDIAVIDEO'
/**
 * @since 13
 */
 | 'ohos.permission.CALLED_TRANSITION_ON_LOCK_SCREEN'
/**
 * @since 13
 */
 | 'ohos.permission.CALLED_BELOW_LOCK_SCREEN'
/**
 * @since 13
 */
 | 'ohos.permission.WINDOW_TOPMOST'
/**
 * @since 12
 */
 | 'ohos.permission.ACCESS_SUPER_HUB'
/**
 * @since 13
 */
 | 'ohos.permission.READ_WRITE_USB_DEV'
/**
 * @since 13
 */
 | 'ohos.permission.USER_AUTH_FROM_BACKGROUND'
/**
 * @since 13
 */
 | 'ohos.permission.READ_WRITE_USER_FILE'
/**
 * @since 14
 */
 | 'ohos.permission.READ_WEATHER_DATA'
/**
 * @since 14
 */
 | 'ohos.permission.CALLED_UIEXTENSION_ON_LOCK_SCREEN'
/**
 * @since 14
 */
 | 'ohos.permission.MANAGE_APP_KEEP_ALIVE'
/**
 * @since 13
 */
 | 'ohos.permission.READ_APP_LOCK'
/**
 * @since 13
 */
 | 'ohos.permission.WRITE_APP_LOCK'
/**
 * @since 13
 */
 | 'ohos.permission.ACCESS_APP_LOCK'
/**
 * @since 13
 */
 | 'ohos.permission.ACCESS_CAR_CONTROL'
/**
 * @since 15
 */
 | 'ohos.permission.ACCESS_APP_SINGLE_PERMISSION_MANAGEMENT'
/**
 * @since 16
 */
 | 'ohos.permission.MANAGE_APN_SETTING'
/**
 * @since 20
 */
 | 'ohos.permission.ACCESS_NET_TRACE_INFO'
/**
 * @since 20
 */
 | 'ohos.permission.LINKTURBO'
/**
 * @since 14
 */
 | 'ohos.permission.kernel.DISABLE_CODE_MEMORY_PROTECTION'
/**
 * @since 14
 */
 | 'ohos.permission.kernel.ALLOW_WRITABLE_CODE_MEMORY'
/**
 * @since 18
 */
 | 'ohos.permission.CAPTURE_PLAYBACK'
/**
 * @since 13
 */
 | 'ohos.permission.ENABLE_EXPERIENCE_HBM'
/**
 * @since 18
 */
 | 'ohos.permission.ANTI_FRAUD'
/**
 * @since 18
 */
 | 'ohos.permission.ACCESS_ENTERPRISE_USER_TRUSTED_CERT'
/**
 * @since 18
 */
 | 'ohos.permission.USE_USER_ACCESS_MANAGER'
/**
 * @since 14
 */
 | 'ohos.permission.kernel.ALLOW_EXECUTABLE_FORT_MEMORY'
/**
 * @since 15
 */
 | 'ohos.permission.ACCESS_ACCOUNT_SERVICE_EXTENSION_ABILITY'
/**
 * @since 15
 */
 | 'ohos.permission.NDK_START_SELF_UI_ABILITY'
/**
 * @since 18
 */
 | 'ohos.permission.SEND_NOTIFICATION_CROSS_USER'
/**
 * @since 16
 */
 | 'ohos.permission.kernel.ALLOW_USE_JITFORT_INTERFACE'
/**
 * @since 17
 */
 | 'ohos.permission.kernel.DISABLE_GOTPLT_RO_PROTECTION'
/**
 * @since 18
 */
 | 'ohos.permission.ALLOW_ACCESS_TIPS'
/**
 * @since 18
 */
 | 'ohos.permission.GET_DOMAIN_ACCOUNT_SERVER_CONFIGS'
/**
 * @since 18
 */
 | 'ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS'
/**
 * @since 18
 */
 | 'ohos.permission.MANAGE_DOMAIN_ACCOUNTS'
/**
 * @since 18
 */
 | 'ohos.permission.SET_LAUNCH_REASON_MESSAGE'
/**
 * @since 18
 */
 | 'ohos.permission.LOCATION_SWITCH_IGNORED'
/**
 * @since 18
 */
 | 'ohos.permission.GET_ANIM_POLICY'
/**
 * @since 18
 */
 | 'ohos.permission.ACCESS_DLP_HIDE_INFO'
/**
 * @since 18
 */
 | 'ohos.permission.DLP_GET_HIDE_STATUS'
/**
 * @since 18
 */
 | 'ohos.permission.WATCH_READ_EMERGENCY_INFO'
/**
 * @since 18
 */
 | 'ohos.permission.WATCH_WRITE_EMERGENCY_INFO'
/**
 * @since 18
 */
 | 'ohos.permission.WATCH_START_SOS_SERVICE'
/**
 * @since 15
 */
 | 'ohos.permission.SET_PAC_URL'
/**
 * @since 18
 */
 | 'ohos.permission.GET_SIGNATURE_INFO'
/**
 * @since 15
 */
 | 'ohos.permission.ACCESS_DISK_PHY_INFO'
/**
 * @since 18
 */
 | 'ohos.permission.ACCESS_USER_ACCOUNT_INFO'
/**
 * @since 18
 */
 | 'ohos.permission.ACCESS_STARTUPGUIDE'
/**
 * @since 18
 */
 | 'ohos.permission.ANTIFRAUD_DETECT'
/**
 * @since 18
 */
 | 'ohos.permission.ACCESS_APP_CLONE_DIR'
/**
 * @since 18
 */
 | 'ohos.permission.ANTIFRAUD_PICTURE_DETECT'
/**
 * @since 18
 */
 | 'ohos.permission.ANTIFRAUD_MODEL_DOWNLOAD'
/**
 * @since 23
 */
 | 'ohos.permission.ANTIFRAUD_VOICE_DETECT'
/**
 * @since 17
 */
 | 'ohos.permission.ACCESS_MEDIALIB_RESTORE'
/**
 * @since 19
 */
 | 'ohos.permission.UPDATE_FONT'
/**
 * @since 18
 */
 | 'ohos.permission.VISIBLE_WINDOW_INFO'
/**
 * @since 18
 */
 | 'ohos.permission.ACCESS_CUSTOM_RINGTONE'
/**
 * @since 18
 */
 | 'ohos.permission.GET_EDM_CONFIG'
/**
 * @since 18
 */
 | 'ohos.permission.READ_DLP_HIDE_SWITCH'
/**
 * @since 18
 */
 | 'ohos.permission.WRITE_DLP_HIDE_SWITCH'
/**
 * @since 18
 */
 | 'ohos.permission.UNLOCK_DEVELOPER_MODE'
/**
 * @since 20
 */
 | 'ohos.permission.ENTERPRISE_ACCESS_DLP_FILE'
/**
 * @since 20
 */
 | 'ohos.permission.SET_NET_EXT_ATTRIBUTE'
/**
 * @since 20
 */
 | 'ohos.permission.PARENT_CONTROL_UI'
/**
 * @since 20
 */
 | 'ohos.permission.PARENT_CONTROL_SERVICE'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.MINORS_PROTECTION_UI'
/**
 * @since 17
 */
 | 'ohos.permission.ACCESS_CALENDARDATA_FOR_BROKER'
/**
 * @since 18
 */
 | 'ohos.permission.READ_DHA'
/**
 * @since 18
 */
 | 'ohos.permission.WRITE_DHA'
/**
 * @since 18
 */
 | 'ohos.permission.NOTIFY_DHA'
/**
 * @since 17
 */
 | 'ohos.permission.GET_FILE_ICON'
/**
 * @since 20
 */
 | 'ohos.permission.CUSTOMIZE_SAVE_BUTTON'
/**
 * @since 23
 */
 | 'ohos.permission.HIVIEW_TRACE_MANAGE'
/**
 * @since 20
 */
 | 'ohos.permission.MANAGE_SCREEN_TIME_GUARD'
/**
 * @since 20
 */
 | 'ohos.permission.RESTORE_APP'
/**
 * @since 17
 */
 | 'ohos.permission.SANDBOX_ACCESS_MANAGER'
/**
 * @since 20
 */
 | 'ohos.permission.BACKGROUND_MANAGER_POWER_SAVE_MODE'
/**
 * @since 20
 */
 | 'ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY'
/**
 * @since 19
 */
 | 'ohos.permission.READ_PARENT_CONTROL_DATA'
/**
 * @since 19
 */
 | 'ohos.permission.WRITE_PARENT_CONTROL_DATA'
/**
 * @since 20
 */
 | 'ohos.permission.REQUEST_DISABLE_NOTIFICATION'
/**
 * @since 20
 */
 | 'ohos.permission.NETWORK_SIMULATE'
/**
 * @since 20
 */
 | 'ohos.permission.ALLOW_IOURING'
/**
 * @since 20
 */
 | 'ohos.permission.GET_ABILITY_INFO'
/**
 * @since 20
 */
 | 'ohos.permission.kernel.AUTH_AUDIT_EVENT'
/**
 * @since 20
 */
 | 'ohos.permission.SUPPORT_APP_SERVICE_EXTENSION'
/**
 * @since 20
 */
 | 'ohos.permission.kernel.ALLOW_APP_CODE_DECRYPT'
/**
 * @since 20
 */
 | 'ohos.permission.GRANT_URI_PERMISSION_AS_CALLER'
/**
 * @since 20
 */
 | 'ohos.permission.ACCESS_FIDO2_ONLINEAUTH'
/**
 * @since 20
 */
 | 'ohos.permission.ACCESS_FIDO2_ONLINEAUTH_PRIVILEGE'
/**
 * @since 20
 */
 | 'ohos.permission.SUPPORT_INSTALL_ON_U1'
/**
 * @since 20
 */
 | 'ohos.permission.GET_ENTERPRISE_CONFIG'
/**
 * @since 20
 */
 | 'ohos.permission.VIRUS_PROTECTION_SERVICE'
/**
 * @since 20
 */
 | 'ohos.permission.UPLOAD_SAMPLE_FILE'
/**
 * @since 20
 */
 | 'ohos.permission.DOWNLOAD_POLICY_FILE'
/**
 * @since 20
 */
 | 'ohos.permission.NOTIFY_VIRUS_PROTECTION'
/**
 * @since 20
 */
 | 'ohos.permission.MANAGE_ANTIVIRUS'
/**
 * @since 20
 */
 | 'ohos.permission.REGISTER_ANTIVIRUS'
/**
 * @since 20
 */
 | 'ohos.permission.MANAGE_PREINSTALLED_ANTIVIRUS'
/**
 * @since 20
 */
 | 'ohos.permission.ACCESS_VIRUS_PROTECTION'
/**
 * @since 20
 */
 | 'ohos.permission.ENTERPRISE_MANAGE_EAP'
/**
 * @since 20
 */
 | 'ohos.permission.ACCESS_TVCOOPERATION'
/**
 * @since 20
 */
 | 'ohos.permission.DETECT_GESTURE'
/**
 * @since 20
 */
 | 'ohos.permission.USE_FLOAT_BALL'
/**
 * @since 24
 */
 | 'ohos.permission.AUTO_RESTORE_MAIN_WINDOW'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.FLOAT_VIEW'
/**
 * @since 20
 */
 | 'ohos.permission.THEME_SKIN'
/**
 * @since 20
 */
 | 'ohos.permission.PUBLISH_FORM_CROSS_BUNDLE'
/**
 * @since 20
 */
 | 'ohos.permission.CLOUD_ROM_UPDATE'
/**
 * @since 20
 */
 | 'ohos.permission.MOUNT_HDCDEBUG_PATH'
/**
 * @since 20
 */
 | 'ohos.permission.ACCESS_CAMERA_SCENARIOS_CARD'
/**
 * @since 20
 */
 | 'ohos.permission.CALL_TPM_CMD'
/**
 * @since 20
 */
 | 'ohos.permission.atomicService.MANAGE_STORAGE'
/**
 * @since 20
 */
 | 'ohos.permission.TRIGGER_LOCAL_WANTAGENT'
/**
 * @since 20
 */
 | 'ohos.permission.FILE_ACCESS_FOR_PRIVATE_SPACE'
/**
 * @since 20
 */
 | 'ohos.permission.ENTERPRISE_MANAGE_USER_GRANT_PERMISSION'
/**
 * @since 20
 */
 | 'ohos.permission.kernel.NET_RAW'
/**
 * @since 20
 */
 | 'ohos.permission.kernel.DEBUGGER'
/**
 * @since 20
 */
 | 'ohos.permission.kernel.ALLOW_DEBUG'
/**
 * @since 20
 */
 | 'ohos.permission.READ_LOCAL_DEVICE_NAME'
/**
 * @since 20
 */
 | 'ohos.permission.SET_WINDOW_TRANSPARENT'
/**
 * @since 19
 */
 | 'ohos.permission.ACCESS_DFX_LOG_DIR'
/**
 * @since 20
 */
 | 'ohos.permission.kernel.IGNORE_LIBRARY_VALIDATION'
/**
 * @since 20
 */
 | 'ohos.permission.kernel.LOAD_INDEPENDENT_LIBRARY'
/**
 * @since 20
 */
 | 'ohos.permission.GET_SCREEN_CONTENT'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ONSCREEN_AWARENESS'
/**
 * @since 20
 */
 | 'ohos.permission.ACCESS_DISTRIBUTED_KEY_STORE'
/**
 * @since 20
 */
 | 'ohos.permission.SIMULATE_USER_INPUT'
/**
 * @since 19
 */
 | 'ohos.permission.SANDBOX_ACCESS_MANAGER_EXT'
/**
 * @since 20
 */
 | 'ohos.permission.KEEP_BACKGROUND_RUNNING_SYSTEM'
/**
 * @since 23
 */
 | 'ohos.permission.GET_BACKGROUND_TASK_INFO'
/**
 * @since 23
 */
 | 'ohos.permission.SET_BACKGROUND_TASK_STATE'
/**
 * @since 20
 */
 | 'ohos.permission.ACCESS_MAPDATA_DIR'
/**
 * @since 20
 */
 | 'ohos.permission.CONNECT_MECHANIC_HARDWARE'
/**
 * @since 20
 */
 | 'ohos.permission.kernel.READ_PROTECT_RANGE'
/**
 * @since 20
 */
 | 'ohos.permission.REPORT_POWER_SCENE_EVENT'
/**
 * @since 20
 */
 | 'ohos.permission.ENTERPRISE_WORKSPACES_EVENT_SUBSCRIBE'
/**
 * @since 20
 */
 | 'ohos.permission.GET_DEVICE_INDEPENDENT_BINARY_CERT'
/**
 * @since 21
 */
 | 'ohos.permission.HOOK_KEY_EVENT'
/**
 * @since 20
 */
 | 'ohos.permission.SET_DEVICE_INDEPENDENT_BINARY_CERT_STATUS'
/**
 * @since 20
 */
 | 'ohos.permission.MEMOSPACE_SYNC'
/**
 * @since 20
 */
 | 'ohos.permission.ACCESS_PICKER_SHIELD_ANIMATE'
/**
 * @since 20
 */
 | 'ohos.permission.READ_IOT_DEVICE_BASIC_DATA'
/**
 * @since 20
 */
 | 'ohos.permission.READ_IOT_DEVICE_PRIVATE_DATA'
/**
 * @since 13
 */
 | 'ohos.permission.CAPTURE_SCREEN_ALL'
/**
 * @since 21
 */
 | 'ohos.permission.ENTERPRISE_DATA_IDENTIFY_FILE'
/**
 * @since 23
 */
 | 'ohos.permission.ENTERPRISE_MANAGE_DEVICE_ADMIN'
/**
 * @since 23
 */
 | 'ohos.permission.ENTERPRISE_READ_LOG'
/**
 * @since 23
 */
 | 'ohos.permission.ENTERPRISE_START_ABILITIES'
/**
 * @since 23
 */
 | 'ohos.permission.ENTERPRISE_DEACTIVATE_DEVICE_ADMIN'
/**
 * @since 21
 */
 | 'ohos.permission.START_WINDOW_BELOW_LOCK_SCREEN'
/**
 * @since 21
 */
 | 'ohos.permission.READ_DIAGNOSTIC_LOGS'
/**
 * @since 21
 */
 | 'ohos.permission.SET_SYSTEMSHARE_APPLAUNCHTRUSTLIST'
/**
 * @since 22
 */
 | 'ohos.permission.ACCESS_USER_FULL_DISK'
/**
 * @since 22
 */
 | 'ohos.permission.INJECT_PLAYBACK_TO_AUDIO_CAPTURE'
/**
 * @since 21
 */
 | 'ohos.permission.WEB_NATIVE_MESSAGING'
/**
 * @since 22
 */
 | 'ohos.permission.TIMEOUT_SCREENOFF_DISABLE_LOCK'
/**
 * @since 21
 */
 | 'ohos.permission.ACCESS_CLOUD_DISK_INFO'
/**
 * @since 22
 */
 | 'ohos.permission.ACCESS_XR_GLASSES'
/**
 * @since 22
 */
 | 'ohos.permission.DATA_IDENTIFY_ANONYMIZE'
/**
 * @since 22
 */
 | 'ohos.permission.CUSTOM_SCREEN_RECORDING'
/**
 * @since 22
 */
 | 'ohos.permission.LOCK_WINDOW_CURSOR'
/**
 * @since 22
 */
 | 'ohos.permission.SUBSCRIBE_NOTIFICATION'
/**
 * @since 22
 */
 | 'ohos.permission.MANAGE_SELF_SKILLS'
/**
 * @since 23
 */
 | 'ohos.permission.ALLOW_EXTERNAL_NATIVE_CODE'
/**
 * @since 22
 */
 | 'ohos.permission.vehicle.VEHICLE_CDM_READ'
/**
 * @since 22
 */
 | 'ohos.permission.vehicle.VEHICLE_CDM_WRITE'
/**
 * @since 22
 */
 | 'ohos.permission.MANAGE_DYNAMIC_UTD_TYPE'
/**
 * @since 22
 */
 | 'ohos.permission.GET_IP_MAC_INFO'
/**
 * @since 23
 */
 | 'ohos.permission.CUSTOMIZE_MENU_ICON'
/**
 * @since 22
 */
 | 'ohos.permission.ACCESS_ANCO_APP_DATA'
/**
 * @since 23
 */
 | 'ohos.permission.kernel.EXEMPT_ANONYMOUS_EXECUTABLE_MEMORY'
/**
 * @since 23
 */
 | 'ohos.permission.INHERIT_PARENT_PERMISSION'
/**
 * @since 24
 */
 | 'ohos.permission.DATACLONE_ACCESS_FILE_MANAGER'
/**
 * @since 23
 */
 | 'ohos.permission.atomicService.MANAGE_AGING'
/**
 * @since 23
 */
 | 'ohos.permission.PUBLISH_FORM_CROSS_BUNDLE_CONTROL'
/**
 * @since 23
 */
 | 'ohos.permission.ALLOW_COREDUMP'
/**
 * @since 23
 */
 | 'ohos.permission.MANAGE_MEDIA_RESOURCES_FOR_PUBLIC'
/**
 * @since 23
 */
 | 'ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME'
/**
 * @since 23
 */
 | 'ohos.permission.MANAGE_MEDIA_SHARED_RESOURCE'
/**
 * @since 23
 */
 | 'ohos.permission.MANAGE_CLOUD_DATA_SERVICE'
/**
 * @since 23
 */
 | 'ohos.permission.GET_DONOTDISTURB_STATE'
/**
 * @since 23
 */
 | 'ohos.permission.MANAGE_RISK_PHOTOS'
/**
 * @since 23
 */
 | 'ohos.permission.MANAGE_CALL_FOR_DEVICES'
/**
 * @since 23
 */
 | 'ohos.permission.ACCESS_SECURE_FENCE'
/**
 * @since 23
 */
 | 'ohos.permission.READ_CLOUD_IMAGEVIDEO'
/**
 * @since 23
 */
 | 'ohos.permission.ACCESS_MINI_SYSTEM'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.QUERY_TOOL_PERMISSIONS'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.MANAGE_TOOL_RUNTIME_PERMISSIONS'
/**
 * @since 23
 */
 | 'ohos.permission.MANAGE_STANDBY'
/**
 * @since 23
 */
 | 'ohos.permission.ACCESS_STANDBY'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.vehicle.CAR_MODE_MANAGEMENT'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.vehicle.AUTO_UPDATER'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ACCESS_CAR_AUDIO'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.GET_LOCAL_ACCOUNT_IDENTIFIERS'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.DLP_POLICY_MANAGER'
/**
 * @since 24
 */
 | 'ohos.permission.SCAN_REMEDIATE_VIRUS'
/**
 * @since 24
 */
 | 'ohos.permission.ASSET_CACHE_MANAGER'
/**
 * @since 24
 */
 | 'ohos.permission.GET_AGENT_CARD'
/**
 * @since 24
 */
 | 'ohos.permission.CONNECT_AGENT'
/**
 * @since 24
 */
 | 'ohos.permission.CONNECT_OBJECTEDITOR_EXTENSION'
/**
 * @since 24
 */
 | 'ohos.permission.KEEP_BACKGROUND_RUNNING_SPECIAL_SCENARIO'
/**
 * @since 24
 */
 | 'ohos.permission.REGISTER_OBJECTEDITOR_EXTENSION'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.POWER_CONFIG'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.REVOKE_FILE_ACCESS_PERSIST'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ACCESS_SHARED_FILE'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.GET_FILE_ACCESS_PERSIST'
/**
 * @since 24
 */
 | 'ohos.permission.HDR_BRIGHTNESS'
/**
 * @since 24
 */
 | 'ohos.permission.INPUT_DEVICE_CONFIGURATOR'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.MODIFY_AGENT_CARD'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.GET_TICKET_INFO'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.START_ABILITY_TO_PAGE'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.SET_WINDOW_TOUCH_AREAS'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.READ_APP_PROTECTION_RECORD'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.CONTROL_DEVICE'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.WRITE_APP_PROTECTION_RECORD'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.CLI_MANAGE_WEB_SANDBOX'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.QUERY_CLI_TOOL'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.EXEC_CLI_TOOL'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ACCESS_FUNCTION'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.READ_SPAM_SHIELD_SETTING'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.WRITE_SPAM_SHIELD_SETTING'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ACCESS_DEVELOPER_PCAP_SWITCH'
/**
 * @since 24
 */
 | 'ohos.permission.EXEMPT_MOTION_SENSORS_RESTRICTION'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.NOTIFICATION_SYSTEM_SUBSCRIBER'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ALLOW_ACCESSORY_ACCESS'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.DCAS_RUN_MODEL'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.EXECUTE_DISTRIBUTED_INTENT'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ENTERPRISE_GET_INSTALLED_BUNDLE_LIST'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ACCESS_SUPPORT_FEEDBACK'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ACCESS_SUPPORT_HELP'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.MANAGE_AOD'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.DCAS_OTA_PERMISSION'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ACCESS_DIGITAL_IDENTITY_ABILITY'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.SUPPORT_CROSS_APP_EMBED_FOR_OA'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.MANAGE_VOLUME_ENCRYPTION_POLICY'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.QUERY_VOLUME_ENCRYPTION_STATUS'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.kernel.LOAD_CERTSIGN_LIBRARY_FOR_WEB'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.SUPPORT_NP_PLUGIN_FOR_WEB'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.LOAD_NATIVE_LIBRARY'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.KNOCK_COLLABORATION'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.CONNECT_GAME_ACCELERATION'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.GET_CALL_TRANSFER_INFO'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.MANAGE_SKILL_PRIVILEGE'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.MANAGE_SKILL'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.kernel.AS_LDK_DRIVER'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ACCESS_INTIMATE_RELATION_INFO'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.MANAGE_WIFI_TOGGLE'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.MANAGE_WIFI_SCAN'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.MANAGE_WIFI_CONNECT'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ENABLE_AGENT_PERMISSION_MGR'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.MANAGE_NFC_SWITCH'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.SET_HOTSPOT'
/**
 * @since 24
 */
 | 'ohos.permission.ACCESS_DEVICE_INTERCONNECTIVITY'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.cli.GET_HOTSPOT'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.CROSS_OS_INTERCONNECT'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.TV_MANAGE_SOURCE'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.TV_MANAGE_PICTURE_QUALITY'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.TV_GET_AUDIO_DEVICE_INFO'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.TV_SET_AUDIO_DEVICE_INFO'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.TV_MANAGE_SOUND_EFFECT'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.TV_MANAGE_AI_AQ'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.TV_MANAGE_CEC'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.TV_CAMERA_AI'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.TV_DIAGNOSIS'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.TV_ACCESS_PROJECTION'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.TV_MANAGE_LOGSYNC'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.automotive.SET_ADAS_CMD'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.automotive.GET_ADAS_INFO'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.automotive.GET_CLUSTER_INFO'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.automotive.SET_CLUSTER_CMD'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.automotive.SET_MMS_CMD'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.automotive.GET_MMS_INFO'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.automotive.GET_XCALL_INFO'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.automotive.SET_XCALL_CMD'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.automotive.SET_SECBOX_CMD'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.automotive.GET_SECBOX_INFO'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.automotive.RECV_HUAP_INFO'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.automotive.SEND_HUAP_MSG'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.TV_ACCESSORY_MANAGE'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.kernel.TRAFFIC_FILTER'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.QUERY_SPACE_OPTIMIZATION'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.vehicle.VEHICLE_THERMAL'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.MANAGE_AUDIO_ACCESSORY'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.kernel.SUPPORT_LOCAL_PLUGIN'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ACCESS_GAME_BUDDY_SERVICE'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ARKWEBCORE_SYS_CAP'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.SUBSCRIBE_OUTDOOR_EXPLORATION_SERVICE'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ENTERPRISE_VPN'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.CREATE_SIGN_CONTENT_TRUST'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.APPEND_SIGN_CONTENT_TRUST'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ACCESS_DIGITAL_IDENTITY'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.UPDATE_FORM_CROSS_BUNDLE'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.HDC_REPORT_INFO'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ACCESS_ASSOCIATE_ASSISTANT'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.CAPTURE_PLAYBACK_DOWNLINK'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.UPDATE_TIPS_STATUS'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ENTERPRISE_SPACE_FILE_TRANSFER_DATA_ACCESS'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.MANAGE_SANDBOX_BUNDLE'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.ACCESS_SE_KEY'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.DETECT_DEVICE'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.AGENT_FILE_ACCESS'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.MUTE_VOIP_CAPTURE'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.MUTE_VOIP_PLAYBACK'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.VOIP_CAPTURE_CONCURRENCY'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.SAMBA_CLIENT_ACCESS'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.FILE_MANAGER_SERVICE_ACCESS'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.FILE_MANAGER_SERVICE_SMART_FILE_ACCESS'
/**
 * @since 26.0.0
 */
 | 'ohos.permission.FILE_MANAGER_SERVICE_DATA_ACCESS';

```
