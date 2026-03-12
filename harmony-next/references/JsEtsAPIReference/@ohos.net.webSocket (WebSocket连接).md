# @ohos.net.webSocket (WebSocket连接)

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

给第三方应用提供webSocket客户端和服务端服务器，实现客户端与服务端的双向连接，目前服务端仅支持智慧屏使用。

客户端：使用WebSocket建立服务器与客户端的双向连接，需要先通过[createWebSocket](#ZH-CN_TOPIC_0000002529285443__websocketcreatewebsocket)方法创建[WebSocket](#ZH-CN_TOPIC_0000002529285443__websocket)对象，然后通过[connect](#ZH-CN_TOPIC_0000002529285443__connect)方法连接到服务器。当连接成功后，客户端会收到[open](#ZH-CN_TOPIC_0000002529285443__onopen)事件的回调，之后客户端就可以通过[send](#ZH-CN_TOPIC_0000002529285443__send)方法与服务器进行通信。当服务器发信息给客户端时，客户端会收到[message](#ZH-CN_TOPIC_0000002529285443__onmessage)事件的回调。当客户端想要取消此连接时，通过调用[close](#ZH-CN_TOPIC_0000002529285443__close)方法主动断开连接后，客户端会收到[close](#ZH-CN_TOPIC_0000002529285443__onclose)事件的回调。若在上述任一过程中发生错误，客户端会收到[error](#ZH-CN_TOPIC_0000002529285443__onerror)事件的回调。

服务端：（目前服务端仅支持智慧屏使用）使用WebSocket建立服务器与客户端的双向连接，需要先通过[createWebSocketServer](#ZH-CN_TOPIC_0000002529285443__websocketcreatewebsocketserver19)方法创建[WebSocketServer](#ZH-CN_TOPIC_0000002529285443__websocketserver19)对象，然后通过[start](#ZH-CN_TOPIC_0000002529285443__start19)方法启动服务器，监听客户端的申请建链的消息。当连接成功后，服务端会收到[connect](#ZH-CN_TOPIC_0000002529285443__onconnect19)事件的回调，之后服务端可以通过[send](#ZH-CN_TOPIC_0000002529285443__send19)方法与客户端进行通信，或者通过[listAllConnections](#ZH-CN_TOPIC_0000002529285443__listallconnections19)方法列举出当前与服务端建链的所有客户端信息。当客户端给服务端发消息时，服务端会收到[messageReceive](#ZH-CN_TOPIC_0000002529285443__onmessagereceive19)事件回调。当服务端想断开与某个客户端的连接时，可以通过调用[close](#ZH-CN_TOPIC_0000002529285443__close19)方法主动断开与某个客户端的连接，之后服务端会收到[close](#ZH-CN_TOPIC_0000002529285443__onclose19)事件的回调。当服务端想停止service时，可以调用[stop](#ZH-CN_TOPIC_0000002529285443__stop19)方法。若在上述任一过程中发生错误，服务端会收到[error](#ZH-CN_TOPIC_0000002529285443__onerror19)事件的回调。

#### 导入模块

```ets
import { webSocket } from '@kit.NetworkKit';
```

#### webSocket.createWebSocket

createWebSocket(): WebSocket

创建一个WebSocket对象，里面包括建立连接、关闭连接、发送数据和订阅/取消订阅WebSocket连接的打开事件、接收到服务器消息事件、关闭事件和错误事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明[WebSocket](#ZH-CN_TOPIC_0000002529285443__websocket)返回一个WebSocket对象，里面包括connect、send、close、on和off方法。

**示例：**

```ets
let ws: webSocket.WebSocket = webSocket.createWebSocket();
```

#### WebSocket

在调用WebSocket的方法前，需要先通过[webSocket.createWebSocket](#ZH-CN_TOPIC_0000002529285443__websocketcreatewebsocket)创建一个WebSocket。

#### connect

connect(url: string, callback: AsyncCallback<boolean>): void

根据URL地址，建立一个WebSocket连接，使用callback方式作为异步方法。

可通过监听error事件获得该接口的执行结果。

callback中返回的boolean值仅表示连接请求创建是否成功。如需感知WebSocket是否连接成功，需要在调用该接口前调用[on('open')](#ZH-CN_TOPIC_0000002529285443__onopen)订阅open事件。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

URL地址长度不能超过1024个字符，否则会连接失败。从API15开始，URL地址长度限制由1024修改为2048。

**参数：**

参数名类型必填说明urlstring是建立WebSocket连接的URL地址。callbackAsyncCallback<boolean>是回调函数。true:连接请求创建成功；false:连接请求创建失败。

**错误码：**

以下错误码的详细介绍参见[webSocket错误码](webSocket错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2302001Websocket url error.2302002Websocket certificate file does not exist.2302003Websocket connection already exists.2302998It is not allowed to access this domain.2302999Internal error.

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
let url = "ws://";
ws.connect(url, (err: BusinessError, value: boolean) => {
  if (!err) {
    console.info("connect success")
  } else {
    console.error(`connect fail. Code: ${err.code}, message: ${err.message}`)
  }
});
```

#### connect

connect(url: string, options: WebSocketRequestOptions, callback: AsyncCallback<boolean>): void

根据URL地址，建立一个WebSocket连接，使用callback方式作为异步方法。

可通过监听error事件获得该接口的执行结果，错误发生时会得到错误码：200。

callback中返回的boolean值仅表示连接请求创建是否成功。如需感知WebSocket是否连接成功，需要在调用该接口前调用[on('open')](#ZH-CN_TOPIC_0000002529285443__onopen)订阅open事件。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

URL地址长度不能超过1024个字符，否则会连接失败。

**参数：**

参数名类型必填说明urlstring是建立WebSocket连接的URL地址。optionsWebSocketRequestOptions是参考[WebSocketRequestOptions](#ZH-CN_TOPIC_0000002529285443__websocketrequestoptions)。callbackAsyncCallback<boolean>是回调函数。true:连接请求创建成功；false:连接请求创建失败。

**错误码：**

以下错误码的详细介绍参见[webSocket错误码](webSocket错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2302001Websocket url error.2302002Websocket certificate file does not exist.2302003Websocket connection already exists.2302998It is not allowed to access this domain.2302999Internal error.

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
let options: webSocket.WebSocketRequestOptions | undefined;
if (options !=undefined) {
  options.header = {
     name1: "value1",
     name2: "value2",
     name3: "value3"
  };
  options.caPath = "";
}
let url = "ws://"
ws.connect(url, options, (err: BusinessError, value: Object) => {
  if (!err) {
    console.info("connect success")
  } else {
    console.error(`connect fail. Code: ${err.code}, message: ${err.message}`)
  }
});
```

#### connect

connect(url: string, options?: WebSocketRequestOptions): Promise<boolean>

根据URL地址和header，建立一个WebSocket连接。使用Promise异步回调。

可通过监听error事件获得该接口的执行结果，错误发生时会得到错误码：200。

callback中返回的boolean值仅表示连接请求创建是否成功。如需感知WebSocket是否连接成功，需要在调用该接口前调用[on('open')](#ZH-CN_TOPIC_0000002529285443__onopen)订阅open事件。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

URL地址长度不能超过1024个字符，否则会连接失败。

**参数：**

参数名类型必填说明urlstring是建立WebSocket连接的URL地址。optionsWebSocketRequestOptions否参考[WebSocketRequestOptions](#ZH-CN_TOPIC_0000002529285443__websocketrequestoptions)。

**返回值：**

类型说明Promise<boolean>回调函数。true:连接请求创建成功；false:连接请求创建失败。

**错误码：**

以下错误码的详细介绍参见[webSocket错误码](webSocket错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2302001Websocket url error.2302002Websocket certificate file does not exist.2302003Websocket connection already exists.2302998It is not allowed to access this domain.2302999Internal error.

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
let url = "ws://"
let promise = ws.connect(url);
promise.then((value: boolean) => {
  console.info("connect success")
}).catch((err:string) => {
  console.error("connect fail, error:" + JSON.stringify(err))
});
```

#### send

send(data: string | ArrayBuffer, callback: AsyncCallback<boolean>): void

通过WebSocket连接发送数据，使用callback方式作为异步方法。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明datastring | ArrayBuffer是

发送的数据。

API 6及更早版本仅支持string类型。API 8起同时支持string和ArrayBuffer类型。最大支持发送5242864字节数据(即5 * 1024 * 1024 - 16)，超过该大小会返回401错误码。

callbackAsyncCallback<boolean>是回调函数。true:发送请求创建成功；false:发送请求创建失败。

**错误码：**

以下错误码的详细介绍参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
let url = "ws://"
class OutValue {
  status: number = 0
  message: string = ""
}
ws.connect(url, (err: BusinessError, value: boolean) => {
    if (!err) {
      console.info("connect success")
    } else {
      console.error(`connect fail. Code: ${err.code}, message: ${err.message}`)
    }
});
ws.on('open', (err: BusinessError, value: Object) => {
  console.info("on open, status:" + (value as OutValue).status + ", message:" + (value as OutValue).message)
    ws.send("Hello, server!", (err: BusinessError, value: boolean) => {
    if (!err) {
      console.info("send success")
    } else {
      console.error(`send fail. Code: ${err.code}, message: ${err.message}`)
    }
  });
});
```

send接口必须在监听到open事件后才可以调用。

#### send

send(data: string | ArrayBuffer): Promise<boolean>

通过WebSocket连接发送数据。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明datastring | ArrayBuffer是

发送的数据。

API 6及更早版本仅支持string类型。API 8起同时支持string和ArrayBuffer类型。最大支持发送5242864字节数据(即5 * 1024 * 1024 - 16)，超过该大小会返回401错误码。

**返回值：**

类型说明Promise<boolean>以Promise形式返回发送数据的结果。true:发送请求创建成功；false:发送请求创建失败。

**错误码：**

以下错误码的详细介绍参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
let url = "ws://"
class OutValue {
  status: number = 0
  message: string = ""
}
ws.connect(url, (err: BusinessError, value: boolean) => {
    if (!err) {
      console.info("connect success")
    } else {
      console.error("connect fail. Code: ${err.code}, message: ${err.message}")
    }
});

ws.on('open', (err: BusinessError, value: Object) => {
  console.info("on open, status:" + (value as OutValue).status + ", message:" + (value as OutValue).message)
  let promise = ws.send("Hello, server!");
  promise.then((value: boolean) => {
    console.info("send success")
  }).catch((err:string) => {
    console.error("send fail, error:" + JSON.stringify(err))
  });
});
```

send接口必须在监听到open事件后才可以调用。

#### close

close(callback: AsyncCallback<boolean>): void

关闭WebSocket连接，使用callback方式作为异步方法。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<boolean>是回调函数。true:关闭请求创建成功；false:关闭请求创建失败。

**错误码：**

以下错误码的详细介绍参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
ws.close((err: BusinessError) => {
  if (!err) {
    console.info("close success")
  } else {
    console.error(`close fail. Code: ${err.code}, message: ${err.message}`)
  }
});
```

#### close

close(options: WebSocketCloseOptions, callback: AsyncCallback<boolean>): void

根据参数options，关闭WebSocket连接，使用callback方式作为异步方法。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明optionsWebSocketCloseOptions是参考[WebSocketCloseOptions](#ZH-CN_TOPIC_0000002529285443__websocketcloseoptions)。callbackAsyncCallback<boolean>是回调函数。true:关闭请求创建成功；false:关闭请求创建失败。

**错误码：**

以下错误码的详细介绍参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();

let options: webSocket.WebSocketCloseOptions | undefined;
if (options != undefined) {
    options.code = 1000
    options.reason = "your reason"
}
ws.close(options, (err: BusinessError) => {
    if (!err) {
        console.info("close success")
    } else {
        console.error(`close fail. Code: ${err.code}, message: ${err.message}`)
    }
});
```

#### close

close(options?: WebSocketCloseOptions): Promise<boolean>

根据可选参数code和reason，关闭WebSocket连接。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明optionsWebSocketCloseOptions否参考[WebSocketCloseOptions](#ZH-CN_TOPIC_0000002529285443__websocketcloseoptions)。

**返回值：**

类型说明Promise<boolean>以Promise形式返回关闭连接的结果。true:关闭请求创建成功；false:关闭请求创建失败。

**错误码：**

以下错误码的详细介绍参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
let options: webSocket.WebSocketCloseOptions | undefined;
if (options != undefined) {
    options.code = 1000
    options.reason = "your reason"
}
let promise = ws.close();
promise.then((value: boolean) => {
    console.info("close success")
}).catch((err:string) => {
    console.error("close fail, error:" + JSON.stringify(err))
});
```

#### on('open')

on(type: 'open', callback: AsyncCallback<Object>): void

订阅WebSocket的打开事件，使用callback方式作为异步方法。该事件用于指示WebSocket是否连接成功。该接口需要在调用[connect](#ZH-CN_TOPIC_0000002529285443__connect)发起连接请求前调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'open'：WebSocket的打开事件。callbackAsyncCallback<Object>是回调函数。

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let ws= webSocket.createWebSocket();
class OutValue {
  status: number = 0
  message: string = ""
}
ws.on('open', (err: BusinessError, value: Object) => {
  console.info("on open, status:" + (value as OutValue).status + ", message:" + (value as OutValue).message)
});
```

#### off('open')

off(type: 'open', callback?: AsyncCallback<Object>): void

取消订阅WebSocket的打开事件，使用callback方式作为异步方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'open'：WebSocket的打开事件。callbackAsyncCallback<Object>否回调函数。

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
class OutValue {
  status: number = 0
  message: string = ""
}
let callback1 = (err: BusinessError, value: Object) => {
 console.info("on open, status:" + ((value as OutValue).status + ", message:" + (value as OutValue).message))
}
ws.on('open', callback1);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
ws.off('open', callback1);
```

#### on('message')

on(type: 'message', callback: AsyncCallback<string | ArrayBuffer>): void

订阅WebSocket的接收服务器消息事件，使用callback方式作为异步方法。

AsyncCallback中的数据可以是字符串（API version 6开始支持）或ArrayBuffer（API version 8开始支持）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'message'：WebSocket的接收服务器消息事件。callbackAsyncCallback<string | ArrayBuffer 8+>是回调函数。

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
ws.on('message', (err: BusinessError<void>, value: string | ArrayBuffer) => {
  console.info("on message, message:" + value)
});
```

#### off('message')

off(type: 'message', callback?: AsyncCallback<string | ArrayBuffer>): void

取消订阅WebSocket的接收服务器消息事件，使用callback方式作为异步方法。

AsyncCallback中的数据可以是字符串(API 6)或ArrayBuffer(API 8)。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'message'：WebSocket的接收到服务器消息事件。callbackAsyncCallback<string |ArrayBuffer 8+>否回调函数。

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.off('message');
```

#### on('close')

on(type: 'close', callback: AsyncCallback<CloseResult>): void

订阅WebSocket的关闭事件，使用callback方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'close'：WebSocket的关闭事件。callbackAsyncCallback<CloseResult>是

回调函数。

close：close错误码，reason：错误码说明

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
ws.on('close', (err: BusinessError, value: webSocket.CloseResult) => {
  console.info("on close, code is " + value.code + ", reason is " + value.reason)
});
```

#### off('close')

off(type: 'close', callback?: AsyncCallback<CloseResult>): void

取消订阅WebSocket的关闭事件，使用callback方式作为异步方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'close'：WebSocket的关闭事件。callbackAsyncCallback<CloseResult>否

回调函数。

close：close错误码，reason：错误码说明

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.off('close');
```

#### on('error')

on(type: 'error', callback: ErrorCallback): void

订阅WebSocket的Error事件，使用callback方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'error'：WebSocket的Error事件。callbackErrorCallback是回调函数。

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
ws.on('error', (err: BusinessError) => {
  console.error(`on error. Code: ${err.code}, message: ${err.message}`)
});
```

#### off('error')

off(type: 'error', callback?: ErrorCallback): void

取消订阅WebSocket的Error事件，使用callback方式作为异步方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'error'：WebSocket的Error事件。callbackErrorCallback否回调函数。

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.off('error');
```

#### on('dataEnd')11+

on(type: 'dataEnd', callback: Callback<void>): void

订阅WebSocket的数据接收结束事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'dataEnd'：WebSocket的数据接收结束事件。callbackCallback<void>是回调函数。

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.on('dataEnd', () => {
  console.info("on dataEnd")
});
```

#### off('dataEnd')11+

off(type: 'dataEnd', callback?: Callback<void>): void

取消订阅WebSocket的数据接收结束事件，使用callback方式作为异步方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'dataEnd'：WebSocket的数据接收结束事件。callbackCallback<void>否回调函数。

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.off('dataEnd');
```

#### on('headerReceive')12+

on(type: 'headerReceive', callback: Callback<ResponseHeaders>): void

订阅HTTP Response Header事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'headerReceive'：WebSocket的headerReceive事件。callbackCallback<ResponseHeaders>是回调函数，返回订阅事件。

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.on('headerReceive', (data) => {
  console.info("on headerReceive " + JSON.stringify(data))
});
```

#### off('headerReceive')12+

off(type: 'headerReceive', callback?: Callback<ResponseHeaders>): void

取消订阅HTTP Response Header事件，使用callback方式作为异步方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'headerReceive'：WebSocket的headerReceive事件。callbackCallback<ResponseHeaders>否回调函数，返回订阅事件。

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.off('headerReceive');
```

#### webSocket.createWebSocketServer19+

createWebSocketServer(): WebSocketServer

创建一个WebSocketServer对象，包括启动服务、发送数据、关闭连接、列出客户端信息、停止服务，订阅/取消订阅webSocket连接的连接事件、接收到客户端消息事件、关闭事件和错误事件。

**系统能力**: SystemCapability.Communication.NetStack

**设备行为差异：** 该接口在TV设备中可正常调用，在其他设备中返回nullptr。

**返回值：**

类型说明[WebSocketServer](#ZH-CN_TOPIC_0000002529285443__websocketserver19)返回一个WebSocketServer对象，里面包括start、listAllConnections、send、close、stop、on和off方法。

**示例：**

```ets
let ws: webSocket.WebSocketServer = webSocket.createWebSocketServer();
```

#### WebSocketServer19+

在调用WebSocketServer方法前，需要先通过[webSocket.createWebSocketServer](#ZH-CN_TOPIC_0000002529285443__websocketcreatewebsocketserver19)创建一个WebSocketServer。

#### start19+

start(config: WebSocketServerConfig): Promise<boolean>

配置config参数，启动服务端service。使用Promise异步回调。

可通过监听error事件获得该接口的执行结果，错误码说明参见[webSocket错误码](webSocket错误码.md)。

**需要权限**: ohos.permission.INTERNET

**系统能力**: SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明config[WebSocketServerConfig](#ZH-CN_TOPIC_0000002529285443__websocketserverconfig19)是启动websocketServer服务器。

**返回值：**

类型说明Promise<boolean>promise对象。返回true表示服务器启动成功；返回false表示服务启动失败。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[webSocket错误码](webSocket错误码.md)。

错误码ID错误信息201Permission denied.2302002Websocket certificate file does not exist.2302004Can't listen on the given NIC.2302005Can't listen on the given Port.2302999Websocket other unknown error.

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer: webSocket.WebSocketServer;
let config: webSocket.WebSocketServerConfig = {
  serverPort: 8080, // 监听端口
  maxConcurrentClientsNumber: 10,
  maxConnectionsForOneClient: 10,
}

localServer = webSocket.createWebSocketServer();
localServer.start(config).then((success: boolean) => {
  if (success) {
    console.info('webSocket server start success');
  } else {
    console.error('websocket server start failed');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
});
```

#### send19+

send(data: string | ArrayBuffer, connection: WebSocketConnection): Promise<boolean>

通过WebSocket连接发送数据。使用Promise异步回调。

send接口必须在监听到connect事件后才可以调用。

**需要权限**: ohos.permission.INTERNET

**系统能力**: SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明datastring | ArrayBuffer是服务端发送消息的数据，同时支持string（字符串）和ArrayBuffer（二进制）类型。最大支持发送5242864字节数据(即5 * 1024 * 1024 - 16)，超过该大小会返回401错误码。connection[WebSocketConnection](#ZH-CN_TOPIC_0000002529285443__websocketconnection19)是发送的客户端信息。

**返回值：**

类型说明Promise<boolean>promise对象。返回true表示发送请求创建成功；返回false表示发送请求创建失败。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[webSocket错误码](webSocket错误码.md)。

错误码ID错误信息201Permission denied.2302006websocket connection does not exist.

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer: webSocket.WebSocketServer;
let config: webSocket.WebSocketServerConfig = {
  serverPort: 8080, // 监听端口
  maxConcurrentClientsNumber: 10,
  maxConnectionsForOneClient: 10,
}

localServer = webSocket.createWebSocketServer();
localServer.start(config).then((success: boolean) => {
  if (success) {
    console.info('webSocket server start success');
  } else {
    console.error('websocket server start failed');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
});

localServer.on('connect', async (connection: webSocket.WebSocketConnection) => {
  console.info(`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}`);
  // 当收到on('connect')事件时，可以通过send()方法与客户端进行通信
  localServer.send("Hello, I'm server!", connection).then((success: boolean) => {
    if (success) {
      console.info('message send successfully');
    } else {
      console.error('message send failed');
    }
  }).catch((error: BusinessError) => {
    console.error(`message send failed, Code: ${error.code}, message: ${error.message}`);
  });
});
```

#### listAllConnections19+

listAllConnections(): WebSocketConnection[]

获取与服务端连接的所有客户端信息。

**需要权限**: ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明[WebSocketConnection[]](#ZH-CN_TOPIC_0000002529285443__websocketconnection19)以字符串数组形式返回所有客户端的信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission denied.

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let connections: webSocket.WebSocketConnection[] = [];
let localServer: webSocket.WebSocketServer;
let config: webSocket.WebSocketServerConfig = {
  serverPort: 8080, // 监听端口
  maxConcurrentClientsNumber: 10,
  maxConnectionsForOneClient: 10,
}

localServer = webSocket.createWebSocketServer();
localServer.start(config).then((success: boolean) => {
  if (success) {
    console.info('webSocket server start success');
  } else {
    console.error('websocket server start failed');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
});

localServer.on('connect', async (connection: webSocket.WebSocketConnection) => {
  console.info(`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}`);
  try {
    connections = await localServer.listAllConnections();
    if (connections.length === 0) {
      console.info('client list is empty');
    } else {
      console.info(`client list cnt: ${connections.length}, client connections list is: ${connections}`);
    }
  } catch (error) {
    console.error(`Failed to listAllConnections. Code: ${error.code}, message: ${error.message}`);
  }
});
```

#### close19+

close(connection: WebSocketConnection, options?: webSocket.WebSocketCloseOptions): Promise<boolean>

关闭指定websocket连接。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明connection[WebSocketConnection](#ZH-CN_TOPIC_0000002529285443__websocketconnection19)是客户端信息，包括客户端的ip地址和端口号port。options[webSocket.WebSocketCloseOptions](#ZH-CN_TOPIC_0000002529285443__websocketcloseoptions)否

关闭WebSocket连接时，可选参数的类型和说明。

- 错误码默认：200。原因值默认：Websocket connect failed。

**返回值：**

类型说明Promise<boolean>promise对象。返回true表示关闭请求创建成功；返回false表示关闭请求创建失败。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[webSocket错误码](webSocket错误码.md)。

错误码ID错误信息201Permission denied.2302006websocket connection does not exist.

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer: webSocket.WebSocketServer;
let config: webSocket.WebSocketServerConfig = {
  serverPort: 8080, // 监听端口
  maxConcurrentClientsNumber: 10,
  maxConnectionsForOneClient: 10,
}

localServer = webSocket.createWebSocketServer();
localServer.start(config).then((success: boolean) => {
  if (success) {
    console.info('webSocket server start success');
  } else {
    console.error('websocket server start failed');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
});

localServer.on('connect', (connection: webSocket.WebSocketConnection) => {
  console.info(`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}`);
  localServer.close(connection).then((success: boolean) => {
    if (success) {
      console.info('close client successfully');
    } else {
      console.error('close client failed');
    }
  });
});
```

#### stop19+

stop(): Promise<boolean>

停止服务端服务。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<boolean>promise对象。返回true表示停止服务端service请求创建成功；返回false表示停止服务端service请求创建失败。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission denied.

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer: webSocket.WebSocketServer;
let config: webSocket.WebSocketServerConfig = {
  serverPort: 8080, // 监听端口
  maxConcurrentClientsNumber: 10,
  maxConnectionsForOneClient: 10,
}

localServer = webSocket.createWebSocketServer();
localServer.start(config).then((success: boolean) => {
  if (success) {
    console.info('webSocket server start success');
  } else {
    console.error('websocket server start failed');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
});

localServer.stop().then((success: boolean) => {
  if (success) {
    console.info('server stop service successfully');
  } else {
    console.error('server stop service failed');
  }
});
```

#### on('connect')19+

on(type: 'connect', callback: Callback<WebSocketConnection>): void

订阅WebSocketServer的连接事件（客户端与服务端建链成功），使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'connect'，当onconnect()调用完成，客户端与服务端建链成功。callbackCallback<[WebSocketConnection](#ZH-CN_TOPIC_0000002529285443__websocketconnection19)>是回调函数。连接的客户端信息。

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.on('connect', (connection: webSocket.WebSocketConnection) => {
  console.info(`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}`);
});
```

#### off('connect')19+

off(type: 'connect', callback?: Callback<WebSocketConnection>): void

取消订阅WebSocketServer的连接事件（客户端与服务端建链成功），使用callback方式作为异步方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'connect'，当offconnect()调用完成，取消监听连接事件成功。callbackCallback<[WebSocketConnection](#ZH-CN_TOPIC_0000002529285443__websocketconnection19)>否回调函数。连接的客户端信息。

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.off('connect');
```

#### on('messageReceive')19+

on(type: 'messageReceive', callback: Callback<WebSocketMessage>): void

订阅WebSocketServer的接收客户端消息的事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'messageReceive'，当onmessageReceive()调用完成，接收到客户端消息成功。callbackCallback<[WebSocketMessage](#ZH-CN_TOPIC_0000002529285443__websocketmessage19)>是

回调函数。

clientconnection:客户端信息，data:客户端发送的数据消息。

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.on('messageReceive', (message: webSocket.WebSocketMessage) => {
  console.info(`on message received, client: ${message.clientConnection}, data: ${message.data}`);
});
```

#### off('messageReceive')19+

off(type: 'messageReceive', callback?: Callback<WebSocketMessage>): void

取消订阅WebSocketServer的接收到客户端消息事件，使用callback方式作为异步方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'messageReceive'，当offmessageReceive()调用完成，取消订阅接收客户端消息成功。callbackCallback<[WebSocketMessage](#ZH-CN_TOPIC_0000002529285443__websocketmessage19)>否

从指定客户端接收到的消息，包括客户端的信息和数据。

- clientconnection：客户端信息。

- data：客户端发送的消息。

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.off('messageReceive');
```

#### on('close')19+

on(type: 'close', callback: ClientConnectionCloseCallback): void

订阅WebSocketServer的关闭事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'close'，当onclose()调用完成，连接关闭成功。callback[ClientConnectionCloseCallback](#ZH-CN_TOPIC_0000002529285443__clientconnectionclosecallback19)是

回调函数。

close：close错误码；reason：错误码说明。

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.on('close', (clientConnection: webSocket.WebSocketConnection, closeReason: webSocket.CloseResult) => {
  console.info(`client close, client: ${clientConnection}, closeReason: Code: ${closeReason.code}, reason: ${closeReason.reason}`);
});
```

#### off('close')19+

off(type: 'close', callback?: ClientConnectionCloseCallback): void

取消订阅WebSocketServer的关闭事件，使用callback方式作为异步方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'close'，当offclose()调用完成，取消订阅连接关闭事件成功。callback[ClientConnectionCloseCallback](#ZH-CN_TOPIC_0000002529285443__clientconnectionclosecallback19)否

回调函数。

close：close错误码；reason：错误码说明。

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.off('close');
```

#### on('error')19+

on(type: 'error', callback: ErrorCallback): void

订阅WebSocketServer的Error事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'error'，当onerror()调用完成，error事件发生。callback[ErrorCallback](@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__errorcallback)是回调函数。

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wsServer: webSocket.WebSocketServer = webSocket.createWebSocketServer();
wsServer.on('error', (err: BusinessError) => {
  console.error(`error. Code: ${err.code}, message: ${err.message}`);
});
```

#### off('error')19+

off(type: 'error', callback?: ErrorCallback): void

取消订阅WebSocketServer的Error事件，使用callback方式作为异步方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'error'，当offerror()调用完成，取消订阅error事件成功。callback[ErrorCallback](@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__errorcallback)否回调函数。默认值：200。

**示例：**

```ets
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.off('error');
```

#### WebSocketRequestOptions

建立WebSocket连接时，可选参数的类型和说明。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明headerObject否是

建立WebSocket连接可选参数，代表建立连接时携带的HTTP头信息。参数内容自定义，也可以不指定。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

caPath11+string否是如果设置了此参数，系统将使用用户指定路径的CA证书，(开发者需保证该路径下CA证书的可访问性)，否则将使用系统预设CA证书，系统预设CA证书位置：/etc/ssl/certs/cacert.pem。证书路径为沙箱映射路径（开发者可通过UIAbilityContext提供的能力获取应用沙箱路径）。目前仅支持格式为pem的文本证书。clientCert11+[ClientCert](#ZH-CN_TOPIC_0000002529285443__clientcert11)否是支持传输客户端证书。proxy12+[ProxyConfiguration](#ZH-CN_TOPIC_0000002529285443__proxyconfiguration12)否是通信过程中的代理信息，默认使用系统网络代理。protocol12+string否是自定义Sec-WebSocket-Protocol字段，默认为""。skipServerCertVerification20+boolean否是是否跳过服务器证书验证。true表示跳过服务器证书验证，false表示不跳过服务器证书验证。默认为false。pingInterval21+number否是自定义[心跳检测](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/websocket-connection#场景介绍)时间，默认为30s。每pingInterval周期会发起心跳检测，设置为0则表示关闭心跳检测。最大值：30000s，最小值：0s。pongTimeout21+number否是自定义发起心跳检测后，超时断开时间，默认为30s。发起心跳检测后若pongTimeout时间未响应则断开连接。最大值：30000s，最小值：0s。pongTimeout须小于等于pingInterval。

#### ClientCert11+

客户端证书类型。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明certPathstring否否证书路径。keyPathstring否否证书密钥的路径。keyPasswordstring否是证书密钥的密码。缺省为空字符串。

#### ProxyConfiguration12+

type ProxyConfiguration = 'system' | 'no-proxy' | HttpProxy

网络代理配置信息

**系统能力**：SystemCapability.Communication.NetStack

类型说明'system'使用系统默认网络代理。'no-proxy'不使用网络代理。[HttpProxy](@ohos.net.connection (网络连接管理).md#ZH-CN_TOPIC_0000002497605446__httpproxy10)使用指定的网络代理。

#### WebSocketCloseOptions

关闭WebSocket连接时，可选参数的类型和说明。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明codenumber否是错误码，关闭WebSocket连接时的可选参数，可根据实际情况来填。传入值需为正整数，默认值为1000。reasonstring否是原因值，关闭WebSocket连接时的可选参数，可根据实际情况来填。默认值为空字符串（""）。

#### CloseResult10+

关闭WebSocket连接时，订阅close事件得到的关闭结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明codenumber否否错误码，订阅close事件得到的关闭连接的错误码。reasonstring否否原因值，订阅close事件得到的关闭连接的错误原因。

#### ResponseHeaders12+

type ResponseHeaders = {

[k: string]: string | string[] | undefined;

}

服务器发送的响应头。

**系统能力**：SystemCapability.Communication.NetStack

名称类型必填说明[k:string]string | string[] | undefined否键值对形式存储。其键的类型为字符，可取任意值，其值的类型为字符、字符数组或undefined。

#### close错误码说明

发送给服务端的错误码可以自行定义，下面的列表仅供参考。

**系统能力**：SystemCapability.Communication.NetStack

值说明1000正常关闭。1001服务器主动关闭。1002协议错误。1003无法处理的数据类型。1004~1015保留值。

#### HttpProxy12+

type HttpProxy = connection.HttpProxy

网络全局代理配置信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

类型说明connection.HttpProxy使用指定的网络代理。

#### WebSocketServerConfig19+

启动服务端的service时，需要输入的配置信息和说明。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明serverIPstring否是服务端监听特定ip地址，默认是"0.0.0.0"。serverPortnumber否否服务端监听的端口号。serverCert[ServerCert](#ZH-CN_TOPIC_0000002529285443__servercert19)否是指定服务端证书的信息，包括服务端证书文件路径和服务端证书的私钥文件路径。protocolstring否是自定义协议。maxConcurrentClientsNumbernumber否否最大并发客户端数量，当到达最大数时，服务端拒绝新连接。默认最大数量为10。maxConnectionsForOneClientnumber否否单个客户端的最大连接数。默认最大数量为10。

#### ServerCert19+

指定服务端证书的信息，包括服务端证书文件路径和服务端证书的私钥文件路径。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明certPathstring否否服务端证书文件路径。keyPathstring否否服务端证书的私钥文件路径。

#### WebSocketMessage19+

从指定客户端接收到的消息，包括客户端的信息和数据。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明datastring |ArrayBuffer否否接收到的客户端发的消息数据。clientConnection[WebSocketConnection](#ZH-CN_TOPIC_0000002529285443__websocketconnection19)否否客户端信息，包括客户端的ip地址和端口号port。

#### WebSocketConnection19+

客户端信息，包括客户端的ip地址和端口号port。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明clientIPstring否否客户端的ip地址。clientPortnumber否否客户端的端口号port。

#### ClientConnectionCloseCallback19+

type ClientConnectionCloseCallback = (clientConnection: WebSocketConnection, closeReason: CloseResult) => void

关闭WebSocketServer连接时，订阅close事件得到的指定客户端的关闭结果。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明clientConnection[WebSocketConnection](#ZH-CN_TOPIC_0000002529285443__websocketconnection19)是客户端信息，包括客户端的ip地址和端口号port。closeReason[CloseResult](#ZH-CN_TOPIC_0000002529285443__closeresult10)是关闭WebSocket连接时，订阅close事件得到的关闭结果。