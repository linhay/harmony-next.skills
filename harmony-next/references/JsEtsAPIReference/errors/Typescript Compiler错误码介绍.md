# Typescript Compiler错误码介绍

TSC(Typescript Compiler)的错误码以'105'开头，是TSC编译流程中的报错提示，会在编辑器、控制台或日志文件中显示输出错误码和相对应的报错描述。

#### 10505001 TSC原生报错

TSC原生报错：以'001'结尾，是Typescript Compiler检查中已有的原生报错规则。在TSC的编译流程中，常见的TSC原生报错原因包括：关键字或符号的缺失、赋值类型与接收类型不一致、类型或变量未定义等。这些问题通常是未按照[语言规范](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/introduction-to-arkts)编写代码导致的，开发者可以根据报错描述修改代码。

#### 关键字或符号的缺失

**错误示例场景：**

```ets
declare type AAA = 'BBB;
```

**错误信息**

Unterminated string literal.

**错误描述**

字符串字面量未正确终止。

**可能原因**

字符串字面量没有在预期的位置正确终止，可能是缺少了结束引号。

**处理步骤**

根据报错描述，补全代码块的引号，修改后代码如下：

```ets
declare type AAA = 'BBB';
```

#### 多个默认导出

**错误示例场景：**

```ets
export default A;
export default B;
```

**错误信息**

A module cannot have multiple default exports.

**错误描述**

一个模块不能有多个默认导出。

**可能原因**

一个模块中定义了多个默认导出。

**处理步骤**

根据报错描述，删除多余的默认导出，修改后代码如下：

```ets
export default A;
```

#### 赋值类型与接收类型不一致

**错误示例场景：**

```ets
let a: number = 1;
let b: string = '2';
a = b;
```

**错误信息**

Type 'string' is not assignable to type 'number'.

**错误描述**

类型 'string' 不能赋值给类型 'number'。

**可能原因**

将一个变量的值赋给另一个不同类型的变量时，会发生类型不匹配错误。

**处理步骤**

根据报错描述，确保类型一致性，进行相应的类型赋值修改，修改后代码如下：

```ets
let a: number = 1;
let b: number = 2;
a = b;
```

#### js文件中接口导出异常

**错误示例场景：**

har1包中有js文件，存在导出接口：

```ets
// har1's src/main/ets/FileJs.js
export let fileJs = 1;
```

har2包引用har1包中该接口：

```ets
import { fileJs } from 'har1/src/main/ets/FileJs';
```

**错误信息**

Cannot find module XXX or its corresponding type declarations.

**错误描述**

当字节码har中有js文件时，编译无法生成声明文件，导致其余模块无法导入。

**可能原因**

js文件在编译时tsc不会生成对应的声明文件，导致其余模块无法导入。

**处理步骤**

若har包中的js文件需要提供对外导出功能，开发者需要：

1.在js文件同级目录中手动编写对应的.d.ts声明文件，并随har包一起编译发布，示例如下：

```ets
// har1's src/main/ets/FileJs.d.ts
export declare let fileJs: number;
```

2.在har1包顶层的Index.ets文件中增加export导出语句，示例如下：

```ets
export { fileJs } from './src/main/ets/FileJs';
```

3.在har2包引用har1包中该接口，示例如下：

```ets
import { fileJs } from 'har1/src/main/ets/FileJs';
```