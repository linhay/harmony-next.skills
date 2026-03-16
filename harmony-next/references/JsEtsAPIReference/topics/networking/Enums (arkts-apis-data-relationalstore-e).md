[]()[]()

# Enums

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### SecurityLevel

数据库的安全级别枚举。请使用枚举名称而非枚举值。数据库的安全等级仅支持由低向高设置，不支持由高向低设置。

若需要进行同步操作，数据库安全等级应不高于对端设备安全等级，具体可见[跨设备同步访问控制机制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sync-app-data-across-devices-overview#跨设备同步访问控制机制)。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称值说明S11表示数据库的安全级别为低级别，当数据泄露时会产生较低影响。例如，包含壁纸等系统数据的数据库。S22表示数据库的安全级别为中级别，当数据泄露时会产生较大影响。例如，包含录音、视频等用户生成数据或通话记录等信息的数据库。S33表示数据库的安全级别为高级别，当数据泄露时会产生重大影响。例如，包含用户运动、健康、位置等信息的数据库。S44表示数据库的安全级别为关键级别，当数据泄露时会产生严重影响。例如，包含认证凭据、财务数据等信息的数据库。[]()[]()

#### EncryptionAlgo14+

数据库的加密方式枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称值说明AES_256_GCM0数据库使用AES_256_GCM加密。AES_256_CBC1数据库使用AES_256_CBC加密。PLAIN_TEXT22+2数据库不进行加密。[]()[]()

#### HmacAlgo14+

数据库的HMAC算法枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称值说明SHA10HMAC_SHA1算法。SHA2561HMAC_SHA256算法。SHA5122HMAC_SHA512算法。[]()[]()

#### KdfAlgo14+

数据库的PBKDF2算法枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称值说明KDF_SHA10PBKDF2_HMAC_SHA1算法。KDF_SHA2561PBKDF2_HMAC_SHA256算法。KDF_SHA5122PBKDF2_HMAC_SHA512算法。[]()[]()

#### Tokenizer17+

描述fts（全文搜索）场景下使用的分词器枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称值说明NONE_TOKENIZER0不使用分词器。ICU_TOKENIZER1表示使用icu分词器，支持中文以及多国语言。指定icu分词器时，可指定使用哪种语言，例如zh_CN表示中文，tr_TR表示土耳其语等。详细支持的语言种类，请查阅[ICU分词器](https://gitcode.com/HarmonyOS/third_party_icu/blob/master/icu4c/source/data/lang/zh.txt)。详细的语言缩写，请查阅该目录（[ICU支持的语言缩写](https://gitcode.com/HarmonyOS/third_party_icu/tree/master/icu4c/source/data/locales)）下的文件名。CUSTOM_TOKENIZER18+2表示使用自研分词器，可支持中文（简体、繁体）、英文、阿拉伯数字。CUSTOM_TOKENIZER相比ICU_TOKENIZER在分词准确率、常驻内存占用上更有优势。自研分词器支持默认分词模式和短词分词模式（short_words）两种，使用参数cut_mode可指定模式，不指定模式时使用默认模式。

在使用不同的分词器时，使用的创表语句会有所区别。

**示例：**

示例代码中this.context定义见Stage模型的应用[Context](../graphics/Context (Stage模型的上下文基类).md)。

使用ICU_TOKENIZER分词器时，创建表的示例：

```ets
import { relationalStore } from '@kit.ArkData'; // 导入模块
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

// 此处示例在Stage模式、Ability中实现，使用者也可以在其他合理场景中使用
class EntryAbility extends UIAbility {
  async onWindowStageCreate(windowStage: window.WindowStage) {
    let store: relationalStore.RdbStore | undefined = undefined;
    const STORE_CONFIG: relationalStore.StoreConfig = {
      name: "MyStore.db",
      securityLevel: relationalStore.SecurityLevel.S3,
      tokenizer: relationalStore.Tokenizer.ICU_TOKENIZER
    };
    store = await relationalStore.getRdbStore(this.context, STORE_CONFIG);

    const SQL_CREATE_TABLE = "CREATE VIRTUAL TABLE example USING fts4(name, content, tokenize=icu zh_CN)";
    if (store != undefined) {
      (store as relationalStore.RdbStore).executeSql(SQL_CREATE_TABLE, (err) => {
        if (err) {
          console.error(`ExecuteSql failed, code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('create virtual table done.');
      });
    }
  }
}
```

使用CUSTOM_TOKENIZER分词器时，创建表的示例：

```ets
import { relationalStore } from '@kit.ArkData'; // 导入模块
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

// 此处示例在Stage模式、Ability中实现，使用者也可以在其他合理场景中使用
class EntryAbility extends UIAbility {
  async onWindowStageCreate(windowStage: window.WindowStage) {
    let store: relationalStore.RdbStore | undefined = undefined;
    const STORE_CONFIG: relationalStore.StoreConfig = {
      name: "MyStore.db",
      securityLevel: relationalStore.SecurityLevel.S3,
      tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER
    };
    store = await relationalStore.getRdbStore(this.context, STORE_CONFIG);

    const SQL_CREATE_TABLE = "CREATE VIRTUAL TABLE example USING fts5(name, content, tokenize='customtokenizer')";
    if (store != undefined) {
      (store as relationalStore.RdbStore).executeSql(SQL_CREATE_TABLE, (err) => {
        if (err) {
          console.error(`ExecuteSql failed, code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('create virtual table done.');
      });
    }
  }
}
```

使用CUSTOM_TOKENIZER分词器，并指定分词模式时，创建表的示例：

```ets
import { relationalStore } from '@kit.ArkData'; // 导入模块
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  async onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('custom tokenizer example: window stage create begin.');
    let store: relationalStore.RdbStore | undefined = undefined;
    const storeConfig: relationalStore.StoreConfig = {
      name: "MyStore.db",
      securityLevel: relationalStore.SecurityLevel.S3
    };
    let customType = relationalStore.Tokenizer.CUSTOM_TOKENIZER;
    let customTypeSupported = relationalStore.isTokenizerSupported(customType);
    if (customTypeSupported) {
      storeConfig.tokenizer = customType;
    } else {
      console.info('custom tokenizer example: not support custom tokenizer.');
      return;
    }
    store = await relationalStore.getRdbStore(this.context, storeConfig);

    const sqlCreateTable =
      "CREATE VIRTUAL TABLE example USING fts5(name, content, tokenize='customtokenizer cut_mode short_words')";
    if (store != undefined) {
      (store as relationalStore.RdbStore).executeSql(sqlCreateTable, (err) => {
        if (err) {
          console.error(`custom tokenizer example: ExecuteSql failed, code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('custom tokenizer example: create virtual table done.');
      });
    }
  }
}
```

[]()[]()

#### AssetStatus10+

描述资产附件的状态枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称值说明ASSET_NORMAL1表示资产状态正常。ASSET_INSERT2表示资产需要插入到云端。ASSET_UPDATE3表示资产需要更新到云端。ASSET_DELETE4表示资产需要在云端删除。ASSET_ABNORMAL5表示资产状态异常。ASSET_DOWNLOADING6表示资产正在下载到本地设备。[]()[]()

#### SyncMode

指数据库同步模式。请使用枚举名称而非枚举值。

名称值说明SYNC_MODE_PUSH0

表示数据从本地设备推送到远程设备。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

SYNC_MODE_PULL1

表示数据从远程设备拉至本地设备。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

SYNC_MODE_TIME_FIRST10+4

表示数据从修改时间较近的一端同步到修改时间较远的一端。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

SYNC_MODE_NATIVE_FIRST10+5

表示数据从本地设备同步到云端。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

SYNC_MODE_CLOUD_FIRST10+6

表示数据从云端同步到本地设备。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

[]()[]()

#### Origin11+

表示数据来源。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

名称值说明LOCAL0表示本地数据。CLOUD1表示云端同步的数据。REMOTE2表示端端同步的数据。[]()[]()

#### Field11+

用于谓词查询条件的特殊字段。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

名称值说明CURSOR_FIELD'#_cursor'用于cursor查找的字段名。ORIGIN_FIELD'#_origin'用于cursor查找时指定数据来源的字段名。DELETED_FLAG_FIELD'#_deleted_flag'

用于cursor查找的结果集返回时填充的字段，表示云端删除的数据同步到本地后数据是否清理。

返回的结果集中，该字段对应的value为false表示数据未清理，true表示数据已清理。

DATA_STATUS_FIELD12+'#_data_status'用于cursor查找的结果集返回时填充的字段，返回的结果集中，该字段对应的0表示正常数据，1表示退出账号保留数据，2表示云侧同步删除，3表示退出账户删除数据。OWNER_FIELD'#_cloud_owner'用于共享表中查找owner时，返回的结果集中填充的字段，表示当前共享记录的共享发起者。PRIVILEGE_FIELD'#_cloud_privilege'用于共享表中查找共享数据权限时，返回的结果集中填充的字段，表示当前共享记录的允许的操作权限。SHARING_RESOURCE_FIELD'#_sharing_resource_field'用于数据共享查找共享数据的共享资源时，返回的结果集中填充的字段，表示共享数据的共享资源标识。[]()[]()

#### SubscribeType

描述订阅类型。请使用枚举名称而非枚举值。

名称值说明SUBSCRIBE_TYPE_REMOTE0

订阅远程数据更改。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

SUBSCRIBE_TYPE_CLOUD10+1

订阅云端数据更改。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

SUBSCRIBE_TYPE_CLOUD_DETAILS10+2

订阅云端数据更改详情。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

SUBSCRIBE_TYPE_LOCAL_DETAILS12+3

订阅本地数据更改详情。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

[]()[]()

#### RebuildType12+

描述数据库重建类型的枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称值说明NONE0表示数据库未进行重建。REBUILT1表示数据库进行了重建并且生成了空数据库，需要应用重新建表和恢复数据。REPAIRED2表示数据库进行了修复，恢复了未损坏的数据，当前只有[向量数据库](../../types/interfaces/Interfaces (其他) (arkts-apis-data-relationalstore-i).md#ZH-CN_TOPIC_0000002529284677__storeconfig)具备该能力。[]()[]()

#### ChangeType10+

描述数据变更类型的枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称值说明DATA_CHANGE0表示是数据发生变更。ASSET_CHANGE1表示是资产附件发生了变更。[]()[]()

#### DistributedType10+

描述表的分布式类型的枚举。请使用枚举名称而非枚举值。

名称值说明DISTRIBUTED_DEVICE0

表示在不同设备之间分布式的数据库表。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

DISTRIBUTED_CLOUD1

表示在设备和云端之间分布式的数据库表。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

[]()[]()

#### ConflictResolution10+

插入和修改接口的冲突解决模式。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称值说明ON_CONFLICT_NONE0表示当冲突发生时，不做任何处理。ON_CONFLICT_ROLLBACK1表示当冲突发生时，中止SQL语句并回滚当前事务。ON_CONFLICT_ABORT2表示当冲突发生时，中止当前SQL语句，并撤销当前 SQL 语句所做的任何更改，但是由同一事务中先前的 SQL 语句引起的更改被保留并且事务保持活动状态。ON_CONFLICT_FAIL3表示当冲突发生时，中止当前 SQL 语句。但它不会撤销失败的 SQL 语句的先前更改，也不会结束事务。ON_CONFLICT_IGNORE4表示当冲突发生时，跳过包含违反约束的行并继续处理 SQL 语句的后续行。ON_CONFLICT_REPLACE5表示当冲突发生时，在插入或更新当前行之前删除导致约束违例的预先存在的行，并且命令会继续正常执行。[]()[]()

#### Progress10+

描述端云同步过程的枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称值说明SYNC_BEGIN0表示端云同步过程开始。SYNC_IN_PROGRESS1表示正在端云同步过程中。SYNC_FINISH2表示端云同步过程已完成。[]()[]()

#### ProgressCode10+

表示端云同步过程的状态。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称值说明SUCCESS0表示端云同步过程成功。UNKNOWN_ERROR1表示端云同步过程遇到未知错误。NETWORK_ERROR2表示端云同步过程遇到网络错误。CLOUD_DISABLED3表示云端不可用。LOCKED_BY_OTHERS4

表示有其他设备正在端云同步，本设备无法进行端云同步。

请确保无其他设备占用云端资源后，再使用本设备进行端云同步任务。

RECORD_LIMIT_EXCEEDED5表示本次端云同步需要同步的条目或大小超出最大值。由云端配置最大值。NO_SPACE_FOR_ASSET6表示云空间剩余空间小于待同步的资产大小。BLOCKED_BY_NETWORK_STRATEGY12+7表示端云同步被网络策略限制。[]()[]()

#### TransactionType14+

描述创建事务对象的枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称值说明DEFERRED0表示创建一个DEFERRED类型的事务对象，该类型的事务对象在创建时只会关闭自动提交而不会真正开始事务，只有在首次读或写操作时会真正开始一个读或写事务。IMMEDIATE1表示创建一个IMMEDIATE类型的事务对象，该类型的事务对象在创建时会真正开始一个写事务；如果有别的写事务未提交，则会创建失败，返回错误码14800024。EXCLUSIVE2表示创建一个EXCLUSIVE类型的事务对象，该类型的事务在WAL模式下和IMMEDIATE相同，但在其他日志模式下能够防止事务期间有其他连接读取数据库。[]()[]()

#### ColumnType18+

描述数据库列存储类型的枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

名称值说明NULL0表示列数据类型为NULL。INTEGER1表示列数据类型为64位整数。可用于保存8位（包括布尔值）、16位、32位、64位整数。如果64位整数大于2^53或小于-2^53，需使用[getString](../../types/interfaces/Interface (ResultSet).md#ZH-CN_TOPIC_0000002497604684__getstring)将64位整数转换为字符串。REAL2表示列类型为浮点数。TEXT3表示列类型为字符串。BLOB4表示列类型为Uint8Array。ASSET5表示列类型为[Asset](../../types/interfaces/Interfaces (其他) (arkts-apis-data-relationalstore-i).md#ZH-CN_TOPIC_0000002529284677__asset10)。ASSETS6表示列类型为[Assets](Types (arkts-apis-data-relationalstore-t).md#ZH-CN_TOPIC_0000002497444708__assets10)。FLOAT_VECTOR7表示列类型为Float32Array。UNLIMITED_INT8表示列类型为bigint。