[]()[]()

# Interfaces (其他)

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### StoreConfig

管理关系数据库配置。

名称类型只读可选说明namestring否否

数据库文件名，也是数据库唯一标识符。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

securityLevel[SecurityLevel](../../topics/networking/Enums (arkts-apis-data-relationalstore-e).md#ZH-CN_TOPIC_0000002497604686__securitylevel)否否

设置数据库安全级别。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

encryptboolean否是

指定数据库是否加密，默认不加密。

true：加密。

false：非加密。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

dataGroupId10+string否是

应用组ID，需要向应用市场获取，详见[dataGroupId申请流程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ime-kit-security#section4219152220459)。基于dataGroupId的数据共享支持两种场景：1.同一应用的不同进程间共享，只支持三方应用中输入法和输入法的扩展场景使用；2.不同应用间的数据共享，只支持系统应用使用。

**模型约束：** 此属性仅在Stage模型下可用。

从API version 10开始，支持此可选参数。dataGroupId共享沙箱的方式不支持多进程访问加密数据库，当此参数不填时，默认在本应用沙箱目录下创建RdbStore实例。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

customDir11+string否是

数据库自定义路径。

**使用约束：** 数据库路径大小限制为128字节，如果超过该大小会开库失败，返回错误。

从API version 11开始，支持此可选参数。数据库将在如下的目录结构中被创建：context.databaseDir + "/rdb/" + customDir，其中context.databaseDir是应用沙箱对应的路径，"/rdb/"表示创建的是关系型数据库，customDir表示自定义的路径。当此参数不填时，默认在本应用沙箱目录下创建RdbStore实例。从API version 18开始，如果同时配置了rootDir参数，将打开或删除如下路径数据库：rootDir + "/" + customDir + "/" + name。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

rootDir18+string否是

指定数据库根路径。

从API version 18开始，支持此可选参数。将从如下目录打开或删除数据库：rootDir + "/" + customDir。通过设置此参数打开的数据库为只读模式，不允许对数据库进行写操作，否则返回错误码801。配置此参数打开或删除数据库时，应确保对应路径下数据库文件存在，并且有读取权限，否则返回错误码14800010。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

autoCleanDirtyData11+boolean否是

指定是否自动清理云端删除后同步到本地的数据，true表示自动清理，false表示手动清理，默认自动清理。

对于端云协同的数据库，当云端删除的数据同步到设备端时，可通过该参数设置设备端是否自动清理。手动清理可以通过[cleanDirtyData11+](Interface (RdbStore).md#ZH-CN_TOPIC_0000002529444649__cleandirtydata11)接口清理。

从API version 11开始，支持此可选参数。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

allowRebuild12+boolean否是

指定数据库是否支持异常时自动删除，并重建一个空库空表，默认不删除。

true：自动删除。

false：不自动删除。

从API version 12开始，支持此可选参数。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

isReadOnly12+boolean否是

指定数据库是否只读，默认为数据库可读写。

true：只允许从数据库读取数据，不允许对数据库进行写操作，否则会返回错误码801。

false：允许对数据库进行读写操作。

从API version 12开始，支持此可选参数。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

pluginLibs12+Array<string>否是

配置加载自定义动态库，数组中可传入多个动态库名称。具体请见[pluginLibs的使用约束和示例](#ZH-CN_TOPIC_0000002529284677__pluginlibs的使用约束和示例)。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

cryptoParam14+[CryptoParam](#ZH-CN_TOPIC_0000002529284677__cryptoparam14)否是

指定用户自定义的加密参数。

当此参数不填时，使用默认的加密参数，见[CryptoParam](#ZH-CN_TOPIC_0000002529284677__cryptoparam14)各参数默认值。

此配置只有在encrypt选项设置为真或密钥非空时才有效。

从API version 14开始，支持此可选参数。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

vector18+boolean否是

指定数据库是否是向量数据库，true表示向量数据库，false表示关系型数据库，默认为false。

向量数据库适用于存储和处理高维向量数据，关系型数据库适用于存储和处理结构化数据。

当使用向量数据库时，在调用deleteRdbStore接口前，应当确保向量数据库已打开的RdbStore和ResultSet均已成功关闭。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

tokenizer17+[Tokenizer](../../topics/networking/Enums (arkts-apis-data-relationalstore-e).md#ZH-CN_TOPIC_0000002497604686__tokenizer17)否是

指定用户在fts场景下使用哪种分词器。

当此参数不填时，则在fts下不支持中文以及多国语言分词，但仍可支持英文分词。

如果用户想使用自定义分词器，可以通过pluginLibs参数进行配置，具体请见[pluginLibs的使用约束和示例](#ZH-CN_TOPIC_0000002529284677__pluginlibs的使用约束和示例)。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

persist18+boolean否是

指定数据库是否需要持久化。true表示持久化，false表示不持久化，即内存数据库。默认为true。

内存数据库不支持加密、backup、restore、跨进程访问及分布式能力，securityLevel属性会被忽略。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

enableSemanticIndex20+boolean否是

指定数据库是否启用语义索引处理功能。true表示启用语义索引处理功能，false表示不启用。默认为false。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

[]()[]()

#### CryptoParam14+

数据库加密参数配置。此配置只有在StoreConfig的encrypt选项设置为true或密钥非空时有效。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称类型只读可选说明encryptionKeyUint8Array否否

指定数据库加/解密使用的密钥。

如传入密钥为空，则由数据库负责生成并保存密钥，并使用生成的密钥打开数据库文件。

使用完后用户需要将密钥内容全部置为零。

iterationCountnumber否是

整数类型，指定数据库PBKDF2算法的迭代次数，默认值为10000。

迭代次数应当为大于零的整数，若非整数则向下取整。

不指定此参数或指定为零时，使用默认值10000，并使用默认加密算法AES_256_GCM。

encryptionAlgo[EncryptionAlgo](../../topics/networking/Enums (arkts-apis-data-relationalstore-e).md#ZH-CN_TOPIC_0000002497604686__encryptionalgo14)否是指定数据库加解密使用的加密算法。如不指定，默认值为 AES_256_GCM。hmacAlgo[HmacAlgo](../../topics/networking/Enums (arkts-apis-data-relationalstore-e).md#ZH-CN_TOPIC_0000002497604686__hmacalgo14)否是指定数据库加解密使用的HMAC算法。如不指定，默认值为SHA256。kdfAlgo[KdfAlgo](../../topics/networking/Enums (arkts-apis-data-relationalstore-e).md#ZH-CN_TOPIC_0000002497604686__kdfalgo14)否是指定数据库加解密使用的PBKDF2算法。如不指定，默认使用和HMAC算法相等的算法。cryptoPageSizenumber否是

整数类型，指定数据库加解密使用的页大小。如不指定，默认值为1024字节。

用户指定的页大小应为1024到65536范围内的整数，并且为2n。若指定值非整数，则向下取整。

[]()[]()

#### Asset10+

记录资产附件（文件、图片、视频等类型文件）的相关信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称类型只读可选说明namestring否否资产的名称。uristring否否资产的uri，在系统里的绝对路径。pathstring否否资产在应用沙箱里的路径。createTimestring否否资产被创建出来的时间。modifyTimestring否否资产最后一次被修改的时间。sizestring否否资产占用空间的大小。在端云同步机制中，本字段作为判定资产是否发生变更的关键依据之一，需确保在全链路中保持统一、一致的存储格式与取值逻辑。建议所有系统节点均采用标准化处理方式（单位为字节（Byte），取值为非负整数），避免因格式差异导致同步异常或误判。status[AssetStatus](../../topics/networking/Enums (arkts-apis-data-relationalstore-e).md#ZH-CN_TOPIC_0000002497604686__assetstatus10)否是资产的状态，默认值为ASSET_NORMAL。[]()[]()

#### ChangeInfo10+

记录端云同步过程详情。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称类型只读可选说明tablestring否否表示发生变化的表的名称。type[ChangeType](../../topics/networking/Enums (arkts-apis-data-relationalstore-e).md#ZH-CN_TOPIC_0000002497604686__changetype10)否否表示发生变化的数据的类型，数据或者资产附件发生变化。insertedArray<string> | Array<number>否否记录插入数据的位置，如果该表的主键是string类型，该值是主键的值，否则该值表示插入数据的行号。updatedArray<string> | Array<number>否否记录更新数据的位置，如果该表的主键是string类型，该值是主键的值，否则该值表示更新数据的行号。deletedArray<string> | Array<number>否否记录删除数据的位置，如果该表的主键是string类型，该值是主键的值，否则该值表示删除数据的行号。[]()[]()

#### DistributedConfig10+

记录表的分布式配置信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称类型只读可选说明autoSyncboolean否否该值为true时，表示该表支持自动同步和手动同步；该值为false时，表示该表只支持手动同步，不支持自动同步。asyncDownloadAsset18+boolean否是表示当前数据库在端云同步时，同步或异步下载资产。true表示优先下载完所有数据后，使用异步任务下载资产；false表示同步下载资产；默认值为false。enableCloud18+boolean否是表示当前数据库是否允许端云同步。true表示允许端云同步；false表示不允许端云同步。默认值为true。[]()[]()

#### Statistic10+

描述数据库表的端云同步过程的统计信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称类型只读可选说明totalnumber否否表示数据库表中需要端云同步的总行数。successfulnumber否否表示数据库表中端云同步成功的行数。failednumber否否表示数据库表中端云同步失败的行数。remainednumber否否表示数据库表中端云同步剩余未执行的行数。[]()[]()

#### TableDetails10+

描述数据库表执行端云同步任务上传和下载的统计信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称类型只读可选说明upload[Statistic](Interfaces (其他) (arkts-apis-data-relationalstore-i).md#ZH-CN_TOPIC_0000002529284677__statistic10)否否表示数据库表中端云同步上传过程的统计信息。download[Statistic](Interfaces (其他) (arkts-apis-data-relationalstore-i).md#ZH-CN_TOPIC_0000002529284677__statistic10)否否表示数据库表中端云同步下载过程的统计信息。[]()[]()

#### ProgressDetails10+

描述数据库整体执行端云同步任务上传和下载的统计信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称类型只读可选说明schedule[Progress](../../topics/networking/Enums (arkts-apis-data-relationalstore-e).md#ZH-CN_TOPIC_0000002497604686__progress10)否否表示端云同步过程。code[ProgressCode](../../topics/networking/Enums (arkts-apis-data-relationalstore-e).md#ZH-CN_TOPIC_0000002497604686__progresscode10)否否表示端云同步过程的状态。detailsRecord<string, [TableDetails](#ZH-CN_TOPIC_0000002529284677__tabledetails10)>否否

表示端云同步各表的统计信息。

键表示表名，值表示该表的端云同步过程统计信息。

[]()[]()

#### SqlExecutionInfo12+

描述数据库执行的SQL语句的统计信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称类型只读可选说明sqlArray<string>否否表示执行的SQL语句的数组。当[batchInsert](Interface (RdbStore).md#ZH-CN_TOPIC_0000002529444649__batchinsert)的参数太大时，可能有多个SQL。totalTimenumber否否表示执行SQL语句的总时间，单位为μs。waitTimenumber否否表示获取句柄的时间，单位为μs。prepareTimenumber否否表示准备SQL和绑定参数的时间，单位为μs。executeTimenumber否否表示执行SQL语句的时间，单位为μs。[]()[]()

#### SqlInfo20+

描述数据库执行的SQL语句的详细信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称类型只读可选说明sqlstring否否表示执行的sql语句。argsArray<[ValueType](../../topics/networking/Types (arkts-apis-data-relationalstore-t).md#ZH-CN_TOPIC_0000002497444708__valuetype)>否否表示执行SQL中的参数信息。[]()[]()

#### ExceptionMessage20+

描述数据库执行的SQL语句的错误信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称类型只读可选说明codenumber否否表示执行SQL返回的错误码，对应的取值和含义请见[sqlite错误码](https://www.sqlite.org/rescode.html)messagestring否否表示执行SQL返回的错误信息。sqlstring否否表示报错执行的SQL语句。[]()[]()

#### TransactionOptions14+

事务对象的配置信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称类型只读可选说明transactionType[TransactionType](../../topics/networking/Enums (arkts-apis-data-relationalstore-e).md#ZH-CN_TOPIC_0000002497604686__transactiontype14)否是事务类型。默认为DEFERRED。[]()[]()

#### pluginLibs的使用约束和示例

**使用约束：**

1. 动态库名的数量限制最多为16个，如果超过该数量会开库失败，返回错误码14800000。

2. 动态库名需为本应用沙箱路径下或系统路径下的动态库，如果动态库无法加载会开库失败，返回错误码14800010。

3. 动态库名需为完整路径，用于被sqlite加载。路径由[context.bundleCodeDir+ "/libs/arm64/" + so名称]组成，其中context.bundleCodeDir是应用沙箱对应的路径，"libs"是固定目录，"arm64"是由系统架构确定的子目录，例如，系统架构为arm64-v8a时，子目录为"arm64"。

样例：[context.bundleCodeDir+ "/libs/arm64/" + libtokenizer.so]。当此参数不填时，默认不加载动态库。

4. 动态库需要包含其全部依赖，避免依赖项丢失导致无法运行。

例如：在ndk工程中，使用默认编译参数构建libtokenizer.so，此动态库依赖c++标准库。在加载此动态库时，由于namespace与编译时不一致，链接到了错误的libc++_shared.so，导致__emutls_get_address符号找不到。要解决此问题，需在编译时静态链接c++标准库，具体请参见[NDK工程构建概述](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/build-with-ndk-overview)。

**使用pluginLibs加载开发者自定义分词器示例：**

1. 开发者需要实现一个fts5可加载分词器扩展，并将其编译成so，编译可参考[使用命令行CMake构建NDK工程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/build-with-ndk-cmake)。

2. 将生成的so文件拷贝到工程目录"entry/libs/"文件夹下的相应子目录中(没有相应目录时用户可自行创建)，子目录根据系统架构确定。例如，系统架构为arm64-v8a时，放置在"entry/libs/arm64-v8a"目录下；系统架构为armeabi-v7a时，放置在"entry/libs/armeabi-v7a"目录下。

3. 加载自定义分词器。

```ets
import relationalStore from '@ohos.data.relationalStore'
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import fs from '@ohos.file.fs';

export default class EntryAbility extends UIAbility {
  async onWindowStageCreate(windowStage: window.WindowStage) {
    let rdbStore: relationalStore.RdbStore | undefined = undefined;
    const STORE_CONFIG: relationalStore.StoreConfig = {
      name: "testTokenize.db",
      securityLevel: relationalStore.SecurityLevel.S1,
    };
    let bundleCodeDir = this.context.bundleCodeDir;
    // libdistributeddb_extension.so为实现的fts5可加载分词器扩展编译成的so名称
    let soPath = bundleCodeDir + "/libs/arm64/libdistributeddb_extension.so";
    let res = await fs.access(soPath);
    if (!res) {
      console.error("Dynamic library not accessible");
      return;
    }
    console.info("Dynamic library found and accessible");

    // 将pluginLibs配置为需要加载的动态库拓展路径。
    STORE_CONFIG.pluginLibs = [soPath];
    try {
      rdbStore = await relationalStore.getRdbStore(this.context, STORE_CONFIG);
      // 使用自定义分词器创建fts5虚拟表，tokenize后面是实现的分词器名称
      await rdbStore.executeSql("CREATE VIRTUAL TABLE IF NOT EXISTS pages USING fts5(title, keywords, body, tokenize=koowork_tokenizer);");
      console.info("CREATE VIRTUAL TABLE OK");
      await rdbStore.executeSql("INSERT INTO pages(keywords, title, body) VALUES('歌曲', 'xxx', '1234歌曲，像北哈升');");
      console.info("INSERT VIRTUAL TABLE OK, body is '1234歌曲，像北哈升'");
      await rdbStore.executeSql("INSERT INTO pages(keywords, title, body) VALUES('歌曲', 'xxx', '我爱北京天安门, 天安门上太阳升');");
      console.info("INSERT VIRTUAL TABLE OK, body is '我爱北京天安门, 天安门上太阳升'");
      let resultSet = await rdbStore.querySql("select * from pages where body match '天安门';");
      while (resultSet.goToNextRow()) {
        console.info(`query result success, match body:${resultSet.getString(resultSet.getColumnIndex("body"))}`);
      }
      resultSet.close();
      await rdbStore.close();
    } catch (err) {
      console.error("RdbStore failed, err: code=" + err.code + " message=" + err.message);
    }
  }
}
```