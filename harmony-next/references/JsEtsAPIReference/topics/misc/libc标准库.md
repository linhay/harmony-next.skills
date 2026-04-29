# libc标准库

#### 简介

C标准函数库在C语言程序设计中，提供符合标准的头文件，以及常用的库函数实现（如I/O输入输出和字符串控制）。

HarmonyOS采用musl作为C标准库，musl库是一个轻量，快速，简单，免费的开源libc库，详细介绍参考[musl官方参考手册](http://musl.libc.org/manual.html)。

musl与glibc的差异点请参考[musl与glibc功能对比](https://wiki.musl-libc.org/functional-differences-from-glibc.html)。

#### 标准C库组件介绍

[libc、libm、libdl](https://zh.cppreference.com/w/c/header)组合实现C11标准C库。

libc：包含线程相关接口，以及大部分标准接口。

libm：数学库函数接口，当前在HarmonyOS中是一个链接，实际都在libc中定义。

libdl：dlopen等动态链接器接口，当前在HarmonyOS中是一个链接，实际都在libc中定义。

#### musl版本号

1.2.0

从HarmonyOS4.0开始，版本升级到1.2.3

从HarmonyOS5.0开始，版本升级到1.2.5

#### 支持的能力

提供兼容C99、C11、POSIX标准的头文件，以及库函数接口，但不是完全兼容；支持armv7a、arm64、x86_64三种架构的支持；

为了更好的适配HarmonyOS设备的高性能、低内存、高安全、轻量化、支持多种形态设备的基本特征；在musl开源库的基础上进行了优化，增强，对不适用嵌入式设备的接口进行了裁剪。

#### 新增能力

1. 动态加载器支持命名空间隔离能力，应用可以dlopen加载的动态库受系统命名空间限制（比如，无法打开系统侧动态库）。
1. 支持dlclose真实卸载动态库能力，musl的开源版本不支持。
1. 支持symbol-versioning功能。
1. dlopen支持直接加载zip包中未压缩的文件。

#### 调试能力

libc提供了动态使能维测log功能（默认关闭），供开发者需要的时候查看libc库异常。使用libc提供的动态使能维测log功能，不需要重新编译libc库，只需设置param属性即可。在正式发布版本中，不建议使能，会影响运行性能。

**1. musl.log功能**

设置musl.log.enable属性为true，打开musl维测log打印。打印其他日志，需先打开此开关。

```ets
param set musl.log.enable true
```

**2. 加载器log功能**

加载器是libc中负责程序引导，dlopen，dlclose等动态链接程序，如需要查看动态加载过程异常，可以打开加载器log。用法如下：

- 使能全部应用的加载器log，log量比较大，请谨慎使用。

```ets
param set musl.log.ld.app true
```

- 使能指定应用的加载器log，{app_name}需要替换成真实需要打印log的应用名字。

```ets
param set musl.log.ld.all false
param set musl.log.ld.app.{app_name} true
```

- 打印全部应用除指定名字应用外的加载器日志。

```ets
param set musl.log.ld.all true
param set musl.log.ld.app.{app_name} false
```

#### musl 差异规格接口说明

| 接口名称 | 说明 |
| --- | --- |
| epoll_create | 在HarmonyOS5.0 上 该接口逻辑与1.2.3版本保持一致，不会对入参进行判断，不区分入参小于等于0的情况，预计下版本更新此接口逻辑与社区1.2.5保持一致，增加入参逻辑判断，入参小于等于0时创建失败，并返回错误码EINVAL。 |

#### ICONV支持的字符集编码格式

musl支持的字符集编码格式，以及受支持的别名。

在进行字符集编码格式转换时，请使用正确的源字符集编码格式，且目标字符集编码格式必须支持这些受转换的字符，否则转换失败。

在musl里不支持将源字符集编码格式转换成这五种目标字符集编码格式：gb18030，gbk，gb2312，big5和euckr。

| 编码格式 | 别名 | musl支持情况 |
| --- | --- | --- |
| utf8 |  | 支持 |
| wchart |  | 支持 |
| ucs2be |  | 支持 |
| ucs2le |  | 支持 |
| utf16be |  | 支持 |
| utf16le |  | 支持 |
| ucs4be | utf32be | 支持 |
| ucs4le | utf32le | 支持 |
| ascii | usascii, iso646, iso646us | 支持 |
| utf16 |  | 支持 |
| ucs4 | utf32 | 支持 |
| ucs2 |  | 支持 |
| eucjp |  | 支持 |
| shiftjis | sjis, cp932 | 支持 |
| iso2022jp |  | 支持 |
| gb18030 |  | 支持 |
| gbk |  | 支持 |
| gb2312 |  | 支持 |
| big5 | bigfive, cp950, big5hkscs | 支持 |
| euckr | ksc5601, ksx1001, cp949 | 支持 |
| iso88591 | latin1 | 支持 |
| iso88592 |  | 支持 |
| iso88593 |  | 支持 |
| iso88594 |  | 支持 |
| iso88595 |  | 支持 |
| iso88596 |  | 支持 |
| iso88597 |  | 支持 |
| iso88598 |  | 支持 |
| iso88599 |  | 支持 |
| iso885910 |  | 支持 |
| iso885911 | tis620 | 支持 |
| iso885913 |  | 支持 |
| iso885914 |  | 支持 |
| iso885915 | latin9 | 支持 |
| iso885916 |  | 支持 |
| cp1250 | windows1250 | 支持 |
| cp1251 | windows1251 | 支持 |
| cp1252 | windows1252 | 支持 |
| cp1253 | windows1253 | 支持 |
| cp1254 | windows1254 | 支持 |
| cp1255 | windows1255 | 支持 |
| cp1256 | windows1256 | 支持 |
| cp1257 | windows1257 | 支持 |
| cp1258 | windows1258 | 支持 |
| koi8r |  | 支持 |
| koi8u |  | 支持 |
| cp437 |  | 支持 |
| cp850 |  | 支持 |
| cp866 |  | 支持 |
| cp1047 | ibm1047 | 支持 |

#### musl不支持接口列表。

[native api中没有导出的符号列表](Native api中没有导出的符号列表.md)

[NDK musl-libc接口受权限影响的说明](NDK涉及的musl libc接口使用限制的说明.md)

[NDK musl-libc补充api文档](https://gitcode.com/openharmony/third_party_musl/tree/master/docs)