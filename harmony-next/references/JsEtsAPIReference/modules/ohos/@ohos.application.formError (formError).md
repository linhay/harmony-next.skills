# @ohos.application.formError (formError)

formError模块提供获取[卡片错误码](../../errors/卡片错误码.md)的能力。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始不再维护，建议使用[卡片错误码](卡片错误码.md)替代。

#### 导入模块

```ets
import { formError } from '@kit.FormKit';
```

#### 权限

无

#### FormError

枚举，支持的卡片类型。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ERR_COMMON | 1 | 默认错误码。 |
| ERR_PERMISSION_DENY | 2 | 没有操作权限。 |
| ERR_GET_INFO_FAILED | 4 | 查询卡片信息失败。 |
| ERR_GET_BUNDLE_FAILED | 5 | 查询应用信息失败。 |
| ERR_GET_LAYOUT_FAILED | 6 | 查询布局信息失败。 |
| ERR_ADD_INVALID_PARAM | 7 | 无效参数。 |
| ERR_CFG_NOT_MATCH_ID | 8 | 卡片ID不匹配。 |
| ERR_NOT_EXIST_ID | 9 | 卡片ID不存在。 |
| ERR_BIND_PROVIDER_FAILED | 10 | 绑定卡片提供方失败。 |
| ERR_MAX_SYSTEM_FORMS | 11 | 系统卡片实例数量超过限制。 |
| ERR_MAX_INSTANCES_PER_FORM | 12 | 每张卡片实例数量超过限制。 |
| ERR_OPERATION_FORM_NOT_SELF | 13 | 操作非自己应用申请的卡片。 |
| ERR_PROVIDER_DEL_FAIL | 14 | 卡片提供方删除卡片失败。 |
| ERR_MAX_FORMS_PER_CLIENT | 15 | 使用方申请卡片实例数超过限制。 |
| ERR_MAX_SYSTEM_TEMP_FORMS | 16 | 临时卡片实例数超过限制。 |
| ERR_FORM_NO_SUCH_MODULE | 17 | 模块不存在。 |
| ERR_FORM_NO_SUCH_ABILITY | 18 | ability组件不存在。 |
| ERR_FORM_NO_SUCH_DIMENSION | 19 | 卡片尺寸不存在。 |
| ERR_FORM_FA_NOT_INSTALLED | 20 | 卡片所在FA未安装。 |
| ERR_SYSTEM_RESPONSES_FAILED | 30 | 系统服务响应失败。 |
| ERR_FORM_DUPLICATE_ADDED | 31 | 重复添加卡片。 |
| ERR_IN_RECOVERY | 36 | 卡片数据覆盖失败。 |