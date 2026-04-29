# @ohos.settings (设置数据项名称)

本模块提供访问设置数据项的能力。

-

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

如果访问的数据项没有获取到值，表示当前系统应用没有将该数据项的值添加到数据库。

#### 导入模块

```ets
import { settings } from '@kit.BasicServicesKit';
```

#### domainName

提供查询的域名。

#### 常量

**系统能力：** SystemCapability.Applications.Settings.Core

| 名称 | 类型 | 只读 | 说明 |
| --- | --- | --- | --- |
| DEVICE_SHARED11+ | string | 是 | 设备属性共享域，所有设置项不区分多用户。 |
| USER_PROPERTY11+ | string | 是 | 为用户属性域，该域下所有配置区分多用户。 |

#### date

提供设置时间和日期格式的数据项。

#### 常量

**系统能力：** SystemCapability.Applications.Settings.Core

| 名称 | 类型 | 只读 | 说明 |
| --- | --- | --- | --- |
| DATE_FORMAT(deprecated21) | string | 是 | 日期格式。 日期格式包括mm/dd/yyyy、dd/mm/yyyy和yyyy/mm/dd，其中mm、dd和yyyy分别代表月份、日期和年份（该常量不支持使用）。 |
| TIME_FORMAT | string | 是 | 时间以12小时格式或24小时格式显示。 - 值为 "12"表示12小时格式。 - 值为"24"表示24小时格式。 |
| AUTO_GAIN_TIME(deprecated21) | string | 是 | 是否自动从网络获取日期、时间和时区。  - 值为true，表示自动从网络获取信息。 - 值为false，表示不自动获取信息（该常量不支持使用）。 |
| AUTO_GAIN_TIME_ZONE(deprecated21) | string | 是 | 是否自动从NITZ获取时区。  - 值为true，表示自动获取。 - 值为false，表示不自动获取（该常量不支持使用）。 |

#### display

提供设置显示效果的数据项。

#### 常量

**系统能力：** SystemCapability.Applications.Settings.Core

| 名称 | 类型 | 只读 | 说明 |
| --- | --- | --- | --- |
| FONT_SCALE | string | 是 | （domainName为USER_PROPERTY）字体的比例因子，值为固定浮点数。标准档位取值为1，其他档位包括0.85、1.15、1.3、1.45。关怀模式下，额外提供1.75、2、3.2档位。 |
| SCREEN_BRIGHTNESS_STATUS | string | 是 | 屏幕亮度。取值范围:0到255。 |
| AUTO_SCREEN_BRIGHTNESS | string | 是 | 是否启用屏幕亮度自动调整。 - 值为AUTO_SCREEN_BRIGHTNESS_MODE，表示启用自动调整。 - 值为MANUAL_SCREEN_BRIGHTNESS_MODE，表示不启用自动调整。 |
| AUTO_SCREEN_BRIGHTNESS_MODE | number | 是 | 使用屏幕亮度自动调整时AUTO_SCREEN_BRIGHTNESS的值。 |
| MANUAL_SCREEN_BRIGHTNESS_MODE | number | 是 | 使用屏幕亮度手动调整时的AUTO_SCREEN_BRIGHTNESS值。 |
| SCREEN_OFF_TIMEOUT | string | 是 | 设备在一段时间不活动后进入睡眠状态的等待时间（单位: ms）。 |
| DEFAULT_SCREEN_ROTATION(deprecated21) | string | 是 | 启用屏幕的自动旋转时，此属性无效。不启用自动旋转时，以下值可用:  - 值为0，表示屏幕旋转0度。 - 值为1，表示屏幕旋转90度。 - 值为2，表示屏幕旋转180度。 - 值为3，表示屏幕旋转270度（该常量不支持使用）。 |
| ANIMATOR_DURATION_SCALE(deprecated21) | string | 是 | 动画持续时间的比例因子，影响所有此类动画的开始延迟和持续时间。 值为0，表示动画将立即结束。默认值为1（该常量不支持使用）。 |
| TRANSITION_ANIMATION_SCALE(deprecated21) | string | 是 | 过渡动画的比例因子。 值为0，表示禁用过渡动画（该常量不支持使用）。 |
| WINDOW_ANIMATION_SCALE(deprecated21) | string | 是 | 普通窗口动画的比例因子。 值为0，表示禁用窗口动画（该常量不支持使用）。 |
| DISPLAY_INVERSION_STATUS(deprecated21) | string | 是 | 是否启用显示颜色反转。 - 值为1，表示启用显示颜色反转。 - 值为0，表示不启用显示颜色反转（该常量不支持使用）。 |

#### general

提供设置设备常规信息的数据项。

#### 常量

**系统能力：** SystemCapability.Applications.Settings.Core

| 名称 | 类型 | 只读 | 说明 |
| --- | --- | --- | --- |
| SETUP_WIZARD_FINISHED(deprecated21) | string | 是 | 是否已运行启动向导。 - 值为0，表示启动向导尚未运行。 - 值为非0，表示启动向导已运行（该常量不支持使用）。 |
| END_BUTTON_ACTION(deprecated21) | string | 是 | 当用户不在呼叫中时，由用户按下呼叫结束按钮后会发生的情况。 - 值为0，表示没有任何反应。 - 值为1，表示显示主屏幕。 - 值为2，表示设备进入睡眠状态，屏幕锁定。 - 值为3，表示显示主屏幕。如果用户已在主屏幕上，设备将进入睡眠状态（该常量不支持使用）。 |
| ACCELEROMETER_ROTATION_STATUS | string | 是 | 是否启用加速计更改屏幕方向（是否启用自动旋转）。 - 值为1，表示启用加速计。 - 值为0，表示不启用加速计。 |
| DEVICE_PROVISION_STATUS(deprecated21) | string | 是 | 是否预配设备。 在具有单个系统用户的多用户设备上，当值为true时，屏幕可能会被锁定。此外，其他功能无法在系统用户上启动，除非被标记在屏幕锁定上显示（该常量不支持使用）。 |
| HDC_STATUS(deprecated21) | string | 是 | 是否启用USB设备上的HDC（硬盘控制器）。 - 值为true，表示启用HDC。 - 值为false，表示不启用HDC（该常量不支持使用）。 |
| BOOT_COUNTING(deprecated21) | string | 是 | 设备开机后的启动操作数（该常量不支持使用）。 |
| CONTACT_METADATA_SYNC_STATUS(deprecated21) | string | 是 | 是否启用联系人元数据同步。 - 值为true，表示启用同步。 - 值为false，表示不启用同步（该常量不支持使用）。 |
| DEVICE_NAME | string | 是 | 设备名称。 |
| USB_STORAGE_STATUS(deprecated21) | string | 是 | 是否启用USB大容量存储。 - 值为true，表示启用USB大容量存储。 - 值为false，表示不启用USB大容量存储（该常量不支持使用）。 |
| DEBUGGER_WAITING(deprecated21) | string | 是 | 设备在启动应用程序进行调试时是否等待调试器进行调试。 - 值为1，表示设备等待调试器。 - 值为0，表示系统不会等待调试器，应用程序正常运行（该常量不支持使用）。 |
| DEBUG_APP_PACKAGE(deprecated21) | string | 是 | 要调试的应用程序的bundle name（该常量不支持使用）。 |
| ACCESSIBILITY_STATUS(deprecated21) | string | 是 | 是否启用辅助功能。 - 值为1，表示启用辅助功能。 - 值为0，表示不启用辅助功能（该常量不支持使用）。 |
| ACTIVATED_ACCESSIBILITY_SERVICES(deprecated21) | string | 是 | 已激活的辅助功能的列表（该常量不支持使用）。 |
| GEOLOCATION_ORIGINS_ALLOWED(deprecated21) | string | 是 | 浏览器可以使用的默认地理位置。多个地理位置由空格分隔（该常量不支持使用）。 |
| SKIP_USE_HINTS(deprecated21) | string | 是 | 控制应用程序首次启动时是否跳过所有介绍性提示。适用于临时用户或熟悉环境的用户。 - 值为1，表示应用程序将在首次启动时跳过所有介绍性提示。 - 值为0，表示应用程序不会在首次启动时跳过所有介绍性提示（该常量不支持使用）。 |
| TOUCH_EXPLORATION_STATUS(deprecated21) | string | 是 | 是否启用触摸浏览。 - 值为1，表示启用触摸浏览。 - 值为0，表示不启用触摸浏览（该常量不支持使用）。 |

#### input

提供设置有关输入法信息的数据项。

#### 常量

**系统能力：** SystemCapability.Applications.Settings.Core

| 名称 | 类型 | 只读 | 说明 |
| --- | --- | --- | --- |
| DEFAULT_INPUT_METHOD(deprecated21) | string | 是 | 默认输入法及其ID（该常量不支持使用）。 |
| ACTIVATED_INPUT_METHOD_SUB_MODE | string | 是 | 默认输入法键盘类型及其ID。 |
| ACTIVATED_INPUT_METHODS(deprecated21) | string | 是 | 已激活的输入法的列表。 该列表是一个字符串，由已激活的输入法ID和输入法键盘类型组成。 输入法ID后添加冒号':'连接，输入法的键盘类型后添加分号';'连接。 用ima代表输入法ID，keyboardType代表键盘类型，示例格式是ima0:keyboardType0;keyboardType1;ima1:ima2:keyboardTypes0（该常量不支持使用）。 |
| SELECTOR_VISIBILITY_FOR_INPUT_METHOD(deprecated21) | string | 是 | 输入法选择器是否可见。 - 值为1，表示输入法选择器可见。 - 值为0，表示输入法选择器不可见（该常量不支持使用）。 |
| AUTO_CAPS_TEXT_INPUT(deprecated21) | string | 是 | 是否为文本编辑器启用自动大写。 - 值为0，表示不启用自动大写。 - 值为1，表示启用自动大写（该常量不支持使用）。 |
| AUTO_PUNCTUATE_TEXT_INPUT(deprecated21) | string | 是 | 是否为文本编辑器启用自动标点符号。自动标点符号使文本编辑器能够将两个空格转换为句点'.'和空格。 - 值为0，表示不启用自动标点符号。 - 值为1，表示启用自动标点符号（该常量不支持使用）。 |
| AUTO_REPLACE_TEXT_INPUT(deprecated21) | string | 是 | 是否为文本编辑器启用自动更正。自动更正使文本编辑器能够更正拼写错误。 - 值为0，表示不启用自动更正。 - 值为1，表示启用自动更正（该常量不支持使用）。 |
| SHOW_PASSWORD_TEXT_INPUT(deprecated21) | string | 是 | 是否在文本编辑器中启用密码显示。密码显示使文本编辑器能够在用户键入密码字符时显示密码字符。 - 值为0，表示不启用密码显示。 - 值为1，表示启用密码显示（该常量不支持使用）。 |

#### network

提供设置网络信息的数据项。

#### 常量

**系统能力：** SystemCapability.Applications.Settings.Core

| 名称 | 类型 | 只读 | 说明 |
| --- | --- | --- | --- |
| DATA_ROAMING_STATUS(deprecated21) | string | 是 | 是否启用数据漫游。 - 值为true，表示启用数据漫游。 - 值为false，表示不启用数据漫游（该常量不支持使用）。 |
| HTTP_PROXY_CFG(deprecated21) | string | 是 | 全局HTTP代理的主机名和端口号。主机名和端口号由冒号':'分隔（该常量不支持使用）。 |
| NETWORK_PREFERENCE_USAGE(deprecated21) | string | 是 | 要使用网络的用户首选项（该常量不支持使用）。 |

#### phone

提供设置来电和去电接听方式的数据项。

#### 常量

**系统能力：** SystemCapability.Applications.Settings.Core

| 名称 | 类型 | 只读 | 说明 |
| --- | --- | --- | --- |
| RTT_CALLING_STATUS(deprecated21) | string | 是 | 是否启用实时文本（RTT）呼叫。启用表示来电和去电在设备以及运营商支持时作为RTT呼叫应答。  - 值为1，表示启用RTT呼叫。  - 值为0，表示不启用RTT呼叫（该常量不支持使用）。 |

#### sound

提供设置声音效果的数据项。

#### 常量

**系统能力：** SystemCapability.Applications.Settings.Core

| 名称 | 类型 | 只读 | 说明 |
| --- | --- | --- | --- |
| VIBRATE_WHILE_RINGING(deprecated21) | string | 是 | 设备在来电响铃时是否振动。此属性由电话和设置应用程序使用。 该值仅影响设备因来电而响铃的情况，不影响任何其他应用程序或场景（该常量不支持使用）。 |
| DEFAULT_ALARM_ALERT(deprecated21) | string | 是 | 系统默认告警的存储区域（该常量不支持使用）。 |
| DTMF_TONE_TYPE_WHILE_DIALING(deprecated21) | string | 是 | 拨号时播放的双音多频（DTMF）音的类型。  - 值为0，表示常规的短音效。 - 值为1，表示长音效（该常量不支持使用）。 |
| DTMF_TONE_WHILE_DIALING(deprecated21) | string | 是 | 拨号时是否播放DTMF音。 - 值为1，表示播放DTMF音。 - 值为0，表示不播放（该常量不支持使用）。 |
| AFFECTED_MODE_RINGER_STREAMS(deprecated21) | string | 是 | 音频流受振铃模式和请勿打扰（DND）模式更改的影响。要求特定的音频流受到振铃模式和DND模式变化的影响，将对应比特位设置为1（该常量不支持使用）。 |
| AFFECTED_MUTE_STREAMS(deprecated21) | string | 是 | 受静音模式影响的音频流。若需在静音模式下保持特定音频流静音，将相应位设为1（该常量不支持使用）。 |
| DEFAULT_NOTIFICATION_SOUND(deprecated21) | string | 是 | 系统默认通知音的存储区域（该常量不支持使用）。 |
| DEFAULT_RINGTONE(deprecated21) | string | 是 | 系统默认铃声的存储区域（该常量不支持使用）。 |
| SOUND_EFFECTS_STATUS(deprecated21) | string | 是 | 声音功能是否可用。 - 值为0，表示不可用。  - 值为1，表示可用（该常量不支持使用）。 |
| VIBRATE_STATUS(deprecated21) | string | 是 | 设备是否为事件振动。该参数在系统内部使用。  - 值为1，表示设备会因事件而振动。  - 值为0，表示设备不因事件振动（该常量不支持使用）。 |
| HAPTIC_FEEDBACK_STATUS(deprecated21) | string | 是 | 设备是否启用触觉反馈。 - 值为true，表示启用触觉反馈。 - 值为false，表示不启用触觉反馈（该常量不支持使用）。 |

#### TTS

提供设置文本到语音(TTS)转换信息的数据项。

#### 常量

**系统能力：** SystemCapability.Applications.Settings.Core

| 名称 | 类型 | 只读 | 说明 |
| --- | --- | --- | --- |
| DEFAULT_TTS_PITCH(deprecated21) | string | 是 | 文本转语音(TTS)引擎的默认音高。 其中100=1x，该值设置为200，表示频率是正常声音频率的两倍（该常量不支持使用）。 |
| DEFAULT_TTS_RATE(deprecated21) | string | 是 | TTS引擎的默认语速。 其中100=1x（该常量不支持使用）。 |
| DEFAULT_TTS_SYNTH(deprecated21) | string | 是 | 默认TTS引擎（该常量不支持使用）。 |
| ENABLED_TTS_PLUGINS(deprecated21) | string | 是 | 用于TTS的已激活插件包列表，多个插件包用空格分隔（该常量不支持使用）。 |

#### wireless

提供设置无线网络信息的数据项。

#### 常量

**系统能力：** SystemCapability.Applications.Settings.Core

| 名称 | 类型 | 只读 | 说明 |
| --- | --- | --- | --- |
| BLUETOOTH_DISCOVER_ABILITY_STATUS(deprecated21) | string | 是 | 设备是否可以被其他设备通过蓝牙发现或连接。 - 值为0，表示设备不可以被连接或发现。 - 值为1，表示设备可以被连接但不可以被发现。 - 值为2，表示设备可以被连接和发现（该常量不支持使用）。 |
| BLUETOOTH_DISCOVER_TIMEOUT(deprecated21) | string | 是 | 通过蓝牙发现设备的持续时间（以秒为单位）。 这段时间后，设备不可以被蓝牙搜寻到（该常量不支持使用）。 |
| AIRPLANE_MODE_RADIOS(deprecated21) | string | 是 | 启用飞行模式时要禁用的无线电信号列表。  多个无线电信号用逗号(,)分隔。 取值包括以下常量：BLUETOOTH_RADIO、 CELL_RADIO、 NFC_RADIO、 WIFI_RADIO（该常量不支持使用）。 |
| BLUETOOTH_RADIO(deprecated21) | string | 是 | 常量，作为AIRPLANE_MODE_RADIOS的取值时表示蓝牙在飞行模式下禁用（该常量不支持使用）。 |
| CELL_RADIO(deprecated21) | string | 是 | 常量，作为AIRPLANE_MODE_RADIOS的取值时表示蜂窝无线电在飞行模式下禁用（该常量不支持使用）。 |
| NFC_RADIO(deprecated21) | string | 是 | 常量，作为AIRPLANE_MODE_RADIOS的取值时表示NFC在飞行模式下禁用（该常量不支持使用）。 |
| WIFI_RADIO(deprecated21) | string | 是 | 常量，作为AIRPLANE_MODE_RADIOS的取值时表示Wi-Fi在飞行模式下禁用（该常量不支持使用）。 |
| BLUETOOTH_STATUS(deprecated21) | string | 是 | 蓝牙是否可用。  - 值为true，表示蓝牙可用。 - 值为false，表示蓝牙不可用（该常量不支持使用）。 |
| OWNER_LOCKDOWN_WIFI_CFG(deprecated21) | string | 是 | 是否应锁定由设备所有者的应用程序创建的Wi-Fi配置。 - 值为true，表示Wi-Fi配置应该被锁定。 - 值为false，表示不应该被锁定（该常量不支持使用）。 |
| WIFI_DHCP_MAX_RETRY_COUNT(deprecated21) | string | 是 | 尝试从DHCP服务器获取IP地址的最大次数（该常量不支持使用）。 |
| WIFI_TO_MOBILE_DATA_AWAKE_TIMEOUT(deprecated21) | string | 是 | Wi-Fi连接断开后等待移动数据连接时保持唤醒锁的最长时间（该常量不支持使用）。 |
| WIFI_STATUS(deprecated21) | string | 是 | Wi-Fi是否可用。 - 值为true，表示Wi-Fi可用。 - 值为false，表示Wi-Fi不可用（该常量不支持使用）。 |
| WIFI_WATCHDOG_STATUS(deprecated21) | string | 是 | Wi-Fi的WatchDog是否可用。  - 值为true，表示可用。 - 值为false，表示不可用（该常量不支持使用）。 |

#### settings.setValue10+

setValue(context: Context, name: string, value: string, callback: AsyncCallback<boolean>): void

将数据项名称及数据项的值保存到DEVICE_SHARED域数据库中，使用callback异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Applications.Settings.Core

**需要权限**： ohos.permission.MANAGE_SETTINGS，仅系统应用可用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文（仅支持UIAbilityContext和ExtensionContext）。 Stage模型的应用Context定义见Context。 |
| name | string | 是 | 数据项的名称。数据项名称分为以下两种： - 上述任意一个数据库中已存在的数据项。 - 开发者自行添加的数据项。 |
| value | string | 是 | 数据项值。取值范围随业务变动。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示操作成功，返回false表示操作失败。 |

**示例**：

```ets
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 更新数据项亮度的值(该数据项在数据库中已存在，故setValue方法将更新该数据项的值)。
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.setValue(context, settings.display.SCREEN_BRIGHTNESS_STATUS, '100', (status) => {
  console.info('Callback return whether value is set.');
});
```

#### settings.setValue10+

setValue(context: Context, name: string, value: string): Promise<boolean>

将数据项名称及数据项的值保存到DEVICE_SHARED域数据库中。使用Promise异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Applications.Settings.Core

**需要权限**： ohos.permission.MANAGE_SETTINGS，该权限仅系统应用可用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文（仅支持UIAbilityContext和ExtensionContext）。 Stage模型的应用Context定义见Context。 |
| name | string | 是 | 数据项的名称。数据项名称分为以下两种： - 上述任意一个数据库中已存在的数据项。 - 开发者自行添加的数据项。 |
valuestring是数据项值。取值范围随业务变动。

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示操作成功，返回false表示操作失败。 |

**示例**：

```ets
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 更新数据项亮度的值(该数据项在数据库中已存在，故setValue方法将更新该数据项的值)。
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.setValue(context, settings.display.SCREEN_BRIGHTNESS_STATUS, '100').then((status) => {
  console.info('Callback return whether value is set.');
});
```

#### settings.setValue11+

setValue(context: Context, name: string, value: string, domainName: string): Promise<boolean>

将数据项名称及数据项的值保存到数据库中。使用Promise异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Applications.Settings.Core

**需要权限**：

- 写入DEVICE_SHARED、USER_PROPERTY域需要权限ohos.permission.MANAGE_SETTINGS，该权限仅系统应用可用。
- 写入USER_SECURITY域需要权限ohos.permission.MANAGE_SECURE_SETTINGS，该权限仅系统应用可用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文（仅支持UIAbilityContext和ExtensionContext）。 Stage模型的应用Context定义见Context。 |
| name | string | 是 | 数据项的名称。数据项名称分为以下两种： - 上述任意一个数据库中已存在的数据项。 - 开发者自行添加的数据项。 |
| value | string | 是 | 数据项值。取值范围随业务变动。 |
| domainName | string | 是 | 指定要设置的域名。  - domainName为domainName.DEVICE_SHARED,  表示设备属性共享域。 - domainName为domainName.USER_PROPERTY,  表示用户属性域。  - domainName为domainName.USER_SECURITY,  表示用户安全属性域(仅对系统应用开放)。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示操作成功，返回false表示操作失败。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例**：

```ets
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 更新数据项亮度的值(该数据项在数据库中已存在，故setValue方法将更新该数据项的值)。
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.setValue(context, settings.display.SCREEN_BRIGHTNESS_STATUS, '100', settings.domainName.DEVICE_SHARED).then((status) => {
  console.info(`callback:return whether value is set.`)
});
```

#### settings.getValue10+

getValue(context: Context, name: string, callback: AsyncCallback<string>): void

获取数据库中DEVICE_SHARD域指定数据项的值。使用callback异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Applications.Settings.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文（仅支持UIAbilityContext和ExtensionContext）。 Stage模型的应用Context定义见Context。 |
| name | string | 是 | 数据项的名称。数据项名称分为以下两种： - 上述任意一个数据库中已存在的数据项。 - 开发者自行添加的数据项。 |
callbackAsyncCallback<string>是使用callback方式获取数据项的值。

**示例**：

```ets
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.getValue(context, settings.display.SCREEN_BRIGHTNESS_STATUS, (err, value) => {
  if (err) {
    console.error(`Failed to get the setting. ${err.message} `);
    return;
  }
  console.info(`callback:value -> ${value}`)
});
```

#### settings.getValue10+

getValue(context: Context, name: string): Promise<string>

获取数据库中DEVICE_SHARD域指定数据项的值。使用Promise异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Applications.Settings.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文（仅支持UIAbilityContext和ExtensionContext）。 Stage模型的应用Context定义见Context。 |
| name | string | 是 | 数据项的名称。数据项名称分为以下两种： - 上述任意一个数据库中已存在的数据项。 - 开发者自行添加的数据项。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回获得的数据项的值。 |

**示例**：

```ets
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.getValue(context, settings.display.SCREEN_BRIGHTNESS_STATUS).then((value) => {
  console.info(`promise:value -> ${value}`)
});
```

#### settings.getValue11+

getValue(context: Context, name: string, domainName: string): Promise<string>

获取数据库中指定数据项的值。使用Promise异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Applications.Settings.Core

**需要权限**：

- 读取USER_SECURITY域需要权限ohos.permission.MANAGE_SECURE_SETTINGS，该权限仅系统应用可用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文（仅支持UIAbilityContext和ExtensionContext）。 Stage模型的应用Context定义见Context。 |
| name | string | 是 | 数据项的名称。数据项名称分为以下两种： - 上述任意一个数据库中已存在的数据项。 - 开发者自行添加的数据项。 |
| domainName | string | 是 | 指定要设置的域名。  - domainName为domainName.DEVICE_SHARED,  设备属性共享域。 - domainName为domainName.USER_PROPERTY,  表示为用户属性域。  - domainName为domainName.USER_SECURITY,  表示为用户安全属性域(仅对系统应用开放)。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回获得的数据项的值。 |

**示例**：

```ets
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 更新数据项亮度的值(该数据项在数据库中已存在，故getValue方法将更新该数据项的值)。
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.getValue(context, settings.display.SCREEN_BRIGHTNESS_STATUS, settings.domainName.DEVICE_SHARED).then((value) => {
  console.info(`Promise:value -> ${value}`);
});
```

#### settings.getValueSync10+

getValueSync(context: Context, name: string, defValue: string): string

获取数据库中DEVICE_SHARED域指定数据项的值。此方法相较getValue为同步方法。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Applications.Settings.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文（仅支持UIAbilityContext和ExtensionContext）。 Stage模型的应用Context定义见Context。 |
| name | string | 是 | 数据项的名称。数据项名称分为以下两种： - 上述任意一个数据库中已存在的数据项。 - 开发者自行添加的数据项。 |
defValuestring是默认值。由开发者设置，在数据库中查询不到该数据时，返回默认值。

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 返回数据项的值。 |

**示例**：

```ets
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取数据项亮度的值(该数据项在数据库中已存在)。
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let value = settings.getValueSync(context, settings.display.SCREEN_BRIGHTNESS_STATUS, '10');
```

#### settings.getValueSync11+

getValueSync(context: Context, name: string, defValue: string, domainName: string): string

获取数据项的值。此方法相较getValue为同步方法。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Applications.Settings.Core

**需要权限**：

- 读取USER_SECURITY域需要权限ohos.permission.MANAGE_SECURE_SETTINGS，该权限仅系统应用可用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文（仅支持UIAbilityContext和ExtensionContext）。 Stage模型的应用Context定义见Context。 |
| name | string | 是 | 数据项的名称。数据项名称分为以下两种： - 上述任意一个数据库中已存在的数据项。 - 开发者自行添加的数据项。 |
| defValue | string | 是 | 默认值。由开发者设置，在数据库中查询不到该数据时，返回默认值。 |
| domainName | string | 是 | 指定要设置的域名。  - domainName为domainName.DEVICE_SHARED,  设备属性共享域。 - domainName为domainName.USER_PROPERTY,  表示为用户属性域。  - domainName为domainName.USER_SECURITY,  表示为用户安全属性域(仅对系统应用开放)。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 返回数据项的值。 |

**示例**：

```ets
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 更新数据项亮度的值(该数据项在数据库中已存在)。
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let value = settings.getValueSync(context, settings.display.SCREEN_BRIGHTNESS_STATUS, '100',  settings.domainName.DEVICE_SHARED);
```

#### settings.setValueSync10+

setValueSync(context: Context, name: string, value: string): boolean

将数据项名称及数据项的值保存到DEVICE_SHARED域数据库中。此方法相较setValue为同步方法。

- 如果数据库中已经存在该数据项，setValueSync方法将更新该数据项的值。
- 如果数据库中不存在该数据项，setValueSync方法将向数据库中插入该数据项。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Applications.Settings.Core

**需要权限**： ohos.permission.MANAGE_SETTINGS，该权限仅系统应用可用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文（仅支持UIAbilityContext和ExtensionContext）。 Stage模型的应用Context定义见Context。 |
| name | string | 是 | 数据项的名称。数据项名称分为以下两种： - 上述任意一个数据库中已存在的数据项。 - 开发者自行添加的数据项。 |
valuestring是数据项的具体数值。取值范围随业务变动。

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 返回设置数据项的值是否成功的结果。true表示设置成功，false表示设置失败。 |

**示例**：

```ets
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 更新数据项亮度的值(该数据项在数据库中已存在，故setValueSync方法将更新该数据项的值)。
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let ret = settings.setValueSync(context, settings.display.SCREEN_BRIGHTNESS_STATUS, '100');
```

#### settings.setValueSync11+

setValueSync(context: Context, name: string, value: string, domainName: string): boolean

设置数据项的值。此方法相较setValue为同步方法。

- 如果数据库中已经存在该数据项，则setValueSync方法将更新该数据项的值。
- 如果数据库中尚未存在该数据项，则setValueSync方法将向数据库中插入该数据项。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Applications.Settings.Core

**需要权限**：

- 写入DEVICE_SHARED、USER_PROPERTY域需要权限ohos.permission.MANAGE_SETTINGS，该权限仅系统应用可用。
- 写入USER_SECURITY域需要权限ohos.permission.MANAGE_SECURE_SETTINGS，该权限仅系统应用可用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文（仅支持UIAbilityContext和ExtensionContext）。 Stage模型的应用Context定义见Context。 |
| name | string | 是 | 数据项的名称。数据项名称分为以下两种： - 上述任意一个数据库中已存在的数据项。 - 开发者自行添加的数据项。 |
| value | string | 是 | 数据项值。取值范围随业务变动。 |
| domainName | string | 是 | 指定要设置的域名。  - domainName为domainName.DEVICE_SHARED,  设备属性共享域。 - domainName为domainName.USER_PROPERTY,  表示为用户属性域。  - domainName为domainName.USER_SECURITY,  表示为用户安全属性域(仅对系统应用开放)。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 返回设置数据项的值是否成功的结果。true表示设置成功，false表示设置失败。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例**：

```ets
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 更新数据项亮度的值(该数据项在数据库中已存在，故setValueSync方法将更新该数据项的值)。
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let ret = settings.setValueSync(context, settings.display.SCREEN_BRIGHTNESS_STATUS, '100', settings.domainName.DEVICE_SHARED);
```

#### settings.registerKeyObserver11+

registerKeyObserver(context: Context, name: string, domainName: string, observer:AsyncCallback<void>): boolean

用于在指定上下文中注册一个观察者，以便在指定域名中观察指定的数据项。当该数据项的值发生变化时，将调用注册的回调函数。成功注册返回true，否则返回false。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Applications.Settings.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文（仅支持UIAbilityContext和ExtensionContext）。 Stage模型的应用Context定义见Context。 |
| name | string | 是 | 数据项的名称。数据项名称分为以下两种： - 上述任意一个数据库中已存在的数据项。 - 开发者自行添加的数据项。 |
| domainName | string | 是 | 指定要设置的域名。  - domainName为domainName.DEVICE_SHARED,  设备属性共享域。 - domainName为domainName.USER_PROPERTY,  表示为用户属性域。  - domainName为domainName.USER_SECURITY,  表示为用户安全属性域(仅对系统应用开放)。 |
observerAsyncCallback<void>是使用callback方式获取数据项的值。

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 返回注册观察者是否成功的结果。true表示注册成功，false表示注册失败。 |

**示例**：

```ets
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.registerKeyObserver(context, settings.display.SCREEN_BRIGHTNESS_STATUS, settings.domainName.DEVICE_SHARED, () => {
  let value:string = settings.getValueSync(context, settings.display.SCREEN_BRIGHTNESS_STATUS, '10');
  console.info(`Promise:value -> ${value}`);
});
```

#### settings.unregisterKeyObserver11+

unregisterKeyObserver(context: Context, name: string, domainName: string): boolean

同步方法，注销指定域名下对指定数据项名称的观察者。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Applications.Settings.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文（仅支持UIAbilityContext和ExtensionContext）。 Stage模型的应用Context定义见Context。 |
| name | string | 是 | 数据项的名称。数据项名称分为以下两种： - 上述任意一个数据库中已存在的数据项。 - 开发者自行添加的数据项。 |
| domainName | string | 是 | 指定要设置的域名。  - domainName为domainName.DEVICE_SHARED,  设备属性共享域。 - domainName为domainName.USER_PROPERTY,  表示为用户属性域。  - domainName为domainName.USER_SECURITY,  表示为用户安全属性域(仅对系统应用开放) |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 返回注销指定域名下指定键的监视器是否成功。true表示注销成功，false表示注销失败。 |

**示例**：

```ets
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let ret = settings.unregisterKeyObserver(context, settings.display.SCREEN_BRIGHTNESS_STATUS,  settings.domainName.DEVICE_SHARED);
```

#### settings.openNetworkManagerSettings18+

openNetworkManagerSettings(context: Context): Promise<boolean>

打开WLAN设置弹窗。使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Settings.Core

**设备行为差异**：该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备调用不生效。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文（仅支持UIAbilityContext和ExtensionContext）。 Stage模型的应用Context定义见Context。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示操作成功，返回false表示操作失败。 |

**错误码**：

以下错误码详细介绍请参考[设置数据项错误码]([设置数据项错误码](../../errors/设置数据项错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800000 | Parameter error. |
| 14800010 | Original service error. |

**示例**：

```ets
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 跳转网络管理器设置页面。
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.openNetworkManagerSettings(context).then((status) => {
  console.info(`callback:return whether settings is open.`);
});
```

#### settings.enableAirplaneMode

enableAirplaneMode(enable: boolean, callback: AsyncCallback<void>): void

启用或禁用飞行模式。使用callback异步回调（暂不支持）。

**系统能力**：SystemCapability.Applications.Settings.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否开启飞行模式。true表示开启，false表示禁用。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例**：

```ets
let isEnabled :boolean = true;
settings.enableAirplaneMode(isEnabled, (err:Error) => {
    if (err) {
        console.error('Failed to enable AirplaneMode.');
        return;
    }
    console.info('Return true if enable.');
})
```

#### settings.enableAirplaneMode

enableAirplaneMode(enable: boolean): Promise<void>

启用或禁用飞行模式。使用Promise异步回调（暂不支持）。

**系统能力**：SystemCapability.Applications.Settings.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否开启飞行模式。true表示开启，false表示禁用。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例**：

```ets
let isEnabled :boolean = true;
settings.enableAirplaneMode(isEnabled).then(() => {
  console.info('Succeeded in enabling AirplaneMode.');
}).catch((err:Error) => {
  console.error(`Failed to enable AirplaneMode. Cause: ${err}`);
})
```

#### settings.canShowFloating

canShowFloating(callback: AsyncCallback<boolean>): void

检查应用是否能够以悬浮窗形式显示。使用callback异步回调（暂不支持）。

**系统能力**：SystemCapability.Applications.Settings.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。 返回true，表示应用能够以悬浮窗形式显示。返回false，表示不能。 |

**示例**：

```ets
settings.canShowFloating((err:Error, status: boolean) => {
  if (err) {
    console.error(`Failed to Checks whether a specified application can show as float window ${err.message} `);
    return;
  }
  console.info('Checks whether a specified application can show as float window.');
});
```

#### settings.canShowFloating

canShowFloating(): Promise<boolean>

检查应用是否能够以悬浮窗形式显示。使用Promise异步回调（暂不支持）。

**系统能力**：SystemCapability.Applications.Settings.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。 返回true，表示应用能够以悬浮窗形式显示。返回false，表示不能。 |

**示例**：

```ets
settings.canShowFloating().then((status:boolean) => {
    console.info('Checks whether a specified application can show as float window.');
});
```

#### settings.getUriSync8+

getUriSync(name: string): string

获取数据项的URI（暂不支持）。

**系统能力**：SystemCapability.Applications.Settings.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 数据项的名称。数据项名称分为以下两种： - 上述任意一个数据库中已存在的数据项。 - 开发者自行添加的数据项。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 数据项的URI。 |

**示例**：

```ets
// 获取数据项的URI。
let uriVar:string = settings.getUriSync(settings.display.SCREEN_BRIGHTNESS_STATUS);
```

#### settings.getURI(deprecated)

getURI(name: string, callback: AsyncCallback<object>): void

获取数据项的URI。使用callback异步回调（暂不支持）。

从 API version 7开始支持，从API version 9开始废弃，此接口不再提供代替接口。

**系统能力**：SystemCapability.Applications.Settings.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 数据项的名称。数据项名称分为以下两种： - 上述任意一个数据库中已存在的数据项。 - 开发者自行添加的数据项。 |
callbackAsyncCallback<object>是回调函数。获取数据项的URI。

**示例**：

```ets
settings.getURI(settings.display.SCREEN_BRIGHTNESS_STATUS, (uri:string) => {
    console.info(`callback:uri -> ${JSON.stringify(uri)}`)
})
```

#### settings.getURI(deprecated)

getURI(name: string): Promise<object>

获取数据项的URI。使用Promise异步回调（暂不支持）。

从 API version 7开始支持，从API version 9开始废弃，此接口不再提供代替接口。

**系统能力**：SystemCapability.Applications.Settings.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 数据项的名称。数据项名称分为以下两种： - 上述任意一个数据库中已存在的数据项。 - 开发者自行添加的数据项。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<object> | Promise对象。返回获取的数据项的URI。 |

**示例**：

```ets
settings.getURI(settings.display.SCREEN_BRIGHTNESS_STATUS).then((uri:string) => {
    console.info(`promise:uri -> ${JSON.stringify(uri)}`)
})
```

#### settings.getValue(deprecated)

getValue(dataAbilityHelper: [DataAbilityHelper](../../topics/misc/DataAbilityHelper.md), name: string, callback: AsyncCallback<object>): void

获取数据库中DEVICE_SHARD域指定数据项的值。使用callback异步回调。


从 API version 7开始支持，从API version 9开始废弃，建议使用[getValue()](#ZH-CN_TOPIC_0000002522241600__settingsgetvalue10)替代。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Applications.Settings.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataAbilityHelper | [DataAbilityHelper](../../topics/misc/DataAbilityHelper.md) | 是 | 数据管理辅助类。 |
| name | string | 是 | 数据项的名称。数据项名称分为以下两种： - 上述任意一个数据库中已存在的数据项。 - 开发者自行添加的数据项。 |
callbackAsyncCallback<object>是使用callback方式获取数据项的值。

**示例**：

```ets
import featureAbility from '@ohos.ability.featureAbility';

let uri:string = settings.getUriSync(settings.display.SCREEN_BRIGHTNESS_STATUS);
let helper = featureAbility.acquireDataAbilityHelper(uri);
settings.getValue(helper, settings.display.SCREEN_BRIGHTNESS_STATUS, (err:Error, value:string) => {
    if (err) {
        console.error(`Failed to get the setting. ${err.message} `);
        return;
    }
    console.info(`callback:value -> ${JSON.stringify(value)}`)
});
```

#### settings.getValue(deprecated)

getValue(dataAbilityHelper: [DataAbilityHelper](../../topics/misc/DataAbilityHelper.md), name: string): Promise<object>

获取数据库中DEVICE_SHARD域指定数据项的值。使用Promise异步回调。


从 API version 7开始支持，从API version 9开始废弃，建议使用[getValue()](#ZH-CN_TOPIC_0000002522241600__settingsgetvalue10-1)替代。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Applications.Settings.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataAbilityHelper | [DataAbilityHelper](../../topics/misc/DataAbilityHelper.md) | 是 | 数据管理辅助类。 |
| name | string | 是 | 数据项的名称。数据项名称分为以下两种： - 上述任意一个数据库中已存在的数据项。 - 开发者自行添加的数据项。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<object> | Promise对象。返回获取的数据项的值。 |

**示例**：

```ets
import featureAbility from '@ohos.ability.featureAbility';

let uri:string = settings.getUriSync(settings.display.SCREEN_BRIGHTNESS_STATUS);
let helper = featureAbility.acquireDataAbilityHelper(uri);
settings.getValue(helper, settings.display.SCREEN_BRIGHTNESS_STATUS).then((value:string) => {
    console.info(`promise:value -> ${JSON.stringify(value)}`)
});
```

#### settings.getValueSync(deprecated)

getValueSync(dataAbilityHelper: [DataAbilityHelper](../../topics/misc/DataAbilityHelper.md), name: string, defValue: string): string

获取数据项的值。此方法相较getValue为同步方法。


从 API version 8开始支持，从API version 9开始废弃，建议使用[getValueSync()](#ZH-CN_TOPIC_0000002522241600__settingsgetvaluesync10)替代。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Applications.Settings.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataAbilityHelper | [DataAbilityHelper](../../topics/misc/DataAbilityHelper.md) | 是 | 数据管理辅助类。 |
| name | string | 是 | 数据项的名称。数据项名称分为以下两种： - 上述任意一个数据库中已存在的数据项。 - 开发者自行添加的数据项。 |
defValuestring是默认值。由开发者设置，在数据库中查询不到该数据时，返回默认值。

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 返回数据项的值。 |

**示例**：

```ets
import featureAbility from '@ohos.ability.featureAbility';

// 获取数据项亮度的值(该数据项在数据库中已存在)。
let uri:string = settings.getUriSync(settings.display.SCREEN_BRIGHTNESS_STATUS);
let helper = featureAbility.acquireDataAbilityHelper(uri);
let value:string = settings.getValueSync(helper, settings.display.SCREEN_BRIGHTNESS_STATUS, '10');
```

#### settings.setValueSync(deprecated)

setValueSync(dataAbilityHelper: [DataAbilityHelper](../../topics/misc/DataAbilityHelper.md), name: string, value: string): boolean

设置数据项的值。此方法相较setValue为同步方法。

- 如果数据库中已经存在该数据项，setValueSync方法将更新该数据项的值。
- 如果数据库中不存在该数据项，setValueSync方法将向数据库中插入该数据项。


从 API version 8开始支持，从API version 9开始废弃，建议使用[setValueSync()](#ZH-CN_TOPIC_0000002522241600__settingssetvaluesync10)替代。

**模型约束**：此接口仅可在FA模型下使用。

**需要权限**：ohos.permission.MANAGE_SETTINGS，该权限仅系统应用可用。

**系统能力**：SystemCapability.Applications.Settings.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataAbilityHelper | [DataAbilityHelper](../../topics/misc/DataAbilityHelper.md) | 是 | 数据管理辅助类。 |
| name | string | 是 | 数据项的名称。数据项名称分为以下两种： - 上述任意一个数据库中已存在的数据项。 - 开发者自行添加的数据项。 |
valuestring是数据项的具体数值。取值范围随业务变动。

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 返回设置数据项的值是否成功的结果。true表示设置成功，false表示设置失败。 |

**示例**：

```ets
import featureAbility from '@ohos.ability.featureAbility';

// 更新数据项亮度的值(该数据项在数据库中已存在，故setValueSync方法将更新该数据项的值)。
let uri:string = settings.getUriSync(settings.display.SCREEN_BRIGHTNESS_STATUS);
let helper = featureAbility.acquireDataAbilityHelper(uri);
let ret:string = settings.setValueSync(helper, settings.display.SCREEN_BRIGHTNESS_STATUS, '100');
```

**settings.openInputMethodSettings23+**

openInputMethodSettings(context: Context): void

打开输入法设置页面。

模型约束：此接口仅可在Stage模型下使用。

系统能力：SystemCapability.Applications.Settings.Core

设备行为差异：该接口在Phone、Tablet设备中可正常调用，在其他设备调用不生效。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文（仅支持UIAbilityContext和ExtensionContext）。 Stage模型的应用Context定义见Context。 |

错误码：

以下错误码详细介绍请参考[设置数据项错误码](设置数据项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16900010 | Parameter error. |

示例：

```ets
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 跳转输入法设置页面。
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.openInputMethodSettings(context);
```

**settings.openInputMethodDetail23+**

openInputMethodDetail(context: Context, bundleName: string, inputMethodId: string): void

打开输入法详情页面。

模型约束：此接口仅可在Stage模型下使用。

系统能力：SystemCapability.Applications.Settings.Core

设备行为差异：该接口在Phone、Tablet设备中可正常调用，在其他设备调用不生效。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文（仅支持UIAbilityContext和ExtensionContext）。 Stage模型的应用Context定义见Context。 |
| bundleName | string | 是 | 拉起输入法的对应包名 |
| inputMethodId | string | 是 | 输入法扩展在应用内唯一标识id。 |

错误码：

以下错误码详细介绍请参考[设置数据项错误码](设置数据项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16900010 | Parameter error. |

示例：

```ets
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 跳转输入法详情页面。
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let bundleName: string = "target inputMethod bundle name";
let inputMethodId: string = "target inputMethod id";
settings.openInputMethodDetail(context, bundleName, inputMethodId);
```