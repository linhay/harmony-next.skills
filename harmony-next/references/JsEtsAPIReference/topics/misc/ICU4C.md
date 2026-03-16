# ICU4C

当今的软件市场是一个全球性的市场，应用程序的开发和维护需要支持多种语言。International Components for Unicode (ICU) 库为多平台多系统提供了强大且功能齐全的多语言文化信息处理能力。

[ICU4C](https://unicode-org.github.io/icu/userguide/icu4c/)是ICU 库的C语言版本，部分接口已开放，支持如下能力：

- 区域与文化标识(uloc.h)
- 时间日期格式化(udat.h)
- 数字及度量衡格式化(unumberformatter.h，unum.h)
- 日历及本地历法(ucal.h)
- 排序(ucol.h)
- 断词换行(ubrk.h)
- 文本正规化(unorm2.h)
- 音译(utrans.h)
- 字符/文本属性(uchar.h，uscript.h)
- 编码转换(ucnv.h)
- 文本双向处理(ubidi.h)
- 域名转换(uidna.h)
- Unicode字符串处理(ustring.h)，从API version 15开始支持
- ICU文本抽象表示(utext.h)，从API version 15开始支持
- ICU版本(uversion.h)，从API version 22开始支持
- Locale ID及Locale各组成部分本地化名称(uldnames.h)，从API version 22开始支持
- Unicode码点处理(utf.h，utf8.h，utf16.h)，从API version 22开始支持
- CLDR版本(ulocdata.h)，从API version 22开始支持

#### 引入ICU4C国际化能力

如果开发者需要使用ICU4C相关功能，请按需要添加对应的头文件。本模块头文件需要添加unicode目录前缀，例如：

```ets
#include <unicode/uloc.h>
```

其次在CMakeList.txt中添加以下动态库:

```ets
libicu.so
```

#### 标准库中导出的符号列表

[native api中导出的ICU4C符号列表](../networking/Native api中导出的ICU4C符号列表.md)