# zlib子系统错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](通用错误码.md)。

#### 900001 传入的源文件错误

**错误信息**

The input source file is invalid.

**错误描述**

当调用compressFile或decompressFile接口时，传入源文件无效。

**可能原因**

当调用compressFile接口时，传入的待压缩的文件不存在；当调用decompressFile接口时，传入的待解压缩的文件不存在。

**处理步骤**

1. 检查源文件是否存在。
1. 检查源文件的后缀是否为.zip。
1. 检查待压缩的文件路径是否存在，并且路径是否在正确的沙箱路径下。

#### 900002 传入的目标文件错误

**错误信息**

The input destination file is invalid.

**错误描述**

当调用compressFile或decompressFile接口时，传入目标文件无效。

**可能原因**

1. 当调用compressFile接口时，传入的目标文件路径无效，如不存在的沙箱路径。
1. 当调用decompressFile接口时，传入的目标目录不存在。

**处理步骤**

1. 检查目标文件路径是否正确，如果不正确，填写正确的沙箱路径。
1. 检查目标文件目录是否存在，如果不存在，新建这个路径。

#### 900003 传入的源文件格式错误或者已损坏

**错误信息**

The input source file is not in ZIP format or is damaged.

**错误描述**

当调用decompressFile接口时，传入源文件的压缩格式有误或者已损坏。

**可能原因**

1. 当调用decompressFile接口时，传入的源文件压缩格式有误。
1. 当调用decompressFile接口时，传入的源文件不完整或已损坏。

**处理步骤**

1. 检查源文件压缩格式是否为ZIP格式。
1. 检查源文件是否完整，如果是网络下载的，需要确保文件下载完成后再调用decompress接口。

#### 17800002 传入的文件或访问模式错误

**错误信息**

No such file or access mode error.

**错误描述**

当调用gzopen或gzdopen接口时，传入的文件路径、文件描述符或文件访问模式错误。

**可能原因**

1. 当调用gzopen接口时，传入的文件路径或文件访问模式错误。
1. 当调用gzdopen接口时，传入的文件描述符或文件访问模式错误。

**处理步骤**

1. 检查gz文件路径或文件描述符是否正确，如果是新建gz文件的操作，需要确保文件访问模式为压缩模式(w或wb等)。
1. 检查文件访问模式，是否为"w"、"wb"、"r"、"rb"、"a"、"ab"等。

#### 17800004 压缩流或解压流错误

**错误信息**

Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure.

**错误描述**

当调用deflate或inflate等接口时，压缩流或解压流发生错误。

**可能原因**

1. 当调用deflate或inflate等接口时，未先使用deflateInit或inflateInit接口对压缩或解压流进行初始化。
1. 当调用gzsetparams、gzclose或gzflush等接口时，传入的刷新模式错误或接口调用前，调用打开gz文件的相关接口时传入的文件访问模式错误。

**处理步骤**

1. 当调用deflate或inflate等接口前，先使用deflateInit或inflateInit接口对压缩或解压流进行初始化。
1. 检查接口调用前，打开gz文件的相关接口是否未被调用或调用失败。
1. 检查接口调用前，调用打开gz文件的相关接口时传入的访问模式是否与该接口匹配。例如gzprintf属于压缩操作接口，调用打开gz文件的相关接口时传入的访问模式需要为压缩模式(w或wb等)。
1. 检查传入的枚举参数是否正确。

#### 17800005 传入的数据错误

**错误信息**

The input data is incorrect. For example, the data does not conform to the zlib compression format, the compressed data is corrupted, or the data is not compressed.

**错误描述**

当调用uncompress或uncompress2等接口时，传入的数据错误。

**可能原因**

当调用uncompress或uncompress2接口时，未先使用compress接口进行压缩。

**处理步骤**

先使用compress进行压缩后再通过uncompress2或uncompress进行解压。

#### 17800006 内存分配失败错误

**错误信息**

Memory allocation failed.

**错误描述**

当调用gzclose或gzclosew接口时，内存分配失败。

**可能原因**

在调用gzclose或gzclosew接口前，调用了gzsetparams接口，传入错误的压缩级别或压缩策略。

**处理步骤**

检查gzsetparams接口的调用，传入正确的压缩级别和压缩策略。

#### 17800007 传入的缓冲区错误

**错误信息**

The input buffer is incorrect, and the output buffer is too small to accommodate the compressed or decompressed data.

**错误描述**

当调用compress或compress2或uncompress或uncompress2接口时，传入的缓冲区错误。

**可能原因**

1. 当调用uncompress或uncompress2接口时，传入的输入buffer大小大于解压后输出buffer的大小。
1. 当调用compress或compress2接口时，传入的输入buffer大小大于压缩后输出buffer的大小。
1. 当调用compress或compress2或uncompress或uncompress2接口，传入的buffer大小为0。

**处理步骤**

增大对应buffer的大小。

#### 17800009 内部结构错误

**错误信息**

Internal structure error.

**错误描述**

当调用gzputc、gzwrite、gzread等接口时，传入的参数错误或接口调用前，调用打开gz文件的相关接口时传入的文件访问模式错误。

**可能原因**

1. 当调用接口前，打开gz文件的相关接口未被调用或调用失败。
1. 当调用接口前，调用打开gz文件的相关接口时传入的文件访问模式错误。
1. 当调用gzwrite接口时，传入的未压缩字节长度为0。
1. 当调用gzfwrite或gzfread接口时，传入的数据块大小或数量为0。
1. 当调用gzprintf接口时，传入的格式化描述符和纯文本为空字符串。
1. 当调用gzgets接口时，传入空的ArrayBuffer。
1. 当调用gzgetc接口时，gz文件为空文件。

**处理步骤**

1. 检查接口调用前，打开gz文件的相关接口是否未被调用或调用失败。
1. 检查接口调用前，调用打开gz文件的相关接口时传入的访问模式是否与该接口匹配。例如gzgetc属于解压缩操作接口，调用打开gz文件的相关接口时传入的访问模式需要为解压缩模式(r或rb等)。
1. 检查传入的参数是否正确。