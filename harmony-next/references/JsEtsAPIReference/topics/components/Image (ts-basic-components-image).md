[]()[]()

# Image

Image为图片组件，常用于在应用中显示图片。Image支持加载[PixelMap](../../types/interfaces/Interface (PixelMap).md)、[ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)和[DrawableDescriptor](#ZH-CN_TOPIC_0000002497444922__drawabledescriptor10)类型的数据源，支持png、jpg、jpeg、bmp、svg、webp、gif和heif类型的图片格式，不支持apng和svga格式。

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

使用快捷组合键对Image组件复制时，Image组件必须处于获焦状态，如何获焦请参考[设置组件是否可获焦](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-events-focus-event#设置组件是否可获焦)。Image组件默认不获焦，需将[focusable](../misc/焦点控制.md#ZH-CN_TOPIC_0000002529444807__focusable)属性设置为true，即可使用Tab键将焦点切换到组件上，再将[focusOnTouch](../misc/焦点控制.md#ZH-CN_TOPIC_0000002529444807__focusontouch9)属性设置为true，即可实现点击获焦。

图片格式支持SVG图源，SVG标签文档请参考[SVG标签说明](../../guides/SVG标签说明.md)。

动图的播放依赖于Image节点的可见性变化，其默认行为是不播放的。当节点可见时，通过回调启动动画，当节点不可见时，停止动画。可见性状态的判断是通过[onVisibleAreaChange](../misc/组件可见区域变化事件.md#ZH-CN_TOPIC_0000002497444844__onvisibleareachange)事件触发的，当可见阈值ratios大于0时，表明Image处于可见状态。

如果图片加载过程中出现白色块，请参考[Image白块问题解决方案](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-image-white-lump-solution)。如果图片加载时间过长，请参考[预置图片资源加载优化](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-texture-compression-improve-performance)。

[]()[]()

#### 需要权限

使用网络图片时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions)。

[]()[]()

#### 子组件

无

[]()[]()

#### 接口

[]()[]()

#### Image

Image(src: PixelMap | ResourceStr | DrawableDescriptor)

通过图片数据源获取图片，用于后续渲染展示。

Image组件加载图片失败或图片尺寸为0时，图片组件大小自动为0，不跟随父组件的布局约束。

Image组件默认按照居中裁剪，例如组件宽高设置相同，原图长宽不等，此时按照中间区域进行裁剪。

Image加载成功且组件不设置宽高时，其显示大小自适应父组件。

-

Image直接传入URL可能会带来的潜在性能问题，例如：(1) 大图加载时无法提前下载，白块显示的时间较长；(2) 小图设置同步加载，在弱网环境下，可能会阻塞UI线程造成冻屏问题；(3) 在快速滑动的瀑布流中，无法提前对即将要显示的图片进行下载，导致滑动白块较多。不同场景下，性能问题会有不同的表现，建议将网络下载部分与Image的显示剥离，可提前下载或者异步下载。如果图片加载过程中出现白色块，请参考[Image白块问题解决方案](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-image-white-lump-solution)。如果图片加载时间过长，请参考[预置图片资源加载优化](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-texture-compression-improve-performance)。

-

src由有效值（可正常解析并加载的图片资源）切换为无效值（无法解析或加载的图片路径）时，组件应保持显示此前成功加载的图片内容，不进行清除或重置操作。

-

当Image组件入参为[PixelMap](../../types/interfaces/Interface (PixelMap).md)类型时，只有当PixelMap对象发生变化（即指向一个新的PixelMap实例），Image组件才能感知到数据的变化。仅修改PixelMap对象的内容（如像素值）而不更换对象引用，无法触发数据变化的感知。

-

Image组件入参为Base64字符串时，Base64字符串通用格式为data:image/subtype;base64,Base64EncodedData，其中subtype为类型声明，Base64EncodedData为数据对应的base64编码，其他为固定字符串。例如：png图像对应的入参为data:image/png;base64,iVBORw0KGgo...。

  1.

image/subType用于声明数据内容的类型。Image组件不会强制校验声明的类型与Base64解码后的实际图片格式是否完全一致。在部分场景下，即使声明的类型与真实格式不一致，图片仍可能正常显示。为避免未来行为变化或未知问题，建议始终保持类型与实际图片格式一致。

  1.

Image组件不支持data:image/*;base64,Base64EncodedData的通配写法，subType必须显示声明具体的图片类型。

  1.

Image组件不支持通过Base64字符串形式加载SVG图片。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明src[PixelMap](../misc/图像类型定义.md#ZH-CN_TOPIC_0000002497604902__pixelmap) | [ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)| [DrawableDescriptor](#ZH-CN_TOPIC_0000002497444922__drawabledescriptor10)是

图片的数据源，支持本地图片和网络图片，引用方式请参考[加载图片资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-graphics-display#加载图片资源)。

1. PixelMap格式为像素图，常用于图片编辑的场景。

2. ResourceStr包含Resource和string格式。

string格式可用于加载网络图片和本地图片，常用于加载网络图片。当[使用相对路径引用本地图片](#ZH-CN_TOPIC_0000002497444922__示例25使用相对路径显示图片)时，不支持跨包/跨模块调用该Image组件，建议使用Resource格式来管理需全局使用的图片资源。

- 支持Base64字符串。

- 传入的字符串为https网络图片地址时，建议参考[示例2下载与显示静态网络图片](#ZH-CN_TOPIC_0000002497444922__示例2下载与显示静态网络图片)。

- 支持file://路径前缀的字符串，应用沙箱URI：file://<bundleName>/<sandboxPath>。应用沙箱路径URI构造可参考[constructor](../../modules/ohos/@ohos.file.fileuri (文件URI).md#ZH-CN_TOPIC_0000002529285247__constructor10)。沙箱路径需要使用[fileUri.getUriFromPath(path)](../../modules/ohos/@ohos.file.fileuri (文件URI).md#ZH-CN_TOPIC_0000002529285247__fileurigeturifrompath)方法将路径转换为应用沙箱URI，然后传入显示。同时需要保证目录包路径下的文件有可读权限。

Resource格式可以跨包/跨模块访问资源文件，是访问本地图片的推荐方式，具体示例参考[跨HAP/HSP包应用资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resource-categories-and-access#跨haphsp包应用资源)。

3. 当传入资源id或name为普通图片时，生成DrawableDescriptor对象。传入[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)类型可播放PixelMap数组动画。

**说明：**

- ArkTS卡片上支持gif图片格式动效，但仅在显示时播放一次。

- ArkTS卡片上不支持http://等网络相关路径前缀和file://路径前缀的字符串。

[]()[]()

#### Image12+

Image(src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent)

src新增[ImageContent](#ZH-CN_TOPIC_0000002497444922__imagecontent12)类型，可指定对应的图形内容。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明src[PixelMap](../misc/图像类型定义.md#ZH-CN_TOPIC_0000002497604902__pixelmap) | [ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)| [DrawableDescriptor](#ZH-CN_TOPIC_0000002497444922__drawabledescriptor10)| [ImageContent](#ZH-CN_TOPIC_0000002497444922__imagecontent12)是

图片的数据源，支持本地图片和网络图片，引用方式请参考[加载图片资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-graphics-display#加载图片资源)。

PixelMap、ResourceStr和DrawableDescriptor的使用请参考[Image](#ZH-CN_TOPIC_0000002497444922__image-1)的src参数说明。

传入[ImageContent](#ZH-CN_TOPIC_0000002497444922__imagecontent12)类型，指定图像内容。

**说明：**

- ArkTS卡片上支持gif图片格式动效，但仅在显示时播放一次。

- ArkTS卡片上不支持http://等网络相关路径前缀和file://路径前缀的字符串。

[]()[]()

#### Image12+

Image(src: PixelMap | ResourceStr | DrawableDescriptor, imageAIOptions: ImageAIOptions)

Image新增[imageAIOptions](../misc/图像类型定义.md#ZH-CN_TOPIC_0000002497604902__imageaioptions12)参数，为组件设置AI分析选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明src[PixelMap](../misc/图像类型定义.md#ZH-CN_TOPIC_0000002497604902__pixelmap) | [ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)| [DrawableDescriptor](#ZH-CN_TOPIC_0000002497444922__drawabledescriptor10)是

图片的数据源，支持本地图片和网络图片，引用方式请参考[加载图片资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-graphics-display#加载图片资源)。

PixelMap、ResourceStr和DrawableDescriptor的使用请参考[Image](#ZH-CN_TOPIC_0000002497444922__image-1)的src参数说明。

**说明：**

- ArkTS卡片上支持gif图片格式动效，但仅在显示时播放一次。

- ArkTS卡片上不支持http://等网络相关路径前缀和file://路径前缀的字符串。

imageAIOptions[ImageAIOptions](../misc/图像类型定义.md#ZH-CN_TOPIC_0000002497604902__imageaioptions12)是给组件设置一个AI分析选项，通过此项可配置分析类型或绑定一个分析控制器。[]()[]()

#### 属性

属性的详细使用指导请参考[添加属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-graphics-display#添加属性)。除支持[通用属性](通用属性 (ts-component-general-attributes).md)外，还支持以下属性：

Image组件不支持设置通用属性[foregroundColor](../misc/前景色设置.md#ZH-CN_TOPIC_0000002497604836__foregroundcolor)，可以通过Image组件的[fillColor](#ZH-CN_TOPIC_0000002497444922__fillcolor)属性设置填充颜色。

[]()[]()

#### alt

alt(value: string | Resource | PixelMap)

设置图片加载过程中显示的占位图。

占位图支持使用[objectFit](#ZH-CN_TOPIC_0000002497444922__objectfit)设置填充效果，与图片的填充效果一致。

当组件的参数类型为[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuestring | [Resource](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | [PixelMap](../../types/interfaces/Interface (PixelMap).md)12+是

设置图片加载过程中显示的占位图，支持本地图片（png、jpg、bmp、svg、gif和heif类型），支持[PixelMap](../../types/interfaces/Interface (PixelMap).md)类型图片，不支持网络图片。

- 支持Base64字符串。

- 支持file://路径前缀的字符串，应用沙箱URI：file://<bundleName>/<sandboxPath>。应用沙箱路径URI构造可参考[constructor](../../modules/ohos/@ohos.file.fileuri (文件URI).md#ZH-CN_TOPIC_0000002529285247__constructor10)。沙箱路径需要使用[fileUri.getUriFromPath(path)](../../modules/ohos/@ohos.file.fileuri (文件URI).md#ZH-CN_TOPIC_0000002529285247__fileurigeturifrompath)方法将路径转换为应用沙箱URI，然后传入显示。同时需要保证目录包路径下的文件有可读权限。

默认值：null

由有效值（可正常解析并加载的图片资源）切换为无效值（无法解析或加载的图片路径）时，组件保持显示此前成功加载的图片内容，不进行清除或重置操作。

[]()[]()

#### alt22+

alt(src: ResourceStr | PixelMap | ImageAlt)

设置图片加载过程中和加载失败时的占位图。

通过[ImageAlt](#ZH-CN_TOPIC_0000002497444922__imagealt22)配置占位图时，Image会根据用户配置的加载过程中和加载失败的占位图源生效，未配置时默认不显示。

占位图支持使用[objectFit](#ZH-CN_TOPIC_0000002497444922__objectfit)设置填充效果，与图片的填充效果一致。

当组件的参数类型为[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 22开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明src[ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | [PixelMap](../../types/interfaces/Interface (PixelMap).md)| [ImageAlt](#ZH-CN_TOPIC_0000002497444922__imagealt22)是

设置图片加载过程中和加载失败时的占位图，支持本地图片（png、jpg、bmp、svg、gif和heif类型），支持[PixelMap](../../types/interfaces/Interface (PixelMap).md)类型图片，不支持网络图片。

- 支持Base64字符串。

- 支持file://路径前缀的字符串，应用沙箱URI：file://<bundleName>/<sandboxPath>。应用沙箱路径URI构造可参考[constructor](../../modules/ohos/@ohos.file.fileuri (文件URI).md#ZH-CN_TOPIC_0000002529285247__constructor10)。沙箱路径需要使用[fileUri.getUriFromPath(path)](../../modules/ohos/@ohos.file.fileuri (文件URI).md#ZH-CN_TOPIC_0000002529285247__fileurigeturifrompath)方法将路径转换为应用沙箱URI，然后传入显示。同时需要保证目录包路径下的文件有可读权限。

[]()[]()

#### objectFit

objectFit(value: ImageFit)

设置图片的填充效果。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ImageFit](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__imagefit)是

图片的填充效果。

默认值：ImageFit.Cover

[]()[]()

#### imageMatrix15+

imageMatrix(matrix: ImageMatrix)

设置图片的变换矩阵。通过[ImageMatrix](#ZH-CN_TOPIC_0000002497444922__imagematrix15对象说明)对象使用平移、旋转、缩放等函数，实现宫格缩略图的最佳呈现。SVG类型图源不支持该属性。

设置resizable、objectRepeat属性时，该属性设置不生效。该属性只针对图源做处理，不会触发Image组件的回调事件。

该属性与[objectFit](#ZH-CN_TOPIC_0000002497444922__objectfit)属性强关联，仅在[objectFit](#ZH-CN_TOPIC_0000002497444922__objectfit)属性设置为[ImageFit](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__imagefit).MATRIX时生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明matrix[ImageMatrix](#ZH-CN_TOPIC_0000002497444922__imagematrix15对象说明)是图片的变换矩阵。[]()[]()

#### objectRepeat

objectRepeat(value: ImageRepeat)

设置图片的重复样式，从中心点向两边重复，剩余空间不足放下一张图片时会截断。SVG类型图源不支持该属性。

当组件的参数类型为[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ImageRepeat](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__imagerepeat)是

图片的重复样式。

默认值：ImageRepeat.NoRepeat

[]()[]()

#### interpolation

interpolation(value: ImageInterpolation)

设置图片的插值效果，即缓解图片在缩放时的锯齿问题。SVG类型图源不支持该属性。

当组件的参数类型为[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ImageInterpolation](#ZH-CN_TOPIC_0000002497444922__imageinterpolation)是

图片的插值效果。

默认值：ImageInterpolation.Low

设置undefined时，取值为ImageInterpolation.None。

[]()[]()

#### renderMode

renderMode(value: ImageRenderMode)

设置图片的渲染模式。SVG类型图源不支持该属性。

设置 [ColorFilter](#ZH-CN_TOPIC_0000002497444922__colorfilter9) 时，该属性设置不生效。

当组件的参数类型为[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ImageRenderMode](#ZH-CN_TOPIC_0000002497444922__imagerendermode)是

图片的渲染模式为原色或黑白。

默认值：ImageRenderMode.Original

[]()[]()

#### sourceSize

sourceSize(value: ImageSourceSize)

设置图片解码尺寸。仅在目标尺寸小于图源尺寸时生效。SVG类型图源和PixelMap资源不支持该属性。

当组件的参数类型为[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ImageSourceSize](#ZH-CN_TOPIC_0000002497444922__imagesourcesize18对象说明)是图片解码尺寸参数，降低图片的分辨率，常用于需要让图片显示尺寸比组件尺寸更小的场景。和ImageFit.None配合使用时可在组件内显示小图。[]()[]()

#### matchTextDirection

matchTextDirection(value: boolean)

设置图片是否跟随系统语言方向，在RTL语言环境下显示镜像翻转显示效果。

当组件的参数类型为[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

图片是否跟随系统语言方向。

默认值：false，false表示图片不跟随系统语言方向，true表示图片跟随系统语言方向，在RTL语言环境下显示镜像翻转显示效果。

[]()[]()

#### fitOriginalSize

fitOriginalSize(value: boolean)

设置图片的显示尺寸是否跟随图源尺寸。

图片组件已设置width、height属性时，fitOriginalSize属性不生效。

当组件的参数类型为[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

图片的显示尺寸是否跟随图源尺寸。

默认值：false

**说明：**

当不设置fitOriginalSize或者设置fitOriginalSize为false时，组件显示大小不跟随图源大小。

当设置fitOriginalSize为true时，组件显示大小跟随图源大小。

[]()[]()

#### fillColor

fillColor(value: ResourceColor)

设置填充颜色。仅对SVG图源生效，设置后会替换SVG图片中所有可绘制元素的填充颜色。如需对png图片进行修改颜色，可以使用[colorFilter](#ZH-CN_TOPIC_0000002497444922__colorfilter9)。

当组件的参数类型为[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)是

设置填充颜色。

**说明：**

默认不对组件进行填充。当传入异常值时，系统将使用默认的主题色：浅色模式下为黑色，深色模式下为白色。

从API version 21开始，当[supportSvg2](#ZH-CN_TOPIC_0000002497444922__supportsvg221)设置为true时，fillColor依赖SVG图源中fill属性的参数配置。当SVG图源中fill属性为'none'时，fillColor不生效。

[]()[]()

#### fillColor15+

fillColor(color: ResourceColor|ColorContent)

设置填充颜色。仅对SVG图源生效，设置后会替换SVG图片中所有可绘制元素的填充颜色。如需对png图片进行修改颜色，可以使用[colorFilter](#ZH-CN_TOPIC_0000002497444922__colorfilter9)。如果想重置填充颜色可以传入[ColorContent](#ZH-CN_TOPIC_0000002497444922__colorcontent15)类型。

当组件的参数类型为[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)时设置该属性不生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明color[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)|[ColorContent](#ZH-CN_TOPIC_0000002497444922__colorcontent15)是

设置填充颜色。

**说明：**

默认不对组件进行填充。当传入异常值时，系统将使用默认的主题色：浅色模式下为黑色，深色模式下为白色。

从API version 21开始，当[supportSvg2](#ZH-CN_TOPIC_0000002497444922__supportsvg221)设置为true时，fillColor依赖SVG图源中fill属性的参数配置。当SVG图源中fill属性为'none'时，fillColor不生效。

[]()[]()

#### fillColor20+

fillColor(color: ResourceColor|ColorContent|ColorMetrics)

设置填充颜色。仅对SVG图源生效，设置后会替换SVG图片中所有可绘制元素的填充颜色。如需对png图片进行修改颜色，可以使用[colorFilter](#ZH-CN_TOPIC_0000002497444922__colorfilter9)。如果想重置填充颜色可以传入[ColorContent](#ZH-CN_TOPIC_0000002497444922__colorcontent15)类型。支持通过传入[ColorMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)类型设置P3色域颜色值，可在支持高色域的设备上获得更丰富的色彩表现。

当组件的参数类型为[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)时设置该属性不生效。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明color[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)|[ColorContent](#ZH-CN_TOPIC_0000002497444922__colorcontent15)|[ColorMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)是

设置填充颜色。

**说明：**

默认不对组件进行填充。当传入异常值时，系统将使用默认的主题色：浅色模式下为黑色，深色模式下为白色。

从API version 21开始，当[supportSvg2](#ZH-CN_TOPIC_0000002497444922__supportsvg221)设置为true时，fillColor依赖SVG图源中fill属性的参数配置。当SVG图源中fill属性为'none'时，fillColor不生效。

[]()[]()

#### autoResize

autoResize(value: boolean)

设置图片解码过程中是否对图源自动缩放。降采样解码时图片的部分信息丢失，因此可能会导致图片质量的下降（如：出现锯齿），这时可以选择把autoResize设为false，按原图尺寸解码，提升显示效果，但会增加内存占用。

原图尺寸和显示尺寸不匹配时，图片都会出现些许的失真、模糊。最佳清晰度配置建议：

图片缩小显示时：.autoResize(false) + .interpolation(.Medium)

图片放大显示时：.interpolation(.High)

当组件的参数类型为[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)和SVG时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

图片解码过程中是否对图源自动缩放。设置为true时，组件会根据显示区域的尺寸决定用于绘制的图源尺寸，有利于减少内存占用。如原图大小为800x1200，而显示区域大小为200x200，则图片会降采样解码到200x300的尺寸（实际计算过程中会依赖缩放和填充类型的配置，从而得到的计算结果会有差异），从而大幅度节省图片占用的内存。

默认值：false，false表示关闭图源自动缩放，true表示开启图源自动缩放。

[]()[]()

#### syncLoad8+

syncLoad(value: boolean)

设置是否同步加载图片。建议加载尺寸较小的本地图片时将syncLoad设为true，因为耗时较短，在主线程上执行即可。

当组件的参数类型为[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)时设置该属性不生效。

如果加载图片时出现闪烁，设置syncLoad为true。详情请参见[并发优化](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-click-to-click-response-optimization#section715115119192)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

是否同步加载图片，默认是异步加载。同步加载时阻塞UI线程，不会显示占位图。

默认值：false，false表示异步加载图片，true表示同步加载图片。

阻塞主线程超过6s将导致AppFreeze，具体参考[AppFreeze（应用冻屏）检测](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appfreeze-guidelines)。

[]()[]()

#### copyOption9+

copyOption(value: CopyOptions)

设置图片是否可复制。当copyOption设置为非CopyOptions.None时，支持使用长按、鼠标右击、快捷组合键'CTRL+C'等方式进行复制。SVG图片不支持复制。

当组件的参数类型为[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[CopyOptions](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__copyoptions9)是

图片是否可复制。

默认值：CopyOptions.None

[]()[]()

#### colorFilter9+

colorFilter(value: ColorFilter | DrawingColorFilter)

为图像设置颜色滤镜效果。

设置该属性时，[renderMode](#ZH-CN_TOPIC_0000002497444922__rendermode)属性设置不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ColorFilter](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__colorfilter9) | [DrawingColorFilter12+](#ZH-CN_TOPIC_0000002497444922__drawingcolorfilter12)是

1. 给图像设置颜色滤镜效果，入参为一个的4x5的RGBA转换矩阵。

2. 从API version12开始支持@ohos.graphics.drawing的ColorFilter类型作为入参。

**说明：**

API version 11及之前，SVG类型图源不支持该属性。

从API version 12开始，该接口中的DrawingColorfilter类型支持在元服务中使用。其中，SVG类型的图源只有设置了stroke属性（无论是否有值）才会生效。

从API version 21开始，当[supportSvg2](#ZH-CN_TOPIC_0000002497444922__supportsvg221)属性设置为true时，colorFilter属性对整个SVG图源起作用。

颜色滤镜通过一个4x5的矩阵来设置图像的颜色滤镜，矩阵第一行表示R（红色）的向量值，第二行表示G（绿色）的向量值，第三行表示B（蓝色）的向量值，第四行表示A（透明度）的向量值，4行分别代表不同的RGBA的向量值。

当矩阵对角线值为1，其余值为0时，保持图片原有色彩。

**计算规则：**

如果输入的滤镜矩阵如下（其中矩阵值的范围[0, 1]）：

像素点为[R, G, B, A]，色值的范围[0, 255]

则过滤后的颜色为 [R’, G’, B’, A’]

该属性的具体使用可以参考[示例9](#ZH-CN_TOPIC_0000002497444922__示例9为图像设置颜色滤镜效果)。

[]()[]()

#### draggable9+

draggable(value: boolean)

设置组件默认拖拽效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

组件默认拖拽效果，设置为true时，组件可拖拽，绑定的长按手势不生效。

API version 9及之前，默认值为false。API version 10及之后，默认值为true。

若用户需要设置自定义手势，则需要将draggable设置为false。设置为false之后，拖拽类事件不再触发。

[]()[]()

#### enableAnalyzer11+

enableAnalyzer(enable: boolean)

设置组件支持AI分析，当前支持主体识别、文字识别和对象查找等功能。具体使用指导请参考[AI识图](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/vision-imageanalyzer)。

不能和[overlay](../misc/浮层.md)属性同时使用，两者同时设置时overlay中[CustomBuilder](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8)属性将失效。该特性依赖设备能力。

分析图像要求是静态非矢量图，即svg、gif等图像类型不支持分析，支持传入[PixelMap](../../types/interfaces/Interface (PixelMap).md)进行分析，目前仅支持[RGBA_8888](../graphics/Enums (arkts-apis-image-e).md#ZH-CN_TOPIC_0000002529285837__pixelmapformat7)类型，使用方式见[示例5开启图像AI分析](#ZH-CN_TOPIC_0000002497444922__示例5开启图像ai分析)。

[alt](#ZH-CN_TOPIC_0000002497444922__alt)占位图不支持分析，[objectRepeat](#ZH-CN_TOPIC_0000002497444922__objectrepeat)属性仅在[ImageRepeat](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__imagerepeat).NoRepeat下支持分析，隐私遮罩属性[obscured](../misc/隐私遮罩.md)打开时不支持分析。

基于完整原始图像进行分析，设置[clip](../misc/形状裁剪.md#ZH-CN_TOPIC_0000002529284827__clip12)、[margin](../misc/尺寸设置.md#ZH-CN_TOPIC_0000002497444850__margin)、[borderRadius](../misc/边框设置.md#ZH-CN_TOPIC_0000002497604832__borderradius)、[position](../misc/位置设置.md#ZH-CN_TOPIC_0000002529284821__position)和[objectFit](#ZH-CN_TOPIC_0000002497444922__objectfit)属性导致图像显示不完整，或使用[renderMode](#ZH-CN_TOPIC_0000002497444922__rendermode)设置蒙层，仍基于完整原始图像进行分析。 [copyOption](#ZH-CN_TOPIC_0000002497444922__copyoption9)属性不影响AI分析功能。

当组件的参数类型为[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)时设置该属性不生效。

-

需要配置权限：ohos.permission.INTERNET。

-

从API version 12开始，该接口支持在[attributeModifier](../misc/动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明enableboolean是

Image组件是否支持AI分析。

设置为true时，Image组件支持AI分析。设置为false时，Image组件不支持AI分析。

默认值：false

[]()[]()

#### resizable11+

resizable(value: ResizableOptions)

设置图像拉伸时可调整大小的图像选项。拉伸对拖拽缩略图以及占位图有效。

设置合法的 [ResizableOptions](#ZH-CN_TOPIC_0000002497444922__resizableoptions11) 时，objectRepeat属性和orientation属性设置不生效。

当设置 top +bottom 大于原图的高或者 left + right 大于原图的宽时 [ResizableOptions](#ZH-CN_TOPIC_0000002497444922__resizableoptions11) 属性设置不生效。

当组件的参数类型为[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)和SVG时设置该属性不生效。

从API version 20开始，该接口支持在[attributeModifier](../misc/动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ResizableOptions](#ZH-CN_TOPIC_0000002497444922__resizableoptions11)是图像拉伸时可调整大小的图像选项。[]()[]()

#### privacySensitive12+

privacySensitive(supported: boolean)

设置是否支持卡片敏感隐私信息。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明supportedboolean是

是否支持卡片敏感隐私信息。

默认值为false，表示不支持卡片敏感隐私信息，当设置为true时，隐私模式下图片将显示为半透明底板样式。

**说明：**

设置null则不敏感。

进入隐私模式需要卡片框架支持。

[]()[]()

#### dynamicRangeMode12+

dynamicRangeMode(value: DynamicRangeMode)

设置期望展示的图像动态范围。SVG类型图源不支持该属性。

**设备行为差异：** 该接口在手机、PC/2in1和Tablet设备中可正常生效，在其他设备类型中无效果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[DynamicRangeMode](#ZH-CN_TOPIC_0000002497444922__dynamicrangemode12枚举说明)是

图像显示的动态范围。

默认值：DynamicRangeMode.STANDARD

[]()[]()

#### orientation14+

orientation(orientation: ImageRotateOrientation)

设置图像内容的显示方向。

该属性对[alt](#ZH-CN_TOPIC_0000002497444922__alt)占位图不生效。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明orientation[ImageRotateOrientation](#ZH-CN_TOPIC_0000002497444922__imagerotateorientation14)是

图像内容的显示方向。

仅支持静态位图的显示。

如果需要显示携带旋转角度信息或翻转信息的图片，建议使用ImageRotateOrientation.AUTO进行设置。

默认值：ImageRotateOrientation.UP

设置为undefined或null时，取值为ImageRotateOrientation.AUTO。

[]()[]()

#### hdrBrightness19+

hdrBrightness(brightness: number)

设置组件在显示HDR图片时的亮度。

SVG类型图源不支持该属性。

该属性与[dynamicRangeMode](#ZH-CN_TOPIC_0000002497444922__dynamicrangemode12)属性同时设置时，[dynamicRangeMode](#ZH-CN_TOPIC_0000002497444922__dynamicrangemode12)属性不生效。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明brightnessnumber是

用于调整组件展示HDR图片的亮度，该接口仅对HDR图源生效。

默认值：1.0

取值范围：[0.0，1.0]，小于0和大于1.0时取1。0表示图片按照SDR亮度显示，1表示图片按照当前允许的最高HDR亮度显示。

[]()[]()

#### supportSvg221+

supportSvg2(enable: boolean)

开启或关闭[SVG标签解析能力增强功能](../misc/SVG标签解析能力增强.md)，开启后相关SVG图片显示效果会有变化。

Image组件创建后，不支持动态修改该属性的值。

**卡片能力：** 从API version 21开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明enableboolean是

控制是否开启SVG标签解析能力增强功能。

默认值：false

true：支持SVG解析新能力；false：保持原有SVG解析能力。

[]()[]()

#### contentTransition21+

contentTransition(transition: ContentTransitionEffect)

图片内容发生变化时，触发过渡动效。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明transition[ContentTransitionEffect](../misc/图像类型定义.md#ZH-CN_TOPIC_0000002497604902__contenttransitioneffect21对象说明)是

过渡动效的类型。

其中取值为ContentTransitionEffect.OPACITY表示淡入淡出效果，取值为ContentTransitionEffect.IDENTITY表示无动画效果。

默认值：ContentTransitionEffect.IDENTITY

设置为undefined或null时，取值为ContentTransitionEffect.IDENTITY。

**说明**：对动态图片资源不生效。

[]()[]()

#### ImageContent12+

指定图像内容。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明EMPTY0空图像。[]()[]()

#### ImageInterpolation

图片的插值效果。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明None-最近邻插值。Low-双线性插值。Medium-MipMap插值。High-Cubic插值，插值质量最高，可能会影响图片渲染的速度。[]()[]()

#### ImageRenderMode

图片的渲染模式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明Original-原色渲染模式。Template-黑白渲染模式。[]()[]()

#### ResizableOptions11+

图像拉伸时可调整大小的图像选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明slice[EdgeWidths](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__edgewidths9)否是

边框宽度类型，用于描述组件边框不同方向的宽度。

**说明：**

只有当bottom和right同时大于0时，该属性生效。

当设置了top时，图片顶部拉伸，图片的像素值保持不变。

当设置了right时，图片右部拉伸，图片的像素值保持不变。

当设置了bottom时，图片底部拉伸，图片的像素值保持不变。

当设置了left时，图片左部拉伸，图片的像素值保持不变。

每个方向的宽度默认值为0，传入数字时默认单位为vp。

设置了EdgeWidths后的效果如图1（设置EdgeWidths效果图）所示。

lattice12+[DrawingLattice](#ZH-CN_TOPIC_0000002497444922__drawinglattice12)否是

矩形网格对象。

**说明：**

通过@ohos.graphics.drawing的createImageLattice接口创建Lattice类型作为入参。将图像划分为矩形网格，同时处于偶数列和偶数行上的网格图像是固定的，不会被拉伸。

该参数对[backgroundImageResizable](../misc/背景设置.md#ZH-CN_TOPIC_0000002529444791__backgroundimageresizable12)接口不生效。

传入数字时默认单位为px。

**图1** 设置EdgeWidths效果图

[]()[]()

#### ImageAlt22+

设置图片占位图。

**卡片能力：** 从API version 22开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明placeholder[ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | [PixelMap](../../types/interfaces/Interface (PixelMap).md)否是加载过程中的占位图。error[ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | [PixelMap](../../types/interfaces/Interface (PixelMap).md)否是加载失败的占位图。[]()[]()

#### DynamicRangeMode12+枚举说明

期望展示的图像动态范围。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明HIGH0不受限动态范围，最大限度进行图片提亮。CONSTRAINT1受限动态范围，受限进行图片提亮。STANDARD2标准动态范围，不进行图片提亮。[]()[]()

#### ImageRotateOrientation14+

期望的图像内容显示方向。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明AUTO0

读取图片携带的EXIF元数据作为显示方向，支持旋转和镜像。

PixelMap和DrawableDescriptor类型的图片不包含头信息，调用该接口时图片显示效果不变化。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

UP1

默认按照当前图片的像素数据进行显示，不做任何处理。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

RIGHT2

将当前图片顺时针旋转90度后显示。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

DOWN3

将当前图片顺时针旋转180度后显示。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

LEFT4

将当前图片顺时针旋转270度后显示。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

UP_MIRRORED20+5

将当前图片水平翻转后显示。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

RIGHT_MIRRORED20+6

将当前图片水平翻转再顺时针旋转90度后显示。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

DOWN_MIRRORED20+7

将当前图片垂直翻转后显示。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

LEFT_MIRRORED20+8

将当前图片水平翻转再顺时针旋转270度后显示。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

[]()[]()

#### ImageSourceSize18+对象说明

图片解码尺寸。

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明width7+number否否

图片解码尺寸宽度。

单位：vp

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

height7+number否否

图片解码尺寸高度。

单位：vp

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[]()[]()

#### DrawableDescriptor10+

type DrawableDescriptor = DrawableDescriptor

作为Image组件的入参对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明[DrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__drawabledescriptor)返回一个DrawableDescriptor对象。[]()[]()

#### DrawingColorFilter12+

type DrawingColorFilter = ColorFilter

颜色滤波器对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明[ColorFilter](../../types/classes/Class (ColorFilter).md)返回一个颜色滤波器。[]()[]()

#### DrawingLattice12+

type DrawingLattice = Lattice

将图片按照矩形网格进行划分。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明[Lattice](../../types/classes/Class (Lattice).md)返回一个矩阵网格对象。[]()[]()

#### ImageMatrix15+对象说明

type ImageMatrix = Matrix4Transit

当前的矩阵对象。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明[Matrix4Transit](../../modules/ohos/@ohos.matrix4 (矩阵变换).md#ZH-CN_TOPIC_0000002529284781__matrix4transit)返回当前的矩阵对象。[]()[]()

#### ColorContent15+

指定颜色填充内容。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明ORIGINColorContent是否重置[fillColor](#ZH-CN_TOPIC_0000002497444922__fillcolor)接口，效果上与不设置[fillColor](#ZH-CN_TOPIC_0000002497444922__fillcolor)一致。[]()[]()

#### 事件

除支持[通用事件](通用事件 (ts-component-general-events).md)外，还支持以下事件：

[]()[]()

#### onComplete

onComplete(callback: (event?: { width: number, height: number, componentWidth: number, componentHeight: number, loadingStatus: number,contentWidth: number, contentHeight: number, contentOffsetX: number, contentOffsetY: number }) => void)

图片数据加载成功和解码成功时均触发该回调，返回成功加载的图片尺寸。

当组件的参数类型为[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)时该事件不触发。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明widthnumber是

图片的宽。

单位：px

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

heightnumber是

图片的高。

单位：px

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

componentWidthnumber是

组件的宽。

单位：px

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

componentHeightnumber是

组件的高。

单位：px

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

loadingStatusnumber是

图片加载成功的状态值。

**说明：**

返回的状态值为0时，表示图片数据加载成功。返回的状态值为1时，表示图片解码成功。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

contentWidth10+number是

图片实际绘制的宽度。

单位：px

**说明：**

仅在loadingStatus返回1时有效。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

contentHeight10+number是

图片实际绘制的高度。

单位：px

**说明：**

仅在loadingStatus返回1时有效。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

contentOffsetX10+number是

实际绘制内容相对于组件自身的x轴偏移。

单位：px

**说明：**

仅在loadingStatus返回1时有效。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

contentOffsetY10+number是

实际绘制内容相对于组件自身的y轴偏移。

单位：px

**说明：**

仅在loadingStatus返回1时有效。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

[]()[]()

#### onError9+

onError(callback: ImageErrorCallback)

图片加载异常时触发该回调。

当组件的参数类型为[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)时该事件不触发。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明callback[ImageErrorCallback](#ZH-CN_TOPIC_0000002497444922__imageerrorcallback9)是

图片加载异常时触发的回调。

**说明：**

建议开发者使用此回调，可快速确认图片加载失败时的具体原因，参见[ImageError](#ZH-CN_TOPIC_0000002497444922__imageerror9)的错误信息详细介绍。

[]()[]()

#### onFinish

onFinish(event: () => void)

当加载的源文件为带动效的SVG格式图片时，SVG动效播放完成时会触发这个回调。如果动效为无限循环动效，则不会触发这个回调。

仅支持SVG格式的图片。当组件的参数类型为[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)时该事件不触发。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event() => void是当加载的源文件为带动效的SVG格式图片时，SVG动效播放完成时会触发这个回调。如果动效为无限循环动效，则不会触发这个回调。[]()[]()

#### ImageErrorCallback9+

type ImageErrorCallback = (error: ImageError) => void

图片加载异常时触发此回调。

当组件的参数类型为[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)时该事件不触发。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明error[ImageError](#ZH-CN_TOPIC_0000002497444922__imageerror9)是图片加载异常时触发回调的返回对象。[]()[]()

#### ImageError9+

图片加载异常时触发回调的返回对象。

当组件的参数类型为[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)时该事件不触发。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明componentWidthnumber否否

组件的宽。

单位：px

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

componentHeightnumber否否

组件的高。

单位：px

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

message10+string否否

报错信息。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

error20+[BusinessError<void>](#ZH-CN_TOPIC_0000002497444922__businesserror20)否是

图片加载异常返回的报错信息，其中code为错误码，message为错误信息。报错信息请参考以下错误信息的详细介绍。

默认值：{ code : -1, message : "" }

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

[]()[]()

#### BusinessError20+

type BusinessError<T = void> = BusinessError<T>

图片加载异常返回的错误信息。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明[BusinessError<T>](../../modules/ohos/@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__businesserror)图片加载异常返回的错误信息。

以下是错误信息的详细介绍：ImageError的error属性为错误信息对象，其中code为错误码，message为错误信息。

错误码ID错误信息错误信息发生阶段图片加载类型101000unknown source type.数据加载未知类型102010sync http task of uri cancelled.数据加载网络文件102011sync http task of uri failed.数据加载网络文件102012async http task of uri cancelled.数据加载网络文件102013async http task of uri failed.数据加载网络文件102030wrong code format.数据加载base64字符串文件102031decode base64 image failed.数据加载base64字符串文件102050path is too long.数据加载沙箱文件102051read data failed.数据加载沙箱文件102070get image data by name failed.数据加载资源文件102071get image data by id failed.数据加载资源文件102072uri is invalid.数据加载资源文件102090uri is invalid.数据加载包内文件102091get asset failed.数据加载包内文件102110open file failed.数据加载媒体库文件102111get file stat failed.数据加载媒体库文件102112read file failed.数据加载媒体库文件102130decoded data is empty.数据加载媒体库缩略图文件102131load shared memory image data timeout.数据加载共享内存文件103100make svg dom failed.数据加载矢量图文件103200image data size is invalid.数据加载位图文件111000image source create failed.数据解码位图文件111001pixelmap create failed.数据解码位图文件[]()[]()

#### 示例

[]()[]()

#### 示例1（加载基本类型图片）

该示例通过传入[Resource](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)资源，加载png、gif、svg和jpg等基本类型的图片。

```ets
@Entry
@Component
struct ImageExample1 {
  build() {
    Column() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
        Row() {
          // 加载png格式图片
          // $r('app.media.ic_camera_master_ai_leaf')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.ic_camera_master_ai_leaf'))
            .width(110).height(110).margin(15)
            .overlay('png', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
          // 加载gif格式图片
          // $r('app.media.loading')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.loading'))
            .width(110).height(110).margin(15)
            .overlay('gif', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
        }
        Row() {
          // 加载svg格式图片
          // $r('app.media.ic_camera_master_ai_clouded')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.ic_camera_master_ai_clouded'))
            .width(110).height(110).margin(15)
            .overlay('svg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
          // 加载jpg格式图片
          // $r('app.media.ic_public_favor_filled')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.ic_public_favor_filled'))
            .width(110).height(110).margin(15)
            .overlay('jpg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
        }
      }
    }.height(320).width(360).padding({ right: 10, top: 10 })
  }
}
```

[]()[]()

#### 示例2（下载与显示静态网络图片）

加载网络图片时，默认网络超时是5分钟，建议使用alt配置加载时的占位图。使用[HTTP](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/http-request)工具包发送网络请求，接着将返回的数据解码为Image组件中的PixelMap，加载gif到PixelMap时，gif显示为静态图。图片开发可参考[图片处理](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-overview)。

使用网络图片时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions)。

```ets
import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct ImageExample2 {
  @State pixelMapImg: PixelMap | undefined = undefined;

  aboutToAppear() {
    this.requestImageUrl('https://www.example.com/xxx.png'); // 请填写一个具体的网络图片地址
  }

  requestImageUrl(url: string) {
    http.createHttp().request(url, (error: BusinessError, data: http.HttpResponse) => {
      if (error) {
        console.error(`request image failed: url: ${url}, code: ${error.code}, message: ${error.message}`);
      } else {
        let imgData: ArrayBuffer = data.result as ArrayBuffer;
        console.info(`request image success, size: ${imgData.byteLength}`);
        let imgSource: image.ImageSource = image.createImageSource(imgData);
        class sizeTmp {
          height: number = 100;
          width: number = 100;
        }
        let options: Record<string, number | boolean | sizeTmp> = {
          'alphaType': 0,
          'editable': false,
          'pixelFormat': 3,
          'scaleMode': 1,
          'size': { height: 100, width: 100 }
        }
        imgSource.createPixelMap(options).then((pixelMap: PixelMap) => {
          console.error('image createPixelMap success');
          this.pixelMapImg = pixelMap;
          imgSource.release();
        }).catch(() => {
          imgSource.release();
        })
      }
    })
  }

  build() {
    Column() {
      Image(this.pixelMapImg)
        // $r('app.media.img')需要替换为开发者所需的图像资源文件。
        .alt($r('app.media.img'))
        .objectFit(ImageFit.None)
        .width('100%')
        .height('100%')
    }
  }
}
```

[]()[]()

#### 示例3（下载与显示网络gif图片）

该示例使用[cacheDownload.download](../../modules/ohos/@ohos.request.cacheDownload (缓存下载).md#ZH-CN_TOPIC_0000002497445530__cachedownloaddownload)接口下载网络gif图片。

使用网络图片时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions)。

```ets
import { cacheDownload } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State src: string = 'https://www.example.com/xxx.gif'; // 请填写一个具体的网络图片地址。

  async aboutToAppear(): Promise<void> {
    // 提供缓存下载任务的配置选项。
    let options: cacheDownload.CacheDownloadOptions = {};
    try {
      // 进行缓存下载，资源若下载成功会被缓存到应用内存或应用沙箱目录的特定文件中。
      cacheDownload.download(this.src, options);
      console.info(`success to download the resource. `);
    } catch (err) {
      console.error(`Failed to download the resource: code: ${err.code}, message: ${err.message}`);
    }
  }

  build() {
    Column() {
      // 若src指定的是网络图片且已成功下载并缓存，则本次显示无需重复下载。
      Image(this.src)
        .width(100)
        .height(100)
        .objectFit(ImageFit.Cover)
        .borderWidth(1)
    }
    .height('100%')
    .width('100%')
  }
}
```

[]()[]()

#### 示例4（为图片添加事件）

该示例为图片添加[onClick](../misc/点击事件.md#ZH-CN_TOPIC_0000002529284807__onclick)和[onFinish](#ZH-CN_TOPIC_0000002497444922__onfinish)事件。

```ets
@Entry
@Component
struct ImageExample3 {
  // $r('app.media.earth')需要替换为开发者所需的图像资源文件。
  private imageOne: Resource = $r('app.media.earth');
  // $r('app.media.star')需要替换为开发者所需的图像资源文件。
  private imageTwo: Resource = $r('app.media.star');
  // $r('app.media.moveStar')需要替换为开发者所需的图像资源文件。
  private imageThree: Resource = $r('app.media.moveStar');
  @State src: Resource = this.imageOne;
  @State src2: Resource = this.imageThree;
  build(){
    Column(){
      // 为图片添加点击事件，点击完成后加载特定图片
      Image(this.src)
        .width(100)
        .height(100)
        .onClick(() => {
          this.src = this.imageTwo;
        })

      // 当加载图片为SVG格式时
      Image(this.src2)
        .width(100)
        .height(100)
        .onFinish(() => {
          // SVG动效播放完成时加载另一张图片
          this.src2 = this.imageOne;
        })
    }.width('100%').height('100%')
  }
}
```

[]()[]()

#### 示例5（开启图像AI分析）

该示例使用[enableAnalyzer](#ZH-CN_TOPIC_0000002497444922__enableanalyzer11)接口开启图像AI分析。

```ets
import { image } from '@kit.ImageKit'

@Entry
@Component
struct ImageExample4 {
  @State imagePixelMap: image.PixelMap | undefined = undefined
  private aiController: ImageAnalyzerController = new ImageAnalyzerController()
  private options: ImageAIOptions = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT],
    aiController: this.aiController
  }

  async aboutToAppear() {
    this.imagePixelMap = await this.getPixmapFromMedia($r('app.media.img'))
  }

  build() {
    Column() {
      Image(this.imagePixelMap, this.options)
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
        .width(200)
        .height(300)
        .margin({left: 10})
      Button('getTypes')
        .onClick(() => {
          this.aiController.getImageAnalyzerSupportTypes()
        })
    }
  }
  private async getPixmapFromMedia(resource: Resource) {
    let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent({
      bundleName: resource.bundleName,
      moduleName: resource.moduleName,
      id: resource.id
    })
    let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength))
    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
      desiredPixelFormat: image.PixelMapFormat.RGBA_8888
    })
    await imageSource.release()
    return createPixelMap
  }
}
```

[]()[]()

#### 示例6（通过slice拉伸图片）

该示例通过[resizable](#ZH-CN_TOPIC_0000002497444922__resizable11)属性的slice选项，调整不同方向对图片进行拉伸。

```ets
@Entry
@Component
struct Index {
  @State top: number = 10;
  @State bottom: number = 10;
  @State left: number = 10;
  @State right: number = 10;

  build() {
    Column({ space: 5 }) {
      // 原图效果
      // $r('app.media.landscape')需要替换为开发者所需的图像资源文件。
      Image($r("app.media.landscape"))
        .width(200).height(200)
        .border({ width: 2, color: Color.Pink })
        .objectFit(ImageFit.Contain)

      // 图像拉伸效果，设置resizable属性，对图片不同方向进行拉伸
      // $r('app.media.landscape')需要替换为开发者所需的图像资源文件。
      Image($r("app.media.landscape"))
        .resizable({
          slice: {
            //传入数字时默认为vp单位，但在不同设备上vp单位会被解析成不同大小的px单位，可以根据需要选择传入的单位
            left: `${this.left}px`,
            right: `${this.right}px`,
            top: `${this.top}px`,
            bottom: `${this.bottom}px`
          }
        })
        .width(200)
        .height(200)
        .border({ width: 2, color: Color.Pink })
        .objectFit(ImageFit.Contain)

      Row() {
        Button("add top to " + this.top).fontSize(10)
          .onClick(() => {
            this.top += 10;
          })
        Button("add bottom to " + this.bottom).fontSize(10)
          .onClick(() => {
            this.bottom += 10;
          })
      }

      Row() {
        Button("add left to " + this.left).fontSize(10)
          .onClick(() => {
            this.left += 10;
          })
        Button("add right to " + this.right).fontSize(10)
          .onClick(() => {
            this.right += 10;
          })
      }

    }
    .justifyContent(FlexAlign.Start).width('100%').height('100%')
  }
}
```

[]()[]()

#### 示例7（通过lattice拉伸图片）

该示例使用[resizable](#ZH-CN_TOPIC_0000002497444922__resizable11)属性的lattice选项，使用矩形网格对象对图片进行拉伸。

```ets
import { drawing } from '@kit.ArkGraphics2D';

@Entry
@Component
struct drawingLatticeTest {
  private xDivs: Array<number> = [1, 2, 200];
  private yDivs: Array<number> = [1, 2, 200];
  private fXCount: number = 3;
  private fYCount: number = 3;
  private drawingLatticeFirst: DrawingLattice =
    drawing.Lattice.createImageLattice(this.xDivs, this.yDivs, this.fXCount, this.fYCount);

  build() {
    Scroll() {
      Column({ space: 10 }) {
        Text('Original Image').fontSize(20).fontWeight(700)
        Column({ space: 10 }) {
          // $r('app.media.mountain')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.mountain'))
            .width(260).height(260)
        }.width('100%')

        Text('Resize by lattice').fontSize(20).fontWeight(700)
        Column({ space: 10 }) {
          // $r('app.media.mountain')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.mountain'))
            .objectRepeat(ImageRepeat.X)
            .width(260)
            .height(260)
            .resizable({
              lattice: this.drawingLatticeFirst
            })
        }.width('100%')
      }.width('100%')
    }
  }
}
```

[]()[]()

#### 示例8（播放PixelMap数组动画）

该示例通过[AnimatedDrawableDescriptor](../../modules/ohos/@ohos.arkui.drawableDescriptor (DrawableDescriptor).md#ZH-CN_TOPIC_0000002497604770__animateddrawabledescriptor12)对象播放PixelMap数组动画。

```ets
import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct ImageExample {
  pixelMaps: PixelMap[] = [];
  @State options: AnimationOptions = { iterations: 1 };
  @State animated: AnimatedDrawableDescriptor | undefined = undefined;

  async aboutToAppear() {
    this.pixelMaps = await this.getPixelMaps();
    this.animated = new AnimatedDrawableDescriptor(this.pixelMaps, this.options);
  }

  build() {
    Column() {
      Row() {
        Image(this.animated)
          .width('500px').height('500px')
          .onFinish(() => {
            console.info('finish');
          })
      }.height('50%')

      Row() {
        Button('once').width(100).padding(5).onClick(() => {
          this.options = { iterations: 1 };
          this.animated = new AnimatedDrawableDescriptor(this.pixelMaps, this.options);
        }).margin(5)
        Button('infinite').width(100).padding(5).onClick(() => {
          this.options = { iterations: -1 };
          this.animated = new AnimatedDrawableDescriptor(this.pixelMaps, this.options);
        }).margin(5)
      }
    }.width('50%')
  }

  private async getPixmapListFromMedia(resource: Resource) {
    let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent(resource.id);
    let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
    let createPixelMap: image.PixelMap[] = await imageSource.createPixelMapList({
      desiredPixelFormat: image.PixelMapFormat.RGBA_8888
    });
    await imageSource.release();
    return createPixelMap;
  }

  private async getPixmapFromMedia(resource: Resource) {
    let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent(resource.id);
    let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
      desiredPixelFormat: image.PixelMapFormat.RGBA_8888
    });
    await imageSource.release();
    return createPixelMap;
  }

  private async getPixelMaps() {
    // $r('app.media.mountain')需要替换为开发者所需的图像资源文件。
    let myPixelMaps: PixelMap[] = await this.getPixmapListFromMedia($r('app.media.mountain')); //添加图片
    // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
    myPixelMaps.push(await this.getPixmapFromMedia($r('app.media.sky')));
    // $r('app.media.clouds')需要替换为开发者所需的图像资源文件。
    myPixelMaps.push(await this.getPixmapFromMedia($r('app.media.clouds')));
    // $r('app.media.landscape')需要替换为开发者所需的图像资源文件。
    myPixelMaps.push(await this.getPixmapFromMedia($r('app.media.landscape')));
    return myPixelMaps;
  }
}
```

[]()[]()

#### 示例9（为图像设置颜色滤镜效果）

该示例通过[colorFilter](#ZH-CN_TOPIC_0000002497444922__colorfilter9)属性实现了给图像设置颜色滤镜效果。

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';

@Entry
@Component
struct ImageExample3 {
  // $r('app.media.1')需要替换为开发者所需的图像资源文件。
  private imageOne: Resource = $r('app.media.1');
  // $r('app.media.2')需要替换为开发者所需的图像资源文件。
  private imageTwo: Resource = $r('app.media.2');
  @State src: Resource = this.imageOne;
  @State src2: Resource = this.imageTwo;
  private colorFilterMatrix: number[] = [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0];
  private color: common2D.Color = {
    alpha: 255,
    red: 255,
    green: 0,
    blue: 0
  };
  @State drawingColorFilterFirst: ColorFilter | undefined = undefined;
  @State drawingColorFilterSecond: ColorFilter | undefined = undefined;
  @State drawingColorFilterThird: ColorFilter | undefined = undefined;

  build() {
    Column() {
      Image(this.src)
        .width(100)
        .height(100)
        .colorFilter(this.drawingColorFilterFirst)
        .onClick(()=>{
          this.drawingColorFilterFirst =
            drawing.ColorFilter.createBlendModeColorFilter(this.color, drawing.BlendMode.SRC_IN);
        })

      Image(this.src2)
        .width(100)
        .height(100)
        .colorFilter(this.drawingColorFilterSecond)
        .onClick(()=>{
          this.drawingColorFilterSecond = new ColorFilter(this.colorFilterMatrix);
        })

      //当加载图片为svg格式时
      // $r('app.media.test_self')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.test_self'))
        .width(110)
        .height(110)
        .margin(15)
        .colorFilter(this.drawingColorFilterThird)
        .onClick(()=>{
          this.drawingColorFilterThird =
            drawing.ColorFilter.createBlendModeColorFilter(this.color, drawing.BlendMode.SRC_IN);
        })
    }
  }
}
```

[]()[]()

#### 示例10（为图像设置填充效果）

该示例通过[objectFit](#ZH-CN_TOPIC_0000002497444922__objectfit)属性为图像设置填充效果。

```ets
@Entry
@Component
struct ImageExample{
  build() {
    Column() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
        Row() {
          // 加载png格式图片
          // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.sky'))
            .width(110).height(110).margin(15)
            .overlay('png', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
            .border({ width: 2, color: Color.Pink })
            .objectFit(ImageFit.TOP_START)
          // 加载gif格式图片
          // $r('app.media.loading')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.loading'))
            .width(110).height(110).margin(15)
            .overlay('gif', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
            .border({ width: 2, color: Color.Pink })
            .objectFit(ImageFit.BOTTOM_START)
        }
        Row() {
          // 加载svg格式图片
          // $r('app.media.svg')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.svg'))
            .width(110).height(110).margin(15)
            .overlay('svg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
            .border({ width: 2, color: Color.Pink })
            .objectFit(ImageFit.TOP_END)
          // 加载jpg格式图片
          // $r('app.media.jpg')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.jpg'))
            .width(110).height(110).margin(15)
            .overlay('jpg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
            .border({ width: 2, color: Color.Pink })
            .objectFit(ImageFit.CENTER)
        }
      }
    }.height(320).width(360).padding({ right: 10, top: 10 })
  }
}
```

[]()[]()

#### 示例11（切换显示不同类型图片）

该示例展示了[ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)类型与[ImageContent](#ZH-CN_TOPIC_0000002497444922__imagecontent12)类型作为数据源的显示图片效果。

```ets
@Entry
@Component
struct ImageContentExample {
  @State imageSrcIndex: number = 0;
  // $r('app.media.app_icon')需要替换为开发者所需的图像资源文件。
  @State imageSrcList: (ResourceStr | ImageContent)[] = [$r('app.media.app_icon'), ImageContent.EMPTY];

  build() {
    Column({ space: 10 }) {
      Image(this.imageSrcList[this.imageSrcIndex])
        .width(100)
        .height(100)
      Button('点击切换Image的src', { type: ButtonType.Capsule, stateEffect: false })
        .height(50)
        .onClick(() => {
          this.imageSrcIndex = (this.imageSrcIndex + 1) % this.imageSrcList.length;
        })
    }.width('100%')
    .padding(20)
  }
}
```

[]()[]()

#### 示例12（配置隐私隐藏）

该示例通过[privacySensitive](#ZH-CN_TOPIC_0000002497444922__privacysensitive12)属性展示了如何配置隐私隐藏，效果展示需要卡片框架支持。

```ets
@Entry
@Component
struct ImageExample {
  build() {
    Column({ space: 10 }) {
      // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.startIcon'))
        .width(50)
        .height(50)
        .margin({top :30})
        .privacySensitive(true)
    }
    .alignItems(HorizontalAlign.Center)
    .width('100%')
  }
}
```

[]()[]()

#### 示例13（为图片设置扫光效果）

该示例通过[linearGradient](DataPanel.md#ZH-CN_TOPIC_0000002497604906__lineargradient10)接口和[animateTo()](../misc/显式动画 (animateTo).md)接口实现了给图片设置扫光效果。

```ets
import { curves } from '@kit.ArkUI';

@Entry
@Component
struct ImageExample11 {
  private curve = curves.cubicBezierCurve(0.33, 0, 0.67, 1);
  @State moveImg: string[] = ['imageScanEffect'];
  @State moveImgVisible: Visibility = Visibility.Visible;
  @State durationTime: number = 1500;
  @State iterationsTimes: number = -1;
  @State private opacityValue: number = 0.5;
  @State imageWidth: number = 450;
  @State visible: Visibility = Visibility.Hidden;
  @State stackBackgroundColor: string = '#E1E4E9';
  @State linePositionX: number = 0 - this.imageWidth;
  @State linePositionY: number = 0;
  @State imgResource: Resource | undefined = undefined;

  startupAnimate() {
    this.moveImg.pop();
    this.moveImg.push('imageScanEffect');
    setTimeout(() => {
      // $r('app.media.img')需要替换为开发者所需的图像资源文件。
      this.imgResource = $r('app.media.img');
    }, 3000);
    this.getUIContext()?.animateTo({
      duration: this.durationTime,
      curve: this.curve,
      tempo: 1,
      iterations: this.iterationsTimes,
      delay: 0
    }, () => {
      this.linePositionX = this.imageWidth;
    })
  }

  build() {
    Column() {
      Row() {
        Stack() {
          Image(this.imgResource)
            .width(this.imageWidth)
            .height(200)
            .objectFit(ImageFit.Contain)
            .visibility(this.visible)
            .onComplete(() => {
              this.visible = Visibility.Visible;
              this.moveImg.pop();
            })
            .onError(() =>{
              setTimeout(() => {
                this.visible = Visibility.Visible;
                this.moveImg.pop();
              }, 2600)
            })
          ForEach(this.moveImg, (item: string) => {
            Row()
              .width(this.imageWidth)
              .height(200)
              .visibility(this.moveImgVisible)
              .position({ x: this.linePositionX, y: this.linePositionY })
              .linearGradient({
                direction: GradientDirection.Right,
                repeating: false,
                colors: [[0xE1E4E9, 0], [0xFFFFFF, 0.75], [0xE1E4E9, 1]]
              })
              .opacity(this.opacityValue)
          })
        }
        .backgroundColor(this.visible ? this.stackBackgroundColor : undefined)
        .margin({top: 20, left: 20, right: 20})
        .borderRadius(20)
        .clip(true)
        .onAppear(() => {
          this.startupAnimate();
        })
      }
    }
  }
}
```

[]()[]()

#### 示例14（为图片添加变换效果）

该示例通过[imageMatrix](#ZH-CN_TOPIC_0000002497444922__imagematrix15)和[objectFit](#ZH-CN_TOPIC_0000002497444922__objectfit)属性，为图片添加旋转和平移的效果。

```ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity()
    .translate({ x: -400, y: -750 })
    .scale({ x: 0.5, y: 0.5 })
    .rotate({
      x: 2,
      y: 0.5,
      z: 3,
      centerX: 10,
      centerY: 10,
      angle: -10
    })

  build() {
    Row() {
      Column({ space: 50 }) {
        Column({ space: 5 }) {
          // $r('app.media.example')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.example'))
            .border({ width:2, color: Color.Black })
            .objectFit(ImageFit.Contain)
            .width(150)
            .height(150)
          Text('图片无变换')
            .fontSize('25px')
        }
        Column({ space: 5 }) {
          // $r('app.media.example')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.example'))
            .border({ width:2, color: Color.Black })
            .objectFit(ImageFit.None)
            .translate({ x: 10, y: 10 })
            .scale({ x: 0.5, y: 0.5 })
            .width(100)
            .height(100)
          Text('Image直接变换，默认显示图源左上角。')
            .fontSize('25px')
        }
        Column({ space: 5 }) {
          // $r('app.media.example')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.example'))
            .objectFit(ImageFit.MATRIX)
            .imageMatrix(this.matrix1)
            .border({ width:2, color: Color.Black })
            .width(150)
            .height(150)
          Text('通过imageMatrix变换，调整图源位置，实现最佳呈现。')
            .fontSize('25px')
        }
      }
      .width('100%')
    }
  }
}
```

[]()[]()

#### 示例15（通过sourceSize设置图片解码尺寸）

该示例通过[sourceSize](Image (ts-basic-components-image).md#ZH-CN_TOPIC_0000002497444922__sourcesize)接口自定义图片的解码尺寸。

```ets
@Entry
@Component
struct Index {
  @State borderRadiusValue: number = 10;
  build() {
    Column() {
      // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.sky'))
        .sourceSize({width:1393, height:1080})
        .height(300)
        .width(300)
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
      // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.sky'))
        .sourceSize({width:13, height:10})
        .height(300)
        .width(300)
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
    }
    .height('100%')
    .width('100%')
  }
}
```

[]()[]()

#### 示例16（通过renderMode设置图片的渲染模式）

该示例通过[renderMode](Image (ts-basic-components-image).md#ZH-CN_TOPIC_0000002497444922__rendermode)接口设置图片渲染模式为黑白模式。

```ets
@Entry
@Component
struct Index {
  @State borderRadiusValue: number = 10;
  build() {
    Column() {
      // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.sky'))
        .renderMode(ImageRenderMode.Template)
        .height(300)
        .width(300)
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
    }
    .height('100%')
    .width('100%')
  }
}
```

[]()[]()

#### 示例17（通过objectRepeat设置图片的重复样式）

该示例通过[objectRepeat](Image (ts-basic-components-image).md#ZH-CN_TOPIC_0000002497444922__objectrepeat)接口在竖直轴上重复绘制图片。

```ets
@Entry
@Component
struct Index {
  @State borderRadiusValue: number = 10;
  build() {
    Column() {
      // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.sky'))
        .objectRepeat(ImageRepeat.Y)
        .height('90%')
        .width('90%')
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
    }
    .height('100%')
    .width('100%')
  }
}
```

[]()[]()

#### 示例18（设置SVG图片的填充颜色）

该示例通过[fillColor](#ZH-CN_TOPIC_0000002497444922__fillcolor15)属性为SVG图片设置不同颜色的填充效果。

```ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('不设置fillColor')
      // $r('app.media.svgExample')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.svgExample'))
        .height(100)
        .width(100)
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
      Text('fillColor传入ColorContent.ORIGIN')
      // $r('app.media.svgExample')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.svgExample'))
        .height(100)
        .width(100)
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
        .fillColor(ColorContent.ORIGIN)
      Text('fillColor传入Color.Blue')
      // $r('app.media.svgExample')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.svgExample'))
        .height(100)
        .width(100)
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
        .fillColor(Color.Blue)
      Text('fillColor传入undefined')
      // $r('app.media.svgExample')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.svgExample'))
        .height(100)
        .width(100)
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
        .fillColor(undefined)
    }
    .height('100%')
    .width('100%')
  }
}
```

[]()[]()

#### 示例19（设置HDR图源动态提亮）

该示例通过[hdrBrightness](#ZH-CN_TOPIC_0000002497444922__hdrbrightness19)属性调整HDR图源的亮度，将hdrBrightness从0调整到1。

```ets
import { image } from '@kit.ImageKit';

const TAG = 'AceImage';

@Entry
@Component
struct Index {
  // 'img_1'需要替换为开发者所需的图像资源文件。
  @State imgUrl: string = 'img_1';
  @State bright: number = 0; // 默认亮度为0
  aboutToAppear(): void {
    // 获取资源管理器中的媒体资源
    let img = this.getUIContext().getHostContext()?.resourceManager.getMediaByNameSync(this.imgUrl);
    // 创建图片源并获取图片信息
    if (img && img.buffer) {
      let imageSource = image.createImageSource(img?.buffer.slice(0));
      let imageInfo = imageSource.getImageInfoSync();
      // 检查图片信息是否获取成功
      if (imageInfo == undefined) {
        console.error(TAG, 'Failed to obtain the image information.');
      } else {
        // 成功获取到图片信息，打印HDR状态
        console.info(TAG, 'imageInfo.isHdr:' + imageInfo.isHdr);
      }
    } else {
      console.error(TAG, 'Failed to obtain the image buffer.');
    }
  }

  build() {
    Column() {
      // $r('app.media.img_1')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.img_1')).width('50%')
        .height('auto')
        .margin({ top: 160 })
        .hdrBrightness(this.bright) // 设置图片的HDR亮度，值由bright状态控制
      Button('图片动态提亮 0->1')
        .onClick(() => {
          // 动画过渡，切换亮度值
          this.getUIContext()?.animateTo({}, () => {
            this.bright = 1.0 - this.bright;
          });
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

[]()[]()

#### 示例20（设置图片是否跟随系统语言方向）

该示例通过[matchTextDirection](#ZH-CN_TOPIC_0000002497444922__matchtextdirection)接口，设置手机语言为维语时图片是否显示镜像翻转显示效果。

```ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
        Row() {
          // 图片不跟随系统语言方向
          // $r('app.media.ocean')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.ocean'))
            .width(110).height(110).margin(15)
            .matchTextDirection(false)
        }
        Row() {
          // 图片跟随系统语言方向
          // $r('app.media.ocean')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.ocean'))
            .width(110).height(110).margin(15)
            .matchTextDirection(true)
        }
      }
    }.height(320).width(360).padding({ right: 10, top: 10 })
  }
}
```

[]()[]()

#### 示例21（设置图像内容的显示方向）

该示例通过[orientation](#ZH-CN_TOPIC_0000002497444922__orientation14)属性，设置图像内容的显示方向。

```ets
@Entry
@Component
struct OrientationExample {
  build() {
    Column() {
      Row({ space: 25 }) {
        Column() {
          Text('AUTO')
          // $r('app.media.hello')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.AUTO)
        }

        Column() {
          Text('UP')
          // $r('app.media.hello')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.UP)
        }

        Column() {
          Text('RIGHT')
          // $r('app.media.hello')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.RIGHT)
        }
      }

      Row({ space: 25 }) {
        Column() {
          Text('DOWN')
          // $r('app.media.hello')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.DOWN)
        }

        Column() {
          Text('LEFT')
          // $r('app.media.hello')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.LEFT)
        }

        Column() {
          Text('UP_MIRRORED')
          // $r('app.media.hello')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.UP_MIRRORED)
        }
      }

      Row({ space: 15 }) {
        Column() {
          Text('RIGHT_MIRRORED')
          // $r('app.media.hello')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.RIGHT_MIRRORED)
        }

        Column() {
          Text('DOWN_MIRRORED')
          // $r('app.media.hello')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.DOWN_MIRRORED)
        }

        Column() {
          Text('LEFT_MIRRORED')
          // $r('app.media.hello')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.LEFT_MIRRORED)
        }
      }
    }
  }
}
```

[]()[]()

#### 示例22（获取图片的exif信息并设置图像内容的显示方向）

该示例通过[getImageProperty](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__getimageproperty11)接口，获取图片的exif信息，再根据获取到的exif信息，通过[orientation](#ZH-CN_TOPIC_0000002497444922__orientation14)属性设置图像内容显示为正确方向。

```ets
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';

@Entry
@Component
struct Example {
  @State rotateOrientation: ImageRotateOrientation = ImageRotateOrientation.UP;
  @State pixelMap: image.PixelMap | undefined = undefined;
  @State text1: string = 'The exif orientation is ';
  @State text2: string = 'Set orientation to ';

  // 根据获取到的EXIF方向信息，转换ImageRotateOrientation，使图片显示为正确的方向。
  getOrientation(orientation: string): ImageRotateOrientation {
    if (orientation == 'Top-right') {
      this.text2 = this.text2 + 'UP_MIRRORED';
      return ImageRotateOrientation.UP_MIRRORED;
    } else if (orientation == 'Bottom-right') {
      this.text2 = this.text2 + 'DOWN';
      return ImageRotateOrientation.DOWN;
    } else if (orientation == 'Bottom-left') {
      this.text2 = this.text2 + 'DOWN_MIRRORED';
      return ImageRotateOrientation.DOWN_MIRRORED;
    } else if (orientation == 'Left-top') {
      this.text2 = this.text2 + 'LEFT_MIRRORED';
      return ImageRotateOrientation.LEFT_MIRRORED;
    } else if (orientation == 'Right-top') {
      this.text2 = this.text2 + 'RIGHT';
      return ImageRotateOrientation.RIGHT;
    } else if (orientation == 'Right-bottom') {
      this.text2 = this.text2 + 'RIGHT_MIRRORED';
      return ImageRotateOrientation.RIGHT_MIRRORED;
    } else if (orientation == 'Left-bottom') {
      this.text2 = this.text2 + 'LEFT';
      return ImageRotateOrientation.LEFT;
    } else if (orientation == 'Top-left') {
      this.text2 = this.text2 + 'UP';
      return ImageRotateOrientation.UP;
    } else {
      this.text2 = this.text2 + 'UP';
      return ImageRotateOrientation.UP;
    }
  }

  async getFileBuffer(context: Context): Promise<ArrayBuffer | undefined> {
    try {
      const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
      // 传入带有EXIF信息的资源文件，获取资源文件内容，返回Uint8Array。
      // 'hello.jpg'需要替换为开发者所需的图像资源文件。
      const fileData: Uint8Array = await resourceMgr.getRawFileContent('hello.jpg');
      console.info('Successfully get RawFileContent');
      // 转为ArrayBuffer并返回。
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    } catch (error) {
      console.error('Failed to get RawFileContent');
      return undefined;
    }
  }

  aboutToAppear() {
    let context = this.getUIContext().getHostContext();
    if (!context) {
      return;
    }
    this.getFileBuffer(context).then((buf: ArrayBuffer | undefined) => {
      let imageSource = image.createImageSource(buf);
      if (!imageSource) {
        return;
      }
      // 从图像源中读取图片的EXIF方向信息。
      imageSource.getImageProperty(image.PropertyKey.ORIENTATION).then((orientation) => {
        this.rotateOrientation = this.getOrientation(orientation);
        this.text1 = this.text1 + orientation;
        let options: image.DecodingOptions = {
          'editable': true,
          'desiredPixelFormat': image.PixelMapFormat.RGBA_8888,
        }
        imageSource.createPixelMap(options).then((pixelMap: image.PixelMap) => {
          this.pixelMap = pixelMap;
          imageSource.release();
        });
      }).catch(() => {
        imageSource.release();
      });
    })
  }

  build() {
    Column({ space: 40 }) {
      Column({ space: 10 }) {
        Text('before').fontSize(20).fontWeight(700)
        // 'hello.jpg'需要替换为开发者所需的图像资源文件。
        Image($rawfile('hello.jpg'))
          .width(100)
          .height(100)
        Text(this.text1)
      }

      Column({ space: 10 }) {
        Text('after').fontSize(20).fontWeight(700)
        Image(this.pixelMap)
          .width(100)
          .height(100)
          .orientation(this.rotateOrientation)
        Text(this.text2)
      }
    }
    .height('80%')
    .width('100%')
  }
}
```

[]()[]()

#### 示例23（动态切换SVG图片的填充颜色）

通过按钮切换不同色域下的颜色值，动态改变SVG图片的填充颜色效果，以展示[ColorMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)类型的使用方式和显示差异。

```ets
import { ColorMetrics } from '@kit.ArkUI';
@Entry
@Component
struct fillColorMetricsDemo {
  @State p3Red: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 0.631, 0.0392, 0.1294);
  @State sRGBRed: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.SRGB, 0.631, 0.0392, 0.1294);
  @State p3Green: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 0.09, 0.662 ,0.552);
  @State sRGBGreen: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.SRGB, 0.09, 0.662 ,0.552);
  @State p3Blue: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 0, 0.290 ,0.686);
  @State sRGBBlue: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.SRGB, 0, 0.290 ,0.686);
  @State colorArray: (Color|undefined|ColorMetrics|ColorContent)[] = [
    this.p3Red, this.sRGBRed, this.p3Green, this.sRGBGreen, this.p3Blue,
    this.sRGBBlue, ColorContent.ORIGIN, Color.Gray, undefined
  ]
  @State colorArrayStr: string[] = [
    "P3 Red", "SRGB Red", "P3 Green", "SRGB Green",
    "P3 Blue", "SRGB Blue", "ORIGIN", "Gray", "undefined"
  ]
  @State arrayIdx: number = 0
  build() {
    Column() {
      Text("FillColor is " + this.colorArrayStr[this.arrayIdx])
      // $r('app.media.svgExample')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.svgExample'))
        .width(110).height(110).margin(15)
        .fillColor(this.colorArray[this.arrayIdx])
      Button("ChangeFillColor")
        .onClick(()=>{
          this.arrayIdx = (this.arrayIdx + 1) % this.colorArray.length
        })
      Blank().height(30).width('100%')
      Text("FillColor is SRGB Red")
      // $r('app.media.svgExample')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.svgExample'))
        .width(110).height(110).margin(15)
        .fillColor(this.sRGBRed)
      Blank().height(30).width('100%')
      Text("FillColor is SRGB Green")
      // $r('app.media.svgExample')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.svgExample'))
        .width(110).height(110).margin(15)
        .fillColor(this.sRGBGreen)
      Blank().height(30).width('100%')
      Text("FillColor is SRGB Blue")
      // $r('app.media.svgExample')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.svgExample'))
        .width(110).height(110).margin(15)
        .fillColor(this.sRGBBlue)
    }
  }
}
```

[]()[]()

#### 示例24（使用应用沙箱路径显示图片）

在当前应用的haps/entry/files目录下预置一张名为cloud.png的图片，随后使用应用沙箱路径显示该图片。

```ets
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
  private getSandBoxUri(): string {
    let context = this.getUIContext().getHostContext();
    if (!context) {
      return '';
    }
    // /data/storage/el2/base/haps/entry/files/cloud.png
    // 从应用沙箱中的文件路径获取URI
    // '/cloud.png'需要替换为开发者所需的图像资源文件。
    return fileUri.getUriFromPath(context.filesDir + '/cloud.png');
  }

  build() {
    Column() {
      Image(this.getSandBoxUri())
        .width(150)
        .height(150)
    }
    .height('100%')
    .width('100%')
  }
}
```

[]()[]()

#### 示例25（使用相对路径显示图片）

在工程pages目录同级位置创建common目录，在common目录下预置一张名为cloud1.png的图片，随后使用相对路径显示该图片。

```ets
@Entry
@Component
struct Index {
  build() {
    Column({ space: 10 }) {
      Image('common/cloud1.png')
        .width(100)
        .height(100)
    }
    .height('100%')
    .width('100%')
  }
}
```

[]()[]()

#### 示例26（使用supportSvg2属性时，SVG图片的显示效果）

该示例通过设置[supportSvg2](#ZH-CN_TOPIC_0000002497444922__supportsvg221)属性，使SVG标签解析能力增强功能生效。

```ets
@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Text('supportSvg2参数设置为true')
        // $rawfile('image.svg')需要替换为开发者所需的图像资源文件。
        Image($rawfile('image.svg'))
          .width(200)
          .height(200)
          .border({ width: 2, color: 'red' })
          .supportSvg2(true)
          .margin({ bottom: 30 })
        Text('supportSvg2参数设置为false（默认值）')
        // $rawfile('image.svg')需要替换为开发者所需的图像资源文件。
        Image($rawfile('image.svg'))
          .width(200)
          .height(200)
          .border({ width: 2, color: 'red' })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

[]()[]()

#### 示例27（使用ContentTransition属性实现图片淡入淡出切换效果）

从API version 21开始，该示例演示了在点击图片切换图源时，通过[contentTransition](#ZH-CN_TOPIC_0000002497444922__contenttransition21)属性实现淡入淡出效果，完成图片的平滑过渡。

```ets
@Entry
@Component
struct ImageExample {
  // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
  @State imageResource: Resource = $r('app.media.icon');

  build() {
    Row() {
      Column() {
        Image(this.imageResource)
          .width(200)
          .height(200)
          // 启用淡入淡出过渡效果。
          .contentTransition(ContentTransitionEffect.OPACITY)
          .onClick(() => {
            // $r('app.media.cloud1')需要替换为开发者所需的图像资源文件。
            this.imageResource = $r('app.media.cloud1')
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

[]()[]()

#### 示例28（使用alt属性实现设置加载失败中图片和加载失败时图片）

该示例演示了在图片加载过程中和加载失败时，通过设置[alt](#ZH-CN_TOPIC_0000002497444922__alt22)属性实现图片加载过程中和图片加载失败时显示指定图片。

```ets
@Entry
@Component
struct ImageExample {
  build() {
      Column() {
      Text('同时设置placeholder属性和error属性')
      // 设置一个错误网址来触发alt的placeholder属性和error属性。
      Image("https://www.example.com/xxx.png")
      // $r('app.media.startIcon')和$r('app.media.example')需要替换为开发者所需的图像资源文件。
        .alt({ placeholder: $r('app.media.startIcon'), error: $r('app.media.example') })
        .width(100)
        .height(100)
        .margin(20)
      Text('只设置placeholder属性')
      Image("https://www.example.com/xxx.png")
        .alt({ placeholder: $r('app.media.startIcon')})
        .width(100)
        .height(100)
        .margin(20)
      Text('只设置error属性')
      Image("https://www.example.com/xxx.png")
        .alt({error: $r('app.media.example')})
        .width(100)
        .height(100)
        .margin(20)
      }
    .width('100%')
    .height('100%')
  }
}
```