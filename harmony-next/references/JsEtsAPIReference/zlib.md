# zlib

#### 简介

[Zlib](https://zlib.net/)是基于C/C++语言实现的一个通用的数据压缩库。

#### 支持的能力

Zlib库提供了内存中（in-memory）压缩、解压缩数据的能力，使用Deflate算法，可以设置不同的压缩级别，对各种类型的数据均有比较好的压缩效果；提供了对处理器和内存使用控制的能力，如果缓冲区足够大，压缩可以通过一个步骤完成，否则可以通过反复调用压缩接口完成。

默认情况下，Zlib接口使用的压缩数据格式是zlib格式（[RFC1950](https://www.rfc-editor.org/rfc/rfc1950)），Zlib库还支持使用以“gz”开头的函数接口读取和写入gzip（[RFC1952](https://www.rfc-editor.org/rfc/rfc1952)）格式的文件。zlib格式的设计目的是在内存和通信通道中使用，紧凑且快速。gzip格式是专为单个文件压缩而设计，其头部比zlib大，以维护目录信息，使用了与zlib不同且较慢的检查方法。

Zlib库解码器会检查压缩数据的一致性，因此即使在输入损坏的情况下，库也不应崩溃。

#### 引入zlib能力

如果开发者需要使用zlib相关功能，首先请添加头文件：

```ets
#include <zlib.h>
```

其次在CMakeLists.txt中添加以下动态链接库：

```ets
libz.so
```

#### 接口列表

详见[Zlib库支持的接口文档](https://www.zlib.net/manual.md)。