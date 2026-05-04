# 组件启动规则（Stage模型）

本文根据华为开发者官网 `component-startup-rules` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-startup-rules>
更新时间：2026-04-24 08:10:21

## 组件启动总体规则
为了保证用户具有更好的使用体验，对以下几种易影响用户体验与系统安全的行为做了限制：
后台应用任意弹框，如各种广告弹窗，影响用户使用。
后台应用相互唤醒，不合理的占用系统资源，导致系统功耗增加或系统卡顿。
前台应用任意跳转至其他应用，如随意跳转到其他应用的支付页面，存在安全风险。
鉴于此，制定了一套组件启动规则，主要包括：
跨应用启动组件，需校验目标组件是否可以被其他应用调用。
若目标组件exported字段配置为true，表示可以被其他应用调用；若目标组件exported字段配置为false，表示不可以被其他应用调用，还需进一步校验ohos.permission.START_INVISIBLE_ABILITY权限（该权限仅系统应用可申请）。组件exported字段说明可参考abilities标签。
位于后台的UIAbility应用，启动组件需校验BACKGROUND权限ohos.permission.START_ABILITIES_FROM_BACKGROUND（该权限仅系统应用可申请）。
前后台应用的判断依据：若应用进程获焦或所属的UIAbility组件位于前台则判定为前台应用，否则为后台应用。
从API version 18开始，如果应用已创建在前台显示的悬浮窗，当该应用退至后台时，无需校验BACKGROUND权限也可以拉起其他Ability。
从API version 21开始，如果应用自身已经添加到状态栏，则当应用退至后台时，无需校验BACKGROUND权限也可以拉起自身的UIAbility。
跨设备使用startAbilityByCall接口，需校验分布式权限ohos.permission.DISTRIBUTED_DATASYNC。

## 同设备组件启动规则
设备内启动组件，不同场景下的规则不同，可分为如下三种场景：
启动UIAbility。
启动ServiceExtensionAbility、DataShareExtensionAbility。
通过startAbilityByCall接口启动UIAbility。
下图中的BACKGROUND权限是指ohos.permission.START_ABILITIES_FROM_BACKGROUND，CALL权限是指ohos.permission.ABILITY_BACKGROUND_COMMUNICATION。

## 分布式跨设备组件启动规则
跨设备启动组件，不同场景下的规则不同，可分为如下三种场景：
启动UIAbility。
启动ServiceExtensionAbility、DataShareExtensionAbility。
通过startAbilityByCall接口启动UIAbility。
下图中的BACKGROUND权限是指ohos.permission.START_ABILITIES_FROM_BACKGROUND，DATASYNC权限是指ohos.permission.DISTRIBUTED_DATASYNC。
