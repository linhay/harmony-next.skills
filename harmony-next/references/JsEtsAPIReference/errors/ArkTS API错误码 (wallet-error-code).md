[]()[]()

# ArkTS API错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

[]()[]()

#### 1010200001 没有权限访问钱包应用

**错误信息**

No permission to access the Wallet APIs.

**错误描述**

三方应用身份校验失败。

**可能原因**

应用没有调用Wallet Kit接口的权限。

**处理步骤**

1. AGC注册账号并接入服务

2. 联系钱包服务对接人，添加应用接入权限管控的白名单

3. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1010200002 钱包应用没有安装

**错误信息**

Wallet app not found.

**错误描述**

钱包应用没有安装。

**可能原因**

钱包应用没有安装。

**处理步骤**

在应用市场下载并安装钱包应用。

[]()[]()

#### 1010200003 访问钱包的前置环境没有准备好

**错误信息**

The environment of the wallet is not ready.

**错误描述**

访问钱包的前置环境没有准备好。

**可能原因**

1. 没有同意用户协议。
1. 没有登录华为账号。

**处理步骤**

打开钱包同意协议，并登录华为账号。

[]()[]()

#### 1010200004 当前设备不支持开通卡券

**错误信息**

The device does not support this card.

**错误描述**

当前设备不支持开通此卡券。

**可能原因**

开通该卡券的机型不支持或是软件版本过低。

**处理步骤**

排查机型或是查看软件版本。

[]()[]()

#### 1010200005 用户主动取消操作

**错误信息**

The operation was canceled by the user.

**错误描述**

用户主动取消操作。

**可能原因**

用户主动点击取消按钮。

**处理步骤**

排查日志查看用户取消流程。

[]()[]()

#### 1010200006 设备远端匹配的手表无法连接

**错误信息**

The device's remote paired watch cannot be connected.

**错误描述**

设备远端匹配的手表无法连接。

**可能原因**

设备远端匹配的手表无法连接。

**处理步骤**

排查手表设备的连接状态。

[]()[]()

#### 1010200007 操作系统版本过低

**错误信息**

The OS version is too old. Please upgrade the OS version.

**错误描述**

设备操作系统版本过低。

**可能原因**

设备操作系统版本过低。

**处理步骤**

升级设备操作系统。

[]()[]()

#### 1010200008 钱包应用版本过低

**错误信息**

The wallet version is too old. Please upgrade the wallet version.

**错误描述**

钱包应用版本过低。

**可能原因**

钱包应用版本过低。

**处理步骤**

升级钱包应用。

[]()[]()

#### 1010200009 无可用的芯片空间

**错误信息**

The chip space is full, and no more cards can be added.

**错误描述**

无可用的芯片空间。

**可能原因**

设备的芯片空间已满。

**处理步骤**

1. 删除钱包无用的卡片

2. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1010200010 网络连接失败

**错误信息**

Network connection error.

**错误描述**

网络连接失败。

**可能原因**

无网络。

**处理步骤**

开启网络，重新连接。

[]()[]()

#### 1010200011 钱包应用环境初始化失败

**错误信息**

Failed to initialize the environment.

**错误描述**

钱包应用环境初始化失败。

**可能原因**

1. 用户没有同意协议。
1. 用户没有登录华为账号。

**处理步骤**

1. 打开钱包并同意协议。
1. 登录华为账号。

[]()[]()

#### 1010200012 重复请求

**错误信息**

Duplicate request.

**错误描述**

重复请求。

**可能原因**

上一次请求没有结束，又重新发起请求。

**处理步骤**

上一次的请求结束后再重新发起请求。

[]()[]()

#### 1010200013 钱包应用内部异常

**错误信息**

Operation failed because of an internal error.

**错误描述**

钱包应用内部异常。

**可能原因**

钱包应用内部问题。

**处理步骤**

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1010200014 钱包应用非机主用户检测

**错误信息**

The Wallet APIs can be called by the device owner only.

**错误描述**

机主用户检测到非机主用户。

**可能原因**

用户切换了访客或者隐私空间。

**处理步骤**

切换到机主用户。

[]()[]()

#### 1010200015 儿童账号不支持此卡片

**错误信息**

This card is not available for a child account.

**错误描述**

儿童账号不支持此卡片。

**可能原因**

账号切换到了儿童账号。

**处理步骤**

切换账号。

[]()[]()

#### 1010200016 此卡不适用于当前国家或地区

**错误信息**

This card is not available for the current country or region.

**错误描述**

此卡不适用于当前国家或地区。

**可能原因**

用户当前服务地未配置交通卡。

**处理步骤**

切换用户服务地到国内。

[]()[]()

#### 1010200017 钱包被用户关闭

**错误信息**

The Wallet app was closed by the user.

**错误描述**

钱包APP被用户关闭。

**可能原因**

用户主动关闭钱包APP。

**处理步骤**

重新点击桌面图标打开钱包APP。

[]()[]()

#### 1010210102 校验token失败

**错误信息**

Failed to verify the caller token.

**错误描述**

Caller Token校验失败。

**可能原因**

传入的token错误。

**处理步骤**

检查token是否正确。

[]()[]()

#### 1010220002 卡片已存在

**错误信息**

The card already exists in the specified device.

**错误描述**

卡片已存在。

**可能原因**

设备已开通此卡片。

**处理步骤**

删除此卡片。

[]()[]()

#### 1010220003 服务器暂时停服

**错误信息**

Pass service is temporarily unavailable.

**错误描述**

服务器暂时停服。

**可能原因**

网络问题或是服务器故障。

**处理步骤**

查看网络是否正常，尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1010220004 卡券不存在当前设备

**错误信息**

The card does not exist in the specified device.

**错误描述**

卡券不存在当前设备。

**可能原因**

卡券被删除或是未开通。

**处理步骤**

先开通此卡券。

[]()[]()

#### 1010220005 卡片数量已经达到了最大开卡上限

**错误信息**

The number of cards has reached the upper limit.

**错误描述**

卡片个数已经达到了开卡数量的最大值。

**可能原因**

卡片个数已达上限。

**处理步骤**

删除不使用的卡片。

[]()[]()

#### 1010220006 蓝牙权限未被同意

**错误信息**

Bluetooth permission is not granted.

**错误描述**

蓝牙连接操作需要用户授权钱包应用。

**可能原因**

蓝牙权限未打开。

**处理步骤**

打开蓝牙权限。

[]()[]()

#### 1010220401 开卡时签名校验失败

**错误信息**

Failed to add the card because the signature verification failed.

**错误描述**

开卡时签名校验失败。

**可能原因**

入参签名算法不一致或是签名内容不对。

**处理步骤**

检查入参。

[]()[]()

#### 1010220402 开卡时数据解析失败

**错误信息**

Failed to add the card because the data decryption failed.

**错误描述**

开卡时数据解析失败。

**可能原因**

入参数据加密数据异常。

**处理步骤**

检查入参。

[]()[]()

#### 1010220403 开卡时实例不存在

**错误信息**

Failed to add the card because the instance ID does not exist.

**错误描述**

开卡时实例不存在。

**可能原因**

入参数据实例不存在。

**处理步骤**

检查入参数据实例。

[]()[]()

#### 1010220404 开卡时实例已存在

**错误信息**

Failed to add the card because the instance ID has been used.

**错误描述**

开卡时实例已存在。

**可能原因**

入参数据实例已存在。

**处理步骤**

检查入参数据实例。

[]()[]()

#### 1010220501 查询卡券不存在

**错误信息**

No card that meets the search criteria is found.

**错误描述**

查询卡券不存在。

**可能原因**

查询卡券不存在。

**处理步骤**

检查入参数据服务号，排查代码卡片的开通流程。

[]()[]()

#### 1010220701 卡片无变更信息

**错误信息**

Failed to update the card because no update is detected.

**错误描述**

卡券无变更信息。

**可能原因**

卡券无变更信息。

**处理步骤**

检查卡券更新流程。

[]()[]()

#### 1010220801 证书校验错误导致删卡失败

**错误信息**

Failed to delete the card because the signature verification failed.

**错误描述**

证书校验错误导致删卡失败。

**可能原因**

证书和删除的卡片不匹配。

**处理步骤**

检查卡券删除流程。

[]()[]()

#### 1010221001 配对码无法获取

**错误信息**

Connection failed because the pairing code is not obtained.

**错误描述**

蓝牙连接过程中的配对码无法获取。

**可能原因**

蓝牙链路异常或是蓝牙协议机制异常。

**处理步骤**

检查获取配对码接口应答是否正常。

[]()[]()

#### 1010221101 重复注册监听

**错误信息**

Registration failed because of duplicate register name.

**错误描述**

重复注册监听。

**可能原因**

监听名重复注册。

**处理步骤**

检查监听注册流程。

[]()[]()

#### 1010221201 监听已经解注册

**错误信息**

The registration may have been unregistered before.

**错误描述**

重复解注册监听。

**可能原因**

监听名已被解注册。

**处理步骤**

检查监听解注册流程。

[]()[]()

#### 1010221301 断连导致车控消息失败

**错误信息**

Failed to send the RKE message because of a connection failure.

**错误描述**

蓝牙链路断连导致车控消息发送失败。

**可能原因**

蓝牙链路断连。

**处理步骤**

检查蓝牙连接流程。

[]()[]()

#### 1010221302 认证失败导致车控消息失败

**错误信息**

Failed to send the RKE message because of an authentication failure.

**错误描述**

蓝牙认证失败导致车控消息发送失败。

**可能原因**

蓝牙认证失败。

**处理步骤**

1. 获取蓝牙空口的相关信息，检查认证流程是否有异常。

2. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1010210101 卡状态不正确

**错误信息**

The card status is not correct.

**错误描述**

获取卡信息失败，卡状态不正确。

**可能原因**

当前卡非正常已开通的卡片。

**处理步骤**

调用getCardMetadataInDevice接口检查卡片是否存在。

[]()[]()

#### 1010210119 读取卡数据失败

**错误信息**

Failed to read the card data.

**错误描述**

读取卡数据失败。

**可能原因**

传入的参数错误，卡不存在。

**处理步骤**

调用getCardMetadataInDevice接口检查卡片是否存在。

[]()[]()

#### 1010210201 指定的设备不支持添加参数issuerId指定的卡

**错误信息**

The device does not support adding the card specified by issuerId.

**错误描述**

指定的设备不支持添加参数issuerId指定的卡。

**可能原因**

指定的设备不支持添加参数issuerId指定的卡。

**处理步骤**

检查管理台该设备是否配置了对应issuerId。

[]()[]()

#### 1010210202 指定设备中已存在与参数IssuerId指定的卡冲突的卡

**错误信息**

A card conflicting with the specified card already exists in the device.

**错误描述**

指定设备中已存在与参数IssuerId指定的卡冲突的卡。

**可能原因**

指定设备中已存在与参数IssuerId指定的卡冲突的卡。

**处理步骤**

检查是否重复开卡。

[]()[]()

#### 1010210203 IssuerId指定的卡已存在

**错误信息**

The specified card already exists.

**错误描述**

IssuerId指定的卡已存在。

**可能原因**

IssuerId指定的卡已存在。

**处理步骤**

检查是否重复开卡。

[]()[]()

#### 1010210204 开卡业务暂时下线

**错误信息**

The card addition service is temporarily offline.

**错误描述**

加卡业务暂时下线。

**可能原因**

加卡业务暂时下线。

**处理步骤**

检查开发服务是否正常打开。

[]()[]()

#### 1010210301 addCardToken已过期

**错误信息**

The card adding conditions are not met. The order can be refunded to end the card addition process.

**错误描述**

addCardToken已过期。

**可能原因**

addCardToken已过期。

**处理步骤**

token已经过期，重新调用接口申请。

[]()[]()

#### 1010210302 确认开卡订单失败

**错误信息**

Failed to confirm the order. The order can be refunded to end the card addition process.

**错误描述**

订单确认失败。订单可以退款，结束加卡流程。

**可能原因**

传入的serverOrderId错误或者状态不对，也可能是SP服务器没有给钱包服务器返回正确的数据。

**处理步骤**

检查serverOrderId是否正确，检查serverOrderId的状态是否正确，检查SP服务器是否有按照文档返回数据。

[]()[]()

#### 1010210319 添加卡失败

**错误信息**

Failed to add the card.

**错误描述**

添加卡失败。

**可能原因**

芯片空间不足，写卡失败等。

**处理步骤**

重新判断是否满足开卡条件。

[]()[]()

#### 1010210401 指定的卡不存在

**错误信息**

The specified card does not exist.

**错误描述**

指定的卡不存在。

**可能原因**

指定的卡不存在。

**处理步骤**

检查要充值的卡片是否被删除。

[]()[]()

#### 1010210402 cardNumber指定的卡状态不正确

**错误信息**

The status of the specified card is incorrect.

**错误描述**

cardNumber指定的卡状态不正确。

**可能原因**

cardNumber指定的卡状态不正确。

**处理步骤**

检查卡的状态是否正常。

[]()[]()

#### 1010210403 确认充值订单失败

**错误信息**

Failed to confirm the order. The order can be refunded to end the recharging process.

**错误描述**

订单确认失败。支持订单退款，结束充值流程。

**可能原因**

传入的serverOrderId错误或者状态不对，也可能是SP服务器没有给钱包服务器返回正确的数据。

**处理步骤**

检查serverOrderId是否正确，检查serverOrderId的状态是否正确，检查SP服务器是否有按照文档返回数据。

[]()[]()

#### 1010210419 余额充值失败

**错误信息**

Failed to recharge the card.

**错误描述**

余额充值失败。

**可能原因**

余额充值失败。

**处理步骤**

检查参数是否正确。

[]()[]()

#### 1010210501 指定的卡不存在

**错误信息**

The specified card does not exist.

**错误描述**

指定的卡不存在。

**可能原因**

cardNumber指定的卡不存在。

**处理步骤**

检查cardNumber是否正确。

[]()[]()

#### 1010210502 cardNumber指定的卡状态不正确

**错误信息**

The status of the specified card is incorrect.

**错误描述**

cardNumber指定的卡状态不正确。

**可能原因**

cardNumber指定的卡状态不正确。

**处理步骤**

重新调用updateTransitCard接口。

[]()[]()

#### 1010210503 确认订单失败

**错误信息**

Failed to confirm the order.

**错误描述**

订单确认失败。

**可能原因**

传入的serverOrderId错误或者状态不对，也可能是SP服务器没有给钱包服务器返回正确的数据。

**处理步骤**

检查serverOrderId是否正确，检查serverOrderId的状态是否正确，检查SP服务器是否有按照文档返回数据。

[]()[]()

#### 1010210519 卡更新失败

**错误信息**

Failed to update the card data.

**错误描述**

卡更新失败。

**可能原因**

卡更新失败。

**处理步骤**

重新调用updateTransitCard接口。

[]()[]()

#### 1010210601 确认订单失败

**错误信息**

Failed to confirm the order.

**错误描述**

订单确认失败。

**可能原因**

传入的serverOrderId错误或者状态不对，也可能是SP服务器没有给钱包服务器返回正确的数据。

**处理步骤**

检查serverOrderId是否正确，检查serverOrderId的状态是否正确，检查SP服务器是否有按照文档返回数据。

[]()[]()

#### 1010210619 删除卡失败

**错误信息**

The card deleting failed.

**错误描述**

删除卡失败。

**可能原因**

删除卡失败。

**处理步骤**

调用getCardMetadataInDevice接口检查卡片是否存在。

[]()[]()

#### 1010210701 校验token失败

**错误信息**

Failed to verify the caller token.

**错误描述**

Caller Token校验失败。

**可能原因**

传入的token错误。

**处理步骤**

检查token是否正确。

[]()[]()

#### 1010210702 无法获取卡的元数据

**错误信息**

Failed to get the metadata of the cards.

**错误描述**

无法获取卡的元数据。

**可能原因**

钱包内部错误，服务器异常等。

**处理步骤**

重新调用接口重试。