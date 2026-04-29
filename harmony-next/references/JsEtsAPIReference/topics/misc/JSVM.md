# JSVM

#### 概述

提供标准的JavaScript引擎能力。功能概述：标准JS引擎是严格遵守ECMAScript规范的JavaScript代码执行引擎。支持[ECMAScript规范](https://ecma262.com/)定义的标准库，提供完备的[C++交互JS的native API](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/jsvm-introduction)。通过JIT编译加速代码执行，为应用提供安全、高效的JS执行能力。标准JS引擎的能力通过一套稳定的ABI，即JSVM-API提供。JSVM-API支持动态链接到不同版本的JS引擎库，从而为开发者屏蔽掉不同引擎接口的差异。JSVM-API提供引擎生命周期管理、JS context管理、JS代码执行、JS/C++互操作、执行环境快照、codecache等能力。

使用平台：arm64平台。

使用方法：链接SDK中的libjsvm.so，并在C++代码中包含ark_runtime/[jsvm.h](jsvm.h.md)头文件。

**起始版本：** 11

#### 文件汇总

| 名称 | 描述 |
| --- | --- |
| [jsvm.h](jsvm.h.md) | 提供JSVM-API接口定义。通过API接口为开发者提供独立、标准、完整的JavaScript引擎能力，包括管理引擎生命周期、编译运行JS代码、实现JS/C++跨语言调用、拍摄快照等。 |
| [jsvm_types.h](jsvm_types.h.md) | 提供JSVM-API类型定义。通过API接口为开发者提供独立、标准、完整的JavaScript引擎能力，包括管理引擎生命周期、编译运行JS代码、实现JS/C++跨语言调用、拍摄快照等。 |
