[]()[]()

# ArkTS API错误码

以下仅介绍Graphics Accelerate Kit特有错误码，通用错误码请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

[]()[]()

#### 1016600000 当前API不允许在资源加速ExtensionAbility中调用

**错误信息**

The API call from an ExtensionAbility is not allowed.

**错误描述**

当前API不允许在资源加速ExtensionAbility中调用。

**可能原因**

当前API不允许在资源加速ExtensionAbility中调用。

**处理步骤**

请确保当前API在资源加速ExtensionAbility的允许调用范围内。assetDownloadManager提供的接口仅支持调用如下方法：

- [assetDownloadManager.fetchManifestUrl](../topics/misc/assetDownloadManager（资源包下载管理）.md#section81101219425)
- [assetDownloadManager.removeAssetDownloadTask](../topics/misc/assetDownloadManager（资源包下载管理）.md#section222042984419)
- [assetDownloadManager.fetchAllAssetDownloadTasks](../topics/misc/assetDownloadManager（资源包下载管理）.md#section918114094718)
- [assetDownloadManager.removeAllAssetDownloadTasks](../topics/misc/assetDownloadManager（资源包下载管理）.md#section2809432393)
- [assetDownloadManager.fetchGroupAssetDownloadTasks](../topics/misc/assetDownloadManager（资源包下载管理）.md#section93791016111111)
- [assetDownloadManager.removeGroupAssetDownloadTasks](../topics/misc/assetDownloadManager（资源包下载管理）.md#section641613495177)
- [assetDownloadManager.limitDownloadTaskSpeed](../topics/misc/assetDownloadManager（资源包下载管理）.md#section17279143882113)

[]()[]()

#### 1016600001 下载任务的域名不在域名白名单中

**错误信息**

The domain name of the download task is not in the domain name trustlist.

**错误描述**

下载任务的域名不在域名白名单中。

**可能原因**

下载任务的域名不在域名白名单中。

**处理步骤**

- 三方CDN前往AGC控制台查看已配置的域名白名单，具体操作步骤请参见[创建下载任务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-release#section1494105011355)。
- 华为CDN的域名白名单是基于资源包下载任务自动配置。

[]()[]()

#### 1016600002 暂停/恢复/获取下载任务时任务ID或组ID不存在

**错误信息**

The task ID or group ID entered during operations such as pause, resume, and fetch does not exist.

**错误描述**

暂停/恢复/获取下载任务时任务ID或组ID不存在。

**可能原因**

未查询到可操作的任务ID或组ID。

**处理步骤**

任务ID/组ID不存在，请确保任务ID/组ID的正确性。

[]()[]()

#### 1016600003 当前任务状态不支持当前操作

**错误信息**

The current task status does not support the current operator.

**错误描述**

当前任务状态不支持当前操作。

**可能原因**

当前任务状态和当前操作不匹配，例如恢复一个未暂停的下载任务，暂停一个已暂停的下载任务。

**处理步骤**

对任务调用操作前，判断当前任务的状态，确保任务操作和任务状态匹配，例如调用[fetchAllAssetDownloadTasks](../topics/misc/assetDownloadManager（资源包下载管理）.md#section918114094718)方法查看任务状态信息。

[]()[]()

#### 1016600004 任务队列已满

**错误信息**

The application task queue is full.

**错误描述**

任务队列已满。

**可能原因**

资源包下载任务的队列超过200个。

**处理步骤**

请在任务队列有空间后再提交任务。

[]()[]()

#### 1016600005 资源加速ExtensionAbility方法执行超时

**错误信息**

Extension life cycle callback execution timed out.

**错误描述**

资源加速ExtensionAbility方法执行超时。

**可能原因**

若资源加速ExtensionAbility方法未在生命周期时长内完成执行，将存在超时问题。

**处理步骤**

通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=201704444384569052&level3=601723606112598571)提交问题，华为工程师会及时处理。

[]()[]()

#### 1016600006 资源加速ExtensionAbility生命周期方法出现异常

**错误信息**

An exception occurs in the callback extension js.

**错误描述**

资源加速ExtensionAbility生命周期方法出现异常。

**可能原因**

资源加速ExtensionAbility内部处理逻辑超时。

**处理步骤**

排查资源加速ExtensionAbility生命周期方法是否存在未捕获异常。

[]()[]()

#### 1016600094 服务异常

**错误信息**

Task service ability error.

**错误描述**

服务异常。

**可能原因**

游戏资源加速服务异常。

**处理步骤**

通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=201704444384569052&level3=601723606112598571)提交问题，华为工程师会及时处理。

[]()[]()

#### 1016600401 参数错误

**错误信息**

Parameter error.

**错误描述**

参数错误。

**可能原因**

输入参数的类型错误或参数值内容错误。

**处理步骤**

检查输入参数是否符合要求，确保无误后再次尝试。