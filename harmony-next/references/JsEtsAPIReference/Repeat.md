# Repeat

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

Repeat基于数组类型数据来进行循环渲染，一般与滚动容器组件配合使用。

本文档仅为API参数说明。组件描述和使用说明见[Repeat开发者指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-rendering-control-repeat)。

#### 接口

#### Repeat: <T>(arr: Array<T>)

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明arrArray<T>是数据源，为Array<T>类型的数组，由开发者决定数据类型。

**示例：**

```ets
// arr是Array<string>类型的数组，以arr为数据源创建Repeat组件
Repeat<string>(this.arr)
```

#### Repeat: <T>(arr: RepeatArray<T>)18+

从API version 18开始，Repeat数据源支持RepeatArray类型。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明arr[RepeatArray<T>](#ZH-CN_TOPIC_0000002497604972__repeatarrayt18)是数据源，为RepeatArray<T>类型的数组，由开发者决定数据类型。

#### 属性

除支持[拖拽排序](拖拽排序.md)属性外，还支持以下属性。

#### each

each(itemGenerator: (repeatItem: RepeatItem<T>) => void)

组件生成函数。当所有.template()的type和.templateId()返回值不匹配（即当前item不适用任何template定义的样式）时，将使用.each()处理数据项。

-

each属性必须有，否则运行时会报错。

-

itemGenerator的参数为RepeatItem，该参数将item和index结合到了一起，请勿将RepeatItem参数拆开使用。

-

该接口不支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明repeatItem[RepeatItem](#ZH-CN_TOPIC_0000002497604972__repeatitemt)<T>否repeat数据项。

**示例：**

```ets
// arr是Array<string>类型的数组，为每个数据创建一个Text组件
Repeat<string>(this.arr)
  .each((obj: RepeatItem<string>) => { Text(obj.item) })
```

#### key

key(keyGenerator: (item: T, index: number) => string)

键值生成函数。

该接口不支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明itemT否arr数组中的数据项。indexnumber否arr数组中的数据项索引。

**示例：**

```ets
// arr是Array<string>类型的数组，为每个数据创建一个Text组件
// 并将字符串的值作为其键值
Repeat<string>(this.arr)
  .each((obj: RepeatItem<string>) => { Text(obj.item) })
  .key((obj: string) => obj)
```

#### virtualScroll

virtualScroll(virtualScrollOptions?: VirtualScrollOptions)

Repeat开启虚拟滚动。

该接口不支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明virtualScrollOptions[VirtualScrollOptions](#ZH-CN_TOPIC_0000002497604972__virtualscrolloptions)否虚拟滚动配置项。

**示例：**

```ets
// arr是Array<string>类型的数组，为每个数据创建一个Text组件
// 在List容器组件中使用Repeat，并打开virtualScroll
List() {
  Repeat<string>(this.arr)
    .each((obj: RepeatItem<string>) => { ListItem() { Text(obj.item) }})
    .virtualScroll()
}
```

#### template

template(type: string, itemBuilder: RepeatItemBuilder<T>, templateOptions?: TemplateOptions)

由template type渲染对应的template子组件。

该接口不支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是当前模板类型。itemBuilder[RepeatItemBuilder](#ZH-CN_TOPIC_0000002497604972__repeatitembuildert)<T>是组件生成函数。templateOptions[TemplateOptions](#ZH-CN_TOPIC_0000002497604972__templateoptions对象说明)否当前模板配置项。

**示例：**

```ets
// arr是Array<string>类型的数组
// 在List容器组件中使用Repeat，并打开virtualScroll
// 创建模板temp，该模板为数据创建Text组件
List() {
  Repeat<string>(this.arr)
    .each((obj: RepeatItem<string>) => {})
    .virtualScroll()
    .template('temp', (obj: RepeatItem<string>) => { ListItem() { Text(obj.item) }})
}
```

#### templateId

templateId(typedFunc: TemplateTypedFunc<T>)

为当前数据项分配template type。

该接口不支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typedFunc[TemplateTypedFunc](#ZH-CN_TOPIC_0000002497604972__templatetypedfunct)<T>是生成当前数据项对应的template type。

**示例：**

```ets
// arr是Array<string>类型的数组
// 在List容器组件中使用Repeat，并打开virtualScroll
// 创建模板temp，该模板为数据创建Text组件
// 所有数据项都使用temp模板
List() {
  Repeat<string>(this.arr)
    .each((obj: RepeatItem<string>) => {})
    .virtualScroll()
    .template('temp', (obj: RepeatItem<string>) => { ListItem() { Text(obj.item) }})
    .templateId((item: string, index: number) => { return 'temp' })
}
```

#### RepeatArray<T>18+

type RepeatArray<T> = Array<T> | ReadonlyArray<T> | Readonly<Array<T>>

Repeat数据源参数联合类型。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明Array<T>常规数组类型。ReadonlyArray<T>只读数组类型，不允许数组对象变更。Readonly<Array<T>>只读数组类型，不允许数组对象变更。

#### RepeatItem<T>

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明itemT否否arr中每一个数据项。T为开发者传入的数据类型。indexnumber否否当前数据项对应的索引。

#### VirtualScrollOptions

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明totalCountnumber否是

加载的数据项总数，可以不等于数据源长度。

取值范围：[0, +∞)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

reusable18+boolean否是

是否开启复用功能。true代表开启复用，false代表关闭复用。

默认值：true

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

onLazyLoading19+(index: number) => void否是

数据懒加载函数，向指定的数据源index中写入数据。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

onTotalCount19+() => number否是

数据项总数计算函数，返回值可以不等于数据源长度。推荐使用onTotalCount代替totalCount。同时设置totalCount与onTotalCount时，忽略totalCount。

取值范围：[0, +∞)

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

#### totalCount：期望加载的数据长度

totalCount表示期望加载的数据长度，默认为原数组长度，可以大于已加载数据项的数量。arr.length表示数据源长度，以下为totalCount的处理规则：

- totalCount缺省或是非自然数时，totalCount默认为arr.length，列表正常滚动。
- 0 <= totalCount < arr.length时，界面中只渲染区间[0, totalCount - 1]范围内的数据。
- totalCount > arr.length时，代表Repeat将渲染区间[0, totalCount - 1]范围内的数据，滚动条样式根据totalCount值变化。

当totalCount > arr.length时，在父组件容器滚动过程中，应用需要保证在列表即将滑动到数据源末尾时请求后续数据。开发者需要对数据请求的错误场景（如网络延迟）进行保护操作，直到数据源全部加载完成，否则列表滑动过程中会出现滚动效果异常。解决方案见[totalCount值大于数据源长度](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-rendering-control-repeat#totalcount值大于数据源长度)。

#### onLazyLoading19+：数据精准懒加载

onLazyLoading从API version 19开始支持，需在懒加载场景下使用。开发者可设置自定义方法，用于向指定的数据源index中写入数据。以下为onLazyLoading的处理规则：

- 在Repeat读取数据源中某一index处对应数据前，会先检查此index处是否存在数据。
- 当不存在数据，但开发者提供了onLazyLoading方法，Repeat将调用此方法。
- 在onLazyLoading方法中，开发者需要向Repeat指定的index中写入数据，方式如下：arr[index] = ...。需要注意的是，不允许使用除[]以外的数组操作，且不允许写入指定index以外的元素，否则系统将抛出异常。
- onLazyLoading方法执行完成后，若指定index中仍无数据，将导致渲染异常。

- 当使用onLazyLoading时，建议与onTotalCount配合使用，不建议使用totalCount。
- 若期望数据源长度大于实际数据源长度，推荐使用onLazyLoading。
- onLazyLoading方法中应避免高耗时操作。若数据加载耗时较长，建议先在onLazyLoading方法中为此数据创建占位符，再创建异步任务加载数据。
- 当使用onLazyLoading，并设置onTotalCount为arr.length + 1时，可实现数据的无限加载。需要注意，在此场景下，开发者需要提供首屏显示所需的初始数据，并建议设置父容器组件cachedCount > 0，否则将会导致渲染异常。若与Swiper-Loop模式同时使用，停留在index = 0处时将导致onLazyLoading方法被持续触发，建议避免与Swiper-Loop模式同时使用。此外，开发者需要关注内存消耗情况，避免因数据持续加载而导致内存过量消耗。

#### onTotalCount19+：计算期望的数据长度

onTotalCount从API version 19开始支持，需在懒加载场景下使用。开发者可设置自定义方法，用于计算期望的数组长度。其返回值应当为自然数，可以不等于实际数据源长度arr.length。以下为onTotalCount的处理规则：

- 当onTotalCount返回值为非自然数时，使用arr.length代替返回值，列表正常滚动。
- 当0 <= onTotalCount返回值 < arr.length时，界面中只渲染区间[0, onTotalCount返回值 - 1]范围内的数据。
- 当onTotalCount返回值 > arr.length时，代表Repeat将渲染区间[0, onTotalCount返回值 - 1]范围内的数据，滚动条样式根据onTotalCount返回值变化。

- 相较于totalCount，Repeat可在需要时主动调用onTotalCount方法，更新期望数据长度。
- totalCount与onTotalCount最多设置一个。如果均未设置，则采用默认值arr.length；如果同时设置，则忽略totalCount。
- 当onTotalCount返回值 > arr.length时，建议配合使用onLazyLoading实现数据懒加载。

#### 示例

```ets
// arr是Array<string>类型的数组，在List容器组件中使用Repeat，并打开virtualScroll
// 将加载的数据项总数设为数据源的长度，并开启复用功能
List() {
  Repeat<string>(this.arr)
    .each((obj: RepeatItem<string>) => { ListItem() { Text(obj.item) }})
    .virtualScroll( { totalCount: this.arr.length, reusable: true } )
}

// 假设数据项总数为100，首屏渲染需3项数据
// 初始数组提供前3项数据（arr = ['No.0', 'No.1', 'No.2']），并开启数据懒加载功能
List() {
  Repeat<string>(this.arr)
    .each((obj: RepeatItem<string>) => { ListItem() { Text(obj.item) }})
    .virtualScroll({
      onTotalCount: () => { return 100; },
      onLazyLoading: (index: number) => { this.arr[index] = `No.${index}`; }
    })
}
```

#### RepeatItemBuilder<T>

type RepeatItemBuilder<T> = (repeatItem: RepeatItem<T>) => void

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明repeatItem[RepeatItem](#ZH-CN_TOPIC_0000002497604972__repeatitemt)<T>否将item和index结合到一起的一个状态变量。

#### TemplateOptions对象说明

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明cachedCountnumber否是当前template的缓存池中可缓存子组件节点的最大数量。取值范围是[0, +∞)，默认值为容器组件显示区域节点与预加载区域节点的个数之和。当容器组件显示区域节点与预加载节点的个数之和增多时（滑动过程中，只有部分高度的子组件在显示区域），cachedCount也会对应增长。需要注意cachedCount数量不会减少。

当cachedCount值被设置为当前template在容器组件显示区域的最大节点数量时，Repeat会做到最大程度的复用。当容器组件显示区域内没有当前template的节点时，缓存列表不会释放，同时应用内存增大。开发者需要根据具体情况自行把控，推荐cachedCount值设置为容器组件显示区域内节点个数。需要注意，不建议设置cachedCount小于2，这会导致在快速滑动场景下频繁创建新的节点，从而造成性能劣化。

滚动容器组件属性.cachedCount()和Repeat组件属性.template()的参数cachedCount都是为了平衡性能和内存，但是含义是不同的。

- 滚动容器组件.cachedCount()：是指在容器组件显示区域外预加载区域的大小，该区域内子组件节点位于组件树上。滚动容器组件会额外渲染这些预加载区域的节点，从而提高列表滑动性能。
- .template()中的cachedCount: 指Repeat每个template的缓存池大小，当渲染新的子组件时，Repeat先判断对应template缓存池中是否有可用节点，有则复用，没有则创建新节点。

**示例：**

```ets
// arr是Array<string>类型的数组，在List容器组件中使用Repeat，并打开virtualScroll
// 创建模板temp，该模板为数据创建Text组件，所有数据项都使用temp模板
// 将temp模板的最大缓存节点数量设为2
List() {
  Repeat<string>(this.arr)
    .each((obj: RepeatItem<string>) => {})
    .virtualScroll()
    .template('temp', (obj: RepeatItem<string>) => { ListItem() { Text(obj.item) }}, { cachedCount: 2 })
    .templateId((item: string, index: number) => { return 'temp' })
}
```

#### TemplateTypedFunc<T>

type TemplateTypedFunc<T> = (item: T, index: number) => string

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明itemT否arr中每一个数据项。T为开发者传入的数据类型。indexnumber否当前数据项对应的索引。