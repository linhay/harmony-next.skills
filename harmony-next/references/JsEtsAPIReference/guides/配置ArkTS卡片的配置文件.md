# 配置ArkTS卡片的配置文件

本文根据华为开发者官网 `arkts-ui-widget-configuration` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-configuration>
更新时间：2026-04-20 06:34:33

## FormExtensionAbility配置
卡片需要在module.json5配置文件的extensionAbilities标签下，配置FormExtensionAbility相关信息。FormExtensionAbility需要填写metadata元信息标签，其中键名称为固定字符串 “ohos.extension.form”，资源为卡片具体配置信息的资源索引。
配置示例如下：
{ "module": { // ... "extensionAbilities": [ { "name": "EntryFormAbility", "srcEntry": "./ets/entryformability/EntryFormAbility.ets", "label": "$string:EntryFormAbility_label", "description": "$string:EntryFormAbility_desc", "type": "form", "metadata": [ { "name": "ohos.extension.form", "resource": "$profile:form_config" } ] } ], // 只在独立卡片包形态中会使用，用来关联卡片包模块。 "formWidgetModule": "library" } }

## 独立卡片包配置
相对应地，在卡片包的module.json5配置文件中，formExtensionModule字段用来关联应用包的module。
配置示例如下：
{ "module": { "name": "library", "type": "shared", "description": "$string:shared_desc", "deviceTypes": [ "phone" ], "deliveryWithInstall": true, // 只在独立卡片包形态中会使用，用来关联应用包模块。 "formExtensionModule": "entry" } }

## 卡片配置
在上述FormExtensionAbility的元信息metadata配置项中，可以指定卡片具体配置信息的资源索引。例如当resource指定为$profile:form_config时，会使用开发视图的resources/base/profile/目录下的form_config.json作为卡片profile配置文件。在创建卡片时会自动生成form_config.json配置文件。

## 配置文件字段说明
表1 卡片form_config.json配置文件
属性名称
含义
数据类型
是否可缺省
forms
表示应用的全部卡片配置信息。
最多支持配置16个卡片，若超过16个，则保留配置的前16个。
数组
否
name
表示卡片的名称，字符串最大长度为127字节。用于开发者区分不同的卡片。

## supportDeviceTypes标签
此标签标识卡片支持的设备类型。
属性名称
含义
数据类型
phone
手机设备。
字符串
tablet
平板设备。
tv
智慧屏设备。
wearable

## supportDevicePerformanceClasses标签
此标签标识卡片支持的设备性能等级信息。
属性名称
含义
数据类型
high
表示设备能力定级为高。
字符串
medium
表示设备能力定级为中。
low
表示设备能力定级为低。

## window标签
此标签标识window对象的内部结构说明。只支持在JS卡片中使用。
属性名称
含义
数据类型
是否可缺省
designWidth
标识页面设计基准宽度。以此为基准，根据实际设备宽度来缩放元素大小。
数值
可缺省，缺省值为720px。
autoDesignWidth
标识页面设计基准宽度是否自动计算。当配置为true时，designWidth将会被忽略，设计基准宽度由设备宽度与屏幕密度计算得出。
布尔值

## funInteractionParams标签
此标签标识趣味交互类型互动卡片配置。funInteractionParams 和 sceneAnimationParams 同时配置时识别为趣味交互类型互动卡片。
名称
类型
必填
说明
abilityName
字符串
否
趣味交互场景LiveFormExtensionAbility名称，默认为空。
targetBundleName
是
趣味交互场景主包包名。

## sceneAnimationParams标签
此标签标识场景动效类型互动卡片配置。funInteractionParams 和 sceneAnimationParams 同时配置时识别为趣味交互类型互动卡片。
名称
类型
必填
说明
abilityName
字符串
是
场景动效LiveFormExtensionAbility名称。
{ "forms": [ { // ... "sceneAnimationParams": { "abilityName": "MyLiveFormExtensionAbility" } } ] }
