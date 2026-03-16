[]()[]()

# 模块描述

本模块提供的ArkTS容器集，可以用于并发场景下的高性能数据传递。功能与JavaScript内建的对应容器类似，但ArkTS容器实例无法通过.或者[]添加或更新属性。

ArkTS容器在多个并发实例间传递时，其默认行为是引用传递，支持多个并发实例可以同时操作同一个容器实例。另外，也支持拷贝传递，即每个并发实例持有一个ArkTS容器实例。

ArkTS容器并不是线程安全的，内部使用了fail-fast（快速失败）机制：当检测多个并发实例同时对容器进行结构性改变时，会触发异常。因此，在多线程读写容器时，容器使用方需要使用ArkTS提供的异步锁机制保证ArkTS容器的安全访问。

当前ArkTS容器集主要包含以下几种容器：[Array](../types/classes/Class (Array).md)、[Map](../types/classes/Class (Map).md)、[Set](../types/classes/Class (Set).md)、TypedArray（[Int8Array](../types/classes/Class (Int8Array).md)、[Uint8Array](../types/classes/Class (Uint8Array).md)、[Int16Array](../types/classes/Class (Int16Array).md)、[Uint16Array](../types/classes/Class (Uint16Array).md)、[Int32Array](../types/classes/Class (Int32Array).md)、[Uint32Array](../types/classes/Class (Uint32Array).md)、[Uint8ClampedArray](../types/classes/Class (Uint8ClampedArray).md)、[Float32Array](../types/classes/Class (Float32Array).md)）、[ArrayBuffer](../types/classes/Class (ArrayBuffer).md)、[BitVector](../types/classes/Class (BitVector).md)、[ConcatArray](../types/interfaces/Interface (ConcatArray).md)。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

[]()[]()

#### 导入模块

```ets
import { collections } from '@kit.ArkTS';
```