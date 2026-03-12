# capture_session.h

#### 概述

声明捕获会话概念。

**引用文件：** <ohcamera/capture_session.h>

**库：** libohcamera.so

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 11

**相关模块：**[OH_Camera](OH_Camera.md)

#### 汇总

#### 结构体

名称typedef关键字描述[CaptureSession_Callbacks](CaptureSession_Callbacks.md)CaptureSession_Callbacks捕获会话的回调。[Camera_CaptureSession](Camera_CaptureSession.md)Camera_CaptureSession

捕获会话对象。

 可以使用[OH_CameraManager_CreateCaptureSession](camera_manager.h.md#ZH-CN_TOPIC_0000002529445763__oh_cameramanager_createcapturesession)方法创建指针。

#### 函数

名称typedef关键字描述[typedef void (*OH_CaptureSession_OnFocusStateChange)(Camera_CaptureSession* session, Camera_FocusState focusState)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_onfocusstatechange)OH_CaptureSession_OnFocusStateChange在[CaptureSession_Callbacks](zh-cn_topic_0000002497445836.html)中被调用的捕获会话焦点状态回调。[typedef void (*OH_CaptureSession_OnError)(Camera_CaptureSession* session, Camera_ErrorCode errorCode)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_onerror)OH_CaptureSession_OnError在[CaptureSession_Callbacks](zh-cn_topic_0000002497445836.html)中被调用的捕获会话错误回调。[typedef void (*OH_CaptureSession_OnSmoothZoomInfo)(Camera_CaptureSession* session, Camera_SmoothZoomInfo* smoothZoomInfo)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_onsmoothzoominfo)OH_CaptureSession_OnSmoothZoomInfo拍照会话平滑变焦信息回调，触发平滑变焦后该回调会返回。[typedef void (*OH_CaptureSession_OnAutoDeviceSwitchStatusChange)(Camera_CaptureSession* session, Camera_AutoDeviceSwitchStatusInfo* autoDeviceSwitchStatusInfo)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_onautodeviceswitchstatuschange)OH_CaptureSession_OnAutoDeviceSwitchStatusChange捕获会话设备切换状态回调。[typedef void (*OH_CaptureSession_OnSystemPressureLevelChange)(Camera_CaptureSession* session, Camera_SystemPressureLevel systemPressureLevel)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_onsystempressurelevelchange)OH_CaptureSession_OnSystemPressureLevelChange捕获系统压力状态变化回调。[typedef void (*OH_CaptureSession_OnControlCenterEffectStatusChange)(Camera_CaptureSession* session, Camera_ControlCenterStatusInfo* controlCenterStatusInfo)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_oncontrolcentereffectstatuschange)OH_CaptureSession_OnControlCenterEffectStatusChange相机控制器效果激活状态变化回调。[Camera_ErrorCode OH_CaptureSession_RegisterCallback(Camera_CaptureSession* session, CaptureSession_Callbacks* callback)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_registercallback)-注册捕获会话事件回调。[Camera_ErrorCode OH_CaptureSession_UnregisterCallback(Camera_CaptureSession* session, CaptureSession_Callbacks* callback)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_unregistercallback)-注销捕获会话事件回调。[Camera_ErrorCode OH_CaptureSession_RegisterSmoothZoomInfoCallback(Camera_CaptureSession* session, OH_CaptureSession_OnSmoothZoomInfo smoothZoomInfoCallback)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_registersmoothzoominfocallback)-注册平滑变焦信息事件回调。[Camera_ErrorCode OH_CaptureSession_UnregisterSmoothZoomInfoCallback(Camera_CaptureSession* session, OH_CaptureSession_OnSmoothZoomInfo smoothZoomInfoCallback)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_unregistersmoothzoominfocallback)-注销平滑变焦信息事件回调。[Camera_ErrorCode OH_CaptureSession_SetSessionMode(Camera_CaptureSession* session, Camera_SceneMode sceneMode)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_setsessionmode)-

设置会话模式。

 此接口不能在[OH_CaptureSession_BeginConfig](capture_session.h.md#ZH-CN_TOPIC_0000002497605800__oh_capturesession_beginconfig)之后使用。

 建议在使用[OH_CameraManager_CreateCaptureSession](camera_manager.h.md#ZH-CN_TOPIC_0000002529445763__oh_cameramanager_createcapturesession)后立即使用此接口。

[Camera_ErrorCode OH_CaptureSession_AddSecureOutput(Camera_CaptureSession* session, Camera_PreviewOutput* previewOutput)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_addsecureoutput)-把其中一条PreviewOutput标记成安全输出。[Camera_ErrorCode OH_CaptureSession_BeginConfig(Camera_CaptureSession* session)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_beginconfig)-开始捕获会话配置。[Camera_ErrorCode OH_CaptureSession_CommitConfig(Camera_CaptureSession* session)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_commitconfig)-提交捕获会话配置。[Camera_ErrorCode OH_CaptureSession_AddInput(Camera_CaptureSession* session, Camera_Input* cameraInput)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_addinput)-添加相机输入。[Camera_ErrorCode OH_CaptureSession_RemoveInput(Camera_CaptureSession* session, Camera_Input* cameraInput)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_removeinput)-删除相机输入。[Camera_ErrorCode OH_CaptureSession_AddPreviewOutput(Camera_CaptureSession* session, Camera_PreviewOutput* previewOutput)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_addpreviewoutput)-添加预览输出。[Camera_ErrorCode OH_CaptureSession_RemovePreviewOutput(Camera_CaptureSession* session, Camera_PreviewOutput* previewOutput)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_removepreviewoutput)-删除预览输出。[Camera_ErrorCode OH_CaptureSession_AddPhotoOutput(Camera_CaptureSession* session, Camera_PhotoOutput* photoOutput)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_addphotooutput)-添加拍照输出。[Camera_ErrorCode OH_CaptureSession_RemovePhotoOutput(Camera_CaptureSession* session, Camera_PhotoOutput* photoOutput)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_removephotooutput)-删除拍照输出。[Camera_ErrorCode OH_CaptureSession_AddVideoOutput(Camera_CaptureSession* session, Camera_VideoOutput* videoOutput)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_addvideooutput)-添加录像输出。[Camera_ErrorCode OH_CaptureSession_RemoveVideoOutput(Camera_CaptureSession* session, Camera_VideoOutput* videoOutput)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_removevideooutput)-删除录像输出。[Camera_ErrorCode OH_CaptureSession_AddMetadataOutput(Camera_CaptureSession* session, Camera_MetadataOutput* metadataOutput)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_addmetadataoutput)-添加元数据输出。[Camera_ErrorCode OH_CaptureSession_RemoveMetadataOutput(Camera_CaptureSession* session, Camera_MetadataOutput* metadataOutput)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_removemetadataoutput)-删除元数据输出。[Camera_ErrorCode OH_CaptureSession_Start(Camera_CaptureSession* session)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_start)-启动捕获会话。[Camera_ErrorCode OH_CaptureSession_Stop(Camera_CaptureSession* session)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_stop)-停止捕获会话。[Camera_ErrorCode OH_CaptureSession_Release(Camera_CaptureSession* session)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_release)-释放捕获会话。[Camera_ErrorCode OH_CaptureSession_HasFlash(Camera_CaptureSession* session, bool* hasFlash)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_hasflash)-检查设备是否有闪光灯。[Camera_ErrorCode OH_CaptureSession_IsFlashModeSupported(Camera_CaptureSession* session, Camera_FlashMode flashMode, bool* isSupported)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_isflashmodesupported)-检查是否支持指定的闪光灯模式。[Camera_ErrorCode OH_CaptureSession_GetFlashMode(Camera_CaptureSession* session, Camera_FlashMode* flashMode)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_getflashmode)-获取当前闪光灯模式。[Camera_ErrorCode OH_CaptureSession_SetFlashMode(Camera_CaptureSession* session, Camera_FlashMode flashMode)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_setflashmode)-设置闪光灯模式。[Camera_ErrorCode OH_CaptureSession_IsExposureModeSupported(Camera_CaptureSession* session, Camera_ExposureMode exposureMode, bool* isSupported)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_isexposuremodesupported)-检查是否支持指定的曝光模式。[Camera_ErrorCode OH_CaptureSession_GetExposureMode(Camera_CaptureSession* session, Camera_ExposureMode* exposureMode)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_getexposuremode)-获取当前曝光模式。[Camera_ErrorCode OH_CaptureSession_SetExposureMode(Camera_CaptureSession* session, Camera_ExposureMode exposureMode)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_setexposuremode)-设置曝光模式。[Camera_ErrorCode OH_CaptureSession_GetMeteringPoint(Camera_CaptureSession* session, Camera_Point* point)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_getmeteringpoint)-获取当前测量点。[Camera_ErrorCode OH_CaptureSession_SetMeteringPoint(Camera_CaptureSession* session, Camera_Point point)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_setmeteringpoint)-设置计量区域的中心点。[Camera_ErrorCode OH_CaptureSession_GetExposureBiasRange(Camera_CaptureSession* session, float* minExposureBias, float* maxExposureBias, float* step)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_getexposurebiasrange)-查询曝光补偿范围。[Camera_ErrorCode OH_CaptureSession_SetExposureBias(Camera_CaptureSession* session, float exposureBias)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_setexposurebias)-设置曝光补偿。[Camera_ErrorCode OH_CaptureSession_GetExposureBias(Camera_CaptureSession* session, float* exposureBias)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_getexposurebias)-获取当前曝光补偿。[Camera_ErrorCode OH_CaptureSession_IsFocusModeSupported(Camera_CaptureSession* session, Camera_FocusMode focusMode, bool* isSupported)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_isfocusmodesupported)-检查是否支持指定的聚焦模式。[Camera_ErrorCode OH_CaptureSession_GetFocusMode(Camera_CaptureSession* session, Camera_FocusMode* focusMode)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_getfocusmode)-获取当前聚焦模式。[Camera_ErrorCode OH_CaptureSession_SetFocusMode(Camera_CaptureSession* session, Camera_FocusMode focusMode)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_setfocusmode)-设置聚焦模式。[Camera_ErrorCode OH_CaptureSession_GetFocusPoint(Camera_CaptureSession* session, Camera_Point* focusPoint)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_getfocuspoint)-获取当前焦点。[Camera_ErrorCode OH_CaptureSession_SetFocusPoint(Camera_CaptureSession* session, Camera_Point focusPoint)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_setfocuspoint)-设置焦点。[Camera_ErrorCode OH_CaptureSession_GetZoomRatioRange(Camera_CaptureSession* session, float* minZoom, float* maxZoom)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_getzoomratiorange)-获取所有支持的缩放比例范围。[Camera_ErrorCode OH_CaptureSession_GetZoomRatio(Camera_CaptureSession* session, float* zoom)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_getzoomratio)-获取当前缩放比例。[Camera_ErrorCode OH_CaptureSession_SetZoomRatio(Camera_CaptureSession* session, float zoom)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_setzoomratio)-设置缩放比例。[Camera_ErrorCode OH_CaptureSession_IsVideoStabilizationModeSupported(Camera_CaptureSession* session, Camera_VideoStabilizationMode mode, bool* isSupported)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_isvideostabilizationmodesupported)-检查是否支持指定的录像防抖模式。[Camera_ErrorCode OH_CaptureSession_GetVideoStabilizationMode(Camera_CaptureSession* session, Camera_VideoStabilizationMode* mode)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_getvideostabilizationmode)-获取当前录像防抖模式。[Camera_ErrorCode OH_CaptureSession_SetVideoStabilizationMode(Camera_CaptureSession* session, Camera_VideoStabilizationMode mode)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_setvideostabilizationmode)-设置录像防抖模式。[Camera_ErrorCode OH_CaptureSession_CanAddInput(Camera_CaptureSession* session, Camera_Input* cameraInput, bool* isSuccessful)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_canaddinput)-确定是否可以将相机输入添加到会话中。[Camera_ErrorCode OH_CaptureSession_CanAddPreviewOutput(Camera_CaptureSession* session, Camera_PreviewOutput* cameraOutput, bool* isSuccessful)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_canaddpreviewoutput)-确定是否可以将相机预览输出添加到会话中。[Camera_ErrorCode OH_CaptureSession_CanAddPhotoOutput(Camera_CaptureSession* session, Camera_PhotoOutput* cameraOutput, bool* isSuccessful)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_canaddphotooutput)-确定是否可以将拍照输出添加到会话中。[Camera_ErrorCode OH_CaptureSession_CanAddVideoOutput(Camera_CaptureSession* session, Camera_VideoOutput* cameraOutput, bool* isSuccessful)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_canaddvideooutput)-确定是否可以将录像输出添加到会话中。[Camera_ErrorCode OH_CaptureSession_CanPreconfig(Camera_CaptureSession* session, Camera_PreconfigType preconfigType, bool* canPreconfig)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_canpreconfig)-检查是否支持指定的预配置类型。[Camera_ErrorCode OH_CaptureSession_CanPreconfigWithRatio(Camera_CaptureSession* session, Camera_PreconfigType preconfigType, Camera_PreconfigRatio preconfigRatio, bool* canPreconfig)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_canpreconfigwithratio)-检查是否支持带比例的预配置类型。[Camera_ErrorCode OH_CaptureSession_Preconfig(Camera_CaptureSession* session, Camera_PreconfigType preconfigType)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_preconfig)-设置预配置类型。[Camera_ErrorCode OH_CaptureSession_PreconfigWithRatio(Camera_CaptureSession* session, Camera_PreconfigType preconfigType, Camera_PreconfigRatio preconfigRatio)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_preconfigwithratio)-设置带有比例的预配置类型。[Camera_ErrorCode OH_CaptureSession_GetExposureValue(Camera_CaptureSession* session, float* exposureValue)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_getexposurevalue)-查询曝光值。[Camera_ErrorCode OH_CaptureSession_GetFocalLength(Camera_CaptureSession* session, float* focalLength)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_getfocallength)-获取当前焦距值。[Camera_ErrorCode OH_CaptureSession_SetSmoothZoom(Camera_CaptureSession* session, float targetZoom, Camera_SmoothZoomMode smoothZoomMode)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_setsmoothzoom)-触发平滑变焦。[Camera_ErrorCode OH_CaptureSession_GetSupportedColorSpaces(Camera_CaptureSession* session, OH_NativeBuffer_ColorSpace** colorSpace, uint32_t* size)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_getsupportedcolorspaces)-获取支持的色彩空间列表。[Camera_ErrorCode OH_CaptureSession_DeleteColorSpaces(Camera_CaptureSession* session, OH_NativeBuffer_ColorSpace* colorSpace)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_deletecolorspaces)-删除色彩空间列表。[Camera_ErrorCode OH_CaptureSession_GetActiveColorSpace(Camera_CaptureSession* session, OH_NativeBuffer_ColorSpace* colorSpace)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_getactivecolorspace)-获取当前色彩空间。[Camera_ErrorCode OH_CaptureSession_SetActiveColorSpace(Camera_CaptureSession* session, OH_NativeBuffer_ColorSpace colorSpace)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_setactivecolorspace)-设置当前色彩空间。[Camera_ErrorCode OH_CaptureSession_RegisterAutoDeviceSwitchStatusCallback(Camera_CaptureSession* session, OH_CaptureSession_OnAutoDeviceSwitchStatusChange autoDeviceSwitchStatusChange)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_registerautodeviceswitchstatuscallback)-注册设备切换事件回调。[Camera_ErrorCode OH_CaptureSession_UnregisterAutoDeviceSwitchStatusCallback(Camera_CaptureSession* session, OH_CaptureSession_OnAutoDeviceSwitchStatusChange autoDeviceSwitchStatusChange)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_unregisterautodeviceswitchstatuscallback)-注销设备切换事件回调。[Camera_ErrorCode OH_CaptureSession_IsAutoDeviceSwitchSupported(Camera_CaptureSession* session, bool* isSupported)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_isautodeviceswitchsupported)-检查是否支持自动设备切换。[Camera_ErrorCode OH_CaptureSession_EnableAutoDeviceSwitch(Camera_CaptureSession* session, bool enabled)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_enableautodeviceswitch)-是否启用相机设备的自动切换。[Camera_ErrorCode OH_CaptureSession_RegisterSystemPressureLevelChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnSystemPressureLevelChange systemPressureLevelChange)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_registersystempressurelevelchangecallback)-注册系统压力状态变化回调。[Camera_ErrorCode OH_CaptureSession_UnregisterSystemPressureLevelChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnSystemPressureLevelChange systemPressureLevelChange)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_unregistersystempressurelevelchangecallback)-注销系统压力状态变化回调。[Camera_ErrorCode OH_CaptureSession_SetQualityPrioritization(Camera_CaptureSession* session, Camera_QualityPrioritization qualityPrioritization)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_setqualityprioritization)-

设置录像质量优先级。

 默认为高录像质量，设置为功耗平衡将降低录像质量以减少功耗。实际功耗收益因平台而异。建议该接口在[OH_CaptureSession_CommitConfig](capture_session.h.md#ZH-CN_TOPIC_0000002497605800__oh_capturesession_commitconfig)和[OH_CaptureSession_Start](capture_session.h.md#ZH-CN_TOPIC_0000002497605800__oh_capturesession_start)之间调用。

[Camera_ErrorCode OH_CaptureSession_IsMacroSupported(Camera_CaptureSession* session, bool* isSupported)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_ismacrosupported)-检查是否支持微距能力。[Camera_ErrorCode OH_CaptureSession_EnableMacro(Camera_CaptureSession* session, bool enabled)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_enablemacro)-是否启用相机设备的微距能力。[Camera_ErrorCode OH_CaptureSession_SetWhiteBalance(Camera_CaptureSession* session, int32_t colorTemperature)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_setwhitebalance)-

设置白平衡的色温。

 设置前，建议通过[OH_CaptureSession_GetWhiteBalanceRange](capture_session.h.md#ZH-CN_TOPIC_0000002497605800__oh_capturesession_getwhitebalancerange)获取支持配置的白平衡色温范围。

[Camera_ErrorCode OH_CaptureSession_GetWhiteBalance(Camera_CaptureSession* session, int32_t *colorTemperature)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_getwhitebalance)-获取当前白平衡色温值。[Camera_ErrorCode OH_CaptureSession_GetWhiteBalanceMode(Camera_CaptureSession* session, Camera_WhiteBalanceMode* whiteBalanceMode)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_getwhitebalancemode)-获取当前的白平衡模式。[Camera_ErrorCode OH_CaptureSession_IsWhiteBalanceModeSupported(Camera_CaptureSession* session, Camera_WhiteBalanceMode whiteBalanceMode, bool* isSupported)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_iswhitebalancemodesupported)-检查是否支持指定的白平衡模式。[Camera_ErrorCode OH_CaptureSession_SetWhiteBalanceMode(Camera_CaptureSession* session, Camera_WhiteBalanceMode whiteBalanceMode)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_setwhitebalancemode)-设置白平衡模式。[Camera_ErrorCode OH_CaptureSession_GetWhiteBalanceRange(Camera_CaptureSession* session, int32_t *minColorTemperature, int32_t *maxColorTemperature)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_getwhitebalancerange)-获取支持配置的白平衡色温范围。[Camera_ErrorCode OH_CaptureSession_IsControlCenterSupported(Camera_CaptureSession* session, bool* isSupported)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_iscontrolcentersupported)-检查是否支持相机控制器。[Camera_ErrorCode OH_CaptureSession_GetSupportedEffectTypes(Camera_CaptureSession* session, Camera_ControlCenterEffectType** types, uint32_t* size)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_getsupportedeffecttypes)-获取相机控制器支持的效果类型。[Camera_ErrorCode OH_CaptureSession_DeleteSupportedEffectTypes(Camera_CaptureSession* session, Camera_ControlCenterEffectType* types, uint32_t size)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_deletesupportedeffecttypes)-删除相机控制器效果类型列表。[Camera_ErrorCode OH_CaptureSession_EnableControlCenter(Camera_CaptureSession* session, bool enabled)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_enablecontrolcenter)-是否启用相机控制器。[Camera_ErrorCode OH_CaptureSession_RegisterControlCenterEffectStatusChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnControlCenterEffectStatusChange controlCenterEffectStatusChange)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_registercontrolcentereffectstatuschangecallback)-注册相机控制器效果激活状态变化回调。[Camera_ErrorCode OH_CaptureSession_UnregisterControlCenterEffectStatusChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnControlCenterEffectStatusChange controlCenterEffectStatusChange)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_unregistercontrolcentereffectstatuschangecallback)-注销相机控制器效果激活状态变化回调。[ typedef void (*OH_CaptureSession_OnMacroStatusChange)(Camera_CaptureSession* session, bool isMacroDetected)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_onmacrostatuschange)OH_CaptureSession_OnMacroStatusChange相机会话微距状态改变回调。[ Camera_ErrorCode OH_CaptureSession_RegisterMacroStatusChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnMacroStatusChange macroStatusChange)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_registermacrostatuschangecallback)-注册相机会话微距状态改变回调函数。[ Camera_ErrorCode OH_CaptureSession_UnregisterMacroStatusChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnMacroStatusChange macroStatusChange)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_unregistermacrostatuschangecallback)-取消注册相机会话微距状态改变回调函数。[typedef void (*OH_CaptureSession_OnIsoChange)(Camera_CaptureSession* session, int32_t isoValue)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_onisochange)OH_CaptureSession_OnIsoChange用于在相机会话中监听感光度（ISO）变化的回调函数。[Camera_ErrorCode OH_CaptureSession_RegisterIsoChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnIsoChange isoChange)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_registerisochangecallback)-注册监听感光度（ISO）改变的事件回调。[Camera_ErrorCode OH_CaptureSession_UnregisterIsoChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnIsoChange isoChange)](#ZH-CN_TOPIC_0000002497605800__oh_capturesession_unregisterisochangecallback)-取消注册监听感光度（ISO）改变的事件回调。

#### 函数说明

#### OH_CaptureSession_OnFocusStateChange()

```ets
typedef void (*OH_CaptureSession_OnFocusStateChange)(Camera_CaptureSession* session, Camera_FocusState focusState)
```

**描述**

在[CaptureSession_Callbacks](CaptureSession_Callbacks.md)中被调用的捕获会话焦点状态回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session传递回调的Camera_CaptureSession实例。[Camera_FocusState](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_focusstate) focusState回调传递的会话焦点状态。

#### OH_CaptureSession_OnError()

```ets
typedef void (*OH_CaptureSession_OnError)(Camera_CaptureSession* session, Camera_ErrorCode errorCode)
```

**描述**

在[CaptureSession_Callbacks](CaptureSession_Callbacks.md)中被调用的捕获会话错误回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session传递回调的Camera_CaptureSession实例。[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode) errorCode捕获会话的错误码。

**参考：**

[CAMERA_SERVICE_FATAL_ERROR](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

#### OH_CaptureSession_OnSmoothZoomInfo()

```ets
typedef void (*OH_CaptureSession_OnSmoothZoomInfo)(Camera_CaptureSession* session,Camera_SmoothZoomInfo* smoothZoomInfo)
```

**描述**

拍照会话平滑变焦信息回调，触发平滑变焦后该回调会返回。

**起始版本：** 12

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session传递回调的Camera_CaptureSession实例。[Camera_SmoothZoomInfo](Camera_SmoothZoomInfo.md)* smoothZoomInfo回调传递的平滑变焦参数信息。

#### OH_CaptureSession_OnAutoDeviceSwitchStatusChange()

```ets
typedef void (*OH_CaptureSession_OnAutoDeviceSwitchStatusChange)(Camera_CaptureSession* session, Camera_AutoDeviceSwitchStatusInfo* autoDeviceSwitchStatusInfo)
```

**描述**

捕获会话设备切换状态回调。

**起始版本：** 13

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session传递回调的Camera_CaptureSession实例。[Camera_AutoDeviceSwitchStatusInfo](Camera_AutoDeviceSwitchStatusInfo.md)* autoDeviceSwitchStatusInfo回调传递的设备切换状态信息。

#### OH_CaptureSession_OnSystemPressureLevelChange()

```ets
typedef void (*OH_CaptureSession_OnSystemPressureLevelChange)(Camera_CaptureSession* session, Camera_SystemPressureLevel systemPressureLevel)
```

**描述**

捕获系统压力状态变化回调。

**起始版本：** 20

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session传递回调的Camera_CaptureSession实例。[Camera_SystemPressureLevel](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_systempressurelevel) systemPressureLevel回调传递的系统压力等级。

#### OH_CaptureSession_OnControlCenterEffectStatusChange()

```ets
typedef void (*OH_CaptureSession_OnControlCenterEffectStatusChange)(Camera_CaptureSession* session, Camera_ControlCenterStatusInfo* controlCenterStatusInfo)
```

**描述**

相机控制器效果激活状态变化回调。

**起始版本：** 20

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session传递回调的Camera_CaptureSession实例。[Camera_ControlCenterStatusInfo](Camera_ControlCenterStatusInfo.md)* controlCenterStatusInfo回调传递的相机控制器效果激活状态。

#### OH_CaptureSession_RegisterCallback()

```ets
Camera_ErrorCode OH_CaptureSession_RegisterCallback(Camera_CaptureSession* session, CaptureSession_Callbacks* callback)
```

**描述**

注册捕获会话事件回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session传递回调的Camera_CaptureSession实例。[CaptureSession_Callbacks](CaptureSession_Callbacks.md)* callback要注册的捕获会话事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CaptureSession_UnregisterCallback()

```ets
Camera_ErrorCode OH_CaptureSession_UnregisterCallback(Camera_CaptureSession* session, CaptureSession_Callbacks* callback)
```

**描述**

注销捕获会话事件回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session传递回调的Camera_CaptureSession实例。[CaptureSession_Callbacks](CaptureSession_Callbacks.md)* callback要注销的捕获会话事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CaptureSession_RegisterSmoothZoomInfoCallback()

```ets
Camera_ErrorCode OH_CaptureSession_RegisterSmoothZoomInfoCallback(Camera_CaptureSession* session, OH_CaptureSession_OnSmoothZoomInfo smoothZoomInfoCallback)
```

**描述**

注册平滑变焦信息事件回调。

**起始版本：** 12

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session传递回调的Camera_CaptureSession实例。[OH_CaptureSession_OnSmoothZoomInfo](capture_session.h.md#ZH-CN_TOPIC_0000002497605800__oh_capturesession_onsmoothzoominfo) smoothZoomInfoCallback要注册的平滑变焦信息事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CaptureSession_UnregisterSmoothZoomInfoCallback()

```ets
Camera_ErrorCode OH_CaptureSession_UnregisterSmoothZoomInfoCallback(Camera_CaptureSession* session, OH_CaptureSession_OnSmoothZoomInfo smoothZoomInfoCallback)
```

**描述**

注销平滑变焦信息事件回调。

**起始版本：** 12

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session传递回调的Camera_CaptureSession实例。[OH_CaptureSession_OnSmoothZoomInfo](capture_session.h.md#ZH-CN_TOPIC_0000002497605800__oh_capturesession_onsmoothzoominfo) smoothZoomInfoCallback要注销的平滑变焦信息事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CaptureSession_SetSessionMode()

```ets
Camera_ErrorCode OH_CaptureSession_SetSessionMode(Camera_CaptureSession* session, Camera_SceneMode sceneMode)
```

**描述**

设置会话模式。

 此接口不能在[OH_CaptureSession_BeginConfig](capture_session.h.md#ZH-CN_TOPIC_0000002497605800__oh_capturesession_beginconfig)之后使用。

 建议在使用[OH_CameraManager_CreateCaptureSession](camera_manager.h.md#ZH-CN_TOPIC_0000002529445763__oh_cameramanager_createcapturesession)后立即使用此接口。

**起始版本：** 12

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_SceneMode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_scenemode) sceneMode相机模式。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_OPERATION_NOT_ALLOWED：操作不允许。

 CAMERA_SESSION_CONFIG_LOCKED：会话配置已锁定。

#### OH_CaptureSession_AddSecureOutput()

```ets
Camera_ErrorCode OH_CaptureSession_AddSecureOutput(Camera_CaptureSession* session, Camera_PreviewOutput* previewOutput)
```

**描述**

把其中一条PreviewOutput标记成安全输出。

**起始版本：** 12

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_PreviewOutput](Camera_PreviewOutput.md)* previewOutput要标记为安全输出的Camera_PreviewOutput。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_OPERATION_NOT_ALLOWED：操作不允许。

 CAMERA_SESSION_CONFIG_LOCKED：会话配置已锁定。

#### OH_CaptureSession_BeginConfig()

```ets
Camera_ErrorCode OH_CaptureSession_BeginConfig(Camera_CaptureSession* session)
```

**描述**

开始捕获会话配置。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_CONFIG_LOCKED：会话配置已锁定。

#### OH_CaptureSession_CommitConfig()

```ets
Camera_ErrorCode OH_CaptureSession_CommitConfig(Camera_CaptureSession* session)
```

**描述**

提交捕获会话配置。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_OPERATION_NOT_ALLOWED：操作不允许。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_CaptureSession_AddInput()

```ets
Camera_ErrorCode OH_CaptureSession_AddInput(Camera_CaptureSession* session, Camera_Input* cameraInput)
```

**描述**

添加相机输入。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_Input](Camera_Input.md)* cameraInput要添加的相机输入实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_OPERATION_NOT_ALLOWED：操作不允许。

#### OH_CaptureSession_RemoveInput()

```ets
Camera_ErrorCode OH_CaptureSession_RemoveInput(Camera_CaptureSession* session, Camera_Input* cameraInput)
```

**描述**

删除相机输入。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_Input](Camera_Input.md)* cameraInput要删除的相机输入实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_OPERATION_NOT_ALLOWED：操作不允许。

#### OH_CaptureSession_AddPreviewOutput()

```ets
Camera_ErrorCode OH_CaptureSession_AddPreviewOutput(Camera_CaptureSession* session, Camera_PreviewOutput* previewOutput)
```

**描述**

添加预览输出。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_PreviewOutput](Camera_PreviewOutput.md)* previewOutput要添加的预览输出实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_OPERATION_NOT_ALLOWED：操作不允许。

#### OH_CaptureSession_RemovePreviewOutput()

```ets
Camera_ErrorCode OH_CaptureSession_RemovePreviewOutput(Camera_CaptureSession* session, Camera_PreviewOutput* previewOutput)
```

**描述**

删除预览输出。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_PreviewOutput](Camera_PreviewOutput.md)* previewOutput要删除的预览输出实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_OPERATION_NOT_ALLOWED：操作不允许。

#### OH_CaptureSession_AddPhotoOutput()

```ets
Camera_ErrorCode OH_CaptureSession_AddPhotoOutput(Camera_CaptureSession* session, Camera_PhotoOutput* photoOutput)
```

**描述**

添加拍照输出。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput要添加的拍照输出实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_OPERATION_NOT_ALLOWED：操作不允许。

#### OH_CaptureSession_RemovePhotoOutput()

```ets
Camera_ErrorCode OH_CaptureSession_RemovePhotoOutput(Camera_CaptureSession* session, Camera_PhotoOutput* photoOutput)
```

**描述**

删除拍照输出。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput要删除的拍照输出实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_OPERATION_NOT_ALLOWED：操作不允许。

#### OH_CaptureSession_AddVideoOutput()

```ets
Camera_ErrorCode OH_CaptureSession_AddVideoOutput(Camera_CaptureSession* session, Camera_VideoOutput* videoOutput)
```

**描述**

添加录像输出。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_VideoOutput](Camera_VideoOutput.md)* videoOutput要添加的录像输出实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_OPERATION_NOT_ALLOWED：操作不允许。

#### OH_CaptureSession_RemoveVideoOutput()

```ets
Camera_ErrorCode OH_CaptureSession_RemoveVideoOutput(Camera_CaptureSession* session, Camera_VideoOutput* videoOutput)
```

**描述**

删除录像输出。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_VideoOutput](Camera_VideoOutput.md)* videoOutput要删除的录像输出实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_OPERATION_NOT_ALLOWED：操作不允许。

#### OH_CaptureSession_AddMetadataOutput()

```ets
Camera_ErrorCode OH_CaptureSession_AddMetadataOutput(Camera_CaptureSession* session, Camera_MetadataOutput* metadataOutput)
```

**描述**

添加元数据输出。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_MetadataOutput](Camera_MetadataOutput.md)* metadataOutput要添加的元数据输出实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_OPERATION_NOT_ALLOWED：操作不允许。

#### OH_CaptureSession_RemoveMetadataOutput()

```ets
Camera_ErrorCode OH_CaptureSession_RemoveMetadataOutput(Camera_CaptureSession* session, Camera_MetadataOutput* metadataOutput)
```

**描述**

删除元数据输出。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_MetadataOutput](Camera_MetadataOutput.md)* metadataOutput要删除的元数据输出实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_OPERATION_NOT_ALLOWED：操作不允许。

#### OH_CaptureSession_Start()

```ets
Camera_ErrorCode OH_CaptureSession_Start(Camera_CaptureSession* session)
```

**描述**

启动捕获会话。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session要启动的Camera_CaptureSession实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_CaptureSession_Stop()

```ets
Camera_ErrorCode OH_CaptureSession_Stop(Camera_CaptureSession* session)
```

**描述**

停止捕获会话。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session要停止的Camera_CaptureSession实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_CaptureSession_Release()

```ets
Camera_ErrorCode OH_CaptureSession_Release(Camera_CaptureSession* session)
```

**描述**

释放捕获会话。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session要释放的Camera_CaptureSession实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_CaptureSession_HasFlash()

```ets
Camera_ErrorCode OH_CaptureSession_HasFlash(Camera_CaptureSession* session, bool* hasFlash)
```

**描述**

检查设备是否有闪光灯。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。bool* hasFlash是否支持闪光灯的结果。返回true表示支持闪光灯，返回false表示不支持。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_IsFlashModeSupported()

```ets
Camera_ErrorCode OH_CaptureSession_IsFlashModeSupported(Camera_CaptureSession* session, Camera_FlashMode flashMode, bool* isSupported)
```

**描述**

检查是否支持指定的闪光灯模式。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_FlashMode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_flashmode) flashMode要检查的闪光灯模式。bool* isSupported是否支持闪光灯模式的结果。返回true表示支持闪光灯模式，返回false表示不支持。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_GetFlashMode()

```ets
Camera_ErrorCode OH_CaptureSession_GetFlashMode(Camera_CaptureSession* session, Camera_FlashMode* flashMode)
```

**描述**

获取当前闪光灯模式。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_FlashMode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_flashmode)* flashMode当前闪光灯模式。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_SetFlashMode()

```ets
Camera_ErrorCode OH_CaptureSession_SetFlashMode(Camera_CaptureSession* session, Camera_FlashMode flashMode)
```

**描述**

设置闪光灯模式。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_FlashMode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_flashmode) flashMode要设置的闪光灯模式。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_IsExposureModeSupported()

```ets
Camera_ErrorCode OH_CaptureSession_IsExposureModeSupported(Camera_CaptureSession* session, Camera_ExposureMode exposureMode, bool* isSupported)
```

**描述**

检查是否支持指定的曝光模式。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_ExposureMode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_exposuremode) exposureMode要检查的曝光模式。bool* isSupported是否支持曝光模式的结果。返回true表示支持曝光模式，返回false表示不支持。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_GetExposureMode()

```ets
Camera_ErrorCode OH_CaptureSession_GetExposureMode(Camera_CaptureSession* session, Camera_ExposureMode* exposureMode)
```

**描述**

获取当前曝光模式。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_ExposureMode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_exposuremode)* exposureMode当前的曝光模式。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_SetExposureMode()

```ets
Camera_ErrorCode OH_CaptureSession_SetExposureMode(Camera_CaptureSession* session, Camera_ExposureMode exposureMode)
```

**描述**

设置曝光模式。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_ExposureMode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_exposuremode) exposureMode要设置的曝光模式。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_GetMeteringPoint()

```ets
Camera_ErrorCode OH_CaptureSession_GetMeteringPoint(Camera_CaptureSession* session, Camera_Point* point)
```

**描述**

获取当前测量点。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_Point](Camera_Point.md)* point当前测量点。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_SetMeteringPoint()

```ets
Camera_ErrorCode OH_CaptureSession_SetMeteringPoint(Camera_CaptureSession* session, Camera_Point point)
```

**描述**

设置计量区域的中心点。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_Point](Camera_Point.md) point要设置的测量点。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_GetExposureBiasRange()

```ets
Camera_ErrorCode OH_CaptureSession_GetExposureBiasRange(Camera_CaptureSession* session, float* minExposureBias, float* maxExposureBias, float* step)
```

**描述**

查询曝光补偿范围。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。float* minExposureBias曝光补偿的最小值。float* maxExposureBias曝光补偿的最大值。float* step每个级别之间的曝光补偿阶梯。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_SetExposureBias()

```ets
Camera_ErrorCode OH_CaptureSession_SetExposureBias(Camera_CaptureSession* session, float exposureBias)
```

**描述**

设置曝光补偿。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。float exposureBias要设置的曝光补偿。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_GetExposureBias()

```ets
Camera_ErrorCode OH_CaptureSession_GetExposureBias(Camera_CaptureSession* session, float* exposureBias)
```

**描述**

获取当前曝光补偿。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。float* exposureBias当前的曝光补偿。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_IsFocusModeSupported()

```ets
Camera_ErrorCode OH_CaptureSession_IsFocusModeSupported(Camera_CaptureSession* session, Camera_FocusMode focusMode, bool* isSupported)
```

**描述**

检查是否支持指定的聚焦模式。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_FocusMode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_focusmode) focusMode要检查的聚焦模式。bool* isSupported是否支持聚焦模式的结果。返回true表示支持聚焦模式，返回false表示不支持。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_GetFocusMode()

```ets
Camera_ErrorCode OH_CaptureSession_GetFocusMode(Camera_CaptureSession* session, Camera_FocusMode* focusMode)
```

**描述**

获取当前聚焦模式。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_FocusMode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_focusmode)* focusMode当前聚焦模式。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_SetFocusMode()

```ets
Camera_ErrorCode OH_CaptureSession_SetFocusMode(Camera_CaptureSession* session, Camera_FocusMode focusMode)
```

**描述**

设置聚焦模式。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_FocusMode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_focusmode) focusMode要设置的聚焦模式。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_GetFocusPoint()

```ets
Camera_ErrorCode OH_CaptureSession_GetFocusPoint(Camera_CaptureSession* session, Camera_Point* focusPoint)
```

**描述**

获取当前焦点。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_Point](Camera_Point.md)* focusPoint当前焦点。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_SetFocusPoint()

```ets
Camera_ErrorCode OH_CaptureSession_SetFocusPoint(Camera_CaptureSession* session, Camera_Point focusPoint)
```

**描述**

设置焦点。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_Point](Camera_Point.md) focusPoint要设置的目标点。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_GetZoomRatioRange()

```ets
Camera_ErrorCode OH_CaptureSession_GetZoomRatioRange(Camera_CaptureSession* session, float* minZoom, float* maxZoom)
```

**描述**

获取所有支持的缩放比例范围。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。float* minZoom缩放比范围的最小值。float* maxZoom缩放比例范围的最大值。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_GetZoomRatio()

```ets
Camera_ErrorCode OH_CaptureSession_GetZoomRatio(Camera_CaptureSession* session, float* zoom)
```

**描述**

获取当前缩放比例。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。float* zoom当前缩放比例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_SetZoomRatio()

```ets
Camera_ErrorCode OH_CaptureSession_SetZoomRatio(Camera_CaptureSession* session, float zoom)
```

**描述**

设置缩放比例。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。float zoom

要设置的目标缩放比。

 设置可变焦距比到底层生效需要一定时间，获取正确设置的可变焦距比需要等待1~2帧的时间。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_IsVideoStabilizationModeSupported()

```ets
Camera_ErrorCode OH_CaptureSession_IsVideoStabilizationModeSupported(Camera_CaptureSession* session, Camera_VideoStabilizationMode mode, bool* isSupported)
```

**描述**

检查是否支持指定的录像防抖模式。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_VideoStabilizationMode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_videostabilizationmode) mode要检查的录像防抖模式。bool* isSupported是否支持录像防抖模式的结果。返回true表示支持录像防抖模式，返回false表示不支持。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_GetVideoStabilizationMode()

```ets
Camera_ErrorCode OH_CaptureSession_GetVideoStabilizationMode(Camera_CaptureSession* session, Camera_VideoStabilizationMode* mode)
```

**描述**

获取当前录像防抖模式。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_VideoStabilizationMode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_videostabilizationmode)* mode当前录像防抖模式。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_SetVideoStabilizationMode()

```ets
Camera_ErrorCode OH_CaptureSession_SetVideoStabilizationMode(Camera_CaptureSession* session, Camera_VideoStabilizationMode mode)
```

**描述**

设置录像防抖模式。

**起始版本：** 11

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_VideoStabilizationMode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_videostabilizationmode) mode要设置的录像防抖模式。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_CanAddInput()

```ets
Camera_ErrorCode OH_CaptureSession_CanAddInput(Camera_CaptureSession* session, Camera_Input* cameraInput, bool* isSuccessful)
```

**描述**

确定是否可以将相机输入添加到会话中。

**起始版本：** 12

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_Input](Camera_Input.md)* cameraInput要设置的相机输入实例。bool* isSuccessful是否可以将相机输入添加到会话中的结果。返回true表示可以将相机输入添加到会话中，返回false表示不可以。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CaptureSession_CanAddPreviewOutput()

```ets
Camera_ErrorCode OH_CaptureSession_CanAddPreviewOutput(Camera_CaptureSession* session, Camera_PreviewOutput* cameraOutput, bool* isSuccessful)
```

**描述**

确定是否可以将相机预览输出添加到会话中。

**起始版本：** 12

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_PreviewOutput](Camera_PreviewOutput.md)* cameraOutput要设置的预览输出实例。bool* isSuccessful是否可以将相机预览输出添加到会话中的结果。返回true表示可以将相机预览输出添加到会话中，返回false表示不可以。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CaptureSession_CanAddPhotoOutput()

```ets
Camera_ErrorCode OH_CaptureSession_CanAddPhotoOutput(Camera_CaptureSession* session, Camera_PhotoOutput* cameraOutput, bool* isSuccessful)
```

**描述**

确定是否可以将拍照输出添加到会话中。

**起始版本：** 12

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_PhotoOutput](Camera_PhotoOutput.md)* cameraOutput要设置的拍照输出实例。bool* isSuccessful拍照输出是否可以添加到会话中的结果。返回true表示拍照输出可以添加到会话中，返回false表示不可以。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CaptureSession_CanAddVideoOutput()

```ets
Camera_ErrorCode OH_CaptureSession_CanAddVideoOutput(Camera_CaptureSession* session, Camera_VideoOutput* cameraOutput, bool* isSuccessful)
```

**描述**

确定是否可以将录像输出添加到会话中。

**起始版本：** 12

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_VideoOutput](Camera_VideoOutput.md)* cameraOutput要添加的录像输出实例。bool* isSuccessful录像输出是否可以添加到会话中的结果。返回true表示录像输出可以添加到会话中，返回false表示不可以。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CaptureSession_CanPreconfig()

```ets
Camera_ErrorCode OH_CaptureSession_CanPreconfig(Camera_CaptureSession* session, Camera_PreconfigType preconfigType, bool* canPreconfig)
```

**描述**

检查是否支持指定的预配置类型。

**起始版本：** 12

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_PreconfigType](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_preconfigtype) preconfigType要检查的预配置类型。bool* canPreconfig是否支持预配置的结果。返回true表示支持预配置，返回false表示不支持。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CaptureSession_CanPreconfigWithRatio()

```ets
Camera_ErrorCode OH_CaptureSession_CanPreconfigWithRatio(Camera_CaptureSession* session, Camera_PreconfigType preconfigType, Camera_PreconfigRatio preconfigRatio, bool* canPreconfig)
```

**描述**

检查是否支持带比例的预配置类型。

**起始版本：** 12

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_PreconfigType](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_preconfigtype) preconfigType要检查的预配置类型。[Camera_PreconfigRatio](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_preconfigratio) preconfigRatio要检查的预配置比例。bool* canPreconfig是否支持预配置的结果。返回true表示支持预配置，返回false表示不支持。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CaptureSession_Preconfig()

```ets
Camera_ErrorCode OH_CaptureSession_Preconfig(Camera_CaptureSession* session, Camera_PreconfigType preconfigType)
```

**描述**

设置预配置类型。

**起始版本：** 12

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_PreconfigType](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_preconfigtype) preconfigType指定的预配置类型。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_CaptureSession_PreconfigWithRatio()

```ets
Camera_ErrorCode OH_CaptureSession_PreconfigWithRatio(Camera_CaptureSession* session, Camera_PreconfigType preconfigType, Camera_PreconfigRatio preconfigRatio)
```

**描述**

设置带有比例的预配置类型。

**起始版本：** 12

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_PreconfigType](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_preconfigtype) preconfigType指定的预配置类型。[Camera_PreconfigRatio](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_preconfigratio) preconfigRatio指定的预配置比例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_CaptureSession_GetExposureValue()

```ets
Camera_ErrorCode OH_CaptureSession_GetExposureValue(Camera_CaptureSession* session, float* exposureValue)
```

**描述**

查询曝光值。

**起始版本：** 12

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。float* exposureValue当前的曝光值。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_CaptureSession_GetFocalLength()

```ets
Camera_ErrorCode OH_CaptureSession_GetFocalLength(Camera_CaptureSession* session, float* focalLength)
```

**描述**

获取当前焦距值。

**起始版本：** 12

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。float* focalLength当前焦距值。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_SetSmoothZoom()

```ets
Camera_ErrorCode OH_CaptureSession_SetSmoothZoom(Camera_CaptureSession* session, float targetZoom, Camera_SmoothZoomMode smoothZoomMode)
```

**描述**

触发平滑变焦。

**起始版本：** 12

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。float targetZoom要设置的目标变焦比。[Camera_SmoothZoomMode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_smoothzoommode) smoothZoomMode平滑变焦模式。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_GetSupportedColorSpaces()

```ets
Camera_ErrorCode OH_CaptureSession_GetSupportedColorSpaces(Camera_CaptureSession* session, OH_NativeBuffer_ColorSpace** colorSpace, uint32_t* size)
```

**描述**

获取支持的色彩空间列表。

**起始版本：** 12

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。OH_NativeBuffer_ColorSpace** colorSpace如果方法调用成功，将记录支持的OH_NativeBuffer_ColorSpace列表。uint32_t* size如果方法调用成功，将记录支持的OH_NativeBuffer_ColorSpace列表的大小。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_DeleteColorSpaces()

```ets
Camera_ErrorCode OH_CaptureSession_DeleteColorSpaces(Camera_CaptureSession* session, OH_NativeBuffer_ColorSpace* colorSpace)
```

**描述**

删除色彩空间列表。

**起始版本：** 12

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[OH_NativeBuffer_ColorSpace](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_colorspace)* colorSpace如果方法调用成功，将删除的OH_NativeBuffer_ColorSpace列表。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CaptureSession_GetActiveColorSpace()

```ets
Camera_ErrorCode OH_CaptureSession_GetActiveColorSpace(Camera_CaptureSession* session, OH_NativeBuffer_ColorSpace* colorSpace)
```

**描述**

获取当前色彩空间。

**起始版本：** 12

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[OH_NativeBuffer_ColorSpace](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_colorspace)* colorSpace当前的OH_NativeBuffer_ColorSpace。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_SetActiveColorSpace()

```ets
Camera_ErrorCode OH_CaptureSession_SetActiveColorSpace(Camera_CaptureSession* session, OH_NativeBuffer_ColorSpace colorSpace)
```

**描述**

设置当前色彩空间。

**起始版本：** 12

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[OH_NativeBuffer_ColorSpace](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_colorspace) colorSpace要设置的目标OH_NativeBuffer_ColorSpace。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_RegisterAutoDeviceSwitchStatusCallback()

```ets
Camera_ErrorCode OH_CaptureSession_RegisterAutoDeviceSwitchStatusCallback(Camera_CaptureSession* session, OH_CaptureSession_OnAutoDeviceSwitchStatusChange autoDeviceSwitchStatusChange)
```

**描述**

注册设备切换事件回调。

**起始版本：** 13

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[OH_CaptureSession_OnAutoDeviceSwitchStatusChange](capture_session.h.md#ZH-CN_TOPIC_0000002497605800__oh_capturesession_onautodeviceswitchstatuschange) autoDeviceSwitchStatusChange要注册的设备切换事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CaptureSession_UnregisterAutoDeviceSwitchStatusCallback()

```ets
Camera_ErrorCode OH_CaptureSession_UnregisterAutoDeviceSwitchStatusCallback(Camera_CaptureSession* session, OH_CaptureSession_OnAutoDeviceSwitchStatusChange autoDeviceSwitchStatusChange)
```

**描述**

注销设备切换事件回调。

**起始版本：** 13

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[OH_CaptureSession_OnAutoDeviceSwitchStatusChange](capture_session.h.md#ZH-CN_TOPIC_0000002497605800__oh_capturesession_onautodeviceswitchstatuschange) autoDeviceSwitchStatusChange要注销的设备切换事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CaptureSession_IsAutoDeviceSwitchSupported()

```ets
Camera_ErrorCode OH_CaptureSession_IsAutoDeviceSwitchSupported(Camera_CaptureSession* session, bool* isSupported)
```

**描述**

检查是否支持自动设备切换。

**起始版本：** 13

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。bool* isSupported是否支持自动设备切换的结果。返回true表示支持自动设备切换，返回false表示不支持。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_EnableAutoDeviceSwitch()

```ets
Camera_ErrorCode OH_CaptureSession_EnableAutoDeviceSwitch(Camera_CaptureSession* session, bool enabled)
```

**描述**

是否启用相机设备的自动切换。

**起始版本：** 13

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。bool enabled是否启用自动切换的标志。返回true表示启用自动切换，返回false表示不启用。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_CaptureSession_RegisterSystemPressureLevelChangeCallback()

```ets
Camera_ErrorCode OH_CaptureSession_RegisterSystemPressureLevelChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnSystemPressureLevelChange systemPressureLevelChange)
```

**描述**

注册系统压力状态变化回调。

**起始版本：** 20

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session传递回调的Camera_CaptureSession实例。[OH_CaptureSession_OnSystemPressureLevelChange](capture_session.h.md#ZH-CN_TOPIC_0000002497605800__oh_capturesession_onsystempressurelevelchange) systemPressureLevelChange要注册的系统压力状态变化OH_CaptureSession_OnSystemPressureLevelChange回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CaptureSession_UnregisterSystemPressureLevelChangeCallback()

```ets
Camera_ErrorCode OH_CaptureSession_UnregisterSystemPressureLevelChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnSystemPressureLevelChange systemPressureLevelChange)
```

**描述**

注销系统压力状态变化回调。

**起始版本：** 20

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session传递回调的Camera_CaptureSession实例。[OH_CaptureSession_OnSystemPressureLevelChange](capture_session.h.md#ZH-CN_TOPIC_0000002497605800__oh_capturesession_onsystempressurelevelchange) systemPressureLevelChange要注销的系统压力状态变化OH_CaptureSession_OnSystemPressureLevelChange回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CaptureSession_SetQualityPrioritization()

```ets
Camera_ErrorCode OH_CaptureSession_SetQualityPrioritization(Camera_CaptureSession* session, Camera_QualityPrioritization qualityPrioritization)
```

**描述**

设置录像质量优先级。

 默认为高录像质量，设置为功耗平衡将降低录像质量以减少功耗。实际功耗收益因平台而异。建议该接口在[OH_CaptureSession_CommitConfig](capture_session.h.md#ZH-CN_TOPIC_0000002497605800__oh_capturesession_commitconfig)和[OH_CaptureSession_Start](capture_session.h.md#ZH-CN_TOPIC_0000002497605800__oh_capturesession_start)之间调用。

**起始版本：** 14

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_QualityPrioritization](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_qualityprioritization) qualityPrioritization要设置的录像质量优先级，默认为高录像质量。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_IsMacroSupported()

```ets
Camera_ErrorCode OH_CaptureSession_IsMacroSupported(Camera_CaptureSession* session, bool* isSupported)
```

**描述**

检查是否支持微距能力。

**起始版本：** 19

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。bool* isSupported是否支持微距能力的结果。返回true表示支持微距能力，返回false表示不支持。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

 CAMERA_OK = 0：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_EnableMacro()

```ets
Camera_ErrorCode OH_CaptureSession_EnableMacro(Camera_CaptureSession* session, bool enabled)
```

**描述**

是否启用相机设备的微距能力。

**起始版本：** 19

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。bool enabled是否启用微距能力的标志。返回true表示启用微距能力，返回false表示不启用。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

 CAMERA_OK = 0：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

 CAMERA_OPERATION_NOT_ALLOWED：不允许操作。

#### OH_CaptureSession_SetWhiteBalance()

```ets
Camera_ErrorCode OH_CaptureSession_SetWhiteBalance(Camera_CaptureSession* session, int32_t colorTemperature)
```

**描述**

设置白平衡的色温。

 设置前，建议通过[OH_CaptureSession_GetWhiteBalanceRange](capture_session.h.md#ZH-CN_TOPIC_0000002497605800__oh_capturesession_getwhitebalancerange)获取支持配置的白平衡色温范围。

**起始版本：** 20

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。int32_t colorTemperature色温值，单位为K。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：设置成功。

 CAMERA_INVALID_ARGUMENT：参数缺失或者参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：相机会话未配置。

#### OH_CaptureSession_GetWhiteBalance()

```ets
Camera_ErrorCode OH_CaptureSession_GetWhiteBalance(Camera_CaptureSession* session, int32_t *colorTemperature)
```

**描述**

获取当前白平衡色温值。

**起始版本：** 20

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。int32_t *colorTemperature色温值，单位为K。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：函数调用成功。

 CAMERA_INVALID_ARGUMENT：参数缺失或者参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：相机会话未配置。

#### OH_CaptureSession_GetWhiteBalanceMode()

```ets
Camera_ErrorCode OH_CaptureSession_GetWhiteBalanceMode(Camera_CaptureSession* session, Camera_WhiteBalanceMode* whiteBalanceMode)
```

**描述**

获取当前的白平衡模式。

**起始版本：** 20

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_WhiteBalanceMode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_whitebalancemode)* whiteBalanceMode白平衡模式。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：函数调用成功。

 CAMERA_INVALID_ARGUMENT：参数缺失或者参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：相机会话未配置。

#### OH_CaptureSession_IsWhiteBalanceModeSupported()

```ets
Camera_ErrorCode OH_CaptureSession_IsWhiteBalanceModeSupported(Camera_CaptureSession* session, Camera_WhiteBalanceMode whiteBalanceMode, bool* isSupported)
```

**描述**

检查是否支持指定的白平衡模式。

**起始版本：** 20

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_WhiteBalanceMode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_whitebalancemode) whiteBalanceMode指定的白平衡模式。bool* isSupported用于返回是否支持指定的白平衡模式，支持返回true，否则返回false。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：函数调用成功。

 CAMERA_INVALID_ARGUMENT：参数缺失或者参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：相机会话未配置。

#### OH_CaptureSession_SetWhiteBalanceMode()

```ets
Camera_ErrorCode OH_CaptureSession_SetWhiteBalanceMode(Camera_CaptureSession* session, Camera_WhiteBalanceMode whiteBalanceMode)
```

**描述**

设置白平衡模式。

**起始版本：** 20

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_WhiteBalanceMode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_whitebalancemode) whiteBalanceMode白平衡模式。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：设置成功。

 CAMERA_INVALID_ARGUMENT：参数缺失或者参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：相机会话未配置。

#### OH_CaptureSession_GetWhiteBalanceRange()

```ets
Camera_ErrorCode OH_CaptureSession_GetWhiteBalanceRange(Camera_CaptureSession* session, int32_t *minColorTemperature, int32_t *maxColorTemperature)
```

**描述**

获取支持配置的白平衡色温范围。

**起始版本：** 20

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。int32_t *minColorTemperature支持的最小色温值，单位为K。int32_t *maxColorTemperature支持的最大色温值，单位为K。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：函数调用成功。

 CAMERA_INVALID_ARGUMENT：参数缺失或者参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：相机会话未配置。

#### OH_CaptureSession_IsControlCenterSupported()

```ets
Camera_ErrorCode OH_CaptureSession_IsControlCenterSupported(Camera_CaptureSession* session, bool* isSupported)
```

**描述**

检查是否支持相机控制器。

**起始版本：** 20

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。bool* isSupported是否支持相机控制器的结果。true表示支持，false表示不支持。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK = 0：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_GetSupportedEffectTypes()

```ets
Camera_ErrorCode OH_CaptureSession_GetSupportedEffectTypes(Camera_CaptureSession* session, Camera_ControlCenterEffectType** types, uint32_t* size)
```

**描述**

获取相机控制器支持的效果类型。

**起始版本：** 20

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_ControlCenterEffectType](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_controlcentereffecttype)** types如果方法调用成功，将记录支持的Camera_ControlCenterEffectType列表。uint32_t* size如果方法调用成功，将记录支持的Camera_ControlCenterEffectType列表的大小。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

#### OH_CaptureSession_DeleteSupportedEffectTypes()

```ets
Camera_ErrorCode OH_CaptureSession_DeleteSupportedEffectTypes(Camera_CaptureSession* session, Camera_ControlCenterEffectType* types, uint32_t size)
```

**描述**

删除相机控制器效果类型列表。

**起始版本：** 20

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。[Camera_ControlCenterEffectType](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_controlcentereffecttype)* types如果方法调用成功，要删除的Camera_ControlCenterEffectType列表。uint32_t size要删除的Camera_ControlCenterEffectType列表的大小。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CaptureSession_EnableControlCenter()

```ets
Camera_ErrorCode OH_CaptureSession_EnableControlCenter(Camera_CaptureSession* session, bool enabled)
```

**描述**

是否启用相机控制器。

**起始版本：** 20

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* sessionCamera_CaptureSession实例。bool enabled是否启用相机控制器的标志。true表示启用，false表示禁用。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK = 0：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_CaptureSession_RegisterControlCenterEffectStatusChangeCallback()

```ets
Camera_ErrorCode OH_CaptureSession_RegisterControlCenterEffectStatusChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnControlCenterEffectStatusChange controlCenterEffectStatusChange)
```

**描述**

注册相机控制器效果激活状态变化回调。

**起始版本：** 20

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session传递回调的Camera_CaptureSession实例。[OH_CaptureSession_OnControlCenterEffectStatusChange](capture_session.h.md#ZH-CN_TOPIC_0000002497605800__oh_capturesession_oncontrolcentereffectstatuschange) controlCenterEffectStatusChange要注册的相机控制器效果激活状态变化OH_CaptureSession_OnControlCenterEffectStatusChange回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CaptureSession_UnregisterControlCenterEffectStatusChangeCallback()

```ets
Camera_ErrorCode OH_CaptureSession_UnregisterControlCenterEffectStatusChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnControlCenterEffectStatusChange controlCenterEffectStatusChange)
```

**描述**

注销相机控制器效果激活状态变化回调。

**起始版本：** 20

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session传递回调的Camera_CaptureSession实例。[OH_CaptureSession_OnControlCenterEffectStatusChange](capture_session.h.md#ZH-CN_TOPIC_0000002497605800__oh_capturesession_oncontrolcentereffectstatuschange) controlCenterEffectStatusChange要注销的相机控制器效果激活状态变化OH_CaptureSession_OnControlCenterEffectStatusChange回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CaptureSession_OnMacroStatusChange()

```ets
 typedef void (*OH_CaptureSession_OnMacroStatusChange)(Camera_CaptureSession* session, bool isMacroDetected)
```

**描述**

相机会话微距状态改变回调。

**起始版本：** 20

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session指向Camera_CaptureSession实例的指针。bool isMacroDetected是否进入超级微距，true表示进入超级微距，false表示未进入超级微距。

#### OH_CaptureSession_RegisterMacroStatusChangeCallback()

```ets
 Camera_ErrorCode OH_CaptureSession_RegisterMacroStatusChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnMacroStatusChange macroStatusChange)
```

**描述**

注册相机会话微距状态改变回调函数。

**起始版本：** 20

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session指向Camera_CaptureSession实例的指针。[OH_CaptureSession_OnMacroStatusChange](capture_session.h.md#ZH-CN_TOPIC_0000002497605800__oh_capturesession_onmacrostatuschange) macroStatusChange微距状态改变回调函数。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CaptureSession_UnregisterMacroStatusChangeCallback()

```ets
 Camera_ErrorCode OH_CaptureSession_UnregisterMacroStatusChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnMacroStatusChange macroStatusChange)
```

**描述**

取消注册相机会话微距状态改变回调函数。

**起始版本：** 20

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session指向Camera_CaptureSession实例的指针。[OH_CaptureSession_OnMacroStatusChange](capture_session.h.md#ZH-CN_TOPIC_0000002497605800__oh_capturesession_onmacrostatuschange) macroStatusChange微距状态改变回调函数。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CaptureSession_OnIsoChange()

```ets
typedef void (*OH_CaptureSession_OnIsoChange)(Camera_CaptureSession* session, int32_t isoValue)
```

**描述**

用于在相机会话中监听感光度（ISO）变化的回调函数。

**起始版本：** 22

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session指向Camera_CaptureSession的指针。int32_t isoValue回调中获取的感光度（ISO）的值。

#### OH_CaptureSession_RegisterIsoChangeCallback()

```ets
Camera_ErrorCode OH_CaptureSession_RegisterIsoChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnIsoChange isoChange)
```

**描述**

注册监听感光度（ISO）改变的事件回调。

**起始版本：** 22

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session指向Camera_CaptureSession实例的指针。[OH_CaptureSession_OnIsoChange](capture_session.h.md#ZH-CN_TOPIC_0000002497605800__oh_capturesession_onisochange) isoChangeOH_CaptureSession_OnIsoChange类型的回调函数，用于监听ISO改变。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数缺失或者参数类型不正确。

#### OH_CaptureSession_UnregisterIsoChangeCallback()

```ets
Camera_ErrorCode OH_CaptureSession_UnregisterIsoChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnIsoChange isoChange)
```

**描述**

取消注册监听感光度（ISO）改变的事件回调。

**起始版本：** 22

**参数：**

参数项描述[Camera_CaptureSession](Camera_CaptureSession.md)* session指向Camera_CaptureSession实例的指针。[OH_CaptureSession_OnIsoChange](capture_session.h.md#ZH-CN_TOPIC_0000002497605800__oh_capturesession_onisochange) isoChangeOH_CaptureSession_OnIsoChange类型的回调函数，用于监听ISO改变。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数缺失或者参数类型不正确。