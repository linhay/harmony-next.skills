# Types

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**MemberType**

type MemberType = number | string | boolean

PhotoAsset的成员类型。

成员类型为下表类型的并集。

系统能力：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 类型 | 说明 |
| --- | --- |
| number | 表示值类型为数字，可取任意值。 |
| string | 表示值类型为字符，可取任意值。 |
| boolean | 表示值类型为布尔类型。 |

**PhotoAssetParams21+**

type PhotoAssetParams = Record<string, MemberType>[]

文件属性名称及其值的Record类型数组。

系统能力: SystemCapability.FileManagement.PhotoAccessHelper.Core

| 类型 | 说明 |
| --- | --- |
| Record<string, MemberType>[] | 文件属性名称及其值的Record类型数组。 |

**OperationValueType22+**

type OperationValueType = number | string | boolean

表示不同谓词所需要匹配的值。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 22开始，该接口支持在元服务中使用。

系统能力： SystemCapability.FileManagement.PhotoAccessHelper.Core

| 类型 | 说明 |
| --- | --- |
| number | 表示字段类型为数字，可取任意值。 |
| string | 表示字段类型为字符串，可取任意值。 |
| boolean | 表示字段类型为布尔值。 |