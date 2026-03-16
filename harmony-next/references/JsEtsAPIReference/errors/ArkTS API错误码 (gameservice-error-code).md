[]()[]()

# ArkTS API错误码

以下仅介绍Game Service Kit特有错误码，通用错误码请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

[]()[]()

#### 1010300001 游戏内部通用错误

**错误信息**

System internal error.

**错误描述**

游戏内部通用错误。

**可能原因**

Game Service Kit系统内部错误。

**处理步骤**

通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101704354579010004&keyWord=Game Service Kit)提交问题，华为工程师会及时处理。

[]()[]()

#### 1010300002 鉴权失败

**错误信息**

Auth failed.

**错误描述**

鉴权失败。

**可能原因**

网络连接或传参错误。

**处理步骤**

1. 首次使用设备进行登录时，请确认网络连接正常。
1. 请检查[init](../topics/misc/gamePerformance (游戏场景感知).md#section131971556806)接口传参是否正确。

[]()[]()

#### 1010300003 非法请求

**错误信息**

Invalid request.

**错误描述**

非法请求。

**可能原因**

未初始化或初始化未成功时，调用了其他接口。

**处理步骤**

请先调用[init](../topics/misc/gamePerformance (游戏场景感知).md#section131971556806)接口，并确保调用成功。

[]()[]()

#### 1002000001 游戏内部通用错误

**错误信息**

System internal error.

**错误描述**

游戏内部通用错误。

**可能原因**

常见原因如下：

- [unionLogin](../topics/misc/gamePlayer（基础游戏服务）.md#section157848375136)登录接口的入参accountIcon总大小超过35KB。
- 接口中的入参context不符合要求。

**处理步骤**

1. 排查游戏官方账号的图标大小，要求图标大小不超过35KB。
1. 排查各接口中的入参context是否符合要求。建议context按照如下方式获取：

```ets
let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
```

1. 通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101704354579010004)提交问题，华为工程师会及时处理。

[]()[]()

#### 1002000002 网络错误

**错误信息**

Network connection error.

**错误描述**

网络错误。

**可能原因**

常见原因如下：

- 未配置手动申请的调试证书签名。
- 未添加调试证书对应的指纹。
- 工程entry模块module.json5文件的client_id、app_id与AppGallery Connect中的实际应用不对应。
- 网络连接错误。

**处理步骤**

1. 请检查配置项是否配置正确，详情请参见[开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameplayer-huawei#section818512085410)。
1. 请检查网络连接是否正常。

[]()[]()

#### 1002000003 未查到华为账号相关信息

**错误信息**

The HUAWEI ID is not signed in or not authorized.

**错误描述**

未查到华为账号相关信息。

**可能原因**

未查到华为账号相关信息。

**处理步骤**

确认华为账号已经登录并授权。

[]()[]()

#### 1002000004 实名认证返回强制实名但用户取消，或需要强制实名但没有实名

**错误信息**

User cancels real name authentication or not real name.

**错误描述**

实名认证返回强制实名但用户取消，或需要强制实名但没有实名。

**可能原因**

实名认证返回强制实名但用户取消，或需要强制实名但没有实名。

**处理步骤**

调用[unionLogin](../topics/misc/gamePlayer（基础游戏服务）.md#section157848375136)接口再次引导用户进行实名认证。

[]()[]()

#### 1002000005 只支持服务地和注册地均为中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）的华为账号

**错误信息**

The country or region of the signed-in Huawei ID does not support.

**错误描述**

只支持服务地和注册地均为中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）的华为账号。

**可能原因**

华为账号服务地和注册地不是中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

**处理步骤**

在用户登录游戏时，引导用户更换或重新注册中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）的华为账号进行登录。

[]()[]()

#### 1002000006 玩家未成年并且当前不在可游戏时间

**错误信息**

User is underage and has no playable time.

**错误描述**

玩家未成年并且当前不在可游戏时间。

**可能原因**

玩家未成年，且当前不在允许游戏的时间内。

**处理步骤**

检查当前未成年人的游戏时间是否为周五、周六、周日和法定节假日的20时至21时：

- 若不是，Game Service Kit已经做了游戏退出逻辑，开发者无需额外处理。
- 若是，可通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101704354579010004)提交问题，华为工程师会及时处理。

[]()[]()

#### 1002000007 商品所属的应用未在指定国家/地区上架

**错误信息**

The application to which the product belongs is not listed in the specified country.

**错误描述**

商品所属的应用未在指定国家/地区上架。

**可能原因**

商品所属的应用未在指定国家/地区上架。

**处理步骤**

请登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，在“我的应用 > 分发 > 版本信息 > 准备提交”中查看商品配置的国家/地区。

[]()[]()

#### 1002000008 该华为账号在禁止名单中

**错误信息**

The HUAWEI ID is in the blocklist.

**错误描述**

该华为账号在禁止名单中

**可能原因**

- 国家公祭日不可玩游戏。
- 当前华为账号的玩家被风控禁止玩游戏。

**处理步骤**

- 若有风控、国家公祭日等弹框提示，游戏无需处理。
- 其它情况可通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101704354579010004)提交问题，华为工程师会及时处理。

[]()[]()

#### 1002000009 当前游戏不支持第三方游戏账号

**错误信息**

The game account is unavailable for the game.

**错误描述**

当前游戏不支持第三方游戏账号。

**可能原因**

登录的游戏号不正确。

**处理步骤**

更换游戏账号。

[]()[]()

#### 1002000010 华为teamPlayerId与当前玩家不匹配

**错误信息**

The playerId is not current player.

**错误描述**

华为teamPlayerId与当前玩家不匹配。

**可能原因**

调用[bindPlayer](../topics/misc/gamePlayer（基础游戏服务）.md#section2090261116551)或[unbindPlayer](../topics/misc/gamePlayer（基础游戏服务）.md#section57861515615)接口时，teamPlayerId传错。

**处理步骤**

请检查teamPlayerId是否正确，并重新调用[bindPlayer](../topics/misc/gamePlayer（基础游戏服务）.md#section2090261116551)或[unbindPlayer](../topics/misc/gamePlayer（基础游戏服务）.md#section57861515615)接口传递正确teamPlayerId。

[]()[]()

#### 1002000011 玩家未确认协议、隐私声明

**错误信息**

Agreement not agreed.

**错误描述**

玩家未确认协议、隐私声明。

**可能原因**

玩家在弹出隐私协议窗口时选择了取消，或init接口未调用成功前调用了其他接口。

**处理步骤**

重新调用[init](../topics/misc/gamePlayer（基础游戏服务）.md#section131971556806)接口。

[]()[]()

#### 1002000012 游戏官方账号与华为teamPlayerId已绑定

**错误信息**

The thirdOpenId or teamPlayerId has been bound.

**错误描述**

游戏官方账号与华为teamPlayerId已绑定。

**可能原因**

调用[bindPlayer](../topics/misc/gamePlayer（基础游戏服务）.md#section2090261116551)接口时，游戏官方账号与华为teamPlayerId已绑定。

**处理步骤**

无需处理。

[]()[]()

#### 1002000013 游戏官方账号与华为teamPlayerId未绑定

**错误信息**

The thirdOpenId and teamPlayerId are not bound.

**错误描述**

游戏官方账号与华为teamPlayerId未绑定。

**可能原因**

调用[unbindPlayer](../topics/misc/gamePlayer（基础游戏服务）.md#section57861515615)接口时，游戏官方账号与华为teamPlayerId未绑定。

**处理步骤**

无需处理。

[]()[]()

#### 1002000014 此接口不适用于此游戏

**错误信息**

This interface is not available for this game.

**错误描述**

此接口不适用于此游戏。

**可能原因**

当前游戏不支持调用此接口。

**处理步骤**

1. 请确认当前游戏调用[unionLogin](../topics/misc/gamePlayer（基础游戏服务）.md#section157848375136)接口是否报错。
1. 若是调用unionLogin接口出现报错，请重新尝试调用除unionLogin以外的接口。
1. 若调用unionlogin以外的接口还是报错，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101704354579010004)提交问题，华为工程师会及时处理。若调用unionlogin以外的接口不报错，说明当前游戏没有使用unionLogin接口的权限，请使用其它接口。
1. 若游戏没有使用unionLogin接口的权限，但游戏又想重新使用unionlogin接口，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101704354579010004)提交问题，华为工程师会及时处理。

[]()[]()

#### 1002000015 当前玩家信息无效

**错误信息**

The current player information is invalid.

**错误描述**

当前玩家信息无效。

**可能原因**

常见原因是游戏登录成功后，用户切换了华为账号，导致游戏中的当前玩家信息无效。

**处理步骤**

请重新调用[unionLogin](../topics/misc/gamePlayer（基础游戏服务）.md#section157848375136)接口，获取玩家信息。

[]()[]()

#### 1002000016 玩家取消联合登录

**错误信息**

Union login canceled by user.

**错误描述**

玩家取消联合登录。

**可能原因**

在联合登录的过程中，玩家取消了联合登录。

**处理步骤**

如需继续登录，请重新调用[unionLogin](../topics/misc/gamePlayer（基础游戏服务）.md#section157848375136)接口。

[]()[]()

#### 1002000017 非法应用

**错误信息**

Illegal application identity.

**错误描述**

非法应用。

**可能原因**

Client ID、APP ID、签名等配置信息错误或缺失。

**处理步骤**

检查[配置签名证书指纹](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameplayer-huawei#section205943551234)、[配置APP ID和Client ID](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameplayer-huawei#section7658201162412)等信息是否已配置或正确，并根据情况补充配置或进行修改。

[]()[]()

#### 1002000018 此API仅支持小游戏

**错误信息**

This API is only provided for HarmonyOS mini games.

**错误描述**

此API仅支持小游戏。

**可能原因**

在不是小游戏的游戏内使用此API。

**处理步骤**

请更改为使用其他API。

[]()[]()

#### 1002000019 参数错误

**错误信息**

Parameter error.

**错误描述**

参数错误。

**可能原因**

- 必选参数没有传入。
- 参数类型错误 (Type Error)。
- 参数数量错误 (Argument Count Error)。
- 空参数错误 (Null Argument Error)。
- 参数格式错误 (Format Error)。
- 参数值范围错误 (Value Range Error)。

**处理步骤**

请检查必选参数是否传入，或者传入的参数类型是否错误，按参数规格说明修改传入参数。

[]()[]()

#### 1002000020 当前操作被用户取消

**错误信息**

The operation was canceled by the user.

**错误描述**

当前操作被用户取消。

**可能原因**

用户已取消当前操作。

**处理步骤**

向用户提示，操作取消。

[]()[]()

#### 1002000021 API调用过于频繁

**错误信息**

Too frequent API calls.

**错误描述**

API调用过于频繁。

**可能原因**

频繁调用API。

**处理步骤**

请控制接口调用频度，接口当前访问间隔时间默认为5s。

[]()[]()

#### 1002000050 无效的商品信息

**错误信息**

Invalid product information.

**错误描述**

无效的商品信息。

**可能原因**

1. 传入的商品ID或者商品类型有误。
1. 在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上创建的商品未提交审核或未审核通过（创建商品及提交审核可参见[新增单个数字商品](https://developer.huawei.com/consumer/cn/doc/app/new-0000001931836320)）。

**处理步骤**

请登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，在“我的应用 > 运营 > 商品管理 > 商品列表” 查看对应商品是否存在或必填信息是否完整及已经提交审核并审核通过。如未审核通过，可使用沙盒账号来测试（参见[沙盒测试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-sandbox)）。

[]()[]()

#### 1002000051 由于已经拥有该商品，购买失败

**错误信息**

Failed to purchase a product because the user already owns the product.

**错误描述**

由于已经拥有该商品，购买失败。

**可能原因**

该商品已经购买。

**处理步骤**

可通过[queryPurchases](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-iap#section1147122418532)接口确认用户是否购买了该商品。

- 若商品为消耗型商品或非续期订阅商品，检查商品是否发货，确认发货成功之后调用[finishPurchase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-iap#section124751324135814)接口完成购买，下次可正常购买。
- 若商品为非消耗型商品或自动续期订阅商品，已经购买则不能再次购买。

[]()[]()

#### 1002000052 由于未拥有该商品，发货失败

**错误信息**

The purchase cannot be finished because the user has not paid for it.

**错误描述**

由于未拥有该商品，发货失败。

**可能原因**

用户未购买该商品。

**处理步骤**

可通过[queryPurchases](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-iap#section1147122418532)接口确认用户是否购买了该商品。

[]()[]()

#### 1002000053 此次购买已经完成发货，无需重复发货

**错误信息**

The purchase has been finished and cannot be finished again.

**错误描述**

此次购买已经完成发货，无需重复发货。

**可能原因**

此次购买已经完成发货，无需重复发货。

**处理步骤**

可通过[queryPurchases](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-iap#section1147122418532)接口查询是否有该商品的确认发货记录。

[]()[]()

#### 1002000054 用户账号所在服务地不在IAP Kit支持结算的国家/地区中

**错误信息**

The country or region of the signed-in HUAWEI ID does not support IAP.

**错误描述**

用户账号所在服务地不在IAP Kit支持结算的国家/地区中。

**可能原因**

用户账号所在服务地不在IAP Kit支持结算的国家/地区中。

**处理步骤**

用户账号服务地为非中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）地区。建议应用隐藏相关支付功能入口。

[]()[]()

#### 1002000056 用户交易被拒绝

**错误信息**

The user is not allowed to make purchase.

**错误描述**

用户交易被拒绝。

**可能原因**

交易行为触发IAP Kit风控。

**处理步骤**

建议稍后重试或更换支付方式。

[]()[]()

#### 1018300001 游戏内部通用错误

**错误信息**

System internal error.

**错误描述**

游戏内部通用错误。

**可能原因**

Game Service Kit系统内部错误。

**处理步骤**

通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101704354579010004&keyWord=Game Service Kit)提交问题，华为工程师会及时处理。

[]()[]()

#### 1018300002 鉴权失败

**错误信息**

Authentication failed.

**错误描述**

鉴权失败。

**可能原因**

网络连接、传参错误或未配置白名单。

**处理步骤**

1. 首次使用设备进行登录时，请确认网络连接正常。
1. 请检查[create](../topics/media/gameNearbyTransfer(游戏近场快传).md#section131971556806)接口传参是否正确。
1. 未配置白名单，请参见[开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-nearbytransfer-config-agc)联系运营申请开通。

[]()[]()

#### 1018300003 请求不合法

**错误信息**

Invalid request.

**错误描述**

请求不合法。

**可能原因**

未创建游戏近场快传服务或创建失败时，调用了其他接口。

**处理步骤**

请先调用[create](../topics/media/gameNearbyTransfer(游戏近场快传).md#section131971556806)接口初始化，并确保调用成功。

[]()[]()

#### 1018300004 服务不可用

**错误信息**

No service available.

**错误描述**

服务不可用。

**可能原因**

没有发现附近有设备可绑定。

**处理步骤**

确认接收方发布后，尝试重新发现并绑定。

[]()[]()

#### 1018300005 WLAN和蓝牙必须开启

**错误信息**

The wireless network and Bluetooth should be enabled at the same time.

**错误描述**

WLAN和蓝牙必须同时开启。

**可能原因**

游戏所在设备的WLAN和蓝牙未同时开启。

**处理步骤**

同时开启游戏所在设备的WLAN及蓝牙。

[]()[]()

#### 1018300006 发布失败

**错误信息**

Publish failed.

**错误描述**

发布失败。

**可能原因**

发布失败。

**处理步骤**

系统内部异常，尝试重新发布。

[]()[]()

#### 1018300007 发现失败

**错误信息**

Discovery failed.

**错误描述**

发现失败。

**可能原因**

未发现设备。

**处理步骤**

确认接收方发布后，尝试重新发现。

[]()[]()

#### 1018300008 非法参数

**错误信息**

Invalid parameter.

**错误描述**

非法参数。

**可能原因**

1. 必填参数为空。
1. 参数类型不正确。
1. 参数校验失败。

**处理步骤**

请检查必选参数是否传入，或者传入参数类型是否错误，按参数规格说明修改传入参数。