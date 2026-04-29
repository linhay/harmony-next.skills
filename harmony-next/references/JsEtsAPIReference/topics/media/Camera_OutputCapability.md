# Camera_OutputCapability

```ets
typedef struct Camera_OutputCapability {...} Camera_OutputCapability
```

**概述**

相机输出能力。

起始版本： 11

相关模块： [OH_Camera](OH_Camera.md)

所在头文件： [camera.h](camera.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| Camera_Profile** previewProfiles | 预览配置文件列表。 |
| uint32_t previewProfilesSize | 预览配置文件列表的大小。 |
| Camera_Profile** photoProfiles | 拍照配置文件列表。  配置文件中的size设置的是相机分辨率宽高，非实际出图宽高。 |
| uint32_t photoProfilesSize | 拍照配置文件列表的大小。 |
| Camera_VideoProfile** videoProfiles | 录像配置文件列表。 |
| uint32_t videoProfilesSize | 录像配置文件列表的大小。 |
| Camera_MetadataObjectType** supportedMetadataObjectTypes | 元数据对象类型列表。 |
| uint32_t metadataProfilesSize | 元数据对象类型列表的大小。 |