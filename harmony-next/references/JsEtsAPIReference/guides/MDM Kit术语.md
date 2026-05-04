# MDM Kit术语

本文根据华为开发者官网 `mdm-kit-term` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-term>
更新时间：2026-04-20 06:34:33

## EDM
Enterprise device manager 企业设备管理, EDM服务是企业设备管理框架中的核心底座。

## BYOD
Bring Your Own Device，自带设备办公。指一些企业允许员工携带自己平板或智能手机到公司，并使用这些设备接入办公环境，用户企业办公或者外来访客携带设备访问工厂、实验室等场景。

## Admin角色

## SDA
Super Device Admin，超级设备管理员。激活为SDA的Admin组件，可以对设备进行管控以及管理其他的DA应用（包括激活、解除激活DA应用），适用于企业设备办公。

## DA
Device Admin，普通设备管理员。激活为DA的Admin组件，可以对设备进行管控，适用于企业设备办公。

## BDA
Byod Device Admin，BYOD设备管理员。激活为BDA的组件，可以对设备进行一些如禁用拍照、录音等简单管控。

## MDM应用（设备管理应用）
又称企业MDM应用，指集成了MDM（Mobile Device Management，移动设备管理）管理功能的应用，能够集中管理、监控和保护企业内的移动设备（如智能手机、平板电脑、笔记本电脑等）。它允许IT管理员远程配置设备、强制执行安全策略、部署应用程序，并确保企业数据的安全。

## 企业设备管理扩展能力
企业设备管理扩展能力（EnterpriseAdminExtensionAbility）组件是MDM应用必备组件。开发者为企业开发MDM应用时，需继承EnterpriseAdminExtensionAbility，在EnterpriseAdminExtensionAbility实例中实现MDM业务逻辑，EnterpriseAdminExtensionAbility实现了系统管理状态变化通知功能，并定义了管理应用激活、去激活、应用安装、卸载事件等回调接口。当MDM应用的企业设备管理扩展能力被激活后，此企业设备管理扩展能力会被保活，当重启、切换用户后会自动启动。企业设备管理扩展能力激活后的MDM应用无法被卸载。

## EMM厂商
EMM厂商是指为其他企业提供企业移动管理全套软件、解决方案和服务的公司。
