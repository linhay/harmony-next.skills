# @ohos.net.socket (Socket连接)

本模块提供利用Socket进行数据传输的能力，支持TCPSocket、UDPSocket、WebSocket和TLSSocket。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块API使用时建议放在worker线程或者taskpool中做网络操作，否则可能会导致UI线程卡顿。

#### 导入模块

```ets
import { socket } from '@kit.NetworkKit';
```

#### socket.constructUDPSocketInstance

constructUDPSocketInstance(): UDPSocket

创建一个UDPSocket对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明[UDPSocket](#ZH-CN_TOPIC_0000002497445470__udpsocket)返回一个UDPSocket对象。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
```

#### UDPSocket

UDPSocket连接。在调用UDPSocket的方法前，需要先通过[socket.constructUDPSocketInstance](#ZH-CN_TOPIC_0000002497445470__socketconstructudpsocketinstance)创建UDPSocket对象。

#### bind

bind(address: NetAddress, callback: AsyncCallback<void>): void

绑定IP地址和端口，端口可以由用户指定或由系统随机分配。使用callback方式作为异步方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明address[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)是本端地址信息，参考[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)。callbackAsyncCallback<void>是回调函数。成功返回空，失败返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',  // 本端地址
  port: 1234
}
udp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
```

#### bind

bind(address: NetAddress): Promise<void>

绑定IP地址和端口，端口可以由用户指定或由系统随机分配。使用Promise方式作为异步方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明address[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)是本端地址信息，参考[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',  // 本端地址
  port: 8080
}
udp.bind(bindAddr).then(() => {
  console.info('bind success');
}).catch((err: BusinessError) => {
  console.error('bind fail');
});
```

#### send

send(options: UDPSendOptions, callback: AsyncCallback<void>): void

通过UDPSocket连接发送数据。使用callback方式作为异步方法。

发送数据前，需要先调用[UDPSocket.bind()](#ZH-CN_TOPIC_0000002497445470__bind)绑定IP地址和端口。该接口为耗时操作，请在Worker线程或taskpool线程调用该接口。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[UDPSendOptions](#ZH-CN_TOPIC_0000002497445470__udpsendoptions)是UDPSocket发送参数，参考[UDPSendOptions](#ZH-CN_TOPIC_0000002497445470__udpsendoptions)。callbackAsyncCallback<void>是回调函数。成功返回空，失败返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2301206Socks5 failed to connect to the proxy server.2301207Socks5 username or password is invalid.2301208Socks5 failed to connect to the remote server.2301209Socks5 failed to negotiate the authentication method.2301210Socks5 failed to send the message.2301211Socks5 failed to receive the message.2301212Socks5 serialization error.2301213Socks5 deserialization error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',  // 本端地址
  port: 1234
}
udp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',  // 对端地址
  port: 8080
}
let sendOptions: socket.UDPSendOptions = {
  data: 'Hello, server!',
  address: netAddress
}
udp.send(sendOptions, (err: BusinessError) => {
  if (err) {
    console.error('send fail');
    return;
  }
  console.info('send success');
});
```

**示例（设置socket代理）：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',  // 本端地址
  port: 1234
}
udp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',  // 对端地址
  port: 8080
}
let socks5Server: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let proxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let sendOptions: socket.UDPSendOptions = {
  data: 'Hello, server!',
  address: netAddress,
  proxy: proxyOptions,
}
udp.send(sendOptions, (err: BusinessError) => {
  if (err) {
    console.error('send fail');
    return;
  }
  console.info('send success');
});
```

#### send

send(options: UDPSendOptions): Promise<void>

通过UDPSocket连接发送数据。使用Promise方式作为异步方法。

发送数据前，需要先调用[UDPSocket.bind()](#ZH-CN_TOPIC_0000002497445470__bind)绑定IP地址和端口。该接口为耗时操作，请在Worker线程或taskpool线程调用该接口。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[UDPSendOptions](#ZH-CN_TOPIC_0000002497445470__udpsendoptions)是UDPSocket发送参数，参考[UDPSendOptions](#ZH-CN_TOPIC_0000002497445470__udpsendoptions)。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2301206Socks5 failed to connect to the proxy server.2301207Socks5 username or password is invalid.2301208Socks5 failed to connect to the remote server.2301209Socks5 failed to negotiate the authentication method.2301210Socks5 failed to send the message.2301211Socks5 failed to receive the message.2301212Socks5 serialization error.2301213Socks5 deserialization error.

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx', // 本端地址
  port: 8080
}
udp.bind(bindAddr).then(() => {
  console.info('bind success');
}).catch((err: BusinessError) => {
  console.error('bind fail');
  return;
});
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx', // 对端地址
  port: 8080
}
let sendOptions: socket.UDPSendOptions = {
  data: 'Hello, server!',
  address: netAddress
}
udp.send(sendOptions).then(() => {
  console.info('send success');
}).catch((err: BusinessError) => {
  console.error('send fail');
});
```

**示例（设置socket代理）：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx', // 本端地址
  port: 8080
}
udp.bind(bindAddr).then(() => {
  console.info('bind success');
}).catch((err: BusinessError) => {
  console.error('bind fail');
  return;
});
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx', // 对端地址
  port: 8080
}
let socks5Server: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let proxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let sendOptions: socket.UDPSendOptions = {
  data: 'Hello, server!',
  address: netAddress,
  proxy: proxyOptions,
}
udp.send(sendOptions).then(() => {
  console.info('send success');
}).catch((err: BusinessError) => {
  console.error('send fail');
});
```

#### close

close(callback: AsyncCallback<void>): void

关闭UDPSocket连接。使用callback方式作为异步方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。关闭UDPSocket连接后触发回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission denied.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
udp.close((err: BusinessError) => {
  if (err) {
    console.error('close fail');
    return;
  }
  console.info('close success');
})
```

#### close

close(): Promise<void>

关闭UDPSocket连接。使用Promise方式作为异步方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission denied.

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
udp.close().then(() => {
  console.info('close success');
}).catch((err: BusinessError) => {
  console.error('close fail');
});
```

#### getState

getState(callback: AsyncCallback<SocketStateBase>): void

获取UDPSocket状态。使用callback方式作为异步方法。

bind方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<[SocketStateBase](#ZH-CN_TOPIC_0000002497445470__socketstatebase)>是回调函数。成功返回UDPSocket状态信息，失败返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission denied.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
udp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.error('bind success');
  udp.getState((err: BusinessError, data: socket.SocketStateBase) => {
    if (err) {
      console.error('getState fail');
      return;
    }
    console.info('getState success:' + JSON.stringify(data));
  })
})
```

#### getState

getState(): Promise<SocketStateBase>

获取UDPSocket状态。使用Promise方式作为异步方法。

bind方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission denied.

**返回值：**

类型说明Promise<[SocketStateBase](#ZH-CN_TOPIC_0000002497445470__socketstatebase)>以Promise形式返回获取UDPSocket状态的结果。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
udp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
  udp.getState().then((data: socket.SocketStateBase) => {
    console.info('getState success:' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error('getState fail' + JSON.stringify(err));
  });
});
```

#### setExtraOptions

setExtraOptions(options: UDPExtraOptions, callback: AsyncCallback<void>): void

设置UDPSocket连接的其他属性。使用callback方式作为异步方法。

bind方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[UDPExtraOptions](#ZH-CN_TOPIC_0000002497445470__udpextraoptions)是UDPSocket连接的其他属性，参考[UDPExtraOptions](#ZH-CN_TOPIC_0000002497445470__udpextraoptions)。callbackAsyncCallback<void>是回调函数。成功返回空，失败返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();

let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
udp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
  let udpextraoptions: socket.UDPExtraOptions = {
    receiveBufferSize: 8192,
    sendBufferSize: 8192,
    reuseAddress: false,
    socketTimeout: 6000,
    broadcast: true
  }
  udp.setExtraOptions(udpextraoptions, (err: BusinessError) => {
    if (err) {
      console.error('setExtraOptions fail');
      return;
    }
    console.info('setExtraOptions success');
  })
})
```

#### setExtraOptions

setExtraOptions(options: UDPExtraOptions): Promise<void>

设置UDPSocket连接的其他属性。使用Promise方式作为异步方法。

bind方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[UDPExtraOptions](#ZH-CN_TOPIC_0000002497445470__udpextraoptions)是UDPSocket连接的其他属性，参考[UDPExtraOptions](#ZH-CN_TOPIC_0000002497445470__udpextraoptions)。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();

let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
udp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
  let udpextraoptions: socket.UDPExtraOptions = {
    receiveBufferSize: 8192,
    sendBufferSize: 8192,
    reuseAddress: false,
    socketTimeout: 6000,
    broadcast: true
  }
  udp.setExtraOptions(udpextraoptions).then(() => {
    console.info('setExtraOptions success');
  }).catch((err: BusinessError) => {
    console.error('setExtraOptions fail');
  });
})
```

#### getLocalAddress12+

getLocalAddress(): Promise<NetAddress>

获取UDP连接的本地Socket地址。使用Promise方式作为异步方法。

bind方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)>以Promise形式返回获取本地socket地址的结果。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)。

错误码ID错误信息2300002System internal error.2301009Bad file descriptor.2303188Socket operation on non-socket.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();

let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
udp.bind(bindAddr).then(() => {
  console.info('bind success');
  udp.getLocalAddress().then((localAddress: socket.NetAddress) => {
        console.info("UDP_Socket get SUCCESS! Address：" + JSON.stringify(localAddress));
      }).catch((err: BusinessError) => {
        console.error("UDP_Socket get FAILED! Error: " + JSON.stringify(err));
      })
}).catch((err: BusinessError) => {
  console.error('bind fail');
});
```

#### on('message')

on(type: 'message', callback: Callback<SocketMessageInfo>): void

订阅UDPSocket连接的接收消息事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'message'：接收消息事件。callbackCallback<[SocketMessageInfo](#ZH-CN_TOPIC_0000002497445470__socketmessageinfo11)>是回调函数。返回订阅某类事件后UDPSocket连接成功的状态信息。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();

udp.on('message', (value: socket.SocketMessageInfo) => {
  let messageView = '';
  let uint8Array = new Uint8Array(value.message);
  for (let i: number = 0; i < value.message.byteLength; i++) {
    let messages = uint8Array[i];
    let message = String.fromCharCode(messages);
    messageView += message;
  }
  console.info('on message message: ' + JSON.stringify(messageView));
  console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
});
```

#### off('message')

off(type: 'message', callback?: Callback<SocketMessageInfo>): void

取消订阅UDPSocket连接的接收消息事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'message'：接收消息事件。callbackCallback<[SocketMessageInfo](#ZH-CN_TOPIC_0000002497445470__socketmessageinfo11)>否回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let messageView = '';
let callback = (value: socket.SocketMessageInfo) => {
  for (let i: number = 0; i < value.message.byteLength; i++) {
    let uint8Array = new Uint8Array(value.message)
    let messages = uint8Array[i]
    let message = String.fromCharCode(messages);
    messageView += message;
  }
  console.info('on message message: ' + JSON.stringify(messageView));
  console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
}
udp.on('message', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
udp.off('message', callback);
udp.off('message');
```

#### on('listening' | 'close')

on(type: 'listening' | 'close', callback: Callback<void>): void

订阅UDPSocket连接的数据包消息事件或关闭事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是

订阅的事件类型。

- 'listening'：数据包消息事件。

- 'close'：关闭事件。

callbackCallback<void>是回调函数。UDPSocket连接的某类数据包消息事件或关闭事件发生变化后触发回调函数。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
udp.on('listening', () => {
  console.info("on listening success");
});
udp.on('close', () => {
  console.info("on close success");
});
```

#### off('listening' | 'close')

off(type: 'listening' | 'close', callback?: Callback<void>): void

取消订阅UDPSocket连接的数据包消息事件或关闭事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是

取消订阅事件类型。

- 'listening'：数据包消息事件。

- 'close'：关闭事件。

callbackCallback<void>否回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let callback1 = () => {
  console.info("on listening, success");
}
udp.on('listening', callback1);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
udp.off('listening', callback1);
udp.off('listening');
let callback2 = () => {
  console.info("on close, success");
}
udp.on('close', callback2);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
udp.off('close', callback2);
udp.off('close');
```

#### on('error')

on(type: 'error', callback: ErrorCallback): void

订阅UDPSocket连接的error事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'error'：error事件。callbackErrorCallback是回调函数。UDPSocket连接发生error事件后触发回调函数。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
udp.on('error', (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err))
});
```

#### off('error')

off(type: 'error', callback?: ErrorCallback): void

取消订阅UDPSocket连接的error事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'error'：error事件。callbackErrorCallback否回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let callback = (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err));
}
udp.on('error', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
udp.off('error', callback);
udp.off('error');
```

#### NetAddress

目标地址信息。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明address11+string否否本地绑定的ip地址。portnumber否否端口号 ，范围0~65535。如果不指定系统随机分配端口。familynumber否否

网络协议类型，可选类型：

- 1：IPv4。默认为1。

- 2：IPv6。地址为IPV6类型，该字段必须被显式指定为2。

- 3：Domain18+。地址为Domain类型，该字段必须被显式指定为3。当前仅支持[TCPSocket.connect](#ZH-CN_TOPIC_0000002497445470__connect)和[TLSSocket.connect](#ZH-CN_TOPIC_0000002497445470__connect9)。

#### ProxyOptions18+

Socket代理信息。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明type[ProxyTypes](#ZH-CN_TOPIC_0000002497445470__proxytypes18)否否代理类型。address[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)否否代理地址信息。usernamestring否是指定用户名，如果使用用户密码验证方式。passwordstring否是指定密码，如果使用用户密码验证方式。

#### ProxyTypes18+

Socket代理类型。

**系统能力**：SystemCapability.Communication.NetStack

名称值说明NONE0不使用代理。SOCKS51使用Socks5代理。

#### UDPSendOptions

UDPSocket发送参数。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明datastring | ArrayBuffer否否发送的数据。address[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)否否目标地址信息。proxy18+[ProxyOptions](#ZH-CN_TOPIC_0000002497445470__proxyoptions18)否是使用的代理信息，默认不使用代理。

#### UDPExtraOptions

UDPSocket连接的其他属性。继承自[ExtraOptionsBase](#ZH-CN_TOPIC_0000002497445470__extraoptionsbase7)。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明broadcastboolean否是是否可以发送广播。true表示可发送广播，false表示不可发送广播。默认为false。

#### SocketMessageInfo11+

socket连接信息

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明messageArrayBuffer否否接收的事件消息。remoteInfo[SocketRemoteInfo](#ZH-CN_TOPIC_0000002497445470__socketremoteinfo)否否socket连接信息。

#### SocketStateBase

Socket的状态信息。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明isBoundboolean否否是否绑定。true：绑定；false：不绑定。isCloseboolean否否是否关闭。true：关闭；false：打开。isConnectedboolean否否是否连接。true：连接；false：断开。

#### SocketRemoteInfo

Socket的连接信息。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明addressstring否否本地绑定的ip地址。family'IPv4' | 'IPv6'否否

网络协议类型，可选类型：

- IPv4

- IPv6

默认为IPv4。

portnumber否否端口号，范围0~65535。sizenumber否否服务器响应信息的字节长度。

#### UDP 错误码说明

UDP 其余错误码映射形式为：2301000 + Linux内核错误码。

错误码的详细介绍参见[Socket错误码](SOCKET 错误码.md)。

#### socket.constructMulticastSocketInstance11+

constructMulticastSocketInstance(): MulticastSocket

创建一个MulticastSocket对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明[MulticastSocket](#ZH-CN_TOPIC_0000002497445470__multicastsocket11)返回一个MulticastSocket对象。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
```

#### MulticastSocket11+

MulticastSocket连接。在调用MulticastSocket的方法前，需要先通过[socket.constructMulticastSocketInstance](#ZH-CN_TOPIC_0000002497445470__socketconstructmulticastsocketinstance11)创建MulticastSocket对象。

#### addMembership11+

addMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>): void

加入多播组。使用callback方法作为异步方法。

多播使用的IP地址属于特定的范围（例如224.0.0.0到239.255.255.255）。

加入多播组后，既可以是发送端，也可以是接收端，相互之间以广播的形式传递数据，不区分客户端或服务端。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明multicastAddress[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)是目标地址信息，参考[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)。callbackAsyncCallback<void>是回调函数。失败返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2301022Invalid argument.2301088Not a socket.2301098Address in use.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
let addr: socket.NetAddress = {
  address: '239.255.0.1',
  port: 8080
}
multicast.addMembership(addr, (err: Object) => {
  if (err) {
    console.error('add membership fail, err: ' + JSON.stringify(err));
    return;
  }
  console.info('add membership success');
})
```

#### addMembership11+

addMembership(multicastAddress: NetAddress): Promise<void>

加入多播组。使用Promise方法作为异步方法。

多播使用的IP地址属于特定的范围（例如224.0.0.0到239.255.255.255）。

加入多播组后，既可以是发送端，也可以是接收端，相互之间以广播的形式传递数据，不区分客户端或服务端。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明multicastAddress[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)是目标地址信息，参考[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)。

**返回值：**

类型说明Promise<void>以Promise形式返回MulticastSocket加入多播组的行为结果。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2301088Not a socket.2301098Address in use.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
let addr: socket.NetAddress = {
  address: '239.255.0.1',
  port: 8080
}
multicast.addMembership(addr).then(() => {
  console.info('addMembership success');
}).catch((err: Object) => {
  console.error('addMembership fail');
});
```

#### dropMembership11+

dropMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>): void

退出多播组。使用callback方法作为异步方法。

多播使用的IP地址属于特定的范围（例如224.0.0.0到239.255.255.255）。

从已加入的多播组中退出，必须在加入多播组 [addMembership](#ZH-CN_TOPIC_0000002497445470__addmembership11) 之后退出才有效。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明multicastAddress[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)是目标地址信息，参考[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)。callbackAsyncCallback<void>是回调函数。失败返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2301088Not a socket.2301098Address in use.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
let addr: socket.NetAddress = {
  address: '239.255.0.1',
  port: 8080
}
multicast.dropMembership(addr, (err: Object) => {
  if (err) {
    console.error('drop membership fail, err: ' + JSON.stringify(err));
    return;
  }
  console.info('drop membership success');
})
```

#### dropMembership11+

dropMembership(multicastAddress: NetAddress): Promise<void>

退出多播组。使用Promise方法作为异步方法。

多播使用的IP地址属于特定的范围（例如224.0.0.0到239.255.255.255）。

从已加入的多播组中退出，必须在加入多播组 [addMembership](#ZH-CN_TOPIC_0000002497445470__addmembership11) 之后退出才有效。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明multicastAddress[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)是目标地址信息，参考[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)。

**返回值：**

类型说明Promise<void>以Promise形式返回MulticastSocket加入多播组的执行结果。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2301088Not a socket.2301098Address in use.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
let addr: socket.NetAddress = {
  address: '239.255.0.1',
  port: 8080
}
multicast.dropMembership(addr).then(() => {
  console.info('drop membership success');
}).catch((err: Object) => {
  console.error('drop membership fail');
});
```

#### setMulticastTTL11+

setMulticastTTL(ttl: number, callback: AsyncCallback<void>): void

设置多播通信时数据包在网络传输过程中路由器最大跳数。使用callback方法作为异步方法。

用于限制数据包在网络中传输时能够经过的最大路由器跳数的字段，TTL (Time to live)。

范围为 0～255，默认值为 1 。

如果一个多播数据包的 TTL 值为 1，那么它只能被直接连接到发送者的主机接收。如果 TTL 被设置为一个较大的值，那么数据包就能够被传送到更远的网络范围内。

在调用 [addMembership](#ZH-CN_TOPIC_0000002497445470__addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明ttlnumber是ttl设置数值，类型为数字number。callbackAsyncCallback<void>是回调函数。失败返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2301022Invalid argument.2301088Not a socket.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
let ttl = 8
multicast.setMulticastTTL(ttl, (err: Object) => {
  if (err) {
    console.error('set ttl fail, err: ' + JSON.stringify(err));
    return;
  }
  console.info('set ttl success');
})
```

#### setMulticastTTL11+

setMulticastTTL(ttl: number): Promise<void>

设置多播通信时数据包在网络传输过程中路由器最大跳数。使用Promise方法作为异步方法。

用于限制数据包在网络中传输时能够经过的最大路由器跳数的字段，TTL (Time to live)。

范围为 0～255，默认值为 1 。

如果一个多播数据包的 TTL 值为 1，那么它只能被直接连接到发送者的主机接收。如果 TTL 被设置为一个较大的值，那么数据包就能够被传送到更远的网络范围内。

在调用 [addMembership](#ZH-CN_TOPIC_0000002497445470__addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明ttlnumber是ttl设置数值，类型为数字Number。

**返回值：**

类型说明Promise<void>以Promise形式返回MulticastSocket设置TTL数值的结果。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2301022Invalid argument.2301088Not a socket.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
multicast.setMulticastTTL(8).then(() => {
  console.info('set ttl success');
}).catch((err: Object) => {
  console.error('set ttl failed');
});
```

#### getMulticastTTL11+

getMulticastTTL(callback: AsyncCallback<number>): void

获取数据包在网络传输过程中路由器最大跳数(TTL)的值。使用callback方法作为异步方法。

用于限制数据包在网络中传输时能够经过的最大路由器跳数的字段，TTL (Time to live)。

范围为 0～255，默认值为 1 。

如果一个多播数据包的 TTL 值为 1，那么它只能被直接连接到发送者的主机接收。如果 TTL 被设置为一个较大的值，那么数据包就能够被传送到更远的网络范围内。

在调用 [addMembership](#ZH-CN_TOPIC_0000002497445470__addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是回调函数。失败返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2301088Not a socket.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
multicast.getMulticastTTL((err: Object, value: Number) => {
  if (err) {
    console.error('set ttl fail, err: ' + JSON.stringify(err));
    return;
  }
  console.info('set ttl success, value: ' + JSON.stringify(value));
})
```

#### getMulticastTTL11+

getMulticastTTL(): Promise<number>

获取数据包在网络传输过程中路由器最大跳数(TTL)的值。使用Promise方法作为异步方法。

用于限制数据包在网络中传输时能够经过的最大路由器跳数的字段，TTL (Time to live)。

范围为 0～255，默认值为 1 。

如果一个多播数据包的 TTL 值为 1，那么它只能被直接连接到发送者的主机接收。如果 TTL 被设置为一个较大的值，那么数据包就能够被传送到更远的网络范围内。

在调用 [addMembership](#ZH-CN_TOPIC_0000002497445470__addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<number>以Promise形式返回当前TTL数值。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2301088Not a socket.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
multicast.getMulticastTTL().then((value: Number) => {
  console.info('ttl: ', JSON.stringify(value));
}).catch((err: Object) => {
  console.error('set ttl failed');
});
```

#### setLoopbackMode11+

setLoopbackMode(flag: boolean, callback: AsyncCallback<void>): void

设置多播通信中的环回模式标志位。使用callback方法作为异步方法。

用于设置环回模式，开启或关闭两种状态，默认为开启状态。

如果一个多播通信中环回模式设置值为 true，那么它允许主机在本地循环接收自己发送的多播数据包。如果为 false，则主机不会接收到自己发送的多播数据包。

在调用 [addMembership](#ZH-CN_TOPIC_0000002497445470__addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明flagboolean是是否开启环回模式。true表示环回模式开启，false表示环回模式关闭。callbackAsyncCallback<void>是回调函数。失败返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2301088Not a socket.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
multicast.setLoopbackMode(false, (err: Object) => {
  if (err) {
    console.error('set loopback mode fail, err: ' + JSON.stringify(err));
    return;
  }
  console.info('set loopback mode success');
})
```

#### setLoopbackMode11+

setLoopbackMode(flag: boolean): Promise<void>

设置多播通信中的环回模式标志位。使用Promise异步回调。

用于设置环回模式，开启或关闭两种状态，默认为开启状态。

如果一个多播通信中环回模式设置值为 true，那么它允许主机在本地循环接收自己发送的多播数据包。如果为 false，则主机不会接收到自己发送的多播数据包。

在调用 [addMembership](#ZH-CN_TOPIC_0000002497445470__addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明flagboolean是是否开启环回模式。true表示环回模式开启，false表示环回模式关闭。

**返回值：**

类型说明Promise<void>以Promise形式返回MulticastSocket设置环回模式的结果。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2301088Not a socket.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
multicast.setLoopbackMode(false).then(() => {
  console.info('set loopback mode success');
}).catch((err: Object) => {
  console.error('set loopback mode failed');
});
```

#### getLoopbackMode11+

getLoopbackMode(callback: AsyncCallback<boolean>): void

获取多播通信中的环回模式状态。使用callback异步回调。

用于获取当前环回模式开启或关闭的状态。

如果获取的属性值为 true，表示环回模式是开启的状态，允许主机在本地循环接收自己发送的多播数据包。如果为 false，则表示环回模式是关闭的状态，主机不会接收到自己发送的多播数据包。

在调用 [addMembership](#ZH-CN_TOPIC_0000002497445470__addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<boolean>是回调函数。返回值为环回模式状态，true表示环回模式开启，false表示环回模式关闭。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2301088Not a socket.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
multicast.getLoopbackMode((err: Object, value: Boolean) => {
  if (err) {
    console.error('get loopback mode fail, err: ' + JSON.stringify(err));
    return;
  }
  console.info('get loopback mode success, value: ' + JSON.stringify(value));
})
```

#### getLoopbackMode11+

getLoopbackMode(): Promise<boolean>

获取多播通信中的环回模式状态。使用Promise方法作为异步方法。

用于获取当前环回模式开启或关闭的状态。

如果获取的属性值为 true，表示环回模式是开启的状态，允许主机在本地循环接收自己发送的多播数据包。如果为 false，则表示环回模式是关闭的状态，主机不会接收到自己发送的多播数据包。

在调用 [addMembership](#ZH-CN_TOPIC_0000002497445470__addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示环回模式开启，返回false表示环回模式关闭。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2301088Not a socket.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
multicast.getLoopbackMode().then((value: Boolean) => {
  console.info('loopback mode: ', JSON.stringify(value));
}).catch((err: Object) => {
  console.error('get loopback mode failed');
});
```

#### socket.constructTCPSocketInstance7+

constructTCPSocketInstance(): TCPSocket

创建一个TCPSocket对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明[TCPSocket](#ZH-CN_TOPIC_0000002497445470__tcpsocket)返回一个TCPSocket对象。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
```

#### TCPSocket

TCPSocket连接。在调用TCPSocket的方法前，需要先通过[socket.constructTCPSocketInstance](#ZH-CN_TOPIC_0000002497445470__socketconstructtcpsocketinstance7)创建TCPSocket对象。

#### bind

bind(address: NetAddress, callback: AsyncCallback<void>): void

绑定IP地址和端口，端口可以指定为0由系统随机分配或由用户指定为其它非0端口。使用callback方法作为异步方法。

bind方法如果因为端口冲突而执行失败，则会由系统随机分配端口号。

TCP客户端可先调用该接口(tcp.bind)显式绑定IP地址和端口号，再调用tcp.connect完成与服务端的连接；也可直接调用tcp.connect由系统自动绑定IP地址和端口号，完成与服务端的连接。

bind的IP为'localhost'或'127.0.0.1'时，只允许本地回环接口的连接，即服务端和客户端运行在同一台机器上。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明address[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)是本端地址信息，参考[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)。callbackAsyncCallback<void>是回调函数。失败返回错误、错误信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tcp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
})
```

#### bind

bind(address: NetAddress): Promise<void>

绑定IP地址和端口，端口可以指定为0由系统随机分配或由用户指定为其它非0端口。使用Promise方法作为异步方法。

bind方法如果因为端口冲突而执行失败，则会由系统随机分配端口号。

TCP客户端可先调用该接口(tcp.bind)显式绑定IP地址和端口号，再调用tcp.connect完成与服务端的连接；也可直接调用tcp.connect由系统自动绑定IP地址和端口号，完成与服务端的连接。

bind的IP为'localhost'或'127.0.0.1'时，只允许本地回环接口的连接，即服务端和客户端运行在同一台机器上。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明address[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)是本端地址信息，参考[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)。

**返回值：**

类型说明Promise<void>以Promise形式返回TCPSocket绑定本机的IP地址和端口的结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tcp.bind(bindAddr).then(() => {
  console.info('bind success');
}).catch((err: BusinessError) => {
  console.error('bind fail');
});
```

#### connect

connect(options: TCPConnectOptions, callback: AsyncCallback<void>): void

连接到指定的IP地址和端口。使用callback方法作为异步方法。

在没有执行tcp.bind的情况下，也可以直接调用该接口完成与TCP服务端的连接

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[TCPConnectOptions](#ZH-CN_TOPIC_0000002497445470__tcpconnectoptions)是TCPSocket连接的参数，参考[TCPConnectOptions](#ZH-CN_TOPIC_0000002497445470__tcpconnectoptions)。callbackAsyncCallback<void>是回调函数。失败返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2301206Socks5 failed to connect to the proxy server.2301207Socks5 username or password is invalid.2301208Socks5 failed to connect to the remote server.2301209Socks5 failed to negotiate the authentication method.2301210Socks5 failed to send the message.2301211Socks5 failed to receive the message.2301212Socks5 serialization error.2301213Socks5 deserialization error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions, (err: BusinessError) => {
  if (err) {
    console.error('connect fail');
    return;
  }
  console.info('connect success');
})
```

**示例（设置socket代理）：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let socks5Server: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let proxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000,
  proxy: proxyOptions,
}
tcp.connect(tcpconnectoptions, (err: BusinessError) => {
  if (err) {
    console.error('connect fail');
    return;
  }
  console.info('connect success');
})
```

#### connect

connect(options: TCPConnectOptions): Promise<void>

连接到指定的IP地址和端口。使用promise方法作为异步方法。

在没有执行tcp.bind的情况下，也可以直接调用该接口完成与TCP服务端的连接。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[TCPConnectOptions](#ZH-CN_TOPIC_0000002497445470__tcpconnectoptions)是TCPSocket连接的参数，参考[TCPConnectOptions](#ZH-CN_TOPIC_0000002497445470__tcpconnectoptions)。

**返回值：**

类型说明Promise<void>以Promise形式返回TCPSocket连接到指定的IP地址和端口的结果。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2301206Socks5 failed to connect to the proxy server.2301207Socks5 username or password is invalid.2301208Socks5 failed to connect to the remote server.2301209Socks5 failed to negotiate the authentication method.2301210Socks5 failed to send the message.2301211Socks5 failed to receive the message.2301212Socks5 serialization error.2301213Socks5 deserialization error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions).then(() => {
  console.info('connect success')
}).catch((err: BusinessError) => {
  console.error('connect fail');
});
```

**示例（设置socket代理）：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let socks5Server: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let proxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000,
  proxy: proxyOptions,
}
tcp.connect(tcpconnectoptions).then(() => {
  console.info('connect success')
}).catch((err: BusinessError) => {
  console.error('connect fail');
});
```

#### send

send(options: TCPSendOptions, callback: AsyncCallback<void>): void

通过TCPSocket连接发送数据。使用callback方式作为异步方法。

connect方法调用成功后，才可调用此方法。该接口为耗时操作，请在Worker线程或taskpool线程调用该接口。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[TCPSendOptions](#ZH-CN_TOPIC_0000002497445470__tcpsendoptions)是TCPSocket发送请求的参数，参考[TCPSendOptions](#ZH-CN_TOPIC_0000002497445470__tcpsendoptions)。callbackAsyncCallback<void>是回调函数。失败返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions, () => {
  console.info('connect success');
  let tcpSendOptions: socket.TCPSendOptions = {
    data: 'Hello, server!'
  }
  tcp.send(tcpSendOptions, (err: BusinessError) => {
    if (err) {
      console.error('send fail');
      return;
    }
    console.info('send success');
  })
})
```

#### send

send(options: TCPSendOptions): Promise<void>

通过TCPSocket连接发送数据。使用Promise方式作为异步方法。

connect方法调用成功后，才可调用此方法。该接口为耗时操作，请在Worker线程或taskpool线程调用该接口。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[TCPSendOptions](#ZH-CN_TOPIC_0000002497445470__tcpsendoptions)是TCPSocket发送请求的参数，参考[TCPSendOptions](#ZH-CN_TOPIC_0000002497445470__tcpsendoptions)。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions, () => {
  console.info('connect success');
  let tcpSendOptions: socket.TCPSendOptions = {
    data: 'Hello, server!'
  }
  tcp.send(tcpSendOptions).then(() => {
    console.info('send success');
  }).catch((err: BusinessError) => {
    console.error('send fail');
  });
})
```

#### close

close(callback: AsyncCallback<void>): void

关闭TCPSocket连接。使用callback方式作为异步方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。失败返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission denied.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();

tcp.close((err: BusinessError) => {
  if (err) {
    console.error('close fail');
    return;
  }
  console.info('close success');
})
```

#### close

close(): Promise<void>

关闭TCPSocket连接。使用Promise方式作为异步方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission denied.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();

tcp.close().then(() => {
  console.info('close success');
}).catch((err: BusinessError) => {
  console.error('close fail');
});
```

#### getRemoteAddress

getRemoteAddress(callback: AsyncCallback<NetAddress>): void

获取对端Socket地址。使用callback方式作为异步方法。

connect方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)>是回调函数。成功时返回对端Socket地址，失败时返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission denied.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions, () => {
  console.info('connect success');
  tcp.getRemoteAddress((err: BusinessError, data: socket.NetAddress) => {
    if (err) {
      console.error('getRemoteAddressfail');
      return;
    }
    console.info('getRemoteAddresssuccess:' + JSON.stringify(data));
  })
});
```

#### getRemoteAddress

getRemoteAddress(): Promise<NetAddress>

获取对端Socket地址。使用Promise方式作为异步方法。

connect方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)>以Promise形式返回获取对端socket地址的结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission denied.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions).then(() => {
  console.info('connect success');
  tcp.getRemoteAddress().then(() => {
    console.info('getRemoteAddress success');
  }).catch((err: BusinessError) => {
    console.error('getRemoteAddressfail');
  });
}).catch((err: BusinessError) => {
  console.error('connect fail');
});
```

#### getState

getState(callback: AsyncCallback<SocketStateBase>): void

获取TCPSocket状态。使用callback方式作为异步方法。

bind或connect方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<[SocketStateBase](#ZH-CN_TOPIC_0000002497445470__socketstatebase)>是回调函数。成功时获取TCPSocket状态，失败时返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission denied.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions, () => {
  console.info('connect success');
  tcp.getState((err: BusinessError, data: socket.SocketStateBase) => {
    if (err) {
      console.error('getState fail');
      return;
    }
    console.info('getState success:' + JSON.stringify(data));
  });
});
```

#### getState

getState(): Promise<SocketStateBase>

获取TCPSocket状态。使用Promise方式作为异步方法。

bind或connect方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[SocketStateBase](#ZH-CN_TOPIC_0000002497445470__socketstatebase)>以Promise形式返回获取TCPSocket状态的结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission denied.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions).then(() => {
  console.info('connect success');
  tcp.getState().then(() => {
    console.info('getState success');
  }).catch((err: BusinessError) => {
    console.error('getState fail');
  });
}).catch((err: BusinessError) => {
  console.error('connect fail');
});
```

#### getSocketFd10+

getSocketFd(callback: AsyncCallback<number>): void

获取TCPSocket的文件描述符。使用callback方式作为异步方法。

bind或connect方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是回调函数，当成功时，返回socket的文件描述符，失败时，返回undefined。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  // 绑定指定网络接口
}
tcp.bind(bindAddr)
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions)
tcp.getSocketFd((err: BusinessError, data: number) => {
  console.error("getSocketFd failed: " + err);
  console.info("tunenlfd: " + data);
})
```

#### getSocketFd10+

getSocketFd(): Promise<number>

获取TCPSocket的文件描述符。使用Promise方式作为异步方法。

bind或connect方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<number>以Promise形式返回socket的文件描述符。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let bindAddr: socket.NetAddress = {
    address: '192.168.xx.xxx',
  // 绑定指定网络接口
}
tcp.bind(bindAddr)
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions)
tcp.getSocketFd().then((data: number) => {
  console.info("tunenlfd: " + data);
})
```

#### setExtraOptions

setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void

设置TCPSocket连接的其他属性。使用callback方式作为异步方法。

bind或connect方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[TCPExtraOptions](#ZH-CN_TOPIC_0000002497445470__tcpextraoptions)是TCPSocket连接的其他属性，参考[TCPExtraOptions](#ZH-CN_TOPIC_0000002497445470__tcpextraoptions)。callbackAsyncCallback<void>是回调函数。失败时返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}

interface SocketLinger {
  on: boolean;
  linger: number;
}

tcp.connect(tcpconnectoptions, () => {
  console.info('connect success');
  let tcpExtraOptions: socket.TCPExtraOptions = {
    keepAlive: true,
    OOBInline: true,
    TCPNoDelay: true,
    socketLinger: { on: true, linger: 10 } as SocketLinger,
    receiveBufferSize: 8192,
    sendBufferSize: 8192,
    reuseAddress: true,
    socketTimeout: 3000
  }
  tcp.setExtraOptions(tcpExtraOptions, (err: BusinessError) => {
    if (err) {
      console.error('setExtraOptions fail');
      return;
    }
    console.info('setExtraOptions success');
  });
});
```

#### setExtraOptions

setExtraOptions(options: TCPExtraOptions): Promise<void>

设置TCPSocket连接的其他属性。使用Promise方式作为异步方法。

bind或connect方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[TCPExtraOptions](#ZH-CN_TOPIC_0000002497445470__tcpextraoptions)是TCPSocket连接的其他属性，参考[TCPExtraOptions](#ZH-CN_TOPIC_0000002497445470__tcpextraoptions)。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}

interface SocketLinger {
  on: boolean;
  linger: number;
}

tcp.connect(tcpconnectoptions, () => {
  console.info('connect success');
  let tcpExtraOptions: socket.TCPExtraOptions = {
    keepAlive: true,
    OOBInline: true,
    TCPNoDelay: true,
    socketLinger: { on: true, linger: 10 } as SocketLinger,
    receiveBufferSize: 8192,
    sendBufferSize: 8192,
    reuseAddress: true,
    socketTimeout: 3000
  }
  tcp.setExtraOptions(tcpExtraOptions).then(() => {
    console.info('setExtraOptions success');
  }).catch((err: BusinessError) => {
    console.error('setExtraOptions fail');
  });
});
```

#### getLocalAddress12+

getLocalAddress(): Promise<NetAddress>

获取TCPSocket的本地Socket地址。使用Promise方式作为异步方法。

bind方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)>以Promise形式返回获取本地socket地址的结果。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)。

错误码ID错误信息2300002System internal error.2301009Bad file descriptor.2303188Socket operation on non-socket.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  family: 1,
  port: 8080
}
tcp.bind(bindAddr).then(() => {
  tcp.getLocalAddress().then((localAddress: socket.NetAddress) => {
    console.info("SUCCESS! Address:" + JSON.stringify(localAddress));
  }).catch((err: BusinessError) => {
    console.error("FAILED! Error:" + JSON.stringify(err));
  })
}).catch((err: BusinessError) => {
  console.error('bind fail');
});
```

#### on('message')

on(type: 'message', callback: Callback<SocketMessageInfo>): void

订阅TCPSocket连接的接收消息事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'message'：接收消息事件。callbackCallback<[SocketMessageInfo](#ZH-CN_TOPIC_0000002497445470__socketmessageinfo11)>是回调函数。返回TCPSocket连接信息。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
tcp.on('message', (value: socket.SocketMessageInfo) => {
  let messageView = '';
  let uint8Array = new Uint8Array(value.message) ;
  for (let i: number = 0; i < value.message.byteLength; i++) {
    let messages = uint8Array[i];
    let message = String.fromCharCode(messages);
    messageView += message;
  }
  console.info('on message message: ' + JSON.stringify(messageView));
  console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
});
```

#### off('message')

off(type: 'message', callback?: Callback<SocketMessageInfo>): void

取消订阅TCPSocket连接的接收消息事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'message'：接收消息事件。callbackCallback<[SocketMessageInfo](#ZH-CN_TOPIC_0000002497445470__socketmessageinfo11)>否回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let messageView = '';
let callback = (value: socket.SocketMessageInfo) => {
  for (let i: number = 0; i < value.message.byteLength; i++) {
    let uint8Array = new Uint8Array(value.message)
    let messages = uint8Array[i]
    let message = String.fromCharCode(messages);
    messageView += message;
  }
  console.info('on message message: ' + JSON.stringify(messageView));
  console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
}
tcp.on('message', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
tcp.off('message', callback);
tcp.off('message');
```

#### on('connect' | 'close')

on(type: 'connect' | 'close', callback: Callback<void>): void

订阅TCPSocket的连接事件或关闭事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是

订阅的事件类型。

- 'connect'：连接事件。

- 'close'：关闭事件。

callbackCallback<void>是回调函数。TCPSocket的连接事件或关闭事件触发时调用回调函数。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
tcp.on('connect', () => {
  console.info("on connect success")
});
tcp.on('close', () => {
  console.info("on close success")
});
```

#### off('connect' | 'close')

off(type: 'connect' | 'close', callback?: Callback<void>): void

取消订阅TCPSocket的连接事件或关闭事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是

取消订阅的事件类型。

- 'connect'：连接事件。

- 'close'：关闭事件。

callbackCallback<void>否回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let callback1 = () => {
  console.info("on connect success");
}
tcp.on('connect', callback1);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
tcp.off('connect', callback1);
tcp.off('connect');
let callback2 = () => {
  console.info("on close success");
}
tcp.on('close', callback2);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
tcp.off('close', callback2);
tcp.off('close');
```

#### on('error')

on(type: 'error', callback: ErrorCallback): void

订阅TCPSocket连接的error事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'error'：error事件。callbackErrorCallback是回调函数。TCPSocket连接订阅的某类error事件触发时调用回调函数。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
tcp.on('error', (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err))
});
```

#### off('error')

off(type: 'error', callback?: ErrorCallback): void

取消订阅TCPSocket连接的error事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'error'：error事件。callbackErrorCallback否回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let callback = (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err));
}
tcp.on('error', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
tcp.off('error', callback);
tcp.off('error');
```

#### TCPConnectOptions

TCPSocket连接的参数。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明address[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)否否绑定的地址以及端口。timeoutnumber否是超时时间，单位毫秒（ms）。默认值为5000。proxy18+[ProxyOptions](#ZH-CN_TOPIC_0000002497445470__proxyoptions18)否是使用的代理信息，默认不使用代理。

#### TCPSendOptions

TCPSocket发送请求的参数。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明datastring| ArrayBuffer否否发送的数据。encodingstring否是字符编码(UTF-8，UTF-16BE，UTF-16LE，UTF-16，US-AECII，ISO-8859-1)，默认为UTF-8。

#### TCPExtraOptions

TCPSocket连接的其他属性。继承自[ExtraOptionsBase](#ZH-CN_TOPIC_0000002497445470__extraoptionsbase7)。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明keepAliveboolean否是是否保持连接。默认为false。true：保持连接；false：断开连接。OOBInlineboolean否是是否为OOB内联。默认为false。true：是OOB内联；false：不是OOB内联。TCPNoDelayboolean否是TCPSocket连接是否无时延。默认为false。true：无时延；false：有时延。socketLinger{on:boolean, linger:number}否是

socket是否继续逗留。

- on：是否逗留（true：逗留；false：不逗留）。

- linger：逗留时长，单位毫秒（ms），取值范围为0~65535。

当入参on设置为true时，才需要设置。

#### socket.constructTCPSocketServerInstance10+

constructTCPSocketServerInstance(): TCPSocketServer

创建一个TCPSocketServer对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明[TCPSocketServer](#ZH-CN_TOPIC_0000002497445470__tcpsocketserver10)返回一个TCPSocketServer对象。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
```

#### TCPSocketServer10+

TCPSocketServer连接。在调用TCPSocketServer的方法前，需要先通过[socket.constructTCPSocketServerInstance](#ZH-CN_TOPIC_0000002497445470__socketconstructtcpsocketserverinstance10)创建TCPSocketServer对象。

#### listen10+

listen(address: NetAddress, callback: AsyncCallback<void>): void

绑定IP地址和端口，端口可以指定或由系统随机分配。监听并接受与此套接字建立的TCPSocket连接。该接口使用多线程并发处理客户端的数据。使用callback方法作为异步方法。

服务端使用该方法完成bind，listen，accept操作，bind方法失败会由系统随机分配端口号。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明address[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)是目标地址信息。callbackAsyncCallback<void>是回调函数。失败时返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2300002System internal error.2303109Bad file number.2303111Resource temporarily unavailable. Try again.2303198Address already in use.2303199Cannot assign requested address.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
})
```

#### listen10+

listen(address: NetAddress): Promise<void>

绑定IP地址和端口，端口可以指定或由系统随机分配。监听并接受与此套接字建立的TCPSocket连接。该接口使用多线程并发处理客户端的数据。使用Promise方法作为异步方法。

服务端使用该方法完成bind，listen，accept操作，bind方法失败会由系统随机分配端口号。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明address[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)是目标地址信息。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2300002System internal error.2303109Bad file number.2303111Resource temporarily unavailable. Try again.2303198Address already in use.2303199Cannot assign requested address.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr).then(() => {
  console.info('listen success');
}).catch((err: BusinessError) => {
  console.error('listen fail');
});
```

#### getState10+

getState(callback: AsyncCallback<SocketStateBase>): void

获取TCPSocketServer状态。使用callback方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<[SocketStateBase](#ZH-CN_TOPIC_0000002497445470__socketstatebase)>是回调函数。失败时返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2300002System internal error.2303188Socket operation on non-socket.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
})
tcpServer.getState((err: BusinessError, data: socket.SocketStateBase) => {
  if (err) {
    console.error('getState fail');
    return;
  }
  console.info('getState success:' + JSON.stringify(data));
})
```

#### getState10+

getState(): Promise<SocketStateBase>

获取TCPSocketServer状态。使用Promise方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[SocketStateBase](#ZH-CN_TOPIC_0000002497445470__socketstatebase)>以Promise形式返回获取TCPSocket状态的结果。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission denied.2300002System internal error.2303188Socket operation on non-socket.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
})
tcpServer.getState().then((data: socket.SocketStateBase) => {
  console.info('getState success' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error('getState fail');
});
```

#### setExtraOptions10+

setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void

设置TCPSocketServer连接的其他属性。使用callback方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[TCPExtraOptions](#ZH-CN_TOPIC_0000002497445470__tcpextraoptions)是TCPSocketServer连接的其他属性。callbackAsyncCallback<void>是回调函数。失败时返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2300002System internal error.2303188Socket operation on non-socket.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
})

interface SocketLinger {
  on: boolean;
  linger: number;
}

let tcpExtraOptions: socket.TCPExtraOptions = {
  keepAlive: true,
  OOBInline: true,
  TCPNoDelay: true,
  socketLinger: { on: true, linger: 10 } as SocketLinger,
  receiveBufferSize: 8192,
  sendBufferSize: 8192,
  reuseAddress: true,
  socketTimeout: 3000
}
tcpServer.setExtraOptions(tcpExtraOptions, (err: BusinessError) => {
  if (err) {
    console.error('setExtraOptions fail');
    return;
  }
  console.info('setExtraOptions success');
});
```

#### setExtraOptions10+

setExtraOptions(options: TCPExtraOptions): Promise<void>

设置TCPSocketServer连接的其他属性。使用Promise方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[TCPExtraOptions](#ZH-CN_TOPIC_0000002497445470__tcpextraoptions)是TCPSocketServer连接的其他属性。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2300002System internal error.2303188Socket operation on non-socket.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}

interface SocketLinger {
  on: boolean;
  linger: number;
}

tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
})

let tcpExtraOptions: socket.TCPExtraOptions = {
  keepAlive: true,
  OOBInline: true,
  TCPNoDelay: true,
  socketLinger: { on: true, linger: 10 } as SocketLinger,
  receiveBufferSize: 8192,
  sendBufferSize: 8192,
  reuseAddress: true,
  socketTimeout: 3000
}
tcpServer.setExtraOptions(tcpExtraOptions).then(() => {
  console.info('setExtraOptions success');
}).catch((err: BusinessError) => {
  console.error('setExtraOptions fail');
});
```

#### getLocalAddress12+

getLocalAddress(): Promise<NetAddress>

获取TCPSocketServer的本地Socket地址。使用Promise方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)>以Promise形式返回获取本地socket地址的结果。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)。

错误码ID错误信息2300002System internal error.2301009Bad file descriptor.2303188Socket operation on non-socket.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr).then(() => {
  tcpServer.getLocalAddress().then((localAddress: socket.NetAddress) => {
    console.info("SUCCESS! Address:" + JSON.stringify(localAddress));
  }).catch((err: BusinessError) => {
    console.error("FerrorAILED! Error:" + JSON.stringify(err));
  })
}).catch((err: BusinessError) => {
  console.error('listen fail');
});
```

#### on('connect')10+

on(type: 'connect', callback: Callback<TCPSocketConnection>): void

订阅TCPSocketServer的连接事件。使用callback方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'connect'：连接事件。callbackCallback<[TCPSocketConnection](#ZH-CN_TOPIC_0000002497445470__tcpsocketconnection10)>是回调函数。失败时返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
  tcpServer.on('connect', (data: socket.TCPSocketConnection) => {
    console.info(JSON.stringify(data))
  });
})
```

#### off('connect')10+

off(type: 'connect', callback?: Callback<TCPSocketConnection>): void

取消订阅TCPSocketServer的连接事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'connect'：连接事件。callbackCallback<[TCPSocketConnection](#ZH-CN_TOPIC_0000002497445470__tcpsocketconnection10)>否回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
  let callback = (data: socket.TCPSocketConnection) => {
    console.info('on connect message: ' + JSON.stringify(data));
  }
  tcpServer.on('connect', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  tcpServer.off('connect', callback);
  tcpServer.off('connect');
})
```

#### on('error')10+

on(type: 'error', callback: ErrorCallback): void

订阅TCPSocketServer连接的error事件。使用callback方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'error'：error事件。callbackErrorCallback是回调函数。失败时返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
  tcpServer.on('error', (err: BusinessError) => {
    console.error("on error, err:" + JSON.stringify(err))
  });
})
```

#### off('error')10+

off(type: 'error', callback?: ErrorCallback): void

取消订阅TCPSocketServer连接的error事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'error'：error事件。callbackErrorCallback否回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
  let callback = (err: BusinessError) => {
    console.error("on error, err:" + JSON.stringify(err));
  }
  tcpServer.on('error', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  tcpServer.off('error', callback);
  tcpServer.off('error');
})
```

#### close20+

close(): Promise<void>

TCPSocketServer停止监听并释放通过[listen](#ZH-CN_TOPIC_0000002497445470__listen10)方法绑定的端口。若多次调用[listen](#ZH-CN_TOPIC_0000002497445470__listen10)方法，再调用此方法时会释放TCPSocketServer的所有监听端口。使用Promise异步回调。

该方法不会关闭已有连接。如需关闭，请调用[TCPSocketConnection](#ZH-CN_TOPIC_0000002497445470__tcpsocketconnection10)的[close](#ZH-CN_TOPIC_0000002497445470__close10)方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission denied.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.on('connect', (connection: socket.TCPSocketConnection) => {
  console.info("connection clientId: " + connection.clientId);
  // 逻辑处理
  tcpServer.close(); // 停止监听
  connection.close(); // 关闭当前连接
});
tcpServer.listen(listenAddr).then(() => {
  console.info('listen success');
}).catch((err: BusinessError) => {
  console.error('listen fail: ' + err.code);
});
```

#### TCPSocketConnection10+

TCPSocketConnection连接，即TCPSocket客户端与服务端的连接。在调用TCPSocketConnection的方法前，需要先获取TCPSocketConnection对象。

客户端与服务端成功建立连接后，才能通过返回的TCPSocketConnection对象调用相应的接口。

**系统能力**：SystemCapability.Communication.NetStack

#### 属性

名称类型只读可选说明clientIdnumber否否客户端与TCPSocketServer建立连接的id。

#### send10+

send(options: TCPSendOptions, callback: AsyncCallback<void>): void

通过TCPSocketConnection连接发送数据。使用callback方式作为异步方法。

与客户端建立连接后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[TCPSendOptions](#ZH-CN_TOPIC_0000002497445470__tcpsendoptions)是TCPSocketConnection发送请求的参数。callbackAsyncCallback<void>是回调函数。失败时返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  let tcpSendOption: socket.TCPSendOptions = {
    data: 'Hello, client!'
  }
  client.send(tcpSendOption, () => {
    console.info('send success');
  });
});
```

#### send10+

send(options: TCPSendOptions): Promise<void>

通过TCPSocketConnection连接发送数据。使用Promise方式作为异步方法。

与客户端建立连接后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[TCPSendOptions](#ZH-CN_TOPIC_0000002497445470__tcpsendoptions)是TCPSocketConnection发送请求的参数。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  let tcpSendOption: socket.TCPSendOptions = {
    data: 'Hello, client!'
  }
  client.send(tcpSendOption).then(() => {
    console.info('send success');
  }).catch((err: BusinessError) => {
    console.error('send fail');
  });
});
```

#### close10+

close(callback: AsyncCallback<void>): void

关闭一个与TCPSocket建立的连接。使用callback方式作为异步方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。失败时返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.close((err: BusinessError) => {
    if (err) {
      console.error('close fail');
      return;
    }
    console.info('close success');
  });
});
```

#### close10+

close(): Promise<void>

关闭一个与TCPSocket建立的连接。使用Promise方式作为异步方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission denied.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.close().then(() => {
    console.info('close success');
  }).catch((err: BusinessError) => {
    console.error('close fail');
  });
});
```

#### getRemoteAddress10+

getRemoteAddress(callback: AsyncCallback<NetAddress>): void

获取对端Socket地址。使用callback方式作为异步方法。

与客户端建立连接后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)>是回调函数。失败时返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2300002System internal error.2303188Socket operation on non-socket.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.getRemoteAddress((err: BusinessError, data: socket.NetAddress) => {
    if (err) {
      console.error('getRemoteAddress fail');
      return;
    }
    console.info('getRemoteAddress success:' + JSON.stringify(data));
  });
});
```

#### getRemoteAddress10+

getRemoteAddress(): Promise<NetAddress>

获取对端Socket地址。使用Promise方式作为异步方法。

与客户端建立连接后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)>以Promise形式返回获取对端socket地址的结果。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission denied.2300002System internal error.2303188Socket operation on non-socket.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.getRemoteAddress().then(() => {
    console.info('getRemoteAddress success');
  }).catch((err: BusinessError) => {
    console.error('getRemoteAddress fail');
  });
});
```

#### getLocalAddress12+

getLocalAddress(): Promise<NetAddress>

获取TCPSocketConnection连接的本地Socket地址。使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)>以Promise形式返回获取本地socket地址的结果。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)。

错误码ID错误信息2300002System internal error.2301009Bad file descriptor.2303188Socket operation on non-socket.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address: "192.168.xx.xx",
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
  let netAddress: socket.NetAddress = {
    address: "192.168.xx.xx",
    port: 8080
  }
  let options: socket.TCPConnectOptions = {
    address: netAddress,
    timeout: 6000
  }
  tcp.connect(options, (err: BusinessError) => {
    if (err) {
      console.error('connect fail');
      return;
    }
    console.info('connect success!');
  })
  tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
    client.getLocalAddress().then((localAddress: socket.NetAddress) => {
      console.info("Family IP Port: " + JSON.stringify(localAddress));
    }).catch((err: BusinessError) => {
      console.error('Error:' + JSON.stringify(err));
    });
  })
})
```

#### on('message')10+

on(type: 'message', callback: Callback<SocketMessageInfo>): void

订阅TCPSocketConnection连接的接收消息事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'message'：接收消息事件。callbackCallback<[SocketMessageInfo](#ZH-CN_TOPIC_0000002497445470__socketmessageinfo11)>是回调函数。失败时返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.on('message', (value: socket.SocketMessageInfo) => {
    let messageView = '';
    let uint8Array = new Uint8Array(value.message);
    for (let i: number = 0; i < value.message.byteLength; i++) {
      let messages = uint8Array[i];
      let message = String.fromCharCode(messages);
      messageView += message;
    }
    console.info('on message message: ' + JSON.stringify(messageView));
    console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
  });
});
```

#### off('message')10+

off(type: 'message', callback?: Callback<SocketMessageInfo>): void

取消订阅TCPSocketConnection连接的接收消息事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'message'：接收消息事件。callbackCallback<[SocketMessageInfo](#ZH-CN_TOPIC_0000002497445470__socketmessageinfo11)>否回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let callback = (value: socket.SocketMessageInfo) => {
  let messageView = '';
  for (let i: number = 0; i < value.message.byteLength; i++) {
    let uint8Array = new Uint8Array(value.message)
    let messages = uint8Array[i]
    let message = String.fromCharCode(messages);
    messageView += message;
  }
  console.info('on message message: ' + JSON.stringify(messageView));
  console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
}
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.on('message', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  client.off('message', callback);
  client.off('message');
});
```

#### on('close')10+

on(type: 'close', callback: Callback<void>): void

订阅TCPSocketConnection的关闭事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'close'：关闭事件。callbackCallback<void>是回调函数。失败时返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.on('close', () => {
    console.info("on close success")
  });
});
```

#### off('close')10+

off(type: 'close', callback?: Callback<void>): void

取消订阅TCPSocketConnection的关闭事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'close'：关闭事件。callbackCallback<void>否回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let callback = () => {
  console.info("on close success");
}
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.on('close', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  client.off('close', callback);
  client.off('close');
});
```

#### on('error')10+

on(type: 'error', callback: ErrorCallback): void

订阅TCPSocketConnection连接的error事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'error'：error事件。callbackErrorCallback是回调函数。失败时返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.on('error', (err: BusinessError) => {
    console.error("on error, err:" + JSON.stringify(err))
  });
});
```

#### off('error')10+

off(type: 'error', callback?: ErrorCallback): void

取消订阅TCPSocketConnection连接的error事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'error'：error事件。callbackErrorCallback否回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let callback = (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err));
}
let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.on('error', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  client.off('error', callback);
  client.off('error');
});
```

#### TCP 错误码说明

TCP 其余错误码映射形式为：2301000 + Linux内核错误码。

错误码的详细介绍参见[Socket错误码](SOCKET 错误码.md)。

#### socket.constructLocalSocketInstance11+

constructLocalSocketInstance(): LocalSocket

创建一个LocalSocket对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明[LocalSocket](#ZH-CN_TOPIC_0000002497445470__localsocket11)返回一个LocalSocket对象。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
let client: socket.LocalSocket = socket.constructLocalSocketInstance();
```

#### LocalSocket11+

LocalSocket连接。在调用LocalSocket的方法前，需要先通过[socket.constructLocalSocketInstance](#ZH-CN_TOPIC_0000002497445470__socketconstructlocalsocketinstance11)创建LocalSocket对象。

#### bind11+

bind(address: LocalAddress): Promise<void>;

绑定本地套接字文件的路径。使用promise方法作为异步方法。

bind方法可以使客户端确保有个明确的本地套接字路径，显式的绑定一个本地套接字文件。

bind方法在本地套接字通信中非必须。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明address[LocalAddress](#ZH-CN_TOPIC_0000002497445470__localaddress11)是本端地址信息，参考[LocalAddress](#ZH-CN_TOPIC_0000002497445470__localaddress11)。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2301013Insufficient permissions.2301022Invalid argument.2301098Address already in use.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance()
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let address : socket.LocalAddress = {
  address: sandboxPath
}
client.bind(address).then(() => {
  console.info('bind success')
}).catch((err: Object) => {
  console.error('failed to bind: ' + JSON.stringify(err))
})
```

#### connect11+

connect(options: LocalConnectOptions): Promise<void>

连接到指定的套接字文件。使用promise方法作为异步方法。

在没有执行localsocket.bind的情况下，也可以直接调用该接口完成与LocalSocket服务端的连接。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[LocalConnectOptions](#ZH-CN_TOPIC_0000002497445470__localconnectoptions11)是LocalSocket连接的参数，参考[LocalConnectOptions](#ZH-CN_TOPIC_0000002497445470__localconnectoptions11)。

**返回值：**

类型说明Promise<void>以Promise形式返回LocalSocket连接服务端的结果。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2301013Insufficient permissions.2301022Invalid argument.2301111Connection refused.2301099Cannot assign requested address.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let localAddress : socket.LocalAddress = {
  address: sandboxPath
}
let connectOpt: socket.LocalConnectOptions = {
  address: localAddress,
  timeout: 6000
}
client.connect(connectOpt).then(() => {
  console.info('connect success')
}).catch((err: Object) => {
  console.error('connect fail: ' + JSON.stringify(err));
});
```

#### send11+

send(options: LocalSendOptions): Promise<void>

通过LocalSocket连接发送数据。使用Promise方式作为异步方法。

connect方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[LocalSendOptions](#ZH-CN_TOPIC_0000002497445470__localsendoptions11)是LocalSocket发送请求的参数，参考[LocalSendOptions](#ZH-CN_TOPIC_0000002497445470__localsendoptions11)。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2301011Operation would block.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance()
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let localAddress : socket.LocalAddress = {
  address: sandboxPath
}
let connectOpt: socket.LocalConnectOptions = {
  address: localAddress,
  timeout: 6000
}
client.connect(connectOpt).then(() => {
  console.info('connect success')
}).catch((err: Object) => {
  console.error('connect failed: ' + JSON.stringify(err))
})
let sendOpt: socket.LocalSendOptions = {
  data: 'Hello world!'
}
client.send(sendOpt).then(() => {
  console.info('send success')
}).catch((err: Object) => {
  console.error('send fail: ' + JSON.stringify(err))
})
```

#### close11+

close(): Promise<void>

关闭LocalSocket连接。使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)。

错误码ID错误信息2301009Bad file descriptor.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();

client.close().then(() => {
  console.info('close success');
}).catch((err: Object) => {
  console.error('close fail: ' + JSON.stringify(err));
});
```

#### getState11+

getState(): Promise<SocketStateBase>

获取LocalSocket状态。使用Promise方式作为异步方法。

bind或connect方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[SocketStateBase](#ZH-CN_TOPIC_0000002497445470__socketstatebase)>以Promise形式返回获取LocalSocket状态的结果。

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let localAddress : socket.LocalAddress = {
  address: sandboxPath
}
let connectOpt: socket.LocalConnectOptions = {
  address: localAddress,
  timeout: 6000
}
client.connect(connectOpt).then(() => {
  console.info('connect success');
  client.getState().then(() => {
    console.info('getState success');
  }).catch((err: Object) => {
    console.error('getState fail: ' + JSON.stringify(err))
  });
}).catch((err: Object) => {
  console.error('connect fail: ' + JSON.stringify(err));
});
```

#### getSocketFd11+

getSocketFd(): Promise<number>

获取LocalSocket的文件描述符。使用Promise方式作为异步方法。

bind或connect方法调用成功后，才可调用此方法。

获取由系统内核分配的唯一文件描述符，用于标识当前使用的套接字。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<number>以Promise形式返回socket的文件描述符。

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let localAddress : socket.LocalAddress = {
  address: sandboxPath
}
let connectOpt: socket.LocalConnectOptions = {
  address: localAddress,
  timeout: 6000
}
client.connect(connectOpt).then(() => {
  console.info('connect ok')
}).catch((err: Object) => {
  console.error('connect fail: ' + JSON.stringify(err))
})
client.getSocketFd().then((data: number) => {
  console.info("fd: " + data);
}).catch((err: Object) => {
  console.error("getSocketFd faile: " + JSON.stringify(err));
})
```

#### setExtraOptions11+

setExtraOptions(options: ExtraOptionsBase): Promise<void>

设置LocalSocket的套接字属性。使用Promise方式作为异步方法。

bind或connect方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[ExtraOptionsBase](#ZH-CN_TOPIC_0000002497445470__extraoptionsbase7)是LocalSocket连接的其他属性，参考[ExtraOptionsBase](#ZH-CN_TOPIC_0000002497445470__extraoptionsbase7)。

**返回值：**

类型说明Promise<void>以Promise形式返回设置LocalSocket套接字属性的结果。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2301009Bad file descriptor.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let localAddress : socket.LocalAddress = {
  address: sandboxPath
}
let connectOpt: socket.LocalConnectOptions = {
  address: localAddress,
  timeout: 6000
}
client.connect(connectOpt).then(() => {
  console.info('connect success');
  let options: socket.ExtraOptionsBase = {
    receiveBufferSize: 8192,
    sendBufferSize: 8192,
    socketTimeout: 3000
  }
  client.setExtraOptions(options).then(() => {
    console.info('setExtraOptions success');
  }).catch((err: Object) => {
    console.error('setExtraOptions fail: ' + JSON.stringify(err));
  });
}).catch((err: Object) => {
  console.error('connect fail: ' + JSON.stringify(err));
});
```

#### getExtraOptions11+

getExtraOptions(): Promise<ExtraOptionsBase>;

获取LocalSocket的套接字属性。使用Promise方式作为异步方法。

bind或connect方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[ExtraOptionsBase](#ZH-CN_TOPIC_0000002497445470__extraoptionsbase7)>以Promise形式返回设置LocalSocket套接字的属性。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)。

错误码ID错误信息2301009Bad file descriptor.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let localAddress : socket.LocalAddress = {
  address: sandboxPath
}
let connectOpt: socket.LocalConnectOptions = {
  address: localAddress,
  timeout: 6000
}
client.connect(connectOpt).then(() => {
  console.info('connect success');
  client.getExtraOptions().then((options : socket.ExtraOptionsBase) => {
    console.info('options: ' + JSON.stringify(options));
  }).catch((err: Object) => {
    console.error('setExtraOptions fail: ' + JSON.stringify(err));
  });
}).catch((err: Object) => {
  console.error('connect fail: ' + JSON.stringify(err));
});
```

#### getLocalAddress12+

getLocalAddress(): Promise<string>

获取LocalSocket的本地Socket地址。使用Promise方式作为异步方法。

bind方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<string>以Promise形式返回获取本地socket地址的结果。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)。

错误码ID错误信息2300002System internal error.2301009Bad file descriptor.2303188Socket operation on non-socket.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { common } from '@kit.AbilityKit';
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let address : socket.LocalAddress = {
  address: sandboxPath
}
client.bind(address).then(() => {
  console.error('bind success');
  client.getLocalAddress().then((localPath: string) => {
    console.info("SUCCESS " + JSON.stringify(localPath));
  }).catch((err: BusinessError) => {
    console.error("FAIL " + JSON.stringify(err));
  })
}).catch((err: Object) => {
  console.error('failed to bind: ' + JSON.stringify(err));
})
```

#### on('message')11+

on(type: 'message', callback: Callback<LocalSocketMessageInfo>): void

订阅LocalSocket连接的接收消息事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'message'：接收消息事件。callbackCallback<[LocalSocketMessageInfo](#ZH-CN_TOPIC_0000002497445470__localsocketmessageinfo11)>是以callback的形式异步返回接收的消息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
client.on('message', (value: socket.LocalSocketMessageInfo) => {
  const uintArray = new Uint8Array(value.message)
  let messageView = '';
  for (let i = 0; i < uintArray.length; i++) {
    messageView += String.fromCharCode(uintArray[i]);
  }
  console.info('total: ' + JSON.stringify(value));
  console.info('message infomation: ' + messageView);
});
```

#### off('message')11+

off(type: 'message', callback?: Callback<LocalSocketMessageInfo>): void

取消订阅LocalSocket连接的接收消息事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'message'：接收消息事件。callbackCallback<[LocalSocketMessageInfo](#ZH-CN_TOPIC_0000002497445470__localsocketmessageinfo11)>否回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let messageView = '';
let callback = (value: socket.LocalSocketMessageInfo) => {
  const uintArray = new Uint8Array(value.message)
  let messageView = '';
  for (let i = 0; i < uintArray.length; i++) {
    messageView += String.fromCharCode(uintArray[i]);
  }
  console.info('total: ' + JSON.stringify(value));
  console.info('message infomation: ' + messageView);
}
client.on('message', callback);
client.off('message');
```

#### on('connect')11+

on(type: 'connect', callback: Callback<void>): void

订阅LocalSocket的连接事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。callbackCallback<void>是以callback的形式异步返回与服务端连接的结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
client.on('connect', () => {
  console.info("on connect success")
});
```

#### off('connect')11+

off(type: 'connect', callback?: Callback<void>): void

取消订阅LocalSocket的连接事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'connect'：LocalSocket的connect事件。callbackCallback<void>否回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let callback = () => {
  console.info("on connect success");
}
client.on('connect', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
client.off('connect', callback);
client.off('connect');
```

#### on('close')11+

on(type: 'close', callback: Callback<void>): void

订阅LocalSocket的关闭事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅LocalSocket的关闭事件。callbackCallback<void>是以callback的形式异步返回关闭localsocket的结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let callback = () => {
  console.info("on close success");
}
client.on('close', callback);
```

#### off('close')11+

off(type: 'close', callback?: Callback<void>): void

取消订阅LocalSocket的关闭事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'close'：LocalSocket的关闭事件。callbackCallback<void>否回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let callback = () => {
  console.info("on close success");
}
client.on('close', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
client.off('close', callback);
client.off('close');
```

#### on('error')11+

on(type: 'error', callback: ErrorCallback): void

订阅LocalSocket连接的error事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅LocalSocket的error事件。callbackErrorCallback是以callback的形式异步返回出现错误的结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
client.on('error', (err: Object) => {
  console.error("on error, err:" + JSON.stringify(err))
});
```

#### off('error')11+

off(type: 'error', callback?: ErrorCallback): void

取消订阅LocalSocket连接的error事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'error'：LocalSocket的error事件。callbackErrorCallback否回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let callback = (err: Object) => {
  console.error("on error, err:" + JSON.stringify(err));
}
client.on('error', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
client.off('error', callback);
client.off('error');
```

#### LocalSocketMessageInfo11+

LocalSocket客户端与服务端通信时接收的数据。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明messageArrayBuffer否否收到的消息数据。addressstring否否使用的本地套接字路径。sizenumber否否数据长度。

#### LocalAddress11+

LocalSocket本地套接字文件路径信息，在传入套接字路径进行绑定时，会在此路径下创建套接字文件。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明addressstring否否本地套接字路径。

#### LocalConnectOptions11+

LocalSocket客户端在连接服务端时传入的参数信息。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明address[LocalAddress](#ZH-CN_TOPIC_0000002497445470__localaddress11)否否指定的本地套接字路径。timeoutnumber否是连接服务端的超时时间，单位为毫秒。默认值为0。需要应用手动设置一下，建议设置为5000。

#### LocalSendOptions11+

LocalSocket发送请求的参数。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明datastring | ArrayBuffer否否需要发送的数据。encodingstring否是字符编码。

#### ExtraOptionsBase7+

Socket套接字的基础属性。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明receiveBufferSizenumber否是接收缓冲区大小（单位：Byte），取值范围0~262144，不设置或设置的值超过取值范围则会默认为8192。sendBufferSizenumber否是发送缓冲区大小（单位：Byte），取值范围0~262144，不设置或设置的值超过取值范围则会默认为8192。reuseAddressboolean否是是否重用地址。true：重用地址；false：不重用地址。socketTimeoutnumber否是套接字超时时间，单位毫秒（ms）。

#### socket.constructLocalSocketServerInstance11+

constructLocalSocketServerInstance(): LocalSocketServer

创建一个LocalSocketServer对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明[LocalSocketServer](#ZH-CN_TOPIC_0000002497445470__localsocketserver11)返回一个LocalSocketServer对象。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
```

#### LocalSocketServer11+

LocalSocketServer类。在调用LocalSocketServer的方法前，需要先通过[socket.constructLocalSocketServerInstance](#ZH-CN_TOPIC_0000002497445470__socketconstructlocalsocketserverinstance11)创建LocalSocketServer对象。

#### listen11+

listen(address: LocalAddress): Promise<void>

绑定本地套接字文件，监听并接受与此套接字建立的LocalSocket连接。该接口使用多线程并发处理客户端的数据。使用Promise方法作为异步方法。

服务端使用该方法完成bind，listen，accept操作，传入套接字文件路径，调用此接口后会自动生成本地套接字文件。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明address[LocalAddress](#ZH-CN_TOPIC_0000002497445470__localaddress11)是目标地址信息。

**返回值：**

类型说明Promise<void>以Promise形式返回执行结果， 成功返回空，失败返回错误码错误信息。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2303109Bad file number.2301013Insufficient permissions.2301022Invalid argument.2301098Address already in use.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let addr: socket.LocalAddress = {
  address: sandboxPath
}
server.listen(addr).then(() => {
  console.info('listen success');
}).catch((err: Object) => {
  console.error('listen fail: ' + JSON.stringify(err));
});
```

#### getState11+

getState(): Promise<SocketStateBase>

获取LocalSocketServer状态。使用Promise方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[SocketStateBase](#ZH-CN_TOPIC_0000002497445470__socketstatebase)>以Promise形式返回获取LocalSocketServer状态的结果。

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let listenAddr: socket.LocalAddress = {
  address: sandboxPath
}
server.listen(listenAddr).then(() => {
  console.info("listen success");
}).catch((err: Object) => {
  console.error("listen fail: " + JSON.stringify(err));
})
server.getState().then((data: socket.SocketStateBase) => {
  console.info('getState success: ' + JSON.stringify(data));
}).catch((err: Object) => {
  console.error('getState fail: ' + JSON.stringify(err));
});
```

#### setExtraOptions11+

setExtraOptions(options: ExtraOptionsBase): Promise<void>

设置LocalSocketServer连接的套接字属性。使用Promise方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[ExtraOptionsBase](#ZH-CN_TOPIC_0000002497445470__extraoptionsbase7)是LocalSocketServer连接的其他属性。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2301009Bad file descriptor.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let listenAddr: socket.NetAddress = {
  address: sandboxPath
}
server.listen(listenAddr).then(() => {
  console.info("listen success");
}).catch((err: Object) => {
  console.error("listen fail: " + JSON.stringify(err));
})

let options: socket.ExtraOptionsBase = {
  receiveBufferSize: 8192,
  sendBufferSize: 8192,
  socketTimeout: 3000
}
server.setExtraOptions(options).then(() => {
  console.info('setExtraOptions success');
}).catch((err: Object) => {
  console.error('setExtraOptions fail: ' + JSON.stringify(err));
});
```

#### getExtraOptions11+

getExtraOptions(): Promise<ExtraOptionsBase>;

获取LocalSocketServer中连接的套接字的属性。使用Promise方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[ExtraOptionsBase](#ZH-CN_TOPIC_0000002497445470__extraoptionsbase7)>以Promise形式返回套接字的属性。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let listenAddr: socket.LocalAddress = {
  address: sandboxPath
}
server.listen(listenAddr).then(() => {
  console.info("listen success");
}).catch((err: Object) => {
  console.error("listen fail: " + JSON.stringify(err));
})
server.getExtraOptions().then((options: socket.ExtraOptionsBase) => {
  console.info('options: ' + JSON.stringify(options));
}).catch((err: Object) => {
  console.error('getExtraOptions fail: ' + JSON.stringify(err));
});
```

#### getLocalAddress12+

getLocalAddress(): Promise<string>

获取LocalSocketServer中本地Socket地址。使用Promise方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<string>以Promise形式返回获取本地socket地址的结果。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)。

错误码ID错误信息2300002System internal error.2301009Bad file descriptor.2303188Socket operation on non-socket.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { common } from '@kit.AbilityKit';
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let listenAddr: socket.LocalAddress = {
  address: sandboxPath
}
server.listen(listenAddr).then(() => {
  console.info("listen success");
  server.getLocalAddress().then((localPath: string) => {
    console.info("SUCCESS " + JSON.stringify(localPath));
  }).catch((err: BusinessError) => {
    console.error("FAIL " + JSON.stringify(err));
  })
}).catch((err: Object) => {
  console.error("listen fail: " + JSON.stringify(err));
})
```

#### on('connect')11+

on(type: 'connect', callback: Callback<LocalSocketConnection>): void

订阅LocalSocketServer的连接事件。使用callback方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'connect'：连接事件。callbackCallback<[LocalSocketConnection](#ZH-CN_TOPIC_0000002497445470__localsocketconnection11)>是以callback的形式异步返回接收到客户端连接的结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
server.on('connect', (connection: socket.LocalSocketConnection) => {
  if (connection) {
    console.info('accept a client')
  }
});
```

#### off('connect')11+

off(type: 'connect', callback?: Callback<LocalSocketConnection>): void

取消订阅LocalSocketServer的连接事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'connect'：LocalSocketServer的连接事件。callbackCallback<[LocalSocketConnection](#ZH-CN_TOPIC_0000002497445470__localsocketconnection11)>否回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let callback = (connection: socket.LocalSocketConnection) => {
  if (connection) {
    console.info('accept a client')
  }
}
server.on('connect', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
server.off('connect', callback);
server.off('connect');
```

#### on('error')11+

on(type: 'error', callback: ErrorCallback): void

订阅LocalSocketServer连接的error事件。使用callback方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'error'：error事件。callbackErrorCallback是以callback的形式异步返回出现错误的结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
server.on('error', (err: Object) => {
  console.error("on error, err:" + JSON.stringify(err))
});
```

#### off('error')11+

off(type: 'error', callback?: ErrorCallback): void

取消订阅LocalSocketServer连接的error事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'error'：error事件。callbackErrorCallback否回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let callback = (err: Object) => {
  console.error("on error, err:" + JSON.stringify(err));
}
server.on('error', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
server.off('error', callback);
server.off('error');
```

#### close20+

close(): Promise<void>

LocalSocketServer停止监听并释放通过[listen](#ZH-CN_TOPIC_0000002497445470__listen11)方法绑定的监听端口。使用Promise异步回调。

该方法不会关闭已有连接。如需关闭，请调用[LocalSocketConnection](#ZH-CN_TOPIC_0000002497445470__localsocketconnection11)的[close](#ZH-CN_TOPIC_0000002497445470__close11-1)方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)。

错误码ID错误信息2300002System internal error.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localserver: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let addr: socket.LocalAddress = {
  address: sandboxPath
}
localserver.on('connect', (connection: socket.LocalSocketConnection) => {
  console.info("connection clientId: " + connection.clientId);
  // 逻辑处理
  localserver.close(); // 停止监听
  connection.close(); // 关闭当前连接
});
localserver.listen(addr).then(() => {
  console.info('listen success');
}).catch((err: BusinessError) => {
  console.error('listen fail: ' + err.code);
});
```

#### LocalSocketConnection11+

LocalSocketConnection连接，即LocalSocket客户端与服务端的会话连接。在调用LocalSocketConnection的方法前，需要先获取LocalSocketConnection对象。

客户端与服务端成功建立连接后，才能通过返回的LocalSocketConnection对象调用相应的接口。

**系统能力**：SystemCapability.Communication.NetStack

#### 属性

名称类型只读可选说明clientIdnumber否否客户端与服务端建立的会话连接的id。

#### send11+

send(options: LocalSendOptions): Promise<void>

通过LocalSocketConnection连接对象发送数据。使用Promise方式作为异步方法。

服务端与客户端建立连接后，服务端通过connect事件回调得到LocalSocketConnection连接对象后，才可使用连接对象调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[LocalSendOptions](#ZH-CN_TOPIC_0000002497445470__localsendoptions11)是LocalSocketConnection发送请求的参数。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2301011Operation would block.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();

server.on('connect', (connection: socket.LocalSocketConnection) => {
  let sendOptions: socket.LocalSendOptions = {
    data: 'Hello, client!'
  }
  connection.send(sendOptions).then(() => {
    console.info('send success');
  }).catch((err: Object) => {
    console.error('send fail: ' + JSON.stringify(err));
  });
});
```

#### close11+

close(): Promise<void>

关闭一个LocalSocket客户端与服务端建立的连接。使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)。

错误码ID错误信息2301009Bad file descriptor.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.close().then(() => {
    console.info('close success');
  }).catch((err: Object) => {
    console.error('close fail: ' + JSON.stringify(err));
  });
});
```

#### getLocalAddress12+

getLocalAddress(): Promise<string>

获取LocalSocketConnection连接中的本地Socket地址。使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<string>以Promise形式返回获取本地socket地址的结果。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)。

错误码ID错误信息2300002System internal error.2301009Bad file descriptor.2303188Socket operation on non-socket.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { common } from '@kit.AbilityKit';
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let localAddr: socket.LocalAddress = {
  address: sandboxPath
}
server.listen(localAddr).then(() => {
  console.info('listen success');
  let client: socket.LocalSocket = socket.constructLocalSocketInstance();
  let connectOpt: socket.LocalConnectOptions = {
    address: localAddr,
    timeout: 6000
  }
  client.connect(connectOpt).then(() => {
    server.getLocalAddress().then((localPath: string) => {
      console.info("success, localPath is" + JSON.stringify(localPath));
    }).catch((err: BusinessError) => {
      console.error("FAIL " + JSON.stringify(err));
    })
  }).catch((err: Object) => {
    console.error('connect fail: ' + JSON.stringify(err));
  });
});
```

#### on('message')11+

on(type: 'message', callback: Callback<LocalSocketMessageInfo>): void

订阅LocalSocketConnection连接的接收消息事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'message'：接收消息事件。callbackCallback<[LocalSocketMessageInfo](#ZH-CN_TOPIC_0000002497445470__localsocketmessageinfo11)>是以callback的形式异步返回接收到的来自客户端的消息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let listenAddr: socket.LocalAddress = {
  address: sandboxPath
}
server.listen(listenAddr).then(() => {
  console.info("listen success");
}).catch((err: Object) => {
  console.error("listen fail: " + JSON.stringify(err));
});
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.on('message', (value: socket.LocalSocketMessageInfo) => {
    const uintArray = new Uint8Array(value.message);
    let messageView = '';
    for (let i = 0; i < uintArray.length; i++) {
      messageView += String.fromCharCode(uintArray[i]);
    }
    console.info('total: ' + JSON.stringify(value));
    console.info('message infomation: ' + messageView);
  });
});
```

#### off('message')11+

off(type: 'message', callback?: Callback<LocalSocketMessageInfo>): void

取消订阅LocalSocketConnection连接的接收消息事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'message'：接收消息事件。callbackCallback<[LocalSocketMessageInfo](#ZH-CN_TOPIC_0000002497445470__localsocketmessageinfo11)>否回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let callback = (value: socket.LocalSocketMessageInfo) => {
  const uintArray = new Uint8Array(value.message)
  let messageView = '';
  for (let i = 0; i < uintArray.length; i++) {
    messageView += String.fromCharCode(uintArray[i]);
  }
  console.info('total: ' + JSON.stringify(value));
  console.info('message infomation: ' + messageView);
}
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.on('message', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  connection.off('message', callback);
  connection.off('message');
});
```

#### on('close')11+

on(type: 'close', callback: Callback<void>): void

订阅LocalSocketConnection的关闭事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'close'：关闭事件。callbackCallback<void>是以callback的形式异步返回会话关闭的结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.on('close', () => {
    console.info("on close success")
  });
});
```

#### off('close')11+

off(type: 'close', callback?: Callback<void>): void

取消订阅LocalSocketConnection的关闭事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'close'：关闭事件。callbackCallback<void>否回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let callback = () => {
  console.info("on close success");
}
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.on('close', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  connection.off('close', callback);
  connection.off('close');
});
```

#### on('error')11+

on(type: 'error', callback: ErrorCallback): void

订阅LocalSocketConnection连接的error事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'error'：error事件。callbackErrorCallback是以callback的形式异步返回出现错误的结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.on('error', (err: Object) => {
    console.error("on error, err:" + JSON.stringify(err))
  });
});
```

#### off('error')11+

off(type: 'error', callback?: ErrorCallback): void

取消订阅LocalSocketConnection连接的error事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是取消订阅的事件类型。'error'：error事件。callbackErrorCallback否回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let callback = (err: Object) => {
  console.error("on error, err: " + JSON.stringify(err));
}
let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.on('error', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  connection.off('error', callback);
  connection.off('error');
});
```

#### LocalSocket 错误码说明

LocalSocket 错误码映射形式为：2301000 + Linux内核错误码。

错误码的详细介绍参见[Socket错误码](SOCKET 错误码.md)。

#### socket.constructTLSSocketInstance9+

constructTLSSocketInstance(): TLSSocket

创建并返回一个TLSSocket对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值:**

类型说明[TLSSocket](#ZH-CN_TOPIC_0000002497445470__tlssocket9)返回一个TLSSocket对象。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
```

#### socket.constructTLSSocketInstance12+

constructTLSSocketInstance(tcpSocket: TCPSocket): TLSSocket

将TCPSocket升级为TLSSocket，创建并返回一个TLSSocket对象。

需要确保TCPSocket已连接，并且当前已经没有传输数据，再调用constructTLSSocketInstance升级TLSSocket。当升级成功后，无需对TCPSocket对象调用close方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明tcpSocket[TCPSocket](#ZH-CN_TOPIC_0000002497445470__tcpsocket)是需要进行升级的TCPSocket对象。

**返回值:**

类型说明[TLSSocket](#ZH-CN_TOPIC_0000002497445470__tlssocket9)返回一个TLSSocket对象。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2300002System internal error.2303601Invalid socket FD.2303602Socket is not connected.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}

tcp.connect(tcpconnectoptions, (err: BusinessError) => {
  if (err) {
    console.error('connect fail');
    return;
  }
  console.info('connect success');

  // 确保TCPSocket已连接后，再升级TLSSocket
  let tls: socket.TLSSocket = socket.constructTLSSocketInstance(tcp);
})
```

#### TLSSocket9+

TLSSocket连接。在调用TLSSocket的方法前，需要先通过[socket.constructTLSSocketInstance](#ZH-CN_TOPIC_0000002497445470__socketconstructtlssocketinstance9)创建TLSSocket对象。

#### bind9+

bind(address: NetAddress, callback: AsyncCallback<void>): void

绑定IP地址和端口。使用callback方法作为异步方法。

如果TLSSocket对象是通过TCPSocket对象升级创建的，可以不用执行bind方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明address[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)是本端地址信息，参考[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)。callbackAsyncCallback<void>是回调函数。成功返回TLSSocket绑定本机的IP地址和端口的结果。失败返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2303198Address already in use.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
```

#### bind9+

bind(address: NetAddress): Promise<void>

绑定IP地址和端口。使用Promise方法作为异步方法。

如果TLSSocket对象是通过TCPSocket对象升级创建的，可以不用执行bind方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明address[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)是本端地址信息，参考[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)。

**返回值：**

类型说明Promise<void>以Promise形式返回TLSSocket绑定本机的IP地址和端口的结果。失败返回错误码，错误信息。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.201Permission denied.2303198Address already in use.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr).then(() => {
  console.info('bind success');
}).catch((err: BusinessError) => {
  console.error('bind fail');
});
```

#### getState9+

getState(callback: AsyncCallback<SocketStateBase>): void

在TLSSocket的bind成功之后，获取TLSSocket状态。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<[SocketStateBase](#ZH-CN_TOPIC_0000002497445470__socketstatebase)>是回调函数。成功返回TLSSocket状态，失败返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)。

错误码ID错误信息2303188Socket operation on non-socket.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
tls.getState((err: BusinessError, data: socket.SocketStateBase) => {
  if (err) {
    console.error('getState fail');
    return;
  }
  console.info('getState success:' + JSON.stringify(data));
});
```

#### getState9+

getState(): Promise<SocketStateBase>

在TLSSocket的bind成功之后，获取TLSSocket状态。使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[SocketStateBase](#ZH-CN_TOPIC_0000002497445470__socketstatebase)>以Promise形式返回获取TLSSocket状态的结果。失败返回错误码，错误信息。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)。

错误码ID错误信息2303188Socket operation on non-socket.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
tls.getState().then(() => {
  console.info('getState success');
}).catch((err: BusinessError) => {
  console.error('getState fail');
});
```

#### setExtraOptions9+

setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void

在TLSSocket的bind成功之后，设置TCPSocket连接的其他属性。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[TCPExtraOptions](#ZH-CN_TOPIC_0000002497445470__tcpextraoptions)是TCPSocket连接的其他属性，参考[TCPExtraOptions](#ZH-CN_TOPIC_0000002497445470__tcpextraoptions)。callbackAsyncCallback<void>是回调函数。成功返回设置TCPSocket连接的其他属性的结果，失败返回错误码、错误信息。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2303188Socket operation on non-socket.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});

interface SocketLinger {
  on: boolean;
  linger: number;
}

let tcpExtraOptions: socket.TCPExtraOptions = {
  keepAlive: true,
  OOBInline: true,
  TCPNoDelay: true,
  socketLinger: { on: true, linger: 10 } as SocketLinger,
  receiveBufferSize: 8192,
  sendBufferSize: 8192,
  reuseAddress: true,
  socketTimeout: 3000
}
tls.setExtraOptions(tcpExtraOptions, (err: BusinessError) => {
  if (err) {
    console.error('setExtraOptions fail');
    return;
  }
  console.info('setExtraOptions success');
});
```

#### setExtraOptions9+

setExtraOptions(options: TCPExtraOptions): Promise<void>

在TLSSocket的bind成功之后，设置TCPSocket连接的其他属性。使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[TCPExtraOptions](#ZH-CN_TOPIC_0000002497445470__tcpextraoptions)是TCPSocket连接的其他属性，参考[TCPExtraOptions](#ZH-CN_TOPIC_0000002497445470__tcpextraoptions)。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2303188Socket operation on non-socket.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});

interface SocketLinger {
  on: boolean;
  linger: number;
}

let tcpExtraOptions: socket.TCPExtraOptions = {
  keepAlive: true,
  OOBInline: true,
  TCPNoDelay: true,
  socketLinger: { on: true, linger: 10 } as SocketLinger,
  receiveBufferSize: 8192,
  sendBufferSize: 8192,
  reuseAddress: true,
  socketTimeout: 3000
}
tls.setExtraOptions(tcpExtraOptions).then(() => {
  console.info('setExtraOptions success');
}).catch((err: BusinessError) => {
  console.error('setExtraOptions fail');
});
```

#### on('message')9+

on(type: 'message', callback: Callback<SocketMessageInfo>): void

订阅TLSSocket连接的接收消息事件。使用callback方式作为异步方法。

bind方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'message'：接收消息事件。callbackCallback<[SocketMessageInfo](#ZH-CN_TOPIC_0000002497445470__socketmessageinfo11)>是回调函数。TLSSocket连接订阅某类接受消息事件触发的调用函数，返回TLSSocket连接信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
  tls.on('message', (value: socket.SocketMessageInfo) => {
    let messageView = '';
    let uint8Array = new Uint8Array(value.message);
    for (let i: number = 0; i < value.message.byteLength; i++) {
      let messages = uint8Array[i];
      let message = String.fromCharCode(messages);
      messageView += message;
    }
    console.info('on message message: ' + JSON.stringify(messageView));
    console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
  });
});
```

#### off('message')9+

off(type: 'message', callback?: Callback<SocketMessageInfo>): void

取消订阅TLSSocket连接的接收消息事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'message'：接收消息事件。callbackCallback<[SocketMessageInfo](#ZH-CN_TOPIC_0000002497445470__socketmessageinfo11)>否回调函数。TLSSocket连接取消订阅某类接受消息事件触发的调用函数，返回TLSSocket连接信息。

**错误码：**

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let messageView = '';
let callback = (value: socket.SocketMessageInfo) => {
  for (let i: number = 0; i < value.message.byteLength; i++) {
    let uint8Array = new Uint8Array(value.message)
    let messages = uint8Array[i]
    let message = String.fromCharCode(messages);
    messageView += message;
  }
  console.info('on message message: ' + JSON.stringify(messageView));
  console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
}
tls.on('message', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
tls.off('message', callback);
```

#### on('connect' | 'close')9+

on(type: 'connect' | 'close', callback: Callback<void>): void

订阅TLSSocket的连接事件或关闭事件。使用callback方式作为异步方法。

bind方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是

订阅的事件类型。

- 'connect'：连接事件。

- 'close'：关闭事件。

callbackCallback<void>是回调函数。TLSSocket连接订阅某类事件触发的调用函数。

**错误码：**

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
  tls.on('connect', () => {
    console.info("on connect success")
  });
  tls.on('close', () => {
    console.info("on close success")
  });
});
```

#### off('connect' | 'close')9+

off(type: 'connect' | 'close', callback?: Callback<void>): void

取消订阅TLSSocket的连接事件或关闭事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是

订阅的事件类型。

- 'connect'：连接事件。

- 'close'：关闭事件。

callbackCallback<void>否回调函数。TLSSocket连接订阅某类事件触发的调用函数。

**错误码：**

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let callback1 = () => {
  console.info("on connect success");
}
tls.on('connect', callback1);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
tls.off('connect', callback1);
tls.off('connect');
let callback2 = () => {
  console.info("on close success");
}
tls.on('close', callback2);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
tls.off('close', callback2);
```

#### on('error')9+

on(type: 'error', callback: ErrorCallback): void

订阅TLSSocket连接的error事件。使用callback方式作为异步方法。

bind方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'error'：error事件。callbackErrorCallback是回调函数。TLSSocket连接订阅某类error事件触发的调用函数。

**错误码：**

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
  tls.on('error', (err: BusinessError) => {
    console.error("on error, err:" + JSON.stringify(err))
  });
});
```

#### off('error')9+

off(type: 'error', callback?: ErrorCallback): void

取消订阅TLSSocket连接的error事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'error'：error事件。callbackErrorCallback否回调函数。TLSSocket连接取消订阅某类error事件触发的调用函数。

**错误码：**

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let callback = (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err));
}
tls.on('error', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
tls.off('error', callback);
```

#### connect9+

connect(options: TLSConnectOptions, callback: AsyncCallback<void>): void

在TLSSocket上bind成功之后，进行通信连接，并创建和初始化TLS会话，实现建立连接过程，启动与服务器的TLS/SSL握手，实现数据传输功能，使用callback方式作为异步方法。需要注意options入参下secureOptions内的ca在API11及之前的版本为必填项，需填入服务端的ca证书(用于认证校验服务端的数字证书)，证书内容以"-----BEGIN CERTIFICATE-----"开头，以"-----END CERTIFICATE-----"结尾，自API12开始，为非必填项。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[TLSConnectOptions](#ZH-CN_TOPIC_0000002497445470__tlsconnectoptions9)是TLSSocket连接所需要的参数。callbackAsyncCallback<void>是回调函数，成功无返回，失败返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.2303104Interrupted system call.2303109Bad file number.2303111Resource temporarily unavailable. Try again.2303188Socket operation on non-socket.2303191Incorrect socket protocol type.2303198Address already in use.2303199Cannot assign requested address.2303210Connection timed out.2303501SSL is null.2303502An error occurred when reading data on the TLS socket.2303503An error occurred when writing data on the TLS socket.2303505An error occurred in the TLS system call.2303506Failed to close the TLS connection.2300002System internal error.2301206Socks5 failed to connect to the proxy server.2301207Socks5 username or password is invalid.2301208Socks5 failed to connect to the remote server.2301209Socks5 failed to negotiate the authentication method.2301210Socks5 failed to send the message.2301211Socks5 failed to receive the message.2301212Socks5 serialization error.2301213Socks5 deserialization error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsTwoWay: socket.TLSSocket = socket.constructTLSSocketInstance();  // Two way authentication
let bindAddr: socket.NetAddress = {
    address: '192.168.xx.xxx',
  // 绑定指定网络接口
}
tlsTwoWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let twoWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let twoWaySecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: twoWayNetAddr,
  secureOptions: twoWaySecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}

tlsTwoWay.connect(tlsConnectOptions, (err: BusinessError) => {
  console.error("connect callback error" + err);
});

let tlsOneWay: socket.TLSSocket = socket.constructTLSSocketInstance(); // One way authentication
tlsOneWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let oneWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let oneWaySecureOptions: socket.TLSSecureOptions = {
  ca: ["xxxx", "xxxx"],
  cipherSuite: "AES256-SHA256"
}
let tlsOneWayConnectOptions: socket.TLSConnectOptions = {
  address: oneWayNetAddr,
  secureOptions: oneWaySecureOptions
}
tlsOneWay.connect(tlsOneWayConnectOptions, (err: BusinessError) => {
  console.error("connect callback error" + err);
});
```

**示例（设置socket代理）：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsTwoWay: socket.TLSSocket = socket.constructTLSSocketInstance();  // 双向认证
let bindAddr: socket.NetAddress = {
   address: '192.168.xx.xxx',
  // 绑定指定网络接口
}
tlsTwoWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let twoWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let socks5Server: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let twoWaySecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let proxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: twoWayNetAddr,
  secureOptions: twoWaySecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"],
  proxy: proxyOptions,
}

tlsTwoWay.connect(tlsConnectOptions, (err: BusinessError) => {
  console.error("connect callback error" + err);
});

let tlsOneWay: socket.TLSSocket = socket.constructTLSSocketInstance(); // 单向认证
tlsOneWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let oneWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let oneWaySecureOptions: socket.TLSSecureOptions = {
  ca: ["xxxx", "xxxx"],
  cipherSuite: "AES256-SHA256"
}
let oneWayProxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let tlsOneWayConnectOptions: socket.TLSConnectOptions = {
  address: oneWayNetAddr,
  secureOptions: oneWaySecureOptions,
  proxy: oneWayProxyOptions,
}
tlsOneWay.connect(tlsOneWayConnectOptions, (err: BusinessError) => {
  console.error("connect callback error" + err);
});
```

#### connect9+

connect(options: TLSConnectOptions): Promise<void>

在TLSSocket上bind成功之后，进行通信连接，并创建和初始化TLS会话，实现建立连接过程，启动与服务器的TLS/SSL握手，实现数据传输功能，该连接包括两种认证方式，单向认证与双向认证，使用Promise方式作为异步方法。需要注意options入参下secureOptions内的ca在API11及之前的版本为必填项，需填入服务端的ca证书(用于认证校验服务端的数字证书)，证书内容以"-----BEGIN CERTIFICATE-----"开头，以"-----END CERTIFICATE-----"结尾，自API12开始，为非必填项。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[TLSConnectOptions](#ZH-CN_TOPIC_0000002497445470__tlsconnectoptions9)是连接所需要的参数。

**返回值：**

类型说明Promise<void>以Promise形式返回，成功无返回，失败返回错误码，错误信息。

**错误码：**

错误码ID错误信息401Parameter error.2303104Interrupted system call.2303109Bad file number.2303111Resource temporarily unavailable. Try again.2303188Socket operation on non-socket.2303191Incorrect socket protocol type.2303198Address already in use.2303199Cannot assign requested address.2303210Connection timed out.2303501SSL is null.2303502An error occurred when reading data on the TLS socket.2303503An error occurred when writing data on the TLS socket.2303505An error occurred in the TLS system call.2303506Failed to close the TLS connection.2300002System internal error.2301206Socks5 failed to connect to the proxy server.2301207Socks5 username or password is invalid.2301208Socks5 failed to connect to the remote server.2301209Socks5 failed to negotiate the authentication method.2301210Socks5 failed to send the message.2301211Socks5 failed to receive the message.2301212Socks5 serialization error.2301213Socks5 deserialization error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsTwoWay: socket.TLSSocket = socket.constructTLSSocketInstance();  // Two way authentication
let bindAddr: socket.NetAddress = {
   address: '192.168.xx.xxx',
  // 绑定指定网络接口
}
tlsTwoWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let twoWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let twoWaySecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: twoWayNetAddr,
  secureOptions: twoWaySecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}

tlsTwoWay.connect(tlsConnectOptions).then(() => {
  console.info("connect successfully");
}).catch((err: BusinessError) => {
  console.error("connect failed " + JSON.stringify(err));
});

let tlsOneWay: socket.TLSSocket = socket.constructTLSSocketInstance(); // One way authentication
tlsOneWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let oneWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let oneWaySecureOptions: socket.TLSSecureOptions = {
  ca: ["xxxx", "xxxx"],
  cipherSuite: "AES256-SHA256"
}
let tlsOneWayConnectOptions: socket.TLSConnectOptions = {
  address: oneWayNetAddr,
  secureOptions: oneWaySecureOptions
}
tlsOneWay.connect(tlsOneWayConnectOptions).then(() => {
  console.info("connect successfully");
}).catch((err: BusinessError) => {
  console.error("connect failed " + JSON.stringify(err));
});
```

**示例（设置socket代理）：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsTwoWay: socket.TLSSocket = socket.constructTLSSocketInstance();  // 双向认证
let bindAddr: socket.NetAddress = {
   address: '192.168.xx.xxx',
  // 绑定指定网络接口
}
tlsTwoWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let twoWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let socks5Server: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let twoWaySecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let proxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: twoWayNetAddr,
  secureOptions: twoWaySecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"],
  proxy: proxyOptions,
}

tlsTwoWay.connect(tlsConnectOptions).then(() => {
  console.info("connect successfully");
}).catch((err: BusinessError) => {
  console.error("connect failed " + JSON.stringify(err));
});

let tlsOneWay: socket.TLSSocket = socket.constructTLSSocketInstance(); // 单向认证
tlsOneWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let oneWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let oneWaySecureOptions: socket.TLSSecureOptions = {
  ca: ["xxxx", "xxxx"],
  cipherSuite: "AES256-SHA256"
}
let oneWayProxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let tlsOneWayConnectOptions: socket.TLSConnectOptions = {
  address: oneWayNetAddr,
  secureOptions: oneWaySecureOptions,
  proxy: oneWayProxyOptions,
}
tlsOneWay.connect(tlsOneWayConnectOptions).then(() => {
  console.info("connect successfully");
}).catch((err: BusinessError) => {
  console.error("connect failed " + JSON.stringify(err));
});
```

#### getRemoteAddress9+

getRemoteAddress(callback: AsyncCallback<NetAddress>): void

在TLSSocket通信连接成功之后，获取对端Socket地址。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)>是回调函数。成功返回对端的socket地址，失败返回错误码、错误信息。

**错误码：**

错误码ID错误信息2303188Socket operation on non-socket.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getRemoteAddress((err: BusinessError, data: socket.NetAddress) => {
  if (err) {
    console.error('getRemoteAddress fail');
    return;
  }
  console.info('getRemoteAddress success:' + JSON.stringify(data));
});
```

#### getRemoteAddress9+

getRemoteAddress(): Promise<NetAddress>

在TLSSocket通信连接成功之后，获取对端Socket地址。使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)>以Promise形式返回获取对端socket地址的结果。失败返回错误码，错误信息。

**错误码：**

错误码ID错误信息2303188Socket operation on non-socket.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getRemoteAddress().then(() => {
  console.info('getRemoteAddress success');
}).catch((err: BusinessError) => {
  console.error('getRemoteAddress fail');
});
```

#### getCertificate9+

getCertificate(callback: AsyncCallback<[X509CertRawData](#ZH-CN_TOPIC_0000002497445470__x509certrawdata9)>): void

在TLSSocket通信连接成功之后，获取本地的数字证书，该接口只适用于双向认证时，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<[X509CertRawData](#ZH-CN_TOPIC_0000002497445470__x509certrawdata9)>是回调函数，成功返回本地的证书，失败返回错误码、错误信息。

**错误码：**

错误码ID错误信息2303501SSL is null.2303504An error occurred when verifying the X.509 certificate.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getCertificate((err: BusinessError, data: socket.X509CertRawData) => {
  if (err) {
    console.error("getCertificate callback error = " + err);
  } else {
    console.info("getCertificate callback = " + data);
  }
});
```

#### getCertificate9+

getCertificate():Promise<[X509CertRawData](#ZH-CN_TOPIC_0000002497445470__x509certrawdata9)>

在TLSSocket通信连接之后，获取本地的数字证书，该接口只适用于双向认证时，使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[X509CertRawData](#ZH-CN_TOPIC_0000002497445470__x509certrawdata9)>以Promise形式返回本地的数字证书的结果。失败返回错误码，错误信息。

**错误码：**

错误码ID错误信息2303501SSL is null.2303504An error occurred when verifying the X.509 certificate.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getCertificate().then((data: socket.X509CertRawData) => {
  const decoder = util.TextDecoder.create();
  const str = decoder.decodeToString(data.data);
  console.info("getCertificate: " + str);
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
```

#### getRemoteCertificate9+

getRemoteCertificate(callback: AsyncCallback<[X509CertRawData](#ZH-CN_TOPIC_0000002497445470__x509certrawdata9)>): void

在TLSSocket通信连接成功之后，获取服务端的数字证书，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<[X509CertRawData](#ZH-CN_TOPIC_0000002497445470__x509certrawdata9)>是回调函数，返回服务端的证书。失败返回错误码、错误信息。

**错误码：**

错误码ID错误信息2303501SSL is null.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getRemoteCertificate((err: BusinessError, data: socket.X509CertRawData) => {
  if (err) {
    console.error("getRemoteCertificate callback error = " + err);
  } else {
    const decoder = util.TextDecoder.create();
    const str = decoder.decodeToString(data.data);
    console.info("getRemoteCertificate callback = " + str);
  }
});
```

#### getRemoteCertificate9+

getRemoteCertificate():Promise<[X509CertRawData](#ZH-CN_TOPIC_0000002497445470__x509certrawdata9)>

在TLSSocket通信连接成功之后，获取服务端的数字证书，使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[X509CertRawData](#ZH-CN_TOPIC_0000002497445470__x509certrawdata9)>以Promise形式返回服务端的数字证书的结果。失败返回错误码，错误信息。

**错误码：**

错误码ID错误信息2303501SSL is null.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getRemoteCertificate().then((data: socket.X509CertRawData) => {
  const decoder = util.TextDecoder.create();
  const str = decoder.decodeToString(data.data);
  console.info("getRemoteCertificate:" + str);
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
```

#### getProtocol9+

getProtocol(callback: AsyncCallback<string>): void

在TLSSocket通信连接成功之后，获取通信的协议版本，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<string>是回调函数，返回通信的协议。失败返回错误码、错误信息。

**错误码：**

错误码ID错误信息2303501SSL is null.2303505An error occurred in the TLS system call.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getProtocol((err: BusinessError, data: string) => {
  if (err) {
    console.error("getProtocol callback error = " + err);
  } else {
    console.info("getProtocol callback = " + data);
  }
});
```

#### getProtocol9+

getProtocol():Promise<string>

在TLSSocket通信连接成功之后，获取通信的协议版本，使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<string>以Promise形式返回通信的协议。失败返回错误码，错误信息。

**错误码：**

错误码ID错误信息2303501SSL is null.2303505An error occurred in the TLS system call.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getProtocol().then((data: string) => {
  console.info(data);
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
```

#### getCipherSuite9+

getCipherSuite(callback: AsyncCallback<Array<string>>): void

在TLSSocket通信连接成功之后，获取通信双方协商后的加密套件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<string>>是回调函数，返回通信双方支持的加密套件。失败返回错误码、错误信息。

**错误码：**

错误码ID错误信息2303501SSL is null.2303502An error occurred when reading data on the TLS socket.2303505An error occurred in the TLS system call.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getCipherSuite((err: BusinessError, data: Array<string>) => {
  if (err) {
    console.error("getCipherSuite callback error = " + err);
  } else {
    console.info("getCipherSuite callback = " + data);
  }
});
```

#### getCipherSuite9+

getCipherSuite(): Promise<Array<string>>

在TLSSocket通信连接成功之后，获取通信双方协商后的加密套件，使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<Array<string>>以Promise形式返回通信双方支持的加密套件。失败返回错误码，错误信息。

**错误码：**

错误码ID错误信息2303501SSL is null.2303502An error occurred when reading data on the TLS socket.2303505An error occurred in the TLS system call.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getCipherSuite().then((data: Array<string>) => {
  console.info('getCipherSuite success:' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
```

#### getSignatureAlgorithms9+

getSignatureAlgorithms(callback: AsyncCallback<Array<string>>): void

在TLSSocket通信连接成功之后，获取通信双方协商后签名算法，该接口只适配双向认证模式下，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<string>>是回调函数，返回双方支持的签名算法。

**错误码：**

错误码ID错误信息2303501SSL is null.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getSignatureAlgorithms((err: BusinessError, data: Array<string>) => {
  if (err) {
    console.error("getSignatureAlgorithms callback error = " + err);
  } else {
    console.info("getSignatureAlgorithms callback = " + data);
  }
});
```

#### getSignatureAlgorithms9+

getSignatureAlgorithms(): Promise<Array<string>>

在TLSSocket通信连接成功之后，获取通信双方协商后的签名算法，该接口只适配双向认证模式下，使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<Array<string>>以Promise形式返回获取到的双方支持的签名算法。

**错误码：**

错误码ID错误信息2303501SSL is null.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getSignatureAlgorithms().then((data: Array<string>) => {
  console.info("getSignatureAlgorithms success" + data);
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
```

#### getLocalAddress12+

getLocalAddress(): Promise<NetAddress>

获取TLSSocket的本地Socket地址。使用Promise方式作为异步方法。

在TLSSocketServer通信连接成功之后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)>以Promise形式返回获取本地socket地址的结果。

**错误码：**

错误码ID错误信息2300002System internal error.2301009Bad file descriptor.2303188Socket operation on non-socket.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getLocalAddress().then((localAddress: socket.NetAddress) => {
  console.info("Get success: " + JSON.stringify(localAddress));
}).catch((err: BusinessError) => {
  console.error("Get failed, error: " + JSON.stringify(err));
})
```

#### getSocketFd16+

getSocketFd(): Promise<number>

获取TLSSocket的文件描述符。使用Promise异步回调。

bind方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<number>以Promise形式返回socket的文件描述符。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
tls.getSocketFd().then((data: number) => {
  console.info("tls socket fd: " + data);
})
```

#### send9+

send(data: string | ArrayBuffer, callback: AsyncCallback<void>): void

在TLSSocket通信连接成功之后，向服务端发送消息，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明datastring | ArrayBuffer是发送的数据内容。callbackAsyncCallback<void>是回调函数,返回TLSSocket发送数据的结果。失败返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.2303501SSL is null.2303503An error occurred when writing data on the TLS socket.2303505An error occurred in the TLS system call.2303506Failed to close the TLS connection.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.send("xxxx", (err: BusinessError) => {
  if (err) {
    console.error("send callback error = " + err);
  } else {
    console.info("send success");
  }
});
```

#### send9+

send(data: string | ArrayBuffer): Promise<void>

在TLSSocket通信连接成功之后，向服务端发送消息，使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明datastring | ArrayBuffer是发送的数据内容。

**错误码：**

错误码ID错误信息401Parameter error.2303501SSL is null.2303503An error occurred when writing data on the TLS socket.2303505An error occurred in the TLS system call.2303506Failed to close the TLS connection.2300002System internal error.

**返回值：**

类型说明Promise<void>以Promise形式返回,返回TLSSocket发送数据的结果。失败返回错误码，错误信息。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.send("xxxx").then(() => {
  console.info("send success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
```

#### close9+

close(callback: AsyncCallback<void>): void

在TLSSocket通信连接成功之后，断开连接，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数,成功返回TLSSocket关闭连接的结果。失败返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.2303501SSL is null.2303505An error occurred in the TLS system call.2303506Failed to close the TLS connection.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.close((err: BusinessError) => {
  if (err) {
    console.error("close callback error = " + err);
  } else {
    console.info("close success");
  }
});
```

#### close9+

close(): Promise<void>

在TLSSocket通信连接成功之后，断开连接，使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<void>以Promise形式返回,返回TLSSocket关闭连接的结果。失败返回错误码，错误信息。

**错误码：**

错误码ID错误信息401Parameter error.2303501SSL is null.2303505An error occurred in the TLS system call.2303506Failed to close the TLS connection.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.close().then(() => {
  console.info("close success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
```

#### TLSConnectOptions9+

TLS连接的操作。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明address[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)否否网关地址。secureOptions[TLSSecureOptions](#ZH-CN_TOPIC_0000002497445470__tlssecureoptions9)否否TLS安全相关操作。ALPNProtocolsArray<string>否是ALPN协议，支持["spdy/1", "http/1.1"]，默认为[]。skipRemoteValidation12+boolean否是是否跳过对服务端进行证书认证，默认为false。true：跳过对服务端进行证书认证；false：不跳过对服务端进行证书认证。proxy18+[ProxyOptions](#ZH-CN_TOPIC_0000002497445470__proxyoptions18)否是使用的代理信息，默认不使用代理。timeout22+number否是连接超时时间，单位：ms，默认为0。传入值需为0-4294967295范围内的整数。TLSSocket连接在超时后会失败。

#### TLSSecureOptions9+

TLS安全相关操作。当本地证书cert和私钥key不为空时，开启双向验证模式。cert和key其中一项为空时，开启单向验证模式。

**系统能力**：SystemCapability.Communication.NetStack

名称类型只读可选说明castring | Array<string>否是服务端的ca证书，用于认证校验服务端的数字证书。默认为系统预置CA证书12+。certstring否是本地客户端的数字证书。keystring否是本地数字证书的私钥。passwordstring否是读取私钥的密码。protocols[Protocol](#ZH-CN_TOPIC_0000002497445470__protocol9) |Array<[Protocol](#ZH-CN_TOPIC_0000002497445470__protocol9)>否是TLS的协议版本，默认为"TLSv1.2"。useRemoteCipherPreferboolean否是优先使用对等方的密码套件。true：优先使用对等方的密码套件；false：不优先使用对等方的密码套件。signatureAlgorithmsstring否是通信过程中的签名算法，默认为"" 。cipherSuitestring否是通信过程中的加密套件，默认为"" 。isBidirectionalAuthentication12+boolean否是用于设置双向认证，默认为false。true：设置双向认证；false：不设置双向认证。

#### Protocol9+

TLS通信的协议版本。

**系统能力**：SystemCapability.Communication.NetStack

名称值说明TLSv12"TLSv1.2"使用TLSv1.2协议通信。TLSv13"TLSv1.3"使用TLSv1.3协议通信。

#### X509CertRawData9+

type X509CertRawData = cert.EncodingBlob

存储证书的数据。

**系统能力**：SystemCapability.Communication.NetStack

类型说明cert.EncodingBlob提供证书编码blob类型。

#### socket.constructTLSSocketServerInstance10+

constructTLSSocketServerInstance(): TLSSocketServer

创建并返回一个TLSSocketServer对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值:**

类型说明[TLSSocketServer](#ZH-CN_TOPIC_0000002497445470__tlssocketserver10)返回一个TLSSocketServer对象。

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
```

#### TLSSocketServer10+

TLSSocketServer连接。在调用TLSSocketServer的方法前，需要先通过[socket.constructTLSSocketServerInstance](#ZH-CN_TOPIC_0000002497445470__socketconstructtlssocketserverinstance10)创建TLSSocketServer对象。

#### listen10+

listen(options: TLSConnectOptions, callback: AsyncCallback<void>): void

绑定IP地址和端口，在TLSSocketServer上bind成功之后，监听客户端的连接，创建和初始化TLS会话，实现建立连接过程，加载证书秘钥并验证，使用callback方式作为异步方法。

IP地址设置为0.0.0.0时，可以监听本机所有地址。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[TLSConnectOptions](#ZH-CN_TOPIC_0000002497445470__tlsconnectoptions9)是TLSSocketServer连接所需要的参数。callbackAsyncCallback<void>是回调函数，成功返回空，失败返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.201Permission denied.2300002System internal error.2303109Bad file number.2303111Resource temporarily unavailable. Try again.2303198Address already in use.2303199Cannot assign requested address.2303501SSL is null.2303502An error occurred when reading data on the TLS socket.2303503An error occurred when writing data on the TLS socket.2303505An error occurred in the TLS system call.2303506Failed to close the TLS connection.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"],
  skipRemoteValidation: false
}
tlsServer.listen(tlsConnectOptions, (err: BusinessError) => {
  console.error("listen callback error" + err);
});
```

#### listen10+

listen(options: TLSConnectOptions): Promise<void>

绑定IP地址和端口，在TLSSocketServer上bind成功之后，监听客户端的连接，并创建和初始化TLS会话，实现建立连接过程，加载证书秘钥并验证，使用Promise方式作为异步方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[TLSConnectOptions](#ZH-CN_TOPIC_0000002497445470__tlsconnectoptions9)是连接所需要的参数。

**返回值：**

类型说明Promise<void>以Promise形式返回，成功返回空，失败返回错误码，错误信息。

**错误码：**

错误码ID错误信息401Parameter error.201Permission denied.2300002System internal error.2303109Bad file number.2303111Resource temporarily unavailable. Try again.2303198Address already in use.2303199Cannot assign requested address.2303501SSL is null.2303502An error occurred when reading data on the TLS socket.2303503An error occurred when writing data on the TLS socket.2303505An error occurred in the TLS system call.2303506Failed to close the TLS connection.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"],
  skipRemoteValidation: false
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
```

#### getState10+

getState(callback: AsyncCallback<SocketStateBase>): void

在TLSSocketServer的listen成功之后，获取TLSSocketServer状态。使用callback方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<[SocketStateBase](#ZH-CN_TOPIC_0000002497445470__socketstatebase)>是回调函数。成功返回TLSSocketServer状态，失败返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.2303188Socket operation on non-socket.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
tlsServer.getState((err: BusinessError, data: socket.SocketStateBase) => {
  if (err) {
    console.error('getState fail');
    return;
  }
  console.info('getState success:' + JSON.stringify(data));
});
```

#### getState10+

getState(): Promise<SocketStateBase>

在TLSSocketServer的listen成功之后，获取TLSSocketServer状态。使用Promise方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[SocketStateBase](#ZH-CN_TOPIC_0000002497445470__socketstatebase)>以Promise形式返回获取TLSSocketServer状态的结果。失败返回错误码，错误信息。

**错误码：**

错误码ID错误信息2303188Socket operation on non-socket.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
tlsServer.getState().then(() => {
  console.info('getState success');
}).catch((err: BusinessError) => {
  console.error('getState fail');
});
```

#### setExtraOptions10+

setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void

在TLSSocketServer的listen成功之后，设置TLSSocketServer连接的其他属性。使用callback方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[TCPExtraOptions](#ZH-CN_TOPIC_0000002497445470__tcpextraoptions)是TLSSocketServer连接的其他属性。callbackAsyncCallback<void>是回调函数。成功返回空，失败返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.2303188Socket operation on non-socket.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});

interface SocketLinger {
  on: boolean;
  linger: number;
}

let tcpExtraOptions: socket.TCPExtraOptions = {
  keepAlive: true,
  OOBInline: true,
  TCPNoDelay: true,
  socketLinger: { on: true, linger: 10 } as SocketLinger,
  receiveBufferSize: 8192,
  sendBufferSize: 8192,
  reuseAddress: true,
  socketTimeout: 3000
}
tlsServer.setExtraOptions(tcpExtraOptions, (err: BusinessError) => {
  if (err) {
    console.error('setExtraOptions fail');
    return;
  }
  console.info('setExtraOptions success');
});
```

#### setExtraOptions10+

setExtraOptions(options: TCPExtraOptions): Promise<void>

在TLSSocketServer的listen成功之后，设置TLSSocketServer连接的其他属性，使用Promise方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明options[TCPExtraOptions](#ZH-CN_TOPIC_0000002497445470__tcpextraoptions)是TLSSocketServer连接的其他属性。

**返回值：**

类型说明Promise<void>以Promise形式返回，成功返回空，失败返回错误码，错误信息。

**错误码：**

错误码ID错误信息401Parameter error.2303188Socket operation on non-socket.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});

interface SocketLinger {
  on: boolean;
  linger: number;
}

let tcpExtraOptions: socket.TCPExtraOptions = {
  keepAlive: true,
  OOBInline: true,
  TCPNoDelay: true,
  socketLinger: { on: true, linger: 10 } as SocketLinger,
  receiveBufferSize: 8192,
  sendBufferSize: 8192,
  reuseAddress: true,
  socketTimeout: 3000
}
tlsServer.setExtraOptions(tcpExtraOptions).then(() => {
  console.info('setExtraOptions success');
}).catch((err: BusinessError) => {
  console.error('setExtraOptions fail');
});
```

#### getCertificate10+

getCertificate(callback: AsyncCallback<[X509CertRawData](#ZH-CN_TOPIC_0000002497445470__x509certrawdata9)>): void

在TLSSocketServer通信连接成功之后，获取本地的数字证书，使用callback方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<[X509CertRawData](#ZH-CN_TOPIC_0000002497445470__x509certrawdata9)>是回调函数，成功返回本地的证书，失败返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.2303501SSL is null.2303504An error occurred when verifying the X.509 certificate.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
tlsServer.getCertificate((err: BusinessError, data: socket.X509CertRawData) => {
  if (err) {
    console.error("getCertificate callback error = " + err);
  } else {
    const decoder = util.TextDecoder.create();
    const str = decoder.decodeToString(data.data);
    console.info("getCertificate callback: " + str);
  }
});
```

#### getCertificate10+

getCertificate():Promise<[X509CertRawData](#ZH-CN_TOPIC_0000002497445470__x509certrawdata9)>

在TLSSocketServer通信连接之后，获取本地的数字证书，使用Promise方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[X509CertRawData](#ZH-CN_TOPIC_0000002497445470__x509certrawdata9)>以Promise形式返回本地的数字证书的结果。失败返回错误码，错误信息。

**错误码：**

错误码ID错误信息2303501SSL is null.2303504An error occurred when verifying the X.509 certificate.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
tlsServer.getCertificate().then((data: socket.X509CertRawData) => {
  const decoder = util.TextDecoder.create();
  const str = decoder.decodeToString(data.data);
  console.info("getCertificate: " + str);
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
```

#### getProtocol10+

getProtocol(callback: AsyncCallback<string>): void

在TLSSocketServer通信连接成功之后，获取通信的协议版本，使用callback方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<string>是回调函数，返回通信的协议。失败返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.2303501SSL is null.2303505An error occurred in the TLS system call.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
tlsServer.getProtocol((err: BusinessError, data: string) => {
  if (err) {
    console.error("getProtocol callback error = " + err);
  } else {
    console.info("getProtocol callback = " + data);
  }
});
```

#### getProtocol10+

getProtocol():Promise<string>

在TLSSocketServer通信连接成功之后，获取通信的协议版本，使用Promise方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<string>以Promise形式返回通信的协议。失败返回错误码，错误信息。

**错误码：**

错误码ID错误信息2303501SSL is null.2303505An error occurred in the TLS system call.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
tlsServer.getProtocol().then((data: string) => {
  console.info(data);
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
```

#### getLocalAddress12+

getLocalAddress(): Promise<NetAddress>

获取TLSSocketServer的本地Socket地址。使用Promise方式作为异步方法。

在TLSSocketServer通信连接成功之后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)>以Promise形式返回获取本地socket地址的结果。

**错误码：**

错误码ID错误信息2300002System internal error.2301009Bad file descriptor.2303188Socket operation on non-socket.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
tlsServer.getLocalAddress().then((localAddress: socket.NetAddress) => {
  console.info("Get success: " + JSON.stringify(localAddress));
}).catch((err: BusinessError) => {
  console.error("Get failed, error: " + JSON.stringify(err));
})
```

#### on('connect')10+

on(type: 'connect', callback: Callback<TLSSocketConnection>): void

订阅TLSSocketServer的连接事件。使用callback方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'connect'：连接事件。callbackCallback<[TLSSocketConnection](#ZH-CN_TOPIC_0000002497445470__tlssocketconnection10)>是回调函数。失败时返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
  tlsServer.on('connect', (data: socket.TLSSocketConnection) => {
    console.info(JSON.stringify(data));
  });
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
```

#### off('connect')10+

off(type: 'connect', callback?: Callback<TLSSocketConnection>): void

取消订阅TLSSocketServer的连接事件。使用callback方式作为异步方法。

listen方法调用成功后，才可调用此方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'connect'：连接事件。callbackCallback<[TLSSocketConnection](#ZH-CN_TOPIC_0000002497445470__tlssocketconnection10)>否回调函数。失败时返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});

let callback = (data: socket.TLSSocketConnection) => {
  console.info('on connect message: ' + JSON.stringify(data));
}
tlsServer.on('connect', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
tlsServer.off('connect', callback);
tlsServer.off('connect');
```

#### on('error')10+

on(type: 'error', callback: ErrorCallback): void

订阅TLSSocketServer连接的error事件。使用callback方式作为异步方法。

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'error'：error事件。callbackErrorCallback是回调函数。失败时返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
tlsServer.on('error', (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err))
});
```

#### off('error')10+

off(type: 'error', callback?: ErrorCallback): void

取消订阅TLSSocketServer连接的error事件。使用callback方式作为异步方法。

listen方法调用成功后，才可调用此方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'error'：error事件。callbackErrorCallback否回调函数。失败时返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});

let callback = (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err));
}
tlsServer.on('error', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
tlsServer.off('error', callback);
tlsServer.off('error');
```

#### close20+

close(): Promise<void>

TLSSocketServer停止监听并释放通过[listen](#ZH-CN_TOPIC_0000002497445470__listen10-2)方法绑定的端口。使用Promise异步回调。

该方法不会关闭已有连接。如需关闭，请调用[TLSSocketConnection](#ZH-CN_TOPIC_0000002497445470__tlssocketconnection10)的[close](#ZH-CN_TOPIC_0000002497445470__close10-2)方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](SOCKET 错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission denied.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.on('connect', (connection: socket.TLSSocketConnection) => {
  console.info("connection clientId: " + connection.clientId);
  // 逻辑处理
  tlsServer.close(); // 停止监听
  connection.close(); // 关闭当前连接
});
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("listen failed: " + err.code);
});
```

#### TLSSocketConnection10+

TLSSocketConnection连接，即TLSSocket客户端与服务端的连接。在调用TLSSocketConnection的方法前，需要先获取TLSSocketConnection对象。

客户端与服务端成功建立连接后，才能通过返回的TLSSocketConnection对象调用相应的接口。

**系统能力**：SystemCapability.Communication.NetStack

#### 属性

名称类型只读可选说明clientIdnumber否否客户端与TLSSocketServer建立连接的id。

#### send10+

send(data: string | ArrayBuffer, callback: AsyncCallback<void>): void

在TLSSocketServer通信连接成功之后，向客户端发送消息，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明datastring | ArrayBuffer是TLSSocketServer发送数据所需要的参数。callbackAsyncCallback<void>是回调函数，成功返回空，失败返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.2303501SSL is null.2303503An error occurred when writing data on the TLS socket.2303505An error occurred in the TLS system call.2303506Failed to close the TLS connection.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.send('Hello, client!', (err: BusinessError) => {
    if (err) {
      console.error('send fail');
      return;
    }
    console.info('send success');
  });
});
```

#### send10+

send(data: string | ArrayBuffer): Promise<void>

在TLSSocketServer通信连接成功之后，向服务端发送消息，使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明datastring | ArrayBuffer是TLSSocketServer发送数据所需要的参数。

**返回值：**

类型说明Promise<void>以Promise形式返回，成功返回空，失败返回错误码，错误信息。

**错误码：**

错误码ID错误信息401Parameter error.2303501SSL is null.2303503An error occurred when writing data on the TLS socket.2303505An error occurred in the TLS system call.2303506Failed to close the TLS connection.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.send('Hello, client!').then(() => {
    console.info('send success');
  }).catch((err: BusinessError) => {
    console.error('send fail');
  });
});
```

#### close10+

close(callback: AsyncCallback<void>): void

在与TLSSocketServer通信连接成功之后，断开连接，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数，成功返回空，失败返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.2303501SSL is null.2303505An error occurred in the TLS system call.2303506Failed to close the TLS connection.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.close((err: BusinessError) => {
    if (err) {
      console.error('close fail');
      return;
    }
    console.info('close success');
  });
});
```

#### close10+

close(): Promise<void>

在与TLSSocketServer通信连接成功之后，断开连接，使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<void>以Promise形式返回，成功返回空。失败返回错误码，错误信息。

**错误码：**

错误码ID错误信息2303501SSL is null.2303505An error occurred in the TLS system call.2303506Failed to close the TLS connection.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.close().then(() => {
    console.info('close success');
  }).catch((err: BusinessError) => {
    console.error('close fail');
  });
});
```

#### getRemoteAddress10+

getRemoteAddress(callback: AsyncCallback<NetAddress>): void

在TLSSocketServer通信连接成功之后，获取对端Socket地址。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)>是回调函数。成功返回对端的socket地址，失败返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.2303188Socket operation on non-socket.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getRemoteAddress((err: BusinessError, data: socket.NetAddress) => {
    if (err) {
      console.error('getRemoteAddress fail');
      return;
    }
    console.info('getRemoteAddress success:' + JSON.stringify(data));
  });
});
```

#### getRemoteAddress10+

getRemoteAddress(): Promise<NetAddress>

在TLSSocketServer通信连接成功之后，获取对端Socket地址。使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)>以Promise形式返回获取对端socket地址的结果。失败返回错误码，错误信息。

**错误码：**

错误码ID错误信息2303188Socket operation on non-socket.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getRemoteAddress().then((data: socket.NetAddress) => {
    console.info('getRemoteAddress success:' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error("failed" + err);
  });
});
```

#### getRemoteCertificate10+

getRemoteCertificate(callback: AsyncCallback<[X509CertRawData](#ZH-CN_TOPIC_0000002497445470__x509certrawdata9)>): void

在TLSSocketServer通信连接成功之后，获取对端的数字证书，该接口只适用于客户端向服务端发送证书时，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<[X509CertRawData](#ZH-CN_TOPIC_0000002497445470__x509certrawdata9)>是回调函数，返回对端的证书。失败返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.2303501SSL is null.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getRemoteCertificate((err: BusinessError, data: socket.X509CertRawData) => {
    if (err) {
      console.error("getRemoteCertificate callback error: " + err);
    } else {
      const decoder = util.TextDecoder.create();
      const str = decoder.decodeToString(data.data);
      console.info("getRemoteCertificate callback: " + str);
    }
  });
});
```

#### getRemoteCertificate10+

getRemoteCertificate():Promise<[X509CertRawData](#ZH-CN_TOPIC_0000002497445470__x509certrawdata9)>

在TLSSocketServer通信连接成功之后，获取对端的数字证书，该接口只适用于客户端向服务端发送证书时，使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[X509CertRawData](#ZH-CN_TOPIC_0000002497445470__x509certrawdata9)>以Promise形式返回对端的数字证书的结果。失败返回错误码，错误信息。

**错误码：**

错误码ID错误信息2303501SSL is null.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getRemoteCertificate().then((data: socket.X509CertRawData) => {
    const decoder = util.TextDecoder.create();
    const str = decoder.decodeToString(data.data);
    console.info("getRemoteCertificate success: " + str);
  }).catch((err: BusinessError) => {
    console.error("failed" + err);
  });
});
```

#### getCipherSuite10+

getCipherSuite(callback: AsyncCallback<Array<string>>): void

在TLSSocketServer通信连接成功之后，获取通信双方协商后的加密套件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<string>>是回调函数，返回通信双方支持的加密套件。失败返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.2303501SSL is null.2303502An error occurred when reading data on the TLS socket.2303505An error occurred in the TLS system call.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getCipherSuite((err: BusinessError, data: Array<string>) => {
    if (err) {
      console.error("getCipherSuite callback error = " + err);
    } else {
      console.info("getCipherSuite callback = " + data);
    }
  });
});
```

#### getCipherSuite10+

getCipherSuite(): Promise<Array<string>>

在TLSSocketServer通信连接成功之后，获取通信双方协商后的加密套件，使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<Array<string>>以Promise形式返回通信双方支持的加密套件。失败返回错误码，错误信息。

**错误码：**

错误码ID错误信息2303501SSL is null.2303502An error occurred when reading data on the TLS socket.2303505An error occurred in the TLS system call.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getCipherSuite().then((data: Array<string>) => {
    console.info('getCipherSuite success:' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error("failed" + err);
  });
});
```

#### getSignatureAlgorithms10+

getSignatureAlgorithms(callback: AsyncCallback<Array<string>>): void

在TLSSocketServer通信连接成功之后，获取通信双方协商后签名算法，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<string>>是回调函数，返回双方支持的签名算法。

**错误码：**

错误码ID错误信息401Parameter error.2303501SSL is null.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getSignatureAlgorithms((err: BusinessError, data: Array<string>) => {
    if (err) {
      console.error("getSignatureAlgorithms callback error = " + err);
    } else {
      console.info("getSignatureAlgorithms callback = " + data);
    }
  });
});
```

#### getSignatureAlgorithms10+

getSignatureAlgorithms(): Promise<Array<string>>

在TLSSocketServer通信连接成功之后，获取通信双方协商后的签名算法，使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<Array<string>>以Promise形式返回获取到的双方支持的签名算法。

**错误码：**

错误码ID错误信息2303501SSL is null.2300002System internal error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getSignatureAlgorithms().then((data: Array<string>) => {
    console.info("getSignatureAlgorithms success" + data);
  }).catch((err: BusinessError) => {
    console.error("failed" + err);
  });
});
```

#### getLocalAddress12+

getLocalAddress(): Promise<NetAddress>

获取TLSSocketConnection连接的本地Socket地址。使用Promise方式作为异步方法。

在TLSSocketServer通信连接成功之后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

类型说明Promise<[NetAddress](#ZH-CN_TOPIC_0000002497445470__netaddress)>以Promise形式返回获取本地socket地址的结果。

**错误码：**

错误码ID错误信息2300002System internal error.2301009Bad file descriptor.2303188Socket operation on non-socket.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getLocalAddress().then((localAddress: socket.NetAddress) => {
    console.info("Family IP Port: " + JSON.stringify(localAddress));
  }).catch((err: BusinessError) => {
    console.error("TLS Client Get Family IP Port failed, error: " + JSON.stringify(err));
  })
});
```

#### on('message')10+

on(type: 'message', callback: Callback<SocketMessageInfo>): void

订阅TLSSocketConnection连接的接收消息事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'message'：接收消息事件。callbackCallback<[SocketMessageInfo](#ZH-CN_TOPIC_0000002497445470__socketmessageinfo11)>是回调函数。成功时返回TLSSocketConnection连接信息，失败时返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.on('message', (value: socket.SocketMessageInfo) => {
    let messageView = '';
    let uint8Array = new Uint8Array(value.message);
    for (let i: number = 0; i < value.message.byteLength; i++) {
      let messages = uint8Array[i];
      let message = String.fromCharCode(messages);
      messageView += message;
    }
    console.info('on message message: ' + JSON.stringify(messageView));
    console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
  });
});
```

#### off('message')10+

off(type: 'message', callback?: Callback<SocketMessageInfo>): void

取消订阅TLSSocketConnection连接的接收消息事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'message'：接收消息事件。callbackCallback<[SocketMessageInfo](#ZH-CN_TOPIC_0000002497445470__socketmessageinfo11)>否回调函数。成功时返回TLSSocketConnection连接信息，失败时返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

let callback = (value: socket.SocketMessageInfo) => {
  let messageView = '';
  for (let i: number = 0; i < value.message.byteLength; i++) {
    let uint8Array = new Uint8Array(value.message)
    let messages = uint8Array[i]
    let message = String.fromCharCode(messages);
    messageView += message;
  }
  console.info('on message message: ' + JSON.stringify(messageView));
  console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
}
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.on('message', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  client.off('message', callback);
  client.off('message');
});
```

#### on('close')10+

on(type: 'close', callback: Callback<void>): void

订阅TLSSocketConnection的关闭事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'close'：关闭事件。callbackCallback<void>是回调函数。成功时返回空，失败时返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.on('close', () => {
    console.info("on close success")
  });
});
```

#### off('close')10+

off(type: 'close', callback?: Callback<void>): void

取消订阅TLSSocketConnection的关闭事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'close'：关闭事件。callbackCallback<void>否回调函数。成功时返回空，失败时返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

let callback = () => {
  console.info("on close success");
}
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.on('close', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  client.off('close', callback);
  client.off('close');
});
```

#### on('error')10+

on(type: 'error', callback: ErrorCallback): void

订阅TLSSocketConnection连接的error事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'error'：error事件。callbackErrorCallback是回调函数。成功时返回空，失败时返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.on('error', (err: BusinessError) => {
    console.error("on error, err:" + JSON.stringify(err))
  });
});
```

#### off('error')10+

off(type: 'error', callback?: ErrorCallback): void

取消订阅TLSSocketConnection连接的error事件。使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

参数名类型必填说明typestring是订阅的事件类型。'error'：error事件。callbackErrorCallback否回调函数。成功时返回空，失败时返回错误码、错误信息。

**错误码：**

错误码ID错误信息401Parameter error.

**示例：**

```ets
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

let callback = (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err));
}
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.on('error', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  client.off('error', callback);
  client.off('error');
});
```