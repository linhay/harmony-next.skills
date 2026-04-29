# Drm

**概述**

提供数字版权保护能力的API。

开发者可根据实际的开发需求，参考对应的开发指南及样例：

- [数字版权保护(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/drm-c-dev-guide)

- [基于AVCodec播放DRM节目(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/drm-avcodec-integration)

起始版本： 11

**文件汇总**

| 名称 | 描述 |
| --- | --- |
| native_drm_common.h | 定义DRM数据类型。 |
| native_drm_err.h | 定义DRM错误码。 |
| native_mediakeysession.h | 定义Drm MediaKeySession API。提供以下功能： 生成媒体密钥请求、处理媒体密钥响应、事件监听、获取内容保护级别、检查媒体密钥状态、删除媒体密钥等。 |
| native_mediakeysystem.h | 定义Drm MediaKeySystem API。提供以下功能： 查询是否支持特定的drm、创建媒体密钥会话、获取和设置配置、获取统计信息、获取内容保护级别、生成提供请求、处理提供响应、事件监听、获取内容防护级别、管理离线媒体密钥等。 |