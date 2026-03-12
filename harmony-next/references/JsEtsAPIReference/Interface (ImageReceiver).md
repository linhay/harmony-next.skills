# Interface (ImageReceiver)

ImageReceiver类，用于获取组件surface id、接收最新的图片和读取下一张图片以及释放ImageReceiver实例。ImageReceiver作为图片的接收方和消费者，其参数属性实际上不会对接收到的图片产生影响。图片属性的配置应在发送方和生产者上进行，如相机预览流[createPreviewOutput](Interface (CameraManager).md#ZH-CN_TOPIC_0000002497445800__createpreviewoutput)。

在调用以下方法前需要先通过[image.createImageReceiver](Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagereceiver11)创建ImageReceiver实例。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002497605844__release9)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

- 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 9开始支持。

#### 导入模块

```ets
import { image } from '@kit.ImageKit';
```

#### 属性

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

名称类型只读可选说明size9+[Size](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__size)是否图片大小。该参数不会影响接收到的图片大小，实际返回大小由生产者决定，如相机。capacity9+number是否同时访问的图像数。该参数仅作为期望值，实际capacity由设备硬件决定。format9+[ImageFormat](Enums.md#ZH-CN_TOPIC_0000002529285837__imageformat9)是否图像格式，取值为[ImageFormat](Enums.md#ZH-CN_TOPIC_0000002529285837__imageformat9)常量（目前仅支持 ImageFormat:JPEG，实际返回格式由生产者决定，如相机）

#### getReceivingSurfaceId9+

getReceivingSurfaceId(callback: AsyncCallback<string>): void

用于获取一个surface id供Camera或其他组件使用。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

参数名类型必填说明callbackAsyncCallback<string>是回调函数，当获取surface id成功，err为undefined，data为获取到的surface id；否则为错误对象。

**示例:**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetReceivingSurfaceId(receiver : image.ImageReceiver) {
  receiver.getReceivingSurfaceId((err: BusinessError, id: string) => {
    if (err) {
      console.error(`Failed to get the ReceivingSurfaceId.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in getting the ReceivingSurfaceId.');
    }
  });
}
```

#### getReceivingSurfaceId9+

getReceivingSurfaceId(): Promise<string>

用于获取一个surface id供Camera或其他组件使用。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**

类型说明Promise<string>Promise对象，返回surface id。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetReceivingSurfaceId(receiver : image.ImageReceiver) {
  receiver.getReceivingSurfaceId().then((id: string) => {
    console.info('Succeeded in getting the ReceivingSurfaceId.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to get the ReceivingSurfaceId.code ${error.code},message is ${error.message}`);
  })
}
```

#### readLatestImage9+

readLatestImage(callback: AsyncCallback<Image>): void

从ImageReceiver读取最新的图片。使用callback异步回调。

此接口需要在[on](#ZH-CN_TOPIC_0000002497605844__on9)回调触发后调用，才能正常的接收到数据。且此接口返回的[Image](zh-cn_topic_0000002497445862.html)对象使用完毕后需要调用[release](Interface (Image).md#ZH-CN_TOPIC_0000002497445862__release9)方法释放，释放后才可以继续接收新的数据。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

参数名类型必填说明callbackAsyncCallback<[Image](Interface (Image).md)>是回调函数，当读取最新图片成功，err为undefined，data为获取到的最新图片；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadLatestImage(receiver : image.ImageReceiver) {
  receiver.readLatestImage((err: BusinessError, img: image.Image) => {
    if (err) {
      console.error(`Failed to read the latest Image.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in reading the latest Image.');
    }
  });
}
```

#### readLatestImage9+

readLatestImage(): Promise<Image>

从ImageReceiver读取最新的图片。使用Promise异步回调。

此接口需要在[on](#ZH-CN_TOPIC_0000002497605844__on9)回调触发后调用，才能正常的接收到数据。且此接口返回的[Image](zh-cn_topic_0000002497445862.html)对象使用完毕后需要调用[release](Interface (Image).md#ZH-CN_TOPIC_0000002497445862__release9)方法释放，释放后才可以继续接收新的数据。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**

类型说明Promise<[Image](Interface (Image).md)>Promise对象，返回最新图片。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadLatestImage(receiver : image.ImageReceiver) {
  receiver.readLatestImage().then((img: image.Image) => {
    console.info('Succeeded in reading the latest Image.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to read the latest Image.code ${error.code},message is ${error.message}`);
  });
}
```

#### readNextImage9+

readNextImage(callback: AsyncCallback<Image>): void

从ImageReceiver读取下一张图片。使用callback异步回调。

此接口需要在[on](#ZH-CN_TOPIC_0000002497605844__on9)回调触发后调用，才能正常的接收到数据。且此接口返回的[Image](zh-cn_topic_0000002497445862.html)对象使用完毕后需要调用[release](Interface (Image).md#ZH-CN_TOPIC_0000002497445862__release9)方法释放，释放后才可以继续接收新的数据。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

参数名类型必填说明callbackAsyncCallback<[Image](Interface (Image).md)>是回调函数，当获取下一张图片成功，err为undefined，data为获取到的下一张图片；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadNextImage(receiver : image.ImageReceiver) {
  receiver.readNextImage((err: BusinessError, img: image.Image) => {
    if (err) {
      console.error(`Failed to read the next Image.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in reading the next Image.');
    }
  });
}
```

#### readNextImage9+

readNextImage(): Promise<Image>

从ImageReceiver读取下一张图片。使用Promise异步回调。

此接口需要在[on](#ZH-CN_TOPIC_0000002497605844__on9)回调触发后调用，才能正常的接收到数据。且此接口返回的[Image](zh-cn_topic_0000002497445862.html)对象使用完毕后需要调用[release](Interface (Image).md#ZH-CN_TOPIC_0000002497445862__release9)方法释放，释放后才可以继续接收新的数据。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**

类型说明Promise<[Image](Interface (Image).md)>Promise对象，返回下一张图片。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadNextImage(receiver : image.ImageReceiver) {
  receiver.readNextImage().then((img: image.Image) => {
    console.info('Succeeded in reading the next Image.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to read the next Image.code ${error.code},message is ${error.message}`);
  });
}
```

#### on9+

on(type: 'imageArrival', callback: AsyncCallback<void>): void

接收图片时注册回调。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

参数名类型必填说明typestring是注册事件的类型，固定为'imageArrival'，接收图片时触发。callbackAsyncCallback<void>是回调函数，当注册事件触发成功，err为undefined，否则为错误对象。

**示例：**

```ets
async function On(receiver : image.ImageReceiver) {
  receiver.on('imageArrival', () => {
    // 接收到图片，实现回调函数逻辑。
  });
}
```

#### off13+

off(type: 'imageArrival', callback?: AsyncCallback<void>): void

释放buffer时移除注册回调。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

参数名类型必填说明typestring是注册事件的类型，固定为'imageArrival'，释放buffer时触发。callbackAsyncCallback<void>否移除的回调函数。

**示例：**

```ets
async function Off(receiver : image.ImageReceiver) {
  let callbackFunc = ()=>{
      // 实现回调函数逻辑。
  };
  receiver.on('imageArrival', callbackFunc);
  receiver.off('imageArrival', callbackFunc);
}
```

#### release9+

release(callback: AsyncCallback<void>): void

释放ImageReceiver实例。使用callback异步回调。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数，当释放ImageReceiver实例成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(receiver : image.ImageReceiver) {
  receiver.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the receiver.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing the receiver.');
    }
  })
}
```

#### release9+

release(): Promise<void>

释放ImageReceiver实例。使用Promise异步回调。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(receiver : image.ImageReceiver) {
  receiver.release().then(() => {
    console.info('Succeeded in releasing the receiver.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the receiver.code ${error.code},message is ${error.message}`);
  })
}
```