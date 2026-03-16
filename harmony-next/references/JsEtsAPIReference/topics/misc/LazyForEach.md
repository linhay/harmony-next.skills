# LazyForEach

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

开发者指南见：[LazyForEach开发者指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)。

在大量子组件的场景下，LazyForEach与缓存列表项、动态预加载、组件复用等方法配合使用，可以进一步提升滑动帧率并降低应用内存占用。最佳实践请参考[优化长列表加载慢丢帧问题](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-best-practices-long-list)。

#### 接口

LazyForEach(dataSource: IDataSource, itemGenerator: (item: any, index: number) => void, keyGenerator?: (item: any, index: number) => string)

LazyForEach从提供的数据源中按需迭代数据，并在每次迭代过程中创建相应的组件。当在滚动容器中使用了LazyForEach，框架会根据滚动容器可视区域按需创建组件，当组件滑出可视区域外时，框架会进行组件销毁回收以降低内存占用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明dataSource[IDataSource](#ZH-CN_TOPIC_0000002529444937__idatasource)是LazyForEach数据源，需要开发者实现相关接口。itemGenerator(item: any, index: number) => void是

子组件生成函数，为数组中的每一个数据项创建一个子组件。

**说明：**

- item是当前数据项（可选），index是数据项索引值（可选）。

- itemGenerator的函数体必须使用大括号{...}。

- itemGenerator每次迭代只能并且必须生成一个子组件。

- itemGenerator中可以使用if语句，但是必须保证if语句每个分支都会创建一个相同类型的子组件。

keyGenerator(item: any, index: number) => string否

键值生成函数，用于给数据源中的每一个数据项生成唯一且固定的键值。修改数据源中的一个数据项若不影响其生成的键值，则对应组件不会被更新，否则此处组件就会被重建更新。keyGenerator参数是可选的，但是，为了使开发框架能够更好地识别数组更改并正确更新组件，建议提供。

**说明：**

- item是当前数据项（可选），index是数据项索引值（可选）。

- keyGenerator缺省时，使用默认的键值生成函数，即(item: Object, index: number) => { return viewId + '-' + index.toString(); }，生成键值仅受索引值index影响（viewId在编译器转换过程中生成，同一个LazyForEach组件内的viewId一致）。

- 为保证LazyForEach正确、高效地更新子组件，避免渲染结果异常、渲染效率降低等问题，键值应满足以下条件。

1. 键值具有唯一性，每个数据项对应的键值互不相同。

2. 键值具有一致性，数据项不变时对应的键值也不变。

应避免在keyGenerator和itemGenerator函数中执行耗时操作，以此来减少应用滑动时卡顿丢帧问题，最佳实践请参考[主线程耗时操作优化-循环渲染](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-time-optimization-of-the-main-thread#section4551193714439)。例如，不推荐使用JSON.stringify函数。在复杂的业务场景中，使用JSON.stringify会对item对象进行序列化，该过程会消耗大量时间与计算资源，从而降低页面性能，最佳实践请参考[懒加载优化性能-键值生成规则](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-lazyforeach-optimization#section68711519072)。

#### 属性

支持[拖拽排序](拖拽排序.md)属性。

#### IDataSource

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### totalCount

totalCount(): number

获得数据总数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明number获得数据总数，由数据源决定实际大小。

#### getData

getData(index: number): any

获取索引值index对应的数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexnumber是获取数据对应的索引值。取值范围是[0, 数据源长度-1]。

**返回值：**

类型说明any获取索引值index对应的数据，由数据源决定具体类型。

应避免在getData函数中执行耗时操作，以此来减少应用滑动时卡顿丢帧问题，最佳实践请参考[主线程耗时操作优化-循环渲染](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-time-optimization-of-the-main-thread#section4551193714439)。

#### registerDataChangeListener

registerDataChangeListener(listener: DataChangeListener): void

注册数据改变的监听器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明listener[DataChangeListener](#ZH-CN_TOPIC_0000002529444937__datachangelistener)是数据变化监听器。

#### unregisterDataChangeListener

unregisterDataChangeListener(listener: DataChangeListener): void

注销数据改变的监听器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明listener[DataChangeListener](#ZH-CN_TOPIC_0000002529444937__datachangelistener)是数据变化监听器。

#### DataChangeListener

数据变化监听器。

DataChangeListener除onDatasetChange以外的方法中，当参数包含index且值为负数时，会默认用0来替换。onDatasetChange中，当单个DataOperation参数包含index且值在数据源索引范围之外（DataAddOperation中index可以等于数据源长度），则对应DataOperation不会生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### onDataReloaded

onDataReloaded(): void

通知组件重新加载所有数据。键值没有变化的数据项会使用原先的子组件，键值发生变化的会重建子组件。重新加载数据完成后调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### onDataAdded(deprecated)

onDataAdded(index: number): void

通知组件index的位置有数据添加。添加数据完成后调用。

从API version 8开始，建议使用[onDataAdd](#ZH-CN_TOPIC_0000002529444937__ondataadd8)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexnumber是数据添加位置的索引值。取值范围是[0, 数据源长度-1]。

#### onDataMoved(deprecated)

onDataMoved(from: number, to: number): void

通知组件数据有移动。将from和to位置的数据进行交换。

从API version 8开始，建议使用[onDataMove](#ZH-CN_TOPIC_0000002529444937__ondatamove8)。

数据移动前后键值要保持不变，如果键值有变化，应使用删除数据和新增数据接口。数据移动起始位置与数据移动目标位置交换完成后调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明fromnumber是数据移动起始位置。取值范围是[0, 数据源长度-1]。tonumber是数据移动目标位置。取值范围是[0, 数据源长度-1]。

#### onDataDeleted(deprecated)

onDataDeleted(index: number): void

通知组件删除index位置的数据并刷新LazyForEach的展示内容。删除数据完成后调用。

从API version 8开始，建议使用[onDataDelete](#ZH-CN_TOPIC_0000002529444937__ondatadelete8)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexnumber是数据删除位置的索引值。取值范围是[0, 数据源长度-1]。

#### onDataChanged(deprecated)

onDataChanged(index: number): void

通知组件index的位置有数据变化。改变数据完成后调用。

从API version 8开始，建议使用[onDataChange](#ZH-CN_TOPIC_0000002529444937__ondatachange8)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexnumber是数据变化监听器。取值范围是[0, 数据源长度-1]。

#### onDataAdd8+

onDataAdd(index: number): void

通知组件index的位置有数据添加。添加数据完成后调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexnumber是数据添加位置的索引值。取值范围是[0, 数据源长度-1]。

#### onDataMove8+

onDataMove(from: number, to: number): void

通知组件数据有移动。将from和to位置的数据进行交换。数据移动起始位置与数据移动目标位置交换完成后调用。

数据移动前后键值要保持不变，如果键值有变化，应使用删除数据和新增数据接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明fromnumber是数据移动起始位置。取值范围是[0, 数据源长度-1]。tonumber是数据移动目标位置。取值范围是[0, 数据源长度-1]。

#### onDataDelete8+

onDataDelete(index: number): void

通知组件删除index位置的数据并刷新LazyForEach的展示内容。删除数据完成后调用。

需要保证dataSource中的对应数据已经在调用onDataDelete前删除，否则页面渲染将出现未定义的行为。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexnumber是数据删除位置的索引值。取值范围是[0, 数据源长度-1]。

#### onDataChange8+

onDataChange(index: number): void

通知组件index的位置有数据有变化。改变数据完成后调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexnumber是数据变化位置的索引值。取值范围是[0, 数据源长度-1]。

#### onDatasetChange12+

onDatasetChange(dataOperations: DataOperation[]): void

进行批量的数据处理后，调用onDatasetChange接口通知组件按照dataOperations刷新组件。

onDatasetChange接口不能与其他DataChangeListener的更新接口混用。例如，在同一个LazyForEach中，调用过onDataAdd接口后，不能再调用onDatasetChange接口；反之，调用过onDatasetChange接口后，也不能调用onDataAdd等其他更新接口。页面中不同LazyForEach之间互不影响。在同一个onDatasetChange批量处理数据时，如果多个DataOperation操作同一个index，只有第一个DataOperation生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明dataOperations[DataOperation](#ZH-CN_TOPIC_0000002529444937__dataoperation12)[]是一次处理数据的操作。

#### DataOperation12+

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### DataAddOperation

添加数据操作。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明type[DataOperationType](#ZH-CN_TOPIC_0000002529444937__dataoperationtype枚举说明).ADD否否数据添加类型。indexnumber否否插入数据索引值。取值范围是[0, 数据源长度-1]。countnumber否是插入数量，默认为1。keystring | Array<string>否是为插入的数据分配键值，默认使用原键值。

#### DataDeleteOperation

删除数据操作。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明type[DataOperationType](#ZH-CN_TOPIC_0000002529444937__dataoperationtype枚举说明).DELETE否否数据删除类型。indexnumber否否起始删除位置索引值。取值范围是[0, 数据源长度-1]。countnumber否是删除数据数量，默认为1。

#### DataChangeOperation

改变数据操作。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明type[DataOperationType](#ZH-CN_TOPIC_0000002529444937__dataoperationtype枚举说明).CHANGE否否数据改变类型。indexnumber否否改变的数据的索引值。取值范围是[0, 数据源长度-1]。keystring否是为改变的数据分配新的键值，默认使用原键值。

#### DataMoveOperation

移动数据操作。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明type[DataOperationType](#ZH-CN_TOPIC_0000002529444937__dataoperationtype枚举说明).MOVE否否数据移动类型。index[MoveIndex](#ZH-CN_TOPIC_0000002529444937__moveindex12)否否移动位置。取值范围是[0, 数据源长度-1]。keystring否是为被移动的数据分配新的键值，默认使用原键值。

#### DataExchangeOperation

交换数据操作。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明type[DataOperationType](#ZH-CN_TOPIC_0000002529444937__dataoperationtype枚举说明).EXCHANGE否否数据交换类型。index[ExchangeIndex](#ZH-CN_TOPIC_0000002529444937__exchangeindex12)否否交换位置。取值范围是[0, 数据源长度-1]。key[ExchangeKey](#ZH-CN_TOPIC_0000002529444937__exchangekey12)否是分配新的键值，默认使用原键值。

#### DataReloadOperation

重载所有数据操作。当onDatasetChange含有DataOperationType.RELOAD操作时，其余操作全部失效，框架会自己调用keyGenerator进行键值比对。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明type[DataOperationType](#ZH-CN_TOPIC_0000002529444937__dataoperationtype枚举说明).RELOAD否否数据全部重载类型。

#### DataOperationType枚举说明

枚举类型，数据操作说明。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明ADDadd数据添加。DELETEdelete数据删除。CHANGEchange数据改变。MOVEmove数据移动。EXCHANGEexchange数据交换。RELOADreload全部数据重载。

#### MoveIndex12+

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明fromnumber否否起始移动位置。取值范围是[0, 数据源长度-1]。tonumber否否目的移动位置。取值范围是[0, 数据源长度-1]。

#### ExchangeIndex12+

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明startnumber否否第一个交换位置。取值范围是[0, 数据源长度-1]。endnumber否否第二个交换位置。取值范围是[0, 数据源长度-1]。

#### ExchangeKey12+

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明startstring否否为第一个交换的位置分配新的键值，默认使用原键值。endstring否否为第二个交换的位置分配新的键值，默认使用原键值。