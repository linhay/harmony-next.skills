[]()[]()

# ArkTS错误码

以下仅介绍本模块返回的错误码， 若错误信息中返回了其他错误码请参考下述链接：

- [云函数](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-References/errorcode-nodejs-0000001733038624)
- [云存储](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-References/0000001057683679-0000001056723660)
- [云数据库](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-Guides/agc-clouddb-error-code-0000001117436042)

[]()[]()

#### 201 没有网络权限

**错误信息**

No Internet permission.

**错误描述**

网络权限未开启。

**可能原因**

工程中未设置开启网络权限。

**处理步骤**

在工程的module.json5文件中添加如下代码开启网络权限。

```ets
"requestPermissions": [
  {
    "name": "ohos.permission.INTERNET"
  }
]
```

[]()[]()

#### 401 参数错误

**错误信息**

Parameter error.

**错误描述**

执行API时传入参数错误。

**可能原因**

1. 入参类型与方法中定义不符。
1. 入参取值超出方法参数定义的范围。

**处理步骤**

检查入参类型和入参取值。

[]()[]()

#### 1008210001 云函数网络连接错误

**错误信息**

Network connection error.

**错误描述**

云函数网络连接错误。

**可能原因**

1. 网络连接了代理。
1. 当前设备无网络。

**处理步骤**

检查设备网络连接情况。

[]()[]()

#### 1008210009 云函数客户端内部错误

**错误信息**

Client internal error.

**错误描述**

云函数客户端内部错误。

**可能原因**

客户端内部错误。

**处理步骤**

请通过[在线工单系统](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101723605535783370&keyWord=Cloud Foundation Kit&channel=ICS0000)联系技术支持人员定位问题。

[]()[]()

#### 1008211001 云函数服务器侧错误

**错误信息**

Server error.

**错误描述**

云函数服务器侧出现错误。

**可能原因**

云函数服务器出现异常，或认证失败。

**处理步骤**

请通过[在线工单系统](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101723605535783370&keyWord=Cloud Foundation Kit&channel=ICS0000)联系技术支持人员定位问题。

[]()[]()

#### 1008220001 云存储网络连接错误

**错误信息**

Network connection error.

**错误描述**

云存储网络连接错误。

**可能原因**

1. 网络连接了代理。
1. 当前设备无网络。

**处理步骤**

检查设备网络连接情况 。

[]()[]()

#### 1008220009 云存储客户端内部错误

**错误信息**

Client internal error.

**错误描述**

云存储客户端内部错误。

**可能原因**

客户端内部错误。

**处理步骤**

请通过[在线工单系统](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101723605535783370&keyWord=Cloud Foundation Kit&channel=ICS0000)联系技术支持人员定位问题。

[]()[]()

#### 1008221001 云存储云侧执行错误

**错误信息**

Server error.

**错误描述**

云存储云侧执行错误。

**可能原因**

云存储客户端请求的云侧文件不存在，云侧安全规则配置不正确，或认证失败等。

**处理步骤**

根据错误信息，检查云侧资源以及请求是否正确。

[]()[]()

#### 1008230001 云数据库网络连接错误

**错误信息**

Network connection error.

**错误描述**

云数据库网络连接错误。

**可能原因**

1. 网络连接了代理。
1. 当前设备无网络。

**处理步骤**

检查设备网络连接情况。

[]()[]()

#### 1008230009 云数据库客户端内部错误

**错误信息**

Client internal error.

**错误描述**

云数据库客户端内部错误。

**可能原因**

客户端内部错误。

**处理步骤**

请通过[在线工单系统](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101723605535783370&keyWord=Cloud Foundation Kit&channel=ICS0000)联系技术支持人员定位问题。

[]()[]()

#### 1008230002 云数据库schema配置错误

**错误信息**

Schema config error.

**错误描述**

云数据库schema.json文件配置错误。

**可能原因**

1. schema.json文件不存在或者路径错误。
1. schema.json文件中的存储对象和代码中创建的存储对象不一致，可能是云侧存储对象发生了变更，但schema.json文件未重新导出。
1. schema.json文件同时存在于AppScope目录和entry目录中。当开发者在entry目录下的schema.json文件中更新了存储对象，在编译构建过程中，这些更新会被AppScope目录下的 schema.json文件覆盖。详细信息请参见[资源分类](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resource-categories-and-access#资源分类)。

**处理步骤**

1. 将schema.json文件下载后放在rawfile目录下。
1. 参见[引入对象类型文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-database-add-file)，确保schema.json文件中对象和代码中创建的存储对象一致。
1. 将entry目录下的schema.json文件移动到AppScope目录下进行维护。

[]()[]()

#### 1008230003 云数据库代码对象错误

**错误信息**

Natural object error.

**错误描述**

云数据库代码对象错误。

**可能原因**

查询代码中传入的存储对象名称和实际是否相符。

**处理步骤**

检查传入存储对象名称参数和实际存储对象名称是否一致。

[]()[]()

#### 1008231001 云数据库服务器侧错误

**错误信息**

Server error.

**错误描述**

云数据库服务器侧出现错误。

**可能原因**

云数据库服务器出现异常，或认证失败。

**处理步骤**

请通过[在线工单系统](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101723605535783370&keyWord=Cloud Foundation Kit&channel=ICS0000)联系技术支持人员定位问题。

[]()[]()

#### 1008240009 预加载客户端内部错误

**错误信息**

Client internal error.

**错误描述**

预加载客户端内部错误。

**可能原因**

客户端内部错误。

**处理步骤**

请通过[在线工单系统](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101723605535783370&keyWord=Cloud Foundation Kit&channel=ICS0000)联系技术支持人员定位问题。