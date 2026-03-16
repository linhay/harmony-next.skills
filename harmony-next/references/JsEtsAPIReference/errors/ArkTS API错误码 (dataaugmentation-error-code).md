[]()[]()

# ArkTS API错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

[]()[]()

#### 1021000000 系统资源不足或内存访问异常

**错误信息**

Insufficient system resources or memory access exception.

**错误描述**

系统资源不足或内存访问异常。

**可能原因**

1. 系统资源不足
1. 系统错误，如空指针、数据服务异常重启、I/O错误、JS引擎异常等。

**处理步骤**

1. 尝试清理内存后重试。
1. 如果依然无法解决，可以提示用户重启应用、升级应用或升级设备版本。

[]()[]()

#### 1021000001 调用LLM超时

**错误信息**

A timeout occurred when calling the LLM.

**错误描述**

与大语言模型交互过程中出现超时错误。

**可能原因**

开发者在streamChat中请求大语言模型时出现超时错误。

**处理步骤**

1. 请开发者重新调用[streamRun](../topics/misc/rag（检索增强生成）.md#section178721756950)。
1. 多次重试均失败则需请开发者优化[streamChat](../topics/misc/rag（检索增强生成）.md#section157381918121212)中使用的大语言模型及相应实现。

[]()[]()

#### 1021000002 调用LLM加载失败

**错误信息**

A loading failure occurred when calling the LLM.

**错误描述**

与大语言模型交互过程中出现加载错误。

**可能原因**

开发者在streamChat中请求大语言模型时出现加载错误。

**处理步骤**

1. 请开发者重新调用[streamRun](../topics/misc/rag（检索增强生成）.md#section178721756950)。
1. 多次重试均失败则需请开发者优化[streamChat](../topics/misc/rag（检索增强生成）.md#section157381918121212)中使用的大语言模型及相应实现。

[]()[]()

#### 1021000003 调用LLM时发生请求失败

**错误信息**

A request failure occurred when calling the LLM.

**错误描述**

与大语言模型交互过程中发生请求失败。

**可能原因**

开发者在[streamChat](../topics/misc/rag（检索增强生成）.md#section157381918121212)中请求大语言模型时失败。

**处理步骤**

1. 请开发者重新调用[streamRun](../topics/misc/rag（检索增强生成）.md#section178721756950)。
1. 多次重试均失败则需请开发者优化[streamChat](../topics/misc/rag（检索增强生成）.md#section157381918121212)中使用的大语言模型及相应实现。

[]()[]()

#### 1021000004 LLM繁忙

**错误信息**

The LLM chat is busy.

**错误描述**

与大语言模型交互过程中大语言模型繁忙。

**可能原因**

开发者在[streamChat](../topics/misc/rag（检索增强生成）.md#section157381918121212)中请求大语言模型时大语言模型繁忙。

**处理步骤**

1. 请开发者重新调用[streamRun](../topics/misc/rag（检索增强生成）.md#section178721756950)。
1. 多次重试均失败则需请开发者优化[streamChat](../topics/misc/rag（检索增强生成）.md#section157381918121212)中使用的大语言模型及相应实现。

[]()[]()

#### 1021000005 LLM输出不符合约束

**错误信息**

The output of LLM chat does not comply with the constraints.

**错误描述**

开发者拿到大语言模型后回复的答案长度超出范围8192字节。

**可能原因**

开发者在[streamChat](../topics/misc/rag（检索增强生成）.md#section157381918121212)中请求大语言模型得到答案后返回了非法输出。

**处理步骤**

请开发者检查大语言模型给出的答案，并检查返回值拼装是否正确。

[]()[]()

#### 1021000006 RAG会话已存在

**错误信息**

The RAG session already exists.

**错误描述**

RAG会话已存在。

**可能原因**

[RagSession](../topics/misc/rag（检索增强生成）.md#section1312212528516)未关闭，重复创建[RagSession](../topics/misc/rag（检索增强生成）.md#section1312212528516)。

**处理步骤**

如果[Config](../topics/misc/rag（检索增强生成）.md#section1033315317182)没有变化，可以使用之前的[RagSession](../topics/misc/rag（检索增强生成）.md#section1312212528516)继续对话，否则，请先使用[close](../topics/misc/rag（检索增强生成）.md#section15625720155116)接口关闭旧的[RagSession](../topics/misc/rag（检索增强生成）.md#section1312212528516)，再使用新的[Config](../topics/misc/rag（检索增强生成）.md#section1033315317182)调用[createRagSession](../topics/misc/rag（检索增强生成）.md#section14201103320529)接口创建新的[RagSession](../topics/misc/rag（检索增强生成）.md#section1312212528516)进行对话。

[]()[]()

#### 1021000007 RAG会话繁忙

**错误信息**

The RAG session is busy.

**错误描述**

RAG会话繁忙。

**可能原因**

前一次[streamRun](../topics/misc/rag（检索增强生成）.md#section178721756950)回答期间重新调用了[streamRun](../topics/misc/rag（检索增强生成）.md#section178721756950)开启新一轮问答。

**处理步骤**

如果开发者希望保留前一次回答结果，请等待前一次[streamRun](../topics/misc/rag（检索增强生成）.md#section178721756950)结束，再重新调用[streamRun](../topics/misc/rag（检索增强生成）.md#section178721756950)进行新一轮问答。

[]()[]()

#### 1021000008 RAG会话已关闭

**错误信息**

The RAG session is Already closed.

**错误描述**

RAG会话已关闭。

**可能原因**

调用[RagSession](../topics/misc/rag（检索增强生成）.md#section1312212528516)的接口时，[RagSession](../topics/misc/rag（检索增强生成）.md#section1312212528516)已关闭。

**处理步骤**

调用[RagSession](../topics/misc/rag（检索增强生成）.md#section1312212528516)的接口前请确认存在打开的[RagSession](../topics/misc/rag（检索增强生成）.md#section1312212528516)。

[]()[]()

#### 1021000009 用户已取消streamRun

**错误信息**

User has canceled the stream run.

**错误描述**

用户已取消[streamRun](../topics/misc/rag（检索增强生成）.md#section178721756950)。

**可能原因**

调用[streamRun](../topics/misc/rag（检索增强生成）.md#section178721756950)接口过程中，用户主动取消了本次[streamRun](../topics/misc/rag（检索增强生成）.md#section178721756950)。

**处理步骤**

用户调用触发产生错误码，排查触发时机是否符合预期即可，无需专门处理。

[]()[]()

#### 1021000010 会话中发生超时

**错误信息**

A timeout occurred in the session.

**错误描述**

会话中发生超时。

**可能原因**

Retriever检索数据超时。

**处理步骤**

请开发者尝试重试[streamRun](../topics/misc/rag（检索增强生成）.md#section178721756950)。

[]()[]()

#### 1021000011 某些参数不满足约束条件

**错误信息**

Some parameter does not meet the constraints.

**错误描述**

某些参数不满足约束条件。

**可能原因**

开发者调用[createRagSession](../topics/misc/rag（检索增强生成）.md#section14201103320529)时传入的[Config](../topics/misc/rag（检索增强生成）.md#section1033315317182)不满足约束条件。

**处理步骤**

请开发者查阅API参考中对各类型的描述，结合实际业务需要配置正确[Config](../topics/misc/rag（检索增强生成）.md#section1033315317182)。

[]()[]()

#### 1021000012 知识库不可用

**错误信息**

The knowledge base is not available.

**错误描述**

知识库不可用。

**可能原因**

1. 未配置知识加工schema。
1. 错误配置知识加工schema。

**处理步骤**

1. 使用rag能力前请确认已配置[知识加工](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-augmentation-knowledge-processing)schema。
1. 检查schema配置文件格式及内容，确保符合相应约束。

[]()[]()

#### 1021000013 Retrieval: 检索过程中发生错误

**错误信息**

Retrieval: An error occurred during the Retrieval.

**错误描述**

检索过程中发生错误。

**可能原因**

1. 在检索模块的Recall阶段发生错误，比如服务内部状态异常，或者输入参数有问题。
1. 在检索模块的Re-ranking阶段发生错误，比如服务端状态异常或排序逻辑错误。

**处理步骤**

1. 检查输入参数是否符合要求。
1. 确保服务端状态正常并且已经完成相关初始化工作。
1. 检查服务的内部逻辑，确保排序方法符合预期。

[]()[]()

#### 1021000014 Retrieval: 存在无效的主键

**错误信息**

Retrieval: There are invalid primary keys.

**错误描述**

存在无效的主键。

**可能原因**

1. 多个召回过程配置的主键个数不一致。
1. 配置的主键为空字符串。

**处理步骤**

1. 检查输入主键是否正确一致。
1. 修正Config中配置的主键信息后重试。

[]()[]()

#### 1021000015 Retrieval: 使用了不支持复合主键的重排序算法

**错误信息**

Retrieval: A re-ranking algorithm that does not support composite primary keys was used.

**错误描述**

使用了不支持复合主键的重排序算法。

**可能原因**

重排序算法中除了rrf排序算法，其他排序算法不支持多主键。

**处理步骤**

1. 确保主键数量不超过算法允许的限制。
1. 修正[Config](../topics/misc/rag（检索增强生成）.md#section1033315317182)后重试。

[]()[]()

#### 1021000016 Retrieval: 筛选器输入无效

**错误信息**

Retrieval: The filter input is invalid.

**错误描述**

筛选器输入无效。

**可能原因**

1. 缺失必要字段。
1. 对于“between”类型，没有定义“range”字段。
1. 对于非“between”类型，没有定义“value”字段。

**处理步骤**

1. 检查filter参数。
1. 修正[Config](../topics/misc/rag（检索增强生成）.md#section1033315317182)后重试。

[]()[]()

#### 1021000017 Retrieval: RecallCondition中存在无效的召回名称

**错误信息**

Retrieval: There are invalid recall names in RecallCondition.

**错误描述**

RecallCondition中存在无效的召回名称。

**可能原因**

不同RecallCondition中的recallName字段取值相同。

**处理步骤**

1. 检查每个RecallCondition中的recallName字段的值，确保其合法性。
1. 修正[Config](../topics/misc/rag（检索增强生成）.md#section1033315317182)后重试。

[]()[]()

#### 1021000018 Retrieval: VectorQuery中的向量相似度阈值高于VectorRerankParameter中的分层阈值

**错误信息**

Retrieval: The vector similarity threshold in VectorQuery is higher than the tiered threshold in VectorRerankParameter.

**错误描述**

VectorQuery中的相似度阈值超出了VectorRerankParameter的分层阈值。

**可能原因**

VectorQuery中输入的相似度阈值大于VectorRerankParameter的最小阈值。

**处理步骤**

1. 检查VectorQuery的参数配置，确保其在合理的范围内。
1. 修正[Config](../topics/misc/rag（检索增强生成）.md#section1033315317182)后重试。

[]()[]()

#### 1021000019 Retrieval: RerankMethod参数与通道类型不匹配

**错误信息**

Retrieval: RerankMethod parameters do not match the channel type.

**错误描述**

RerankMethod参数与通道类型不匹配。

**可能原因**

输入的参数和通道类型未正确关联。

**处理步骤**

1. 检查输入的通道类型和参数是否匹配。
1. 修正[Config](../topics/misc/rag（检索增强生成）.md#section1033315317182)后重试。

[]()[]()

#### 1021200001 数据库文件损坏

**错误信息**

The database is corrupted.

**错误描述**

该错误码表示在调用数据库read、write等接口时，数据库已损坏。

**可能原因**

调用数据库read、write等接口操作数据库时，数据库文件已损坏。

**处理步骤**

目前暂不支持数据库的备份、恢复，如果可以接受数据库数据丢失，则可尝试删除数据库后重新创建。

[]()[]()

#### 1021200002 数据库或事务关闭

**错误信息**

The database is closed.

**错误描述**

数据库或事务关闭。

**可能原因**

1. 执行当前操作时，已调用过close接口关闭数据库或者开库未成功。
1. 执行当前操作时，已调用过commit接口提交事务或者调用过rollback接口回滚事务。

**处理步骤**

1. 使用getStore接口重新开库，注意入参应与前一次成功开库时的入参保持一致。
1. 使用createTransaction接口重新创建事务。

[]()[]()

#### 1021200003 数据库BUSY

**错误信息**

The database is busy.

**错误描述**

数据库BUSY。

**可能原因**

1. 同一应用多个进程同时打开了同一个数据库，进行读写操作。
1. 进程内多线程同时进行读写操作，导致某一线程读写操作超时。
1. 存在一个事务调用过write接口写入数据但未提交或回滚。

**处理步骤**

1. 避免进程并发操作数据库。
1. 等待一段时间重试。
1. 提交或回滚未关闭的事务。

[]()[]()

#### 1021200004 数据库内存不足

**错误信息**

The database is out of memory.

**错误描述**

数据库内存不足。

**可能原因**

数据库内存不足，可能是由于数据量过大或内存分配不足导致的。

**处理步骤**

减小数据量或尝试通过清理其他进程增加内存分配。

[]()[]()

#### 1021200100 SQLite 通用错误

**错误信息**

SQLite: Generic error.

**错误描述**

SQLite：通用错误。

**可能原因**

执行sql语句过程中出现错误，如：

1. 插入或更新未创建的表。
1. 插入或更新未曾有的列。
1. 查询时指定了未曾有的列，或指定了不存在的表。
1. 调用未定义的函数等，参见SQLITE_ERROR的相关错误场景。

**处理步骤**

开发者分析错误的SQL语句，找出错误点。

[]()[]()

#### 1021200101 SQLite:访问权限被拒绝

**错误信息**

SQLite: Access permission denied.

**错误描述**

SQLite访问权限被拒绝。

**可能原因**

1. 操作系统级别的权限问题，意味着SQLite试图访问或修改一个文件，但是没有足够的权限去执行这个操作。
1. 参见SQLITE_PERM的相关错误场景。

**处理步骤**

1. 确认文件没有只读属性，如果有，去掉只读属性。
1. 检查文件和文件夹的权限，确保当前用户有足够的权限来读写文件。
1. 检查文件系统是否为只读，如果是，改为可写状态。
1. 确认没有其他进程锁定数据库文件，如果有，关闭占用文件的进程。
1. 在处理权限问题时，确保有足够的权限去更改相关的文件或文件夹权限。

[]()[]()

#### 1021200102 SQLite:数据库文件已锁定

**错误信息**

SQLite: The database file is locked.

**错误描述**

SQLite数据库文件已锁定。

**可能原因**

1. 同一应用两个进程，例如UIability和datashareability同时打开了同一个数据库，进行增删改操作，或者不同应用的同一个group组内的进程通过group组打开同一个数据库，进行增删改操作。
1. 参见SQLITE_BUSY的相关错误场景。

**处理步骤**

1. 避免进程并发操作数据库。
1. 等待一段时间重试。

[]()[]()

#### 1021200103 SQLite:发生了某种磁盘I/O错误

**错误信息**

SQLite: Some kind of disk I/O error occurred.

**错误描述**

SQLite发生了某种磁盘I/O错误。

**可能原因**

可能是由于多种原因造成的，包括但不限于：

1. 文件不存在。
1. 文件是只读的。
1. 磁盘空间不足。
1. 文件损坏。
1. 参见SQLITE_IOERR的相关错误场景。

**处理步骤**

1. 检查文件路径是否正确，文件是否存在。
1. 确保文件没有设置为只读。
1. 检查磁盘空间是否足够，并清理不必要的文件释放空间。
1. 检查文件的权限，确保应用程序有足够的权限去读写文件。

[]()[]()

#### 1021200104 WAL文件大小超过默认上限

**错误信息**

SQLite: The WAL file size exceeds the default limit.

**错误描述**

WAL文件大小超过默认上限（512MB）。

**可能原因**

在开启读事务或者结果集未关闭的情况下，不断执行增删改操作，导致WAL文件大小超过默认上限。

**处理步骤**

1. 检查结果集或者事务是否未关闭。
1. 关闭所有的结果集或者事务。

[]()[]()

#### 1021200105 无法打开数据库文件

**错误信息**

SQLite: Unable to open the database file.

**错误描述**

无法打开数据库文件。

**可能原因**

1. 文件不存在，并且创建新数据库失败。
1. 文件存在，但是数据库文件损坏。
1. 文件权限问题，SQLite无法读写文件。
1. 磁盘空间不足。
1. 参见SQLITE_CANTOPEN的相关错误场景

**处理步骤**

1. 确认数据库文件路径是否正确，检查文件权限，确保应用程序有足够的权限去读写文件。
1. 确认磁盘空间足够。

[]()[]()

#### 1021201000 Retrieval: Recall error

**错误信息**

Retrieval: An error occurred during the recall phase.

**错误描述**

在检索模块的Recall阶段发生错误。

**可能原因**

服务内部状态异常，或者输入参数有问题。

**处理步骤**

1. 检查输入参数是否符合要求。
1. 确保服务端状态正常并且已经完成相关初始化工作。

[]()[]()

#### 1021201001 Retrieval: Re-ranking error

**错误信息**

Retrieval: An error occurred during the re-ranking phase.

**错误描述**

在检索模块的Re-ranking阶段发生错误。

**可能原因**

服务端状态异常或排序逻辑错误。

**处理步骤**

1. 检查输入的排序参数时候正确。
1. 检查服务的内部逻辑，确保排序方法符合预期。

[]()[]()

#### 1021201002 Retrieval: Numerical parameter out of range

**错误信息**

Retrieval: The value of the numerical parameter is outside the constrained range.

**错误描述**

某数值参数的值超出了允许的范围。

**可能原因**

提供的参数值未按文档要求设置参数。

**处理步骤**

1. 检查输入的数值参数，确保其在文档指定的范围内。
1. 修改参数值并重试。

[]()[]()

#### 1021201003 Retrieval: Invalid primary keys

**错误信息**

Retrieval: The primary key is invalid.

**错误描述**

Primary keys值未按文档要求设置参数。

**可能原因**

1. 在多个Recall过程中，recall的参数中使用的主键个数不一致。
1. recall接口的参数中，主键的个数为空。
1. recall接口的参数中，主键为空字符串。

**处理步骤**

1. 检查输入主键是否正确一致。
1. 修正Recall流程中的主键信息后重试。

[]()[]()

#### 1021201004 Retrieval: Unsupport composite primary key in re-ranking

**错误信息**

Retrieval: A re-ranking algorithm that does not support composite primary keys was used.

**错误描述**

不支持多主键的re-ranking算法中传入的主键个数大于1。

**可能原因**

Re-ranking算法中除了rrf排序算法，其他排序算法不支持多主键。

**处理步骤**

1. 确保主键数量不超过算法允许的限制。
1. 修正输入数据后重试。

[]()[]()

#### 1021201005 Retrieval: Empty string field

**错误信息**

Retrieval: There is a field with an empty string.

**错误描述**

输入参数中存在空字符串字段。

**可能原因**

输入参数包含不合法的空字符串值。

**处理步骤**

1. 检查输入字符串字段，确保所有值为非空。
1. 修正输入数据后重试。

[]()[]()

#### 1021201006 Retrieval: Illegal filter input

**错误信息**

Retrieval: The filter input is invalid.

**错误描述**

提供的filters是无效参数。

**可能原因**

1. FilterInfo缺失必要字段（columns字段为空；filterValue字段和filterRange字段的值都未赋值；operator字段未赋值）。
1. 对于between类型过滤，没有定义filterRange。
1. 对于非between类型过滤，没有定义filterValue。

**处理步骤**

1. 检查filters参数。
1. 修正输入数据后重试。

[]()[]()

#### 1021201007 Retrieval: Invalid recall field name

**错误信息**

Retrieval: There is invalid recall name in RecallCondition.

**错误描述**

RecallCondition中的recallName字段取值相同。

**可能原因**

不同RecallCondition中的recallName字段取值相同。

**处理步骤**

1. 检查每个RecallCondition中的recallName字段的值，确保其合法性。
1. 根据文档修改字段的值并重试。

[]()[]()

#### 1021201008 Retrieval: Vector similarity threshold too high

**错误信息**

Retrieval: The vector similarity threshold in VectorQuery is higher than the tiered threshold in VectorRerankParameter.

**错误描述**

VectorQuery中的相似度阈值超出了VectorRerankParameter的分层阈值。

**可能原因**

VectorQuery中输入的相似度阈值大于VectorRerankParameter的最小阈值。

**处理步骤**

1. 检查VectorQuery的参数配置，确保其在合理的范围内。
1. 修改相似度阈值后重试。

[]()[]()

#### 1021201009 Retrieval: RerankMethod parameters do not match the channel type

**错误信息**

Retrieval: RerankMethod parameters do not match the channel type.

**错误描述**

RerankMethod参数与通道类型不匹配。

**可能原因**

输入的参数和通道类型未正确关联。

**处理步骤**

1. 检查输入的通道类型和参数是否匹配。
1. 修改参数配置后重试。

[]()[]()

#### 1021201010 Retrieval: Empty parameter value

**错误信息**

Retrieval: There exists a parameter value that should not be empty but is actually not defined.

**错误描述**

输入的参数为空。

**可能原因**

调用时未提供合法的参数。

**处理步骤**

1. 检查输入的参数是否合法。
1. 修改参数配置后重试。

[]()[]()

#### 1021200012 Unable to generate embeddings

**错误信息**

Unable to generate embeddings

**错误描述**

加载模型失败。

**可能原因**

1. 当前版本不支持自动生成query的向量，需要直接导入向量数组。

2. 可能因资源不足导致模型加载异常。

**处理步骤**

修改参数配置后重试。

[]()[]()

#### 1021400000 内部错误

**错误信息**

Internal error.

**错误描述**

内部错误。

**可能原因**

1. 优先查看错误日志，通过日志可以详细了解错误原因，主要有以下几种：
1. 接口执行异常。
1. 内部状态异常。
1. 错误地使用接口。
1. 系统错误，如空指针、数据服务异常重启、I/O错误、JS引擎异常等。
1. 数据库异常。

**处理步骤**

1. 开发者排查是否按接口文档正确使用接口。
1. 尝试重试，如果依然无法解决，可以提示用户重启应用、升级应用或升级设备版本。

[]()[]()

#### 1021400001 知识源未配置

**错误信息**

The knowledge source is not configured.

**错误描述**

知识源配置中的rdbSource未配置。

**可能原因**

1. 知识源配置中的rdbSource未配置。

**处理步骤**

1. 参照[知识源配置](../topics/system-services/knowledgeProcessor（知识加工）.md#section5324144573013)类型，正确配置rdbSource字段。

[]()[]()

#### 1021400002 知识schema文件不存在

**错误信息**

The knowledge schema file is not found.

**错误描述**

知识schema文件不存在。

**可能原因**

1. 知识schema文件未放到指定目录下。

**处理步骤**

1. 参考开发步骤中的[知识schema配置示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-augmentation-knowledge-processing#section912287171317)，将knowledge_schema.json放到指定的entry/src/main/resources/rawfile/arkdata/knowledge目录下。

[]()[]()

#### 1021400003 知识schema内容不合法

**错误信息**

The knowledge schema content is invalid.

**错误描述**

知识schema内容不合法。

**可能原因**

1. 知识schema中的内容不符合当前的规格及约束限制。

**处理步骤**

1. 参照[知识schema规格及约束限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-augmentation-knowledge-processing#section13189205451011)修改其中内容。

[]()[]()

#### 1021400004 操作RDB数据源时发生错误

**错误信息**

An error occurred during operations on the RDB source.

**错误描述**

操作RDB数据源时发生错误。

**可能原因**

1. RDB数据源异常导致操作RDB数据源时发生了错误。

**处理步骤**

1. 尝试重试，如果依然无法解决，可以提示用户重启应用、升级应用或升级设备版本。

[]()[]()

#### 1021900001 调用端侧问答模型超时

**错误信息**

A timeout occurs when the local chat model is called.

**错误描述**

调用端侧大模型超时。

**可能原因**

1. 输入的问题内容过长导致端侧问答模型处理过久。
1. 系统繁忙，硬件资源紧张，端侧问答模型处理过慢。

**处理步骤**

1. 尝试缩短输入问题的长度。
1. 关闭后台优先级低的进程，并稍后重试。

[]()[]()

#### 1021900002 端侧问答模型加载失败

**错误信息**

A loading failure occurs when the local chat model is called.

**错误描述**

调用端侧大模型时端侧问答模型加载失败。

**可能原因**

1. 没有在PC模型管家下载模型文件。
1. PC模型管家服务拉起失败。

**处理步骤**

1. 在PC模型管家下载页面下载模型。
1. 重启应用后重试。

[]()[]()

#### 1021900003 端侧问答模型请求失败

**错误信息**

A request failure occurs when the local chat model is called.

**错误描述**

调用端侧问答模型时端侧问答模型请求失败。

**可能原因**

1. 内部处理流程异常。

**处理步骤**

1. 稍后重试。

[]()[]()

#### 1021900004 端侧问答模型繁忙

**错误信息**

The local chat model is busy.

**错误描述**

调用端侧问答模型时端侧问答模型繁忙。

**可能原因**

1. 模型正在处理其他任务。

**处理步骤**

1. 关闭其他优先级低的问答请求，并稍后重试。

[]()[]()

#### 1021900005 某些参数不满足指定的约束条件

**错误信息**

Some parameters do not meet the specified constraints.

**错误描述**

某些参数不满足指定的约束条件。

**可能原因**

1. 接口的入参不符合约束条件。

**处理步骤**

1. 按照约束条件修改入参后重试。