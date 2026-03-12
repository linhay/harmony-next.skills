# @ohos.arkui.StateManagement (状态管理)

状态管理模块提供了应用程序的数据存储能力、持久化数据管理能力、UIAbility数据存储能力和应用程序需要的环境状态、工具。

本模块首批接口从API version 12开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

本文中T和S的含义如下：

类型说明TClass，number，boolean，string和这些类型的数组形式。Snumber，boolean，string。

#### 导入模块

```ets
import { AppStorageV2, PersistenceV2, UIUtils } from '@kit.ArkUI';
```

#### AppStorageV2

AppStorageV2具体UI使用说明，详见[AppStorageV2(应用全局的UI状态存储)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-appstoragev2)。

#### connect

static connect<T extends object>(

type: TypeConstructorWithArgs<T>,

keyOrDefaultCreator?: string | StorageDefaultCreator<T>,

defaultCreator?: StorageDefaultCreator<T>

): T | undefined

将键值对数据储存在应用内存中。如果给定的key已经存在于[AppStorageV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-appstoragev2)中，返回对应的值；否则，通过获取默认值的构造器构造默认值，并返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明type[TypeConstructorWithArgs<T>](#ZH-CN_TOPIC_0000002529444753__typeconstructorwithargst)是指定的类型，若未指定key，则使用type的name作为key。keyOrDefaultCreatorstring | [StorageDefaultCreator<T>](#ZH-CN_TOPIC_0000002529444753__storagedefaultcreatort)否指定的key，或者是获取默认值的构造器。defaultCreatorStorageDefaultCreator<T>否获取默认值的构造器。

1、若未指定key，使用第二个参数作为默认构造器；否则使用第三个参数作为默认构造器（第二个参数非法也使用第三个参数作为默认构造器）。

2、确保数据已经存储在AppStorageV2中，可省略默认构造器，获取存储的数据；否则必须指定默认构造器，不指定将导致应用异常。

3、同一个key，connect不同类型的数据会导致应用异常，应用需要确保类型匹配。

4、key建议使用有意义的值，长度不超过255，使用非法字符或空字符的行为是未定义的。

**返回值：**

类型说明T | undefined创建或获取AppStorageV2数据成功时，返回数据；否则返回undefined。

**示例：**

```ets
import { AppStorageV2 } from '@kit.ArkUI';

@ObservedV2
class SampleClass {
  @Trace p: number = 0;
}

// 将key为SampleClass、value为new SampleClass()对象的键值对存储到内存中，并赋值给as1
const as1: SampleClass | undefined = AppStorageV2.connect(SampleClass, () => new SampleClass());

// 将key为key_as2、value为new SampleClass()对象的键值对存储到内存中，并赋值给as2
const as2: SampleClass = AppStorageV2.connect(SampleClass, 'key_as2', () => new SampleClass())!;

// key为SampleClass已经在AppStorageV2中，将key为SampleClass的值返回给as3
const as3: SampleClass = AppStorageV2.connect(SampleClass) as SampleClass;
```

#### remove

static remove<T>(keyOrType: string | TypeConstructorWithArgs<T>): void

将指定的键值对数据从[AppStorageV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-appstoragev2)里面删除。如果指定的键值不存在于AppStorageV2中，将删除失败。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明keyOrTypestring | TypeConstructorWithArgs<T>是需要删除的key；如果指定的是type类型，删除的key为type的name。

删除AppStorageV2中不存在的key会报警告。

**示例：**

```ets
// 假设AppStorageV2中存在key为key_as2的键，从AppStorageV2中删除该键值对数据
AppStorageV2.remove('key_as2');

// 假设AppStorageV2中存在key为SampleClass的键，从AppStorageV2中删除该键值对数据
AppStorageV2.remove(SampleClass);

// 假设AppStorageV2中不存在key为key_as1的键，报警告
AppStorageV2.remove('key_as1');
```

#### keys

static keys(): Array<string>

获取[AppStorageV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-appstoragev2)中的所有key。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明Array<string>所有AppStorageV2中的key。

key在Array中的顺序是无序的，与key插入到AppStorageV2中的顺序无关。

**示例：**

```ets
// 假设AppStorageV2中存在两个key（key_as1、key_as2），返回[key_as1、key_as2]赋值给keys
const keys: Array<string> = AppStorageV2.keys();
```

#### PersistenceV2

继承自[AppStorageV2](#ZH-CN_TOPIC_0000002529444753__appstoragev2)，PersistenceV2具体UI使用说明，详见[PersistenceV2(持久化存储UI状态)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-persistencev2)。

#### globalConnect18+

static globalConnect<T extends object>(type: ConnectOptions<T>): T | undefined

将键值对数据储存在应用磁盘中。如果给定的key已经存在于[PersistenceV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-persistencev2)中，返回对应的值；否则，会通过获取默认值的构造器构造默认值，并返回。如果globalConnect的是@ObservedV2对象，该对象@Trace属性的变化，会触发整个关联对象的自动刷新；非@Trace属性变化则不会，如有必要，可调用PersistenceV2.save接口手动存储。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明type[ConnectOptions<T>](#ZH-CN_TOPIC_0000002529444753__connectoptions18)是传入的connect参数，详细说明见ConnectOptions参数说明。

**返回值：**

类型说明T | undefined创建或获取数据成功时，返回数据；否则返回undefined。

1、若未指定key，使用第二个参数作为默认构造器；否则使用第三个参数作为默认构造器（第二个参数非法也使用第三个参数作为默认构造器）。

2、确保数据已经存储在PersistenceV2中，可省略默认构造器，获取存储的数据；否则必须指定默认构造器，不指定将导致应用异常。

3、同一个key，globalConnect不同类型的数据会导致应用异常，应用需要确保类型匹配。

4、key建议使用有意义的值，可由字母、数字、下划线组成，长度不超过255，使用非法字符或空字符的行为是未定义的。

5、关联[@Observed](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)对象时，因为该类型的name属性未定义，需要指定key或者自定义name属性。

6、数据的存储路径为应用级别，不同module使用相同的key和相同的加密分区进行globalConnect，存储的数据副本应用仅有一份。

7、globalConnect使用同一个key但设置了不同的加密级别，数据为第一个使用globalConnect的加密级别，并且PersistenceV2中的数据也会存入最先使用key的加密级别。

8、connect和globalConnect不建议混用，因为数据副本路径不同，如果混用，则key不可以一样，否则会crash。

9、EL5加密要想生效，需要开发者在module.json中配置字段ohos.permission.PROTECT_SCREEN_LOCK_DATA，使用说明见[声明权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions)。

**示例：**

仅供开发者了解globalConnect用法，完整使用需开发者自己写出@Entry组件。

```ets
import { PersistenceV2, Type, ConnectOptions } from '@kit.ArkUI';
import { contextConstant } from '@kit.AbilityKit';

@ObservedV2
class SampleChild {
  @Trace childId: number = 0;
  groupId: number = 1;
}

@ObservedV2
export class Sample {
  // 对于复杂对象需要@Type修饰，确保序列化成功
  @Type(SampleChild)
  @Trace father: SampleChild = new SampleChild();
}

// key不传入尝试用为type的name作为key，加密参数不传入默认加密等级为EL2
const p: Sample = PersistenceV2.globalConnect({ type: Sample, defaultCreator: () => new Sample() })!;

// 使用key:global1连接，传入加密等级为EL1
const p1: Sample = PersistenceV2.globalConnect({
  type: Sample,
  key: 'global1',
  defaultCreator: () => new Sample(),
  areaMode: contextConstant.AreaMode.EL1
})!;

// 使用key:global2连接，使用构造函数形式，加密参数不传入默认加密等级为EL2
const p2: Sample = PersistenceV2.globalConnect({ type: Sample, key: 'global2', defaultCreator: () => new Sample() })!;

// 使用key:global3连接，直接写加密数值，范围只能在0-4，否则运行会crash,例如加密设置为EL3
const p3: Sample = PersistenceV2.globalConnect({
  type: Sample,
  key: 'global3',
  defaultCreator: () => new Sample(),
  areaMode: 3
})!;
```

#### save

static save<T>(keyOrType: string | TypeConstructorWithArgs<T>): void

将指定的键值对数据持久化一次。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明keyOrTypestring | TypeConstructorWithArgs<T>是需要持久化的key；如果指定的是type类型，持久化的key为type的name。

由于非[@Trace](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace)的数据改变不会触发[PersistenceV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-persistencev2)的自动持久化，如有必要，可调用该接口持久化对应key的数据。

手动持久化当前内存中不处于connect状态的key是无意义的。

**示例：**

```ets
@ObservedV2
class SampleClass {
  @Trace p: number = 0;
}

// 假设PersistenceV2中存在key为key_as2的键，持久化该键值对数据
PersistenceV2.save('key_as2');

// 假设PersistenceV2中存在key为SampleClass的键，持久化该键值对数据
PersistenceV2.save(SampleClass);

// 假设PersistenceV2中不存在key为key_as1的键，无意义的操作
PersistenceV2.save('key_as1');
```

#### notifyOnError

static notifyOnError(callback: PersistenceErrorCallback | undefined): void

在持久化失败时调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明callbackPersistenceErrorCallback | undefined是持久化失败时调用。

**示例：**

```ets
// 持久化失败时调用
PersistenceV2.notifyOnError((key: string, reason: string, msg: string) => {
  console.error(`error key: ${key}, reason: ${reason}, message: ${msg}`);
});
```

#### ConnectOptions18+

globalConnect参数类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明typeTypeConstructorWithArgs<T>否否指定的类型。keystring否是传入的key，不传则使用type的名字作为key。defaultCreatorStorageDefaultCreator<T>否是默认数据的构造器，建议传递，如果globalConnect是第一次连接key，不传会报错。areaModecontextConstant.AreaMode否是加密级别：EL1-EL5，详见[加密级别](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-context-stage#获取和修改加密分区)，对应数值：0-4，不传时默认为EL2，不同加密级别对应不同的加密分区，即不同的存储路径，传入的加密等级数值不在0-4会直接运行crash。

#### UIUtils

UIUtils提供一些方法，用于处理状态管理相关的数据转换。

#### getTarget

static getTarget<T extends object>(source: T): T

从状态管理框架包裹的代理对象中获取原始对象。详见[getTarget接口：获取状态管理框架代理前的原始对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-gettarget)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明sourceT是数据源对象。

**返回值：**

类型说明T数据源对象去除状态管理框架所加代理后的原始对象。

**示例：**

```ets
import { UIUtils } from '@kit.ArkUI';

class NonObservedClass {
  name: string = 'Tom';
}

let nonObservedClass: NonObservedClass = new NonObservedClass();

@Entry
@Component
struct Index {
  @State someClass: NonObservedClass = nonObservedClass;

  build() {
    Column() {
      Text(`this.someClass === nonObservedClass: ${this.someClass === nonObservedClass}`) // false
      Text(`UIUtils.getTarget(this.someClass) === nonObservedClass: ${UIUtils.getTarget(this.someClass) ===
        nonObservedClass}`) // true
    }
  }
}
```

#### makeObserved

static makeObserved<T extends object>(source: T): T

将普通不可观察数据变为可观察数据。详见[makeObserved接口：将非观察数据变为可观察数据](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-makeobserved)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明sourceT是

数据源对象。支持非@Observed和@ObservedV2装饰的class，JSON.parse返回的Object和@Sendable修饰的class。

支持Array、Map、Set和Date。

支持collection.Array, collection.Set和collection.Map。

具体使用规则，详见[makeObserved接口：将非观察数据变为可观察数据](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-makeobserved)。

**返回值：**

类型说明T可观察的数据。

**示例：**

```ets
import { UIUtils } from '@kit.ArkUI';

class NonObservedClass {
  name: string = 'Tom';
}

@Entry
@ComponentV2
struct Index {
  observedClass: NonObservedClass = UIUtils.makeObserved(new NonObservedClass());
  nonObservedClass: NonObservedClass = new NonObservedClass();

  build() {
    Column() {
      Text(`observedClass: ${this.observedClass.name}`)
        .onClick(() => {
          this.observedClass.name = 'Jane'; // 刷新
        })
      Text(`observedClass: ${this.nonObservedClass.name}`)
        .onClick(() => {
          this.nonObservedClass.name = 'Jane'; // 不刷新
        })
    }
  }
}
```

#### enableV2Compatibility19+

static enableV2Compatibility<T extends object>(source: T): T

使V1的状态变量能够在@ComponentV2中观察，主要应用于状态管理V1、V2混用场景。详见[状态管理V1V2混用文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-mixusage)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明sourceT是数据源，仅支持V1状态数据。

**返回值：**

类型说明T如果数据源是V1的状态数据，则返回能够在@ComponentV2中观察的数据。否则返回数据源本身。

**示例：**

```ets
import { UIUtils } from '@kit.ArkUI';

@Observed
class ObservedClass {
  name: string = 'Tom';
}

@Entry
@Component
struct CompV1 {
  @State observedClass: ObservedClass = new ObservedClass();

  build() {
    Column() {
      Text(`@State observedClass: ${this.observedClass.name}`)
        .onClick(() => {
          this.observedClass.name = 'State'; // 刷新
        })
      // 将V1的状态变量使能V2的观察能力
      CompV2({ observedClass: UIUtils.enableV2Compatibility(this.observedClass) })
    }
  }
}

@ComponentV2
struct CompV2 {
  @Param observedClass: ObservedClass = new ObservedClass();

  build() {
    // V1状态变量在使能V2观察能力后，可以在V2观察第一层的变化
    Text(`@Param observedClass: ${this.observedClass.name}`)
      .onClick(() => {
        this.observedClass.name = 'Param'; // 刷新
      })
  }
}
```

#### makeV1Observed19+

static makeV1Observed<T extends object>(source: T): T

将不可观察的对象包装成状态管理V1可观察的对象，其能力等同于@Observed，可初始化@ObjectLink。

该接口可搭配[enableV2Compatibility](#ZH-CN_TOPIC_0000002529444753__enablev2compatibility19)应用于状态管理V1和V2混用场景，详见[状态管理V1V2混用文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-mixusage)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明sourceT是

数据源。支持普通class、Array、Map、Set、Date类型。

不支持[collections类型](模块描述.md)和[@Sendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable)修饰的class。

不支持undefined和null。不支持状态管理V2的数据和[makeObserved](#ZH-CN_TOPIC_0000002529444753__makeobserved)的返回值。

**返回值：**

类型说明T对于支持的入参类型，返回状态管理V1的观察数据。对于不支持的入参类型，返回数据源对象本身。

**示例：**

```ets
import { UIUtils } from '@kit.ArkUI';

class Outer {
  outerValue: string = 'outer';
  inner: Inner;

  constructor(inner: Inner) {
    this.inner = inner;
  }
}

class Inner {
  interValue: string = 'inner';
}

@Entry
@Component
struct Index {
  @State outer: Outer = new Outer(UIUtils.makeV1Observed(new Inner()));

  build() {
    Column() {
      // makeV1Observed的返回值可初始化@ObjectLink
      Child({ inner: this.outer.inner })
    }
    .height('100%')
    .width('100%')
  }
}

@Component
struct Child {
  @ObjectLink inner: Inner;

  build() {
    Text(`${this.inner.interValue}`)
      .onClick(() => {
        this.inner.interValue += '!';
      })
  }
}
```

#### makeBinding20+

static makeBinding<T>(getter: GetterCallback<T>): Binding<T>

创建只读的单向数据绑定实例，用于构建@Builder函数中参数类型为Binding的对应实参。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明getter[GetterCallback<T>](#ZH-CN_TOPIC_0000002529444753__gettercallback20)是获取值的回调函数，每次访问值都会重新执行函数，获取最新值。

**返回值：**

类型说明[Binding<T>](#ZH-CN_TOPIC_0000002529444753__bindingt20)仅包含一个value属性，用于获取当前绑定的值。只能读取值，不能直接修改。

**示例：**

```ets
import { Binding, MutableBinding, UIUtils } from '@kit.ArkUI';

@Builder
function CustomButton(num1: Binding<number>) {
  Row() {
    Button(`Custom Button: ${num1.value}`)
      .onClick(() => {
        // num1.value += 1; 会报错，Binding类型不支持修改
      })
  }
}

@Entry
@ComponentV2
struct CompV2 {
  @Local number1: number = 5;
  @Local number2: number = 10;

  build() {
    Column() {
      Text('parent component')

      CustomButton(
        /**
         * 创建只读绑定实例
         * @param getter - 返回this.number1的函数
         * @returns 只读的Binding<number>对象
         *
         * 特点：
         * 1. 每次访问.value时重新计算
         * 2. 不能直接修改值
         */
        UIUtils.makeBinding<number>(
          () => this.number1 // GetterCallback
        )
      )
    }
  }
}
```

#### makeBinding20+

static makeBinding<T>(getter: GetterCallback<T>, setter: SetterCallback<T>): MutableBinding<T>

创建可修改的双向数据绑定实例，用于构建@Builder函数中参数类型为MutableBinding的对应实参。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明getter[GetterCallback<T>](#ZH-CN_TOPIC_0000002529444753__gettercallback20)是获取值的回调函数，每次访问值都会重新执行函数，获取最新值。setter[SetterCallback<T>](#ZH-CN_TOPIC_0000002529444753__settercallback20)是定义如何更新值，当.value被修改时自动调用此函数。

**返回值：**

类型说明[MutableBinding<T>](#ZH-CN_TOPIC_0000002529444753__mutablebindingt20)包含一个value属性，支持通过.value读取和修改数据，设置值时会检查类型是否匹配泛型T。

**示例：**

```ets
import { Binding, MutableBinding, UIUtils } from '@kit.ArkUI';

@Builder
function CustomButton(num2: MutableBinding<number>) {
  Row() {
    Button(`Custom Button: ${num2.value}`)
      .onClick(() => {
        // MutableBinding类型支持修改
        num2.value += 1;
      })
  }
}

@Entry
@ComponentV2
struct CompV2 {
  @Local number1: number = 5;
  @Local number2: number = 10;

  build() {
    Column() {
      Text('parent component')

      CustomButton(
        /**
         * 创建可变绑定
         * @param getter - 返回this.number2的函数
         * @param setter - 当绑定值修改时调用的回调
         * @returns 可变的MutableBinding<number>对象
         *
         * 特点：
         * 1. 支持读取和写入操作
         * 2. 修改.value时会自动调用setter回调
         */
        UIUtils.makeBinding<number>(
          () => this.number2, // GetterCallback
          (val: number) => {
            this.number2 = val;
          }) // SetterCallback
      )
    }
  }
}
```

#### addMonitor20+

static addMonitor(target: object, path: string | string[], monitorCallback: MonitorCallback, options?: MonitorOptions): void

给状态管理V2的状态变量动态添加监听方法，详见[addMonitor/clearMonitor](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-addmonitor-clearmonitor)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明targetobject是

目标对象，仅支持[@ComponentV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#componentv2)和[@ObservedV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace)实例。

对于不支持的类型，会抛出运行时错误，错误码见表格。

pathstring | string[]是

添加监听的变量名路径。可指定一个路径或者传入string数组用于一次性指定多个监听的变量路径。

仅支持string和string数组，对于不支持的类型，会抛出运行时错误，错误码见表格。

monitorCallback[MonitorCallback](#ZH-CN_TOPIC_0000002529444753__monitorcallback20)是

给对应的状态变量注册的监听函数，即path路径对应的状态变量改变时，会回调对应的函数。

对于不支持的类型，会抛出运行时错误，错误码见表格。

options[MonitorOptions](#ZH-CN_TOPIC_0000002529444753__monitoroptions20)否监听函数的配置项，具体可见[MonitorOptions](#ZH-CN_TOPIC_0000002529444753__monitoroptions20)。

**错误码：**

以下错误码的详细介绍请参见[状态管理错误码](状态管理错误码.md)。

错误码ID错误信息130000The target is not a custom component instance or V2 class instance.130001The path is invalid.130002monitorCallback is not a function or an anonymous function.

**示例：**

下面的示例：

1. 在ObservedClass的构造方法里，添加对name属性的同步监听回调onChange。
1. 点击Text组件，将name改为Jack和Jane，触发两次onChange回调，打印日志如下。

```ets
ObservedClass property name change from Tom to Jack
ObservedClass property name change from Jack to Jane
```

```ets
import { UIUtils } from '@kit.ArkUI';

@ObservedV2
class ObservedClass {
  @Trace name: string = 'Tom';

  onChange(mon: IMonitor) {
    mon.dirty.forEach((path: string) => {
      console.info(`ObservedClass property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
    });
  }

  constructor() {
    // 给当前ObservedClass的实例this添加对属性name的监听回调this.onChange，且当前监听回调是同步监听
    UIUtils.addMonitor(this, 'name', this.onChange, { isSynchronous: true });
  }
}

@Entry
@ComponentV2
struct Index {
  @Local observedClass: ObservedClass = new ObservedClass();

  build() {
    Column() {
      Text(`name: ${this.observedClass.name}`)
        .fontSize(20)
        .onClick(() => {
          this.observedClass.name = 'Jack';
          this.observedClass.name = 'Jane';
        })
    }
  }
}
```

#### clearMonitor20+

static clearMonitor(target: object, path: string | string[], monitorCallback?: MonitorCallback): void

删除通过[addMonitor](#ZH-CN_TOPIC_0000002529444753__addmonitor20)给状态管理V2的状态变量添加的监听方法，详见[addMonitor/clearMonitor](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-addmonitor-clearmonitor)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明targetobject是

目标对象，仅支持[@ComponentV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#componentv2)和[@ObservedV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace)实例。

对于不支持的类型，会抛出运行时错误，错误码见表格。

pathstring | string[]是

删除监听的变量名路径。可指定一个路径或者传入string数组用于一次性指定删除多个状态变量的监听函数。

仅支持string和数组，对于不支持的类型，会抛出运行时错误，错误码见表格。

monitorCallback[MonitorCallback](#ZH-CN_TOPIC_0000002529444753__monitorcallback20)否

指定被删除的监听函数。

当开发者不传此参数时，将删除path对应变量注册的所有监听函数。

对于不支持的类型，会抛出运行时错误，错误码见表格。

**错误码：**

以下错误码的详细介绍请参见[状态管理错误码](状态管理错误码.md)。

错误码ID错误信息130000The target is not a custom component instance or V2 class instance.130001The path is invalid.130002monitorCallback is not a function or an anonymous function.

**示例：**

在下面的示例中：

1. 在ObservedClass的构造方法中，添加对age属性的同步监听回调onChange。
1. 点击Text组件，触发age自增，onChange的监听回调函数被触发。打印日志如下。

```ets
ObservedClass property age change from 10 to 11
```

1. 点击clear monitor，删除age的监听函数onChange。
1. 再次点击Text组件，触发age自增，onChange不会被触发。

```ets
import { UIUtils } from '@kit.ArkUI';

@ObservedV2
class ObservedClass {
  @Trace age: number = 10;

  onChange(mon: IMonitor) {
    mon.dirty.forEach((path: string) => {
      console.info(`ObservedClass property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
    });
  }

  constructor() {
    // 给当前ObservedClass的实例this添加对属性name的监听回调this.onChange，且当前监听回调是同步监听
    UIUtils.addMonitor(this, 'age', this.onChange);
  }
}

@Entry
@ComponentV2
struct Index {
  @Local observedClass: ObservedClass = new ObservedClass();

  build() {
    Column() {
      Text(`age: ${this.observedClass.age}`)
        .fontSize(20)
        .onClick(() => {
          // 点击触发age++，触发onChange回调
          this.observedClass.age++;
        })
      Button('clear monitor')
        .onClick(() => {
          // 点击clearMonitor，删除this.observedClass中age的监听函数onChange
          // 再次点击触发age++，没有触发监听函数onChange
          UIUtils.clearMonitor(this.observedClass, 'age', this.observedClass.onChange);
        })
    }
  }
}
```

#### applySync22+

static applySync<T>(task: TaskCallback): T

同步刷新指定的状态变量，该接口接收一个闭包函数，仅刷新闭包函数内的修改，包括更新[@Computed计算](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-computed)、[@Monitor回调](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-monitor)以及重新渲染UI节点，详见[applySync/flushUpdates/flushUIUpdates接口：同步刷新](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-applysync-flushupdates-flushuiupdates)。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明task[TaskCallback](#ZH-CN_TOPIC_0000002529444753__taskcallback22)是闭包函数，该闭包中产生的状态变量修改会同步执行。

**返回值：**

类型说明T闭包函数执行得到的返回值。

**错误码：**

以下错误码的详细介绍请参见[状态管理错误码](状态管理错误码.md)。

错误码ID错误信息140001The function is not allowed to be called in @Computed.

**示例：**

```ets
import { UIUtils } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local w: number = 50; // 宽度
  @Local h: number = 50; // 高度
  @Local message: string = 'Hello';

  build() {
    Column() {
      Button('change size')
        .margin(20)
        .onClick(() => {
          // 在执行动画前，存在额外的修改
          UIUtils.applySync(() => {
            this.w = 100;
            this.h = 100;
            this.message = 'Hello World';
          });
          // 动画在1s内，Column方框的尺寸由（100*100）渐变为（200*200），方框内的文本变为Hello ArkUI
          this.getUIContext().animateTo({
            duration: 1000
          }, () => {
            console.info(`animateTo-in, w=${this.w}, h=${this.h}`);
            this.w = 200;
            this.h = 200;
            this.message = 'Hello ArkUI';
            console.info(`animateTo-out, w=${this.w}, h=${this.h}`);
          });
        })
      // Column方框
      Column() {
        Text(`${this.message}`)
      }
      .backgroundColor('#ff17a98d')
      .width(this.w)
      .height(this.h)
    }
  }
}
```

#### flushUpdates22+

static flushUpdates(): void

同步刷新在调用该函数之前所有的状态变量修改，包括更新@Computed计算、@Monitor回调以及重新渲染UI节点，详见[applySync/flushUpdates/flushUIUpdates接口：同步刷新](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-applysync-flushupdates-flushuiupdates)。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**错误码：**

以下错误码的详细介绍请参见[状态管理错误码](状态管理错误码.md)。

错误码ID错误信息140001The function is not allowed to be called in @Computed.140002The function is not allowed to be called in @Monitor.

**示例：**

```ets
import { UIUtils } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local w: number = 50; // 宽度
  @Local h: number = 50; // 高度
  @Local message: string = 'Hello';

  build() {
    Column() {
      Button('change size')
        .margin(20)
        .onClick(() => {
          // 在执行动画前，存在额外的修改
          this.w = 100;
          this.h = 100;
          this.message = 'Hello World';
          UIUtils.flushUpdates();
          // 动画在1s内，Column方框的尺寸由（100*100）渐变为（200*200），方框内的文本变为Hello ArkUI
          this.getUIContext().animateTo({
            duration: 1000
          }, () => {
            console.info(`animateTo-in, w=${this.w}, h=${this.h}`);
            this.w = 200;
            this.h = 200;
            this.message = 'Hello ArkUI';
            console.info(`animateTo-out, w=${this.w}, h=${this.h}`);
          });
        })
      // Column方框
      Column() {
        Text(`${this.message}`)
      }
      .backgroundColor('#ff17a98d')
      .width(this.w)
      .height(this.h)
    }
  }
}
```

#### flushUIUpdates22+

static flushUIUpdates(): void

立即处理在调用该函数之前所有的状态变量修改，同步[标脏](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-introduce#触发更新)对应的UI节点，但不会同步执行@Computed计算和@Monitor回调，详见[applySync/flushUpdates/flushUIUpdates接口：同步刷新](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-applysync-flushupdates-flushuiupdates)。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**错误码：**

以下错误码的详细介绍请参见[状态管理错误码](状态管理错误码.md)。

错误码ID错误信息140001The function is not allowed to be called in @Computed.140002The function is not allowed to be called in @Monitor.

**示例：**

```ets
import { UIUtils } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local w: number = 50; // 宽度
  @Local h: number = 50; // 高度
  @Local message: string = 'Hello';

  build() {
    Column() {
      Button('change size')
        .margin(20)
        .onClick(() => {
          // 在执行动画前，存在额外的修改
          this.w = 100;
          this.h = 100;
          this.message = 'Hello World';
          UIUtils.flushUIUpdates();
          // 动画在1s内，Column方框的尺寸由（100*100）渐变为（200*200），方框内的文本变为Hello ArkUI
          this.getUIContext().animateTo({
            duration: 1000
          }, () => {
            console.info(`animateTo-in, w=${this.w}, h=${this.h}`);
            this.w = 200;
            this.h = 200;
            this.message = 'Hello ArkUI';
            console.info(`animateTo-out, w=${this.w}, h=${this.h}`);
          });
        })
      // Column方框
      Column() {
        Text(`${this.message}`)
      }
      .backgroundColor('#ff17a98d')
      .width(this.w)
      .height(this.h)
    }
  }
}
```

#### TaskCallback22+

type TaskCallback = () => T

同步执行的回调方法。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明T闭包函数执行得到的返回值。

#### MonitorOptions20+

[addMonitor](#ZH-CN_TOPIC_0000002529444753__addmonitor20)的可选参数，用于配置回调类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明isSynchronousboolean否是配置当前回调函数否是为同步回调。true为同步回调。默认值为false，即异步回调。

#### MonitorCallback20+

type MonitorCallback = (monitorValue: IMonitor) => void

参数为[IMonitor](状态变量变化监听.md#ZH-CN_TOPIC_0000002497604970__imonitor12)类型的监听回调函数。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明monitorValueIMonitor是回调函数传入的变化信息。

#### StorageDefaultCreator<T>

type StorageDefaultCreator<T> = () => T

返回默认构造器的函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明T默认构造器执行得到的返回值。

**示例：**

```ets
import { PersistenceV2 } from '@kit.ArkUI';

@ObservedV2
class SampleClass {
  @Trace id: number = 0;
  count: number = 1;
}

@ObservedV2
class FatherSampleClass {
  @Trace sampleClass: SampleClass = new SampleClass();
}

// 将key为SampleClass、value为new SampleClass()对象的键值对持久化，并赋值给source
// StorageDefaultCreator 指的是 () => new FatherSampleClass()
const source: FatherSampleClass | undefined = PersistenceV2.connect(FatherSampleClass, () => new FatherSampleClass());

@Entry
@Component
struct SampleComp {
  data: FatherSampleClass | undefined = source;

  build() {
    Column() {
      Text(`${this.data?.sampleClass.id}`)
    }
  }
}
```

#### TypeConstructorWithArgs<T>

含有任意入参的类构造器。

#### new

new(...args: any): T

创建并返回一个指定类型T的实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明...argsany否函数入参。

**返回值：**

类型说明TT类型的实例。

**示例：**

```ets
import { PersistenceV2 } from '@kit.ArkUI';

@ObservedV2
  // TypeConstructorWithArgs 指的是 SampleClass
class SampleClass {
  @Trace id: number = 0;
  count: number = 1;
}

@ObservedV2
class FatherSampleClass {
  @Trace sampleClass: SampleClass = new SampleClass();
}

// 将key为SampleClass、value为new SampleClass()对象的键值对持久化，并赋值给source
const source: FatherSampleClass | undefined = PersistenceV2.connect(FatherSampleClass, () => new FatherSampleClass());

@Entry
@Component
struct SampleComp {
  data: FatherSampleClass | undefined = source;

  build() {
    Column() {
      Text(`${this.data?.sampleClass.id}`)
    }
  }
}
```

#### PersistenceErrorCallback

type PersistenceErrorCallback = (key: string, reason: 'quota' | 'serialization' | 'unknown', message: string) => void

持久化失败时返回错误原因的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明keystring是出错的键值。reason'quota' | 'serialization' | 'unknown'是出错的原因类型。messagestring是出错的更多消息。

**示例：**

```ets
import { PersistenceV2, Type } from '@kit.ArkUI';

@ObservedV2
class SampleChild {
  @Trace id: number = 0;
  count: number = 10;
}

@ObservedV2
export class Sample {
  // 对于复杂对象需要@Type修饰，确保序列化成功
  @Type(SampleChild)
  @Trace sampleChild: SampleChild = new SampleChild();
}

// 接受序列化失败的回调
// PersistenceErrorCallback 指的是 (key: string, reason: string, msg: string) => {console.error(`error key: ${key}, reason: ${reason}, message: ${msg}`);}
PersistenceV2.notifyOnError((key: string, reason: string, msg: string) => {
  console.error(`error key: ${key}, reason: ${reason}, message: ${msg}`);
});

@Entry
@ComponentV2
struct Index {
  // 在PersistenceV2中创建一个key为Sample的键值对（如果存在，则返回PersistenceV2中的数据），并且和data关联
  // 对于需要换connect对象的data属性，需要加@Local修饰（不建议对属性换connect的对象）
  @Local data: Sample = PersistenceV2.connect(Sample, () => new Sample())!;
  pageStack: NavPathStack = new NavPathStack();

  build() {
    Text(`Index add 1 to data.id: ${this.data.sampleChild.id}`)
      .fontSize(30)
      .onClick(() => {
        this.data.sampleChild.id++;
      })
  }
}
```

#### TypeConstructor<T>

类构造函数。

#### new

new(): T

创建并返回一个指定类型T的实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明TT类型的实例。

**示例：**

```ets
import { PersistenceV2, Type } from '@kit.ArkUI';

@ObservedV2
class SampleChild {
  @Trace id: number = 0;
  count: number = 10;
}

@ObservedV2
export class Sample {
  // 对于复杂对象需要@Type修饰，确保序列化成功
  // TypeConstructor 指的是 SampleChild
  @Type(SampleChild)
  @Trace sampleChild: SampleChild = new SampleChild();
}

@Entry
@ComponentV2
struct Index {
  data: Sample = PersistenceV2.connect(Sample, () => new Sample())!;

  build() {
    Column() {
      Text(`Index add 1 to data.id: ${this.data.sampleChild.id}`)
        .fontSize(30)
        .onClick(() => {
          this.data.sampleChild.id++;
        })
    }
  }
}
```

#### TypeDecorator

type TypeDecorator = <T>(type: TypeConstructor<T>) => PropertyDecorator

属性装饰器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明type[TypeConstructor<T>](#ZH-CN_TOPIC_0000002529444753__typeconstructort)是标记类属性的类型。

**返回值：**

类型说明PropertyDecorator属性装饰器。

**示例：**

```ets
import { PersistenceV2, Type } from '@kit.ArkUI';

@ObservedV2
class SampleChild {
  @Trace id: number = 0;
  count: number = 10;
}

@ObservedV2
export class Sample {
  // 对于复杂对象需要@Type修饰，确保序列化成功
  // TypeDecorator 指的是 @Type
  @Type(SampleChild)
  @Trace sampleChild: SampleChild = new SampleChild();
}

@Entry
@ComponentV2
struct Index {
  data: Sample = PersistenceV2.connect(Sample, () => new Sample())!;

  build() {
    Column() {
      Text(`Index add 1 to data.id: ${this.data.sampleChild.id}`)
        .fontSize(30)
        .onClick(() => {
          this.data.sampleChild.id++;
        })
    }
  }
}
```

#### GetterCallback20+

type GetterCallback<T> = () => T

获取值的回调方法。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明TT类型的值。

**示例：**

```ets
import { Binding, MutableBinding, UIUtils } from '@kit.ArkUI';

@Builder
function CustomButton(num1: Binding<number>) {
  Row() {
    Button(`Custom Button: ${num1.value}`)
      .onClick(() => {
        // num1.value += 1; 会报错，Binding类型不支持修改
      })
  }
}

@Entry
@ComponentV2
struct CompV2 {
  @Local number1: number = 5;
  @Local number2: number = 10;

  build() {
    Column() {
      Text('parent component')

      CustomButton(
        // 对于UIUtils.makeBinding函数的第一个参数需要传入GetterCallback
        UIUtils.makeBinding<number>(
          () => this.number1 // GetterCallback
        )
      )
    }
  }
}
```

#### SetterCallback20+

type SetterCallback<T> = (newValue: T) => void

设置值的回调方法。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明newValueT是类型为T的参数。

**示例：**

```ets
import { Binding, MutableBinding, UIUtils } from '@kit.ArkUI';

@Builder
function CustomButton(num2: MutableBinding<number>) {
  Row() {
    Button(`Custom Button: ${num2.value}`)
      .onClick(() => {
        // MutableBinding支持可变，可以修改num2.value
        num2.value += 1;
      })
  }
}

@Entry
@ComponentV2
struct CompV2 {
  @Local number1: number = 5;
  @Local number2: number = 10;

  build() {
    Column() {
      Text('parent component')

      CustomButton(
        // 对于UIUtils.makeBinding函数的第二个参数需要传入SetterCallback
        UIUtils.makeBinding<number>(
          () => this.number2, // GetterCallback
          (val: number) => {
            this.number2 = val;
          }) // SetterCallback 必须提供，否则触发时会造成运行时错误
      )
    }
  }
}
```

#### Binding<T>20+

只读数据绑定的泛型类，可以绑定任意类型的数据。

#### value20+

get value(): T

提供get访问器，用于获取绑定的值。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明T返回值类型为泛型参数T，与Binding<T>定义的类型一致。

**示例：**

```ets
import { Binding, MutableBinding, UIUtils } from '@kit.ArkUI';

@Builder
function CustomButton(num1: Binding<number>) {
  // CustomButton的第一个参数为Binding，一个只读数据绑定的泛型类
  Row() {
    // num1.value Binding类可以使用绑定的值
    Button(`Custom Button: ${num1.value}`)
      .onClick(() => {
        // num1.value += 1; 会报错，只读数据绑定的泛型类不能修改值
      })
  }
}

@Entry
@ComponentV2
struct CompV2 {
  @Local number1: number = 5;
  @Local number2: number = 10;

  build() {
    Column() {
      Text('parent component')

      CustomButton(
        UIUtils.makeBinding<number>(
          () => this.number1 // GetterCallback
        )
      )
    }
  }
}
```

#### MutableBinding<T>20+

可变数据绑定的泛型类，允许对绑定值进行读写操作，提供完整的get和set访问器。

#### value20+

set value(newValue: T)

提供set访问器，用于设置当前绑定值的值。构造MutableBinding类实例时必须提供set访问器，否则触发set访问器会造成运行时错误。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明newValueT是参数类型为泛型参数T，与MutableBinding<T>定义的类型一致。

#### value20+

get value(): T

提供get访问器，用于获取当前绑定值。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明T返回值类型为泛型参数T，与Binding<T>定义的类型一致。

**示例：**

```ets
import { Binding, MutableBinding, UIUtils } from '@kit.ArkUI';

@Builder
function CustomButton(num2: MutableBinding<number>) {
  // CustomButton的第二个参数为MutableBinding，一个可变数据绑定的泛型类
  Row() {
    Button(`Custom Button: ${num2.value}`)
      .onClick(() => {
        // 可变数据绑定的泛型类可以修改绑定的值
        num2.value += 1;
      })
  }
}

@Entry
@ComponentV2
struct CompV2 {
  @Local number1: number = 5;
  @Local number2: number = 10;

  build() {
    Column() {
      Text('parent component')

      CustomButton(
        UIUtils.makeBinding<number>(
          () => this.number2, // GetterCallback
          (val: number) => {
            this.number2 = val;
          }) // SetterCallback 必须提供，否则触发时会造成运行时错误
      )
    }
  }
}
```