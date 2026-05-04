# 使用Picker选择媒体库资源

本文根据华为开发者官网 `photoaccesshelper-photoviewpicker` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-photoviewpicker>
更新时间：2026-04-30 02:41:24

## 指定URI读取文件数据
待界面从图库返回后，再通过一个类似按钮的组件去调用其他函数，使用fileIo.openSync接口，通过媒体文件uri打开这个文件得到fd。这里需要注意接口权限参数是fileIo.OpenMode.READ_ONLY。
try { const file = fileIo.openSync(uri, fileIo.OpenMode.READ_ONLY); console.info('file fd: ' + file.fd); return { fd: file.fd, file: file }; } catch (error) { console.error('openSync failed with err: ' + error); return null; }
通过fd使用fileIo.readSync接口读取这个文件内的数据，读取完成后关闭fd。
try { const buffer = new ArrayBuffer(bufferSize); const readLen = fileIo.readSync(fileObj.fd, buffer); console.info('readSync data to file succeed and buffer size is:' + readLen); return { data: buffer, length: readLen }; } catch (error) { console.error('readSync failed with err: ' + error); return null; }

## 指定URI获取图片或视频资源
媒体库支持Picker选择媒体文件URI后，根据指定URI获取图片或视频资源，下面以查询指定URI为'file://media/Photo/1/IMG_datetime_0001/displayName.jpg'为例。
定义媒体资源处理器MediaAssetDataHandler，系统在资源准备就绪时向应用回调onDataPrepared。
export class MediaAssetDataHandler implements photoAccessHelper.MediaAssetDataHandler<ArrayBuffer> { private callback?: MediaDataHandlerCallback; constructor(callback?: MediaDataHandlerCallback) { this.callback = callback; } // 使用箭头函数确保this引用不会丢失 onDataPrepared = (data: ArrayBuffer) => { if (data === undefined) { console.error('Error occurred when preparing data'); return; } console.info('on image data prepared'); // 现在this始终指向MediaAssetDataHandler实例 if (this.callback) { this.callback(data); } }; }
使用getAssets接口获取要访问的资产，并通过requestImageData获取对应资源。
出于对用户隐私安全的保护，对媒体资源EXIF中的地理位置和拍摄参数信息做了去隐私化处理。如果需要获取被去隐私化的EXIF信息，需要申请相册管理模块权限'ohos.permission.MEDIA_LOCATION'。
static async getMediaResourceByUri(uri: string, context: common.Context, callback?: MediaDataHandlerCallback) : Promise<void> { try { // 创建PhotoAccessHelper实例 const phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context); // 创建查询条件 const predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates(); predicates.equalTo(photoAccessHelper.PhotoKeys.URI, uri); // 设置查询选项 const fetchOptions: photoAccessHelper.FetchOptions = { fetchColumns: [photoAccessHelper.PhotoKeys.TITLE], predicates: predicates }; // 查询资产 const fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions); const photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject(); if (photoAsset) { console.info('getAssets photoAsset.uri : ' + photoAsset.uri); // 获取标题属性 console.info('title : ' + photoAsset.get(photoAccessHelper.PhotoKeys.TITLE)); // 设置请求选项 const requestOptions: photoAccessHelper.RequestOptions = { deliveryMode: photoAccessHelper.DeliveryMode.HIGH_QUALITY_MODE, }; // 请求图片数据 await photoAccessHelper.MediaAssetManager.requestImageData( context, photoAsset, requestOptions, new MediaAssetDataHandler(callback)); console.info('requestImageData successfully'); } else { console.error('No asset found for URI: ' + uri); } // 关闭查询结果 fetchResult.close(); } catch (err) { console.error('getMediaResourceByUri failed with err: ' + err); } }
