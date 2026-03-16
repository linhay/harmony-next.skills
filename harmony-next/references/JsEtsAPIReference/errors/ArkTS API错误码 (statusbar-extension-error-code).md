[]()[]()

# ArkTS API错误码

以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

[]()[]()

#### 1010710001 图片尺寸不符合要求

**错误信息**

Maximum number of categories reached

**错误描述**

调用添加图标等接口时，传入的图标图片尺寸不符合要求。

**可能原因**

- 未知原因

当前图标尺寸不做严格限制。

**处理步骤**

请更换传入的图片数据或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1010710002 菜单项数量超出限制

**错误信息**

The number of menu items or submenu items exceeds the limit.

**错误描述**

调用添加图标等接口时，传入的菜单项数量超出限制。

**可能原因**

- 传入的所有一级菜单项的数量超过限制上限20
- 传入的某个一级菜单项的子菜单项的数量超过上限20

**处理步骤**

请重新设置一级菜单项和二级菜单项或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1010710003 API调用频繁

**错误信息**

The API is being called too frequently.

**错误描述**

指定API调用频繁。

**可能原因**

addToStatusBar，removeFromStatusBar，updateStatusBarIcon，updateQuickOperationHeight，

updateStatusBarMenu方法调用间隔小于20ms。

**处理步骤**

请注意设置API的调用间隔或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1010710004 无前台窗口不允许移除图标

**错误信息**

The icon cannot be deleted when no window is in the foreground.

**错误描述**

前台无应用窗口，不允许调用removeFromStatusBar移除状态栏图标。

**可能原因**

应用退后台后调用了removeFromStatusBar方法。

**处理步骤**

请注意API的调用时机或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1010710005 字符串长度超出阈值

**错误信息**

The string length exceeds the threshold.

**错误描述**

字串长度超出限制范围。

**可能原因**

- [StatusBarItem](../topics/components/statusBarManager（状态栏管理服务）.md#section105181855219)中配置的hoverTips字符串长度为0或者大于128。
- 调用[updateStatusBarHoverTips](../topics/components/statusBarManager（状态栏管理服务）.md#section0391124717248)方法时传入的字符串长度为0或者大于128。

**处理步骤**

检查传入字符串的长度是否在取值范围中，如果无法解决请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1010720001 传入的一级菜单项数据不满足要求

**错误信息**

A menu item contains neither submenu nor menuAction.

**错误描述**

调用添加图标、更新菜单等接口时，传入的一级菜单项数据不满足要求。

**可能原因**

当前传入的某个一级菜单项既不包含[menuAction](../topics/components/statusBarManager（状态栏管理服务）.md#section3627115133810)，也不包含[subMenu](../topics/components/statusBarManager（状态栏管理服务）.md#section3627115133810)。

**处理步骤**

请排查传入的一级菜单项的参数或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1020210001 菜单分组数量超过限制。

**错误信息**

Maximum number of categories reached.

**错误描述**

调用添加分组接口时，添加的数量超出限制。

**可能原因**

分组最大数量为3，添加的菜单分组数量超过了限制。

**处理步骤**

请重新设置菜单分组的数量或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1020210002 菜单分组名称重复。

**错误信息**

Duplicate category name.

**错误描述**

调用添加分组接口时，传入的分组名称和其他分组名称重复。

**可能原因**

传入的分组名称和已存在的分组名称重复。

**处理步骤**

请重新设置菜单分组的名称或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1020210003 未找到菜单分组。

**错误信息**

Category not found.

**错误描述**

调用获取分组、更新分组、删除分组等接口时，未找到对应的菜单分组。

**可能原因**

- 没有添加菜单分组就去获取所有的菜单分组。
- 更新菜单分组时传入的分组Id有误，未找到对应的菜单分组。
- 删除菜单分组时传入的分组Id有误，未找到对应的菜单分组。
- 获取一个分组下的所有任务时传入的分组Id有误，未找到对应的菜单分组。
- 添加菜单任务时传入的分组Id有误，未找到对应的菜单分组。

**处理步骤**

请重新设置已存在的分组Id或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1020210004 未找到菜单任务。

**错误信息**

Quick task not found.

**错误描述**

调用获取任务、更新任务、删除任务等接口时，未找到对应的菜单任务。

**可能原因**

- 删除菜单任务时传入的任务Id有误，未找到对应的菜单任务。
- 获取一个分组下的所有任务时，获取的任务数量为0。
- 更新菜单任务时传入的任务Id有误，未找到对应的菜单任务。

**处理步骤**

请重新设置已存在的任务Id或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1020210008 字符串长度超出限制。

**错误信息**

The string length exceeds the threshold.

**错误描述**

传入的字符串参数的长度超过限制。

**可能原因**

- 调用[addCustomCategory](../topics/components/quickBarManager（快捷栏管理服务）.md#section665018220561)方法时传入的字符串长度为0或者大于512。
- 调用[updateCustomCategory](../topics/components/quickBarManager（快捷栏管理服务）.md#section1623472312366)方法时传入的字符串长度为0或者大于512。
- 调用[addQuickTask](../topics/components/quickBarManager（快捷栏管理服务）.md#section13991750101114)方法时传入的字符串长度为0或者大于512。
- 调用[updateQuickTask](../topics/components/quickBarManager（快捷栏管理服务）.md#section1427319917408)方法时传入的字符串长度为0或者大于512。

**处理步骤**

请重新设置字符串的长度或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1020210009 无效的parameter。

**错误信息**

Invalid parameter.

**错误描述**

传入的parameters参数的数组大小超过限制。

**可能原因**

- 调用[addQuickTask](../topics/components/quickBarManager（快捷栏管理服务）.md#section13991750101114)方法时传入的parameters参数的数组大小超过64。
- 调用[updateQuickTask](../topics/components/quickBarManager（快捷栏管理服务）.md#section1427319917408)方法时传入的parameters参数的数组大小超过64。

**处理步骤**

请重新设置parameters参数的数组大小或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。