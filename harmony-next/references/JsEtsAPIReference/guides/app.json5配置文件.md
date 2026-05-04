# app.json5配置文件

本文根据华为开发者官网 `app-configuration-file` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-configuration-file>
更新时间：2026-04-30 02:41:24

## 配置文件示例
先通过一个示例，了解app.json5配置文件的结构和内容。
{ "app": { "bundleName": "com.application.myapplication", "vendor": "example", "versionCode": 1000000, "versionName": "1.0.0", "icon": "$media:layered_image", "label": "$string:app_name", "description": "$string:description_application", "minAPIVersion": 9, "targetAPIVersion": 9, "debug": false, "car": { "minAPIVersion": 8 }, "appEnvironments": [ { "name":"name1", "value": "value1" } ], "maxChildProcess": 5, "multiAppMode": { "multiAppModeType": "appClone", "maxCount": 5 }, "hwasanEnabled": false, "ubsanEnabled": false, "cloudFileSyncEnabled": false, "cloudStructuredDataSyncEnabled": false, "configuration": "$profile:configuration", "assetAccessGroups": [ "com.ohos.photos", "com.ohos.screenshot", "com.ohos.note" ], "startMode": "mainTask", "buildVersion": "1.0.0" } }

## 配置文件标签
app.json5配置文件包含以下标签。
表1 app.json5配置文件标签说明
属性名称
含义
数据类型
是否可缺省
bundleName
标识应用的Bundle名称，用于标识应用的唯一性。命名规则如下 ：
- 必须为以点号（.）分隔的字符串，且至少包含三段，每段中仅允许使用英文字母、数字、下划线（_）。
- 首段以英文字母开头，非首段以数字或英文字母开头，每一段以数字或者英文字母结尾。
- 不允许多个点号（.）连续出现。
- 字符串最小长度为7字节，最大长度128字节。

## appEnvironments标签
此标签标识应用配置的环境变量。应用运行时有时会依赖一些三方库，这些三方库会使用到一些自定义的环境变量，为了不修改三方库的实现逻辑，可以在工程的配置文件中设置自定义的环境变量，以供运行时使用。
表2 appEnvironments标签说明
属性名称
含义
数据类型
是否可缺省
name
标识环境变量的变量名称。取值为长度不超过4096字节的字符串。
字符串
该标签可缺省，缺省值为空。
value
标识环境变量的值。取值为长度不超过4096字节的字符串。

## multiAppMode标签
应用多开模式。
表3 multiAppMode标签说明
属性名称
含义
数据类型
是否可缺省
multiAppModeType
标识应用多开模式类型，支持的取值如下：
- multiInstance：多实例模式。该标签仅支持2in1设备，常驻进程不支持该标签。
- appClone：应用分身模式。
字符串
该标签不可缺省。

## configuration标签
该标签对应一个profile文件资源，对应文件用于配置应用字体大小是否跟随系统变更。
configuration标签示例：
{ "app": { // ... "configuration": "$profile:configuration", // ... } }
在开发视图的AppScope/resources/base/profile下面定义配置文件configuration.json，其中文件名"configuration"可自定义，需要和configuration标签指定的文件资源对应。配置文件中列举了设置当前应用字体大小跟随系统变化所需要的属性。
表4 configuration标签说明
属性名称
含义
数据类型
是否可缺省
fontSizeScale
应用字体大小是否跟随系统，支持的取值如下：
- followSystem：跟随系统。
