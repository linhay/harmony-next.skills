# urpc

本模块提供URPC功能。应用程序可通过URPC提供的生成代码接口发起RPC请求。常见的URPC方法包括urpcStubCreate、call、cancel、destroy。

**起始版本：**5.0.1(13)

#### 导入模块

```ets
import { urpc } from "@kit.RemoteCommunicationKit";
```

#### FlowbufType

type FlowbufType =

'INT8' | 'UINT8' | 'INT16' | 'UINT16' | 'INT32' | 'UINT32' | 'INT64' | 'UINT64' | 'BOOL' | 'FLOAT' | 'DOUBLE' | 'STRING' | 'BYTES' | 'MESSAGE' | 'REPEATED_INT8' | 'REPEATED_UINT8' | 'REPEATED_INT16' | 'REPEATED_UINT16' | 'REPEATED_INT32' | 'REPEATED_UINT32' | 'REPEATED_INT64' | 'REPEATED_UINT64' | 'REPEATED_BOOL' | 'REPEATED_FLOAT' | 'REPEATED_DOUBLE' | 'REPEATED_STRING' | 'REPEATED_BYTES' | 'REPEATED_MESSAGE' | 'ARRAY_INT8' | 'ARRAY_UINT8' | 'ARRAY_INT16' | 'ARRAY_UINT16' | 'ARRAY_INT32' | 'ARRAY_UINT32' | 'ARRAY_INT64' | 'ARRAY_UINT64' | 'ARRAY_BOOL' | 'ARRAY_FLOAT' | 'ARRAY_DOUBLE';

表示通过URPC通信允许传入和接收返回值的类型。

**系统能力**：SystemCapability.Collaboration.RemoteCommunication

**起始版本：**5.0.1(13)

类型

说明

'INT8'

表示参数类型为'INT8'。

'UINT8'

表示参数类型为'UINT8'。

'INT16'

表示参数类型为'INT16'。

'UINT16'

表示参数类型为'UINT16'。

'INT32'

表示参数类型为'INT32'。

'UINT32'

表示参数类型为'UINT32'。

'INT64'

表示参数类型为'INT64'。

'UINT64'

表示参数类型为'UINT64'。

'BOOL'

表示参数类型为'BOOL'。

'FLOAT'

表示参数类型为'FLOAT'。

'DOUBLE'

表示参数类型为'DOUBLE'。

'STRING'

表示参数类型为'STRING'。

'BYTES'

表示参数类型为'BYTES'。

'MESSAGE'

表示参数类型为自定义的'MESSAGE'。

'REPEATED_INT8'

表示参数类型为可变长度的'INT8'数组，该字段为预留字段，在当前版本不能使用。

'REPEATED_UINT8'

表示参数类型为可变长度的'UINT8'数组，该字段为预留字段，在当前版本不能使用。

'REPEATED_INT16'

表示参数类型为可变长度的'INT16'数组，该字段为预留字段，在当前版本不能使用。

'REPEATED_UINT16'

表示参数类型为可变长度的'UINT16'数组，该字段为预留字段，在当前版本不能使用。

'REPEATED_INT32'

表示参数类型为可变长度的'INT32'数组，该字段为预留字段，在当前版本不能使用。

'REPEATED_UINT32'

表示参数类型为可变长度的'UINT32'数组，该字段为预留字段，在当前版本不能使用。

'REPEATED_INT64'

表示参数类型为可变长度的'INT64'数组，该字段为预留字段，在当前版本不能使用。

'REPEATED_UINT64'

表示参数类型为可变长度的'UINT64'数组，该字段为预留字段，在当前版本不能使用。

'REPEATED_BOOL'

表示参数类型为可变长度的'BOOL'数组，该字段为预留字段，在当前版本不能使用。

'REPEATED_FLOAT'

表示参数类型为可变长度的'INT8'数组，该字段为预留字段，在当前版本不能使用。

'REPEATED_DOUBLE'

表示参数类型为可变长度的'DOUBLE'数组，该字段为预留字段，在当前版本不能使用。

'REPEATED_STRING'

表示参数类型为可变长度的'STRING'数组，该字段为预留字段，在当前版本不能使用。

'REPEATED_BYTES'

表示参数类型为可变长度的'BYTES'数组，该字段为预留字段，在当前版本不能使用。

'REPEATED_MESSAGE'

表示参数类型为可变长度的自定义'MESSAGE'数组，该字段为预留字段，在当前版本不能使用。

'ARRAY_INT8'

表示参数类型为固定长度的'INT8'数组，该字段为预留字段，在当前版本不能使用。

'ARRAY_UINT8'

表示参数类型为固定长度的'UINT8'数组，该字段为预留字段，在当前版本不能使用。

'ARRAY_INT16'

表示参数类型为固定长度的'INT16'数组，该字段为预留字段，在当前版本不能使用。

'ARRAY_UINT16'

表示参数类型为固定长度的'UINT16'数组，该字段为预留字段，在当前版本不能使用。

'ARRAY_INT32'

表示参数类型为固定长度的'INT32'数组，该字段为预留字段，在当前版本不能使用。

'ARRAY_UINT32'

表示参数类型为固定长度的'UINT32'数组，该字段为预留字段，在当前版本不能使用。

'ARRAY_INT64'

表示参数类型为固定长度的'INT64'数组，该字段为预留字段，在当前版本不能使用。

'ARRAY_UINT64'

表示参数类型为固定长度的'UINT64'数组，该字段为预留字段，在当前版本不能使用。

'ARRAY_BOOL'

表示参数类型为固定长度的'BOOL'数组，该字段为预留字段，在当前版本不能使用。

'ARRAY_FLOAT'

表示参数类型为固定长度的'FLOAT'数组，该字段为预留字段，在当前版本不能使用。

'ARRAY_DOUBLE'

表示参数类型为固定长度的'DOUBLE'数组，该字段为预留字段，在当前版本不能使用。

#### FlowbufElement<T>

FlowbufElement<T>用于定义非数组的URPC入参和返回值类型。

**系统能力**：SystemCapability.Collaboration.RemoteCommunication

**起始版本：**5.0.1(13)

名称

类型

只读

可选

说明

type

[FlowbufType](#section123121188272)

否

否

表示通过URPC通信允许传入和接收返回值的类型。

value

T

否

否

表示该参数的具体数值。

name

string

否

否

表示该参数的名称。

**示例：**

```ets
import { urpc } from "@kit.RemoteCommunicationKit"

let version: urpc.FlowbufElement<number> = {type: 'INT8', value: 0, name: ""};
```

#### FlowbufArrayElement<T>

FlowbufArrayElement<T>用于定义数组类型的URPC入参和返回值类型。

**系统能力**：SystemCapability.Collaboration.RemoteCommunication

**起始版本：**5.0.1(13)

名称

类型

只读

可选

说明

type

[FlowbufType](#section123121188272)

否

否

表示通过URPC通信允许传送和接收返回值的类型。

value

T[]

否

否

表示该参数的具体数值。

length

number

否

否

表示该参数数组的长度，长度范围[0, 2147483647]。

**示例：**

```ets
import { urpc } from "@kit.RemoteCommunicationKit"

let version: urpc.FlowbufArrayElement<number> = {type: 'ARRAY_INT8', value: [1,2,3], length: 3};
```

#### urpc.urpcStubCreate

urpcStubCreate(config: UrpcInitConfiguration, funcList: string | string[]): Promise<UrpcStub>

创建UrpcStub，使用Promise异步回调。

**系统能力**：SystemCapability.Collaboration.RemoteCommunication

**需要****权限：**ohos.permission.INTERNET

**起始版本：**5.0.1(13)

**参数：**

参数名

类型

必填

说明

config

[UrpcInitConfiguration](#section18613443123412)

是

stub配置。

funcList

string | string[]

是

URPC函数调用列表。

**返回值：**

类型

说明

Promise<[UrpcStub](#section1671892662116)>

Promise对象，返回可用于发出URPC请求的对象。

**错误码：**

错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

201

Permission denied.

401

Parameter error.

10079100998

Function name error.

**示例：**

```ets
import { urpc } from "@kit.RemoteCommunicationKit";

let node: urpc.IpAndPort = {
  ip: '127.0.0.1',
  port: 8000
}
let connect: urpc.UrpcConnectConfiguration = {
  node: node,
  protocol: 'eat',
}
let config: urpc.UrpcInitConfiguration = {
  timeout: 3000,
  mode: 'client',
  connect: connect
}

const funcList:string[] = ["uploadFile"];
let urpcStub = await urpc.urpcStubCreate(config, funcList);
```

#### UrpcCall

type UrpcCall = (funcName: string, request: object, returnValue: object, config?: CallingOption) => UrpcPromise;

用于发起一个URPC请求，并接收来自服务器的响应。

**系统能力**：SystemCapability.Collaboration.RemoteCommunication

**起始版本：**5.0.1(13)

**参数：**

参数名

类型

必填

说明

funcName

string

是

URPC请求函数名。

request

object

是

URPC请求对象，请求数据的最大值为1M。

returnValue

object

是

URPC接受response的对象，接收数据的最大值为100KB。

config

[CallingOption](#section731665213712)

否

单次请求配置选项。该字段为预留字段，在当前版本并不生效。

**返回值：**

类型

说明

[UrpcPromise](#section154329285418)

Promise对象，返回来自服务器的响应对象。

**错误码：**错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

#### UrpcCancel

type UrpcCancel = (callingId?: number | number[]) => void;

用于取消指定或所有正在进行的URPC请求。

**系统能力**：SystemCapability.Collaboration.RemoteCommunication

**起始版本：**5.0.1(13)

**参数：**

参数名

类型

必填

说明

callingId

number | number[]

否

取消指定callingId的请求。如果不填该字段表示取消本次UrpcStub对应的所有请求，取值范围[0, 2147483647]。

**错误码：**错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

#### UrpcDestroy

type UrpcDestroy = () => void

用于销毁[UrpcStub](#section1671892662116)实例。

**系统能力**：SystemCapability.Collaboration.RemoteCommunication

**起始版本：**5.0.1(13)

**错误码：**错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

#### UrpcStub

表示可用于发出URPC请求的通信会话。它提供了各种远程调用方法（call、cancel、destroy）。

**系统能力**：SystemCapability.Collaboration.RemoteCommunication

**起始版本：**5.0.1(13)

**属性：**

名称

类型

只读

可选

说明

id

number

是

否

UrpcStub的唯一标识id。

call

[UrpcCall](#section1223416820339)

否

否

表示调用URPC请求。

cancel

[UrpcCancel](#section16128181393419)

否

否

表示取消URPC请求。

destroy

[UrpcDestroy](#section4758175133410)

否

否

表示销毁UrpcStub。

#### UrpcInitConfiguration

SessionConfiguration接口定义了会话的配置参数，为开发者提供了对HTTP会话各个方面的详细控制。

**系统能力**：SystemCapability.Collaboration.RemoteCommunication

**起始版本：**5.0.1(13)

名称

类型

只读

可选

说明

mode

[UrpcMode](#section1898141153617)

否

是

URPC的运行模式，默认值为'client'，表示client模式。

connect

[UrpcConnectConfiguration](#section4802256134519)

否

否

指定与stub相关联的连接配置，包括ip地址和端口号、URPC连接协议、是否多径等配置项。

timeout

number

否

否

设置URPC的连接超时时间，表示请求等待多久后超时返回，单位是毫秒（ms），取值范围[0, 4294967295]。该字段为预留字段，在当前版本并不生效。

**示例：**

```ets
import { urpc } from "@kit.RemoteCommunicationKit";

let node: urpc.IpAndPort = {
  ip: '127.0.0.1',
  port: 8000
}
let connect: urpc.UrpcConnectConfiguration = {
  node: node,
  protocol: 'eat',
}
let config: urpc.UrpcInitConfiguration = {
  timeout: 3000,
  mode: 'client',
  connect: connect
}
```

#### UrpcMode

type UrpcMode = 'client';

当前仅支持填写'client'，表示该URPC节点为client模式，可主动发起请求，等待服务器的响应。

**系统能力**：SystemCapability.Collaboration.RemoteCommunication

**起始版本：**5.0.1(13)

类型

说明

'client'

表示URPC节点的模式，值固定为'client'。

#### UrpcConnectConfiguration

UrpcConnectConfiguration配置URPC连接的关键信息，可以配置连接的ip和端口号，以及传输协议等可选参数。

**系统能力**：SystemCapability.Collaboration.RemoteCommunication

**起始版本：**5.0.1(13)

名称

类型

只读

可选

说明

node

[IpAndPort](#section59321354193610)

否

否

连接的IP和端口配置。

protocol

[UrpcProtocol](#section557714186379)

否

是

传输连接采用的协议类型，默认值为'eat'，表示采用eat协议。

multiPath

boolean

否

是

是否支持多路径传输，true表示支持多路径传输，多路径包含蜂窝网络和Wi-Fi；false表示不支持多路径传输，默认值为false。该字段为预留字段，在当前版本并不生效。

flags

number

否

是

证书标记位，非0表示开启证书校验。默认值为0，表示不开启证书校验。

host

string

否

是

urpc服务的域名，默认值为空字符串。

caPath

string

否

是

校验证书的路径名称，默认值为空字符串。

**示例：**

```ets
import { urpc } from "@kit.RemoteCommunicationKit"

let node: urpc.IpAndPort = {
  ip: '127.0.0.1',
  port: 8000
}
let connect: urpc.UrpcConnectConfiguration = {
  node: node,
  protocol: 'eat',
  multiPath: false,
  flags: 0,
  host: "127.0.0.1",
  caPath: "data/single_urpc/eat.pem"
}
```

#### IpAndPort

IpAndPort用于配置URPC的连接IP和端口号。

**系统能力**：SystemCapability.Collaboration.RemoteCommunication

**起始版本：**5.0.1(13)

名称

类型

只读

可选

说明

ip

string

否

否

指定UPRC的IPv4或IPv6地址。

port

number

否

否

指定URPC端口号，取值范围[0, 65535]。

**示例：**

```ets
import { urpc } from "@kit.RemoteCommunicationKit"

let node: urpc.IpAndPort = {
  ip: '127.0.0.1',
  port: 8000
}
```

#### UrpcPromise

表示URPC请求的返回值

**系统能力**：SystemCapability.Collaboration.RemoteCommunication

**起始版本：**5.0.1(13)

名称

类型

只读

可选

说明

promise

Promise<Object>

否

否

URPC请求的响应对象。

callingId

number

否

否

URPC请求的唯一标识Id，取值范围[0, 2147483647]。

#### UrpcProtocol

type UrpcProtocol = 'eat'

当前仅支持填写'eat'，表示URPC的协议类型为eat。

**系统能力**：SystemCapability.Collaboration.RemoteCommunication

**起始版本：**5.0.1(13)

类型

说明

'eat'

表示URPC节点的协议类型，值固定为'eat'。

#### CallingOption

用于配置URPC请求的优先级。

**系统能力**：SystemCapability.Collaboration.RemoteCommunication

**起始版本：**5.0.1(13)

名称

类型

只读

可选

说明

priority

number

否

是

配置URPC请求的优先级，默认为0，最大取值为3，表示优先级最高，优先级高的可以优先传输。该字段为预留字段，当前版本并不生效。