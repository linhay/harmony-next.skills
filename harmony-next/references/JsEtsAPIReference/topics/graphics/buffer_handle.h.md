# buffer_handle.h

**概述**

定义NativeWindow模块使用的BufferHandle的结构体。

引用文件： <native_window/buffer_handle.h>

库： libnative_window.so

系统能力： SystemCapability.Graphic.Graphic2D.NativeWindow

起始版本： 8

相关模块： [NativeWindow](NativeWindow.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| BufferHandle | BufferHandle | 缓冲区句柄，用于对缓冲区的信息传递和获取。句柄包含了缓冲区的文件描述符、尺寸、格式、用途、虚拟地址、共享内存键、物理地址、自定义数据。 |