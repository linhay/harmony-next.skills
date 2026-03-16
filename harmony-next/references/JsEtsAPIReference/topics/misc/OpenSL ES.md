# OpenSL ES

HarmonyOS上的OpenSL ES接口，是早期SDK8版本开始提供，用于支持应用Native层音频开发的接口。但随着版本演进，接口定义的可扩展性不足，不再能满足音频系统的能力拓展，因此当前已不再推荐应用开发者继续使用此接口进行音频功能开发，

请开发者[从OpenSL ES切换到OHAudio](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/replace-opensles-by-ohaudio)。

#### 简介

OpenSL ES（Open Sound Library for Embedded System）即嵌入式音频加速标准。为开发者提供了标准化、高性能以及低响应时间的音频功能开发的对象和接口。相对于开源免费的OpenSL ES，HarmonyOS基于[OpenSL ES](https://www.khronos.org/opensles/) 1.0.1 API规范实现了部分Native API，相关接口开放情况如表[支持的API](#ZH-CN_TOPIC_0000002497446202__支持的api)所示。

#### 引入OpenSL ES能力

如果开发者需要使用OpenSL ES相关功能，首先请添加头文件：

```ets
#include <SLES/OpenSLES.h>
#include <SLES/OpenSLES_OpenHarmony.h>
#include <SLES/OpenSLES_Platform.h>
```

其次在CMakeLists.txt中添加以下链接动态库：

```ets
libOpenSLES.so
```

#### 支持的API

对象对外接口接口调用详情是否支持说明SLEngineItfCreateAudioPlayerCreateAudioPlayer(SLEngineItf self, SLObjectItf *pPlayer, SLDataSource *pAudioSrc, SLDataSink *pAudioSnk, SLuint32 numInterfaces, const SLInterfaceID *pInterfaceIds, const SLboolean *pInterfaceRequired)是创建音频播放机。SLEngineItfCreateAudioRecorderCreateAudioRecorder(SLEngineItf self, SLObjectItf *pRecorder, SLDataSource *pAudioSrc, SLDataSink *pAudioSnk, SLuint32 numInterfaces, const SLInterfaceID *pInterfaceIds, const SLboolean *pInterfaceRequired)是创建音频录制器。SLEngineItfCreateAudioOutputMixCreateOutputMix(SLEngineItf self, SLObjectItf *pMix, SLuint32 numInterfaces, const SLInterfaceID *pInterfaceIds, const SLboolean *pInterfaceRequired)是创建混音器。SLObjectItfRealizeRealize(SLObjectItf self, SLboolean async)是创建音频播放机。SLObjectItfgetStateGetState(SLObjectItf self, SLuint32 *pState)是获取状态。SLObjectItfgetInterfaceGetInterface(SLObjectItf self, const SLInterfaceID iid, void *pInterface)是获取接口。SLObjectItfDestroyDestroy(SLObjectItf self)是销毁对象。SLOHBufferQueueItfEnqueueEnqueue(SLOHBufferQueueItf self, const void *pBuffer, SLuint32 size)是将buffer加入实际队列中。SLOHBufferQueueItfclearClear(SLOHBufferQueueItf self)是释放buffer队列SLOHBufferQueueItfgetStateGetState(SLOHBufferQueueItf self, SLOHBufferQueueState *pState)是获取BufferQueue状态。SLOHBufferQueueItfgetBufferGetBuffer(SLOHBufferQueueItf self, SLuint8 **buffer, SLuint32 *size)是获取buffer。SLOHBufferQueueItfRegisterCallbackRegisterCallback(SLOHBufferQueueItf self, SlOHBufferQueueCallback callback, void *pContext)是注册回调函数。SLPlayItfSetPlayStateSetPlayState(SLPlayItf self, SLuint32 state)是设置播放状态。SLPlayItfGetPlayStateGetPlayState(SLPlayItf self, SLuint32 *pState)是获取播放状态。SLRecordItfSetRecordStateSetRecordState(SLRecordItf self, SLuint32 state)是设置录制状态。SLRecordItfGetRecordStateGetRecordState(SLRecordItf self, SLuint32 *pState)是获取录制状态。SLVolumeItfSetVolumeLevelSetVolumeLevel(SLVolumeItf self, SLmillibel level)是设置音量。SLVolumeItfGetVolumeLevelGetVolumeLevel(SLVolumeItf self, SLmillibel *pLevel)是获取音量。SLVolumeItfGetMaxVolumeLevelGetMaxVolumeLevel(SLVolumeItf self, SLmillibel *pMaxLevel)是获取最大音量。