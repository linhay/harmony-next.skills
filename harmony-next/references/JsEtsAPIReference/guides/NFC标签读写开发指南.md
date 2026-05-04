# NFC标签读写开发指南

本文根据华为开发者官网 `nfc-tag-access-guide` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nfc-tag-access-guide>
更新时间：2026-04-24 08:10:21

## 简介
近场通信(Near Field Communication，NFC)是一种短距高频的无线电技术，在13.56MHz频率运行，通信距离一般在10厘米距离内。电子设备可以通过NFC通信技术和NFC标签通信，从标签中读取数据，或写入数据到标签。
NFC标签支持一种或多种通信技术，具体技术如下：
NfcA (也称为 ISO 14443-3A)
NfcB (也称为 ISO 14443-3B)
NfcF (也称为 JIS 6319-4)
NfcV (也称为 ISO 15693)
IsoDep (也称为 ISO 14443-4)
NDEF
MifareClassic
MifareUltralight

## 场景介绍
电子设备通过NFC天线位置触碰NFC标签卡片，完成NFC标签卡片的读取或写入。从使用场景上，可以分成NFC标签前台读写和NFC标签后台读写。
NFC标签前台读写
前台读写是指在触碰NFC标签之前，用户先在电子设备上打开特定的应用程序，用户明确想使用所打开的应用程序和NFC标签进行读写操作。用户打开应用程序在前台，并且进入应用的刷卡页面之后，电子设备触碰NFC标签，只会把读取到的卡片分发给前台应用。
NFC标签后台读写
后台读写是指不打开特定的NFC标签应用程序，电子设备触碰发现NFC标签后，根据NFC标签的技术类型，分发给能够处理的应用程序。如果能匹配到多个应用程序，则弹出应用选择器列举出应用列表给用户手动选择。用户选择指定的应用后，自动跳转到应用程序的NFC标签读写卡页面。
常用读写NDEF格式Tag定制功能
读取定制Tag内容拉起AirTouch服务，通过碰一碰服务直达，满足用户碎片化需求，如：NFC碰一碰点单、支付、活动推广等，详细应用开发接入指导及标签制作参考AirTouch服务。更多NDEF标签格式规范请关注NFC论坛。
标签读写约束条件
不管是前台读写，还是后台读写，电子设备能够发现NFC标签的前提条件是设备必须是亮屏和解锁状态。

## 接口说明
NFC标签读写完整的JS API说明以及实例代码请参考：NFC标签接口。
获取不同技术类型标签对象的接口说明如下表，根据不同技术的标签对象来执行NFC标签的读写。
接口名
支持版本
功能描述
getNfcA(tagInfo: TagInfo): NfcATag
从API version 9开始支持
获取NfcA技术类型的标签对象。
getNfcB(tagInfo: TagInfo): NfcBTag
获取NfcB技术类型的标签对象。
getNfcF(tagInfo: TagInfo): NfcFTag
获取NfcF技术类型的标签对象。

## 开发准备

## NFC标签前台读写或后台读写的选择
NFC标签读写应用开发者根据业务需要，可以选择实现前台读卡或者后台读卡。两种不同的读卡方式，代码实现上会存在一些差异。
NFC标签前台读写
在配置文件module.json5中，不需要静态声明过滤读取NFC标签的技术类型，而是通过tag.registerForegroundDispatch或者tag.on来完成动态注册。
通过tag.registerForegroundDispatch或tag.on来动态注册前台读写标签时，入参中必须指定需要读取NFC标签的技术类型。
如果选择tag.registerForegroundDispatch注册，当应用运行在前台并进入该页面，NFC的卡模拟功能在打开时，可以同时完成刷卡。如果选择tag.on注册，当应用运行在前台并进入该页面时，NFC的卡模拟是关闭的，无法同时进行刷卡功能。
当应用页面切换到后台时，需要显式调用tag.unregisterForegroundDispatch或者tag.off来取消注册，退出前台读卡优先功能。
NFC标签后台读写
在配置文件module.json5中，需要静态声明过滤读取NFC标签的技术类型。根据业务需要至少定义一种读标签的技术类型，‘tag-tech/’是前缀，后面跟着技术类型描述。
技术类型的描述字符，必须完整匹配并区分大小写，需要严格匹配。
从API version 9之后的应用开发新增支持Stage模型，作为目前主推并长期演进的模型。
NFC标签读写示例代码的提供，全部按照Stage模型来说明。

## 开发步骤

## 前台读取标签
在module.json5文件中声明NFC标签读取的权限，以及声明NFC标签特定的action。
import需要的tag模块和其他相关的模块。
判断设备是否支持NFC能力。
调用tag模块中前台优先的接口，使能前台应用程序优先处理所发现的NFC标签功能。
获取特定技术类型的NFC标签对象。
执行读写接口完成标签数据的读取或写入数据到标签。
退出应用程序NFC标签页面时，调用tag模块退出前台优先功能。
"abilities": [ { "name": "EntryAbility", "srcEntry": "./ets/entryability/EntryAbility.ts", "description": "$string:EntryAbility_desc", "icon": "$media:icon", "label": "$string:EntryAbility_label", "startWindowIcon": "$media:icon", "startWindowBackground": "$color:start_window_background", "exported": true, "skills": [ { "entities": [ "entity.system.home" ], "actions": [ "ohos.want.action.home", // actions必须包含"ohos.nfc.tag.action.TAG_FOUND" "ohos.nfc.tag.action.TAG_FOUND" ] } ] } ], "requestPermissions": [ { // 添加NFC标签操作的权限 "name": "ohos.permission.NFC_TAG", "reason": "$string:app_name", } ]
import { tag } from '@kit.ConnectivityKit'; import { BusinessError } from '@kit.BasicServicesKit'; import { hilog } from '@kit.PerformanceAnalysisKit'; import { AbilityConstant, UIAbility, Want, bundleManager } from '@kit.AbilityKit'; let nfcTagElementName: bundleManager.ElementName; let foregroundRegister: boolean; async function readerModeCb(error: BusinessError, tagInfo: tag.TagInfo) { if (!error) { // 获取特定技术类型的NFC标签对象 if (tagInfo == null) { hilog.error(0x0000, 'testTag', 'readerModeCb tagInfo is invalid'); return; } if (tagInfo.uid == null) { hilog.error(0x0000, 'testTag', 'readerModeCb uid is invalid'); return; } if (tagInfo.technology == null || tagInfo.technology.length == 0) { hilog.error(0x0000, 'testTag', 'readerModeCb technology is invalid'); return; } // 标签里面可能支持多种技术类型，选择特定的技术类型接口，完成标签数据的读取或写入 // 下面示例代码，使用IsoDep完成标签数据的读取或写入 let isoDep: tag.IsoDepTag | null = null; for (let i = 0; i < tagInfo.technology.length; i++) { if (tagInfo.technology[i] == tag.ISO_DEP) { try { isoDep = tag.getIsoDep(tagInfo); } catch (error) { hilog.error(0x0000, 'testTag', 'readerModeCb getIsoDep error = %{public}s', JSON.stringify(error)); return; } } // 也可以按需选择其它类型的技术读写标签 } if (isoDep == null) { hilog.error(0x0000, 'testTag', 'readerModeCb getIsoDep is invalid'); return; } // 使用IsoDep技术连接到NFC标签 try { isoDep.connect(); } catch (error) { hilog.error(0x0000, 'testTag', 'readerModeCb isoDep.connect() error = %{public}s', JSON.stringify(error)); return; } if (!isoDep.isConnected()) { hilog.error(0x0000, 'testTag', 'readerModeCb isoDep.isConnected() false.'); return; } // 发送指令到已连接的标签，获取标签的响应数据 let cmdData = [0x01, 0x02, 0x03, 0x04]; // 修改为正确的访问标签的指令数据 try { isoDep.transmit(cmdData).then((response: number[]) => { hilog.info(0x0000, 'testTag', 'readerModeCb isoDep.transmit() response = %{public}s.', JSON.stringify(response)); }).catch((err: BusinessError) => { hilog.error(0x0000, 'testTag', 'readerModeCb isoDep.transmit() err = %{public}s.', JSON.stringify(err)); return; }); } catch (businessError) { hilog.error(0x0000, 'testTag', 'readerModeCb isoDep.transmit() businessError = %{public}s.', JSON.stringify(businessError)); return; } } else { hilog.info(0x0000, 'testTag', 'readerModeCb readerModeCb error %{public}s', JSON.stringify(error)); } } export default class EntryAbility extends UIAbility { onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) { hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate'); // 判断设备是否支持NFC能力 if (!canIUse("SystemCapability.Communication.NFC.Core")) { hilog.error(0x0000, 'testTag', 'nfc unavailable.'); return; } // 根据应用程序信息，初始化正确的值 nfcTagElementName = { bundleName: want.bundleName ?? '', abilityName: want.abilityName ?? '', moduleName: want.moduleName, } } onForeground() { // 应用进入前台，调用tag模块中前台优先的接口，使能前台应用程序优先处理所发现的NFC标签功能 hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground'); if (nfcTagElementName != undefined) { // 根据业务需要，选择需要读取标签的通信技术 let techList: number[] = [tag.NFC_A, tag.NFC_B, tag.NFC_F, tag.NFC_V]; try { tag.on('readerMode', nfcTagElementName, techList, readerModeCb); foregroundRegister = true; } catch (error) { hilog.error(0x0000, 'testTag', 'on readerMode error = %{public}s', JSON.stringify(error)); } } } onBackground() { hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground'); // 退出应用程序NFC标签页面时，调用tag模块退出前台优先功能 if (foregroundRegister) { foregroundRegister = false; try { tag.off('readerMode', nfcTagElementName); } catch (error) { hilog.error(0x0000, 'testTag', 'off readerMode error = %{public}s', JSON.stringify(error)); } } } }

## 后台读取标签
在module.json5文件中声明NFC标签读取的权限，声明NFC标签特定的action，以及声明本应用程序的能够处理的NFC标签技术类型。
import需要的tag模块和其他相关的模块。
获取特定技术类型的NFC标签对象。
执行读写接口完成标签数据的读取或写入数据到标签。
应用程序需要支持后台读卡时，需要在应用的属性配置文件中，声明与NFC相关的属性值。比如，在module.json5文件中，声明下面属性值。
声明"actions"字段的内容填写，必须包含"ohos.nfc.tag.action.TAG_FOUND"，不能更改。
声明技术时"uris"中"type"字段的内容填写，前缀必须是"tag-tech/"，后面接着NfcA/NfcB/NfcF/NfcV/IsoDep/Ndef/MifareClassic/MifareUL/NdefFormatable"中的一个。如果存在多个"type"时，需要分行填写。填写错误会造成解析失败。
声明权限时"requestPermissions"中的"name"字段的内容填写，必须是"ohos.permission.NFC_TAG"，不能更改。
Wearable设备不支持后台读卡。
"abilities": [ { "name": "EntryAbility", "srcEntry": "./ets/entryability/EntryAbility.ts", "description": "$string:EntryAbility_desc", "icon": "$media:icon", "label": "$string:EntryAbility_label", "startWindowIcon": "$media:icon", "startWindowBackground": "$color:start_window_background", "exported": true, "skills": [ { "entities": [ "entity.system.home" ], "actions": [ "ohos.want.action.home", // actions必须包含"ohos.nfc.tag.action.TAG_FOUND" "ohos.nfc.tag.action.TAG_FOUND" ], // 根据业务需要至少定义一种读标签的技术类型，‘tag-tech/’是前缀，后面跟着技术类型描述 "uris": [ { "type":"tag-tech/NfcA" }, { "type":"tag-tech/IsoDep" } // 必要时可添加其他技术类型 // 例如: NfcB/NfcF/NfcV/Ndef/MifareClassic/MifareUL/NdefFormatable ] } ] } ], "requestPermissions": [ { // 添加NFC标签操作的权限 "name": "ohos.permission.NFC_TAG", "reason": "$string:app_name", } ]
import { tag } from '@kit.ConnectivityKit'; import { BusinessError } from '@kit.BasicServicesKit'; import { hilog } from '@kit.PerformanceAnalysisKit'; import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit'; export default class EntryAbility extends UIAbility { onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) { hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate'); // 获取特定技术类型的NFC标签对象 let tagInfo: tag.TagInfo; try { tagInfo = tag.getTagInfo(want); } catch (error) { hilog.error(0x0000, 'testTag', 'getTagInfo error = %{public}s', JSON.stringify(error)); return; } if (tagInfo == null) { hilog.error(0x0000, 'testTag', 'tagInfo is invalid'); return; } if (tagInfo.uid == null) { hilog.error(0x0000, 'testTag', 'uid is invalid'); return; } if (tagInfo.technology == null || tagInfo.technology.length == 0) { hilog.error(0x0000, 'testTag', 'technology is invalid'); return; } // 标签里面可能支持多种技术类型，选择特定的技术类型接口，完成标签数据的读取或写入 // 下面示例代码，使用IsoDep完成标签数据的读取或写入 let isoDep: tag.IsoDepTag | null = null; for (let i = 0; i < tagInfo.technology.length; i++) { if (tagInfo.technology[i] == tag.ISO_DEP) { try { isoDep = tag.getIsoDep(tagInfo); } catch (error) { hilog.error(0x0000, 'testTag', 'getIsoDep error = %{public}s', JSON.stringify(error)); return; } } // 也可以按需选择其它类型的技术读写标签 } if (isoDep == null) { hilog.error(0x0000, 'testTag', 'getIsoDep is invalid'); return; } // 使用IsoDep技术连接到NFC标签 try { isoDep.connect(); } catch (error) { hilog.error(0x0000, 'testTag', 'isoDep.connect() error = %{public}s', JSON.stringify(error)); return; } if (!isoDep.isConnected()) { hilog.error(0x0000, 'testTag', 'isoDep.isConnected() false.'); return; } // 发送指令到已连接的标签，获取标签的响应数据 let cmdData = [0x01, 0x02, 0x03, 0x04]; // 修改为正确的访问标签的指令数据 try { isoDep.transmit(cmdData).then((response: number[]) => { hilog.info(0x0000, 'testTag', 'isoDep.transmit() response = %{public}s.', JSON.stringify(response)); }).catch((err: BusinessError) => { hilog.error(0x0000, 'testTag', 'isoDep.transmit() err = %{public}s.', JSON.stringify(err)); return; }); } catch (businessError) { hilog.error(0x0000, 'testTag', 'isoDep.transmit() businessError = %{public}s.', JSON.stringify(businessError)); return; } } }
