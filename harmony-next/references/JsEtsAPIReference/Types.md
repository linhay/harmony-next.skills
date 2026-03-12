# Types

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

#### ISendable

type ISendable = lang.ISendable

ISendable是所有Sendable类型（除null和undefined）的父类型。自身没有任何必须的方法和属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

类型说明[lang.ISendable](@arkts.lang (ArkTS语言基础能力).md#ZH-CN_TOPIC_0000002497444768__langisendable)所有Sendable类型的父类型。

#### ArrayFromMapFn18+

type ArrayFromMapFn<FromElementType, ToElementType> = (value: FromElementType, index: number) => ToElementType

ArkTS Array归约函数类型，被Array类的'from' 接口使用。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明valueFromElementType是当前正在处理的元素。indexnumber是当前遍历的ArkTS Array元素下标。

**返回值：**

类型说明ToElementType归约函数的结果，该结果会作为数组的新元素。

#### ArrayPredicateFn18+

type ArrayPredicateFn<ElementType, ArrayType> = (value: ElementType, index: number, array: ArrayType) => boolean

ArkTS Array归约函数类型，被Array类的'some'和'every'接口使用，用来判断数组元素是否满足测试条件。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明valueElementType是当前正在处理的元素。indexnumber是当前遍历的ArkTS Array元素下标。arrayArrayType是当前遍历的ArkTS Array本身。

**返回值：**

类型说明boolean归约函数的结果，该结果作为判断当前元素是否通过测试条件。为true时表示当前或之前的某个元素已满足条件，为false时表示尚未找到符合条件的元素。

#### ArrayReduceCallback18+

type ArrayReduceCallback<AccType, ElementType, ArrayType> =

 (previousValue: AccType, currentValue: ElementType, currentIndex: number, array: ArrayType) => AccType

ArkTS Array归约函数类型，被Array类的'reduceRight'接口使用。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明previousValueAccType是当前遍历所累积的值。currentValueElementType是当前遍历的ArkTS Array元素。currentIndexnumber是当前遍历的ArkTS Array元素下标。arrayArrayType是当前遍历的ArkTS Array实例。

**返回值：**

类型说明AccType归约函数的结果，该结果会作为下一次调用ArrayReduceCallback时的previousValue参数。

#### TypedArrayFromMapFn

type TypedArrayFromMapFn<FromElementType, ToElementType> = (value: FromElementType, index: number) => ToElementType

ArkTS TypedArray映射函数类型。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明valueFromElementType是当前遍历的用于构造ArkTS TypedArray的元素。indexnumber是当前遍历的用于构造ArkTS TypedArray的元素下标，从0开始。

**返回值：**

类型说明ToElementType转换后的元素值。

#### TypedArrayPredicateFn

type TypedArrayPredicateFn<ElementType, ArrayType> = (value: ElementType, index: number, array: ArrayType) => boolean

ArkTS TypedArray断言测试函数类型。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明valueElementType是当前遍历的ArkTS TypedArray元素。indexnumber是当前遍历的ArkTS TypedArray元素下标，从0开始。arrayArrayType是当前遍历的ArkTS TypedArray实例。

**返回值：**

类型说明boolean如果值符合条件，则为true，否则为false。

#### TypedArrayForEachCallback

type TypedArrayForEachCallback<ElementType, ArrayType> = (value: ElementType, index: number, array: ArrayType) => void

ArkTS TypedArray遍历函数类型。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明valueElementType否当前遍历的ArkTS TypedArray元素。indexnumber否当前遍历的ArkTS TypedArray元素下标，从0开始。arrayArrayType否当前遍历的ArkTS TypedArray实例。

#### TypedArrayMapCallback

type TypedArrayMapCallback<ElementType, ArrayType> = (value: ElementType, index: number, array: ArrayType) => ElementType

ArkTS TypedArray转换映射函数类型。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明valueElementType是当前映射的ArkTS TypedArray元素。indexnumber是当前映射的ArkTS TypedArray元素下标，从0开始。arrayArrayType是当前映射的ArkTS TypedArray实例。

**返回值：**

类型说明ElementType转换后的元素值。

#### TypedArrayReduceCallback

type TypedArrayReduceCallback<AccType, ElementType, ArrayType> = (previousValue: AccType, currentValue: ElementType, currentIndex: number, array: ArrayType) => AccType

ArkTS TypedArray归约函数类型。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明previousValueAccType是当前遍历所累积的值。currentValueElementType是当前遍历的ArkTS TypedArray元素。currentIndexnumber是当前遍历的ArkTS TypedArray元素下标，从0开始。arrayArrayType是当前遍历的ArkTS TypedArray实例。

**返回值：**

类型说明AccType归约函数的结果。该结果会作为下一次调用TypedArrayReduceCallback时的previousValue参数。

#### TypedArrayCompareFn

type TypedArrayCompareFn<ElementType> = (first: ElementType, second: ElementType) => number

ArkTS TypedArray排序函数类型。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明firstElementType是当前待比较的第一个元素。secondElementType是当前待比较的第二个元素。

**返回值：**

类型说明number元素比较的结果。如果first小于second，返回值为负数；如果first大于second，返回值为正数；如果两个值相等，返回值为0。