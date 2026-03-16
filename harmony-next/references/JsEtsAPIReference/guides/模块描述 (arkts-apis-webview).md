[]()[]()

# 模块描述

@ohos.web.webview提供Web控制能力，[Web](../topics/misc/组件描述.md)组件提供网页显示的能力。

元服务中使用ArkWeb的说明，请参考[https://developer.huawei.com/consumer/cn/doc/atomic-guides/atomicserviceweb-guidelines](https://developer.huawei.com/consumer/cn/doc/atomic-guides/atomicserviceweb-guidelines)

-

本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

-

静态方法必须在用户界面（UI）线程上使用。

该模块提供以下Web控制相关的常用功能：

- [AdsBlockManager](../types/classes/Class (AdsBlockManager).md)：广告过滤配置。
- [BackForwardCacheOptions](../types/classes/Class (BackForwardCacheOptions).md)：前进后退缓存配置。
- [BackForwardCacheSupportedFeatures](../types/classes/Class (BackForwardCacheSupportedFeatures).md)：前进后退缓存特性配置。
- [GeolocationPermissions](../types/classes/Class (GeolocationPermissions).md)：地理位置权限配置。
- [JsMessageExt](../types/classes/Class (JsMessageExt).md)：执行JavaScript脚本的结果。
- [MediaSourceInfo](../types/classes/Class (MediaSourceInfo).md)：媒体源信息配置。
- [NativeMediaPlayerSurfaceInfo](../types/classes/Class (NativeMediaPlayerSurfaceInfo).md)：应用接管媒体播放时渲染信息。
- [PdfData](../types/classes/Class (PdfData).md)：生成的PDF输出数据。
- [ProxyConfig](../types/classes/Class (ProxyConfig).md)：网络代理配置。
- [ProxyController](../types/classes/Class (ProxyController).md)：网络代理控制器。
- [WebviewController](../types/classes/Class (WebviewController).md)：Web组件控制器。
- [WebCookieManager](../types/classes/Class (WebCookieManager).md)：Cookie管理。
- [WebDataBase](../types/classes/Class (WebDataBase).md)：数据库管理。
- [WebDownloadDelegate](../types/classes/Class (WebDownloadDelegate).md)：下载任务状态事件。
- [WebDownloadItem](../types/classes/Class (WebDownloadItem).md)：下载任务。
- [WebDownloadManager](../types/classes/Class (WebDownloadManager).md)：下载任务管理。
- [WebHttpBodyStream](../types/classes/Class (WebHttpBodyStream).md)：HTTP请求体。
- [WebMessageExt](../types/classes/Class (WebMessageExt).md)：前端与应用通信数据对象。
- [WebResourceHandler](../types/classes/Class (WebResourceHandler).md)：资源加载控制。
- [WebSchemeHandler](../types/classes/Class (WebSchemeHandler).md)：指定Scheme的请求拦截器。
- [WebSchemeHandlerRequest](../types/classes/Class (WebSchemeHandlerRequest).md)：通过拦截器拦截到的请求。
- [WebSchemeHandlerResponse](../types/classes/Class (WebSchemeHandlerResponse).md)：为拦截到的请求创建自定义响应。
- [WebStorage](../types/classes/Class (WebStorage).md)：Web组件存储操作接口。
- [BackForwardList](../types/interfaces/Interface (BackForwardList).md)：历史信息列表。
- [NativeMediaPlayerBridge](../types/interfaces/Interface (NativeMediaPlayerBridge).md)：托管网页媒体播放器桥接接口。
- [NativeMediaPlayerHandler](../types/interfaces/Interface (NativeMediaPlayerHandler).md)：托管网页媒体播放器的事件接口。
- [WebMessagePort](../types/interfaces/Interface (WebMessagePort).md)：网页前端与应用的消息端口。

[]()[]()

#### 需要权限

访问在线网页时需添加网络权限：ohos.permission.INTERNET，具体申请方式请参考[声明权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions)。

[]()[]()

#### 导入模块

```ets
import { webview } from '@kit.ArkWeb';
```

**系统能力：** SystemCapability.Web.Webview.Core