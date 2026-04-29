# @ohos.deviceInfo (设备信息)

本模块提供终端设备信息查询，开发者不可配置。

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

部分参数返回值为default的，会在正式发布的版本中配置。

本模块接口返回设备常量信息，建议应用只调用一次，不需要频繁调用。

#### 导入模块

```ets
import { deviceInfo } from '@kit.BasicServicesKit';
```

#### 常量

未特殊说明的字段，数据长度最大值为96字节。

**系统能力**：SystemCapability.Startup.SystemInfo。

**权限**：以下各项所需要的权限有所不同，详见下表。

| 名称 | 类型 | 只读 | 说明 |
| --- | --- | --- | --- |
| deviceType | string | 是 | 设备类型。详细请参考deviceTypes标签。 元服务API：从API version 11开始，该接口支持在元服务中使用。 示例：phone |
| manufacture | string | 是 | 设备厂家名称。 示例：HUAWEI |
| brand | string | 是 | 设备品牌名称。 元服务API：从API version 11开始，该接口支持在元服务中使用。 示例：HUAWEI |
| marketName | string | 是 | 外部产品系列。 示例：HUAWEI Mate 60 Pro |
| productSeries | string | 是 | 产品系列。 示例：ALN |
| productModel | string | 是 | 认证型号。 元服务API：从API version 11开始，该接口支持在元服务中使用。 示例：ALN-AL00 |
| productModelAlias14+ | string | 是 | 认证型号别名。 元服务API：从API version 14开始，该接口支持在元服务中使用。 示例：TAS-AL00 |
| softwareModel | string | 是 | 内部软件子型号。 示例：ALN-AL00 |
| hardwareModel | string | 是 | 硬件版本号。 示例：HL1CMSM |
| hardwareProfile(deprecated) | string | 是 | 硬件Profile。 说明： 从API version 6 开始支持，从API version 9 开始废弃，建议使用syscap能力替代。 示例：default |
| serial | string | 是 | 设备序列号SN(Serial Number)。 说明：可作为设备唯一识别码。 需要权限：ohos.permission.sec.ACCESS_UDID(该权限只允许系统应用及企业定制应用申请) 示例：序列号随设备差异 |
| bootloaderVersion | string | 是 | Bootloader版本号。 示例：bootloader |
| abiList | string | 是 | 应用二进制接口（Abi）。 示例：arm64-v8a |
| securityPatchTag | string | 是 | 安全补丁级别。 示例：2024/1/1 |
| displayVersion | string | 是 | 产品版本。 示例：ALN-AL00 5.0.0.1(XXX) |
| incrementalVersion | string | 是 | 差异版本号。 示例：default |
| osReleaseType | string | 是 | 系统的发布类型，取值为： - Canary：面向特定开发者发布的早期预览版本，不承诺API稳定性。 - Beta：面向开发者公开发布的Beta版本，不承诺API稳定性。 - Release：面向开发者公开发布的正式版本，承诺API稳定性。 示例：Canary1/Beta2/Release |
| osFullName | string | 是 | 系统版本，版本格式OpenHarmony-x.x.x.x,x为数值。 元服务API：从API version 11开始，该接口支持在元服务中使用。 示例：OpenHarmony-5.0.0.1(Canary1) |
| majorVersion | number | 是 | Major版本号，随主版本更新增加，值为osFullName中的第一位数值，建议直接使用deviceInfo.majorVersion获取，可提升效率，不建议开发者解析osFullName获取。 示例：5 |
| seniorVersion | number | 是 | Senior版本号，随局部架构、重大特性增加，值为osFullName中的第二位数值，建议直接使用deviceInfo.seniorVersion获取，可提升效率，不建议开发者自主解析osFullName获取。 示例：0 |
| featureVersion | number | 是 | Feature版本号，标识规划的新特性版本，值为osFullName中的第三位数值，建议直接使用deviceInfo.featureVersion获取，可提升效率，不建议开发者自主解析osFullName获取。 示例：0 |
| buildVersion | number | 是 | Build版本号，标识编译构建的版本号，值为osFullName中的第四位数值，建议直接使用deviceInfo.buildVersion获取，可提升效率，不建议开发者自主解析osFullName获取。 示例：1 |
| sdkApiVersion | number | 是 | 系统软件API版本。 元服务API：从API version 14开始，该接口支持在元服务中使用。 示例：12 |
| firstApiVersion | number | 是 | 首个版本系统软件API版本。 示例：3 |
| versionId | string | 是 | 版本ID。由deviceType、manufacture、brand、productSeries、osFullName、productModel、softwareModel、sdkApiVersion、incrementalVersion、buildType拼接组成。 示例：wearable/HUAWEI/HUAWEI/TAS/OpenHarmony-5.0.0.1/TAS-AL00/TAS-AL00/12/default/release:nolog |
| buildType | string | 是 | 构建类型。 示例：default |
| buildUser | string | 是 | 构建用户。 示例：default |
| buildHost | string | 是 | 构建主机。 示例：default |
| buildTime | string | 是 | 构建时间。 示例：default |
| buildRootHash | string | 是 | 构建版本Hash。 示例：default |
| udid7+ | string | 是 | 设备Udid。 说明：数据长度为65字节。可作为设备唯一识别码。 需要权限：ohos.permission.sec.ACCESS_UDID(该权限只允许系统应用及企业类应用申请) 示例：9D6AABD147XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXE5536412 |
| distributionOSName10+ | string | 是 | 发行版系统名称。 示例：OpenHarmony |
| distributionOSVersion10+ | string | 是 | 发行版系统版本号。格式为x.x.x，x是数字 示例：5.0.0 |
| distributionOSApiVersion10+ | number | 是 | 发行版系统api版本。 示例：50001 |
| distributionOSApiName13+ | string | 是 | 发行版系统api版本名称。 |
| distributionOSReleaseType10+ | string | 是 | 发行版系统类型。 示例：Release |
| ODID12+ | string | 是 | 开发者匿名设备标识符。 ODID值会在以下场景重新生成： 手机恢复出厂设置。 同一设备上同一个开发者(developerId相同)的应用全部卸载后重新安装时。 ODID生成规则： 根据签名信息里developerId解析出的groupId生成，developerId规则为groupId.developerId，若无groupId则取整个developerId作为groupId。 同一设备上运行的同一个开发者(developerId相同)的应用，ODID相同。 同一个设备上不同开发者(developerId不同)的应用，ODID不同。 不同设备上同一个开发者(developerId相同)的应用，ODID不同。 不同设备上不同开发者(developerId不同)的应用，ODID不同。 说明：数据长度为37字节(包含结束符)。 示例：1234a567-XXXX-XXXX-XXXX-XXXXXXXXXXXX |
| diskSN15+ | string | 是 | 硬盘序列号。 说明 ：该字段只能在2in1上设备进行查询，其他设备查询结果为空。 需要权限：ohos.permission.ACCESS_DISK_PHY_INFO 示例：2502EM400567 |
| performanceClass19+ | PerformanceClassLevel | 是 | 描述设备能力等级，基于CPU、内存、存储读写性能和屏幕分辨率等因素综合评估。 |
| chipType21+ | string | 是 | 当前设备CPU芯片型号 示例：xxxxx |
| bootCount21+ | number | 是 | 当前设备重启次数，获取失败时返回-1 示例：100 |

**示例**

```ets
    import { deviceInfo } from '@kit.BasicServicesKit';

    let deviceTypeInfo: string = deviceInfo.deviceType;
    // 输出结果：the value of the deviceType is :wearable
    console.info('the value of the deviceType is :' + deviceTypeInfo);

    let manufactureInfo: string = deviceInfo.manufacture;
    // 输出结果：the value of the manufacture is :HUAWEI
    console.info('the value of the manufactureInfo is :' + manufactureInfo);

    let brandInfo: string = deviceInfo.brand;
    // 输出结果：the value of the brand is :HUAWEI
    console.info('the value of the device brand is :' + brandInfo);

    let marketNameInfo: string = deviceInfo.marketName;
    // 输出结果：the value of the marketName is :Mate XX
    console.info('the value of the deviceInfo marketName is :' + marketNameInfo);

    let productSeriesInfo: string = deviceInfo.productSeries;
    // 输出结果：the value of the productSeries is :TAS
    console.info('the value of the deviceInfo productSeries is :' + productSeriesInfo);

    let productModelInfo: string = deviceInfo.productModel;
    // 输出结果：the value of the productModel is :TAS-AL00
    console.info('the value of the deviceInfo productModel is :' + productModelInfo);

    let productModelAliasInfo: string = deviceInfo.productModelAlias;
    console.info('the value of the deviceInfo productModelAlias is :' + productModelAliasInfo);

    let softwareModelInfo: string = deviceInfo.softwareModel;
    // 输出结果：the value of the softwareModel is :TAS-AL00
    console.info('the value of the deviceInfo softwareModel is :' + softwareModelInfo);

    let hardwareModelInfo: string = deviceInfo.hardwareModel;
    // 输出结果：the value of the hardwareModel is :TASA00CVN1
    console.info('the value of the deviceInfo hardwareModel is :' + hardwareModelInfo);

    let serialInfo: string = deviceInfo.serial;
    // 输出结果：the value of the serial is :序列号随设备差异
    console.info('the value of the deviceInfo serial is :' + serialInfo);

    let bootloaderVersionInfo: string = deviceInfo.bootloaderVersion;
    // 输出结果：the value of the bootloaderVersion is :bootloader
    console.info('the value of the deviceInfo bootloaderVersion is :' + bootloaderVersionInfo);

    let abiListInfo: string = deviceInfo.abiList;
    // 输出结果：the value of the abiList is :arm64-v8a
    console.info('the value of the deviceInfo abiList is :' + abiListInfo);

    let securityPatchTagInfo: string = deviceInfo.securityPatchTag;
    // 输出结果：the value of the securityPatchTag is :2021/01/01
    console.info('the value of the deviceInfo securityPatchTag is :' + securityPatchTagInfo);

    let displayVersionInfo: string = deviceInfo.displayVersion;
    // 输出结果：the value of the displayVersion is :XXX X.X.X.X
    console.info('the value of the deviceInfo displayVersion is :' + displayVersionInfo);

    let incrementalVersionInfo: string = deviceInfo.incrementalVersion;
    // 输出结果：the value of the incrementalVersion is :default
    console.info('the value of the deviceInfo incrementalVersion is :' + incrementalVersionInfo);

    let osReleaseTypeInfo: string = deviceInfo.osReleaseType;
    // 输出结果：the value of the osReleaseType is :Release
    console.info('the value of the deviceInfo osReleaseType is :' + osReleaseTypeInfo);

    let osFullNameInfo: string = deviceInfo.osFullName;
    // 输出结果：the value of the osFullName is :OpenHarmony-5.0.0.1
    console.info('the value of the deviceInfo osFullName is :' + osFullNameInfo);

    let majorVersionInfo: number = deviceInfo.majorVersion;
    // 输出结果：the value of the majorVersion is :5
    console.info('the value of the deviceInfo majorVersion is :' + majorVersionInfo);

    let seniorVersionInfo: number = deviceInfo.seniorVersion;
    // 输出结果：the value of the seniorVersion is :0
    console.info('the value of the deviceInfo seniorVersion is :' + seniorVersionInfo);

    let featureVersionInfo: number = deviceInfo.featureVersion;
    // 输出结果：the value of the featureVersion is :0
    console.info('the value of the deviceInfo featureVersion is :' + featureVersionInfo);

    let buildVersionInfo: number = deviceInfo.buildVersion;
    // 输出结果：the value of the buildVersion is :1
    console.info('the value of the deviceInfo buildVersion is :' + buildVersionInfo);

    let sdkApiVersionInfo: number = deviceInfo.sdkApiVersion;
    // 输出结果：the value of the sdkApiVersion is :12
    console.info('the value of the deviceInfo sdkApiVersion is :' + sdkApiVersionInfo);

    let firstApiVersionInfo: number = deviceInfo.firstApiVersion;
    // 输出结果：the value of the firstApiVersion is :3
    console.info('the value of the deviceInfo firstApiVersion is :' + firstApiVersionInfo);

    let versionIdInfo: string = deviceInfo.versionId;
    // 输出结果：the value of the versionId is :wearable/HUAWEI/HUAWEI/TAS/OpenHarmony-5.0.0.1/TAS-AL00/TAS-AL00/12/default/release:nolog
    console.info('the value of the deviceInfo versionId is :' + versionIdInfo);

    let buildTypeInfo: string = deviceInfo.buildType;
    // 输出结果：the value of the buildType is :default
    console.info('the value of the deviceInfo buildType is :' + buildTypeInfo);

    let buildUserInfo: string = deviceInfo.buildUser;
    // 输出结果：the value of the buildUser is :default
    console.info('the value of the deviceInfo buildUser is :' + buildUserInfo);

    let buildHostInfo: string = deviceInfo.buildHost;
    // 输出结果：the value of the buildHost is :default
    console.info('the value of the deviceInfo buildHost is :' + buildHostInfo);

    let buildTimeInfo: string = deviceInfo.buildTime;
    // 输出结果：the value of the buildTime is :default
    console.info('the value of the deviceInfo buildTime is :' + buildTimeInfo);

    let buildRootHashInfo: string = deviceInfo.buildRootHash;
    // 输出结果：the value of the buildRootHash is :default
    console.info('the value of the deviceInfo buildRootHash is :' + buildRootHashInfo);

    let udid: string = deviceInfo.udid;
    // 输出结果：the value of the udid is :9D6AABD147XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXE5536412
    console.info('the value of the deviceInfo udid is :' + udid);

    let distributionOSName: string = deviceInfo.distributionOSName
    // 输出结果：the value of the distributionOSName is :OpenHarmony
    console.info('the value of the deviceInfo distributionOSName is :' + distributionOSName);

    let distributionOSVersion: string = deviceInfo.distributionOSVersion
    // 输出结果：the value of the distributionOSVersion is :5.0.0
    console.info('the value of the deviceInfo distributionOSVersion is :' + distributionOSVersion);

    let distributionOSApiVersion: number = deviceInfo.distributionOSApiVersion
    // 输出结果：the value of the distributionOSApiVersion is :500001
    console.info('the value of the deviceInfo distributionOSApiVersion is :' + distributionOSApiVersion);

    let distributionOSApiName: string = deviceInfo.distributionOSApiName
    console.info('the value of the deviceInfo distributionOSApiName is :' + distributionOSApiName);

    let distributionOSReleaseType: string = deviceInfo.distributionOSReleaseType
    // 输出结果：the value of the distributionOSReleaseType is :Release
    console.info('the value of the deviceInfo distributionOSReleaseType is :' + distributionOSReleaseType);

    let odid: string = deviceInfo.ODID;
    // 输出结果：the value of the ODID is :1234a567-XXXX-XXXX-XXXX-XXXXXXXXXXXX
    console.info('the value of the deviceInfo odid is :' + odid);

    let diskSN: string = deviceInfo.diskSN;
    // 输出结果：the value of the deviceInfo diskSN is :2502EM400567
    console.info('the value of the deviceInfo diskSN is :' + diskSN);

    let performanceClass = deviceInfo.performanceClass;
    // 输出结果：the value of the deviceInfo performanceClass is :0
    console.info('the value of the deviceInfo performanceClass is :' + performanceClass);

    let chipType: string = deviceInfo.chipType;
    // 输出结果：the value of the deviceInfo chipType is :xxxxx
    console.info('the value of the deviceInfo chipType is :' + chipType);

    let bootCount: number = deviceInfo.bootCount
    // 输出结果：the value of the bootCount is :100
    console.info('the value of the deviceInfo bootCount is :' + bootCount);
```

#### PerformanceClassLevel19+

表示设备能力定级的枚举。

**系统能力**：SystemCapability.Startup.SystemInfo

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CLASS_LEVEL_HIGH | 0 | 表示设备能力定级为高。 |
| CLASS_LEVEL_MEDIUM | 1 | 表示设备能力定级为中。 |
| CLASS_LEVEL_LOW | 2 | 表示设备能力定级为低。 |

#### DeviceTypes20+

设备类型枚举值，可用于校验deviceType的返回值。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Startup.SystemInfo

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TYPE_DEFAULT | 'default' | 默认设备。 |
| TYPE_PHONE | 'phone' | 手机。 |
| TYPE_TABLET | 'tablet' | 平板。 |
| TYPE_2IN1 | '2in1' | PC/2in1。 |
| TYPE_TV | 'tv' | 智慧屏。 |
| TYPE_WEARABLE | 'wearable' | 智能手表。 |
| TYPE_CAR | 'car' | 车机。 |

**示例**

```ets
    let deviceTypesInfoDefault: string = deviceInfo.DeviceTypes.TYPE_DEFAULT;
    // 输出结果：the value of the DeviceTypes is :default
    console.info('the value of the DeviceTypes is :' + deviceTypesInfoDefault);

    let deviceTypesInfoPhone: string = deviceInfo.DeviceTypes.TYPE_PHONE;
    // 输出结果：the value of the DeviceTypes is :phone
    console.info('the value of the DeviceTypes is :' + deviceTypesInfoPhone);

    let deviceTypesInfoTablet: string = deviceInfo.DeviceTypes.TYPE_TABLET;
    // 输出结果：the value of the DeviceTypes is :tablet
    console.info('the value of the DeviceTypes is :' + deviceTypesInfoTablet);

    let deviceTypesInfo2IN1: string = deviceInfo.DeviceTypes.TYPE_2IN1;
    // 输出结果：the value of the DeviceTypes is :2in1
    console.info('the value of the DeviceTypes is :' + deviceTypesInfo2IN1);

    let deviceTypesInfoTV: string = deviceInfo.DeviceTypes.TYPE_TV;
    // 输出结果：the value of the DeviceTypes is :tv
    console.info('the value of the DeviceTypes is :' + deviceTypesInfoTV);

    let deviceTypesInfoWearable: string = deviceInfo.DeviceTypes.TYPE_WEARABLE;
    // 输出结果：the value of the DeviceTypes is :wearable
    console.info('the value of the DeviceTypes is :' + deviceTypesInfoWearable);

    let deviceTypesInfoCar: string = deviceInfo.DeviceTypes.TYPE_CAR;
    // 输出结果：the value of the DeviceTypes is :car
    console.info('the value of the DeviceTypes is :' + deviceTypesInfoCar);
```