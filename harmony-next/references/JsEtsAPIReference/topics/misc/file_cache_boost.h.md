# file_cache_boost.h

**概述**

声明通用文件缓存加速的API集合。

引用文件： <PreviewKit/file_cache_boost.h>

库： libfile_cache_boost.so

系统能力： SystemCapability.PCService.OpenFileBoost

起始版本： 6.1.0(23)

相关模块： [Preview](Preview.md)

**汇总**

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef struct CacheKey CacheKey | 开发者传入的key相关数据结构的对外声明，开发者只需在序列化函数SerializeFunc和反序列化函数DeserializeFunc调用WriteFunc和ReadFunc时传入即可。 |
| typedef FileCacheBoost_ErrCode(* ReadFunc) (void *buffer, size_t *bufferLen, struct CacheKey *key) | DeserializeFunc进行反序列化的过程中调用此函数，可从缓存读取数据到缓冲区。 |
| typedef FileCacheBoost_ErrCode(* WriteFunc) (const void *buffer, size_t bufferLen, struct CacheKey *key) | SerializeFunc进行序列化的过程中调用此函数，将数据写入缓存。 |
| typedef FileCacheBoost_CbErrCode(* DeserializeFunc) (void **object, ReadFunc readFunc, struct CacheKey *key) | 系统执行反序列化操作的回调函数定义。由开发者实现，用于将已序列化的数据恢复为原始数据。 |
| typedef FileCacheBoost_CbErrCode(* SerializeFunc) (const void *object, WriteFunc writeFunc, struct CacheKey *key) | 系统执行序列化操作的回调函数定义。由开发者实现，用于将复杂类型数据进行序列化操作。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| FileCacheBoost_ErrCode { FILE_CACHE_BOOST_SUCCESS = 0,  FILE_CACHE_BOOST_ERROR_INVALID_PARAM = 401,  FILE_CACHE_BOOST_ERROR_NOT_SUPPORTED = 801, FILE_CACHE_BOOST_ERROR_NOMEM = 1017220001, FILE_CACHE_BOOST_ERROR_INTERNAL_ERROR = 1017220002, FILE_CACHE_BOOST_ERROR_KEY_NOT_FOUND = 1017220003, FILE_CACHE_BOOST_ERROR_KEY_EXIST = 1017220004, FILE_CACHE_BOOST_ERROR_NOT_DIR = 1017220005, FILE_CACHE_BOOST_ERROR_IO = 1017220006, FILE_CACHE_BOOST_ERROR_IO_CANCELED = 1017220007, FILE_CACHE_BOOST_ERROR_NOT_INITIALIZED = 1017220008, FILE_CACHE_BOOST_ERROR_EXCEED_LIMIT = 1017220009， FILE_CACHE_BOOST_ERROR_IO_CANCEL_FAILED = 1017220010 } | 文件缓存加速相关的错误码定义。 |
| FileCacheBoost_CbErrCode {  FILE_CACHE_BOOST_CALLBACK_SUCCESS = 0, FILE_CACHE_BOOST_CALLBACK_FAILURE = 1017221001， FILE_CACHE_BOOST_CALLBACK_IO_CANCELED = 1017221002 } | 回调函数DeserializeFunc和SerializeFunc的错误码定义，用于应用程序将回调函数的执行结果返回给系统。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| FileCacheBoost_ErrCode HMS_FileCacheBoost_Init (const char *path, size_t pathLen, uint32_t cacheUpperLimitMb, const char *dbName, size_t dbNameLen) | 初始化缓存路径、缓存容量上限、数据库名称。系统保证了线程并发安全控制，如需支持多进程并发场景，建议各进程使用不同的数据库文件名以保证访问安全性。 |
| FileCacheBoost_ErrCode HMS_FileCacheBoost_AddObjectByKey (const uint8_t *key, size_t keyLen, const uint8_t *data, size_t dataLen, uint32_t weight) | 创建并添加一个缓存对象至文件缓存。  系统通过key管理缓存，建议开发者合理设计和管理key值，确保其在不同上下文中的唯一性和准确性。 当不再需要缓存时，推荐开发者主动调用HMS_FileCacheBoost_RemoveObjectByKey删除对应的缓存项，以避免资源浪费。 若不主动删除，系统将在缓存容量不足时，依据系统策略进行清除。 开发者若想要对key对应的缓存内容做修改，需要先调用HMS_FileCacheBoost_RemoveObjectByKey删除之前的key，再重新创建和添加。 |
| FileCacheBoost_ErrCode HMS_FileCacheBoost_GetObjectByKey (const uint8_t *key, size_t keyLen, uint8_t **data, size_t *dataLen) | 根据指定的key查询缓存对象。若缓存对象存在，则从磁盘中加载缓存对象的内容。调用该函数，系统会分配一段内存用于存储缓存数据，作为出参返回给开发者。开发者需在使用完毕后调用HMS_FileCacheBoost_FreeObject显式释放该内存。 |
| void HMS_FileCacheBoost_FreeObject (uint8_t *data) | 释放调用HMS_FileCacheBoost_GetObjectByKey或HMS_FileCacheBoost_GetSerialObjectByKey分配的内存，建议开发者不再使用该内存时，及时调用此函数进行释放，避免造成内存泄漏。 |
| FileCacheBoost_ErrCode HMS_FileCacheBoost_AddSerialObjectByKey (const uint8_t *key, size_t keyLen, SerializeFunc func, const void *object, uint32_t weight) | 创建一个复杂类型对象的缓存项，通过传入自定义的序列化函数SerializeFunc对该象进行序列化处理，以便将其存储至磁盘并支持后续恢复。 例如图像数据需要同时保存其元数据和像素数据，才能实现完整的缓存与读取过程。序列化和反序列化会占用内存，请开发者控制object大小，降低内存压力。 |
| FileCacheBoost_ErrCode HMS_FileCacheBoost_GetSerialObjectByKey (const uint8_t *key, size_t keyLen, DeserializeFunc func, void **object) | 根据指定的key值获取复杂类型缓存对象，并通过传入的反序列化函数DeserializeFunc将其还原为原始数据，从而获得完整的对象内容。 调用该函数系统会分配一段内存用于存储缓存数据，作为出参返回给开发者，开发者需在使用完毕后调用HMS_FileCacheBoost_FreeObject显式释放该内存。 |
| FileCacheBoost_ErrCode HMS_FileCacheBoost_RemoveObjectByKey (const uint8_t *key, size_t keyLen) | 根据指定的key删除对应的缓存对象。 |
| FileCacheBoost_ErrCode HMS_FileCacheBoost_CancelOngoingIOByKey (const uint8_t *key, size_t keyLen) | 取消key对应的缓存对象当前正在进行的I/O操作。 当开发者需要释放数据对象时，应调用本函数，防止有其他线程对该数据对象进行添加缓存对象或者获取缓存对象的操作。 若该对象正处于缓存过程中，则操作将被中止；若已缓存完成，则此函数不做任何处理。 例如当一个线程尝试删除数据对象的同时，有其他线程对其进行HMS_FileCacheBoost_AddObjectByKey操作，调用本函数可确保缓存对象的安全性，避免引发数据竞争问题。 |
| FileCacheBoost_ErrCode HMS_FileCacheBoost_ClearAllCache (void) | 清理所有的缓存对象。 该函数会释放通过HMS_FileCacheBoost_AddObjectByKey和HMS_FileCacheBoost_AddSerialObjectByKey创建的所有缓存对象。 |