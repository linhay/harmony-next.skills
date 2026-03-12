# @system.storage (数据存储)

-

从API Version 6开始，该模块不再维护，可以使用模块[@ohos.data.storage](@ohos.data.storage (轻量级存储).md)。在API Version 9后，推荐使用新模块[@ohos.data.preferences](@ohos.data.preferences (用户首选项).md)。

-

本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本模块接口仅可在FA模型下使用。

#### 导入模块

```ets
import storage from '@system.storage';
```

#### storage.get

get(options: GetStorageOptions): void

通过索引读取缓存中存储的值。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**参数：**

参数名类型必填说明options[GetStorageOptions](#ZH-CN_TOPIC_0000002497444714__getstorageoptions)是接口配置信息。

**示例：**

```ets
export default {
  storageGet() {
    storage.get({
      key: 'storage_key',
      success: function(data) {
        console.log('call storage.get success: ' + data);
      },
      fail: function(data, code) {
        console.log('call storage.get fail, code: ' + code + ', data: ' + data);
      },
      complete: function() {
        console.log('call complete');
      },
    });
  }
}
```

#### storage.set

set(options: SetStorageOptions): void

修改缓存中索引对应的值。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**参数：**

参数名类型必填说明options[SetStorageOptions](#ZH-CN_TOPIC_0000002497444714__setstorageoptions)是接口配置信息。

**示例：**

```ets
export default {
  storageSet() {
    storage.set({
      key: 'storage_key',
      value: 'storage value',
      success: function() {
        console.log('call storage.set success.');
      },
      fail: function(data, code) {
        console.log('call storage.set fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### storage.clear

clear(options?: ClearStorageOptions): void

清空缓存中存储的键值对。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**参数：**

参数名类型必填说明options[ClearStorageOptions](#ZH-CN_TOPIC_0000002497444714__clearstorageoptions)否接口配置信息。

**示例：**

```ets
export default {
  storageClear() {
    storage.clear({
      success: function() {
        console.log('call storage.clear success.');
      },
      fail: function(data, code) {
        console.log('call storage.clear fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### storage.delete

delete(options: DeleteStorageOptions): void

删除缓存中索引对应的键值对。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**参数：**

参数名类型必填说明options[DeleteStorageOptions](#ZH-CN_TOPIC_0000002497444714__deletestorageoptions)是接口配置信息。

**示例：**

```ets
export default {
  storageDelete() {
    storage.delete({
      key: 'Storage1',
      success: function() {
        console.log('call storage.delete success.');
      },
      fail: function(data, code) {
        console.log('call storage.delete fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

#### GetStorageOptions

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

名称类型必填说明keystring是内容索引。defaultstring否key不存在则返回的默认值。success(data: any) => void否接口调用成功的回调函数，data为返回key对应的value。fail(data: string, code: number) => void否接口调用失败的回调函数，data为错误信息，code为错误码。complete() => void否接口调用结束的回调函数。

#### SetStorageOptions

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

名称类型必填说明keystring是要修改的存储值的索引。valuestring是新值。长度需小于128字节。success() => void否接口调用成功的回调函数。fail(data: string, code: number) => void否接口调用失败的回调函数，data为错误信息，code为错误码。complete() => void否接口调用结束的回调函数。

#### ClearStorageOptions

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

名称类型必填说明success() => void否接口调用成功的回调函数。fail(data: string, code: number) => void否接口调用失败的回调函数，data为错误信息，code为错误码。complete() => void否接口调用结束的回调函数。

#### DeleteStorageOptions

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

名称类型必填说明keystring是内容索引。success() => void否接口调用成功的回调函数。fail(data: string, code: number) => void否接口调用失败的回调函数，data为错误信息，code为错误码。complete() => void否接口调用结束的回调函数。