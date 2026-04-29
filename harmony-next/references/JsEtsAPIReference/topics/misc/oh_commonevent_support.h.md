# oh_commonevent_support.h

**概述**

提供系统定义的公共事件常量。

库： libohcommonevent.so

引用文件： <BasicServicesKit/oh_commonevent_support.h>

系统能力： SystemCapability.Notification.CommonEvent

起始版本： 12

相关模块： [OH_CommonEvent](OH_CommonEvent.md)

**汇总**

**常量**

| 名称 | 描述 |
| --- | --- |
| static const char * const COMMON_EVENT_SHUTDOWN = "usual.event.SHUTDOWN" | 表示设备正在关闭并将继续直至最终关闭的公共事件。 起始版本： 12 系统能力： SystemCapability.Notification.CommonEvent |
| static const char * const COMMON_EVENT_BATTERY_CHANGED = "usual.event.BATTERY_CHANGED" | 表示电池充电状态、电平和其他信息发生变化的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_BATTERY_LOW = "usual.event.BATTERY_LOW" | 表示电池电量低的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_BATTERY_OKAY = "usual.event.BATTERY_OKAY" | 表示电池退出低电平状态的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_POWER_CONNECTED = "usual.event.POWER_CONNECTED" | 表示设备连接到外部电源的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_POWER_DISCONNECTED = "usual.event.POWER_DISCONNECTED" | 表示设备与外部电源断开的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_SCREEN_OFF = "usual.event.SCREEN_OFF" | 表示设备屏幕关闭且设备处于睡眠状态的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_SCREEN_ON = "usual.event.SCREEN_ON" | 表示设备屏幕打开且设备处于交互状态的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_ENTER_HIBERNATE = "usual.event.ENTER_HIBERNATE" | 表示设备即将进入休眠模式的公共事件的动作。 起始版本： 15 |
| static const char * const COMMON_EVENT_EXIT_HIBERNATE = "usual.event.EXIT_HIBERNATE" | 表示设备退出休眠模式的公共事件的动作。 起始版本： 15 |
| static const char * const COMMON_EVENT_THERMAL_LEVEL_CHANGED = "usual.event.THERMAL_LEVEL_CHANGED" | 表示设备热状态的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_TIME_TICK = "usual.event.TIME_TICK" | 表示系统时间更改的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_TIME_CHANGED = "usual.event.TIME_CHANGED" | 表示设置系统时间的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_TIMEZONE_CHANGED = "usual.event.TIMEZONE_CHANGED" | 表示系统时区更改的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_PACKAGE_ADDED = "usual.event.PACKAGE_ADDED" | 表示设备上已安装新应用包的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_PACKAGE_REMOVED = "usual.event.PACKAGE_REMOVED" | 表示已从设备卸载已安装的应用程序，但应用程序数据保留的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_BUNDLE_REMOVED = "usual.event.BUNDLE_REMOVED" | 表示已从设备中卸载已安装的捆绑包，但应用程序数据仍保留的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_PACKAGE_FULLY_REMOVED = "usual.event.PACKAGE_FULLY_REMOVED" | 表示已从设备中完全卸载已安装的应用程序（包括应用程序数据和代码）的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_PACKAGE_CHANGED = "usual.event.PACKAGE_CHANGED" | 表示应用包已更改的公共事件（例如，包中的组件已启用或禁用）。 起始版本： 12 |
| static const char * const COMMON_EVENT_PACKAGE_RESTARTED = "usual.event.PACKAGE_RESTARTED" | 表示用户重启应用包并杀死其所有进程的普通事件的动作。 起始版本： 12 |
| static const char * const COMMON_EVENT_PACKAGE_DATA_CLEARED = "usual.event.PACKAGE_DATA_CLEARED" | 表示用户清除应用包数据的公共事件的动作。 起始版本： 12 |
| static const char * const COMMON_EVENT_PACKAGE_CACHE_CLEARED = "usual.event.PACKAGE_CACHE_CLEARED" | 表示用户清除应用包缓存数据的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_PACKAGES_SUSPENDED = "usual.event.PACKAGES_SUSPENDED" | 表示应用包已挂起的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_MY_PACKAGE_SUSPENDED = "usual.event.MY_PACKAGE_SUSPENDED" | 表示应用包被挂起的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_MY_PACKAGE_UNSUSPENDED = "usual.event.MY_PACKAGE_UNSUSPENDED" | 表示应用包未挂起的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_LOCALE_CHANGED = "usual.event.LOCALE_CHANGED" | 表示设备区域设置已更改的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_MANAGE_PACKAGE_STORAGE = "usual.event.MANAGE_PACKAGE_STORAGE" | 表示设备存储空间不足的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_USER_UNLOCKED = "usual.event.USER_UNLOCKED" | 表示设备重启后解锁时，当前用户的凭据加密存储已解锁的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGOUT = "common.event.DISTRIBUTED_ACCOUNT_LOGOUT" | 表示分布式账号登出成功的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_DISTRIBUTED_ACCOUNT_TOKEN_INVALID = "common.event.DISTRIBUTED_ACCOUNT_TOKEN_INVALID" | 表示分布式账号token令牌无效的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGOFF = "common.event.DISTRIBUTED_ACCOUNT_LOGOFF" | 表示分布式账号注销的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_WIFI_POWER_STATE = "usual.event.wifi.POWER_STATE" | 表示Wi-Fi状态公共事件，如启用和禁用。 起始版本： 12 |
| static const char * const COMMON_EVENT_WIFI_SCAN_FINISHED = "usual.event.wifi.SCAN_FINISHED" | 表示Wi-Fi接入点已被扫描并证明可用的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_WIFI_RSSI_VALUE = "usual.event.wifi.RSSI_VALUE" | 表示Wi-Fi信号强度（RSSI）改变的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_WIFI_CONN_STATE = "usual.event.wifi.CONN_STATE" | 表示Wi-Fi连接状态发生改变的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_WIFI_HOTSPOT_STATE = "usual.event.wifi.HOTSPOT_STATE" | 表示Wi-Fi热点状态的公共事件，如启用或禁用。 起始版本： 12 |
| static const char * const COMMON_EVENT_WIFI_AP_STA_JOIN = "usual.event.wifi.WIFI_HS_STA_JOIN" | 表示客户端加入当前设备Wi-Fi热点的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_WIFI_AP_STA_LEAVE = "usual.event.wifi.WIFI_HS_STA_LEAVE" | 表示客户端已断开与当前设备Wi-Fi热点的连接的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_WIFI_MPLINK_STATE_CHANGE = "usual.event.wifi.mplink.STATE_CHANGE" | 表示MPLink（增强Wi-Fi功能）状态已更改的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_WIFI_P2P_CONN_STATE = "usual.event.wifi.p2p.CONN_STATE_CHANGE" | 表示Wi-Fi P2P连接状态改变的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_WIFI_P2P_STATE_CHANGED = "usual.event.wifi.p2p.STATE_CHANGE" | 表示Wi-Fi P2P状态公共事件，如启用和禁用。 起始版本： 12 |
| static const char * const COMMON_EVENT_WIFI_P2P_PEERS_STATE_CHANGED = "usual.event.wifi.p2p.DEVICES_CHANGE" | 表示Wi-Fi P2P对等体状态变化的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_WIFI_P2P_PEERS_DISCOVERY_STATE_CHANGED = "usual.event.wifi.p2p.PEER_DISCOVERY_STATE_CHANGE" | 表示Wi-Fi P2P发现状态变化的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_WIFI_P2P_CURRENT_DEVICE_STATE_CHANGED = "usual.event.wifi.p2p.CURRENT_DEVICE_CHANGE" | 表示Wi-Fi P2P当前设备状态变化的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_WIFI_P2P_GROUP_STATE_CHANGED = "usual.event.wifi.p2p.GROUP_STATE_CHANGED" | 表示Wi-Fi P2P群组信息已更改的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_NFC_ACTION_ADAPTER_STATE_CHANGED = "usual.event.nfc.action.ADAPTER_STATE_CHANGED" | 表示设备NFC状态已更改的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_NFC_ACTION_RF_FIELD_ON_DETECTED = "usual.event.nfc.action.RF_FIELD_ON_DETECTED" | 表示检测到NFC场强进入的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_NFC_ACTION_RF_FIELD_OFF_DETECTED = "usual.event.nfc.action.RF_FIELD_OFF_DETECTED" | 表示检测到NFC场强离开的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_DISCHARGING = "usual.event.DISCHARGING" | 表示系统停止为电池充电的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_CHARGING = "usual.event.CHARGING" | 表示系统开始为电池充电的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_DEVICE_IDLE_MODE_CHANGED = "usual.event.DEVICE_IDLE_MODE_CHANGED" | 表示系统待机空闲模式已更改的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_CHARGE_IDLE_MODE_CHANGED = "usual.event.CHARGE_IDLE_MODE_CHANGED" | 表示设备进入充电空闲模式的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_POWER_SAVE_MODE_CHANGED = "usual.event.POWER_SAVE_MODE_CHANGED" | 表示系统节能模式更改的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_USB_STATE = "usual.event.hardware.usb.action.USB_STATE" | 表示USB设备状态发生变化的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_USB_PORT_CHANGED = "usual.event.hardware.usb.action.USB_PORT_CHANGED" | 表示用户设备的USB端口状态发生改变的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_USB_DEVICE_ATTACHED = "usual.event.hardware.usb.action.USB_DEVICE_ATTACHED" | 当用户设备作为USB主机时，USB设备已挂载的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_USB_DEVICE_DETACHED = "usual.event.hardware.usb.action.USB_DEVICE_DETACHED" | 当用户设备作为USB主机时，USB设备被卸载的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_AIRPLANE_MODE_CHANGED = "usual.event.AIRPLANE_MODE" | 表示设备飞行模式已更改的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_SPLIT_SCREEN = "common.event.SPLIT_SCREEN" | 表示分屏的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_QUICK_FIX_APPLY_RESULT = "usual.event.QUICK_FIX_APPLY_RESULT" | 表示快速修复应用的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_QUICK_FIX_REVOKE_RESULT = "usual.event.QUICK_FIX_REVOKE_RESULT" | 表示撤销快速修复的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_USER_INFO_UPDATED = "usual.event.USER_INFO_UPDATED" | 表示用户信息已更新的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_SIM_STATE_CHANGED = "usual.event.SIM_STATE_CHANGED" | 表示SIM卡状态更新的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_CALL_STATE_CHANGED = "usual.event.CALL_STATE_CHANGED" | 表示呼叫状态更新的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_NETWORK_STATE_CHANGED = "usual.event.NETWORK_STATE_CHANGED" | 表示网络状态更新的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_SIGNAL_INFO_CHANGED = "usual.event.SIGNAL_INFO_CHANGED" | 表示信号信息更新的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_SCREEN_UNLOCKED = "usual.event.SCREEN_UNLOCKED" | 表示屏幕解锁的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_SCREEN_LOCKED = "usual.event.SCREEN_LOCKED" | 表示屏幕锁定的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_HTTP_PROXY_CHANGE = "usual.event.HTTP_PROXY_CHANGE" | 表示HTTP代理的配置信息发生变化的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_CONNECTIVITY_CHANGE = "usual.event.CONNECTIVITY_CHANGE" | 表示网络连接状态变化的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_MINORSMODE_ON = "usual.event.MINORSMODE_ON" | 表示未成年人模式开启的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_MINORSMODE_OFF = "usual.event.MINORSMODE_OFF" | 表示未成年人模式关闭的公共事件。 起始版本： 12 |
| static const char * const COMMON_EVENT_MANAGED_BROWSER_POLICY_CHANGED = "usual.event.MANAGED_BROWSER_POLICY_CHANGED" | 表示浏览器托管策略已更改。 起始版本： 15 |
| static const char* const COMMON_EVENT_TABLET_MODE_CHANGED = "usual.event.TABLET_MODE_CHANGED" | 表示可感知支架开合的设备，其支架开合状态变化的公共事件。 起始版本： 23 |
| static const char* const COMMON_EVENT_LID_STATE_CHANGED = "usual.event.LID_STATE_CHANGED" | 表示可感知开合盖子的设备，其开合盖状态变化的公共事件。 起始版本： 23 |