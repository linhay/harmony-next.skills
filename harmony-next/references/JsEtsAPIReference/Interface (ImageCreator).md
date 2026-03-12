# Interface (ImageCreator)

ImageCreator类，用于请求图像数据区域，并开放给应用编译图像数据的能力。

在调用以下方法前需要先通过[image.createImageCreator](Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagecreator11)创建ImageCreator实例，ImageCreator不支持多线程。

由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002529285833__release9)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

- 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 9开始支持。

#### 导入模块

```ets
import { image } from '@kit.ImageKit';
```

#### 属性

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

名称类型只读可选说明capacity9+number是否同时访问的图像数。该参数仅作为期望值，实际capacity由设备硬件决定。format9+[ImageFormat](Enums.md#ZH-CN_TOPIC_0000002529285837__imageformat9)是否图像格式。

#### dequeueImage9+

dequeueImage(callback: AsyncCallback<Image>): void

从空闲队列中获取buffer图片，用于绘制UI内容。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

参数名类型必填说明callbackAsyncCallback<[Image](Interface (Image).md)>是回调函数，当获取最新图片成功，err为undefined，data为获取到的最新图片；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function DequeueImage(creator : image.ImageCreator) {
  creator.dequeueImage((err: BusinessError, img: image.Image) => {
    if (err) {
      console.error(`Failed to dequeue the Image.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in dequeuing the Image.');
    }
  });
}
```

#### dequeueImage9+

dequeueImage(): Promise<Image>

从空闲队列中获取buffer图片，用于绘制UI内容。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**返回值：**

类型说明Promise<[Image](Interface (Image).md)>Promise对象，返回最新图片。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function DequeueImage(creator : image.ImageCreator) {
  creator.dequeueImage().then((img: image.Image) => {
    console.info('Succeeded in dequeuing the Image.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to dequeue the Image.code ${error.code},message is ${error.message}`);
  })
}
```

#### queueImage9+

queueImage(image: Image, callback: AsyncCallback<void>): void

将绘制好的图片放入队列。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

参数名类型必填说明image[Image](Interface (Image).md)是绘制好的buffer图像。callbackAsyncCallback<void>是回调函数，当将图片放入队列成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function QueueImage(creator : image.ImageCreator) {
  creator.dequeueImage().then((img: image.Image) => {
    // 绘制图片。
    img.getComponent(4).then((component : image.Component) => {
      let bufferArr: Uint8Array = new Uint8Array(component.byteBuffer);
      for (let i = 0; i < bufferArr.length; i += 4) {
        bufferArr[i] = 0; // B
        bufferArr[i + 1] = 0; // G
        bufferArr[i + 2] = 255; // R
        bufferArr[i + 3] = 255; // A
      }
    })
    creator.queueImage(img, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to queue the Image.code ${err.code},message is ${err.message}`);
      } else {
        console.info('Succeeded in queuing the Image.');
      }
    })
  })
}
```

#### queueImage9+

queueImage(image: Image): Promise<void>

将绘制好的图片放入队列。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

参数名类型必填说明image[Image](Interface (Image).md)是绘制好的buffer图像。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function QueueImage(creator : image.ImageCreator) {
  creator.dequeueImage().then((img: image.Image) => {
    // 绘制图片。
    img.getComponent(4).then((component: image.Component) => {
      let bufferArr: Uint8Array = new Uint8Array(component.byteBuffer);
      for (let i = 0; i < bufferArr.length; i += 4) {
        bufferArr[i] = 0; // B
        bufferArr[i + 1] = 0; // G
        bufferArr[i + 2] = 255; // R
        bufferArr[i + 3] = 255; // A
      }
    })
    creator.queueImage(img).then(() => {
      console.info('Succeeded in queuing the Image.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to queue the Image.code ${error.code},message is ${error.message}`);
    })
  })
}
```

#### on9+

on(type: 'imageRelease', callback: AsyncCallback<void>): void

监听imageRelease事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

参数名类型必填说明typestring是监听事件类型，如'imageRelease'。callbackAsyncCallback<void>是回调函数，当监听事件触发成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function On(creator : image.ImageCreator) {
  creator.on('imageRelease', (err: BusinessError) => {
    if (err) {
      console.error(`Failed to get the imageRelease callback.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in getting imageRelease callback.');
    }
  })
}
```

#### off13+

off(type: 'imageRelease', callback?: AsyncCallback<void>): void

释放buffer时，移除注册的回调函数。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

参数名类型必填说明typestring是监听事件类型，如'imageRelease'。callbackAsyncCallback<void>否回调函数。当移除注册成功时，err返回null，否则为错误对象。

**示例：**

```ets
async function Off(creator : image.ImageCreator) {
  let callbackFunc = ()=>{
      // 实现回调函数逻辑。
  }
  creator.on('imageRelease', callbackFunc)
  creator.off('imageRelease', callbackFunc)
}
```

#### release9+

release(callback: AsyncCallback<void>): void

释放当前图像。使用callback异步回调。

由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数，当图像释放成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(creator : image.ImageCreator) {
  creator.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the creator.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing creator.');
    }
  });
}
```

#### release9+

release(): Promise<void>

释放当前图像。使用Promise异步回调。

由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(creator : image.ImageCreator) {
  creator.release().then(() => {
    console.info('Succeeded in releasing creator.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the creator.code ${error.code},message is ${error.message}`);
  })
}
```