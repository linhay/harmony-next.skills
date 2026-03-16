# Drawing

#### 概述

Drawing模块提供包括2D图形渲染、文字绘制和图片显示等功能函数。

本模块采用屏幕物理像素单位px。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

#### 文件汇总

名称描述[drawing_bitmap.h](../../capi/headers/drawing_bitmap.h.md)文件中定义了与位图相关的功能函数。[drawing_brush.h](../../capi/headers/drawing_brush.h.md)文件中定义了与画刷相关的功能函数。[drawing_canvas.h](../../capi/headers/drawing_canvas.h.md)

文件中定义了与画布相关的功能函数。

画布自带一个黑色，开启抗锯齿，不具备其他任何样式的默认画刷，当且仅当画布中主动设置的画刷和画笔都不存在时生效。

[drawing_color.h](../../capi/headers/drawing_color.h.md)文件中定义了与颜色相关的功能函数。[drawing_color_filter.h](../../capi/headers/drawing_color_filter.h.md)声明与绘图模块中的颜色滤波器对象相关的函数。[drawing_color_space.h](../../capi/headers/drawing_color_space.h.md)文件中定义了与颜色空间相关的功能函数。[drawing_error_code.h](../../capi/headers/drawing_error_code.h.md)声明与绘图模块中的错误码相关的函数。include native_drawing/drawing_error_code.h[drawing_filter.h](../../capi/headers/drawing_filter.h.md)声明与绘图模块中的滤波器对象相关的函数。[drawing_font.h](../../capi/headers/drawing_font.h.md)文件中定义了与字体相关的功能函数。[drawing_font_collection.h](../../capi/headers/drawing_font_collection.h.md)定义绘制模块中与字体集合相关的函数。[drawing_font_mgr.h](../../capi/headers/drawing_font_mgr.h.md)文件中定义了与字体管理相关的功能函数，用于加载和匹配系统中可用的字体。[drawing_gpu_context.h](../../capi/headers/drawing_gpu_context.h.md)声明与绘图模块中的图形处理器上下文对象相关的函数。[drawing_image.h](../../capi/headers/drawing_image.h.md)文件中定义了与图片相关的功能函数。[drawing_image_filter.h](../../capi/headers/drawing_image_filter.h.md)声明与绘图模块中的图像滤波器对象相关的函数。[drawing_mask_filter.h](../../capi/headers/drawing_mask_filter.h.md)声明与绘图模块中的对象相关的函数。[drawing_matrix.h](../../capi/headers/drawing_matrix.h.md)文件中定义了与矩阵相关的功能函数。[drawing_memory_stream.h](../../capi/headers/drawing_memory_stream.h.md)文件中定义了与内存流相关的功能函数。[drawing_path.h](../../capi/headers/drawing_path.h.md)文件中定义了与自定义路径相关的功能函数。[drawing_path_effect.h](../../capi/headers/drawing_path_effect.h.md)文件中定义了与路径效果相关的功能函数。[drawing_pen.h](../../capi/headers/drawing_pen.h.md)文件中定义了与画笔相关的功能函数。[drawing_pixel_map.h](../../capi/headers/drawing_pixel_map.h.md)声明与绘图模块中的像素图对象相关的函数。[drawing_point.h](../../capi/headers/drawing_point.h.md)文件中定义了与坐标点相关的功能函数。[drawing_record_cmd.h](../../capi/headers/drawing_record_cmd.h.md)文件中定义了与录制指令对象相关的功能函数。[drawing_rect.h](../../capi/headers/drawing_rect.h.md)文件中定义了与矩形相关的功能函数。[drawing_region.h](../../capi/headers/drawing_region.h.md)定义了与区域相关的功能函数，包括区域的创建，边界设置和销毁等。[drawing_register_font.h](../../capi/headers/drawing_register_font.h.md)定义绘制模块中字体管理器相关的函数。[drawing_round_rect.h](../../capi/headers/drawing_round_rect.h.md)文件中定义了与圆角矩形相关的功能函数。[drawing_sampling_options.h](../../capi/headers/drawing_sampling_options.h.md)文件中定义了与采样相关的功能函数。用于图片或者纹理等图像的采样。[drawing_shader_effect.h](../../capi/headers/drawing_shader_effect.h.md)声明与绘图模块中的着色器对象相关的函数。[drawing_shadow_layer.h](../../capi/headers/drawing_shadow_layer.h.md)声明与绘图模块中的阴影层对象相关的函数。[drawing_surface.h](../../capi/headers/drawing_surface.h.md)文件中定义与surface相关的功能函数，包括surface的创建、销毁和使用等。[drawing_text_blob.h](../../capi/headers/drawing_text_blob.h.md)文件中定义了与文字相关的功能函数。[drawing_text_declaration.h](../../capi/headers/drawing_text_declaration.h.md)提供2d 绘制文本相关的数据结构声明[drawing_text_font_descriptor.h](../../capi/headers/drawing_text_font_descriptor.h.md)定义了字体信息的相关接口，比如获取字体信息，查找指定字体等。[drawing_text_global.h](../../capi/headers/drawing_text_global.h.md)提供文本全局信息的相关接口，比如设置文本渲染高对比度模式等。[drawing_text_line.h](../../capi/headers/drawing_text_line.h.md)提供获取文本行内的字符位置、获取渲染单元信息和按行截断等功能。[drawing_text_lineTypography.h](../../capi/headers/drawing_text_lineTypography.h.md)提供排版行相关的接口，比如获取指定位置处开始可以排版的字符个数等函数。[drawing_text_run.h](../../capi/headers/drawing_text_run.h.md)提供字体渲染单元的相关接口，比如绘制功能、获取排版边界功能等。[drawing_text_typography.h](../../capi/headers/drawing_text_typography.h.md)定义绘制模块中排版相关的函数。[drawing_typeface.h](../../capi/headers/drawing_typeface.h.md)

文件中定义了与字形相关的功能函数。

不同的平台有自己的默认字形，也可以从ttf文件解析出三方指定字形，如宋体、黑体字形等。

[drawing_types.h](../../capi/headers/drawing_types.h.md)文件中定义了用于绘制2d图形的数据类型，包括画布、画笔、画刷、位图和路径。