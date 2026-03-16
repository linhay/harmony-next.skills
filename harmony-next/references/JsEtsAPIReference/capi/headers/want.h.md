# want.h

#### 概述

Want是对象间信息传递的载体，可以用于应用组件间的信息传递。 Want的使用场景之一是作为startAbility的参数，其包含了指定的启动目标，以及启动时需携带的相关数据，如bundleName和abilityName字段分别指明目标Ability所在应用的Bundle名称以及对应包内的Ability名称。当Ability A需要启动Ability B并传入一些数据时，可使用Want作为载体将这些数据传递给Ability B。

**引用文件：** <AbilityKit/ability_base/want.h>

**库：** libability_base_want.so

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 15

**相关模块：**[AbilityBase](../../topics/system-services/AbilityBase.md)

#### 汇总

#### 结构体

名称typedef关键字描述[AbilityBase_Element](../../topics/system-services/AbilityBase_Element.md)AbilityBase_Element声明Want中Element结构体。[AbilityBase_Want](../../topics/system-services/AbilityBase_Want.md)AbilityBase_Want声明Want数据结构。

#### 函数

名称描述[AbilityBase_Want* OH_AbilityBase_CreateWant(AbilityBase_Element element)](#ZH-CN_TOPIC_0000002529284653__oh_abilitybase_createwant)创建Want。[AbilityBase_ErrorCode OH_AbilityBase_DestroyWant(AbilityBase_Want* want)](#ZH-CN_TOPIC_0000002529284653__oh_abilitybase_destroywant)销毁Want。销毁后的Want不可使用，否则会导致未定义行为。[AbilityBase_ErrorCode OH_AbilityBase_SetWantElement(AbilityBase_Want* want, AbilityBase_Element element)](#ZH-CN_TOPIC_0000002529284653__oh_abilitybase_setwantelement)设置Want中由bundleName、moduleName与abilityName组成的Element结构体。[AbilityBase_ErrorCode OH_AbilityBase_GetWantElement(AbilityBase_Want* want, AbilityBase_Element* element)](#ZH-CN_TOPIC_0000002529284653__oh_abilitybase_getwantelement)获取Want中由bundleName、moduleName与abilityName组成的Element结构体。[AbilityBase_ErrorCode OH_AbilityBase_SetWantCharParam(AbilityBase_Want* want, const char* key, const char* value)](#ZH-CN_TOPIC_0000002529284653__oh_abilitybase_setwantcharparam)设置Want Param参数。[AbilityBase_ErrorCode OH_AbilityBase_GetWantCharParam(AbilityBase_Want* want, const char* key,char* value, size_t valueSize)](#ZH-CN_TOPIC_0000002529284653__oh_abilitybase_getwantcharparam)获取Want Param参数。[AbilityBase_ErrorCode OH_AbilityBase_AddWantFd(AbilityBase_Want* want, const char* key, int32_t fd)](#ZH-CN_TOPIC_0000002529284653__oh_abilitybase_addwantfd)添加Want文件描述符。[AbilityBase_ErrorCode OH_AbilityBase_GetWantFd(AbilityBase_Want* want, const char* key, int32_t* fd)](#ZH-CN_TOPIC_0000002529284653__oh_abilitybase_getwantfd)获取Want文件描述符。[AbilityBase_ErrorCode OH_AbilityBase_SetWantUri(AbilityBase_Want* want, const char* uri)](#ZH-CN_TOPIC_0000002529284653__oh_abilitybase_setwanturi)设置Want中URI字符串。[AbilityBase_ErrorCode OH_AbilityBase_GetWantUri(AbilityBase_Want* want, char* uri, size_t uriSize)](#ZH-CN_TOPIC_0000002529284653__oh_abilitybase_getwanturi)获取Want中URI字符串。URI可参考[Want中uri描述](../../modules/ohos/@ohos.app.ability.Want (Want).md)。[AbilityBase_ErrorCode OH_AbilityBase_SetWantInt32Param(AbilityBase_Want* want, const char* key, int32_t value)](#ZH-CN_TOPIC_0000002529284653__oh_abilitybase_setwantint32param)设置Want中int32_t类型的值。[AbilityBase_ErrorCode OH_AbilityBase_GetWantInt32Param(AbilityBase_Want* want, const char* key, int32_t* value)](#ZH-CN_TOPIC_0000002529284653__oh_abilitybase_getwantint32param)获取Want中int32_t类型的值。[AbilityBase_ErrorCode OH_AbilityBase_SetWantBoolParam(AbilityBase_Want* want, const char* key, bool value)](#ZH-CN_TOPIC_0000002529284653__oh_abilitybase_setwantboolparam)设置Want中bool类型的值。[AbilityBase_ErrorCode OH_AbilityBase_GetWantBoolParam(AbilityBase_Want* want, const char* key, bool* value)](#ZH-CN_TOPIC_0000002529284653__oh_abilitybase_getwantboolparam)获取Want中bool类型的值。[AbilityBase_ErrorCode OH_AbilityBase_SetWantDoubleParam(AbilityBase_Want* want, const char* key, double value)](#ZH-CN_TOPIC_0000002529284653__oh_abilitybase_setwantdoubleparam)设置Want中double类型的值。[AbilityBase_ErrorCode OH_AbilityBase_GetWantDoubleParam(AbilityBase_Want* want, const char* key, double* value)](#ZH-CN_TOPIC_0000002529284653__oh_abilitybase_getwantdoubleparam)获取Want中double类型的值。

#### 函数说明

#### OH_AbilityBase_CreateWant()

```ets
AbilityBase_Want* OH_AbilityBase_CreateWant(AbilityBase_Element element)
```

**描述**

创建Want。

**起始版本：** 15

**参数：**

参数项描述[AbilityBase_Element](../../topics/system-services/AbilityBase_Element.md) elementElement数据结构。

**返回：**

类型说明[AbilityBase_Want](../../topics/system-services/AbilityBase_Want.md)*返回want数据结构。

#### OH_AbilityBase_DestroyWant()

```ets
AbilityBase_ErrorCode OH_AbilityBase_DestroyWant(AbilityBase_Want* want)
```

**描述**

销毁Want。销毁后的Want不可使用，否则会导致未定义行为。

**起始版本：** 15

**参数：**

参数项描述[AbilityBase_Want](../../topics/system-services/AbilityBase_Want.md)* wantWant指针。

**返回：**

类型说明[AbilityBase_ErrorCode](ability_base_common.h.md#ZH-CN_TOPIC_0000002529444623__abilitybase_errorcode)

返回执行结果。

ABILITY_BASE_ERROR_CODE_NO_ERROR - 销毁want成功。

ABILITY_BASE_ERROR_CODE_PARAM_INVALID - element参数无效。

#### OH_AbilityBase_SetWantElement()

```ets
AbilityBase_ErrorCode OH_AbilityBase_SetWantElement(AbilityBase_Want* want, AbilityBase_Element element)
```

**描述**

设置Want中由bundleName、moduleName与abilityName组成的Element结构体。

**起始版本：** 15

**参数：**

参数项描述[AbilityBase_Want](../../topics/system-services/AbilityBase_Want.md)* wantWant指针。[AbilityBase_Element](../../topics/system-services/AbilityBase_Element.md) elementElement结构体。

**返回：**

类型说明[AbilityBase_ErrorCode](ability_base_common.h.md#ZH-CN_TOPIC_0000002529444623__abilitybase_errorcode)

返回执行结果。

ABILITY_BASE_ERROR_CODE_NO_ERROR - 设置element成功。

ABILITY_BASE_ERROR_CODE_PARAM_INVALID - want为空，element参数无效。

#### OH_AbilityBase_GetWantElement()

```ets
AbilityBase_ErrorCode OH_AbilityBase_GetWantElement(AbilityBase_Want* want, AbilityBase_Element* element)
```

**描述**

获取Want中由bundleName、moduleName与abilityName组成的Element结构体。

**起始版本：** 15

**参数：**

参数项描述[AbilityBase_Want](../../topics/system-services/AbilityBase_Want.md)* wantWant指针。[AbilityBase_Element](../../topics/system-services/AbilityBase_Element.md)* elementElement结构体。

**返回：**

类型说明[AbilityBase_ErrorCode](ability_base_common.h.md#ZH-CN_TOPIC_0000002529444623__abilitybase_errorcode)

返回执行结果。

ABILITY_BASE_ERROR_CODE_NO_ERROR - 获取element成功。

ABILITY_BASE_ERROR_CODE_PARAM_INVALID - want为空，element参数无效。

#### OH_AbilityBase_SetWantCharParam()

```ets
AbilityBase_ErrorCode OH_AbilityBase_SetWantCharParam(AbilityBase_Want* want, const char* key, const char* value)
```

**描述**

设置Want Param参数，Param可参考[Want中的parameters参数](../../topics/misc/Want.md)。

**起始版本：** 15

**参数：**

参数项描述[AbilityBase_Want](../../topics/system-services/AbilityBase_Want.md)* wantWant指针。const char* keyWant中字符串参数索引。const char* valueWant中字符串。

**返回：**

类型说明[AbilityBase_ErrorCode](ability_base_common.h.md#ZH-CN_TOPIC_0000002529444623__abilitybase_errorcode)

返回执行结果。

ABILITY_BASE_ERROR_CODE_NO_ERROR - 设置param成功。

ABILITY_BASE_ERROR_CODE_PARAM_INVALID - want为空或非法入参。

#### OH_AbilityBase_GetWantCharParam()

```ets
AbilityBase_ErrorCode OH_AbilityBase_GetWantCharParam(AbilityBase_Want* want, const char* key,char* value, size_t valueSize)
```

**描述**

获取[OH_AbilityBase_SetWantCharParam](#ZH-CN_TOPIC_0000002529284653__oh_abilitybase_setwantcharparam)方法设置的Want Param参数。

**起始版本：** 15

**参数：**

参数项描述[AbilityBase_Want](../../topics/system-services/AbilityBase_Want.md)* wantWant指针。const char* keyWant中字符串参数索引。char* valueWant中字符串。size_t valueSizevalue字符串长度。如果valueSize小于实际需要获取的value长度，则会报[ABILITY_BASE_ERROR_CODE_PARAM_INVALID](ability_base_common.h.md#ZH-CN_TOPIC_0000002529444623__abilitybase_errorcode)错误。

**返回：**

类型说明[AbilityBase_ErrorCode](ability_base_common.h.md#ZH-CN_TOPIC_0000002529444623__abilitybase_errorcode)

返回执行结果。

ABILITY_BASE_ERROR_CODE_NO_ERROR - 获取param成功。

ABILITY_BASE_ERROR_CODE_PARAM_INVALID - want为空或非法入参。

#### OH_AbilityBase_AddWantFd()

```ets
AbilityBase_ErrorCode OH_AbilityBase_AddWantFd(AbilityBase_Want* want, const char* key, int32_t fd)
```

**描述**

添加Want文件描述符，文件描述符可通过[fs.open](../../modules/ohos/@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002529445221__fsopen)获取。

**起始版本：** 15

**参数：**

参数项描述[AbilityBase_Want](../../topics/system-services/AbilityBase_Want.md)* wantWant指针。const char* keyWant中字符串参数索引。int32_t fd文件描述符，可通过[fs.open](../../modules/ohos/@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002529445221__fsopen)获取。

**返回：**

类型说明[AbilityBase_ErrorCode](ability_base_common.h.md#ZH-CN_TOPIC_0000002529444623__abilitybase_errorcode)

返回执行结果。

ABILITY_BASE_ERROR_CODE_NO_ERROR - 添加want文件描述符成功。

ABILITY_BASE_ERROR_CODE_PARAM_INVALID - want为空或非法入参。

#### OH_AbilityBase_GetWantFd()

```ets
AbilityBase_ErrorCode OH_AbilityBase_GetWantFd(AbilityBase_Want* want, const char* key, int32_t* fd)
```

**描述**

获取Want文件描述符。

**起始版本：** 15

**参数：**

参数项描述[AbilityBase_Want](../../topics/system-services/AbilityBase_Want.md)* wantWant指针。const char* keyWant中字符串参数索引。int32_t* fd文件描述符。

**返回：**

类型说明[AbilityBase_ErrorCode](ability_base_common.h.md#ZH-CN_TOPIC_0000002529444623__abilitybase_errorcode)

返回执行结果。

ABILITY_BASE_ERROR_CODE_NO_ERROR - 获取want文件描述符成功。

ABILITY_BASE_ERROR_CODE_PARAM_INVALID - want为空或非法入参。

#### OH_AbilityBase_SetWantUri()

```ets
AbilityBase_ErrorCode OH_AbilityBase_SetWantUri(AbilityBase_Want* want, const char* uri)
```

**描述**

设置Want中URI字符串，URI可参考[Want中URI描述](../../modules/ohos/@ohos.app.ability.Want (Want).md)。

**起始版本：** 17

**参数：**

参数项描述[AbilityBase_Want](../../topics/system-services/AbilityBase_Want.md)* wantWant指针。const char* uri表示URI。如果在Want中指定了URI，则Want将匹配指定的URI信息。URI可参考[Want中URI描述](../../modules/ohos/@ohos.app.ability.Want (Want).md)。

**返回：**

类型说明[AbilityBase_ErrorCode](ability_base_common.h.md#ZH-CN_TOPIC_0000002529444623__abilitybase_errorcode)

返回执行结果。

ABILITY_BASE_ERROR_CODE_NO_ERROR - 设置want中uri字符串成功。

ABILITY_BASE_ERROR_CODE_PARAM_INVALID - want为空或非法入参。

#### OH_AbilityBase_GetWantUri()

```ets
AbilityBase_ErrorCode OH_AbilityBase_GetWantUri(AbilityBase_Want* want, char* uri, size_t uriSize)
```

**描述**

获取Want中URI字符串。URI可参考[Want中URI描述](../../modules/ohos/@ohos.app.ability.Want (Want).md)。

**起始版本：** 17

**参数：**

参数项描述[AbilityBase_Want](../../topics/system-services/AbilityBase_Want.md)* wantWant指针。char* uri表示URI。如果在Want中指定了URI，则Want将匹配指定的URI信息。URI可参考[Want中URI描述](../../modules/ohos/@ohos.app.ability.Want (Want).md)。size_t uriSizeURI字符串长度。如果uriSize小于实际需要获取的URI长度，则会报[ABILITY_BASE_ERROR_CODE_PARAM_INVALID](ability_base_common.h.md#ZH-CN_TOPIC_0000002529444623__abilitybase_errorcode)错误。

**返回：**

类型说明[AbilityBase_ErrorCode](ability_base_common.h.md#ZH-CN_TOPIC_0000002529444623__abilitybase_errorcode)

返回执行结果。

ABILITY_BASE_ERROR_CODE_NO_ERROR - 获取want中URI字符串成功。

ABILITY_BASE_ERROR_CODE_PARAM_INVALID - want为空或非法入参。

#### OH_AbilityBase_SetWantInt32Param()

```ets
AbilityBase_ErrorCode OH_AbilityBase_SetWantInt32Param(AbilityBase_Want* want, const char* key, int32_t value)
```

**描述**

设置Want中int32_t类型的值。

**起始版本：** 17

**参数：**

参数项描述[AbilityBase_Want](../../topics/system-services/AbilityBase_Want.md)* wantWant指针。const char* keyWant中int32_t类型值的参数索引。int32_t valueWant中int32_t类型的值。

**返回：**

类型说明[AbilityBase_ErrorCode](ability_base_common.h.md#ZH-CN_TOPIC_0000002529444623__abilitybase_errorcode)

返回执行结果。

ABILITY_BASE_ERROR_CODE_NO_ERROR - 设置want中int32_t类型的值成功。

ABILITY_BASE_ERROR_CODE_PARAM_INVALID - want为空或非法入参。

#### OH_AbilityBase_GetWantInt32Param()

```ets
AbilityBase_ErrorCode OH_AbilityBase_GetWantInt32Param(AbilityBase_Want* want, const char* key, int32_t* value)
```

**描述**

获取Want中int32_t类型的值。

**起始版本：** 17

**参数：**

参数项描述[AbilityBase_Want](../../topics/system-services/AbilityBase_Want.md)* wantWant指针。const char* keyWant中int32_t类型值的参数索引。int32_t* valueWant中int32_t类型的值。

**返回：**

类型说明[AbilityBase_ErrorCode](ability_base_common.h.md#ZH-CN_TOPIC_0000002529444623__abilitybase_errorcode)

返回执行结果。

ABILITY_BASE_ERROR_CODE_NO_ERROR - 获取want中int32_t类型的值成功。

ABILITY_BASE_ERROR_CODE_PARAM_INVALID - want为空或非法入参。

#### OH_AbilityBase_SetWantBoolParam()

```ets
AbilityBase_ErrorCode OH_AbilityBase_SetWantBoolParam(AbilityBase_Want* want, const char* key, bool value)
```

**描述**

设置Want中bool类型的值。

**起始版本：** 17

**参数：**

参数项描述[AbilityBase_Want](../../topics/system-services/AbilityBase_Want.md)* wantWant指针。const char* keyWant中bool类型值的参数索引。bool valueWant中bool类型的值。

**返回：**

类型说明[AbilityBase_ErrorCode](ability_base_common.h.md#ZH-CN_TOPIC_0000002529444623__abilitybase_errorcode)

返回执行结果。

ABILITY_BASE_ERROR_CODE_NO_ERROR - 设置want中bool类型的值成功。

ABILITY_BASE_ERROR_CODE_PARAM_INVALID - want为空或非法入参。

#### OH_AbilityBase_GetWantBoolParam()

```ets
AbilityBase_ErrorCode OH_AbilityBase_GetWantBoolParam(AbilityBase_Want* want, const char* key, bool* value)
```

**描述**

获取Want中bool类型的值。

**起始版本：** 17

**参数：**

参数项描述[AbilityBase_Want](../../topics/system-services/AbilityBase_Want.md)* wantWant指针。const char* keyWant中bool类型值的参数索引。bool* valueWant中bool类型的值。

**返回：**

类型说明[AbilityBase_ErrorCode](ability_base_common.h.md#ZH-CN_TOPIC_0000002529444623__abilitybase_errorcode)

返回执行结果。

ABILITY_BASE_ERROR_CODE_NO_ERROR - 获取want中bool类型的值成功。

ABILITY_BASE_ERROR_CODE_PARAM_INVALID - want为空或非法入参。

#### OH_AbilityBase_SetWantDoubleParam()

```ets
AbilityBase_ErrorCode OH_AbilityBase_SetWantDoubleParam(AbilityBase_Want* want, const char* key, double value)
```

**描述**

设置Want中double类型的值。

**起始版本：** 17

**参数：**

参数项描述[AbilityBase_Want](../../topics/system-services/AbilityBase_Want.md)* wantWant指针。const char* keyWant中double类型值的参数索引。double valueWant中double类型的值。

**返回：**

类型说明[AbilityBase_ErrorCode](ability_base_common.h.md#ZH-CN_TOPIC_0000002529444623__abilitybase_errorcode)

返回执行结果。

ABILITY_BASE_ERROR_CODE_NO_ERROR - 设置want中double类型的值成功。

ABILITY_BASE_ERROR_CODE_PARAM_INVALID - want为空或非法入参。

#### OH_AbilityBase_GetWantDoubleParam()

```ets
AbilityBase_ErrorCode OH_AbilityBase_GetWantDoubleParam(AbilityBase_Want* want, const char* key, double* value)
```

**描述**

获取Want中double类型的值。

**起始版本：** 17

**参数：**

参数项描述[AbilityBase_Want](../../topics/system-services/AbilityBase_Want.md)* wantWant指针。const char* keyWant中double类型值的参数索引。double* valueWant中double类型的值。

**返回：**

类型说明[AbilityBase_ErrorCode](ability_base_common.h.md#ZH-CN_TOPIC_0000002529444623__abilitybase_errorcode)

返回执行结果。

ABILITY_BASE_ERROR_CODE_NO_ERROR - 获取want中double类型的值成功。

ABILITY_BASE_ERROR_CODE_PARAM_INVALID - want为空或非法入参。