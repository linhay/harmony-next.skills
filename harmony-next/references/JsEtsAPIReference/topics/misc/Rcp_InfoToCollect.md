# Rcp_InfoToCollect

#### 概述

指定要收集的请求处理事件。可以通过响应对象检查收集的事件。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

bool [textual](Rcp_InfoToCollect.md#ZH-CN_TOPIC_0000002317039133__aff60c2d577af35be42684cddc8287b23)

是否收集未分类的文本事件。默认值为false。

bool [incomingHeader](Rcp_InfoToCollect.md#ZH-CN_TOPIC_0000002317039133__a540ee4c661375b5d261c399c2a95da03)

是否收集传入HTTP标头事件。默认值为false。

bool [outgoingHeader](Rcp_InfoToCollect.md#ZH-CN_TOPIC_0000002317039133__a3b8cc7c5c55ca74be187ea24f8788f69)

是否收集传出HTTP标头事件。默认值为false。

bool [incomingData](Rcp_InfoToCollect.md#ZH-CN_TOPIC_0000002317039133__ae80433cb5192667786963b6a8a189155)

是否收集有关传入HTTP数据的事件。默认值为false。

bool [outgoingData](Rcp_InfoToCollect.md#ZH-CN_TOPIC_0000002317039133__a7324cc52ff8e8d7c3c0c6ec94631c986)

是否收集有关传出HTTP数据的事件。默认值为false。

bool [incomingSslData](Rcp_InfoToCollect.md#ZH-CN_TOPIC_0000002317039133__a55f47927846a107a20ea48c32f5b1ce5)

是否收集传入的SSL/TLS事件。默认值为false。

bool [outgoingSslData](Rcp_InfoToCollect.md#ZH-CN_TOPIC_0000002317039133__a1c467842caa404c49e282ec6b76a45f1)

是否收集传出的SSL/TLS事件。默认值为false。

#### 结构体成员变量说明

#### incomingData

```ets
bool Rcp_InfoToCollect::incomingData
```

**描述**

是否收集有关传入HTTP数据的事件。默认值为false。

#### incomingHeader

```ets
bool Rcp_InfoToCollect::incomingHeader
```

**描述**

是否收集传入HTTP标头事件。默认值为false。

#### incomingSslData

```ets
bool Rcp_InfoToCollect::incomingSslData
```

**描述**

是否收集传入的SSL/TLS事件。默认值为false。

#### outgoingData

```ets
bool Rcp_InfoToCollect::outgoingData
```

**描述**

是否收集有关传出HTTP数据的事件。默认值为false。

#### outgoingHeader

```ets
bool Rcp_InfoToCollect::outgoingHeader
```

**描述**

是否收集传出HTTP标头事件。默认值为false。

#### outgoingSslData

```ets
bool Rcp_InfoToCollect::outgoingSslData
```

**描述**

是否收集传出的SSL/TLS事件。默认值为false。

#### textual

```ets
bool Rcp_InfoToCollect::textual
```

**描述**

是否收集未分类的文本事件。默认值为false。