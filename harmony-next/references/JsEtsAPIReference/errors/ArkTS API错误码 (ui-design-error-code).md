[]()[]()

# ArkTS API错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

[]()[]()

#### 401参数检查失败

**错误信息**

Parameter error. The value of bundleName is incorrect.

Parameter error. The value of layeredDrawableDescriptor is incorrect.

Parameter error. The value of size is incorrect.

Parameter error. The value of hasBorder is incorrect.

Parameter error. The value of pixelMap is incorrect.

Parameter error. The value of mask is incorrect.

Parameter error. The value of icons is incorrect.

Parameter error. The value of parallelNumber is incorrect.

Parameter error. The number of parameters is incorrect.

Parameter error. The type of ttf resource is error, the type must be resource.

Parameter error. The type of json resource is error, the type must be resource.

Parameter error. The ttf resource is null.

Parameter error. The json resource is null.

Parameter error. Load ttf resource failed.

Parameter error. Load json resource failed.

Parameter error. The ttf resource size is zero.

Parameter error. The json resource size is zero.

Parameter error. The json resource schema is incorrect.

**错误描述**

参数检查失败，包括必选参数没有传入，参数类型错误。无论是同步还是异步接口，此类异常大部分都通过同步的方式抛出。

**可能原因**

必选参数没有传入，或者参数类型错误。

**处理步骤**

1、请检查必选参数是否传入，或者传的参数类型是否错误。

2、请检查传入的资源是否为空。

3、请检查传入的JSON资源格式是否正确。

[]()[]()

#### 801 设备类型错误

**错误信息**

Device Type error.

**错误描述**

设备类型错误。

**可能原因**

设备类型错误。

**处理步骤**

请使用支持的设备类型。

[]()[]()

#### 1012600001 并发任务忙碌

**错误信息**

Task is busy.

**错误描述**

并发任务忙碌。

**可能原因**

上一个并发任务还没结束。

**处理步骤**

1、检查 [hdsDrawable.getHdsLayeredIcons](../topics/graphics/hdsDrawable.md#section712131324710)， [hdsDrawable.getHdsIcons](../topics/graphics/hdsDrawable.md#section12429174135913)的调用是否在对应返回结果后再执行，或者使用单次处理的API接口进行处理。

2、通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1012600002 资源大小超过规格限制

**错误信息**

Resource size error. The ttf resource out of size.

Resource size error. The json resource out of size.

**错误描述**

资源大小超过规格限制。

**可能原因**

用户传入的资源大小超过规格限制的大小，限制用户最多自定义10个图标。

**处理步骤**

裁剪接口传入的自定义Symbol图标个数以及配套动效参数个数。

[]()[]()

#### 1012600003 资源解析失败

**错误信息**

Resource error. Parse the ttf resource failed.

Resource error. Parse the json resource failed.

**错误描述**

资源解析失败。

**可能原因**

用户传入的资源内容有误。

**处理步骤**

1、请检查传入的图标资源是否正确。

2、请检查传入的动效参数资源是否正确。