# relational_store_error_code.h

#### 概述

声明关系型数据库（RDB）的错误码信息。

**引用文件：** <database/rdb/relational_store_error_code.h>

**库：** libnative_rdb_ndk.z.so

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 10

**相关模块：**[RDB](../../topics/misc/RDB.md)

#### 汇总

#### 枚举

名称typedef关键字描述[OH_Rdb_ErrCode](#ZH-CN_TOPIC_0000002497604706__oh_rdb_errcode)OH_Rdb_ErrCode表示错误码信息。

#### 枚举类型说明

#### OH_Rdb_ErrCode

```ets
enum OH_Rdb_ErrCode
```

**描述**

表示错误码信息。

**起始版本：** 10

枚举项描述RDB_ERR = -1执行出错。RDB_OK = 0执行成功。E_BASE = 14800000异常错误代码的基础。RDB_E_NOT_SUPPORTED = 801RDB不具备该能力。RDB_E_ERROR = E_BASE常见异常的错误代码。RDB_E_INVALID_ARGS = (E_BASE + 1)参数非法。RDB_E_CANNOT_UPDATE_READONLY = (E_BASE + 2)更新只读数据库。RDB_E_REMOVE_FILE = (E_BASE + 3)删除文件失败。RDB_E_EMPTY_TABLE_NAME = (E_BASE + 5)表名为空。RDB_E_EMPTY_VALUES_BUCKET = (E_BASE + 6)键值对内容为空。RDB_E_EXECUTE_IN_STEP_QUERY = (E_BASE + 7)查询时执行的SQL语句错误。RDB_E_INVALID_COLUMN_INDEX = (E_BASE + 8)列索引非法。RDB_E_INVALID_COLUMN_TYPE = (E_BASE + 9)列类型非法。RDB_E_EMPTY_FILE_NAME = (E_BASE + 10)文件名称为空。RDB_E_INVALID_FILE_PATH = (E_BASE + 11)文件路径非法。RDB_E_TRANSACTION_IN_EXECUTE = (E_BASE + 12)开启事务执行出错。RDB_E_INVALID_STATEMENT = (E_BASE + 13)SQL语句预编译出错。RDB_E_EXECUTE_WRITE_IN_READ_CONNECTION = (E_BASE + 14)在读连接中执行写操作。RDB_E_BEGIN_TRANSACTION_IN_READ_CONNECTION = (E_BASE + 15)在读连接中开启事务。RDB_E_NO_TRANSACTION_IN_SESSION = (E_BASE + 16)在数据库会话中不存在开启的事务。RDB_E_MORE_STEP_QUERY_IN_ONE_SESSION = (E_BASE + 17)在一个数据库会话中执行多次查询。RDB_E_NO_ROW_IN_QUERY = (E_BASE + 18)查询得到的结果集不存在任何记录。RDB_E_INVALID_BIND_ARGS_COUNT = (E_BASE + 19)SQL语句中绑定的参数个数非法。RDB_E_INVALID_OBJECT_TYPE = (E_BASE + 20)对象类型非法。RDB_E_INVALID_CONFLICT_FLAG = (E_BASE + 21)冲突解决类型非法。RDB_E_HAVING_CLAUSE_NOT_IN_GROUP_BY = (E_BASE + 22)HAVING关键字只能用于GROUP BY之后。RDB_E_NOT_SUPPORTED_BY_STEP_RESULT_SET = (E_BASE + 23)不支持step形式数据库结果集。RDB_E_STEP_RESULT_SET_CROSS_THREADS = (E_BASE + 24)结果集查询出错。RDB_E_STEP_RESULT_QUERY_NOT_EXECUTED = (E_BASE + 25)结果集查询语句未被执行。RDB_E_STEP_RESULT_IS_AFTER_LAST = (E_BASE + 26)结果集的游标已经处于最后一行。RDB_E_STEP_RESULT_QUERY_EXCEEDED = (E_BASE + 27)结果集查询次数已经超过上限。RDB_E_STATEMENT_NOT_PREPARED = (E_BASE + 28)SQL语句未被预编译。RDB_E_EXECUTE_RESULT_INCORRECT = (E_BASE + 29)数据库执行结果异常。RDB_E_STEP_RESULT_CLOSED = (E_BASE + 30)结果集已经关闭。RDB_E_RELATIVE_PATH = (E_BASE + 31)相对路径。RDB_E_EMPTY_NEW_ENCRYPT_KEY = (E_BASE + 32)新的密钥文件为空。RDB_E_CHANGE_UNENCRYPTED_TO_ENCRYPTED = (E_BASE + 33)将非加密的数据库更改为加密数据库。RDB_E_CHANGE_ENCRYPT_KEY_IN_BUSY = (E_BASE + 34)在数据库繁忙时更新数据库密钥。RDB_E_STEP_STATEMENT_NOT_INIT = (E_BASE + 35)预编译的SQL语句未被初始化。RDB_E_NOT_SUPPORTED_ATTACH_IN_WAL_MODE = (E_BASE + 36)在WAL日志模式下不支持ATTACH操作。RDB_E_CREATE_FOLDER_FAIL = (E_BASE + 37)创建文件夹失败。RDB_E_SQLITE_SQL_BUILDER_NORMALIZE_FAIL = (E_BASE + 38)SQL语句构建失败。RDB_E_STORE_SESSION_NOT_GIVE_CONNECTION_TEMPORARILY = (E_BASE + 39)数据库会话暂未提供连接。RDB_E_STORE_SESSION_NO_CURRENT_TRANSACTION = (E_BASE + 40)数据库会话不具有当前的事务。RDB_E_NOT_SUPPORT = (E_BASE + 41)不支持当前操作。RDB_E_INVALID_PARCEL = (E_BASE + 42)当前PARCEL非法。RDB_E_QUERY_IN_EXECUTE = (E_BASE + 43)执行query查询出错。RDB_E_SET_PERSIST_WAL = (E_BASE + 44)设置WAL模式下数据库文件的持久化时出错。RDB_E_DB_NOT_EXIST = (E_BASE + 45)数据库不存在。RDB_E_ARGS_READ_CON_OVERLOAD = (E_BASE + 46)设置的读连接数大于上限。RDB_E_WAL_SIZE_OVER_LIMIT = (E_BASE + 47)WAL日志文件大小超过默认值。RDB_E_CON_OVER_LIMIT = (E_BASE + 48)数据库连接数已用完。RDB_E_ALREADY_CLOSED = (E_BASE + 50)

数据库已关闭。

**起始版本：** 18

RDB_E_DATABASE_BUSY = (E_BASE + 51)

数据库无响应。

**起始版本：** 18

RDB_E_SQLITE_CORRUPT = (E_BASE + 52)

数据库损坏。

**起始版本：** 18

RDB_E_SQLITE_PERM = (E_BASE + 53)

SQLite错误码：访问权限被拒绝。

**起始版本：** 18

RDB_E_SQLITE_BUSY = (E_BASE + 54)

SQLite错误码：数据库文件被锁定。

**起始版本：** 18

RDB_E_SQLITE_LOCKED = (E_BASE + 55)

SQLite错误码：数据库中的表被锁定。

**起始版本：** 18

RDB_E_SQLITE_NOMEM = (E_BASE + 56)

SQLite错误码：数据库内存不足。

**起始版本：** 18

RDB_E_SQLITE_READONLY = (E_BASE + 57)

SQLite错误码：尝试写入只读数据库。

**起始版本：** 18

RDB_E_SQLITE_IOERR = (E_BASE + 58)

SQLite错误码：磁盘I/O错误。

**起始版本：** 18

RDB_E_SQLITE_FULL = (E_BASE + 59)

SQLite错误码：数据库已满。

**起始版本：** 18

RDB_E_SQLITE_CANT_OPEN = (E_BASE + 60)

SQLite错误码：无法打开数据库文件。

**起始版本：** 18

RDB_E_SQLITE_TOO_BIG = (E_BASE + 61)

SQLite错误码：TEXT或BLOB超出大小限制。

**起始版本：** 18

RDB_E_SQLITE_MISMATCH = (E_BASE + 62)

SQLite错误码：数据类型不匹配。

**起始版本：** 18

RDB_E_DATA_TYPE_NULL = (E_BASE + 63)

表示存储数据为空。

**起始版本：** 18

RDB_E_TYPE_MISMATCH = (E_BASE + 64)

表示数据类型不匹配。

**起始版本：** 18

RDB_E_SQLITE_CONSTRAINT = (E_BASE + 65)

表示SQLite错误码：SQLite约束。

**起始版本：** 18

RDB_E_SUB_LIMIT_REACHED = (E_BASE + 66)

表示订阅数量超过限制。

**起始版本：** 22