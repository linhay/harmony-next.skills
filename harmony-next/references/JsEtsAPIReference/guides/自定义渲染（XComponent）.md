# 自定义渲染 (XComponent)

本文根据华为开发者官网 `napi-xcomponent-guidelines` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-xcomponent-guidelines>
更新时间：2026-04-30 02:41:24

## 概述
XComponent组件作为一种渲染组件，可用于EGL/OpenGLES和媒体数据写入，通过使用XComponent持有的“NativeWindow”渲染画面，满足开发需要实现高级自定义渲染的需求，例如相机预览流的显示和游戏画面的渲染。开发者可通过指定XComponent组件的type字段来实现不同的渲染方式，分别为XComponentType.SURFACE和XComponentType.TEXTURE。对于SURFACE类型，开发者将定制的绘制内容单独展示到屏幕上。对于TEXTURE类型，开发者将定制的绘制内容和XComponent组件的内容合成后展示到屏幕上。
可以将XComponent类比为一个“画布”，在其上支持使用各种渲染技术（如OpenGL、Vulkan等）绘制复杂的图形，而XComponent组件则负责管理这个画布的位置、大小和各种交互事件。
目前XComponent主要用于两类场景：
场景类型
使用场景
高性能渲染
游戏画面、3D图形、复杂动画等。
媒体数据处理
相机预览、视频播放、图像处理等。

## 约束与限制
当开发者传输的绘制内容包含透明元素时，Surface区域的显示效果会与下方内容进行合成展示。例如，若传输的内容完全透明，且XComponent的背景色被设置为黑色，同时Surface保持默认的大小与位置，则最终显示的将是一片黑色区域。

## XComponent渲染上屏原理
XComponent持有一个Surface，开发者能通过调用NativeWindow等接口，申请并提交Buffer至图形队列，以此方式将自绘制内容传送至该Surface，其主体流程如下：
应用RequestBuffer获取空闲帧 → 应用生产帧数据 → 应用调用FlushBuffer提交到BufferQueue → 系统渲染侧通过AcquireBuffer获取帧 → 渲染到屏幕 → 系统渲染侧通过调用ReleaseBuffer释放。
经过上述流程，应用自绘制的内容就可以显示在XComponent持有的Surface区域，而XComponent则负责将此Surface整合进UI界面，其中展示的内容正是开发者发送的自绘制内容。Surface的默认位置与大小与XComponent组件一致，开发者可利用setXComponentSurfaceRect接口自定义调整Surface的位置和大小。XComponent组件负责创建Surface，并通过回调将Surface的相关信息告知应用。应用可以通过一系列接口设定Surface的属性。该组件本身不对所绘制的内容进行感知，亦不提供渲染绘制的接口。
主体流程中提到需要应用进行的RequestBuffer和FlushBuffer操作，在具体场景下一般已经被相关API（如相机模块、播放器模块、OpenGL相关接口等）封装，应用的实际开发者只需按要求调用这些API即可，不需要直接操作BufferQueue。

## 创建XComponent和管理Surface生命周期
为满足开发者的各种需求，XComponent组件提供了多种创建方式以及多种Surface生命周期的管理方式，下面将进行介绍。

## 创建XComponent
目前ArkUI提供了三种UI组件的创建方式，分别是使用ArkTS声明式UI描述创建、使用ArkTS自定义组件节点创建以及使用NDK接口创建。
通用UI界面开发场景下，建议使用ArkTS声明式UI描述创建XComponent组件。对于需要使用ArkTS自定义组件节点创建以及NDK接口创建的具体场景请参考这两种创建方式的相关介绍。

## 管理XComponent持有Surface的生命周期
在XComponent渲染上屏原理中提到，XComponent能够显示应用自绘制的内容依赖的是其持有的Surface，因此了解如何获取XComponent持有的Surface的生命周期也十分重要。
XComponent推荐使用两种方式获取XComponent持有Surface的生命周期，分别为在ArkTS侧使用XComponentController管理Surface生命周期，以及在Native侧使用OH_ArkUI_SurfaceHolder管理Surface生命周期。
对于需要在ArkTS侧使用已封装接口进行功能开发（如相机预览、视频播放等）或对跨语言性能损耗不敏感的跨语言开发，建议直接在ArkTS侧使用XComponentController管理Surface生命周期。其生命周期的触发时机如下：
onSurfaceCreated回调
触发时刻：XComponent创建完成且创建好Surface后触发。
ArkTS侧onSurfaceCreated的时序如下图：
onSurfaceChanged回调
触发时刻：Surface大小变化触发重新布局之后触发。
ArkTS侧onSurfaceChanged的时序如下图：
onSurfaceDestroyed回调
触发时刻：XComponent组件被销毁时触发，与一般ArkUI的组件销毁时机一致。
ArkTS侧onSurfaceDestroyed的时序图：

## XComponent的开发范式
将创建XComponent和管理XComponent持有Surface的生命周期进行排列组合，除使用NDK接口创建的XComponent无法在ArkTS侧使用XComponentController来管理Surface生命周期外，目前共有以下五种XComponent开发范式：
通过ArkTS声明式UI描述来创建组件并结合XComponentController实现对Surface生命周期的管理。
import nativeRender from 'libnativerender.so'; // 重写XComponentController，设置生命周期回调 class MyXComponentController extends XComponentController{ onSurfaceCreated(surfaceId: string): void { console.info(`onSurfaceCreated surfaceId: ${surfaceId}`); nativeRender.SetSurfaceId(BigInt(surfaceId)); } onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void { console.info(`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}}`); // 在onSurfaceChanged中调用ChangeSurface绘制内容 nativeRender.ChangeSurface(BigInt(surfaceId), rect.surfaceWidth, rect.surfaceHeight); } onSurfaceDestroyed(surfaceId: string): void { console.info(`onSurfaceDestroyed surfaceId: ${surfaceId}`); nativeRender.DestroySurface(BigInt(surfaceId)); } } @Entry @Component struct Index { @State currentStatus: string = 'index'; xComponentController: XComponentController = new MyXComponentController(); build() { Column() { // ··· // 在xxx.ets中定义XComponent Column({ space: 10 }) { XComponent({ type: XComponentType.SURFACE, controller: this.xComponentController }) Text(this.currentStatus) .fontSize('24fp') .fontWeight(500) } .onClick(() => { let surfaceId = this.xComponentController.getXComponentSurfaceId(); nativeRender.ChangeColor(BigInt(surfaceId)); let hasChangeColor: boolean = false; if (nativeRender.GetXComponentStatus(BigInt(surfaceId))) { hasChangeColor = nativeRender.GetXComponentStatus(BigInt(surfaceId)).hasChangeColor; } if (hasChangeColor) { this.currentStatus = "change color"; } }) // ··· } .width('100%') .height('100%') } }
通过ArkTS声明式UI描述来创建组件并结合OH_ArkUI_SurfaceHolders实现对Surface生命周期的管理。
import native from 'libnativerender.so'; // ... @Component export struct SurfaceHolderDeclarative { @State currentStatus: string = 'init'; private xcNode: FrameNode | null = null; build() { NavDestination() { // ... Column({ space: 10 }) { // 创建XComponent组件 XComponent({ type: XComponentType.SURFACE, }) .id('XComponentSurfaceHolder') .onAttach(() => { this.xcNode = this.getUIContext().getAttachedFrameNodeById('XComponentSurfaceHolder'); if (!this.xcNode) { return; } native.bindNode('XComponentSurfaceHolder', this.xcNode); // 跨语言调用至Native侧获取SurfaceHolder并绑定Surface生命周期回调 }) .onDetach(() => { native.unbindNode('XComponentSurfaceHolder'); this.xcNode = null; }) } // ... } } }
Native侧获取SurfaceHolder并绑定Surface生命周期回调的具体实现。
napi_value PluginManager::BindNode(napi_env env, napi_callback_info info) { size_t argc = 2; napi_value args[2] = {nullptr}; napi_get_cb_info(env, info, &argc, args, nullptr, nullptr); std::string nodeId = value2String(env, args[0]); ArkUI_NodeHandle handle; OH_ArkUI_GetNodeHandleFromNapiValue(env, args[1], &handle); // 获取nodeHandle OH_ArkUI_SurfaceHolder *holder = OH_ArkUI_SurfaceHolder_Create(handle); // 获取SurfaceHolder nodeHandleMap_[nodeId] = handle; surfaceHolderMap_[handle] = holder; auto callback = OH_ArkUI_SurfaceCallback_Create(); // 创建SurfaceCallback callbackMap_[holder] = callback; auto render = new EGLRender(); OH_ArkUI_SurfaceHolder_SetUserData(holder, render); // 将render保存在holder中 OH_ArkUI_SurfaceCallback_SetSurfaceCreatedEvent(callback, OnSurfaceCreatedNative); // 注册OnSurfaceCreated回调 OH_ArkUI_SurfaceCallback_SetSurfaceChangedEvent(callback, OnSurfaceChangedNative); // 注册OnSurfaceChanged回调 OH_ArkUI_SurfaceCallback_SetSurfaceDestroyedEvent(callback, OnSurfaceDestroyedNative); // 注册OnSurfaceDestroyed回调 OH_ArkUI_SurfaceHolder_AddSurfaceCallback(holder, callback); // 注册SurfaceCallback回调 // ... return nullptr; }
通过ArkTS自定义组件节点来创建组件并结合XComponentController实现对Surface生命周期的管理。
// 重写XComponentController，设置生命周期回调 class MyXComponentController extends XComponentController { onSurfaceCreated(surfaceId: string): void { console.info(`onSurfaceCreated surfaceId: ${surfaceId}`); } onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void { console.info(`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}}`); } onSurfaceDestroyed(surfaceId: string): void { console.info(`onSurfaceDestroyed surfaceId: ${surfaceId}`); } } class MyNodeController extends NodeController { public xComponent: typeNode.XComponent | undefined = undefined; public xComponentId: string = 'xcp' + (new Date().getTime()); public node: FrameNode | undefined = undefined; public column: typeNode.Column | undefined = undefined; private xcController: MyXComponentController = new MyXComponentController(); makeNode(uiContext: UIContext): FrameNode | null { this.node = new FrameNode(uiContext); this.column = typeNode.createNode(uiContext, 'Column') this.column.initialize() .width('100%') .height('100%') try { this.node.appendChild(this.column); } catch (error) { console.error('Fail to append child: ', error); } // 创建XComponent组件节点，并绑定XComponentController this.xComponent = typeNode.createNode(uiContext, 'XComponent', { type: XComponentType.SURFACE, controller: this.xcController }); this.xComponent.attribute try { this.column.appendChild(this.xComponent); } catch (error) { console.error('Fail to append child: ', error); } return this.node; } }
通过ArkTS自定义组件节点来创建组件并结合OH_ArkUI_SurfaceHolder实现对Surface生命周期的管理。
import native from 'libnativerender.so'; import { FrameNode, NodeController, typeNode, UIContext } from '@kit.ArkUI'; class MyNodeController extends NodeController { // ... makeNode(uiContext: UIContext): FrameNode | null { // ... // 创建XComponent组件节点 this.xComponent = typeNode.createNode(uiContext, 'XComponent', { type: XComponentType.SURFACE }); this.xComponent.attribute .id(this.xComponentId) .focusable(true) .focusOnTouch(true) native.bindNode(this.xComponentId, this.xComponent) // 跨语言调用至Native侧绑定Surface生命周期回调 // ... } // ... } // ... @Component export struct SurfaceHolderTypeNode { // ... myNodeController: MyNodeController = new MyNodeController(); build() { NavDestination() { Column() { // ... Column() { if (this.isShow) { NodeContainer(this.myNodeController) .width(200) .height(200) .focusable(true) .focusOnTouch(true) .defaultFocus(true) } }.height(200) // ... } .width('100%') } } }
Native侧绑定Surface生命周期回调的具体实现。

## OH_NativeXComponent向OH_ArkUI_SurfaceHolder的迁移
从API version 8开始，开发者可以通过基于OH_NativeXComponent实例相关的接口进行XComponent组件Surface的生命周期监听、获取NativeWindow实例以及监听基础事件，实现渲染绘制和响应交互功能。但使用OH_NativeXComponent相关的接口存在以下问题：
OH_NativeXComponent实例生命周期与XComponent组件强相关，开发者如果在XComponent组件销毁后仍然操作该对象将可能出现稳定性问题，造成应用的崩溃。
OH_NativeXComponent提供的交互事件接口不够丰富，只提供基础的触摸、鼠标、键盘交互接口，开发者若想识别长按、拖拽等高级手势需要自己写识别逻辑。
基于上述问题，建议使用OH_ArkUI_SurfaceHolder相关接口代替OH_NativeXComponent相关接口，以下以使用ArkTS声明式UI描述创建组件为例，介绍如何将使用OH_NativeXComponent管理Surface生命周期切换为使用OH_ArkUI_SurfaceHolder管理Surface生命周期。

## 组件创建
组件创建过程中的主要差异在于使用OH_NativeXComponent需要传入id和libraryname属性以支持在Native侧获取对应的OH_NativeXComponent实例；而使用OH_ArkUI_SurfaceHolder管理Surface生命周期的XComponent不再需要在XComponent的构造参数中传入id和libraryname属性，而是直接将组件对应的FrameNode节点传递至Native侧进行生命周期绑定和其他设置。
OH_NativeXComponent
XComponent({ id: 'xcomponentId', type: XComponentType.SURFACE, libraryname: 'nativerender' // 利用id和libraryname属性在Native侧获取NativeXcomponent并绑定Surface生命周期 }) .onLoad((xComponentContext) => { this.xComponentContext = xComponentContext as XComponentContext; this.currentStatus = 'index'; }) .onDestroy(() => { console.info('onDestroy'); }) .id('xcomponent')
OH_ArkUI_SurfaceHolder
XComponent({ type: XComponentType.SURFACE, }) .id('XComponentSurfaceHolder') .onAttach(() => { this.xcNode = this.getUIContext().getAttachedFrameNodeById('XComponentSurfaceHolder'); if (!this.xcNode) { return; } native.bindNode('XComponentSurfaceHolder', this.xcNode); // 跨语言调用至Native侧获取SurfaceHolder并绑定Surface生命周期回调 this.currentStatus = 'index'; }) .onDetach(() => { native.unbindNode('XComponentSurfaceHolder'); this.xcNode = null; })

## 绑定Surface生命周期
绑定Surface生命周期中的主要差异在于注册生命周期回调的接口不同，具体回调内执行的逻辑基本保持不变。
OH_NativeXComponent
void PluginManager::Export(napi_env env, napi_value exports) { if ((env == nullptr) || (exports == nullptr)) { OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "PluginManager", "Export: env or exports is null"); return; } napi_value exportInstance = nullptr; // 利用OH_NATIVE_XCOMPONENT_OBJ字段获取NativeXComponent实例 if (napi_get_named_property(env, exports, OH_NATIVE_XCOMPONENT_OBJ, &exportInstance) != napi_ok) { OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "PluginManager", "Export: napi_get_named_property fail"); return; } OH_NativeXComponent *nativeXComponent = nullptr; if (napi_unwrap(env, exportInstance, reinterpret_cast<void **>(&nativeXComponent)) != napi_ok) { OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "PluginManager", "Export: napi_unwrap fail"); return; } char idStr[OH_XCOMPONENT_ID_LEN_MAX + 1] = {'\0'}; uint64_t idSize = OH_XCOMPONENT_ID_LEN_MAX + 1; // 从NativeXComponent实例中获取id属性用来和ArkTS侧的XComponent组件一一对应 if (OH_NativeXComponent_GetXComponentId(nativeXComponent, idStr, &idSize) != OH_NATIVEXCOMPONENT_RESULT_SUCCESS) { OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "PluginManager", "Export: OH_NativeXComponent_GetXComponentId fail"); return; } std::string id(idStr); auto context = PluginManager::GetInstance(); if ((context != nullptr) && (nativeXComponent != nullptr)) { context->SetNativeXComponent(id, nativeXComponent); auto render = context->GetRender(id); if (render != nullptr) { // 注册Surface生命周期 render->RegisterCallback(nativeXComponent); render->Export(env, exports); } } }
注册Surface生命周期。
void PluginRender::RegisterCallback(OH_NativeXComponent* nativeXComponent) { renderCallback_.OnSurfaceCreated = OnSurfaceCreatedCB; renderCallback_.OnSurfaceChanged = OnSurfaceChangedCB; renderCallback_.OnSurfaceDestroyed = OnSurfaceDestroyedCB; // ... OH_NativeXComponent_RegisterCallback(nativeXComponent, &renderCallback_); // ... }
OH_ArkUI_SurfaceHolder
napi_value PluginManager::BindNode(napi_env env, napi_callback_info info) { size_t argc = 2; napi_value args[2] = {nullptr}; napi_get_cb_info(env, info, &argc, args, nullptr, nullptr); std::string nodeId = value2String(env, args[0]); ArkUI_NodeHandle handle; OH_ArkUI_GetNodeHandleFromNapiValue(env, args[1], &handle); // 获取nodeHandle OH_ArkUI_SurfaceHolder *holder = OH_ArkUI_SurfaceHolder_Create(handle); // 获取SurfaceHolder nodeHandleMap_[nodeId] = handle; surfaceHolderMap_[handle] = holder; auto callback = OH_ArkUI_SurfaceCallback_Create(); // 创建SurfaceCallback callbackMap_[holder] = callback; auto render = new EGLRender(); OH_ArkUI_SurfaceHolder_SetUserData(holder, render); // 将render保存在holder中 OH_ArkUI_SurfaceCallback_SetSurfaceCreatedEvent(callback, OnSurfaceCreatedNative); // 注册OnSurfaceCreated回调 OH_ArkUI_SurfaceCallback_SetSurfaceChangedEvent(callback, OnSurfaceChangedNative); // 注册OnSurfaceChanged回调 OH_ArkUI_SurfaceCallback_SetSurfaceDestroyedEvent(callback, OnSurfaceDestroyedNative); // 注册OnSurfaceDestroyed回调 OH_ArkUI_SurfaceHolder_AddSurfaceCallback(holder, callback); // 注册SurfaceCallback回调 // ... return nullptr; }

## 获取NativeWindow方式
获取NativeWindow方式的差异如下：
OH_NativeXComponent
在OnSurfaceCreated等生命周期回调返回的参数(即下面的void *window)中获取。
void OnSurfaceCreatedCB(OH_NativeXComponent *component, void *window) { // ... } void OnSurfaceChangedCB(OH_NativeXComponent *component, void *window) { // ... } void OnSurfaceDestroyedCB(OH_NativeXComponent *component, void *window) { // ... } void DispatchTouchEventCB(OH_NativeXComponent *component, void *window) { // ... }
OH_ArkUI_SurfaceHolder
调用OH_ArkUI_XComponent_GetNativeWindow接口从OH_ArkUI_SurfaceHolder中获取。
void OnSurfaceCreatedNative(OH_ArkUI_SurfaceHolder *holder) { auto window = OH_ArkUI_XComponent_GetNativeWindow(holder); // 获取native window // ... }

## 监听交互事件
使用OH_NativeXComponent方式进行交互事件的监听，只能使用OH_NativeXComponent上相关的接口监听触摸、鼠标、按键等基础事件。而使用OH_ArkUI_SurfaceHolder相关的接口，除监听基础事件外还能监听长按、拖拽等高级手势。
OH_NativeXComponent
renderCallback_.DispatchTouchEvent = DispatchTouchEventCB; // 注册触摸事件 OH_NativeXComponent_RegisterCallback(nativeXComponent, &renderCallback_); mouseCallback_.DispatchMouseEvent = DispatchMouseEventCB; mouseCallback_.DispatchHoverEvent = DispatchHoverEventCB; OH_NativeXComponent_RegisterMouseEventCallback(nativeXComponent, &mouseCallback_); // 注册鼠标事件 OH_NativeXComponent_RegisterFocusEventCallback(nativeXComponent, OnFocusEventCB); // 注册获焦事件 OH_NativeXComponent_RegisterKeyEventCallback(nativeXComponent, OnKeyEventCB); // 注册按键事件 OH_NativeXComponent_RegisterBlurEventCallback(nativeXComponent, OnBlurEventCB); // 注册失焦事件
OH_ArkUI_SurfaceHolder
以下只以注册touch事件为例，鼠标、按键以及更多的手势请参考监听组件事件。
if (!nodeAPI->addNodeEventReceiver(handle, onEvent)) { // 添加事件监听，返回成功码 0 OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "onBind", "addNodeEventReceiver error"); } if (!nodeAPI->registerNodeEvent(handle, NODE_TOUCH_EVENT, 0, nullptr)) { // 用C接口注册touch事件，返回成功码 0 OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "onBind", "registerTouchEvent error"); }
