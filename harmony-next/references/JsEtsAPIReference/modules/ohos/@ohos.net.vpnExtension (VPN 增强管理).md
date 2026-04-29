# @ohos.net.vpnExtension (VPN 增强管理)

三方VPN管理模块，支持三方VPN的启动和停止功能。三方VPN是指由第三方提供的VPN服务，它们通常提供更多的功能和更广泛的网络连接选项，包括更多的安全和隐私功能，以及更全面的定制选项。当前提供三方VPN能力主要用于创建虚拟网卡及配置VPN路由信息，连接隧道过程及内部连接的协议需要应用内部自行实现。

本模块首批接口从 API version 11 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

如下模块不支持在VpnExtensionAbility引用，可能会导致程序异常退出。

-

[@ohos.contact(联系人)](@ohos.contact (联系人).md)

-

[@ohos.geolocation](@ohos.geolocation (位置服务).md)、[@ohos.geoLocationManager(位置服务)](@ohos.geoLocationManager (位置服务).md)

-

[@ohos.multimedia.audio(音频管理)](模块描述.md)

-

[@ohos.multimedia.camera(相机管理)](模块描述.md)

-

[@ohos.telephony.call(拨打电话)](@ohos.telephony.call (拨打电话).md)

-

[@ohos.telephony.sim(SIM卡管理)](@ohos.telephony.sim (SIM卡管理).md)

-

[@ohos.telephony.sms(短信服务)](@ohos.telephony.sms (短信服务).md)

#### 导入模块

```ets
import { vpnExtension } from '@kit.NetworkKit';
```

**LinkAddress**

type LinkAddress = connection.LinkAddress

获取网络链接信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 类型 | 说明 |
| --- | --- |
| connection.LinkAddress | 网络链路信息。 |

**RouteInfo**

type RouteInfo = connection.RouteInfo

获取网络路由信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 类型 | 说明 |
| --- | --- |
| connection.RouteInfo | 网络路由信息。 |

**[VpnExtensionContext](../../topics/networking/VpnExtensionContext.md)**

type VpnExtensionContext = [_VpnExtensionContext](../../topics/networking/VpnExtensionContext.md)

VPN扩展的上下文。它允许访问serviceExtension特定资源。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [_VpnExtensionContext](../../topics/networking/VpnExtensionContext.md) | VPN扩展的上下文。 |

#### vpnExtension.startVpnExtensionAbility

startVpnExtensionAbility(want: Want): Promise<void>

启动新的三方VPN功能。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 指示要启动的信息。  说明： 从API version 22开始，支持在VPN首次启动时传递want中的parameters字段。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[元能力子系统错误码]([元能力子系统错误码](../../errors/元能力子系统错误码.md).md)和[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16200001 | The caller has been released. |

**示例：**

Stage 模型示例：

```ets
import { Want } from '@kit.AbilityKit';
import { vpnExtension } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let want: Want = {
  deviceId: "",
  bundleName: "com.example.myvpndemo",
  abilityName: "MyVpnExtAbility",
};

@Entry
@Component
struct Index {
  @State message: string = 'Hello World'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(40)
          .fontWeight(FontWeight.Bold).onClick(() => {
          console.info("btn click")
        })
        Button('Start Extension').onClick(() => {
          vpnExtension.startVpnExtensionAbility(want).then(() => {
            console.info('startVpnExtensionAbility success');
          }).catch((err: BusinessError) => {
            console.error('startVpnExtensionAbility error: ' + JSON.stringify(err));
          })
        }).width('70%').fontSize(30).margin(16)
      }.width('100%')
    }.height('100%')
  }
```

#### vpnExtension.stopVpnExtensionAbility

stopVpnExtensionAbility(want: Want): Promise<void>

停止同一应用程序中的服务。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 指示要启动的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[元能力子系统错误码](元能力子系统错误码.md)和[通用错误码](通用错误码.md)。

| 错误码 ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000006 | Cross-user operations are not allowed. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16200001 | The caller has been released. |

**示例：**

Stage 模型示例：

```ets
import { Want } from '@kit.AbilityKit';
import { vpnExtension } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let want: Want = {
  deviceId: "",
  bundleName: "com.example.myvpndemo",
  abilityName: "MyVpnExtAbility",
};

@Entry
@Component
struct Index {
  @State message: string = 'Hello World'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold).onClick(() => {
          console.info("btn click")
        })
        Button('Start Extension').onClick(() => {
          vpnExtension.startVpnExtensionAbility(want).then(() => {
            console.info('startVpnExtensionAbility success');
          }).catch((err: BusinessError) => {
            console.error('startVpnExtensionAbility error: ' + JSON.stringify(err));
          })
        }).width('70%').fontSize(30).margin(16)
        Button('Stop Extension').onClick(() => {
          console.info("btn end")
          vpnExtension.stopVpnExtensionAbility(want).then(() => {
            console.info('stopVpnExtensionAbility success');
          }).catch((err: BusinessError) => {
            console.error('stopVpnExtensionAbility error: ' + JSON.stringify(err));
          })
        }).width('70%').fontSize(30).margin(16)

      }.width('100%')
    }.height('100%')
  }
```

#### vpnExtension.createVpnConnection

createVpnConnection(context: [VpnExtensionContext](../../topics/networking/VpnExtensionContext.md)): VpnConnection

创建一个三方VPN连接对象。

调用createVpnConnection接口前，需要先调用startVpnExtensionAbility接口启用VPN功能。

**系统能力**：SystemCapability.Communication.NetManager.Vpn

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [VpnExtensionContext](../../topics/networking/VpnExtensionContext.md) | 是 | 指定 context。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| VpnConnection | 返回一个VPN连接对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

Stage 模型示例：

```ets
import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
import { common, Want } from '@kit.AbilityKit';

let context: vpnExtension.VpnExtensionContext;
export default class MyVpnExtAbility extends VpnExtensionAbility {
  onCreate(want: Want) {
    let vpnConnection : vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
    console.info("VPN createVpnConnection: " + JSON.stringify(vpnConnection));
  }
```

#### VpnConnection

VPN连接对象。在调用VpnConnection的方法前，需要先通过vpnExt.createVpnConnection创建VPN连接对象。

#### create

create(config: VpnConfig): Promise<number>

使用config创建一个VPN网络。使用Promise异步回调。


建议在不需要VPN网络的时候配对调用[destroy()](#ZH-CN_TOPIC_0000002553201445__destroy)或[destroy(vpnId: string)](#ZH-CN_TOPIC_0000002553201445__destroy20)接口销毁启动的VPN网络，并执行资源清理等操作。

**系统能力**：SystemCapability.Communication.NetManager.Vpn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | VpnConfig | 是 | 指定VPN网络的配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以 Promise 形式返回获取结果，返回指定虚拟网卡的文件描述符 fd。 |

**错误码：**

以下错误码的详细介绍请参见[VPN错误码]([VPN错误码](../../errors/VPN错误码.md).md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2200001 | Invalid parameter value. |
| 2200002 | Operation failed. Cannot connect to service. |
| 2200003 | System internal error. |
| 2203001 | VPN creation denied, please check the user type. |
| 2203002 | VPN exist already, please execute destroy first. |

**示例：**

```ets
import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
import { common, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let context: vpnExtension.VpnExtensionContext;
export default class MyVpnExtAbility extends VpnExtensionAbility {
  private tunIp: string = '10.0.0.5';
  private blockedAppName: string = 'com.example.myvpndemo';
  onCreate(want: Want) {
    let vpnConnection : vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
    console.info("vpn createVpnConnection: " + JSON.stringify(vpnConnection));
    this.SetupVpn();
  }
  SetupVpn() {
        class Address {
            address: string;
            family: number;

            constructor(address: string, family: number) {
                this.address = address;
                this.family = family;
            }

        class AddressWithPrefix {
            address: Address;
            prefixLength: number;

            constructor(address: Address, prefixLength: number) {
                this.address = address;
                this.prefixLength = prefixLength;
        }

        class Config {
            addresses: AddressWithPrefix[];
            mtu: number;
            dnsAddresses: string[];
            trustedApplications: string[];
            blockedApplications: string[];

            constructor(
                tunIp: string,
                blockedAppName: string
            ) {
                this.addresses = [
                    new AddressWithPrefix(new Address(tunIp, 1), 24)
                ];
                this.mtu = 1400;
                this.dnsAddresses = ["114.114.114.114"];
                this.trustedApplications = [];
                this.blockedApplications = [blockedAppName];
            }

        let config = new Config(this.tunIp, this.blockedAppName);

        try {
            let vpnConnection : vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
            vpnConnection.create(config).then((data) => {
                hilog.error(0x0000, 'developTag', 'tunfd: %{public}s', JSON.stringify(data) ?? '');
            })
        } catch (error) {
            hilog.error(0x0000, 'developTag', 'VPN setUp fail: %{public}s', JSON.stringify(error) ?? '');
        }
```

#### protect

protect(socketFd: number): Promise<void>

保护套接字不受VPN连接影响，通过该套接字发送的数据将直接基于物理网络收发，因此其流量不会通过VPN转发。使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetManager.Vpn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| socketFd | number | 是 | 指定保护的 socketfd，该文件描述符通过getSocketFd获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[VPN错误码](VPN错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2200001 | Invalid parameter value. |
| 2200002 | Operation failed. Cannot connect to service. |
| 2200003 | System internal error. |
| 2203004 | Invalid socket file descriptor. |

**示例：**

```ets
import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
import { common, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let g_tunnelFd = -1;
let context: vpnExtension.VpnExtensionContext;
export default class MyVpnExtAbility extends VpnExtensionAbility {
  private vpnServerIp: string = '192.168.31.13';
  onCreate(want: Want) {
    let vpnConnection : vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
    console.info("VPN createVpnConnection: " + JSON.stringify(vpnConnection));
    this.CreateTunnel();
    this.Protect();
  }
  CreateTunnel() {
      g_tunnelFd = 8888;
  }
  Protect() {
        hilog.info(0x0000, 'developTag', '%{public}s', 'VPN Protect');
        let vpnConnection : vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
        vpnConnection.protect(g_tunnelFd).then(() => {
            hilog.info(0x0000, 'developTag', '%{public}s', 'VPN Protect Success');
        }).catch((err : Error) => {
            hilog.error(0x0000, 'developTag', 'VPN Protect Failed %{public}s', JSON.stringify(err) ?? '');
        })
  }
```

#### destroy

destroy(): Promise<void>

销毁启动的VPN网络。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Vpn

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[VPN错误码](VPN错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2200002 | Operation failed. Cannot connect to service. |
| 2200003 | System internal error. |

**示例：**

```ets
import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context: vpnExtension.VpnExtensionContext;
export default class MyVpnExtAbility extends VpnExtensionAbility {
  onCreate(want: Want) {
    let vpnConnection : vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
    console.info("VPN createVpnConnection: " + JSON.stringify(vpnConnection));
    vpnConnection.destroy().then(() => {
      console.info("destroy success.");
    }).catch((error : BusinessError) => {
      console.error("destroy fail" + JSON.stringify(error));
    });
  }
```

#### destroy20+

destroy(vpnId: string): Promise<void>

根据vpnId销毁指定的VPN网络。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Vpn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vpnId | string | 是 | vpn唯一标识。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[VPN错误码](VPN错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19900001 | Invalid parameter value. |
| 19900002 | System internal error. |

**示例：**

```ets
import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
import { BusinessError } from "@kit.BasicServicesKit";

export default class MyVpnExtAbility extends VpnExtensionAbility {
  onCreate() {
    let vpnConnection = vpnExtension.createVpnConnection(this.context);

    // 可通过generateVpnId()获取vpnId
    let vpnId = 'testVpnId';
    vpnConnection.destroy(vpnId).then(() => {
      console.info("destroy success");
    }).catch((error: BusinessError) => {
      console.error(`destroy fail, Code is ${error.code}, message is ${error.message}`);
    });
  }
```

#### generateVpnId20+

generateVpnId(): Promise<string>

生成VPN唯一标识。使用Promise异步回调。

如需使用系统多VPN能力，需调用该接口生成vpnId，配置到VpnConfig中。

**系统能力**：SystemCapability.Communication.NetManager.Vpn

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 以Promise形式返回获取结果，返回vpnId。 |

**错误码：**

以下错误码的详细介绍请参见[VPN错误码](VPN错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19900001 | Invalid parameter value. |
| 19900002 | System internal error. |

**示例：**

```ets
import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
import { BusinessError } from "@kit.BasicServicesKit";

export default class MyVpnExtAbility extends VpnExtensionAbility {
  onCreate() {
    let vpnConnection = vpnExtension.createVpnConnection(this.context);
    vpnConnection.generateVpnId().then((data) => {
      if (data) {
        console.info("generateVpnId success, vpnId = " + JSON.stringify(data));
      }
    }).catch((error: BusinessError) => {
      console.error(`generateVpnId fail, Code is ${error.code}, message is ${error.message}`);
    });
  }
```

#### protectProcessNet22+

protectProcessNet(): Promise<void>

保护应用进程不受VPN连接影响，被保护的进程直接基于物理网络收发数据，流量不通过VPN转发。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Vpn

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```ets
import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let g_tunnelFd = -1;
export default class MyVpnExtAbility  extends VpnExtensionAbility {
  onCreate() {
    let vpnConnection = vpnExtension.createVpnConnection(this.context);
    console.info("VPN createVpnConnection: " + JSON.stringify(vpnConnection));
    this.ProtectNetByProcess();
  }
  CreateTunnel() {
    g_tunnelFd = 8888;
  }
  ProtectNetByProcess() {
    hilog.info(0x0000, 'developTag', '%{public}s', 'vpn ProtectNetByProcess');
    let vpnConnection = vpnExtension.createVpnConnection(this.context);
    vpnConnection.protectProcessNet().then(() => {
      hilog.info(0x0000, 'developTag', '%{public}s', 'vpn ProtectNetByProcess Success');
      this.CreateTunnel();
    }).catch((err: Error) => {
      hilog.error(0x0000, 'developTag', 'vpn ProtectNetByProcess Failed %{public}s', JSON.stringify(err) ?? '');
    })
  }
```

#### VpnConfig

三方VPN配置参数。

**系统能力**：SystemCapability.Communication.NetManager.Vpn

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| addresses | Array<LinkAddress> | 否 | 否 | VPN虚拟网卡的IP地址。API version 23之前，最多支持64个IP地址；从API version 23开始，最多支持2000个IP地址。 |
| vpnId20+ | string | 否 | 是 | VPN唯一标识。 |
| routes | Array<RouteInfo> | 否 | 是 | VPN虚拟网卡的路由信息（API version 23前最多可配置1024条路由；从API version 23开始最多可配置10000条路由）。 |
| dnsAddresses | Array<string> | 否 | 是 | DNS服务器地址信息。当配置DNS服务器地址后，VPN启动状态下被代理的应用上网时，使用配置的DNS服务器做DNS查询。 |
| searchDomains | Array<string> | 否 | 是 | DNS的搜索域列表。 |
| mtu | number | 否 | 是 | 最大传输单元MTU值（单位：字节）。取值范围：[576，1500]。 |
| isIPv4Accepted | boolean | 否 | 是 | 是否支持IPv4。true表示支持，false表示不支持, 默认值为true。 注意：若支持IPv4功能，需要在addresses中配置IPv4类型的IP地址。 |
| isIPv6Accepted | boolean | 否 | 是 | 是否支持IPv6。true表示支持，false表示不支持, 默认值为false。 注意：若支持IPv6功能，需要在addresses中配置IPv6类型的IP地址。 |
| isInternal | boolean | 否 | 是 | 是否支持内置VPN。true表示支持，false表示不支持, 默认值为false。 |
| isBlocking | boolean | 否 | 是 | 是否阻塞模式。true表示阻塞模式，false表示非阻塞模式, 默认值为false。 |
| trustedApplications | Array<string> | 否 | 是 | 受信任的应用信息列表，string类型表示的包名。当配置该列表后，仅该列表中的应用数据才能根据routes被VPN代理。 注意：trustedApplications和blockedApplications列表不能同时配置。 |
| blockedApplications | Array<string> | 否 | 是 | 被阻止的应用信息列表，string类型表示的包名。当配置该列表后，该列表中的应用数据不会被VPN代理，其他应用可以根据routes配置被VPN代理。 注意：trustedApplications和blockedApplications列表不能同时配置。 |

**示例：**

```ets
import { vpnExtension} from '@kit.NetworkKit';

let vpnConfig: vpnExtension.VpnConfig = {
  addresses: [],
  vpnId: '123',
  routes: [{
    interface: "eth0",
    destination: {
      address: {
        address:'',
        family:1,
        port:8080
      },
      prefixLength:1
    },
    gateway: {
      address:'',
      family:1,
      port:8080
    },
    hasGateway: true,
    isDefaultRoute: true,
  }],
  mtu: 1400,
  dnsAddresses: ["223.5.5.5", "223.6.6.6"],
  trustedApplications: [],
  blockedApplications: [],
}
let context: vpnExtension.VpnExtensionContext;

function vpnCreate(){
  let vpnConnection: vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
  vpnConnection.create(vpnConfig).then((data) => {
    console.info("VPN create " + JSON.stringify(data));
  })
}
```