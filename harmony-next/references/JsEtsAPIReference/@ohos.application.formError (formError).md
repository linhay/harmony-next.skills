# @ohos.application.formError (formError)

formError模块提供获取卡片错误码的能力。

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

名称值说明ERR_COMMON1默认错误码。ERR_PERMISSION_DENY2没有操作权限。ERR_GET_INFO_FAILED4查询卡片信息失败。ERR_GET_BUNDLE_FAILED5查询应用信息失败。ERR_GET_LAYOUT_FAILED6查询布局信息失败。ERR_ADD_INVALID_PARAM7无效参数。ERR_CFG_NOT_MATCH_ID8卡片ID不匹配。ERR_NOT_EXIST_ID9卡片ID不存在。ERR_BIND_PROVIDER_FAILED10绑定卡片提供方失败。ERR_MAX_SYSTEM_FORMS11系统卡片实例数量超过限制。ERR_MAX_INSTANCES_PER_FORM12每张卡片实例数量超过限制。ERR_OPERATION_FORM_NOT_SELF13操作非自己应用申请的卡片。ERR_PROVIDER_DEL_FAIL14卡片提供方删除卡片失败。ERR_MAX_FORMS_PER_CLIENT15使用方申请卡片实例数超过限制。ERR_MAX_SYSTEM_TEMP_FORMS16临时卡片实例数超过限制。ERR_FORM_NO_SUCH_MODULE17模块不存在。ERR_FORM_NO_SUCH_ABILITY18ability组件不存在。ERR_FORM_NO_SUCH_DIMENSION19卡片尺寸不存在。ERR_FORM_FA_NOT_INSTALLED20卡片所在FA未安装。ERR_SYSTEM_RESPONSES_FAILED30系统服务响应失败。ERR_FORM_DUPLICATE_ADDED31重复添加卡片。ERR_IN_RECOVERY36卡片数据覆盖失败。