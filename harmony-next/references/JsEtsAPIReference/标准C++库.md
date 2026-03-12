# 标准C++库

HarmonyOS使用llvm开源项目的C++标准库[libc++](https://libcxx.llvm.org/)作为C++运行时库。

#### libc++版本

从HarmonyOS 4.0开始到HarmonyOS 6.0，libc++升级到clang/llvm 15.0.4版本

从HarmonyOS 3.2开始，libc++升级到clang/llvm 12.0.1版本

从HarmonyOS 3.0开始，libc++使用clang/llvm 10.0.1版本

#### C++语言支持能力

C++11、C++14标准已完全支持，C++17和C++20标准的部分特性已支持。开发者可以通过[如何修改代码工程所支持的C++语言版本](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-9)来设置自己开发所需C++标准版本。如果将C++版本设置为C++17或者C++20，但使用了不支持的特性，会导致编译失败。具体语言特性支持标准可以参考[https://libcxx.llvm.org/](https://libcxx.llvm.org/)网站对应的Release Notes。

#### 如何在CMake中选择C++

在NDK的{ndk_root}/build/cmake/ohos.toolchain.cmake文件中，定义了OHOS_STL变量，可以通过设置"c++_shared"或者"c++_static"来控制应用工程中原生库链接C++运行库的方式。

- c++_shared，原生库动态链接libc++_shared.so
- c++_static，原生库静态链接libc++_static.a

#### C++运行时兼容性

在HarmonyOS系统中，系统库与应用原生库都在使用C++标准库，两部分升级节奏不一样，依赖C++运行时版本也可能不一样。系统库依赖的C++标准库随镜像版本升级，而应用原生库依赖的C++标准库随编译使用的SDK版本升级，两部分依赖的C++基础库会跨多个大版本，产生ABI兼容性问题。为了解决此问题，HarmonyOS上把两部分依赖的C++标准库进行了区分。

```ets
* 系统库：使用libc++.so， 随系统镜像发布。
* 应用Native库：使用libc++_shared.so，随应用发布。
```

 两个库使用的C++命名空间不一样，libc++_shared.so使用__n1作为C++符号的命名空间，libc++.so使用__h作为C++符号的命名空间。

 注意：两边使用的C++标准库不能进行混用，Native API接口当前只能是C接口，可以通过这个接口隔离两边的C++运行环境。

#### 注意事项

1.

C++运行时库工具链进行大版本升级的时候，不保证一定二进制兼容；一个应用包如果有多个动态库，这些动态库**必须用同一个大版本的clang工具链进行编译**，依赖相同版本的libc++_shared库，否则有可能产生不可预知的错误。

1.

在一个应用工程里面，如果只有一个共享库，建议使用静态链接c++_static，这样能够让链接器精简使用的C++运行时代码，降低包大小。如果有多个库，或者依赖带动态库的har包，或者ohpm上带库的二进制中间件，建议采用动态链接C++库；采用静态链接会导致程序中定义多个函数或对象的副本，会破坏C++的单一定义规则（One Definition Rule），出现不可预知问题。