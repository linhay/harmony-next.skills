# Hid_EmitItem

```ets
typedef struct Hid_EmitItem {...} Hid_EmitItem
```

**概述**

事件信息。

起始版本： 11

相关模块： [HidDdk](HidDdk.md)

所在头文件： [hid_ddk_types.h](hid_ddk_types.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| uint16_t type | 事件类型 |
| uint16_t code | 事件编码 |
| uint32_t value | 事件值 |