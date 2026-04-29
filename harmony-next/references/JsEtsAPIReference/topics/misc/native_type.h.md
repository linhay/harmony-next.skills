# native_type.h

**概述**

提供NativeModule公共的类型定义。

引用文件： <arkui/native_type.h>

库： libace_ndk.z.so

系统能力： SystemCapability.ArkUI.ArkUI.Full

起始版本： 12

相关模块： [ArkUI_NativeModule](ArkUI_NativeModule.md)

相关示例： [NativeTypeSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeTypeSample)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_Node | ArkUI_Node | 定义ArkUI native组件实例对象。 |
| ArkUI_ContextCallback | ArkUI_ContextCallback | 事件回调类型。 |
| ArkUI_NumberValue | ArkUI_NumberValue | ArkUI在Native侧的数字类型定义。 |
| ARKUI_TextPickerRangeContent | ARKUI_TextPickerRangeContent | 定义单列滑动数据选择器支持的图片资源结构体。 |
| ARKUI_TextPickerCascadeRangeContent | ARKUI_TextPickerCascadeRangeContent | 定义多列联动滑动数据选择器的结构体。 |
| ArkUI_ColorStop | ArkUI_ColorStop | 定义渐变色结构。 |
| ArkUI_Rect | ArkUI_Rect | 定义遮罩屏蔽区域的范围结构体。 |
| ArkUI_IntSize | ArkUI_IntSize | 尺寸类型，用于描述组件的宽高。 |
| ArkUI_IntOffset | ArkUI_IntOffset | 位置，用于描述组件的位置。 |
| ArkUI_Margin | ArkUI_Margin | 外边距属性，用于描述组件的外边距属性。 |
| ArkUI_TranslationOptions | ArkUI_TranslationOptions | 定义组件转场时的平移效果对象。 |
| ArkUI_ScaleOptions | ArkUI_ScaleOptions | 定义组件转场时的缩放效果对象。 |
| ArkUI_RotationOptions | ArkUI_RotationOptions | 定义组件转场时的旋转效果对象。 |
| ArkUI_NativeDialog | ArkUI_NativeDialog | 提供ArkUI在Native侧的自定义弹窗控制器对象定义。 |
| ArkUI_LayoutConstraint | ArkUI_LayoutConstraint | 布局约束，组件布局时，进行尺寸范围限制。 |
| ArkUI_DrawContext | ArkUI_DrawContext | 定义组件绘制上下文类型结构。 |
| ArkUI_Node* | ArkUI_NodeHandle | 定义ArkUI native组件实例对象指针定义。 |
| ArkUI_NativeDialog* | ArkUI_NativeDialogHandle | 定义ArkUI在Native侧的自定义弹窗控制器对象指针。 |
| ArkUI_GridItemSize | ArkUI_GridItemSize | 定义Grid布局选项onGetIrregularSizeByIndex回调返回值结构体。 |
| ArkUI_GridItemRect | ArkUI_GridItemRect | 定义Grid布局选项onGetRectByIndex回调返回值结构体。 |
| ArkUI_GridLayoutOptions | ArkUI_GridLayoutOptions | 定义Grid布局选项。 |
| ArkUI_WaterFlowSectionOption | ArkUI_WaterFlowSectionOption | 定义FlowItem分组配置信息。 |
| ArkUI_ListItemSwipeActionItem | ArkUI_ListItemSwipeActionItem | 定义ListItemSwipeActionOption方法内Item的配置信息。 |
| ArkUI_ListItemSwipeActionOption | ArkUI_ListItemSwipeActionOption | 定义ListItemSwipeActionOption方法的配置信息。 |
| ArkUI_Context | ArkUI_Context | 定义ArkUI native UI的上下文实例对象。 |
| ArkUI_Context* | ArkUI_ContextHandle | 定义ArkUI native UI的上下文实例对象指针定义。 |
| ArkUI_NodeContent* | ArkUI_NodeContentHandle | 定义ArkUI NodeContent实例在Native侧的实例对象指针定义。 |
| ArkUI_AlignmentRuleOption | ArkUI_AlignmentRuleOption | 指定设置在相对容器中子组件的对齐规则。 |
| ArkUI_GuidelineOption | ArkUI_GuidelineOption | guideLine参数，用于定义guideline的id、方向和位置。 |
| ArkUI_BarrierOption | ArkUI_BarrierOption | barrier参数，用于定义barrier的id、方向和生成时所依赖的组件。 |
| ArkUI_ImageAnimatorFrameInfo | ArkUI_ImageAnimatorFrameInfo | 定义图片帧信息。 |
| ArkUI_ListChildrenMainSize | ArkUI_ListChildrenMainSize | 定义List的ChildrenMainSize类信息。 |
| ArkUI_ProgressLinearStyleOption | ArkUI_ProgressLinearStyleOption | 定义线性进度条样式。 |
| ArkUI_CustomProperty | ArkUI_CustomProperty | 定义自定义属性的CustomProperty类信息。 |
| ArkUI_HostWindowInfo | ArkUI_HostWindowInfo | 定义窗口属性的HostWindowInfo类信息。 |
| ArkUI_ActiveChildrenInfo | ArkUI_ActiveChildrenInfo | 定义ActiveChildrenInfo类信息。 |
| ArkUI_CrossLanguageOption | ArkUI_CrossLanguageOption | 定义跨语言配置项。 |
| AbilityBase_Want | AbilityBase_Want | 声明元能力want结构。 |
| ArkUI_EmbeddedComponentOption | ArkUI_EmbeddedComponentOption | 为EmbeddedComponent定义参数EmbeddedComponentOption。 |
| ArkUI_AccessibilityState | ArkUI_AccessibilityState | 定义组件无障碍状态。 |
| ArkUI_AccessibilityValue | ArkUI_AccessibilityValue | 定义组件无障碍信息值。 |
| ArkUI_SystemFontStyleEvent | ArkUI_SystemFontStyleEvent | 系统字体变更事件定义。 |
| ArkUI_CustomSpanMeasureInfo | ArkUI_CustomSpanMeasureInfo | 自定义段落组件的测量信息。 |
| ArkUI_CustomSpanMetrics | ArkUI_CustomSpanMetrics | 自定义段落组件的度量指标。 |
| ArkUI_CustomSpanDrawInfo | ArkUI_CustomSpanDrawInfo | 自定义段落组件的绘制信息。 |
| ArkUI_SwiperIndicator | ArkUI_SwiperIndicator | 定义Swiper组件的导航指示器风格。 |
| ArkUI_SwiperDigitIndicator | ArkUI_SwiperDigitIndicator | 定义Swiper组件的数字导航指示器风格。 |
| ArkUI_SwiperArrowStyle | ArkUI_SwiperArrowStyle | 定义Swiper组件的导航箭头风格。 |
| ArkUI_StyledString_Descriptor | ArkUI_StyledString_Descriptor | 定义文本组件支持的属性字符串的数据对象。 |
| ArkUI_SnapshotOptions | ArkUI_SnapshotOptions | 定义截图的可选项。 |
| ArkUI_TextPickerRangeContentArray | ArkUI_TextPickerRangeContentArray | 定义文本选择器的数据选择列表。 |
| ArkUI_TextCascadePickerRangeContentArray | ArkUI_TextCascadePickerRangeContentArray | 定义多列联动数据选择器的多列联动数据选择列表。 |
| ArkUI_SelectionOptions | ArkUI_SelectionOptions | 定义选择操作的相关选项。 |
| ArkUI_VisibleAreaEventOptions | ArkUI_VisibleAreaEventOptions | 可见区域变化监听的参数。 |
| ArkUI_PositionEdges | ArkUI_PositionEdges | 相对容器内容区边界的位置参数。 |
| ArkUI_PixelRoundPolicy | ArkUI_PixelRoundPolicy | 定义组件的像素取整策略结构体。 |
| ArkUI_ContentTransitionEffect | ArkUI_ContentTransitionEffect | 内容过渡效果。 |
| ArkUI_ShowCounterConfig | ArkUI_ShowCounterConfig | 定义文本输入框的计数器配置。 |
| ArkUI_TextContentBaseController | ArkUI_TextContentBaseController | 定义文本内容基础控制器。 |
| ArkUI_TextMenuItem | ArkUI_TextMenuItem | 定义文本菜单项结构体。 |
| ArkUI_TextMenuItemArray | ArkUI_TextMenuItemArray | 定义文本菜单项数组结构体。 |
| ArkUI_TextEditMenuOptions | ArkUI_TextEditMenuOptions | 定义文本菜单扩展项结构体。 |
| ArkUI_TextSelectionMenuOptions | ArkUI_TextSelectionMenuOptions | 定义自定义文本选择菜单结构体。 |
| ArkUI_SelectedDragPreviewStyle | ArkUI_SelectedDragPreviewStyle | 定义选中状态下文本拖拽预览样式。 |
| ArkUI_MotionPathOptions | ArkUI_MotionPathOptions | 定义路径动画的运动路径配置项。 |
| ArkUI_PickerIndicatorBackground | ArkUI_PickerIndicatorBackground | 背景样式指示器的样式参数。 |
| ArkUI_PickerIndicatorDivider | ArkUI_PickerIndicatorDivider | 分割线样式指示器的样式参数。 |
| ArkUI_PickerIndicatorStyle | ArkUI_PickerIndicatorStyle | 选中项指示器的样式。 |
| ArkUI_TextMarqueeOptions | ArkUI_TextMarqueeOptions | 定义文本跑马灯模式配置项。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_Alignment | ArkUI_Alignment | 定义布局对齐枚举值。 |
| ArkUI_ImageRepeat | ArkUI_ImageRepeat | 定义图片重复铺设枚举值。 |
| ArkUI_FontStyle | ArkUI_FontStyle | 定义字体样式枚举值。 |
| ArkUI_FontWeight | ArkUI_FontWeight | 定义字体粗细/字重枚举值。 |
| ArkUI_TextAlignment | ArkUI_TextAlignment | 定义字体水平对齐样式枚举值。 |
| ArkUI_TextVerticalAlignment | ArkUI_TextVerticalAlignment | 定义文本垂直对齐样式枚举值。 |
| ArkUI_EnterKeyType | ArkUI_EnterKeyType | 定义单行文本输入法回车键类型枚举值。 |
| ArkUI_TextInputType | ArkUI_TextInputType | 定义单行文本输入法类型枚举值。 |
| ArkUI_TextAreaType | ArkUI_TextAreaType | 定义多行文本输入法类型枚举值。 |
| ArkUI_CancelButtonStyle | ArkUI_CancelButtonStyle | 定义清除按钮样式枚举值。 |
| ArkUI_XComponentType | ArkUI_XComponentType | 定义XComponent类型枚举值。 |
| ArkUI_ProgressType | ArkUI_ProgressType | 定义进度条类型枚举值。 |
| ArkUI_TextDecorationType | ArkUI_TextDecorationType | 定义装饰线类型枚举值。 |
| ArkUI_TextDecorationStyle | ArkUI_TextDecorationStyle | 定义装饰线样式枚举值。 |
| ArkUI_TextCase | ArkUI_TextCase | 定义文本大小写枚举值。 |
| ArkUI_CopyOptions | ArkUI_CopyOptions | 定义文本复制粘贴模式枚举值。 |
| ArkUI_ShadowType | ArkUI_ShadowType | 定义阴影类型枚举值。 |
| ArkUI_DatePickerMode | ArkUI_DatePickerMode | 定义日期选择器列显示模式的枚举值。 |
| ArkUI_TextPickerRangeType | ArkUI_TextPickerRangeType | 定义滑动选择文本选择器输入类型。 |
| ArkUI_AccessibilityCheckedState | ArkUI_AccessibilityCheckedState | 定义无障碍复选框状态类型枚举值。 |
| ArkUI_AccessibilityActionType | ArkUI_AccessibilityActionType | 定义无障碍操作类型。 |
| ArkUI_EdgeEffect | ArkUI_EdgeEffect | 定义边缘滑动效果枚举值。 |
| ArkUI_BarState | ArkUI_BarState | 定义文本控制滚动条状态枚举值。 |
| ArkUI_EffectEdge | ArkUI_EffectEdge | 定义边缘效果生效边缘的方向枚举值。 |
| ArkUI_ScrollDirection | ArkUI_ScrollDirection | 定义Scroll组件排列方向枚举值。 |
| ArkUI_ScrollSnapAlign | ArkUI_ScrollSnapAlign | 定义列表项滚动结束对齐效果枚举值。 |
| ArkUI_ScrollBarDisplayMode | ArkUI_ScrollBarDisplayMode | 定义滚动条状态枚举值。 |
| ArkUI_Axis | ArkUI_Axis | 定义滚动方向和List组件排列方向枚举值。 |
| ArkUI_StickyStyle | ArkUI_StickyStyle | 定义列表是否吸顶和吸底枚举值。 |
| ArkUI_ContentClipMode | ArkUI_ContentClipMode | 定义滚动容器的内容层裁剪区域枚举值。 |
| ArkUI_WaterFlowLayoutMode | ArkUI_WaterFlowLayoutMode | 定义WaterFlow组件布局模式枚举值。 |
| ArkUI_BorderStyle | ArkUI_BorderStyle | 边框线条样式枚举值。 |
| ArkUI_HitTestMode | ArkUI_HitTestMode | 触摸测试控制枚举值。 |
| ArkUI_ShadowStyle | ArkUI_ShadowStyle | 阴影效果枚举值。 |
| ArkUI_AnimationCurve | ArkUI_AnimationCurve | 动画曲线枚举值。 |
| ArkUI_SwiperArrow | ArkUI_SwiperArrow | Swiper导航点箭头枚举值。 |
| ArkUI_SwiperNestedScrollMode | ArkUI_SwiperNestedScrollMode | Swiper组件和父组件的嵌套滚动模式。 |
| ArkUI_PageFlipMode | ArkUI_PageFlipMode | Swiper组件鼠标滚轮翻页模式。 |
| ArkUI_SwiperAnimationMode | ArkUI_SwiperAnimationMode | Swiper组件跳转到目标index的动画模式。 |
| ArkUI_AccessibilityMode | ArkUI_AccessibilityMode | 定义无障碍辅助服务模式。 |
| ArkUI_TextCopyOptions | ArkUI_TextCopyOptions | 定义组件支持设置文本是否可复制粘贴。 |
| ArkUI_TextHeightAdaptivePolicy | ArkUI_TextHeightAdaptivePolicy | 定义文本自适应高度的方式。 |
| ArkUI_ScrollNestedMode | ArkUI_ScrollNestedMode | 定义嵌套滚动选项。 |
| ArkUI_ScrollEdge | ArkUI_ScrollEdge | 定义滚动到的边缘位置。 |
| ArkUI_ScrollAlignment | ArkUI_ScrollAlignment | 滚动到具体item时的对齐方式。 |
| ArkUI_ScrollState | ArkUI_ScrollState | 定义当前滚动状态。 |
| ArkUI_SliderBlockStyle | ArkUI_SliderBlockStyle | 定义滑块形状。 |
| ArkUI_SliderDirection | ArkUI_SliderDirection | 定义滑动条滑动方向。 |
| ArkUI_SliderStyle | ArkUI_SliderStyle | 定义滑块与滑轨显示样式。 |
| ArkUI_CheckboxShape | ArkUI_CheckboxShape | 定义CheckBox组件形状。 |
| ArkUI_AnimationPlayMode | ArkUI_AnimationPlayMode | 定义动画播放模式。 |
| ArkUI_ImageSize | ArkUI_ImageSize | 定义图片宽高样式。 |
| ArkUI_AdaptiveColor | ArkUI_AdaptiveColor | 定义取色模式。 |
| ArkUI_ColorMode | ArkUI_ColorMode | 定义深浅色模式。 |
| ArkUI_SystemColorMode | ArkUI_SystemColorMode | 定义系统深浅色模式。 |
| ArkUI_BlurStyle | ArkUI_BlurStyle | 定义背景模糊样式。 |
| ArkUI_BlurStyleActivePolicy | ArkUI_BlurStyleActivePolicy | 定义背景模糊激活策略。 |
| ArkUI_VerticalAlignment | ArkUI_VerticalAlignment | 定义垂直对齐方式。 |
| ArkUI_HorizontalAlignment | ArkUI_HorizontalAlignment | 定义语言方向对齐方式。 |
| ArkUI_TextOverflow | ArkUI_TextOverflow | 定义文本超长时的显示方式。 |
| ArkUI_ImageSpanAlignment | ArkUI_ImageSpanAlignment | 定义图片基于文本的对齐方式。 |
| ArkUI_ObjectFit | ArkUI_ObjectFit | 定义image填充效果。ImageSpanAlignment |
| ArkUI_ImageInterpolation | ArkUI_ImageInterpolation | 定义图片插值效果。 |
| ArkUI_DynamicRangeMode | ArkUI_DynamicRangeMode | 定义图像动态范围模式（例如：SDR/HDR），用于控制图像的明暗与色彩显示范围。 |
| ArkUI_ImageRotateOrientation | ArkUI_ImageRotateOrientation | 定义图像旋转方向。 |
| ArkUI_BlendMode | ArkUI_BlendMode | 混合模式枚举值。 |
| ArkUI_Direction | ArkUI_Direction | 设置容器元素内主轴方向上的布局枚举值。 |
| ArkUI_ItemAlignment | ArkUI_ItemAlignment | 设置子组件在父容器交叉轴的对齐格式枚举值。 |
| ArkUI_ColorStrategy | ArkUI_ColorStrategy | 前景色枚举值。 |
| ArkUI_FlexAlignment | ArkUI_FlexAlignment | 定义垂直方向对齐方式。 |
| ArkUI_FlexDirection | ArkUI_FlexDirection | 定义Flex容器的主轴方向。 |
| ArkUI_FlexWrap | ArkUI_FlexWrap | 定义Flex行列布局模式模式。 |
| ArkUI_Visibility | ArkUI_Visibility | 控制组件的显隐枚举值。 |
| ArkUI_CalendarAlignment | ArkUI_CalendarAlignment | 日历选择器与入口组件对齐方式。 |
| ArkUI_MaskType | ArkUI_MaskType | 遮罩类型枚举。 |
| ArkUI_ClipType | ArkUI_ClipType | 裁剪类型枚举。 |
| ArkUI_ShapeType | ArkUI_ShapeType | 自定义形状。 |
| ArkUI_LinearGradientDirection | ArkUI_LinearGradientDirection | 定义渐变方向结构。 |
| ArkUI_WordBreak | ArkUI_WordBreak | 定义文本断行规则。 |
| ArkUI_EllipsisMode | ArkUI_EllipsisMode | 定义文本省略位置。 |
| ArkUI_ImageRenderMode | ArkUI_ImageRenderMode | 定义图片渲染模式。 |
| ArkUI_TransitionEdge | ArkUI_TransitionEdge | 定义转场从边缘滑入和滑出的效果。 |
| ArkUI_FinishCallbackType | ArkUI_FinishCallbackType | 在动画中定义onFinish回调的类型。 |
| ArkUI_ListItemAlignment | ArkUI_ListItemAlignment | 交叉轴方向的布局方式。 |
| ArkUI_BlendApplyType | ArkUI_BlendApplyType | 指定的混合模式应用于视图的内容选项. |
| ArkUI_LengthMetricUnit | ArkUI_LengthMetricUnit | 定义组件的单位模式。 |
| ArkUI_TextInputContentType | ArkUI_TextInputContentType | 定义自动填充类型。 |
| ArkUI_BarrierDirection | ArkUI_BarrierDirection | 定义屏障线的方向。 |
| ArkUI_RelativeLayoutChainStyle | ArkUI_RelativeLayoutChainStyle | 定义链的风格。 |
| ArkUI_TextInputStyle | ArkUI_TextInputStyle | 定义输入框风格。 |
| ArkUI_KeyboardAppearance | ArkUI_KeyboardAppearance | 定义输入框拉起的键盘样式。 |
| ArkUI_TextDataDetectorType | ArkUI_TextDataDetectorType | 定义文本识别的实体类型。 |
| ArkUI_ButtonType | ArkUI_ButtonType | 定义按钮样式枚举值。 |
| ArkUI_RenderFit | ArkUI_RenderFit | 定义动画终态内容大小与位置的枚举值。 |
| ArkUI_SwiperIndicatorType | ArkUI_SwiperIndicatorType | 定义Swiper组件的导航指示器类型。 |
| ArkUI_AnimationDirection | ArkUI_AnimationDirection | 动画播放模式。 |
| ArkUI_ListItemSwipeActionState | ArkUI_ListItemSwipeActionState | 定义Listitem组件SwipeAction方法的显隐模式。 |
| ArkUI_ListItemSwipeEdgeEffect | ArkUI_ListItemSwipeEdgeEffect | 定义Listitem组件SwipeAction方法的滚动模式。 |
| ArkUI_ListItemSwipeActionDirection | ArkUI_ListItemSwipeActionDirection | ListItem划出菜单的展开方向。 |
| ArkUI_AnimationStatus | ArkUI_AnimationStatus | 定义帧动画的播放状态。 |
| ArkUI_AnimationFillMode | ArkUI_AnimationFillMode | 定义帧动画组件在动画开始前和结束后的状态。 |
| ArkUI_ErrorCode | ArkUI_ErrorCode | 定义错误码枚举值。 |
| ArkUI_ScrollSource | ArkUI_ScrollSource | 定义滚动来源枚举值。 |
| ArkUI_SafeAreaType | ArkUI_SafeAreaType | 定义扩展安全区域的枚举值。 |
| ArkUI_SafeAreaEdge | ArkUI_SafeAreaEdge | 定义扩展安全区域的方向的枚举值。 |
| ArkUI_FocusMove | ArkUI_FocusMove | 定义焦点移动方向的枚举值。 |
| ArkUI_ListItemGroupArea | ArkUI_ListItemGroupArea | 定义ListItemGroup组件区域。 |
| ArkUI_KeyboardAvoidMode | ArkUI_KeyboardAvoidMode | 键盘避让模式。 |
| ArkUI_HoverModeAreaType | ArkUI_HoverModeAreaType | 悬停态显示区域。 |
| ArkUI_ExpandMode | ArkUI_ExpandMode | 定义子节点展开模式枚举值。 |
| ArkUI_NavDestinationState | ArkUI_NavDestinationState | 定义NavDestination组件的状态。 |
| ArkUI_RouterPageState | ArkUI_RouterPageState | 定义Router Page的状态。 |
| ArkUI_UIState | ArkUI_UIState | 组件的UI状态枚举，用于处理状态样式。 |
| ArkUI_FocusWrapMode | ArkUI_FocusWrapMode | 组件走焦换行规则。 |
| ArkUI_ItemFillPolicy | ArkUI_ItemFillPolicy | 为不同响应式断点规格指定列数。 |
| ArkUI_EdgeDirection | ArkUI_EdgeDirection | 定义矩形边方向。 |
| ArkUI_CornerDirection | ArkUI_CornerDirection | 定义角度方向。 |
| ArkUI_LayoutPolicy | ArkUI_LayoutPolicy | 布局策略枚举。 |
| ArkUI_PixelRoundCalcPolicy | ArkUI_PixelRoundCalcPolicy | 定义像素取整计算策略枚举。 |
| ArkUI_GridItemStyle | ArkUI_GridItemStyle | GridItem样式枚举。 |
| ArkUI_MenuPolicy | ArkUI_MenuPolicy | 菜单弹出策略。 |
| ArkUI_ResponseRegionSupportedTool | ArkUI_ResponseRegionSupportedTool | 定义支持响应区域设置的事件工具类型。 |
| ArkUI_TextMenuItemId | ArkUI_TextMenuItemId | 文本菜单项id枚举。 |
| ArkUI_TextSpanType | ArkUI_TextSpanType | 自定义文本选择菜单的文本识别类型枚举。 |
| ArkUI_TextResponseType | ArkUI_TextResponseType | 自定义文本选择菜单的响应类型枚举。 |
| ArkUI_HoverEffect | ArkUI_HoverEffect | 组件被悬停时的效果。 |
| ArkUI_FocusPriority | ArkUI_FocusPriority | 应用程序内焦点管理的优先级级别。确定UI组件在交互期间接收焦点的顺序。 |
| ArkUI_LayoutSafeAreaType | ArkUI_LayoutSafeAreaType | 定义扩展安全区域的枚举值。 |
| ArkUI_LayoutSafeAreaEdge | ArkUI_LayoutSafeAreaEdge | 定义扩展安全区域的方向的枚举值。 |
| ArkUI_LocalizedAlignment | ArkUI_LocalizedAlignment | 定义Stack容器中子组件的对齐规则。 |
| ArkUI_RenderStrategy | ArkUI_RenderStrategy | 定义组件绘制圆角的模式。 |
| ArkUI_MarqueeStartPolicy | ArkUI_MarqueeStartPolicy | 定义跑马灯启动策略枚举。 |
| ArkUI_MarqueeUpdatePolicy | ArkUI_MarqueeUpdatePolicy | 定义跑马灯更新策略枚举。 |
| ArkUI_PickerIndicatorType | ArkUI_PickerIndicatorType | 选择器的选中指示器类型。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_LayoutConstraint* OH_ArkUI_LayoutConstraint_Create() | - | 创建布局约束。 |
| ArkUI_LayoutConstraint* OH_ArkUI_LayoutConstraint_Copy(const ArkUI_LayoutConstraint* Constraint) | - | 布局约束深拷贝。 |
| void* OH_ArkUI_LayoutConstraint_Dispose(ArkUI_LayoutConstraint* Constraint) | - | 销毁布局约束指针。 |
| int32_t OH_ArkUI_LayoutConstraint_GetMaxWidth(const ArkUI_LayoutConstraint* Constraint) | - | 通过布局约束获取最大宽度，单位为px。 |
| int32_t OH_ArkUI_LayoutConstraint_GetMinWidth(const ArkUI_LayoutConstraint* Constraint) | - | 通过布局约束获取最小宽度，单位为px。 |
| int32_t OH_ArkUI_LayoutConstraint_GetMaxHeight(const ArkUI_LayoutConstraint* Constraint) | - | 通过布局约束获取最大高度，单位为px。 |
| int32_t OH_ArkUI_LayoutConstraint_GetMinHeight(const ArkUI_LayoutConstraint* Constraint) | - | 通过布局约束获取最小高度，单位为px。 |
| int32_t OH_ArkUI_LayoutConstraint_GetPercentReferenceWidth(const ArkUI_LayoutConstraint* Constraint) | - | 通过布局约束获取宽度百分比基准。 |
| int32_t OH_ArkUI_LayoutConstraint_GetPercentReferenceHeight(const ArkUI_LayoutConstraint* Constraint) | - | 通过布局约束获取高度百分比基准。 |
| void OH_ArkUI_LayoutConstraint_SetMaxWidth(ArkUI_LayoutConstraint* Constraint, int32_t value) | - | 设置最大宽度。 |
| void OH_ArkUI_LayoutConstraint_SetMinWidth(ArkUI_LayoutConstraint* Constraint, int32_t value) | - | 设置最小宽度。 |
| void OH_ArkUI_LayoutConstraint_SetMaxHeight(ArkUI_LayoutConstraint* Constraint, int32_t value) | - | 设置最大高度。 |
| void OH_ArkUI_LayoutConstraint_SetMinHeight(ArkUI_LayoutConstraint* Constraint, int32_t value) | - | 设置最小高度。 |
| void OH_ArkUI_LayoutConstraint_SetPercentReferenceWidth(ArkUI_LayoutConstraint* Constraint, int32_t value) | - | 设置宽度百分比基准。 |
| void OH_ArkUI_LayoutConstraint_SetPercentReferenceHeight(ArkUI_LayoutConstraint* Constraint, int32_t value) | - | 设置高度百分比基准。 |
| void* OH_ArkUI_DrawContext_GetCanvas(ArkUI_DrawContext* context) | - | 获取绘制canvas指针，可以转换为图形库的OH_Drawing_Canvas指针进行绘制。 |
| ArkUI_IntSize OH_ArkUI_DrawContext_GetSize(ArkUI_DrawContext* context) | - | 获取可绘制区域大小。 |
| ArkUI_WaterFlowSectionOption* OH_ArkUI_WaterFlowSectionOption_Create() | - | 创建FlowItem分组配置信息。 |
| void OH_ArkUI_WaterFlowSectionOption_Dispose(ArkUI_WaterFlowSectionOption* option) | - | 销毁FlowItem分组配置信息指针。 |
| void OH_ArkUI_WaterFlowSectionOption_SetSize(ArkUI_WaterFlowSectionOption* option, int32_t size) | - | 设置FlowItem分组配置信息数组长度。 |
| int32_t OH_ArkUI_WaterFlowSectionOption_GetSize(ArkUI_WaterFlowSectionOption* option) | - | 获取FlowItem分组配置信息数组长度。 |
| void OH_ArkUI_WaterFlowSectionOption_SetItemCount(ArkUI_WaterFlowSectionOption* option, int32_t index, int32_t itemCount) | - | 设置分组中FlowItem数量。 |
| int32_t OH_ArkUI_WaterFlowSectionOption_GetItemCount(ArkUI_WaterFlowSectionOption* option, int32_t index) | - | 通过FlowItem分组配置信息获取对应索引下的FlowItem数量。 |
| void OH_ArkUI_WaterFlowSectionOption_SetCrossCount(ArkUI_WaterFlowSectionOption* option, int32_t index, int32_t crossCount) | - | 设置布局栅格，纵向布局时为列数，横向布局时为行数。 |
| int32_t OH_ArkUI_WaterFlowSectionOption_GetCrossCount(ArkUI_WaterFlowSectionOption* option, int32_t index) | - | 通过FlowItem分组配置信息获取对应索引下的布局栅格数。 |
| void OH_ArkUI_WaterFlowSectionOption_SetColumnGap(ArkUI_WaterFlowSectionOption* option, int32_t index, float columnGap) | - | 设置分组的列间距。 |
| float OH_ArkUI_WaterFlowSectionOption_GetColumnGap(ArkUI_WaterFlowSectionOption* option, int32_t index) | - | 通过FlowItem分组配置信息获取对应索引下的分组的列间距。 |
| void OH_ArkUI_WaterFlowSectionOption_SetRowGap(ArkUI_WaterFlowSectionOption* option, int32_t index, float rowGap) | - | 设置分组的行间距。 |
| float OH_ArkUI_WaterFlowSectionOption_GetRowGap(ArkUI_WaterFlowSectionOption* option, int32_t index) | - | 通过FlowItem分组配置信息获取对应索引下的分组的行间距。 |
| void OH_ArkUI_WaterFlowSectionOption_SetMargin(ArkUI_WaterFlowSectionOption* option, int32_t index,float marginTop, float marginRight, float marginBottom, float marginLeft) | - | 设置分组的外边距。 |
| ArkUI_Margin OH_ArkUI_WaterFlowSectionOption_GetMargin(ArkUI_WaterFlowSectionOption* option, int32_t index) | - | 通过FlowItem分组配置信息获取对应索引下的分组的外边距。 |
| void OH_ArkUI_WaterFlowSectionOption_RegisterGetItemMainSizeCallbackByIndex (ArkUI_WaterFlowSectionOption* option, int32_t index, float(*callback)(int32_t itemIndex)) | - | 通过FlowItem分组配置信息根据flowItemIndex获取指定Item的主轴大小。 |
| void OH_ArkUI_WaterFlowSectionOption_RegisterGetItemMainSizeCallbackByIndexWithUserData (ArkUI_WaterFlowSectionOption* option, int32_t index, void* userData, float (*callback)(int32_t itemIndex, void* userData)) | - | 通过FlowItem分组配置信息根据flowItemIndex获取指定Item的主轴大小。 |
| ArkUI_GuidelineOption* OH_ArkUI_GuidelineOption_Create(int32_t size) | - | 创建RelativeContainer容器内的辅助线信息。 |
| void OH_ArkUI_GuidelineOption_Dispose(ArkUI_GuidelineOption* guideline) | - | 销毁辅助线信息。 |
| void OH_ArkUI_GuidelineOption_SetId(ArkUI_GuidelineOption* guideline, const char* value, int32_t index) | - | 设置辅助线的Id。 |
| void OH_ArkUI_GuidelineOption_SetDirection(ArkUI_GuidelineOption* guideline, ArkUI_Axis value, int32_t index) | - | 设置辅助线的方向。 |
| void OH_ArkUI_GuidelineOption_SetPositionStart(ArkUI_GuidelineOption* guideline, float value, int32_t index) | - | 设置距离容器左侧或者顶部的距离。 |
| void OH_ArkUI_GuidelineOption_SetPositionEnd(ArkUI_GuidelineOption* guideline, float value, int32_t index) | - | 设置距离容器右侧或者底部的距离。 |
| const char* OH_ArkUI_GuidelineOption_GetId(ArkUI_GuidelineOption* guideline, int32_t index) | - | 获取辅助线的Id。 |
| ArkUI_Axis OH_ArkUI_GuidelineOption_GetDirection(ArkUI_GuidelineOption* guideline, int32_t index) | - | 获取辅助线的方向。 |
| float OH_ArkUI_GuidelineOption_GetPositionStart(ArkUI_GuidelineOption* guideline, int32_t index) | - | 获取距离容器左侧或者顶部的距离。 |
| float OH_ArkUI_GuidelineOption_GetPositionEnd(ArkUI_GuidelineOption* guideline, int32_t index) | - | 获取距离容器右侧或者底部的距离。 |
| ArkUI_BarrierOption* OH_ArkUI_BarrierOption_Create(int32_t size) | - | 创建RelativeContainer容器内的屏障信息。 |
| void OH_ArkUI_BarrierOption_Dispose(ArkUI_BarrierOption* barrierStyle) | - | 销毁屏障信息。 |
| void OH_ArkUI_BarrierOption_SetId(ArkUI_BarrierOption* barrierStyle, const char* value, int32_t index) | - | 设置屏障的Id。 |
| void OH_ArkUI_BarrierOption_SetDirection(ArkUI_BarrierOption* barrierStyle, ArkUI_BarrierDirection value, int32_t index) | - | 设置屏障的方向。 |
| void OH_ArkUI_BarrierOption_SetReferencedId(ArkUI_BarrierOption* barrierStyle, const char* value, int32_t index) | - | 设置屏障的依赖的组件。 |
| const char* OH_ArkUI_BarrierOption_GetId(ArkUI_BarrierOption* barrierStyle, int32_t index) | - | 获取屏障的Id。 |
| ArkUI_BarrierDirection OH_ArkUI_BarrierOption_GetDirection(ArkUI_BarrierOption* barrierStyle, int32_t index) | - | 获取屏障的方向。 |
| const char* OH_ArkUI_BarrierOption_GetReferencedId(ArkUI_BarrierOption* barrierStyle, int32_t index , int32_t referencedIndex) | - | 获取屏障的依赖的组件。 |
| int32_t OH_ArkUI_BarrierOption_GetReferencedIdSize(ArkUI_BarrierOption* barrierStyle, int32_t index) | - | 获取屏障的依赖的组件的个数。 |
| ArkUI_AlignmentRuleOption* OH_ArkUI_AlignmentRuleOption_Create() | - | 创建相对容器中子组件的对齐规则信息。 |
| void OH_ArkUI_AlignmentRuleOption_Dispose(ArkUI_AlignmentRuleOption* option) | - | 销毁相对容器中子组件的对齐规则信息。 |
| void OH_ArkUI_AlignmentRuleOption_SetStart(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_HorizontalAlignment alignment) | - | 设置相对布局的左对齐方式。 |
| void OH_ArkUI_AlignmentRuleOption_SetEnd(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_HorizontalAlignment alignment) | - | 设置相对布局的右对齐方式。 |
| void OH_ArkUI_AlignmentRuleOption_SetCenterHorizontal(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_HorizontalAlignment alignment) | - | 设置相对布局的横向居中对齐方式。 |
| void OH_ArkUI_AlignmentRuleOption_SetTop(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_VerticalAlignment alignment) | - | 设置相对布局的顶部对齐的方式。 |
| void OH_ArkUI_AlignmentRuleOption_SetBottom(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_VerticalAlignment alignment) | - | 设置相对布局的底部对齐的方式。 |
| void OH_ArkUI_AlignmentRuleOption_SetCenterVertical(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_VerticalAlignment alignment) | - | 设置相对布局的纵向居中对齐方式。 |
| void OH_ArkUI_AlignmentRuleOption_SetBiasHorizontal(ArkUI_AlignmentRuleOption* option, float horizontal) | - | 设置组件在锚点约束下的水平方向上偏移参数。 |
| void OH_ArkUI_AlignmentRuleOption_SetBiasVertical(ArkUI_AlignmentRuleOption* option, float vertical) | - | 设置组件在锚点约束下的垂直方向上偏移参数。 |
| const char* OH_ArkUI_AlignmentRuleOption_GetStartId(ArkUI_AlignmentRuleOption* option) | - | 获取左对齐锚点组件的Id。 |
| ArkUI_HorizontalAlignment OH_ArkUI_AlignmentRuleOption_GetStartAlignment(ArkUI_AlignmentRuleOption* option) | - | 获取左对齐方式。 |
| const char* OH_ArkUI_AlignmentRuleOption_GetEndId(ArkUI_AlignmentRuleOption* option) | - | 获取右对齐锚点组件的Id。 |
| ArkUI_HorizontalAlignment OH_ArkUI_AlignmentRuleOption_GetEndAlignment(ArkUI_AlignmentRuleOption* option) | - | 获取右对齐方式。 |
| const char* OH_ArkUI_AlignmentRuleOption_GetCenterIdHorizontal(ArkUI_AlignmentRuleOption* option) | - | 获取横向居中对齐锚点组件的Id。 |
| ArkUI_HorizontalAlignment OH_ArkUI_AlignmentRuleOption_GetCenterAlignmentHorizontal(ArkUI_AlignmentRuleOption* option) | - | 获取横向居中对齐方式。 |
| const char* OH_ArkUI_AlignmentRuleOption_GetTopId(ArkUI_AlignmentRuleOption* option) | - | 获取顶部对齐锚点组件的Id。 |
| ArkUI_VerticalAlignment OH_ArkUI_AlignmentRuleOption_GetTopAlignment(ArkUI_AlignmentRuleOption* option) | - | 获取顶部对齐的方式。 |
| const char* OH_ArkUI_AlignmentRuleOption_GetBottomId(ArkUI_AlignmentRuleOption* option) | - | 获取底部对齐锚点组件的Id。 |
| ArkUI_VerticalAlignment OH_ArkUI_AlignmentRuleOption_GetBottomAlignment(ArkUI_AlignmentRuleOption* option) | - | 获取底部对齐的方式。 |
| const char* OH_ArkUI_AlignmentRuleOption_GetCenterIdVertical(ArkUI_AlignmentRuleOption* option) | - | 获取纵向居中对齐锚点组件的Id。 |
| ArkUI_VerticalAlignment OH_ArkUI_AlignmentRuleOption_GetCenterAlignmentVertical(ArkUI_AlignmentRuleOption* option) | - | 获取纵向居中对齐方式。 |
| float OH_ArkUI_AlignmentRuleOption_GetBiasHorizontal(ArkUI_AlignmentRuleOption* option) | - | 获取水平方向上的bias值。 |
| float OH_ArkUI_AlignmentRuleOption_GetBiasVertical(ArkUI_AlignmentRuleOption* option) | - | 获取垂直方向上的bias值。 |
| ArkUI_SwiperIndicator* OH_ArkUI_SwiperIndicator_Create(ArkUI_SwiperIndicatorType type) | - | 创建Swiper组件的导航指示器。 |
| void OH_ArkUI_SwiperIndicator_Dispose(ArkUI_SwiperIndicator* indicator) | - | 销毁Swiper组件的导航指示器指针。 |
| void OH_ArkUI_SwiperIndicator_SetStartPosition(ArkUI_SwiperIndicator* indicator, float value) | - | 设置导航点距离Swiper组件左边的距离。 |
| float OH_ArkUI_SwiperIndicator_GetStartPosition(ArkUI_SwiperIndicator* indicator) | - | 获取导航点距离Swiper组件左边的距离。 |
| void OH_ArkUI_SwiperIndicator_SetTopPosition(ArkUI_SwiperIndicator* indicator, float value) | - | 设置导航点距离Swiper组件顶部的距离。 |
| float OH_ArkUI_SwiperIndicator_GetTopPosition(ArkUI_SwiperIndicator* indicator) | - | 获取导航点距离Swiper组件顶部的距离。 |
| void OH_ArkUI_SwiperIndicator_SetEndPosition(ArkUI_SwiperIndicator* indicator, float value) | - | 设置导航点距离Swiper组件右边的距离。 |
| float OH_ArkUI_SwiperIndicator_GetEndPosition(ArkUI_SwiperIndicator* indicator) | - | 获取导航点距离Swiper组件右边的距离。 |
| void OH_ArkUI_SwiperIndicator_SetBottomPosition(ArkUI_SwiperIndicator* indicator, float value) | - | 设置导航点距离Swiper组件底部的距离。 |
| float OH_ArkUI_SwiperIndicator_GetBottomPosition(ArkUI_SwiperIndicator* indicator) | - | 获取导航点距离Swiper组件底部的距离。 |
| void OH_ArkUI_SwiperIndicator_SetIgnoreSizeOfBottom(ArkUI_SwiperIndicator* indicator, int32_t ignoreSize) | - | 设置OH_ArkUI_SwiperIndicator_SetBottomPosition是否忽略导航点大小。 |
| int32_t OH_ArkUI_SwiperIndicator_GetIgnoreSizeOfBottom(ArkUI_SwiperIndicator* indicator) | - | 获取OH_ArkUI_SwiperIndicator_SetBottomPosition是否忽略导航点大小。 |
| void OH_ArkUI_SwiperIndicator_SetItemWidth(ArkUI_SwiperIndicator* indicator, float value) | - | 设置Swiper组件圆点导航指示器的宽。 |
| float OH_ArkUI_SwiperIndicator_GetItemWidth(ArkUI_SwiperIndicator* indicator) | - | 获取Swiper组件圆点导航指示器的宽。 |
| void OH_ArkUI_SwiperIndicator_SetItemHeight(ArkUI_SwiperIndicator* indicator, float value) | - | 设置Swiper组件圆点导航指示器的高。 |
| float OH_ArkUI_SwiperIndicator_GetItemHeight(ArkUI_SwiperIndicator* indicator) | - | 获取Swiper组件圆点导航指示器的高。 |
| void OH_ArkUI_SwiperIndicator_SetSelectedItemWidth(ArkUI_SwiperIndicator* indicator, float value) | - | 设置被选中的Swiper组件圆点导航指示器的宽。 |
| float OH_ArkUI_SwiperIndicator_GetSelectedItemWidth(ArkUI_SwiperIndicator* indicator) | - | 获取被选中Swiper组件圆点导航指示器的宽。 |
| void OH_ArkUI_SwiperIndicator_SetSelectedItemHeight(ArkUI_SwiperIndicator* indicator, float value) | - | 设置被选中的Swiper组件圆点导航指示器的高。 |
| float OH_ArkUI_SwiperIndicator_GetSelectedItemHeight(ArkUI_SwiperIndicator* indicator) | - | 获取被选中Swiper组件圆点导航指示器的高。 |
| void OH_ArkUI_SwiperIndicator_SetMask(ArkUI_SwiperIndicator* indicator, int32_t mask) | - | 设置是否显示Swiper组件圆点导航指示器的蒙版样式。 |
| int32_t OH_ArkUI_SwiperIndicator_GetMask(ArkUI_SwiperIndicator* indicator) | - | 获取是否显示Swiper组件圆点导航指示器的蒙版样式。 |
| void OH_ArkUI_SwiperIndicator_SetColor(ArkUI_SwiperIndicator* indicator, uint32_t color) | - | 设置Swiper组件圆点导航指示器的颜色。 |
| uint32_t OH_ArkUI_SwiperIndicator_GetColor(ArkUI_SwiperIndicator* indicator) | - | 获取Swiper组件圆点导航指示器的颜色。 |
| void OH_ArkUI_SwiperIndicator_SetSelectedColor(ArkUI_SwiperIndicator* indicator, uint32_t selectedColor) | - | 设置被选中Swiper组件圆点导航指示器的颜色。 |
| uint32_t OH_ArkUI_SwiperIndicator_GetSelectedColor(ArkUI_SwiperIndicator* indicator) | - | 获取被选中Swiper组件圆点导航指示器的颜色。 |
| int32_t OH_ArkUI_SwiperIndicator_SetMaxDisplayCount(ArkUI_SwiperIndicator* indicator, int32_t maxDisplayCount) | - | 设置圆点导航点指示器样式下，导航点显示个数的最大值。 |
| int32_t OH_ArkUI_SwiperIndicator_GetMaxDisplayCount(ArkUI_SwiperIndicator* indicator) | - | 获取圆点导航点指示器样式下，导航点显示个数的最大值。 |
| ArkUI_SwiperDigitIndicator *OH_ArkUI_SwiperDigitIndicator_Create() | - | 创建Swiper组件的数字导航指示器。 |
| void OH_ArkUI_SwiperDigitIndicator_Destroy(ArkUI_SwiperDigitIndicator* indicator) | - | 销毁Swiper组件的数字导航指示器指针。 |
| void OH_ArkUI_SwiperDigitIndicator_SetStartPosition(ArkUI_SwiperDigitIndicator* indicator, float value) | - | 设置数字导航指示器距离Swiper组件左边的距离，在从右至左显示的语言模式下，设置其距离Swiper组件右边的距离。 |
| float OH_ArkUI_SwiperDigitIndicator_GetStartPosition(ArkUI_SwiperDigitIndicator* indicator) | - | 获取数字导航指示器距离Swiper组件左边的距离，在从右至左显示的语言模式下，获取其距离Swiper组件右边的距离。 |
| void OH_ArkUI_SwiperDigitIndicator_SetTopPosition(ArkUI_SwiperDigitIndicator* indicator, float value) | - | 设置数字导航指示器距离Swiper组件顶部的距离。 |
| float OH_ArkUI_SwiperDigitIndicator_GetTopPosition(ArkUI_SwiperDigitIndicator* indicator) | - | 获取数字导航指示器距离Swiper组件顶部的距离。 |
| void OH_ArkUI_SwiperDigitIndicator_SetEndPosition(ArkUI_SwiperDigitIndicator* indicator, float value) | - | 设置数字导航指示器距离Swiper组件右边的距离，在从右至左显示的语言模式下，设置其距离Swiper组件左边的距离。 |
| float OH_ArkUI_SwiperDigitIndicator_GetEndPosition(ArkUI_SwiperDigitIndicator* indicator) | - | 获取数字导航指示器距离Swiper组件右边的距离，在从右至左显示的语言模式下，获取其距离Swiper组件左边的距离。 |
| void OH_ArkUI_SwiperDigitIndicator_SetBottomPosition(ArkUI_SwiperDigitIndicator* indicator, float value) | - | 设置数字导航指示器距离Swiper组件底部的距离。 |
| float OH_ArkUI_SwiperDigitIndicator_GetBottomPosition(ArkUI_SwiperDigitIndicator* indicator) | - | 获取数字导航指示器距离Swiper组件底部的距离。 |
| void OH_ArkUI_SwiperDigitIndicator_SetFontColor(ArkUI_SwiperDigitIndicator* indicator, uint32_t color) | - | 设置Swiper组件数字导航指示器字体颜色。 |
| uint32_t OH_ArkUI_SwiperDigitIndicator_GetFontColor(ArkUI_SwiperDigitIndicator* indicator) | - | 获取Swiper组件数字导航指示器字体颜色。 |
| void OH_ArkUI_SwiperDigitIndicator_SetSelectedFontColor(ArkUI_SwiperDigitIndicator* indicator, uint32_t selectedColor) | - | 设置被选中Swiper组件数字导航指示器字体颜色。 |
| uint32_t OH_ArkUI_SwiperDigitIndicator_GetSelectedFontColor(ArkUI_SwiperDigitIndicator* indicator) | - | 获取被选中Swiper组件数字导航指示器字体颜色。 |
| void OH_ArkUI_SwiperDigitIndicator_SetFontSize(ArkUI_SwiperDigitIndicator* indicator, float size) | - | 设置Swiper组件数字导航指示器字体大小。 |
| float OH_ArkUI_SwiperDigitIndicator_GetFontSize(ArkUI_SwiperDigitIndicator* indicator) | - | 获取Swiper组件数字导航指示器字体大小。 |
| void OH_ArkUI_SwiperDigitIndicator_SetSelectedFontSize(ArkUI_SwiperDigitIndicator* indicator, float size) | - | 设置被选中Swiper组件数字导航指示器字体大小。 |
| float OH_ArkUI_SwiperDigitIndicator_GetSelectedFontSize(ArkUI_SwiperDigitIndicator* indicator) | - | 获取被选中Swiper组件数字导航指示器字体大小。 |
| void OH_ArkUI_SwiperDigitIndicator_SetFontWeight(ArkUI_SwiperDigitIndicator *indicator, ArkUI_FontWeight fontWeight) | - | 设置Swiper组件数字导航指示器字体粗细属性。 |
| ArkUI_FontWeight OH_ArkUI_SwiperDigitIndicator_GetFontWeight(ArkUI_SwiperDigitIndicator* indicator) | - | 获取Swiper组件数字导航指示器字体粗细属性。 |
| void OH_ArkUI_SwiperDigitIndicator_SetSelectedFontWeight(ArkUI_SwiperDigitIndicator *indicator, ArkUI_FontWeight selectedFontWeight) | - | 设置被选中Swiper组件数字导航指示器字体粗细属性。 |
| ArkUI_FontWeight OH_ArkUI_SwiperDigitIndicator_GetSelectedFontWeight(ArkUI_SwiperDigitIndicator* indicator) | - | 获取被选中Swiper组件数字导航指示器字体粗细属性。 |
| ArkUI_SwiperArrowStyle *OH_ArkUI_SwiperArrowStyle_Create() | - | 创建Swiper组件的导航箭头。 |
| void OH_ArkUI_SwiperArrowStyle_Destroy(ArkUI_SwiperArrowStyle* arrowStyle) | - | 销毁Swiper组件的导航箭头指针。 |
| void OH_ArkUI_SwiperArrowStyle_SetShowBackground(ArkUI_SwiperArrowStyle* arrowStyle, int32_t showBackground) | - | 设置Swiper组件导航箭头底板是否显示。 |
| int32_t OH_ArkUI_SwiperArrowStyle_GetShowBackground(ArkUI_SwiperArrowStyle* arrowStyle) | - | 获取Swiper组件导航箭头底板是否显示。 |
| void OH_ArkUI_SwiperArrowStyle_SetShowSidebarMiddle(ArkUI_SwiperArrowStyle* arrowStyle, int32_t showSidebarMiddle) | - | 设置Swiper组件导航箭头显示位置。 |
| int32_t OH_ArkUI_SwiperArrowStyle_GetShowSidebarMiddle(ArkUI_SwiperArrowStyle* arrowStyle) | - | 获取Swiper组件导航箭头显示位置。 |
| void OH_ArkUI_SwiperArrowStyle_SetBackgroundSize(ArkUI_SwiperArrowStyle* arrowStyle, float backgroundSize) | - | 设置Swiper组件导航箭头底板大小。 |
| float OH_ArkUI_SwiperArrowStyle_GetBackgroundSize(ArkUI_SwiperArrowStyle* arrowStyle) | - | 获取Swiper组件导航箭头底板大小。 |
| void OH_ArkUI_SwiperArrowStyle_SetBackgroundColor(ArkUI_SwiperArrowStyle* arrowStyle, uint32_t backgroundColor) | - | 设置Swiper组件导航箭头底板颜色。 |
| uint32_t OH_ArkUI_SwiperArrowStyle_GetBackgroundColor(ArkUI_SwiperArrowStyle* arrowStyle) | - | 获取Swiper组件导航箭头底板颜色。 |
| void OH_ArkUI_SwiperArrowStyle_SetArrowSize(ArkUI_SwiperArrowStyle* arrowStyle, float arrowSize) | - | 设置Swiper组件导航箭头大小。 |
| float OH_ArkUI_SwiperArrowStyle_GetArrowSize(ArkUI_SwiperArrowStyle* arrowStyle) | - | 获取Swiper组件导航箭头大小。 |
| void OH_ArkUI_SwiperArrowStyle_SetArrowColor(ArkUI_SwiperArrowStyle* arrowStyle, uint32_t arrowColor) | - | 设置Swiper组件导航箭头颜色。 |
| uint32_t OH_ArkUI_SwiperArrowStyle_GetArrowColor(ArkUI_SwiperArrowStyle* arrowStyle) | - | 获取Swiper组件导航箭头颜色。 |
| void OH_ArkUI_SwiperIndicator_SetSpace(ArkUI_SwiperIndicator* indicator, float space) | - | 设置导航点间距。 |
| float OH_ArkUI_SwiperIndicator_GetSpace(ArkUI_SwiperIndicator* indicator) | - | 获取导航点间距。 |
| void OH_ArkUI_SwiperDigitIndicator_SetIgnoreSizeOfBottom(ArkUI_SwiperDigitIndicator* indicator, int32_t ignoreSize) | - | 设置OH_ArkUI_SwiperDigitIndicator_SetBottomPosition是否忽略导航点大小。 |
| int32_t OH_ArkUI_SwiperDigitIndicator_GetIgnoreSizeOfBottom(ArkUI_SwiperDigitIndicator* indicator) | - | 获取OH_ArkUI_SwiperDigitIndicator_SetBottomPosition是否忽略导航点大小。 |
| ArkUI_ListItemSwipeActionItem* OH_ArkUI_ListItemSwipeActionItem_Create() | - | 创建ListItemSwipeActionItem接口设置的配置项。 |
| void OH_ArkUI_ListItemSwipeActionItem_Dispose(ArkUI_ListItemSwipeActionItem* item) | - | 销毁ListItemSwipeActionItem实例。 |
| void OH_ArkUI_ListItemSwipeActionItem_SetContent(ArkUI_ListItemSwipeActionItem* item, ArkUI_NodeHandle node) | - | 设置ListItemSwipeActionItem的布局内容。 |
| void OH_ArkUI_ListItemSwipeActionItem_SetActionAreaDistance(ArkUI_ListItemSwipeActionItem* item, float distance) | - | 设置组件长距离滑动删除距离阈值。 |
| float OH_ArkUI_ListItemSwipeActionItem_GetActionAreaDistance(ArkUI_ListItemSwipeActionItem* item) | - | 获取组件长距离滑动删除距离阈值。 |
| void OH_ArkUI_ListItemSwipeActionItem_SetOnEnterActionArea(ArkUI_ListItemSwipeActionItem* item, void (*callback)()) | - | 设置滑动条目进入删除区域时调用的事件。 |
| void OH_ArkUI_ListItemSwipeActionItem_SetOnEnterActionAreaWithUserData (ArkUI_ListItemSwipeActionItem* item,void* userData, void (*callback)(void* userData)) | - | 设置滑动条目进入删除区域时调用的事件。 |
| void OH_ArkUI_ListItemSwipeActionItem_SetOnAction(ArkUI_ListItemSwipeActionItem* item, void (*callback)()) | - | 设置组件进入长距删除区后删除ListItem时调用的事件。 |
| void OH_ArkUI_ListItemSwipeActionItem_SetOnActionWithUserData(ArkUI_ListItemSwipeActionItem* item,void* userData, void (*callback)(void* userData)) | - | 设置组件进入长距删除区后删除ListItem时调用的事件。 |
| void OH_ArkUI_ListItemSwipeActionItem_SetOnExitActionArea(ArkUI_ListItemSwipeActionItem* item, void (*callback)()) | - | 设置滑动条目退出删除区域时调用的事件。 |
| void OH_ArkUI_ListItemSwipeActionItem_SetOnExitActionAreaWithUserData (ArkUI_ListItemSwipeActionItem* item,void* userData, void (*callback)(void* userData)) | - | 设置滑动条目退出删除区域时调用的事件。 |
| void OH_ArkUI_ListItemSwipeActionItem_SetOnStateChange (ArkUI_ListItemSwipeActionItem* item,void (*callback)(ArkUI_ListItemSwipeActionState swipeActionState)) | - | 设置列表项滑动状态变化时候触发的事件。 |
| void OH_ArkUI_ListItemSwipeActionItem_SetOnStateChangeWithUserData (ArkUI_ListItemSwipeActionItem* item,void* userData, void (*callback)(ArkUI_ListItemSwipeActionState swipeActionState, void* userData)) | - | 设置列表项滑动状态变化时候触发的事件。 |
| ArkUI_ListItemSwipeActionOption* OH_ArkUI_ListItemSwipeActionOption_Create() | - | 创建ListItemSwipeActionOption接口设置的配置项。 |
| void OH_ArkUI_ListItemSwipeActionOption_Dispose(ArkUI_ListItemSwipeActionOption* option) | - | 销毁ListItemSwipeActionOption实例。 |
| void OH_ArkUI_ListItemSwipeActionOption_SetStart(ArkUI_ListItemSwipeActionOption* option, ArkUI_ListItemSwipeActionItem* item) | - | 设置ListItemSwipeActionItem的左侧（垂直布局）或上方（横向布局）布局内容。 |
| void OH_ArkUI_ListItemSwipeActionOption_SetEnd(ArkUI_ListItemSwipeActionOption* option, ArkUI_ListItemSwipeActionItem* item) | - | 设置ListItemSwipeActionItem的右侧（垂直布局）或下方（横向布局）布局内容。 |
| void OH_ArkUI_ListItemSwipeActionOption_SetEdgeEffect(ArkUI_ListItemSwipeActionOption* option, ArkUI_ListItemSwipeEdgeEffect edgeEffect) | - | 设置滑动效果。 |
| int32_t OH_ArkUI_ListItemSwipeActionOption_GetEdgeEffect(ArkUI_ListItemSwipeActionOption* option) | - | 获取滑动效果。 |
| void OH_ArkUI_ListItemSwipeActionOption_SetOnOffsetChange(ArkUI_ListItemSwipeActionOption* option, void (*callback)(float offset)) | - | 滑动操作偏移量更改时调用的事件。 |
| void OH_ArkUI_ListItemSwipeActionOption_SetOnOffsetChangeWithUserData (ArkUI_ListItemSwipeActionOption* option, void* userData, void (*callback)(float offset, void* userData)) | - | 滑动操作偏移量更改时调用的事件。 |
| int32_t OH_ArkUI_ListItemSwipeAction_Expand(ArkUI_NodeHandle node, ArkUI_ListItemSwipeActionDirection direction) | - | 展开指定ListItem的划出菜单。 |
| int32_t OH_ArkUI_ListItemSwipeAction_Collapse(ArkUI_NodeHandle node) | - | 收起指定ListItem的划出菜单。 |
| ArkUI_AccessibilityState* OH_ArkUI_AccessibilityState_Create(void) | - | 创建无障碍状态。 |
| void OH_ArkUI_AccessibilityState_Dispose(ArkUI_AccessibilityState* state) | - | 销毁无障碍状态指针。 |
| void OH_ArkUI_AccessibilityState_SetDisabled(ArkUI_AccessibilityState* state, int32_t isDisabled) | - | 设置无障碍状态是否禁用。 |
| int32_t OH_ArkUI_AccessibilityState_IsDisabled(ArkUI_AccessibilityState* state) | - | 获取无障碍状态是否禁用。 |
| void OH_ArkUI_AccessibilityState_SetSelected(ArkUI_AccessibilityState* state, int32_t isSelected) | - | 设置无障碍状态是否选中。 |
| int32_t OH_ArkUI_AccessibilityState_IsSelected(ArkUI_AccessibilityState* state) | - | 获取无障碍状态是否选中。 |
| void OH_ArkUI_AccessibilityState_SetCheckedState(ArkUI_AccessibilityState* state, int32_t checkedState) | - | 设置无障碍状态复选框状态。 |
| int32_t OH_ArkUI_AccessibilityState_GetCheckedState(ArkUI_AccessibilityState* state) | - | 获取无障碍状态复选框状态。 |
| ArkUI_AccessibilityValue* OH_ArkUI_AccessibilityValue_Create(void) | - | 创建无障碍信息。 |
| void OH_ArkUI_AccessibilityValue_Dispose(ArkUI_AccessibilityValue* value) | - | 销毁无障碍信息指针。 |
| void OH_ArkUI_AccessibilityValue_SetMin(ArkUI_AccessibilityValue* value, int32_t min) | - | 设置无障碍最小值信息。 |
| int32_t OH_ArkUI_AccessibilityValue_GetMin(ArkUI_AccessibilityValue* value) | - | 获取无障碍最小值信息。 |
| void OH_ArkUI_AccessibilityValue_SetMax(ArkUI_AccessibilityValue* value, int32_t max) | - | 设置无障碍最大值信息。 |
| int32_t OH_ArkUI_AccessibilityValue_GetMax(ArkUI_AccessibilityValue* value) | - | 获取无障碍最大值信息。 |
| void OH_ArkUI_AccessibilityValue_SetCurrent(ArkUI_AccessibilityValue* value, int32_t current) | - | 设置无障碍当前值信息。 |
| int32_t OH_ArkUI_AccessibilityValue_GetCurrent(ArkUI_AccessibilityValue* value) | - | 获取无障碍当前值信息。 |
| void OH_ArkUI_AccessibilityValue_SetRangeMin(ArkUI_AccessibilityValue* value, int32_t rangeMin) | - | 设置范围组件的无障碍最小值信息。 |
| int32_t OH_ArkUI_AccessibilityValue_GetRangeMin(ArkUI_AccessibilityValue* value) | - | 获取范围组件的无障碍最小值信息。 |
| void OH_ArkUI_AccessibilityValue_SetRangeMax(ArkUI_AccessibilityValue* value, int32_t rangeMax) | - | 设置范围组件的无障碍最大值信息。 |
| int32_t OH_ArkUI_AccessibilityValue_GetRangeMax(ArkUI_AccessibilityValue* value) | - | 获取范围组件的无障碍最大值信息。 |
| void OH_ArkUI_AccessibilityValue_SetRangeCurrent(ArkUI_AccessibilityValue* value, int32_t rangeCurrent) | - | 用于设置范围组件的无障碍当前值信息。 |
| int32_t OH_ArkUI_AccessibilityValue_GetRangeCurrent(ArkUI_AccessibilityValue* value) | - | 用于获取范围组件的无障碍当前值信息。 |
| void OH_ArkUI_AccessibilityValue_SetText(ArkUI_AccessibilityValue* value, const char* text) | - | 设置无障碍文本描述信息。 |
| const char* OH_ArkUI_AccessibilityValue_GetText(ArkUI_AccessibilityValue* value) | - | 获取无障碍文本描述信息。 |
| ArkUI_ImageAnimatorFrameInfo* OH_ArkUI_ImageAnimatorFrameInfo_CreateFromString(char* src) | - | 使用图片路径创建帧图片信息，图片格式为svg，png和jpg。 |
| ArkUI_ImageAnimatorFrameInfo* OH_ArkUI_ImageAnimatorFrameInfo_CreateFromDrawableDescriptor(ArkUI_DrawableDescriptor* drawable) | - | 使用 DrawableDescriptor 对象创建帧图片信息，图片格式为Resource和PixelMap。 |
| void OH_ArkUI_ImageAnimatorFrameInfo_Dispose(ArkUI_ImageAnimatorFrameInfo* imageInfo) | - | 销毁帧图片对象指针。 |
| void OH_ArkUI_ImageAnimatorFrameInfo_SetWidth(ArkUI_ImageAnimatorFrameInfo* imageInfo, int32_t width) | - | 设置图片宽度。 |
| int32_t OH_ArkUI_ImageAnimatorFrameInfo_GetWidth(ArkUI_ImageAnimatorFrameInfo* imageInfo) | - | 获取图片宽度。 |
| void OH_ArkUI_ImageAnimatorFrameInfo_SetHeight(ArkUI_ImageAnimatorFrameInfo* imageInfo, int32_t height) | - | 设置图片高度。 |
| int32_t OH_ArkUI_ImageAnimatorFrameInfo_GetHeight(ArkUI_ImageAnimatorFrameInfo* imageInfo) | - | 获取图片高度。 |
| void OH_ArkUI_ImageAnimatorFrameInfo_SetTop(ArkUI_ImageAnimatorFrameInfo* imageInfo, int32_t top) | - | 设置图片相对于组件左上角的纵向坐标。 |
| int32_t OH_ArkUI_ImageAnimatorFrameInfo_GetTop(ArkUI_ImageAnimatorFrameInfo* imageInfo) | - | 获取图片相对于组件左上角的纵向坐标。 |
| void OH_ArkUI_ImageAnimatorFrameInfo_SetLeft(ArkUI_ImageAnimatorFrameInfo* imageInfo, int32_t left) | - | 设置图片相对于组件左上角的横向坐标。 |
| int32_t OH_ArkUI_ImageAnimatorFrameInfo_GetLeft(ArkUI_ImageAnimatorFrameInfo* imageInfo) | - | 获取图片相对于组件左上角的横向坐标。 |
| void OH_ArkUI_ImageAnimatorFrameInfo_SetDuration(ArkUI_ImageAnimatorFrameInfo* imageInfo, int32_t duration) | - | 设置图片的播放时长。 |
| int32_t OH_ArkUI_ImageAnimatorFrameInfo_GetDuration(ArkUI_ImageAnimatorFrameInfo* imageInfo) | - | 获取图片的播放时长。 |
| ArkUI_ListChildrenMainSize* OH_ArkUI_ListChildrenMainSizeOption_Create() | - | 创建ListChildrenMainSize接口设置的配置项。 |
| void OH_ArkUI_ListChildrenMainSizeOption_Dispose(ArkUI_ListChildrenMainSize* option) | - | 销毁ListChildrenMainSize实例。 |
| int32_t OH_ArkUI_ListChildrenMainSizeOption_SetDefaultMainSize(ArkUI_ListChildrenMainSize* option, float defaultMainSize) | - | 设置List组件的ChildrenMainSizeOption默认大小。 |
| float OH_ArkUI_ListChildrenMainSizeOption_GetDefaultMainSize(ArkUI_ListChildrenMainSize* option) | - | 获取List组件的ChildrenMainSizeOption默认大小。 |
| void OH_ArkUI_ListChildrenMainSizeOption_Resize(ArkUI_ListChildrenMainSize* option, int32_t totalSize) | - | 重置List组件的ChildrenMainSizeOption的数组大小。 |
| int32_t OH_ArkUI_ListChildrenMainSizeOption_Splice(ArkUI_ListChildrenMainSize* option, int32_t index, int32_t deleteCount, int32_t addCount) | - | 对List组件的ChildrenMainSizeOption数组操作大小调整。 |
| int32_t OH_ArkUI_ListChildrenMainSizeOption_UpdateSize(ArkUI_ListChildrenMainSize* option, int32_t index, float mainSize) | - | 更新List组件的ChildrenMainSizeOption数组的值。 |
| float OH_ArkUI_ListChildrenMainSizeOption_GetMainSize(ArkUI_ListChildrenMainSize* option, int32_t index) | - | 获取List组件的ChildrenMainSizeOption数组的值。 |
| ArkUI_CustomSpanMeasureInfo* OH_ArkUI_CustomSpanMeasureInfo_Create(void) | - | 创建自定义段落组件测量信息。 |
| void OH_ArkUI_CustomSpanMeasureInfo_Dispose(ArkUI_CustomSpanMeasureInfo* info) | - | 销毁自定义段落组件测量信息。 |
| float OH_ArkUI_CustomSpanMeasureInfo_GetFontSize(ArkUI_CustomSpanMeasureInfo* info) | - | 获取自定义段落组件的父节点Text的字体大小。 |
| ArkUI_CustomSpanMetrics* OH_ArkUI_CustomSpanMetrics_Create(void) | - | 创建自定义段落组件度量信息。 |
| void OH_ArkUI_CustomSpanMetrics_Dispose(ArkUI_CustomSpanMetrics* metrics) | - | 销毁自定义段落组件度量信息。 |
| int32_t OH_ArkUI_CustomSpanMetrics_SetWidth(ArkUI_CustomSpanMetrics* metrics, float width) | - | 设置自定义段落组件的宽度。 |
| int32_t OH_ArkUI_CustomSpanMetrics_SetHeight(ArkUI_CustomSpanMetrics* metrics, float height) | - | 设置自定义段落组件的高度。 |
| ArkUI_CustomSpanDrawInfo* OH_ArkUI_CustomSpanDrawInfo_Create(void) | - | 创建自定义段落组件绘制信息。 |
| void OH_ArkUI_CustomSpanDrawInfo_Dispose(ArkUI_CustomSpanDrawInfo* info) | - | 销毁自定义段落组件绘制信息。 |
| float OH_ArkUI_CustomSpanDrawInfo_GetXOffset(ArkUI_CustomSpanDrawInfo* info) | - | 获取自定义段落组件相对于挂载组件的x轴偏移值。 |
| float OH_ArkUI_CustomSpanDrawInfo_GetLineTop(ArkUI_CustomSpanDrawInfo* info) | - | 获取自定义段落组件相对于挂载组件的上边距。 |
| float OH_ArkUI_CustomSpanDrawInfo_GetLineBottom(ArkUI_CustomSpanDrawInfo* info) | - | 获取自定义段落组件相对于挂载组件的下边距。 |
| float OH_ArkUI_CustomSpanDrawInfo_GetBaseline(ArkUI_CustomSpanDrawInfo* info) | - | 获取自定义段落组件相对于挂载组件的基线偏移量。 |
| void OH_ArkUI_CustomProperty_Destroy(ArkUI_CustomProperty* handle) | - | 销毁CustomProperty实例。 |
| const char* OH_ArkUI_CustomProperty_GetStringValue(ArkUI_CustomProperty* handle) | - | 获取自定义属性value信息。 |
| const char* OH_ArkUI_HostWindowInfo_GetName(ArkUI_HostWindowInfo* info) | - | 获取HostWindowInfo对象中的窗口名称。 |
| void OH_ArkUI_HostWindowInfo_Destroy(ArkUI_HostWindowInfo* info) | - | 销毁HostWindowInfo对象。 |
| void OH_ArkUI_ActiveChildrenInfo_Destroy(ArkUI_ActiveChildrenInfo* handle) | - | 销毁ActiveChildrenInfo实例。 |
| ArkUI_NodeHandle OH_ArkUI_ActiveChildrenInfo_GetNodeByIndex(ArkUI_ActiveChildrenInfo* handle, int32_t index) | - | 获取ActiveChildrenInfo结构体的下标为index的子节点。 |
| int32_t OH_ArkUI_ActiveChildrenInfo_GetCount(ArkUI_ActiveChildrenInfo* handle) | - | 获取ActiveChildrenInfo结构体内的节点数量。 |
| ArkUI_ProgressLinearStyleOption* OH_ArkUI_ProgressLinearStyleOption_Create(void) | - | 创建线性进度条样式信息。 |
| void OH_ArkUI_ProgressLinearStyleOption_Destroy(ArkUI_ProgressLinearStyleOption* option) | - | 销毁线性进度条样式信息。 |
| void OH_ArkUI_ProgressLinearStyleOption_SetSmoothEffectEnabled(ArkUI_ProgressLinearStyleOption* option, bool enabled) | - | 设置进度平滑动效的开关。 |
| void OH_ArkUI_ProgressLinearStyleOption_SetScanEffectEnabled(ArkUI_ProgressLinearStyleOption* option, bool enabled) | - | 设置扫光效果的开关。 |
| void OH_ArkUI_ProgressLinearStyleOption_SetStrokeWidth(ArkUI_ProgressLinearStyleOption* option, float strokeWidth) | - | 设置进度条宽度。 |
| void OH_ArkUI_ProgressLinearStyleOption_SetStrokeRadius(ArkUI_ProgressLinearStyleOption* option, float strokeRadius) | - | 设置进度条圆角半径。 |
| bool OH_ArkUI_ProgressLinearStyleOption_GetSmoothEffectEnabled(ArkUI_ProgressLinearStyleOption* option) | - | 获取进度平滑动效的开关信息。 |
| bool OH_ArkUI_ProgressLinearStyleOption_GetScanEffectEnabled(ArkUI_ProgressLinearStyleOption* option) | - | 获取扫光效果的开关信息。 |
| float OH_ArkUI_ProgressLinearStyleOption_GetStrokeWidth(ArkUI_ProgressLinearStyleOption* option) | - | 获取进度条宽度。 |
| float OH_ArkUI_ProgressLinearStyleOption_GetStrokeRadius(ArkUI_ProgressLinearStyleOption* option) | - | 获取进度条圆角半径值。 |
| ArkUI_SnapshotOptions* OH_ArkUI_CreateSnapshotOptions() | - | 创建一个截图选项，当返回值不再使用时必须通过OH_ArkUI_DestroySnapshotOptions()释放。 |
| void OH_ArkUI_DestroySnapshotOptions(ArkUI_SnapshotOptions* snapshotOptions) | - | 销毁截图选项指针。 |
| int32_t OH_ArkUI_SnapshotOptions_SetScale(ArkUI_SnapshotOptions* snapshotOptions, float scale) | - | 配置截图选项中的缩放属性。 |
| int32_t OH_ArkUI_SnapshotOptions_SetColorMode(ArkUI_SnapshotOptions* snapshotOptions, int32_t colorSpace, bool isAuto) | - | 设置截图选项中的色彩空间。 |
| int32_t OH_ArkUI_SnapshotOptions_SetDynamicRangeMode(ArkUI_SnapshotOptions* snapshotOptions, int32_t dynamicRangeMode, bool isAuto) | - | 设置截图选项中的动态范围模式。 |
| ArkUI_CrossLanguageOption* OH_ArkUI_CrossLanguageOption_Create(void) | - | 创建跨语言配置项实例。 |
| void OH_ArkUI_CrossLanguageOption_Destroy(ArkUI_CrossLanguageOption* option) | - | 销毁跨语言配置项实例。 |
| void OH_ArkUI_CrossLanguageOption_SetAttributeSettingStatus(ArkUI_CrossLanguageOption* option, bool enabled) | - | 设置配置项中是否允许跨语言修改属性。 |
| bool OH_ArkUI_CrossLanguageOption_GetAttributeSettingStatus(ArkUI_CrossLanguageOption* option) | - | 获取配置项中是否允许跨语言修改属性。 |
| ArkUI_VisibleAreaEventOptions* OH_ArkUI_VisibleAreaEventOptions_Create() | - | 创建可见区域变化监听的参数。 |
| void OH_ArkUI_VisibleAreaEventOptions_Dispose(ArkUI_VisibleAreaEventOptions* option) | - | 销毁可见区域变化监听的参数。 |
| int32_t OH_ArkUI_VisibleAreaEventOptions_SetRatios(ArkUI_VisibleAreaEventOptions* option, float* value, int32_t size) | - | 设置阈值数组。 |
| int32_t OH_ArkUI_VisibleAreaEventOptions_SetExpectedUpdateInterval(ArkUI_VisibleAreaEventOptions *option, int32_t value) | - | 设置预期更新间隔，单位为ms。定义了开发者期望的更新间隔。 |
| int32_t OH_ArkUI_VisibleAreaEventOptions_SetMeasureFromViewport(ArkUI_VisibleAreaEventOptions *option, bool measureFromViewport) | - | 设置可见区域计算模式。 |
| int32_t OH_ArkUI_VisibleAreaEventOptions_GetRatios(ArkUI_VisibleAreaEventOptions* option, float* value, int32_t* size) | - | 获取阈值数组。 |
| int32_t OH_ArkUI_VisibleAreaEventOptions_GetExpectedUpdateInterval(ArkUI_VisibleAreaEventOptions* option) | - | 获取预期更新间隔。 |
| bool OH_ArkUI_VisibleAreaEventOptions_GetMeasureFromViewport(ArkUI_VisibleAreaEventOptions* option) | - | 获取可见区域计算模式。 |
| ArkUI_TextPickerRangeContentArray* OH_ArkUI_TextPickerRangeContentArray_Create(int32_t length) | - | 创建TextPickerRangeContent数组的对象。 |
| void OH_ArkUI_TextPickerRangeContentArray_SetIconAtIndex(ArkUI_TextPickerRangeContentArray* handle, char* icon, int32_t index) | - | 指定TextPickerRangeContent数组指定位置的icon数据。 |
| void OH_ArkUI_TextPickerRangeContentArray_SetTextAtIndex(ArkUI_TextPickerRangeContentArray* handle, char* text, int32_t index) | - | 指定TextPickerRangeContent数组指定位置的text数据。 |
| void OH_ArkUI_TextPickerRangeContentArray_Destroy(ArkUI_TextPickerRangeContentArray* handle) | - | 删除TextPickerRangeContent数组对象。 |
| ArkUI_TextCascadePickerRangeContentArray* OH_ArkUI_TextCascadePickerRangeContentArray_Create(int32_t length) | - | 创建TextCascadePickerRangeContent数组对象。 |
| void OH_ArkUI_TextCascadePickerRangeContentArray_SetTextAtIndex (ArkUI_TextCascadePickerRangeContentArray* handle, char* text, int32_t index) | - | 指定TextCascadePickerRangeContent数组指定位置的text数据。 |
| void OH_ArkUI_TextCascadePickerRangeContentArray_SetChildAtIndex (ArkUI_TextCascadePickerRangeContentArray* handle, ArkUI_TextCascadePickerRangeContentArray* child, int32_t index) | - | 指定TextCascadePickerRangeContent数组指定位置的child数据。 |
| void OH_ArkUI_TextCascadePickerRangeContentArray_Destroy (ArkUI_TextCascadePickerRangeContentArray* handle) | - | 删除TextCascadePickerRangeContent数组对象。 |
| ArkUI_EmbeddedComponentOption* OH_ArkUI_EmbeddedComponentOption_Create() | - | 创建EmbeddedComponent组件选项的对象。 |
| void OH_ArkUI_EmbeddedComponentOption_Dispose(ArkUI_EmbeddedComponentOption* option) | - | 删除EmbeddedComponent组件选项的对象。 |
| void OH_ArkUI_EmbeddedComponentOption_SetOnError (ArkUI_EmbeddedComponentOption* option, void (*callback)(int32_t code, const char* name, const char* message)) | - | 设置EmbeddedComponent组件的onError回调。EmbeddedComponent组件在运行过程中发生异常时触发本回调。 |
| void OH_ArkUI_EmbeddedComponentOption_SetOnTerminated (ArkUI_EmbeddedComponentOption* option, void (*callback)(int32_t code, AbilityBase_Want* want)) | - | 设置EmbeddedComponent组件的onTerminated回调。EmbeddedComponent组件正常退出时触发本回调。 |
| ArkUI_PositionEdges* OH_ArkUI_PositionEdges_Create() | - | 创建PositionEdges属性对象。 |
| ArkUI_PositionEdges* OH_ArkUI_PositionEdges_Copy(const ArkUI_PositionEdges* edges) | - | 深拷贝PositionEdges属性对象。 |
| void OH_ArkUI_PositionEdges_Dispose(ArkUI_PositionEdges* edges) | - | 销毁PositionEdges属性对象。 |
| void OH_ArkUI_PositionEdges_SetTop(ArkUI_PositionEdges* edges, float value) | - | 设置PositionEdges属性对象的上方向值。 |
| int32_t OH_ArkUI_PositionEdges_GetTop(ArkUI_PositionEdges* edges, float* value) | - | 获取PositionEdges属性对象的上方向值。 |
| void OH_ArkUI_PositionEdges_SetLeft(ArkUI_PositionEdges* edges, float value) | - | 设置PositionEdges属性对象的左方向值。 |
| int32_t OH_ArkUI_PositionEdges_GetLeft(ArkUI_PositionEdges* edges, float* value) | - | 获取PositionEdges属性对象的左方向值。 |
| void OH_ArkUI_PositionEdges_SetBottom(ArkUI_PositionEdges* edges, float value) | - | 设置PositionEdges属性对象的下方向值。 |
| int32_t OH_ArkUI_PositionEdges_GetBottom(ArkUI_PositionEdges* edges, float* value) | - | 获取PositionEdges属性对象的下方向值。 |
| void OH_ArkUI_PositionEdges_SetRight(ArkUI_PositionEdges* edges, float value) | - | 设置PositionEdges属性对象的右方向值。 |
| int32_t OH_ArkUI_PositionEdges_GetRight(ArkUI_PositionEdges* edges, float* value) | - | 获取PositionEdges属性对象的右方向值。 |
| ArkUI_PixelRoundPolicy* OH_ArkUI_PixelRoundPolicy_Create() | - | 创建PixelRoundPolicy属性对象。 |
| void OH_ArkUI_PixelRoundPolicy_Dispose(ArkUI_PixelRoundPolicy* policy) | - | 释放PixelRoundPolicy属性对象。 |
| void OH_ArkUI_PixelRoundPolicy_SetTop(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value) | - | 设置PixelRoundPolicy属性对象的上部方向值。 |
| int32_t OH_ArkUI_PixelRoundPolicy_GetTop(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value) | - | 获取PixelRoundPolicy属性对象的上部方向值。 |
| void OH_ArkUI_PixelRoundPolicy_SetStart(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value) | - | 设置PixelRoundPolicy属性对象的前部方向值。 |
| int32_t OH_ArkUI_PixelRoundPolicy_GetStart(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value) | - | 获取PixelRoundPolicy属性对象的前部方向值。 |
| void OH_ArkUI_PixelRoundPolicy_SetBottom(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value) | - | 设置PixelRoundPolicy属性对象的下部方向值。 |
| int32_t OH_ArkUI_PixelRoundPolicy_GetBottom(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value) | - | 获取PixelRoundPolicy属性对象的下部方向值。 |
| void OH_ArkUI_PixelRoundPolicy_SetEnd(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value) | - | 设置PixelRoundPolicy属性对象的尾部方向值。 |
| int32_t OH_ArkUI_PixelRoundPolicy_GetEnd(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value) | - | 获取PixelRoundPolicy属性对象的尾部方向值。 |
| ArkUI_ContentTransitionEffect* OH_ArkUI_ContentTransitionEffect_Create(int32_t type) | - | 创建ContentTransitionEffect属性对象。 |
| ArkUI_GridLayoutOptions* OH_ArkUI_GridLayoutOptions_Create() | - | 创建Grid布局选项。 |
| void OH_ArkUI_GridLayoutOptions_Dispose(ArkUI_GridLayoutOptions* option) | - | 销毁Grid布局选项。 |
| int32_t OH_ArkUI_GridLayoutOptions_SetIrregularIndexes(ArkUI_GridLayoutOptions* option, uint32_t* irregularIndexes, int32_t size) | - | 设置Grid中不规则GridItem的索引数组。 |
| int32_t OH_ArkUI_GridLayoutOptions_GetIrregularIndexes(ArkUI_GridLayoutOptions* option, uint32_t* irregularIndexes, int32_t* size) | - | 获取Grid中不规则GridItem的索引数组。当不设置OH_ArkUI_GridLayoutOptions_RegisterGetIrregularSizeByIndexCallback时，irregularIndexes中GridItem的默认大小为垂直滚动Grid的一整行或水平滚动Grid的一整列。 |
| void OH_ArkUI_GridLayoutOptions_RegisterGetIrregularSizeByIndexCallback(ArkUI_GridLayoutOptions* option, void* userData, ArkUI_GridItemSize(*callback)(int32_t itemIndex, void* userData)) | - | Grid布局选项通过GridItem索引获取指定Item占用的行列数。 |
| void OH_ArkUI_GridLayoutOptions_RegisterGetRectByIndexCallback(ArkUI_GridLayoutOptions* option, void* userData, ArkUI_GridItemRect (*callback)(int32_t itemIndex, void* userData)) | - | Grid布局选项通过GridItem索引获取指定Item的起始行列和占用的行列数。 |
| ArkUI_SelectionOptions OH_ArkUI_SelectionOptions_Create() | - | 创建选择选项。 |
| void OH_ArkUI_SelectionOptions_Dispose(ArkUI_SelectionOptions* options) | - | 释放选择选项对象。 |
| void OH_ArkUI_SelectionOptions_SetMenuPolicy(ArkUI_SelectionOptions* options, ArkUI_MenuPolicy menuPolicy) | - | 设置选择选项的菜单弹出策略。 |
| ArkUI_MenuPolicy OH_ArkUI_SelectionOptions_GetMenuPolicy(ArkUI_SelectionOptions* options) | - | 获取选择选项的菜单弹出策略。 |
| ArkUI_TextContentBaseController* OH_ArkUI_TextContentBaseController_Create() | - | 创建文本内容基础控制器对象。 |
| void OH_ArkUI_TextContentBaseController_Dispose(ArkUI_TextContentBaseController* controller) | - | 销毁文本内容基础控制器对象。 |
| void OH_ArkUI_TextContentBaseController_DeleteBackward(ArkUI_TextContentBaseController* controller) | - | 在编辑态时删除光标前字符。其他状态删除输入框组件的最后一个字符。 |
| void OH_ArkUI_TextContentBaseController_ScrollToVisible(ArkUI_TextContentBaseController* controller, int32_t start, int32_t end) | - | 将起始索引与结束索引传递给与其绑定的输入框组件，并将此范围内的文字滚动到可视区域。 |
| ArkUI_TextMenuItem* OH_ArkUI_TextMenuItem_Create() | - | 创建文本菜单项对象。 |
| void OH_ArkUI_TextMenuItem_Dispose(ArkUI_TextMenuItem* textMenuItem) | - | 释放文本菜单项对象。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItem_SetContent(ArkUI_TextMenuItem* item, const char* content) | - | 设置文本菜单项标题。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItem_GetContent(const ArkUI_TextMenuItem* item, char* buffer, int32_t bufferSize, int32_t* writeLength) | - | 获取文本菜单项标题。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItem_SetIcon(ArkUI_TextMenuItem* item, const char* icon) | - | 设置文本菜单项图标路径。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItem_GetIcon(const ArkUI_TextMenuItem* item, char* buffer, int32_t bufferSize, int32_t* writeLength) | - | 获取文本菜单项图标路径。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItem_SetLabelInfo(ArkUI_TextMenuItem* item, const char* labelInfo) | - | 设置文本菜单项快捷键提示，例如“复制”菜单项的快捷键提示可以设置为“Ctrl+C”。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItem_GetLabelInfo(const ArkUI_TextMenuItem* item, char* buffer, int32_t bufferSize, int32_t* writeLength) | - | 获取文本菜单项快捷键提示，例如“复制”菜单项的快捷键提示一般为“Ctrl+C”。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItem_SetId(ArkUI_TextMenuItem* item, int32_t id) | - | 设置文本菜单项id。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItem_GetId(const ArkUI_TextMenuItem* item, int32_t* id) | - | 获取文本菜单项id。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_GetSize(ArkUI_TextMenuItemArray* items, int32_t* size) | - | 获取文本菜单项数组大小。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_GetItem(ArkUI_TextMenuItemArray* items, int32_t index, ArkUI_TextMenuItem** item) | - | 获取文本菜单项数组中指定索引位置的文本菜单项。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_Insert(ArkUI_TextMenuItemArray* items, ArkUI_TextMenuItem* item, int32_t index) | - | 在文本菜单项数组中指定索引位置插入一个文本菜单项。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_Erase(ArkUI_TextMenuItemArray* items, int32_t index) | - | 删除文本菜单项数组中指定索引位置的文本菜单项。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_Clear(ArkUI_TextMenuItemArray* items) | - | 清除文本菜单项数组中所有的文本菜单项。 |
| ArkUI_TextEditMenuOptions* OH_ArkUI_TextEditMenuOptions_Create() | - | 创建文本菜单扩展项对象。 |
| void OH_ArkUI_TextEditMenuOptions_Dispose(ArkUI_TextEditMenuOptions* editMenuOptions) | - | 释放文本菜单扩展项对象。 |
| typedef void (*ArkUI_TextCreateMenuCallback)(ArkUI_TextMenuItemArray* items, void* userData) | ArkUI_TextCreateMenuCallback | 文本菜单创建事件回调函数，在文本菜单创建时会触发此回调函数，开发者可在此函数中设置菜单数据。 |
| typedef void (*ArkUI_TextPrepareMenuCallback)(ArkUI_TextMenuItemArray* items, void* userData) | ArkUI_TextPrepareMenuCallback | 文本菜单准备事件回调函数，当文本选择区域变化后显示菜单之前会触发此回调函数，开发者可在此函数中配置菜单数据。 |
| typedef bool (*ArkUI_TextMenuItemClickCallback)(const ArkUI_TextMenuItem* item,int32_t start, int32_t end, void* userData) | ArkUI_TextMenuItemClickCallback | 文本菜单项点击事件回调函数，在菜单项被点击时触发此回调函数，开发者可在此函数中对系统默认处理行为进行拦截。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditMenuOptions_RegisterOnCreateMenuCallback(ArkUI_TextEditMenuOptions* editMenuOptions, void* userData, ArkUI_TextCreateMenuCallback cb) | - | 注册文本菜单创建事件回调函数。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditMenuOptions_RegisterOnPrepareMenuCallback(ArkUI_TextEditMenuOptions* editMenuOptions, void* userData, ArkUI_TextPrepareMenuCallback cb) | - | 注册文本菜单准备事件回调函数。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditMenuOptions_RegisterOnMenuItemClickCallback(ArkUI_TextEditMenuOptions* editMenuOptions, void* userData, ArkUI_TextMenuItemClickCallback cb) | - | 注册文本菜单项点击事件回调函数。 |
| ArkUI_TextSelectionMenuOptions* OH_ArkUI_TextSelectionMenuOptions_Create() | - | 创建自定义文本选择菜单对象。 |
| void OH_ArkUI_TextSelectionMenuOptions_Dispose(ArkUI_TextSelectionMenuOptions* selectionMenuOptions) | - | 释放自定义文本选择菜单对象。 |
| ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_SetSpanType(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_TextSpanType textSpanType) | - | 设置自定义文本选择菜单的文本识别类型。 |
| ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_GetSpanType(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_TextSpanType* spanType) | - | 获取自定义文本选择菜单的文本识别类型。 |
| ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_SetContentNode(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_NodeHandle node) | - | 设置自定义文本选择菜单的内容节点。 |
| ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_GetContentNode(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_NodeHandle* node) | - | 获取自定义文本选择菜单的内容节点。 |
| ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_SetResponseType(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_TextResponseType responseType) | - | 设置自定义文本选择菜单的响应类型。 |
| ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_GetResponseType(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_TextResponseType* responseType) | - | 获取自定义文本选择菜单的响应类型。 |
| ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_RegisterOnMenuShowCallback(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, void* userData, void (*callback)(int32_t start, int32_t end, void* userData)) | - | 注册自定义文本选择菜单显示事件回调。 |
| ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_RegisterOnMenuHideCallback(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, void* userData, void (*callback)(int32_t start, int32_t end, void* userData)) | - | 注册自定义文本选择菜单隐藏事件回调。 |
| ArkUI_TextMarqueeOptions* OH_ArkUI_TextMarqueeOptions_Create() | - | 创建文本跑马灯模式配置项。 |
| void OH_ArkUI_TextMarqueeOptions_Dispose(ArkUI_TextMarqueeOptions* option) | - | 销毁文本跑马灯模式配置项指针。 |
| void OH_ArkUI_TextMarqueeOptions_SetStart(ArkUI_TextMarqueeOptions* option, bool start) | - | 设置文本跑马灯模式配置项是否播放。 |
| bool OH_ArkUI_TextMarqueeOptions_GetStart(ArkUI_TextMarqueeOptions* option) | - | 获取文本跑马灯模式配置项是否播放。 |
| void OH_ArkUI_TextMarqueeOptions_SetStep(ArkUI_TextMarqueeOptions* option, float step) | - | 设置文本跑马灯模式配置项的步长。 |
| float OH_ArkUI_TextMarqueeOptions_GetStep(ArkUI_TextMarqueeOptions* option) | - | 获取文本跑马灯模式配置项的步长。 |
| void OH_ArkUI_TextMarqueeOptions_SetSpacing(ArkUI_TextMarqueeOptions* option, float spacing) | - | 设置文本跑马灯模式配置项的首尾间距。 |
| float OH_ArkUI_TextMarqueeOptions_GetSpacing(ArkUI_TextMarqueeOptions* option) | - | 获取文本跑马灯模式配置项的首尾间距。 |
| void OH_ArkUI_TextMarqueeOptions_SetLoop(ArkUI_TextMarqueeOptions* option, int32_t loop) | - | 设置文本跑马灯模式配置项的重复滚动的次数，小于等于零时无限循环。 |
| int32_t OH_ArkUI_TextMarqueeOptions_GetLoop(ArkUI_TextMarqueeOptions* option) | - | 获取文本跑马灯模式配置项的重复滚动的次数。 |
| void OH_ArkUI_TextMarqueeOptions_SetFromStart(ArkUI_TextMarqueeOptions* option, bool fromStart) | - | 设置文本跑马灯模式配置项的运行方向。 |
| bool OH_ArkUI_TextMarqueeOptions_GetFromStart(ArkUI_TextMarqueeOptions* option) | - | 获取文本跑马灯模式配置项的运行方向。 |
| void OH_ArkUI_TextMarqueeOptions_SetDelay(ArkUI_TextMarqueeOptions* option, int32_t delay) | - | 设置文本跑马灯模式配置项的每轮滚动延迟时间。 |
| int32_t OH_ArkUI_TextMarqueeOptions_GetDelay(ArkUI_TextMarqueeOptions* option) | - | 获取文本跑马灯模式配置项的每轮滚动延迟时间。 |
| void OH_ArkUI_TextMarqueeOptions_SetFadeout(ArkUI_TextMarqueeOptions* option, bool fadeout) | - | 设置文本跑马灯模式配置项是否支持文字超长时的渐隐效果。当Text内容超出显示范围时，未完全展现的文字边缘将应用渐隐效果。若两端均有文字未完全显示，则两端同时应用渐隐效果。在渐隐效果开启状态下，NODE_CLIP属性将自动锁定为true，不允许设置为false。 |
| bool OH_ArkUI_TextMarqueeOptions_GetFadeout(ArkUI_TextMarqueeOptions* option) | - | 获取文本跑马灯模式配置项是否支持文字超长时的渐隐效果。 |
| void OH_ArkUI_TextMarqueeOptions_SetStartPolicy(ArkUI_TextMarqueeOptions* option, ArkUI_MarqueeStartPolicy startPolicy) | - | 设置文本跑马灯模式配置项的启动策略。 |
| ArkUI_MarqueeStartPolicy OH_ArkUI_TextMarqueeOptions_GetStartPolicy(ArkUI_TextMarqueeOptions* option) | - | 获取文本跑马灯模式配置项的启动策略。 |
| void OH_ArkUI_TextMarqueeOptions_SetUpdatePolicy(ArkUI_TextMarqueeOptions* option, ArkUI_MarqueeUpdatePolicy updatePolicy) | - | 设置文本跑马灯模式配置项的更新策略。 |
| ArkUI_MarqueeUpdatePolicy OH_ArkUI_TextMarqueeOptions_GetUpdatePolicy(ArkUI_TextMarqueeOptions* option) | - | 获取文本跑马灯模式配置项的更新策略。 |
| ArkUI_PickerIndicatorStyle OH_ArkUI_PickerIndicatorStyle_Create(ArkUI_PickerIndicatorType type) | ArkUI_PickerIndicatorStyle | 创建选中项指示器的样式实例。 |
| void OH_ArkUI_PickerIndicatorStyle_Dispose(ArkUI_PickerIndicatorStyle* style) | - | 销毁选中项指示器的样式实例。 |
| ArkUI_ErrorCode OH_ArkUI_PickerIndicatorStyle_ConfigureBackground(ArkUI_PickerIndicatorStyle* style, ArkUI_PickerIndicatorBackground* background) | - | 设置背景样式参数，此接口仅当选择器选中项样式枚举类型为ARKUI_PICKER_INDICATOR_BACKGROUND时生效。 |
| ArkUI_ErrorCode OH_ArkUI_PickerIndicatorStyle_ConfigureDivider(ArkUI_PickerIndicatorStyle* style, ArkUI_PickerIndicatorDivider* divider) | - | 设置分割线样式参数，此接口仅当选择器选中项样式枚举类型为ARKUI_PICKER_INDICATOR_DIVIDER时生效。 |

**枚举类型说明**

**ArkUI_Alignment**

```ets
enum ArkUI_Alignment
```

描述：

定义布局对齐枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ALIGNMENT_TOP_START = 0 | 顶部起始，该值为默认值。 |
| ARKUI_ALIGNMENT_TOP = 1 | 顶部居中。 |
| ARKUI_ALIGNMENT_TOP_END = 2 | 顶部尾端。 |
| ARKUI_ALIGNMENT_START = 3 | 起始端纵向居中。 |
| ARKUI_ALIGNMENT_CENTER = 4 | 横向和纵向居中。 |
| ARKUI_ALIGNMENT_END = 5 | 尾端纵向居中。 |
| ARKUI_ALIGNMENT_BOTTOM_START = 6 | 底部起始端。 |
| ARKUI_ALIGNMENT_BOTTOM = 7 | 底部横向居中。 |
| ARKUI_ALIGNMENT_BOTTOM_END = 8 | 底部尾端。 |

**ArkUI_ImageRepeat**

```ets
enum ArkUI_ImageRepeat
```

描述：

定义图片重复铺设枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_IMAGE_REPEAT_NONE = 0 | 不重复。 |
| ARKUI_IMAGE_REPEAT_X = 1 | 在X轴方向重复。 |
| ARKUI_IMAGE_REPEAT_Y = 2 | 在Y轴方向重复。 |
| ARKUI_IMAGE_REPEAT_XY = 3 | 在X轴和Y轴方向重复。 |

**ArkUI_FontStyle**

```ets
enum ArkUI_FontStyle
```

描述：

定义字体样式枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_FONT_STYLE_NORMAL = 0 | 标准字体样式。 |
| ARKUI_FONT_STYLE_ITALIC = 1 | 斜体字体样式。 |

**ArkUI_FontWeight**

```ets
enum ArkUI_FontWeight
```

描述：

定义字体粗细/字重枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_FONT_WEIGHT_W100 = 0 | 100 |
| ARKUI_FONT_WEIGHT_W200 = 1 | 200 |
| ARKUI_FONT_WEIGHT_W300 = 2 | 300 |
| ARKUI_FONT_WEIGHT_W400 = 3 | 400 |
| ARKUI_FONT_WEIGHT_W500 = 4 | 500 |
| ARKUI_FONT_WEIGHT_W600 = 5 | 600 |
| ARKUI_FONT_WEIGHT_W700 = 6 | 700 |
| ARKUI_FONT_WEIGHT_W800 = 7 | 800 |
| ARKUI_FONT_WEIGHT_W900 = 8 | 900 |
| ARKUI_FONT_WEIGHT_BOLD = 9 | 字体较粗。 |
| ARKUI_FONT_WEIGHT_NORMAL = 10 | 字体粗细正常。 |
| ARKUI_FONT_WEIGHT_BOLDER = 11 | 字体非常粗。 |
| ARKUI_FONT_WEIGHT_LIGHTER = 12 | 字体较细。 |
| ARKUI_FONT_WEIGHT_MEDIUM = 13 | 字体粗细适中。 |
| ARKUI_FONT_WEIGHT_REGULAR = 14 | 字体粗细正常。 |

**ArkUI_TextAlignment**

```ets
enum ArkUI_TextAlignment
```

描述：

定义字体水平对齐样式枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_TEXT_ALIGNMENT_START = 0 | 水平对齐首部。 |
| ARKUI_TEXT_ALIGNMENT_CENTER = 1 | 水平居中对齐。 |
| ARKUI_TEXT_ALIGNMENT_END = 2 | 水平对齐尾部。 |
| ARKUI_TEXT_ALIGNMENT_JUSTIFY = 3 | 双端对齐。 |
| ARKUI_TEXT_ALIGNMENT_LEFT_TO_RIGHT = 4 | 从左到右对齐。 起始版本： 23 |
| ARKUI_TEXT_ALIGNMENT_RIGHT_TO_LEFT = 5 | 从右到左对齐。 起始版本： 23 |

**ArkUI_TextVerticalAlignment**

```ets
enum ArkUI_TextVerticalAlignment
```

描述：

定义文本垂直对齐样式枚举值。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_TEXT_VERTICAL_ALIGNMENT_BASELINE = 0 | 基线对齐。 |
| ARKUI_TEXT_VERTICAL_ALIGNMENT_BOTTOM = 1 | 底部对齐。 |
| ARKUI_TEXT_VERTICAL_ALIGNMENT_CENTER = 2 | 居中对齐。 |
| ARKUI_TEXT_VERTICAL_ALIGNMENT_TOP = 3 | 顶部对齐。 |

**ArkUI_TextContentAlign**

```ets
enum ArkUI_TextContentAlign
```

描述：

定义文本内容区垂直对齐样式枚举值。

起始版本： 21

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_TEXT_CONTENT_ALIGN_TOP = 0 | 顶部对齐。 |
| ARKUI_TEXT_CONTENT_ALIGN_CENTER = 1 | 居中对齐。 |
| ARKUI_TEXT_CONTENT_ALIGN_BOTTOM = 2 | 底部对齐。 |

**ArkUI_TextDirection**

```ets
enum ArkUI_TextDirection
```

描述：

定义文本排版方向枚举值。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_TEXT_DIRECTION_LTR = 0 | 文本排版方向从左到右。 |
| ARKUI_TEXT_DIRECTION_RTL = 1 | 文本排版方向从右到左。 |
| ARKUI_TEXT_DIRECTION_DEFAULT = 2 | 文本排版方向遵循组件布局。 |
| ARKUI_TEXT_DIRECTION_AUTO = 3 | 遵循自身实际文本内容的排版方向，如果文本为 RTL（Right-to-Left）类语言（如藏文、维吾尔文），文本排版方向为从右到左。如果为 LTR（Left-to-Right）类语言（如中文、英文），文本排版方向为从左到右。 |

**ArkUI_EnterKeyType**

```ets
enum ArkUI_EnterKeyType
```

描述：

定义单行文本输入法回车键类型枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ENTER_KEY_TYPE_GO = 2 | 显示为开始样式。 |
| ARKUI_ENTER_KEY_TYPE_SEARCH = 3 | 显示为搜索样式。 |
| ARKUI_ENTER_KEY_TYPE_SEND = 4 | 显示为发送样式。 |
| ARKUI_ENTER_KEY_TYPE_NEXT = 5 | 显示为下一个样式。 |
| ARKUI_ENTER_KEY_TYPE_DONE = 6 | 显示为完成样式。 |
| ARKUI_ENTER_KEY_TYPE_PREVIOUS = 7 | 显示为上一个样式。 |
| ARKUI_ENTER_KEY_TYPE_NEW_LINE = 8 | 显示为换行样式。 |

**ArkUI_TextInputType**

```ets
enum ArkUI_TextInputType
```

描述：

定义单行文本输入法类型枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_TEXTINPUT_TYPE_NORMAL = 0 | 基本输入模式。 |
| ARKUI_TEXTINPUT_TYPE_NUMBER = 2 | 纯数字模式。 |
| ARKUI_TEXTINPUT_TYPE_PHONE_NUMBER = 3 | 电话号码输入模式。 |
| ARKUI_TEXTINPUT_TYPE_EMAIL = 5 | 邮箱地址输入模式。 |
| ARKUI_TEXTINPUT_TYPE_PASSWORD = 7 | 密码输入模式。 |
| ARKUI_TEXTINPUT_TYPE_NUMBER_PASSWORD = 8 | 纯数字密码输入模式。 |
| ARKUI_TEXTINPUT_TYPE_SCREEN_LOCK_PASSWORD = 9 | 锁屏应用密码输入模式。 |
| ARKUI_TEXTINPUT_TYPE_USER_NAME = 10 | 用户名输入模式。 |
| ARKUI_TEXTINPUT_TYPE_NEW_PASSWORD = 11 | 新密码输入模式。 |
| ARKUI_TEXTINPUT_TYPE_NUMBER_DECIMAL = 12 | 带小数点的数字输入模式。 |
| ARKUI_TEXTINPUT_TYPE_ONE_TIME_CODE = 14 | 验证码输入模式。 起始版本： 20 |

**ArkUI_TextAreaType**

```ets
enum ArkUI_TextAreaType
```

描述：

定义多行文本输入法类型枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_TEXTAREA_TYPE_NORMAL = 0 | 基本输入模式。 |
| ARKUI_TEXTAREA_TYPE_NUMBER = 2 | 纯数字模式。 |
| ARKUI_TEXTAREA_TYPE_PHONE_NUMBER = 3 | 电话号码输入模式。 |
| ARKUI_TEXTAREA_TYPE_EMAIL = 5 | 邮箱地址输入模式。 |
| ARKUI_TEXTAREA_TYPE_ONE_TIME_CODE = 14 | 验证码输入模式。 起始版本： 20 |

**ArkUI_CancelButtonStyle**

```ets
enum ArkUI_CancelButtonStyle
```

描述：

定义清除按钮样式枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_CANCELBUTTON_STYLE_CONSTANT = 0 | 清除按钮常显样式。 |
| ARKUI_CANCELBUTTON_STYLE_INVISIBLE = 1 | 清除按钮常隐样式。 |
| ARKUI_CANCELBUTTON_STYLE_INPUT = 2 | 清除按钮输入样式。 |

**ArkUI_XComponentType**

```ets
enum ArkUI_XComponentType
```

描述：

定义XComponent类型枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_XCOMPONENT_TYPE_SURFACE = 0 | 用于EGL/OpenGLES和媒体数据写入，开发者定制绘制内容单独显示在屏幕上。 |
| ARKUI_XCOMPONENT_TYPE_TEXTURE = 2 | 用于EGL/OpenGLES和媒体数据写入，开发者定制绘制内容和XComponent组件内容合成后展示在屏幕上。 |

**ArkUI_ProgressType**

```ets
enum ArkUI_ProgressType
```

描述：

定义进度条类型枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_PROGRESS_TYPE_LINEAR = 0 | 线性样式。 |
| ARKUI_PROGRESS_TYPE_RING = 1 | 环形无刻度样式。 |
| ARKUI_PROGRESS_TYPE_ECLIPSE = 2 | 圆形样式。 |
| ARKUI_PROGRESS_TYPE_SCALE_RING = 3 | 环形有刻度样式。 |
| ARKUI_PROGRESS_TYPE_CAPSULE = 4 | 胶囊样式。 |

**ArkUI_TextDecorationType**

```ets
enum ArkUI_TextDecorationType
```

描述：

定义装饰线类型枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_TEXT_DECORATION_TYPE_NONE = 0 | 不使用装饰线。 |
| ARKUI_TEXT_DECORATION_TYPE_UNDERLINE = 1 | 文字下划线修饰。 |
| ARKUI_TEXT_DECORATION_TYPE_OVERLINE = 2 | 文字上划线修饰。 |
| ARKUI_TEXT_DECORATION_TYPE_LINE_THROUGH = 3 | 穿过文本的修饰线。 |

**ArkUI_TextDecorationStyle**

```ets
enum ArkUI_TextDecorationStyle
```

描述：

定义装饰线样式枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_TEXT_DECORATION_STYLE_SOLID = 0 | 单实线。 |
| ARKUI_TEXT_DECORATION_STYLE_DOUBLE = 1 | 双实线。 |
| ARKUI_TEXT_DECORATION_STYLE_DOTTED = 2 | 点线。 |
| ARKUI_TEXT_DECORATION_STYLE_DASHED = 3 | 虚线。 |
| ARKUI_TEXT_DECORATION_STYLE_WAVY = 4 | 波浪线。 |

**ArkUI_TextCase**

```ets
enum ArkUI_TextCase
```

描述：

定义文本大小写枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_TEXT_CASE_NORMAL = 0 | 保持原有大小写。 |
| ARKUI_TEXT_CASE_LOWER = 1 | 文本全小写。 |
| ARKUI_TEXT_CASE_UPPER = 2 | 文本全大写。 |

**ArkUI_CopyOptions**

```ets
enum ArkUI_CopyOptions
```

描述：

定义文本复制粘贴模式枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_COPY_OPTIONS_NONE = 0 | 不支持复制。 |
| ARKUI_COPY_OPTIONS_IN_APP = 1 | 支持应用内复制。 |
| ARKUI_COPY_OPTIONS_LOCAL_DEVICE = 2 | 支持设备内复制。 |
| ARKUI_COPY_OPTIONS_CROSS_DEVICE = 3 | 支持跨设备复制。 |

**ArkUI_ShadowType**

```ets
enum ArkUI_ShadowType
```

描述：

定义阴影类型枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SHADOW_TYPE_COLOR = 0 | 颜色。 |
| ARKUI_SHADOW_TYPE_BLUR = 1 | 模糊。 |

**ArkUI_DatePickerMode**

```ets
enum ArkUI_DatePickerMode
```

描述：

定义日期选择器列显示模式的枚举值。

起始版本： 18

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_DATEPICKER_MODE_DATE = 0 | 默认值。日期列显示年、月、日三列。 |
| ARKUI_DATEPICKER_YEAR_AND_MONTH = 1 | 日期列显示年、月二列。 |
| ARKUI_DATEPICKER_MONTH_AND_DAY = 2 | 日期列显示月、日二列。 |

**ArkUI_TextPickerRangeType**

```ets
enum ArkUI_TextPickerRangeType
```

描述：

定义滑动选择文本选择器输入类型。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_TEXTPICKER_RANGETYPE_SINGLE = 0 | 单列数据选择器。 |
| ARKUI_TEXTPICKER_RANGETYPE_MULTI = 1 | 多列数据选择器。 |
| ARKUI_TEXTPICKER_RANGETYPE_RANGE_CONTENT = 2 | 支持图片资源的单列数据选择器。 |
| ARKUI_TEXTPICKER_RANGETYPE_CASCADE_RANGE_CONTENT = 3 | 支持联动的多列数据选择器。 |

**ArkUI_AccessibilityCheckedState**

```ets
enum ArkUI_AccessibilityCheckedState
```

描述：

定义无障碍复选框状态类型枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ACCESSIBILITY_UNCHECKED = 0 | 复选框未被选中。 |
| ARKUI_ACCESSIBILITY_CHECKED = 1 | 复选框被选中。 |

**ArkUI_AccessibilityActionType**

```ets
enum ArkUI_AccessibilityActionType
```

描述：

定义无障碍操作类型。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ACCESSIBILITY_ACTION_CLICK = 1 << 0 | 点击操作。 |
| ARKUI_ACCESSIBILITY_ACTION_LONG_CLICK = 1 << 1 | 长按操作。 |
| ARKUI_ACCESSIBILITY_ACTION_CUT = 1 << 2 | 剪切操作。 |
| ARKUI_ACCESSIBILITY_ACTION_COPY = 1 << 3 | 复制操作。 |
| ARKUI_ACCESSIBILITY_ACTION_PASTE = 1 << 4 | 粘贴操作。 |

**ArkUI_EdgeEffect**

```ets
enum ArkUI_EdgeEffect
```

描述：

定义边缘滑动效果枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_EDGE_EFFECT_SPRING = 0 | 弹性物理动效，滑动到边缘后可以根据初始速度或通过触摸事件继续滑动一段距离，松手后回弹。 |
| ARKUI_EDGE_EFFECT_FADE = 1 | 阴影效果，滑动到边缘后会有圆弧状的阴影。 |
| ARKUI_EDGE_EFFECT_NONE = 2 | 滑动到边缘后无效果。 |

**ArkUI_BarState**

```ets
enum ArkUI_BarState
```

描述：

定义文本控制滚动条状态枚举值。

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_BAR_STATE_OFF = 0 | 不显示。 |
| ARKUI_BAR_STATE_AUTO = 1 | 按需显示。 |
| ARKUI_BAR_STATE_ON = 2 | 常驻显示。 |

**ArkUI_EffectEdge**

```ets
enum ArkUI_EffectEdge
```

描述：

定义边缘效果生效边缘的方向枚举值。

起始版本： 18

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_EFFECT_EDGE_START = 1 | 起始边生效。 |
| ARKUI_EFFECT_EDGE_END = 2 | 末尾边生效。 |

**ArkUI_ScrollDirection**

```ets
enum ArkUI_ScrollDirection
```

描述：

定义Scroll组件排列方向枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SCROLL_DIRECTION_VERTICAL = 0 | 仅支持竖直方向滚动。 |
| ARKUI_SCROLL_DIRECTION_HORIZONTAL = 1 | 仅支持水平方向滚动。 |
| ARKUI_SCROLL_DIRECTION_NONE = 3 | 禁止滚动。 |
| ARKUI_SCROLL_DIRECTION_FREE = 4 | 自由滚动。 起始版本： 20 |

**ArkUI_ScrollSnapAlign**

```ets
enum ArkUI_ScrollSnapAlign
```

描述：

定义列表项滚动结束对齐效果枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SCROLL_SNAP_ALIGN_NONE = 0 | 默认无项目滚动对齐效果。 |
| ARKUI_SCROLL_SNAP_ALIGN_START = 1 | 视图中的第一项将在列表的开头对齐。 |
| ARKUI_SCROLL_SNAP_ALIGN_CENTER = 2 | 视图中的中间项将在列表中心对齐。 |
| ARKUI_SCROLL_SNAP_ALIGN_END = 3 | 视图中的最后一项将在列表末尾对齐。 |

**ArkUI_ScrollBarDisplayMode**

```ets
enum ArkUI_ScrollBarDisplayMode
```

描述：

定义滚动条状态枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SCROLL_BAR_DISPLAY_MODE_OFF = 0 | 不显示。 |
| ARKUI_SCROLL_BAR_DISPLAY_MODE_AUTO = 1 | 按需显示(触摸时显示，2s后消失)。 |
| ARKUI_SCROLL_BAR_DISPLAY_MODE_ON = 2 | 常驻显示。 |

**ArkUI_Axis**

```ets
enum ArkUI_Axis
```

描述：

定义滚动方向和[List](List.md)组件排列方向枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_AXIS_VERTICAL = 0 | 仅支持竖直方向滚动，该值为默认值。 |
| ARKUI_AXIS_HORIZONTAL = 1 | 仅支持水平方向滚动。 |

**ArkUI_StickyStyle**

```ets
enum ArkUI_StickyStyle
```

描述：

定义列表是否吸顶和吸底枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_STICKY_STYLE_NONE = 0 | ListItemGroup的header不吸顶，footer不吸底。 |
| ARKUI_STICKY_STYLE_HEADER = 1 | ListItemGroup的header吸顶，footer不吸底。 |
| ARKUI_STICKY_STYLE_FOOTER = 2 | ListItemGroup的header不吸顶，footer吸底。 |
| ARKUI_STICKY_STYLE_BOTH = 3 | ListItemGroup的header吸顶，footer吸底。 |

**ArkUI_ContentClipMode**

```ets
enum ArkUI_ContentClipMode
```

描述：

定义滚动容器的内容层裁剪区域枚举值。

起始版本： 18

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_CONTENT_CLIP_MODE_CONTENT_ONLY = 0 | 按内容区裁剪。 |
| ARKUI_CONTENT_CLIP_MODE_BOUNDARY = 1 | 按组件区域裁剪。 |
| ARKUI_CONTENT_CLIP_MODE_SAFE_AREA = 2 | 按组件配置的SafeArea区域裁剪。 |

**ArkUI_WaterFlowLayoutMode**

```ets
enum ArkUI_WaterFlowLayoutMode
```

描述：

定义WaterFlow组件布局模式枚举值。

起始版本： 18

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_WATER_FLOW_LAYOUT_MODE_ALWAYS_TOP_DOWN = 0 | 从上到下布局。列数切换场景需要从第一个FlowItem开始布局到当前显示的FlowItem。 |
| ARKUI_WATER_FLOW_LAYOUT_MODE_SLIDING_WINDOW = 1 | 移动窗口布局。列数切换场景只重新布局当前显示范围到FlowItem，手指向下滑动再布局从上方进入显示范围的FlowItem。 |

**ArkUI_BorderStyle**

```ets
enum ArkUI_BorderStyle
```

描述：

边框线条样式枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_BORDER_STYLE_SOLID = 0 | 显示为一条实线，该值为默认值。 |
| ARKUI_BORDER_STYLE_DASHED = 1 | 显示为一系列短的方形虚线。 |
| ARKUI_BORDER_STYLE_DOTTED = 2 | 显示为一系列圆点。 |

**ArkUI_HitTestMode**

```ets
enum ArkUI_HitTestMode
```

描述：

触摸测试控制枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_HIT_TEST_MODE_DEFAULT = 0 | 默认触摸测试效果。自身及子节点响应触摸测试，但阻塞兄弟节点的触摸测试，不影响祖先节点的触摸测试。 |
| ARKUI_HIT_TEST_MODE_BLOCK = 1 | 自身响应触摸测试，阻塞子节点、兄弟节点和祖先节点的触摸测试。 |
| ARKUI_HIT_TEST_MODE_TRANSPARENT = 2 | 自身和子节点都响应触摸测试，不会阻塞兄弟节点和祖先节点的触摸测试。 |
| ARKUI_HIT_TEST_MODE_NONE = 3 | 自身不响应触摸测试，不会阻塞子节点、兄弟节点和祖先节点的触摸测试。 |
| ARKUI_HIT_TEST_MODE_BLOCK_HIERARCHY = 4 | 自身和子节点响应触摸测试，阻止所有优先级较低的兄弟节点和父节点参与触摸测试。 起始版本： 20 |
| ARKUI_HIT_TEST_MODE_BLOCK_DESCENDANTS = 5 | 自身不响应触摸测试，并且所有的后代（孩子，孙子等）也不响应触摸测试，不会影响祖先节点的触摸测试。 起始版本： 20 |

**ArkUI_ShadowStyle**

```ets
enum ArkUI_ShadowStyle
```

描述：

阴影效果枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SHADOW_STYLE_OUTER_DEFAULT_XS = 0 | 超小阴影。 |
| ARKUI_SHADOW_STYLE_OUTER_DEFAULT_SM = 1 | 小阴影。 |
| ARKUI_SHADOW_STYLE_OUTER_DEFAULT_MD = 2 | 中阴影。 |
| ARKUI_SHADOW_STYLE_OUTER_DEFAULT_LG = 3 | 大阴影。 |
| ARKUI_SHADOW_STYLE_OUTER_FLOATING_SM = 4 | 浮动小阴影。 |
| ARKUI_SHADOW_STYLE_OUTER_FLOATING_MD = 5 | 浮动中阴影。 |

**ArkUI_AnimationCurve**

```ets
enum ArkUI_AnimationCurve
```

描述：

动画曲线枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_CURVE_LINEAR = 0 | 动画从头到尾的速度都是相同。 |
| ARKUI_CURVE_EASE = 1 | 动画以低速开始，然后加快，在结束前变慢。 |
| ARKUI_CURVE_EASE_IN = 2 | 动画以低速开始。 |
| ARKUI_CURVE_EASE_OUT = 3 | 动画以低速结束。 |
| ARKUI_CURVE_EASE_IN_OUT = 4 | 动画以低速开始和结束。 |
| ARKUI_CURVE_FAST_OUT_SLOW_IN = 5 | 动画标准曲线。 |
| ARKUI_CURVE_LINEAR_OUT_SLOW_IN = 6 | 动画减速曲线。 |
| ARKUI_CURVE_FAST_OUT_LINEAR_IN = 7 | 动画加速曲线。 |
| ARKUI_CURVE_EXTREME_DECELERATION = 8 | 动画急缓曲线。 |
| ARKUI_CURVE_SHARP = 9 | 动画锐利曲线。 |
| ARKUI_CURVE_RHYTHM = 10 | 动画节奏曲线。 |
| ARKUI_CURVE_SMOOTH = 11 | 动画平滑曲线。 |
| ARKUI_CURVE_FRICTION = 12 | 动画阻尼曲线。 |

**ArkUI_SwiperArrow**

```ets
enum ArkUI_SwiperArrow
```

描述：

Swiper导航点箭头枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SWIPER_ARROW_HIDE = 0 | 不显示swiper中导航点箭头。 |
| ARKUI_SWIPER_ARROW_SHOW = 1 | 显示swiper中导航点箭头。 |
| ARKUI_SWIPER_ARROW_SHOW_ON_HOVER = 2 | 在鼠标悬浮状态下显示swiper的导航点箭头。 |

**ArkUI_SwiperNestedScrollMode**

```ets
enum ArkUI_SwiperNestedScrollMode
```

描述：

Swiper组件和父组件的嵌套滚动模式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SWIPER_NESTED_SRCOLL_SELF_ONLY = 0 | Swiper只自身滚动，不与父组件联动。 |
| ARKUI_SWIPER_NESTED_SRCOLL_SELF_FIRST = 1 | Swiper自身先滚动，自身滚动到边缘以后父组件滚动。父组件滚动到边缘以后，如果父组件有边缘效果，则父组件触发边缘效果，否则Swiper触发边缘效果。 |

**ArkUI_PageFlipMode**

```ets
enum ArkUI_PageFlipMode
```

描述：

[Swiper](Swiper.md)组件鼠标滚轮翻页模式。

起始版本： 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_PAGE_FLIP_MODE_CONTINUOUS = 0 | 连续翻页模式，鼠标滚轮连续滚动时翻多页。 |
| ARKUI_PAGE_FLIP_MODE_SINGLE = 1 | 一次翻页动画结束前不响应其他鼠标滚轮事件。 |

**ArkUI_SwiperAnimationMode**

```ets
enum ArkUI_SwiperAnimationMode
```

描述：

Swiper组件跳转到目标页面的动画模式。

起始版本： 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SWIPER_NO_ANIMATION = 0 | 无动画跳转到目标页面。 |
| ARKUI_SWIPER_DEFAULT_ANIMATION = 1 | 做动画跳转到目标页面。 |
| ARKUI_SWIPER_FAST_ANIMATION = 2 | 先无动画跳转到目标附近再做动画跳转到目标页面。 |

**ArkUI_AccessibilityMode**

```ets
enum ArkUI_AccessibilityMode
```

描述：

定义无障碍辅助服务模式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ACCESSIBILITY_MODE_AUTO = 0 | 根据组件不同会转换为“enabled”或者“disabled”。 |
| ARKUI_ACCESSIBILITY_MODE_ENABLED = 1 | 当前组件可被无障碍辅助服务所识别。 |
| ARKUI_ACCESSIBILITY_MODE_DISABLED = 2 | 当前组件不可被无障碍辅助服务所识别。 |
| ARKUI_ACCESSIBILITY_MODE_DISABLED_FOR_DESCENDANTS = 3 | 当前组件及其所有子组件不可被无障碍辅助服务所识别。 |

**ArkUI_TextCopyOptions**

```ets
enum ArkUI_TextCopyOptions
```

描述：

定义组件支持设置文本是否可复制粘贴。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_TEXT_COPY_OPTIONS_NONE = 0 | 不支持复制。 |
| ARKUI_TEXT_COPY_OPTIONS_IN_APP = 1 | 支持应用内复制。 |
| ARKUI_TEXT_COPY_OPTIONS_LOCAL_DEVICE = 2 | 支持设备内复制。 |
| ARKUI_TEXT_COPY_OPTIONS_CROSS_DEVICE = 3 | 支持跨设备复制。 |

**ArkUI_TextHeightAdaptivePolicy**

```ets
enum ArkUI_TextHeightAdaptivePolicy
```

描述：

定义文本自适应高度的方式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_TEXT_HEIGHT_ADAPTIVE_POLICY_MAX_LINES_FIRST = 0 | 设置文本高度自适应方式为以MaxLines优先。 |
| ARKUI_TEXT_HEIGHT_ADAPTIVE_POLICY_MIN_FONT_SIZE_FIRST = 1 | 设置文本高度自适应方式为以缩小字体优先。 |
| ARKUI_TEXT_HEIGHT_ADAPTIVE_POLICY_LAYOUT_CONSTRAINT_FIRST = 2 | 设置文本高度自适应方式为以布局约束（高度）优先。 |

**ArkUI_ScrollNestedMode**

```ets
enum ArkUI_ScrollNestedMode
```

描述：

定义嵌套滚动选项。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SCROLL_NESTED_MODE_SELF_ONLY = 0 | 只自身滚动，不与父组件联动。 |
| ARKUI_SCROLL_NESTED_MODE_SELF_FIRST = 1 | 自身先滚动，自身滚动到边缘以后父组件滚动。父组件滚动到边缘以后 |
| ARKUI_SCROLL_NESTED_MODE_PARENT_FIRST = 2 | 父组件先滚动，父组件滚动到边缘以后自身滚动。 |
| ARKUI_SCROLL_NESTED_MODE_PARALLEL = 3 | 自身和父组件同时滚动，自身和父组件都到达边缘以后 |

**ArkUI_ScrollEdge**

```ets
enum ArkUI_ScrollEdge
```

描述：

定义滚动到的边缘位置。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SCROLL_EDGE_TOP = 0 | 竖直方向上边缘。 |
| ARKUI_SCROLL_EDGE_BOTTOM = 1 | 竖直方向下边缘。 |
| ARKUI_SCROLL_EDGE_START = 2 | 水平方向起始位置。 |
| ARKUI_SCROLL_EDGE_END = 3 | 水平方向末尾位置。 |

**ArkUI_ScrollAlignment**

```ets
enum ArkUI_ScrollAlignment
```

描述：

滚动到具体item时的对齐方式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SCROLL_ALIGNMENT_START = 0 | 首部对齐。指定item首部与容器首部对齐。 |
| ARKUI_SCROLL_ALIGNMENT_CENTER = 1 | 居中对齐。指定item主轴方向居中对齐于容器。 |
| ARKUI_SCROLL_ALIGNMENT_END = 2 | 尾部对齐。指定item尾部与容器尾部对齐。 |
| ARKUI_SCROLL_ALIGNMENT_AUTO = 3 | 自动对齐。若指定item完全处于显示区，不做调整。否则依照滑动距离最短的原则，将指定item首部对齐或尾部对齐于容器,使指定item完全处于显示区。 |

**ArkUI_ScrollState**

```ets
enum ArkUI_ScrollState
```

描述：

定义当前滚动状态。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SCROLL_STATE_IDLE = 0 | 空闲状态。使用控制器提供的方法控制滚动时触发，拖动滚动条滚动时触发。 |
| ARKUI_SCROLL_STATE_SCROLL = 1 | 滚动状态。使用手指拖动容器滚动时触发。 |
| ARKUI_SCROLL_STATE_FLING = 2 | 惯性滚动状态。快速划动松手后进行惯性滚动和划动到边缘回弹时触发。 |

**ArkUI_SliderBlockStyle**

```ets
enum ArkUI_SliderBlockStyle
```

描述：

定义滑块形状。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SLIDER_BLOCK_STYLE_DEFAULT = 0 | 使用默认滑块（圆形）。 |
| ARKUI_SLIDER_BLOCK_STYLE_IMAGE = 1 | 使用图片资源作为滑块。 |
| ARKUI_SLIDER_BLOCK_STYLE_SHAPE = 2 | 使用自定义形状作为滑块。 |

**ArkUI_SliderDirection**

```ets
enum ArkUI_SliderDirection
```

描述：

定义滑动条滑动方向。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SLIDER_DIRECTION_VERTICAL = 0 | 方向为纵向。 |
| ARKUI_SLIDER_DIRECTION_HORIZONTAL = 1 | 方向为横向。 |

**ArkUI_SliderStyle**

```ets
enum ArkUI_SliderStyle
```

描述：

定义滑块与滑轨显示样式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SLIDER_STYLE_OUT_SET = 0 | 滑块在滑轨上。 |
| ARKUI_SLIDER_STYLE_IN_SET = 1 | 滑块在滑轨内。 |
| ARKUI_SLIDER_STYLE_NONE = 2 | 无滑块。 |

**ArkUI_CheckboxShape**

```ets
enum ArkUI_CheckboxShape
```

描述：

定义CheckBox组件形状。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ArkUI_CHECKBOX_SHAPE_CIRCLE = 0 | 圆形。 |
| ArkUI_CHECKBOX_SHAPE_ROUNDED_SQUARE = 1 | 圆角方形。 |

**ArkUI_AnimationPlayMode**

```ets
enum ArkUI_AnimationPlayMode
```

描述：

定义动画播放模式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ANIMATION_PLAY_MODE_NORMAL = 0 | 动画正向播放。 |
| ARKUI_ANIMATION_PLAY_MODE_REVERSE = 1 | 动画反向播放。 |
| ARKUI_ANIMATION_PLAY_MODE_ALTERNATE = 2 | 动画在奇数次（1、3、5...）正向播放，在偶数次（2、4、6...）反向播放。 |
| ARKUI_ANIMATION_PLAY_MODE_ALTERNATE_REVERSE = 3 | 动画在奇数次（1、3、5...）反向播放，在偶数次（2、4、6...）正向播放。 |

**ArkUI_ImageSize**

```ets
enum ArkUI_ImageSize
```

描述：

定义图片宽高样式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_IMAGE_SIZE_AUTO = 0 | 保持原图的比例不变。 |
| ARKUI_IMAGE_SIZE_COVER = 1 | 保持宽高比进行缩小或者放大，使得图片两边都大于或等于显示边界。 |
| ARKUI_IMAGE_SIZE_CONTAIN = 2 | 保持宽高比进行缩小或者放大，使得图片完全显示在显示边界内。 |

**ArkUI_AdaptiveColor**

```ets
enum ArkUI_AdaptiveColor
```

描述：

定义取色模式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ADAPTIVE_COLOR_DEFAULT = 0 | 不使用取色模糊。 |
| ARKUI_ADAPTIVE_COLOR_AVERAGE = 1 | 使用取色模糊。 |

**ArkUI_ColorMode**

```ets
enum ArkUI_ColorMode
```

描述：

定义深浅色模式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_COLOR_MODE_SYSTEM = 0 | 跟随系统深浅色模式。 |
| ARKUI_COLOR_MODE_LIGHT = 1 | 固定使用浅色模式。 |
| ARKUI_COLOR_MODE_DARK = 2 | 固定使用深色模式。 |

**ArkUI_SystemColorMode**

```ets
enum ArkUI_SystemColorMode
```

描述：

定义系统深浅色模式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SYSTEM_COLOR_MODE_LIGHT = 0 | 浅色模式。 |
| ARKUI_SYSTEM_COLOR_MODE_DARK = 1 | 深色模式。 |

**ArkUI_BlurStyle**

```ets
enum ArkUI_BlurStyle
```

描述：

定义背景模糊样式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_BLUR_STYLE_THIN = 0 | 轻薄材质模糊。 |
| ARKUI_BLUR_STYLE_REGULAR = 1 | 普通厚度材质模糊。 |
| ARKUI_BLUR_STYLE_THICK = 2 | 厚材质模糊。 |
| ARKUI_BLUR_STYLE_BACKGROUND_THIN = 3 | 近距景深模糊。 |
| ARKUI_BLUR_STYLE_BACKGROUND_REGULAR = 4 | 中距景深模糊。 |
| ARKUI_BLUR_STYLE_BACKGROUND_THICK = 5 | 远距景深模糊。 |
| ARKUI_BLUR_STYLE_BACKGROUND_ULTRA_THICK = 6 | 超远距景深模糊。 |
| ARKUI_BLUR_STYLE_NONE = 7 | 关闭模糊。 |
| ARKUI_BLUR_STYLE_COMPONENT_ULTRA_THIN = 8 | 组件超轻薄材质模糊。 |
| ARKUI_BLUR_STYLE_COMPONENT_THIN = 9 | 组件轻薄材质模糊。 |
| ARKUI_BLUR_STYLE_COMPONENT_REGULAR = 10 | 组件普通材质模糊。 |
| ARKUI_BLUR_STYLE_COMPONENT_THICK = 11 | 组件厚材质模糊。 |
| ARKUI_BLUR_STYLE_COMPONENT_ULTRA_THICK = 12 | 组件超厚材质模糊。 |

**ArkUI_BlurStyleActivePolicy**

```ets
enum ArkUI_BlurStyleActivePolicy
```

描述：

定义背景模糊激活策略。

起始版本： 19

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_BLUR_STYLE_ACTIVE_POLICY_FOLLOWS_WINDOW_ACTIVE_STATE = 0 | 模糊效果跟随窗口焦点状态变化，非焦点不模糊，焦点模糊。 |
| ARKUI_BLUR_STYLE_ACTIVE_POLICY_ALWAYS_ACTIVE = 1 | 一直有模糊效果。 |
| ARKUI_BLUR_STYLE_ACTIVE_POLICY_ALWAYS_INACTIVE = 2 | 一直无模糊效果。 |

**ArkUI_VerticalAlignment**

```ets
enum ArkUI_VerticalAlignment
```

描述：

定义垂直对齐方式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_VERTICAL_ALIGNMENT_TOP = 0 | 顶部对齐。 |
| ARKUI_VERTICAL_ALIGNMENT_CENTER = 1 | 居中对齐，默认对齐方式。 |
| ARKUI_VERTICAL_ALIGNMENT_BOTTOM = 2 | 底部对齐。 |

**ArkUI_HorizontalAlignment**

```ets
enum ArkUI_HorizontalAlignment
```

描述：

定义语言方向对齐方式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_HORIZONTAL_ALIGNMENT_START = 0 | 按照语言方向起始端对齐。 |
| ARKUI_HORIZONTAL_ALIGNMENT_CENTER = 1 | 居中对齐，默认对齐方式。 |
| ARKUI_HORIZONTAL_ALIGNMENT_END = 2 | 按照语言方向末端对齐。 |

**ArkUI_TextOverflow**

```ets
enum ArkUI_TextOverflow
```

描述：

定义文本超长时的显示方式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_TEXT_OVERFLOW_NONE = 0 | 文本超长时不裁剪显示。 |
| ARKUI_TEXT_OVERFLOW_CLIP = 1 | 文本超长时进行裁剪显示。 |
| ARKUI_TEXT_OVERFLOW_ELLIPSIS = 2 | 文本超长时显示不下的文本用省略号代替。 |
| ARKUI_TEXT_OVERFLOW_MARQUEE = 3 | 文本超长时以跑马灯的方式展示。 |

**ArkUI_ImageSpanAlignment**

```ets
enum ArkUI_ImageSpanAlignment
```

描述：

定义图片基于文本的对齐方式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_IMAGE_SPAN_ALIGNMENT_BASELINE = 0 | 图片下边沿与文本BaseLine对齐。 |
| ARKUI_IMAGE_SPAN_ALIGNMENT_BOTTOM | 图片下边沿与文本下边沿对齐。 |
| ARKUI_IMAGE_SPAN_ALIGNMENT_CENTER | 图片中间与文本中间对齐。 |
| ARKUI_IMAGE_SPAN_ALIGNMENT_TOP | 图片上边沿与文本上边沿对齐。 |
| ARKUI_IMAGE_SPAN_ALIGNMENT_FOLLOW_PARAGRAPH | 图片对齐方式跟随Text组件对齐方式。 起始版本： 20 |

**ArkUI_ObjectFit**

```ets
enum ArkUI_ObjectFit
```

描述：

定义image填充效果。ImageSpanAlignment

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_OBJECT_FIT_CONTAIN = 0 | 保持宽高比进行缩小或者放大，使得图片完全显示在显示边界内。 |
| ARKUI_OBJECT_FIT_COVER = 1 | 保持宽高比进行缩小或者放大，使得图片两边都大于或等于显示边界。 |
| ARKUI_OBJECT_FIT_AUTO = 2 | 自适应显示。 |
| ARKUI_OBJECT_FIT_FILL = 3 | 不保持宽高比进行放大缩小，使得图片充满显示边界。 |
| ARKUI_OBJECT_FIT_SCALE_DOWN = 4 | 保持宽高比显示，图片缩小或者保持不变。 |
| ARKUI_OBJECT_FIT_NONE = 5 | 保持原有尺寸显示。 |
| ARKUI_OBJECT_FIT_NONE_AND_ALIGN_TOP_START = 6 | 图片大小不变，在image组件中顶部起始端对齐。 |
| ARKUI_OBJECT_FIT_NONE_AND_ALIGN_TOP = 7 | 图片大小不变，在image组件中顶部横向居中对齐。 |
| ARKUI_OBJECT_FIT_NONE_AND_ALIGN_TOP_END = 8 | 图片大小不变，在image组件中顶部尾端对齐。 |
| ARKUI_OBJECT_FIT_NONE_AND_ALIGN_START = 9 | 图片大小不变，在image组件中起始端纵向居中对齐。 |
| ARKUI_OBJECT_FIT_NONE_AND_ALIGN_CENTER = 10 | 图片大小不变，在image组件中横向和纵向居中对齐。 |
| ARKUI_OBJECT_FIT_NONE_AND_ALIGN_END = 11 | 图片大小不变，在image组件中尾端纵向居中对齐。 |
| ARKUI_OBJECT_FIT_NONE_AND_ALIGN_BOTTOM_START = 12 | 图片大小不变，在image组件中底部起始端对齐。 |
| ARKUI_OBJECT_FIT_NONE_AND_ALIGN_BOTTOM = 13 | 图片大小不变，在image组件中底部横向居中对齐。 |
| ARKUI_OBJECT_FIT_NONE_AND_ALIGN_BOTTOM_END = 14 | 图片大小不变，在image组件中底部尾端对齐。 |
| ARKUI_OBJECT_FIT_NONE_MATRIX = 15 | 不改变图像原始大小，需要配合NODE_IMAGE_IMAGE_MATRIX使用。 起始版本： 21 |

**ArkUI_ImageInterpolation**

```ets
enum ArkUI_ImageInterpolation
```

描述：

定义图片插值效果。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_IMAGE_INTERPOLATION_NONE = 0 | 不使用图片插值。 |
| ARKUI_IMAGE_INTERPOLATION_LOW = 1 | 低图片插值。 |
| ARKUI_IMAGE_INTERPOLATION_MEDIUM = 2 | 中图片插值。 |
| ARKUI_IMAGE_INTERPOLATION_HIGH = 3 | 高图片插值，插值质量最高。 |

**ArkUI_DynamicRangeMode**

```ets
enum ArkUI_DynamicRangeMode
```

描述：

定义图像动态范围模式（例如：SDR/HDR），用于控制图像的明暗与色彩显示范围。

起始版本： 21

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_DYNAMIC_RANGE_MODE_HIGH = 0 | 高动态范围（High Dynamic Range，简称HDR），表示图片中显示亮度（brightness）的最小值和最大值的范围，范围越大图像的亮度表达更逼近真实环境，在太亮的环境下不会产生过曝（一片白），太暗的环境下产生过暗的效果（一片黑）。 |
| ARKUI_DYNAMIC_RANGE_MODE_CONSTRAINT | 受限的高动态范围，包含比SDR更丰富的亮度和色彩，但不是完整的HDR，一般用于需要兼容SDR的情况。 |
| ARKUI_DYNAMIC_RANGE_MODE_STANDARD | 标准动态范围（Standard Dynamic Range，简称SDR），表示亮度范围有限，一般在0~100尼特（亮度单位）左右，明暗对比度较小，暗部容易糊成黑，亮部容易爆白。 |

**ArkUI_ImageRotateOrientation**

```ets
enum ArkUI_ImageRotateOrientation
```

描述：

定义图像旋转方向。

起始版本： 21

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ORIENTATION_AUTO = 0 | 读取图片携带的EXIF元数据作为显示方向，支持旋转和镜像。 |
| ARKUI_ORIENTATION_UP | 默认按照当前图片的像素数据进行显示，不做任何处理。 |
| ARKUI_ORIENTATION_RIGHT | 将当前图片顺时针旋转90度后显示。 |
| ARKUI_ORIENTATION_DOWN | 将当前图片顺时针旋转180度后显示。 |
| ARKUI_ORIENTATION_LEFT | 将当前图片顺时针旋转270度后显示。 |
| ARKUI_ORIENTATION_UP_MIRRORED | 将当前图片水平翻转后显示。 |
| ARKUI_ORIENTATION_RIGHT_MIRRORED | 将当前图片水平翻转再顺时针旋转90度后显示。 |
| ARKUI_ORIENTATION_DOWN_MIRRORED | 将当前图片垂直翻转后显示。 |
| ARKUI_ORIENTATION_LEFT_MIRRORED | 将当前图片水平翻转再顺时针旋转270度后显示。 |

**ArkUI_BlendMode**

```ets
enum ArkUI_BlendMode
```

描述：

混合模式枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_BLEND_MODE_NONE = 0 | 将上层图像直接覆盖到下层图像上，不进行任何混合操作。 |
| ARKUI_BLEND_MODE_CLEAR = 1 | 将源像素覆盖的目标像素清除为完全透明。 |
| ARKUI_BLEND_MODE_SRC = 2 | r = s，只显示源像素。 |
| ARKUI_BLEND_MODE_DST = 3 | r = d，只显示目标像素。 |
| ARKUI_BLEND_MODE_SRC_OVER = 4 | r = s + (1 - sa) * d，将源像素按照透明度进行混合，覆盖在目标像素上。 |
| ARKUI_BLEND_MODE_DST_OVER = 5 | r = d + (1 - da) * s，将目标像素按照透明度进行混合，覆盖在源像素上。 |
| ARKUI_BLEND_MODE_SRC_IN = 6 | r = s * da，只显示源像素中与目标像素重叠的部分。 |
| ARKUI_BLEND_MODE_DST_IN = 7 | r = d * sa，只显示目标像素中与源像素重叠的部分。 |
| ARKUI_BLEND_MODE_SRC_OUT = 8 | r = s * (1 - da)，只显示源像素中与目标像素不重叠的部分。 |
| ARKUI_BLEND_MODE_DST_OUT = 9 | r = d * (1 - sa)，只显示目标像素中与源像素不重叠的部分。 |
| ARKUI_BLEND_MODE_SRC_ATOP = 10 | r = s * da + d * (1 - sa)，在源像素和目标像素重叠的地方绘制源像素，在源像素和目标像素不重叠的地方绘制目标像素。 |
| ARKUI_BLEND_MODE_DST_ATOP = 11 | r = d * sa + s * (1 - da)，在源像素和目标像素重叠的地方绘制目标像素，在源像素和目标像素不重叠的地方绘制源像素。 |
| ARKUI_BLEND_MODE_XOR = 12 | r = s * (1 - da) + d * (1 - sa)，只显示源像素与目标像素不重叠的部分。 |
| ARKUI_BLEND_MODE_PLUS = 13 | r = min(s + d, 1)，将源像素值与目标像素值相加，并将结果作为新的像素值。 |
| ARKUI_BLEND_MODE_MODULATE = 14 | r = s * d，将源像素与目标像素进行乘法运算，并将结果作为新的像素值。 |
| ARKUI_BLEND_MODE_SCREEN = 15 | r = s + d - s * d，将两个图像的像素值相加，然后减去它们的乘积来实现混合。 |
| ARKUI_BLEND_MODE_OVERLAY = 16 | 根据目标像素来决定使用MULTIPLY混合模式还是SCREEN混合模式。 |
| ARKUI_BLEND_MODE_DARKEN = 17 | rc = s + d - max(s * da, d * sa), ra = kSrcOver，当两个颜色重叠时，较暗的颜色会覆盖较亮的颜色。 |
| ARKUI_BLEND_MODE_LIGHTEN = 18 | rc = s + d - min(s * da, d * sa), ra = kSrcOver，将源图像和目标图像中的像素进行比较，选取两者中较亮的像素作为最终的混合结果。 |
| ARKUI_BLEND_MODE_COLOR_DODGE = 19 | 使目标像素变得更亮来反映源像素。 |
| ARKUI_BLEND_MODE_COLOR_BURN = 20 | 使目标像素变得更暗来反映源像素。 |
| ARKUI_BLEND_MODE_HARD_LIGHT = 21 | 根据源像素的值来决定目标像素变得更亮或者更暗。根据源像素来决定使用MULTIPLY混合模式还是SCREEN混合模式。 |
| ARKUI_BLEND_MODE_SOFT_LIGHT = 22 | 根据源像素来决定使用LIGHTEN混合模式还是DARKEN混合模式。 |
| ARKUI_BLEND_MODE_DIFFERENCE = 23 | rc = s + d - 2 * (min(s * da, d * sa)), ra = kSrcOver，对比源像素和目标像素，亮度更高的像素减去亮度更低的像素，产生高对比度的效果。 |
| ARKUI_BLEND_MODE_EXCLUSION = 24 | rc = s + d - two(s * d), ra = kSrcOver，对比源像素和目标像素，亮度更高的像素减去亮度更低的像素，产生柔和的效果。 |
| ARKUI_BLEND_MODE_MULTIPLY = 25 | r = s * (1 - da) + d * (1 - sa) + s * d，将源图像与目标图像进行乘法混合，得到一张新的图像。 |
| ARKUI_BLEND_MODE_HUE = 26 | 保留源图像的亮度和饱和度，但会使用目标图像的色调来替换源图像的色调。 |
| ARKUI_BLEND_MODE_SATURATION = 27 | 保留目标像素的亮度和色调，但会使用源像素的饱和度来替换目标像素的饱和度。 |
| ARKUI_BLEND_MODE_COLOR = 28 | 保留源像素的饱和度和色调，但会使用目标像素的亮度来替换源像素的亮度。 |
| ARKUI_BLEND_MODE_LUMINOSITY = 29 | 保留目标像素的色调和饱和度，但会用源像素的亮度替换目标像素的亮度。 |

**ArkUI_Direction**

```ets
enum ArkUI_Direction
```

描述：

设置容器元素内主轴方向上的布局枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_DIRECTION_LTR = 0 | 元素从左到右布局，该值为默认值。 |
| ARKUI_DIRECTION_RTL = 1 | 元素从右到左布局。 |
| ARKUI_DIRECTION_AUTO = 3 | 使用系统布局方向。 |

**ArkUI_ItemAlignment**

```ets
enum ArkUI_ItemAlignment
```

描述：

设置子组件在父容器交叉轴的对齐格式枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ITEM_ALIGNMENT_AUTO = 0 | 使用Flex容器中默认配置，该值为默认值。 |
| ARKUI_ITEM_ALIGNMENT_START = 1 | 元素在Flex容器中，交叉轴方向首部对齐。 |
| ARKUI_ITEM_ALIGNMENT_CENTER = 2 | 元素在Flex容器中，交叉轴方向居中对齐。 |
| ARKUI_ITEM_ALIGNMENT_END = 3 | 元素在Flex容器中，交叉轴方向底部对齐。 |
| ARKUI_ITEM_ALIGNMENT_STRETCH = 4 | 元素在Flex容器中，交叉轴方向拉伸填充。 |
| ARKUI_ITEM_ALIGNMENT_BASELINE = 5 | 元素在Flex容器中，交叉轴方向文本基线对齐。 |

**ArkUI_ColorStrategy**

```ets
enum ArkUI_ColorStrategy
```

描述：

前景色枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_COLOR_STRATEGY_INVERT = 0 | 前景色为控件背景色的反色。 |
| ARKUI_COLOR_STRATEGY_AVERAGE = 1 | 控件背景阴影色为控件背景阴影区域的平均色。 |
| ARKUI_COLOR_STRATEGY_PRIMARY = 2 | 控件背景阴影色为控件背景阴影区域的主色。 |

**ArkUI_FlexAlignment**

```ets
enum ArkUI_FlexAlignment
```

描述：

定义垂直方向对齐方式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_FLEX_ALIGNMENT_START = 1 | 主轴方向首端对齐，该值为默认值。 |
| ARKUI_FLEX_ALIGNMENT_CENTER = 2 | 主轴方向中心对齐。 |
| ARKUI_FLEX_ALIGNMENT_END = 3 | 主轴方向尾部对齐。 |
| ARKUI_FLEX_ALIGNMENT_SPACE_BETWEEN = 6 | Flex主轴方向均匀分配弹性元素，相邻元素之间距离相同，第一个元素行首对齐，最后的元素行尾对齐。 |
| ARKUI_FLEX_ALIGNMENT_SPACE_AROUND = 7 | Flex主轴方向均匀分配弹性元素，相邻元素之间距离相同，第一个元素到行首的距离时相邻元素间距离的一半。 |
| ARKUI_FLEX_ALIGNMENT_SPACE_EVENLY = 8 | Flex主轴方向均匀分配弹性元素，相邻元素之间距离、第一个元素到行首的距离和最后的元素到行尾的距离均相等。 |

**ArkUI_FlexDirection**

```ets
enum ArkUI_FlexDirection
```

描述：

定义[Flex](Flex.md)容器的主轴方向。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_FLEX_DIRECTION_ROW = 0 | 主轴与行方向一致，该值为默认值。 |
| ARKUI_FLEX_DIRECTION_COLUMN = 1 | 主轴与列方向一致。 |
| ARKUI_FLEX_DIRECTION_ROW_REVERSE = 2 | 主轴与行方向相反。 |
| ARKUI_FLEX_DIRECTION_COLUMN_REVERSE = 3 | 主轴与列方向相反。 |

**ArkUI_FlexWrap**

```ets
enum ArkUI_FlexWrap
```

描述：

定义Flex行列布局模式模式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_FLEX_WRAP_NO_WRAP = 0 | 单行/单列布局，子项不能超出容器，该值为默认值。 |
| ARKUI_FLEX_WRAP_WRAP = 1 | 多行/多列布局，子项允许超出容器。 |
| ARKUI_FLEX_WRAP_WRAP_REVERSE = 2 | 反向多行/多列布局，子项允许超出容器。 |

**ArkUI_Visibility**

```ets
enum ArkUI_Visibility
```

描述：

控制组件的显隐枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_VISIBILITY_VISIBLE = 0 | 显示。 |
| ARKUI_VISIBILITY_HIDDEN = 1 | 隐藏，但参与布局进行占位。 |
| ARKUI_VISIBILITY_NONE = 2 | 隐藏，但不参与布局，不进行占位。 |

**ArkUI_CalendarAlignment**

```ets
enum ArkUI_CalendarAlignment
```

描述：

日历选择器与入口组件对齐方式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_CALENDAR_ALIGNMENT_START = 0 | 选择器和入口组件左对齐方式。 |
| ARKUI_CALENDAR_ALIGNMENT_CENTER = 1 | 选择器和入口组件居中对齐方式。 |
| ARKUI_CALENDAR_ALIGNMENT_END = 2 | 选择器和入口组件右对齐方式。 |

**ArkUI_MaskType**

```ets
enum ArkUI_MaskType
```

描述：

遮罩类型枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_MASK_TYPE_RECTANGLE = 0 | 矩形类型。 |
| ARKUI_MASK_TYPE_CIRCLE = 1 | 圆形类型。 |
| ARKUI_MASK_TYPE_ELLIPSE = 2 | 椭圆形类型。 |
| ARKUI_MASK_TYPE_PATH = 3 | 路径类型。 |
| ARKUI_MASK_TYPE_PROGRESS = 4 | 进度类型。 |

**ArkUI_ClipType**

```ets
enum ArkUI_ClipType
```

描述：

裁剪类型枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_CLIP_TYPE_RECTANGLE = 0 | 矩形类型。 |
| ARKUI_CLIP_TYPE_CIRCLE = 1 | 圆形类型。 |
| ARKUI_CLIP_TYPE_ELLIPSE = 2 | 椭圆形类型。 |
| ARKUI_CLIP_TYPE_PATH = 3 | 路径类型。 |

**ArkUI_ShapeType**

```ets
enum ArkUI_ShapeType
```

描述：

自定义形状。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SHAPE_TYPE_RECTANGLE = 0 | 矩形类型。 |
| ARKUI_SHAPE_TYPE_CIRCLE = 1 | 圆形类型。 |
| ARKUI_SHAPE_TYPE_ELLIPSE = 2 | 椭圆形类型。 |
| ARKUI_SHAPE_TYPE_PATH = 3 | 路径类型。 |

**ArkUI_LinearGradientDirection**

```ets
enum ArkUI_LinearGradientDirection
```

描述：

定义渐变方向结构。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_LINEAR_GRADIENT_DIRECTION_LEFT = 0 | 向左渐变。 |
| ARKUI_LINEAR_GRADIENT_DIRECTION_TOP = 1 | 向上渐变。 |
| ARKUI_LINEAR_GRADIENT_DIRECTION_RIGHT = 2 | 向右渐变。 |
| ARKUI_LINEAR_GRADIENT_DIRECTION_BOTTOM = 3 | 向下渐变。 |
| ARKUI_LINEAR_GRADIENT_DIRECTION_LEFT_TOP = 4 | 向左上渐变。 |
| ARKUI_LINEAR_GRADIENT_DIRECTION_LEFT_BOTTOM = 5 | 向左下渐变。 |
| ARKUI_LINEAR_GRADIENT_DIRECTION_RIGHT_TOP = 6 | 向右上渐变。 |
| ARKUI_LINEAR_GRADIENT_DIRECTION_RIGHT_BOTTOM = 7 | 向右下渐变。 |
| ARKUI_LINEAR_GRADIENT_DIRECTION_NONE = 8 | 不渐变。 |
| ARKUI_LINEAR_GRADIENT_DIRECTION_CUSTOM = 9 | 自定义渐变方向. |

**ArkUI_WordBreak**

```ets
enum ArkUI_WordBreak
```

描述：

定义文本断行规则。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_WORD_BREAK_NORMAL = 0 | CJK(中文、日文、韩文)文本可以在任意2个字符间断行，而Non-CJK文本（如英文等）只能在空白符处断行。 |
| ARKUI_WORD_BREAK_BREAK_ALL | 对于Non-CJK的文本，可在任意2个字符间断行。CJK(中文、日文、韩文)文本可以在任意2个字符间断行。 |
| ARKUI_WORD_BREAK_BREAK_WORD | 对于Non-CJK的文本可在任意2个字符间断行，一行文本中有断行破发点（如空白符）时，优先按破发点换行。对于CJK的文本，换行效果与NORMAL效果保持一致。 |
| ARKUI_WORD_BREAK_HYPHENATION | 对于Non-CJK的文本，可以按照音节断行。对于CJK的文本，换行效果与NORMAL效果保持一致。 起始版本： 18 |

**ArkUI_EllipsisMode**

```ets
enum ArkUI_EllipsisMode
```

描述：

定义文本省略位置。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ELLIPSIS_MODE_START = 0 | 省略行首内容。 |
| ARKUI_ELLIPSIS_MODE_CENTER | 省略行中内容。 |
| ARKUI_ELLIPSIS_MODE_END | 省略行末内容。 |

**ArkUI_ImageRenderMode**

```ets
enum ArkUI_ImageRenderMode
```

描述：

定义图片渲染模式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_IMAGE_RENDER_MODE_ORIGINAL = 0 | 原色渲染模式。 |
| ARKUI_IMAGE_RENDER_MODE_TEMPLATE = 1 | 黑白渲染模式。 |

**ArkUI_TransitionEdge**

```ets
enum ArkUI_TransitionEdge
```

描述：

定义转场从边缘滑入和滑出的效果。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_TRANSITION_EDGE_TOP = 0 | 窗口的上边缘。 |
| ARKUI_TRANSITION_EDGE_BOTTOM = 1 | 窗口的下边缘。 |
| ARKUI_TRANSITION_EDGE_START = 2 | 窗口的左边缘。 |
| ARKUI_TRANSITION_EDGE_END = 3 | 窗口的右边缘。 |

**ArkUI_FinishCallbackType**

```ets
enum ArkUI_FinishCallbackType
```

描述：

在动画中定义onFinish回调的类型。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_FINISH_CALLBACK_REMOVED = 0 | 当整个动画结束并立即删除时，将触发回调。 |
| ARKUI_FINISH_CALLBACK_LOGICALLY = 1 | 当动画在逻辑上处于下降状态，但可能仍处于其长尾状态时，将触发回调。 |

**ArkUI_ListItemAlignment**

```ets
enum ArkUI_ListItemAlignment
```

描述：

交叉轴方向的布局方式，默认值为ARKUI_LIST_ITEM_ALIGNMENT_START。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_LIST_ITEM_ALIGNMENT_START = 0 | ListItem在List中，交叉轴方向首部对齐。 |
| ARKUI_LIST_ITEM_ALIGNMENT_CENTER = 1 | ListItem在List中，交叉轴方向居中对齐。 |
| ARKUI_LIST_ITEM_ALIGNMENT_END = 2 | ListItem在List中，交叉轴方向尾部对齐。 |

**ArkUI_BlendApplyType**

```ets
enum ArkUI_BlendApplyType
```

描述：

指定的混合模式应用于视图的内容选项.

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| BLEND_APPLY_TYPE_FAST = 0 | 在目标图像上按顺序混合视图的内容. |
| BLEND_APPLY_TYPE_OFFSCREEN = 1 | 将此组件和子组件内容绘制到离屏画布上，然后整体进行混合. |

**ArkUI_LengthMetricUnit**

```ets
enum ArkUI_LengthMetricUnit
```

描述：

定义组件的单位模式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_LENGTH_METRIC_UNIT_DEFAULT = -1 | 默认，字体类单位为FP，非字体类单位为VP。 |
| ARKUI_LENGTH_METRIC_UNIT_PX = 0 | 单位为PX。 |
| ARKUI_LENGTH_METRIC_UNIT_VP = 1 | 单位为VP。 |
| ARKUI_LENGTH_METRIC_UNIT_FP = 2 | 单位为FP。 |

**ArkUI_TextInputContentType**

```ets
enum ArkUI_TextInputContentType
```

描述：

定义自动填充类型。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_TEXTINPUT_CONTENT_TYPE_USER_NAME = 0 | 【用户名】在已启用密码保险箱的情况下，支持用户名的自动保存和自动填充。 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_PASSWORD | 【密码】在已启用密码保险箱的情况下，支持密码的自动保存和自动填充。 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_NEW_PASSWORD | 【新密码】在已启用密码保险箱的情况下，支持自动生成新密码。 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_FULL_STREET_ADDRESS | 【详细地址】在已启用情景化自动填充的情况下，支持详细地址的自动保存和自动填充。 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_HOUSE_NUMBER | 【门牌号】在已启用情景化自动填充的情况下，支持门牌号的自动保存和自动填充。 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_DISTRICT_ADDRESS | 【区/县】在已启用情景化自动填充的情况下，支持区/县的自动保存和自动填充。 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_CITY_ADDRESS | 【市】在已启用情景化自动填充的情况下，支持市的自动保存和自动填充。 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_PROVINCE_ADDRESS | 【省】在已启用情景化自动填充的情况下，支持省的自动保存和自动填充。 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_COUNTRY_ADDRESS | 【国家】在已启用情景化自动填充的情况下，支持国家的自动保存和自动填充。 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_PERSON_FULL_NAME | 【姓名】在已启用情景化自动填充的情况下，支持姓名的自动保存和自动填充。 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_PERSON_LAST_NAME | 【姓氏】在已启用情景化自动填充的情况下，支持姓氏的自动保存和自动填充。 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_PERSON_FIRST_NAME | 【名字】在已启用情景化自动填充的情况下，支持名字的自动保存和自动填充。 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_PHONE_NUMBER | 【手机号】在已启用情景化自动填充的情况下，支持手机号的自动保存和自动填充。 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_PHONE_COUNTRY_CODE | 【国家代码】在已启用情景化自动填充的情况下，支持国家代码的自动保存和自动填充。 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_FULL_PHONE_NUMBER | 【包含国家代码的手机号】在已启用情景化自动填充的情况下，支持包含国家代码的手机号的自动保存和自动填充。 |
| ARKUI_TEXTINPUT_CONTENT_EMAIL_ADDRESS | 【邮箱地址】在已启用情景化自动填充的情况下，支持邮箱地址的自动保存和自动填充。 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_BANK_CARD_NUMBER | 【银行卡号】在已启用情景化自动填充的情况下，支持银行卡号的自动保存和自动填充。 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_ID_CARD_NUMBER | 【身份证号】在已启用情景化自动填充的情况下，支持身份证号的自动保存和自动填充。 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_NICKNAME | 【昵称】在已启用情景化自动填充的情况下，支持昵称的自动保存和自动填充。 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_DETAIL_INFO_WITHOUT_STREET | 【无街道地址】在已启用情景化自动填充的情况下，支持无街道地址的自动保存和自动填充。 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_FORMAT_ADDRESS | 【标准地址】在已启用情景化自动填充的情况下，支持标准地址的自动保存和自动填充。 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_PASSPORT_NUMBER | 【护照号】在已启用情景化自动填充的情况下，支持护照号的自动保存和自动填充。 起始版本： 18 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_VALIDITY | 【护照有效期】在已启用情景化自动填充的情况下，支持护照有效期的自动保存和自动填充。 起始版本： 18 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_ISSUE_AT | 【护照签发地】在已启用情景化自动填充的情况下，支持护照签发地的自动保存和自动填充。 起始版本： 18 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_ORGANIZATION | 【发票抬头名称】在已启用情景化自动填充的情况下，支持发票抬头名称的自动保存和自动填充。 起始版本： 18 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_TAX_ID | 【税号】在已启用情景化自动填充的情况下，支持税号的自动保存和自动填充。 起始版本： 18 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_ADDRESS_CITY_AND_STATE | 【所在地区】在已启用情景化自动填充的情况下，支持所在地区的自动保存和自动填充。 起始版本： 18 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_FLIGHT_NUMBER | 【航班号】暂不支持自动保存和自动填充。 起始版本： 18 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_LICENSE_NUMBER | 【驾驶证号】暂不支持自动保存和自动填充。 起始版本： 18 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_LICENSE_FILE_NUMBER | 【驾驶证档案编号】暂不支持自动保存和自动填充。 起始版本： 18 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_LICENSE_PLATE | 【车牌号】在已启用情景化自动填充的情况下，支持车牌号的自动保存和自动填充。 起始版本： 18 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_ENGINE_NUMBER | 【行驶证发动机号】暂不支持自动保存和自动填充。 起始版本： 18 |
| ARKUI_TEXTINPUT_CONTENT_TYPE_LICENSE_CHASSIS_NUMBER | 【车牌识别号】暂不支持自动保存和自动填充。 起始版本： 18 |

**ArkUI_BarrierDirection**

```ets
enum ArkUI_BarrierDirection
```

描述：

定义屏障线的方向。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_BARRIER_DIRECTION_START = 0 | 屏障在其所有referencedId的最左侧，该值为默认值。 |
| ARKUI_BARRIER_DIRECTION_END = 1 | 屏障在其所有referencedId的最右侧。 |
| ARKUI_BARRIER_DIRECTION_TOP = 2 | 屏障在其所有referencedId的最上方。 |
| ARKUI_BARRIER_DIRECTION_BOTTOM = 3 | 屏障在其所有referencedId的最下方。 |

**ArkUI_RelativeLayoutChainStyle**

```ets
enum ArkUI_RelativeLayoutChainStyle
```

描述：

定义链的风格。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_RELATIVE_LAYOUT_CHAIN_STYLE_SPREAD = 0 | 组件在约束锚点间均匀分布，该值为默认值。 |
| ARKUI_RELATIVE_LAYOUT_CHAIN_STYLE_SPREAD_INSIDE = 1 | 除首尾2个子组件的其他组件在约束锚点间均匀分布。 |
| ARKUI_RELATIVE_LAYOUT_CHAIN_STYLE_PACKED = 2 | 链内子组件无间隙。 |

**ArkUI_TextInputStyle**

```ets
enum ArkUI_TextInputStyle
```

描述：

定义输入框风格。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_TEXTINPUT_STYLE_DEFAULT = 0 | 默认风格，光标宽1.5vp，光标高度与文本选中底板高度和字体大小相关。 |
| ARKUI_TEXTINPUT_STYLE_INLINE | 内联输入风格。文本选中底板高度与输入框高度相同。 |

**ArkUI_KeyboardAppearance**

```ets
enum ArkUI_KeyboardAppearance
```

描述：

定义输入框拉起的键盘样式。

起始版本： 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_KEYBOARD_APPEARANCE_NONE_IMMERSIVE = 0 | 默认模式，不使用沉浸式样式。 |
| ARKUI_KEYBOARD_APPEARANCE_IMMERSIVE = 1 | 沉浸式模式，由系统决定采用的样式。 |
| ARKUI_KEYBOARD_APPEARANCE_LIGHT_IMMERSIVE = 2 | 浅色沉浸式样式。 |
| ARKUI_KEYBOARD_APPEARANCE_DARK_IMMERSIVE = 3 | 深色沉浸式样式。 |

**ArkUI_TextDataDetectorType**

```ets
enum ArkUI_TextDataDetectorType
```

描述：

定义文本识别的实体类型。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_TEXT_DATA_DETECTOR_TYPE_PHONE_NUMBER = 0 | 电话号码。 |
| ARKUI_TEXT_DATA_DETECTOR_TYPE_URL | 链接。 |
| ARKUI_TEXT_DATA_DETECTOR_TYPE_EMAIL | 邮箱。 |
| ARKUI_TEXT_DATA_DETECTOR_TYPE_ADDRESS | 地址。 |

**ArkUI_ButtonType**

```ets
enum ArkUI_ButtonType
```

描述：

定义按钮样式枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_BUTTON_TYPE_NORMAL = 0 | 普通按钮，默认不带圆角。 |
| ARKUI_BUTTON_TYPE_CAPSULE = 1 | 胶囊型按钮，圆角默认为高度的一半。 |
| ARKUI_BUTTON_TYPE_CIRCLE = 2 | 圆形按钮。 |
| ARKUI_BUTTON_ROUNDED_RECTANGLE = 8 | 圆角矩形按钮。 起始版本： 19 |

**ArkUI_RenderFit**

```ets
enum ArkUI_RenderFit
```

描述：

定义动画终态内容大小与位置的枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_RENDER_FIT_CENTER = 0 | 保持动画终态的内容大小，并且内容始终与组件保持中心对齐。 |
| ARKUI_RENDER_FIT_TOP = 1 | 保持动画终态的内容大小，并且内容始终与组件保持顶部中心对齐。 |
| ARKUI_RENDER_FIT_BOTTOM = 2 | 保持动画终态的内容大小，并且内容始终与组件保持底部中心对齐。 |
| ARKUI_RENDER_FIT_LEFT = 3 | 保持动画终态的内容大小，并且内容始终与组件保持左侧对齐。 |
| ARKUI_RENDER_FIT_RIGHT = 4 | 保持动画终态的内容大小，并且内容始终与组件保持右侧对齐。 |
| ARKUI_RENDER_FIT_TOP_LEFT = 5 | 保持动画终态的内容大小，并且内容始终与组件保持左上角对齐。 |
| ARKUI_RENDER_FIT_TOP_RIGHT = 6 | 保持动画终态的内容大小，并且内容始终与组件保持右上角对齐。 |
| ARKUI_RENDER_FIT_BOTTOM_LEFT = 7 | 保持动画终态的内容大小，并且内容始终与组件保持左下角对齐。 |
| ARKUI_RENDER_FIT_BOTTOM_RIGHT = 8 | 保持动画终态的内容大小，并且内容始终与组件保持右下角对齐。 |
| ARKUI_RENDER_FIT_RESIZE_FILL = 9 | 不考虑动画终态内容的宽高比，并且内容始终缩放到组件的大小。 |
| ARKUI_RENDER_FIT_RESIZE_CONTAIN = 10 | 保持动画终态内容的宽高比进行缩小或放大，使内容完整显示在组件内，且与组件保持中心对齐。 |
| ARKUI_RENDER_FIT_RESIZE_CONTAIN_TOP_LEFT = 11 | 保持动画终态内容的宽高比进行缩小或放大，使内容完整显示在组件内。当组件宽方向有剩余时，内容与组件保持左侧对齐，当组件高方向有剩余时，内容与组件保持顶部对齐。 |
| ARKUI_RENDER_FIT_RESIZE_CONTAIN_BOTTOM_RIGHT = 12 | 保持动画终态内容的宽高比进行缩小或放大，使内容完整显示在组件内。当组件宽方向有剩余时，内容与组件保持右侧对齐，当组件高方向有剩余时，内容与组件保持底部对齐。 |
| ARKUI_RENDER_FIT_RESIZE_COVER = 13 | 保持动画终态内容的宽高比进行缩小或放大，使内容两边都大于或等于组件两边，且与组件保持中心对齐，显示内容的中间部分。 |
| ARKUI_RENDER_FIT_RESIZE_COVER_TOP_LEFT = 14 | 保持动画终态内容的宽高比进行缩小或放大，使内容的两边都恰好大于或等于组件两边。当内容宽方向有剩余时，内容与组件保持左侧对齐，显示内容的左侧部分。当内容高方向有剩余时，内容与组件保持顶部对齐，显示内容的顶侧部分。 |
| ARKUI_RENDER_FIT_RESIZE_COVER_BOTTOM_RIGHT = 15 | 保持动画终态内容的宽高比进行缩小或放大，使内容的两边都恰好大于或等于组件两边。当内容宽方向有剩余时，内容与组件保持右侧对齐，显示内容的右侧部分。当内容高方向有剩余时，内容与组件保持底部对齐，显示内容的底侧部分。 |

**ArkUI_SwiperIndicatorType**

```ets
enum ArkUI_SwiperIndicatorType
```

描述：

定义Swiper组件的导航指示器类型。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SWIPER_INDICATOR_TYPE_DOT = 0 | 圆点指示器类型。 |
| ARKUI_SWIPER_INDICATOR_TYPE_DIGIT = 1 | 数字指示器类型。 |

**ArkUI_AnimationDirection**

```ets
enum ArkUI_AnimationDirection
```

描述：

动画播放模式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ANIMATION_DIRECTION_NORMAL = 0 | 动画正向循环播放。 |
| ARKUI_ANIMATION_DIRECTION_REVERSE = 1 | 动画反向循环播放。 |
| ARKUI_ANIMATION_DIRECTION_ALTERNATE = 2 | 动画交替循环播放，奇数次正向播放，偶数次反向播放。 |
| ARKUI_ANIMATION_DIRECTION_ALTERNATE_REVERSE = 3 | 动画反向交替循环播放，奇数次反向播放，偶数次正向播放。 |

**ArkUI_ListItemSwipeActionState**

```ets
enum ArkUI_ListItemSwipeActionState
```

描述：

定义[Listitem](ListItem.md#ZH-CN_TOPIC_0000002553200785__listitem10)组件[SwipeAction](ListItem.md#ZH-CN_TOPIC_0000002553200785__swipeaction9)方法的显隐模式，默认值为ARKUI_LIST_ITEM_SWIPE_ACTION_STATE_COLLAPSED。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_LIST_ITEM_SWIPE_ACTION_STATE_COLLAPSED = 0 | 收起状态，当ListItem与主轴方向相反滑动时操作项处于隐藏状态。 |
| ARKUI_LIST_ITEM_SWIPE_ACTION_STATE_EXPANDED = 1 | 收起状态，当ListItem与主轴方向相反滑动时操作项处于显示状态。 |
| ARKUI_LIST_ITEM_SWIPE_ACTION_STATE_ACTIONING = 2 | 长距离状态，当ListItem进入长距删除区后删除ListItem的状态。 |

**ArkUI_ListItemSwipeEdgeEffect**

```ets
enum ArkUI_ListItemSwipeEdgeEffect
```

描述：

定义Listitem组件[SwipeAction](ListItem.md#ZH-CN_TOPIC_0000002553200785__swipeaction9)方法的滚动模式，默认值为ARKUI_LIST_ITEM_SWIPE_EDGE_EFFECT_SPRING。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_LIST_ITEM_SWIPE_EDGE_EFFECT_SPRING = 0 | ListItem划动距离超过划出组件大小后可以继续划动。 |
| ARKUI_LIST_ITEM_SWIPE_EDGE_EFFECT_NONE = 1 | ListItem划动距离不能超过划出组件大小。 |

**ArkUI_ListItemSwipeActionDirection**

```ets
enum ArkUI_ListItemSwipeActionDirection
```

描述：

ListItem划出菜单的展开方向。

起始版本： 21

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_LIST_ITEM_SWIPE_ACTION_DIRECTION_START = 0 | 当列表方向是垂直方向时，LTR模式下表示ListItem的左边，RTL模式下表示ListItem的右边。当列表是水平方向时，表示ListItem的上边。 |
| ARKUI_LIST_ITEM_SWIPE_ACTION_DIRECTION_END = 1 | 当列表方向是垂直方向时，LTR模式下表示ListItem的右边，RTL模式下表示ListItem的左边。当列表是水平方向时，表示ListItem的下边。 |

**ArkUI_AnimationStatus**

```ets
enum ArkUI_AnimationStatus
```

描述：

定义帧动画的播放状态。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ANIMATION_STATUS_INITIAL = 0 | 动画初始状态。 |
| ARKUI_ANIMATION_STATUS_RUNNING = 1 | 动画处于播放状态。 |
| ARKUI_ANIMATION_STATUS_PAUSED = 2 | 动画处于暂停状态。 |
| ARKUI_ANIMATION_STATUS_STOPPED = 3 | 动画处于停止状态。 |

**ArkUI_AnimationFillMode**

```ets
enum ArkUI_AnimationFillMode
```

描述：

定义帧动画组件在动画开始前和结束后的状态。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ANIMATION_FILL_MODE_NONE = 0 | 动画未执行时不会将任何样式应用于目标，动画播放完成之后恢复初始默认状态。 |
| ARKUI_ANIMATION_FILL_MODE_FORWARDS = 1 | 目标将保留动画执行期间最后一个关键帧的状态。 |
| ARKUI_ANIMATION_FILL_MODE_BACKWARDS = 2 | 动画将在应用于目标时立即应用第一个关键帧中定义的值，并在delay期间保留此值。 |
| ARKUI_ANIMATION_FILL_MODE_BOTH = 3 | 动画将遵循Forwards和Backwards的规则，从而在两个方向上扩展动画属性。 |

**ArkUI_ErrorCode**

```ets
enum ArkUI_ErrorCode
```

描述：

定义错误码枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ERROR_CODE_NO_ERROR = 0 | 无错误。 |
| ARKUI_ERROR_CODE_PARAM_INVALID = 401 | 参数错误。 |
| ARKUI_ERROR_CODE_CAPI_INIT_ERROR = 500 | 接口初始化错误。 起始版本： 18 |
| ARKUI_ERROR_CODE_INTERNAL_ERROR = 100001 | 出现内部错误，例如内部环境错误导致失败，或者由于内部执行失败导致操作失败。 起始版本： 15 |
| ARKUI_ERROR_CODE_PARAM_ERROR = 100023 | 参数错误。错误码的详细介绍请参见自定义节点错误码。 起始版本： 21 |
| ARKUI_ERROR_CODE_XCOMPONENT_STATE_INVALID = 103501 | 当前XComponent状态异常，方法调用失败。错误码的详细介绍请参见XComponent组件错误码。 起始版本： 19 |
| ARKUI_ERROR_CODE_ATTRIBUTE_OR_EVENT_NOT_SUPPORTED = 106102 | 组件不支持特定的属性或者事件。错误码的详细介绍请参见交互事件错误码。 |
| ARKUI_ERROR_CODE_NOT_SUPPROTED_FOR_ARKTS_NODE = 106103 | 不支持对ArkTS创建的节点执行对应的操作。错误码的详细介绍请参见自定义节点错误码。 |
| ARKUI_ERROR_CODE_ADAPTER_NOT_BOUND = 106104 | 懒加载适配器未绑定到组件上。错误码的详细介绍请参见106104-适配器未绑定。 |
| ERROR_CODE_NATIVE_IMPL_NODE_ADAPTER_EXIST = 106105 | 适配器已存在。错误码的详细介绍请参见106105-适配器已存在。 |
| ARKUI_ERROR_CODE_CHILD_NODE_EXIST = 106106 | 对应节点已存在子节点，无法添加适配器。错误码的详细介绍请参见106106-子节点已存在。 |
| ARKUI_ERROR_CODE_NODE_EVENT_PARAM_INDEX_OUT_OF_RANGE = 106107 | 组件事件中参数长度超限。错误码的详细介绍请参见106107-参数下标越界。 |
| ARKUI_ERROR_CODE_NODE_EVENT_PARAM_INVALID = 106108 | 组件事件中不存在该数据。错误码的详细介绍请参见106108-数据不存在。 |
| ARKUI_ERROR_CODE_NODE_EVENT_NO_RETURN = 106109 | 组件事件不支持返回值。错误码的详细介绍请参见106109-不支持返回值。 |
| ARKUI_ERROR_CODE_NODE_UNSUPPORTED_EVENT_TYPE = 106110 | 暂不支持该事件类型。错误码的详细介绍请参见106110-暂不支持该事件类型。 起始版本： 21 |
| ARKUI_ERROR_CODE_NODE_INDEX_INVALID = 106200 | 传入的索引值非法。 错误码的详细介绍请参见106200-传入的索引值非法。 |
| ARKUI_ERROR_CODE_GET_INFO_FAILED = 106201 | 查询路由导航信息失败。 错误码的详细介绍请参见106201-查询路由导航信息失败。 |
| ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR = 106202 | 传入的buffer size异常（数据过大）。 错误码的详细介绍请参见106202-传入的buffer size异常。 |
| ARKUI_ERROR_CODE_NODE_NOT_ON_MAIN_TREE = 106203 | 传入的节点未挂载到组件树上。错误码的详细介绍请参见自定义节点错误码。 起始版本： 15 |
| ARKUI_ERROR_CODE_NODE_ON_INVALID_THREAD = 106204 | 不支持在非UI线程操作传入的节点。错误码的详细介绍请参见自定义节点错误码。 起始版本： 22 |
| ARKUI_ERROR_CODE_FORCE_DARK_CONFIG_INVALID = 106205 | 反色能力入参错误。错误码的详细介绍请参见反色能力错误码。 起始版本： 20 |
| ARKUI_ERROR_CODE_NODE_IS_ADOPTED = 106206 | 节点已被接纳为附属节点。错误码的详细介绍请参见附属节点错误码。 起始版本： 22 |
| ARKUI_ERROR_CODE_NODE_HAS_PARENT = 106207 | 被接纳的节点已有父节点。错误码的详细介绍请参见附属节点错误码。 起始版本： 22 |
| ARKUI_ERROR_CODE_NODE_CAN_NOT_BE_ADOPTED = 106208 | 节点无法被接纳为附属节点。错误码的详细介绍请参见附属节点错误码。 起始版本： 22 |
| ARKUI_ERROR_CODE_NODE_CAN_NOT_ADOPT_TO = 106209 | 节点无法接纳其他节点。错误码的详细介绍请参见附属节点错误码。 起始版本： 22 |
| ARKUI_ERROR_CODE_NODE_IS_NOT_IN_ADOPTED_CHILDREN = 106210 | 节点不是被目标节点接纳的附属节点。错误码的详细介绍请参见附属节点错误码。 起始版本： 22 |
| ARKUI_ERROR_CODE_NOT_CUSTOM_NODE = 106401 | 当前节点不是自定义节点。错误码的详细介绍请参见渲染节点错误码。 起始版本： 20 |
| ARKUI_ERROR_CODE_CHILD_EXISTED = 106402 | 当前节点已存在子节点。错误码的详细介绍请参见渲染节点错误码。 起始版本： 20 |
| ARKUI_ERROR_CODE_RENDER_PARENT_EXISTED = 106403 | 当前渲染节点存在父组件。错误码的详细介绍请参见渲染节点错误码。 起始版本： 20 |
| ARKUI_ERROR_CODE_RENDER_CHILD_NOT_EXIST = 106404 | 未找到对应的渲染子节点。错误码的详细介绍请参见渲染节点错误码。 起始版本： 20 |
| ARKUI_ERROR_CODE_PARAM_OUT_OF_RANGE = 106405 | 参数值超出范围。错误码的详细介绍请参见渲染节点错误码。 起始版本： 20 |
| ARKUI_ERROR_CODE_RENDER_IS_FROM_FRAME_NODE = 106406 | 当前渲染节点从FrameNode中获取。错误码的详细介绍请参见渲染节点错误码。 起始版本： 22 |
| ARKUI_ERROR_CODE_RENDER_HAS_INVALID_FRAME_NODE = 106407 | 当前渲染节点从FrameNode中获取且该FrameNode已被取消接纳为附属节点或销毁。错误码的详细介绍请参见渲染节点错误码。 起始版本： 22 |
| ARKUI_ERROR_CODE_RENDER_NOT_ADOPTED_NODE = 106408 | 当前节点不处于被接纳状态。错误码的详细介绍请参见渲染节点错误码。 起始版本： 22 |
| ARKUI_ERROR_CODE_FOCUS_NON_FOCUSABLE = 150001 | 当前节点无法获得焦点。错误码的详细介绍请参见焦点错误码。 起始版本： 15 |
| ARKUI_ERROR_CODE_FOCUS_NON_FOCUSABLE_ANCESTOR = 150002 | 当前节点对应的祖先节点中存在无法获焦节点。错误码的详细介绍请参见焦点错误码。 起始版本： 15 |
| ARKUI_ERROR_CODE_FOCUS_NON_EXISTENT = 150003 | 当前节点不存在。错误码的详细介绍请参见焦点错误码。 起始版本： 15 |
| ARKUI_ERROR_CODE_COMPONENT_SNAPSHOT_TIMEOUT = 160002 | 截图超时。错误码的详细介绍请参见截图错误码。 起始版本： 15 |
| ARKUI_ERROR_CODE_COMPONENT_SNAPSHOT_MODE_NOT_SUPPORTED = 160003 | 截图选项不支持的色彩空间或动态范围模式。错误码的详细介绍请参见截图错误码。 起始版本： 23 |
| ARKUI_ERROR_CODE_COMPONENT_SNAPSHOT_AUTO_NOT_SUPPORTED = 160004 | 离屏节点截图不支持色彩空间或动态范围模式的isAuto参数设置为true。错误码的详细介绍请参见截图错误码。 起始版本： 23 |
| ARKUI_ERROR_CODE_NON_SCROLLABLE_CONTAINER = 180001 | 非滚动类容器。错误码的详细介绍请参见交互事件错误码。 |
| ARKUI_ERROR_CODE_BUFFER_SIZE_NOT_ENOUGH = 180002 | 存储区大小不足。错误码的详细介绍请参见交互事件错误码。 |
| ARKUI_ERROR_CODE_NOT_CLONED_POINTER_EVENT = 180003 | 该事件不是克隆事件。错误码的详细介绍请参见交互事件错误码。 起始版本： 15 |
| ARKUI_ERROR_CODE_POST_CLONED_COMPONENT_STATUS_ABNORMAL = 180004 | 组件状态异常。错误码的详细介绍请参见交互事件错误码。 起始版本： 15 |
| ARKUI_ERROR_CODE_POST_CLONED_NO_COMPONENT_HIT_TO_RESPOND_TO_THE_EVENT = 180005 | 未命中可响应事件的组件。错误码的详细介绍请参见交互事件错误码。 起始版本： 15 |
| ARKUI_ERROR_INPUT_EVENT_TYPE_NOT_SUPPORTED = 180006 | 接口不支持此输入事件类型。 起始版本： 20 |
| ARKUI_ERROR_CODE_INVALID_STYLED_STRING = 180101 | 无效的属性字符串。错误码的详细介绍请参见属性字符串错误码。 起始版本： 14 |
| ARKUI_ERROR_CODE_UI_CONTEXT_INVALID = 190001 | 无效的UIContext对象。错误码的详细介绍请参见UI上下文错误码。 起始版本： 18 |
| ARKUI_ERROR_CODE_CALLBACK_INVALID = 190002 | 无效的回调函数。错误码的详细介绍请参见UI上下文错误码。 起始版本： 18 |
| ARKUI_ERROR_CODE_RECOGNIZER_TYPE_NOT_SUPPORTED = 180102 | 不支持手势识别器类型。错误码的详细介绍请参见交互事件错误码。 起始版本： 18 |
| ARKUI_ERROR_CODE_DRAG_DROP_OPERATION_NOT_ALLOWED = 190004 | 当前阶段不允许该操作。错误码的详细介绍请参见拖拽事件错误码。 起始版本： 19 |

**ArkUI_ScrollSource**

```ets
enum ArkUI_ScrollSource
```

描述：

定义滚动来源枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SCROLL_SOURCE_DRAG = 0 | 手指拖动。 |
| ARKUI_SCROLL_SOURCE_FLING = 1 | 手指拖动后的惯性滚动。 |
| ARKUI_SCROLL_SOURCE_EDGE_EFFECT = 2 | 在过界时执行EdgeEffect.Spring边缘特效。 |
| ARKUI_SCROLL_SOURCE_OTHER_USER_INPUT = 3 | 除了拖动以外的其他用户输入，如鼠标滚轮、键盘事件等。 |
| ARKUI_SCROLL_SOURCE_SCROLL_BAR = 4 | 拖动滚动条。 |
| ARKUI_SCROLL_SOURCE_SCROLL_BAR_FLING = 5 | 拖动滚动条后的惯性滚动。 |
| ARKUI_SCROLL_SOURCE_SCROLLER = 6 | 滚动控制器引起的无动画的滚动。 |
| ARKUI_SCROLL_SOURCE_ANIMATION = 7 | 滚动控制器引起的带动画的滚动。 |

**ArkUI_SafeAreaType**

```ets
enum ArkUI_SafeAreaType
```

描述：

定义扩展安全区域的枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SAFE_AREA_TYPE_SYSTEM = 1 | 系统默认非安全区域，包括状态栏、导航栏，该值为默认值。 |
| ARKUI_SAFE_AREA_TYPE_CUTOUT = 1 << 1 | 设备的非安全区域，例如刘海屏或挖孔屏区域。 |
| ARKUI_SAFE_AREA_TYPE_KEYBOARD = 1 << 2 | 软键盘区域。 |

**ArkUI_SafeAreaEdge**

```ets
enum ArkUI_SafeAreaEdge
```

描述：

定义扩展安全区域的方向的枚举值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SAFE_AREA_EDGE_TOP = 1 | 上方区域，该值为默认值。 |
| ARKUI_SAFE_AREA_EDGE_BOTTOM = 1 << 1 | 下方区域。 |
| ARKUI_SAFE_AREA_EDGE_START = 1 << 2 | 前部区域。 |
| ARKUI_SAFE_AREA_EDGE_END = 1 << 3 | 尾部区域。 |

**ArkUI_FocusMove**

```ets
enum ArkUI_FocusMove
```

描述：

定义焦点移动方向的枚举值。

起始版本： 18

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_FOCUS_MOVE_FORWARD = 0 | 向前移动焦点。 |
| ARKUI_FOCUS_MOVE_BACKWARD = 1 | 向后移动焦点。 |
| ARKUI_FOCUS_MOVE_UP = 2 | 向上移动焦点。 |
| ARKUI_FOCUS_MOVE_DOWN = 3 | 向下移动焦点。 |
| ARKUI_FOCUS_MOVE_LEFT = 4 | 向左移动焦点。 |
| ARKUI_FOCUS_MOVE_RIGHT = 5 | 向右移动焦点。 |

**ArkUI_ListItemGroupArea**

```ets
enum ArkUI_ListItemGroupArea
```

描述：

定义[ListItemGroup](ListItemGroup.md)组件区域，默认值为ARKUI_LIST_ITEM_GROUP_AREA_OUTSIDE。

起始版本： 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_LIST_ITEM_GROUP_AREA_OUTSIDE = 0 | ListItemGroup区域外。 |
| ARKUI_LIST_ITEM_SWIPE_AREA_NONE = 1 | ListItemGroup没有header、footer和ListItem时的区域。 |
| ARKUI_LIST_ITEM_SWIPE_AREA_ITEM = 2 | ListItemGroup的ListItem区域。 |
| ARKUI_LIST_ITEM_SWIPE_AREA_HEADER = 3 | ListItemGroup的header区域。 |
| ARKUI_LIST_ITEM_SWIPE_AREA_FOOTER = 4 | ListItemGroup的footer区域。 |

**ArkUI_KeyboardAvoidMode**

```ets
enum ArkUI_KeyboardAvoidMode
```

描述：

键盘避让模式。

起始版本： 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_KEYBOARD_AVOID_MODE_DEFAULT = 0 | 默认避让软键盘并在到达极限高度之后进行高度压缩。 |
| ARKUI_KEYBOARD_AVOID_MODE_NONE = 1 | 不避让键盘。 |

**ArkUI_HoverModeAreaType**

```ets
enum ArkUI_HoverModeAreaType
```

描述：

悬停态显示区域。

起始版本： 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_HOVER_MODE_AREA_TYPE_TOP = 0 | 上半屏。 |
| ARKUI_HOVER_MODE_AREA_TYPE_BOTTOM = 1 | 下半屏。 |

**ArkUI_ExpandMode**

```ets
enum ArkUI_ExpandMode
```

描述：

定义子节点展开模式枚举值。

起始版本： 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_NOT_EXPAND = 0 | 不展开。 |
| ARKUI_EXPAND = 1 | 展开。 |
| ARKUI_LAZY_EXPAND = 2 | 懒展开，按需展开当前节点的子节点。 |

**ArkUI_NavDestinationState**

```ets
enum ArkUI_NavDestinationState
```

描述：

定义[NavDestination](NavDestination.md)组件的状态。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_NAV_DESTINATION_STATE_ON_SHOW = 0 | NavDestination组件显示。 |
| ARKUI_NAV_DESTINATION_STATE_ON_HIDE = 1 | NavDestination组件隐藏。 |
| ARKUI_NAV_DESTINATION_STATE_ON_APPEAR = 2 | NavDestination从组件树上挂载。 |
| ARKUI_NAV_DESTINATION_STATE_ON_DISAPPEAR = 3 | NavDestination从组件树上卸载。 |
| ARKUI_NAV_DESTINATION_STATE_ON_WILL_SHOW = 4 | NavDestination组件显示之前。 |
| ARKUI_NAV_DESTINATION_STATE_ON_WILL_HIDE = 5 | NavDestination组件隐藏之前。 |
| ARKUI_NAV_DESTINATION_STATE_ON_WILL_APPEAR = 6 | NavDestination挂载到组件树之前。 |
| ARKUI_NAV_DESTINATION_STATE_ON_WILL_DISAPPEAR = 7 | NavDestination从组件树上卸载之前。 |
| ARKUI_NAV_DESTINATION_STATE_ON_BACK_PRESS = 100 | NavDestination从组件返回。 |

**ArkUI_RouterPageState**

```ets
enum ArkUI_RouterPageState
```

描述：

定义[Router Page](@ohos.router (页面路由)(不推荐).md)（路由页面）的状态。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ROUTER_PAGE_STATE_ABOUT_TO_APPEAR = 0 | Router Page即将创建。 |
| ARKUI_ROUTER_PAGE_STATE_ABOUT_TO_DISAPPEAR = 1 | Router Page即将销毁。 |
| ARKUI_ROUTER_PAGE_STATE_ON_SHOW = 2 | Router Page显示。 |
| ARKUI_ROUTER_PAGE_STATE_ON_HIDE = 3 | Router Page隐藏。 |
| ARKUI_ROUTER_PAGE_STATE_ON_BACK_PRESS = 4 | Router Page返回时。 |

**ArkUI_UIState**

```ets
enum ArkUI_UIState
```

描述：

组件的UI状态枚举，用于处理状态样式。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| UI_STATE_NORMAL = 0 | 正常状态。 |
| UI_STATE_PRESSED = 1 << 0 | 按压状态。 |
| UI_STATE_FOCUSED = 1 << 1 | 获焦状态。 |
| UI_STATE_DISABLED = 1 << 2 | 禁用状态。 |
| UI_STATE_SELECTED = 1 << 3 | 选中状态，此状态仅由某些特定类型的组件支持，分别是Checkbox、Radio、Toggle、List、Grid和MenuItem。 |

**ArkUI_FocusWrapMode**

```ets
enum ArkUI_FocusWrapMode
```

描述：

组件走焦换行规则。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_FOCUS_WRAP_MODE_DEFAULT = 0 | 默认规则，使用方向键走焦不换行。 |
| ARKUI_FOCUS_WRAP_WITH_ARROW = 1 | 使用方向键走焦自动换行。 |

**ArkUI_ItemFillPolicy**

```ets
enum ArkUI_ItemFillPolicy
```

描述：

为不同响应式[断点规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-grid-layout#栅格容器断点)指定列数。

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ITEMFILLPOLICY_NONE = -1 | 没有设置响应式断点规格。 |
| ARKUI_ITEMFILLPOLICY_DEFAULT = 0 | 针对List和Swiper组件：在组件宽度属于sm及更小的断点区间时显示1列，属于md断点区间时显示2列，属于lg及更大的断点区间时显示3列。 针对Grid和WaterFlow组件：在组件宽度属于sm及更小的断点区间时显示2列，属于md断点区间时显示3列，属于lg及更大的断点区间时显示5列。 |
| ARKUI_ITEMFILLPOLICY_SM1MD2LG3 = 1 | 在组件宽度属于sm及更小的断点区间时显示1列，属于md断点区间时显示2列，属于lg及更大的断点区间时显示3列。 |
| ARKUI_ITEMFILLPOLICY_SM2MD3LG5 = 2 | 在组件宽度属于sm及更小的断点区间时显示2列，属于md断点区间时显示3列，属于lg及更大的断点区间时显示5列。 |

**ArkUI_ScrollSnapAnimationSpeed**

```ets
enum ArkUI_ScrollSnapAnimationSpeed
```

描述：

列表限位滚动动画速度。

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SCROLL_SNAP_ANIMATION_NORMAL = 0 | 限位滚动动画速度正常。 |
| ARKUI_SCROLL_SNAP_ANIMATION_SLOW = 1 | 限位滚动动画速度慢。 |

**ArkUI_EdgeDirection**

```ets
enum ArkUI_EdgeDirection
```

描述：

定义矩形边方向。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_EDGE_DIRECTION_ALL = 0 | 设置四个方向的内容。 |
| ARKUI_EDGE_DIRECTION_LEFT = 1 << 0 | 设置左侧方向内容。 |
| ARKUI_EDGE_DIRECTION_RIGHT = 1 << 1 | 设置右侧方向内容。 |
| ARKUI_EDGE_DIRECTION_TOP = 1 << 2 | 设置上侧方向内容。 |
| ARKUI_EDGE_DIRECTION_BOTTOM = 1 << 3 | 设置下侧方向内容。 |

**ArkUI_CornerDirection**

```ets
enum ArkUI_CornerDirection
```

描述：

定义角度方向。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_CORNER_DIRECTION_ALL = 0 | 设置四个角度方向的内容。 |
| ARKUI_CORNER_DIRECTION_TOP_LEFT = 1 << 0 | 设置左上侧方向内容。 |
| ARKUI_CORNER_DIRECTION_TOP_RIGHT = 1 << 1 | 设置右上侧方向内容。 |
| ARKUI_CORNER_DIRECTION_BOTTOM_LEFT = 1 << 2 | 设置左下侧方向内容。 |
| ARKUI_CORNER_DIRECTION_BOTTOM_RIGHT = 1 << 3 | 设置右下侧方向容。 |

**ArkUI_LayoutPolicy**

```ets
enum ArkUI_LayoutPolicy
```

描述：

定义布局策略枚举。

起始版本： 21

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_LAYOUTPOLICY_MATCHPARENT = 0 | 组件自适应父组件布局。 |
| ARKUI_LAYOUTPOLICY_WRAPCONTENT = 1 | 组件自适应子组件（内容），且其大小受父组件内容区大小约束。 |
| ARKUI_LAYOUTPOLICY_FIXATIDEALSIZE = 2 | 组件自适应子组件（内容），且其大小不受父组件内容区大小约束。 |

**ArkUI_PixelRoundCalcPolicy**

```ets
enum ArkUI_PixelRoundCalcPolicy
```

描述：

定义像素取整计算策略枚举。

起始版本： 21

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_PIXELROUNDCALCPOLICY_NOFORCEROUND = 0 | 非取整计算。 |
| ARKUI_PIXELROUNDCALCPOLICY_FORCECEIL = 1 | 向上取整计算。 |
| ARKUI_PIXELROUNDCALCPOLICY_FORCEFLOOR = 2 | 向下取整计算。 |

**ArkUI_GridItemAlignment**

```ets
enum ArkUI_GridItemAlignment
```

描述：

GridItem对齐方式枚举。

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| GRID_ITEM_ALIGNMENT_DEFAULT = 0 | Grid的默认对齐方式。 |
| GRID_ITEM_ALIGNMENT_STRETCH = 1 | 以一行中的最高的GridItem作为其他GridItem的高度。 |

**ArkUI_GridItemStyle**

```ets
enum ArkUI_GridItemStyle
```

描述：

GridItem样式枚举。

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| GRID_ITEM_STYLE_NONE = 0 | 无样式。 |
| GRID_ITEM_STYLE_PLAIN = 1 | 显示Hover、Press态样式。 |

**ArkUI_HoverEffect**

```ets
enum ArkUI_HoverEffect
```

描述：

组件被悬停时的效果。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_HOVER_EFFECT_AUTO = 0 | 默认效果。 |
| ARKUI_HOVER_EFFECT_SCALE | 缩放效果。 |
| ARKUI_HOVER_EFFECT_HIGHLIGHT | 高亮效果。 |
| ARKUI_HOVER_EFFECT_NONE | 无效果。 |

**ArkUI_FocusPriority**

```ets
enum ArkUI_FocusPriority
```

描述：

应用程序内焦点管理的优先级级别。确定UI组件在交互期间接收焦点的顺序。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_FOCUS_PRIORITY_AUTO = 0 | 默认优先级。 |
| ARKUI_FOCUS_PRIORITY_PRIOR = 2000 | 容器内优先获焦的优先级。 |
| ARKUI_FOCUS_PRIORITY_PREVIOUS = 3000 | 上一次容器整体失焦时获焦节点的优先级。 |

**ArkUI_MenuPolicy**

```ets
enum ArkUI_MenuPolicy
```

描述：

菜单弹出策略。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_MENU_POLICY_DEFAULT = 0 | 根据底层默认逻辑确定是否弹出菜单。 |
| ARKUI_MENU_POLICY_HIDE = 1 | 不弹出菜单。 |
| ARKUI_MENU_POLICY_SHOW = 2 | 弹出菜单。 |

**ArkUI_ResponseRegionSupportedTool**

```ets
enum ArkUI_ResponseRegionSupportedTool
```

描述：

定义支持响应区域设置的事件工具类型。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_RESPONSE_REGIN_SUPPORTED_TOOL_ALL = 0 | 所有输入工具类型。 |
| ARKUI_RESPONSE_REGIN_SUPPORTED_TOOL_FINGER = 1 | 手指类型。 |
| ARKUI_RESPONSE_REGIN_SUPPORTED_TOOL_PEN = 2 | 手写笔类型。 |
| ARKUI_RESPONSE_REGIN_SUPPORTED_TOOL_MOUSE = 3 | 鼠标类型。 |

**ArkUI_TextMenuItemId**

```ets
enum ArkUI_TextMenuItemId
```

描述

文本菜单项id枚举。

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_TEXT_MENU_ITEM_ID_CUT = 0 | 裁剪。 |
| ARKUI_TEXT_MENU_ITEM_ID_COPY = 1 | 复制。 |
| ARKUI_TEXT_MENU_ITEM_ID_PASTE = 2 | 粘贴。 |
| ARKUI_TEXT_MENU_ITEM_ID_SELECT_ALL = 3 | 全选。 |
| ARKUI_TEXT_MENU_ITEM_ID_COLLABORATION_SERVICE = 4 | 互通服务。例如跨设备交互，包括跨设备的相机访问等能力。 |
| ARKUI_TEXT_MENU_ITEM_ID_CAMERA_INPUT = 5 | 拍摄输入。 |
| ARKUI_TEXT_MENU_ITEM_ID_AI_WRITER = 6 | AI帮写。该菜单项依赖大模型能力，否则不生效。 |
| ARKUI_TEXT_MENU_ITEM_ID_TRANSLATE = 7 | 翻译。对选中的文本提供翻译服务。 |
| ARKUI_TEXT_MENU_ITEM_ID_SEARCH = 8 | 搜索。对选中的文本提供搜索服务，拉起浏览器搜索选中文本内容。 |
| ARKUI_TEXT_MENU_ITEM_ID_SHARE = 9 | 分享。对选中的文本提供分享服务，拉起分享窗口分享选中文本内容。 |
| ARKUI_TEXT_MENU_ITEM_ID_URL = 10 | 打开链接。对选中的URL提供跳转服务，拉起浏览器搜索或者应用页面。 |
| ARKUI_TEXT_MENU_ITEM_ID_EMAIL = 11 | 新建邮件。对选中的邮箱地址提供跳转服务，拉起邮箱应用。 |
| ARKUI_TEXT_MENU_ITEM_ID_PHONE_NUMBER = 12 | 呼叫。对选中的电话号码跳转服务，拉起电话拨号页面。 |
| ARKUI_TEXT_MENU_ITEM_ID_ADDRESS = 13 | 导航前往。对选中的地址提供跳转服务，拉起地图应用。 |
| ARKUI_TEXT_MENU_ITEM_ID_DATA_TIME = 14 | 新建日程。对选中的日期和时间提供跳转服务，拉起新建日程页面。 |
| ARKUI_TEXT_MENU_ITEM_ID_ASK_AI = 15 | 问问AI。对选中的文本提供AI问询能力。 |
| ARKUI_TEXT_MENU_ITEM_ID_APP_RESERVED_BEGIN = 10000 | 应用自定义菜单项起始id，除了系统内置的菜单项id，应用还可以自定义菜单项id。 |
| ARKUI_TEXT_MENU_ITEM_ID_APP_RESERVED_END = 20000 | 应用自定义菜单项结束id，除了系统内置的菜单项id，应用还可以自定义菜单项id。 |

**ArkUI_TextSpanType**

```ets
enum ArkUI_TextSpanType
```

描述

自定义文本选择菜单的文本识别类型枚举。

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_TEXT_SPAN_TYPE_TEXT = 0 | 选中文本内容为文字类型。 |
| ARKUI_TEXT_SPAN_TYPE_IMAGE = 1 | 选中文本内容为图像类型。 |
| ARKUI_TEXT_SPAN_TYPE_MIXED = 2 | 选中文本内容为图文混合类型。 |
| ARKUI_TEXT_SPAN_TYPE_DEFAULT = 3 | 如果设置为此类型且设置了其他类型时，选中文本后会显示与选中文本内容类型对应的菜单。如果设置为此类型但其他类型未设置时，选中文本后会显示此类型对应的菜单。例如，同时设置了文本识别类型为ARKUI_TEXT_SPAN_TYPE_TEXT、ARKUI_TEXT_SPAN_TYPE_DEFAULT的两个菜单，此时选中文本内容为文字类型会触发ARKUI_TEXT_SPAN_TYPE_TEXT对应的菜单弹出，选中文本内容为图像类型则会触发ARKUI_TEXT_SPAN_TYPE_DEFAULT对应的菜单弹出。 |

**ArkUI_TextResponseType**

```ets
enum ArkUI_TextResponseType
```

描述

自定义文本选择菜单的响应类型枚举。

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_TEXT_RESPONSE_TYPE_RIGHT_CLICK = 0 | 通过鼠标右键触发菜单弹出。 |
| ARKUI_TEXT_RESPONSE_TYPE_LONG_PRESS = 1 | 通过长按触发菜单弹出。 |
| ARKUI_TEXT_RESPONSE_TYPE_SELECT = 2 | 通过鼠标选中触发菜单弹出。 |
| ARKUI_TEXT_RESPONSE_TYPE_DEFAULT = 3 | 如果设置为此类型且设置了其他类型时，触发其他类型的操作会显示对应类型的菜单。如果设置为此类型但其他类型未设置时，触发其他类型的操作会显示此类型对应的菜单。例如，同时设置了响应类型为ARKUI_TEXT_RESPONSE_TYPE_RIGHT_CLICK、ARKUI_TEXT_RESPONSE_TYPE_DEFAULT的两个菜单，此时通过鼠标右键会触发ARKUI_TEXT_RESPONSE_TYPE_RIGHT_CLICK对应的菜单弹出，长按则会触发ARKUI_TEXT_RESPONSE_TYPE_DEFAULT对应的菜单弹出。 |

**ArkUI_MarqueeStartPolicy**

```ets
enum ArkUI_MarqueeStartPolicy
```

描述：

定义跑马灯启动策略枚举。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_MARQUEESTARTPOLICY_DEFAULT = 0 | 默认持续滚动。 |
| ARKUI_MARQUEESTARTPOLICY_ONFOCUS = 1 | 获焦以及鼠标悬浮时开始滚动。 |

**ArkUI_MarqueeUpdatePolicy**

```ets
enum ArkUI_MarqueeUpdatePolicy
```

描述：

定义跑马灯更新策略枚举。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_MARQUEEUPDATEPOLICY_DEFAULT = 0 | 跑马灯组件属性更新后，从开始位置，运行跑马灯效果。 |
| ARKUI_MARQUEEUPDATEPOLICY_PRESERVEPOSITION = 1 | 跑马灯组件属性更新后，保持当前位置，运行跑马灯效果。 |

**ArkUI_LayoutSafeAreaType**

```ets
enum ArkUI_LayoutSafeAreaType
```

描述：

定义扩展安全区域的枚举值。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_LAYOUT_SAFE_AREA_TYPE_SYSTEM = 1 | 系统默认非安全区域，包括状态栏、导航栏。 |

**ArkUI_LayoutSafeAreaEdge**

```ets
enum ArkUI_LayoutSafeAreaEdge
```

描述：

定义扩展安全区域的方向的枚举值。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_LAYOUT_SAFE_AREA_EDGE_TOP = 1 | 上方区域。 |
| ARKUI_LAYOUT_SAFE_AREA_EDGE_BOTTOM = 1 << 1 | 下方区域。 |
| ARKUI_LAYOUT_SAFE_AREA_EDGE_START = 1 << 2 | 前部区域。 |
| ARKUI_LAYOUT_SAFE_AREA_EDGE_END = 1 << 3 | 尾部区域。 |
| ARKUI_LAYOUT_SAFE_AREA_EDGE_VERTICAL = ARKUI_LAYOUT_SAFE_AREA_EDGE_TOP | ARKUI_LAYOUT_SAFE_AREA_EDGE_BOTTOM = 3 | 垂直区域。 |
| ARKUI_LAYOUT_SAFE_AREA_EDGE_HORIZONTAL = ARKUI_LAYOUT_SAFE_AREA_EDGE_START | ARKUI_LAYOUT_SAFE_AREA_EDGE_END = 12 | 水平区域。 |
| ARKUI_LAYOUT_SAFE_AREA_EDGE_ALL = ARKUI_LAYOUT_SAFE_AREA_EDGE_VERTICAL | ARKUI_LAYOUT_SAFE_AREA_EDGE_HORIZONTAL = 15 | 全部区域。 |

**ArkUI_LocalizedAlignment**

```ets
enum ArkUI_LocalizedAlignment
```

描述：

定义Stack容器中子组件的对齐规则。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_LOCALIZED_ALIGNMENT_TOP_START = 0 | 顶部起始。 |
| ARKUI_LOCALIZED_ALIGNMENT_TOP = 1 | 顶部居中。 |
| ARKUI_LOCALIZED_ALIGNMENT_TOP_END = 2 | 顶部尾端。 |
| ARKUI_LOCALIZED_ALIGNMENT_START = 3 | 起始端纵向居中。 |
| ARKUI_LOCALIZED_ALIGNMENT_CENTER = 4 | 横向和纵向居中。 |
| ARKUI_LOCALIZED_ALIGNMENT_END = 5 | 尾端纵向居中。 |
| ARKUI_LOCALIZED_ALIGNMENT_BOTTOM_START = 6 | 底部起始端。 |
| ARKUI_LOCALIZED_ALIGNMENT_BOTTOM = 7 | 底部横向居中。 |
| ARKUI_LOCALIZED_ALIGNMENT_BOTTOM_END = 8 | 底部尾端。 |

**ArkUI_RenderStrategy**

```ets
enum ArkUI_RenderStrategy
```

描述：

定义组件绘制圆角的模式。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_RENDERSTRATEGY_FAST = 0 | 在线绘制模式。 |
| ARKUI_RENDERSTRATEGY_OFFSCREEN = 1 | 离屏绘制模式。 |

**ArkUI_PickerIndicatorType**

```ets
enum ArkUI_PickerIndicatorType
```

描述

选择器的选中指示器类型。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_PICKER_INDICATOR_BACKGROUND = 0 | 背景样式。 |
| ARKUI_PICKER_INDICATOR_DIVIDER = 1 | 分割线样式。 |

**函数说明**

**OH_ArkUI_LayoutConstraint_Create()**

```ets
ArkUI_LayoutConstraint* OH_ArkUI_LayoutConstraint_Create()
```

描述：

创建布局约束。

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_LayoutConstraint* | 创建布局约束的指针。 |

**OH_ArkUI_LayoutConstraint_Copy()**

```ets
ArkUI_LayoutConstraint* OH_ArkUI_LayoutConstraint_Copy(const ArkUI_LayoutConstraint* Constraint)
```

描述：

布局约束深拷贝。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_LayoutConstraint* | 新的布局约束指针。 |

**OH_ArkUI_LayoutConstraint_Dispose()**

```ets
void* OH_ArkUI_LayoutConstraint_Dispose(ArkUI_LayoutConstraint* Constraint)
```

描述：

销毁布局约束指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| void* | 空指针。 |

**OH_ArkUI_LayoutConstraint_GetMaxWidth()**

```ets
int32_t OH_ArkUI_LayoutConstraint_GetMaxWidth(const ArkUI_LayoutConstraint* Constraint)
```

描述：

通过布局约束获取最大宽度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 最大宽度，单位为px。 |

**OH_ArkUI_LayoutConstraint_GetMinWidth()**

```ets
int32_t OH_ArkUI_LayoutConstraint_GetMinWidth(const ArkUI_LayoutConstraint* Constraint)
```

描述：

通过布局约束获取最小宽度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 最小宽度，单位为px。 |

**OH_ArkUI_LayoutConstraint_GetMaxHeight()**

```ets
int32_t OH_ArkUI_LayoutConstraint_GetMaxHeight(const ArkUI_LayoutConstraint* Constraint)
```

描述：

通过布局约束获取最大高度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 最大高度，单位为px。 |

**OH_ArkUI_LayoutConstraint_GetMinHeight()**

```ets
int32_t OH_ArkUI_LayoutConstraint_GetMinHeight(const ArkUI_LayoutConstraint* Constraint)
```

描述：

通过布局约束获取最小高度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 最小高度，单位为px。 |

**OH_ArkUI_LayoutConstraint_GetPercentReferenceWidth()**

```ets
int32_t OH_ArkUI_LayoutConstraint_GetPercentReferenceWidth(const ArkUI_LayoutConstraint* Constraint)
```

描述：

通过布局约束获取宽度百分比基准。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 宽度百分比基准。 |

**OH_ArkUI_LayoutConstraint_GetPercentReferenceHeight()**

```ets
int32_t OH_ArkUI_LayoutConstraint_GetPercentReferenceHeight(const ArkUI_LayoutConstraint* Constraint)
```

描述：

通过布局约束获取高度百分比基准。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 高度百分比基准。 |

**OH_ArkUI_LayoutConstraint_SetMaxWidth()**

```ets
void OH_ArkUI_LayoutConstraint_SetMaxWidth(ArkUI_LayoutConstraint* Constraint, int32_t value)
```

描述：

设置最大宽度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |
| int32_t value | 最大宽度，单位为px，取值范围：[0, +∞)。 |

**OH_ArkUI_LayoutConstraint_SetMinWidth()**

```ets
void OH_ArkUI_LayoutConstraint_SetMinWidth(ArkUI_LayoutConstraint* Constraint, int32_t value)
```

描述：

设置最小宽度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |
| int32_t value | 最小宽度，单位为px，取值范围：[0, +∞)。 |

**OH_ArkUI_LayoutConstraint_SetMaxHeight()**

```ets
void OH_ArkUI_LayoutConstraint_SetMaxHeight(ArkUI_LayoutConstraint* Constraint, int32_t value)
```

描述：

设置最大高度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |
| int32_t value | 最大高度，单位为px，取值范围：[0, +∞)。 |

**OH_ArkUI_LayoutConstraint_SetMinHeight()**

```ets
void OH_ArkUI_LayoutConstraint_SetMinHeight(ArkUI_LayoutConstraint* Constraint, int32_t value)
```

描述：

设置最小高度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |
| int32_t value | 最小高度，单位为px，取值范围：[0, +∞)。 |

**OH_ArkUI_LayoutConstraint_SetPercentReferenceWidth()**

```ets
void OH_ArkUI_LayoutConstraint_SetPercentReferenceWidth(ArkUI_LayoutConstraint* Constraint, int32_t value)
```

描述：

设置宽度百分比基准。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |
| int32_t value | 宽度百分比基准，取值范围：[0, +∞)。 |

**OH_ArkUI_LayoutConstraint_SetPercentReferenceHeight()**

```ets
void OH_ArkUI_LayoutConstraint_SetPercentReferenceHeight(ArkUI_LayoutConstraint* Constraint, int32_t value)
```

描述：

设置高度百分比基准。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |
| int32_t value | 高度百分比基准，取值范围：[0, +∞)。 |

**OH_ArkUI_DrawContext_GetCanvas()**

```ets
void* OH_ArkUI_DrawContext_GetCanvas(ArkUI_DrawContext* context)
```

描述：

获取绘制canvas指针，可以转换为图形库的OH_Drawing_Canvas指针进行绘制。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawContext* context | 绘制上下文。 |

返回：

| 类型 | 说明 |
| --- | --- |
| void* | 用于绘制的canvas指针。 |

**OH_ArkUI_DrawContext_GetSize()**

```ets
ArkUI_IntSize OH_ArkUI_DrawContext_GetSize(ArkUI_DrawContext* context)
```

描述：

获取可绘制区域大小。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawContext* context | 绘制上下文。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_IntSize | 可绘制区域大小。 |

**OH_ArkUI_WaterFlowSectionOption_Create()**

```ets
ArkUI_WaterFlowSectionOption* OH_ArkUI_WaterFlowSectionOption_Create()
```

描述：

创建FlowItem分组配置信息。

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_WaterFlowSectionOption* | FlowItem分组配置信息。 |

**OH_ArkUI_WaterFlowSectionOption_Dispose()**

```ets
void OH_ArkUI_WaterFlowSectionOption_Dispose(ArkUI_WaterFlowSectionOption* option)
```

描述：

销毁FlowItem分组配置信息指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_WaterFlowSectionOption* option | FlowItem分组配置信息。 |

**OH_ArkUI_WaterFlowSectionOption_SetSize()**

```ets
void OH_ArkUI_WaterFlowSectionOption_SetSize(ArkUI_WaterFlowSectionOption* option,int32_t size)
```

描述：

设置FlowItem分组配置信息数组长度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_WaterFlowSectionOption* option | FlowItem分组配置信息。 |
| int32_t size | 数组长度。 |

**OH_ArkUI_WaterFlowSectionOption_GetSize()**

```ets
int32_t OH_ArkUI_WaterFlowSectionOption_GetSize(ArkUI_WaterFlowSectionOption* option)
```

描述：

获取FlowItem分组配置信息数组长度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_WaterFlowSectionOption* option | FlowItem分组配置信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 数组长度。如果返回-1，则返回失败。失败的原因可能是option参数异常，如空指针。 |

**OH_ArkUI_WaterFlowSectionOption_SetItemCount()**

```ets
void OH_ArkUI_WaterFlowSectionOption_SetItemCount(ArkUI_WaterFlowSectionOption* option,int32_t index, int32_t itemCount)
```

描述：

设置分组中FlowItem数量。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_WaterFlowSectionOption* option | FlowItem分组配置信息。 |
| int32_t index | 分组配置信息数组索引值。 |
| int32_t itemCount | 分组中FlowItem数量。 |

**OH_ArkUI_WaterFlowSectionOption_GetItemCount()**

```ets
int32_t OH_ArkUI_WaterFlowSectionOption_GetItemCount(ArkUI_WaterFlowSectionOption* option, int32_t index)
```

描述：

通过FlowItem分组配置信息获取对应索引下的FlowItem数量。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_WaterFlowSectionOption* option | FlowItem分组配置信息。 |
| int32_t index | 分组配置信息数组索引值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 分组中FlowItem数量。 |

**OH_ArkUI_WaterFlowSectionOption_SetCrossCount()**

```ets
void OH_ArkUI_WaterFlowSectionOption_SetCrossCount(ArkUI_WaterFlowSectionOption* option,int32_t index, int32_t crossCount)
```

描述：

设置布局栅格，纵向布局时为列数，横向布局时为行数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_WaterFlowSectionOption* option | FlowItem分组配置信息。 |
| int32_t index | 分组配置信息数组索引值。 |
| int32_t crossCount | 布局栅格数量。 |

**OH_ArkUI_WaterFlowSectionOption_GetCrossCount()**

```ets
int32_t OH_ArkUI_WaterFlowSectionOption_GetCrossCount(ArkUI_WaterFlowSectionOption* option, int32_t index)
```

描述：

通过FlowItem分组配置信息获取对应索引下的布局栅格数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_WaterFlowSectionOption* option | FlowItem分组配置信息。 |
| int32_t index | 分组配置信息数组索引值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 布局栅格数量。 |

**OH_ArkUI_WaterFlowSectionOption_SetColumnGap()**

```ets
void OH_ArkUI_WaterFlowSectionOption_SetColumnGap(ArkUI_WaterFlowSectionOption* option,int32_t index, float columnGap)
```

描述：

设置分组的列间距。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_WaterFlowSectionOption* option | FlowItem分组配置信息。 |
| int32_t index | 分组配置信息数组索引值。 |
| float columnGap | 列间距。 |

**OH_ArkUI_WaterFlowSectionOption_GetColumnGap()**

```ets
float OH_ArkUI_WaterFlowSectionOption_GetColumnGap(ArkUI_WaterFlowSectionOption* option, int32_t index)
```

描述：

通过FlowItem分组配置信息获取对应索引下的分组的列间距。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_WaterFlowSectionOption* option | FlowItem分组配置信息。 |
| int32_t index | 分组配置信息数组索引值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 列间距。 |

**OH_ArkUI_WaterFlowSectionOption_SetRowGap()**

```ets
void OH_ArkUI_WaterFlowSectionOption_SetRowGap(ArkUI_WaterFlowSectionOption* option,int32_t index, float rowGap)
```

描述：

设置分组的行间距。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_WaterFlowSectionOption* option | FlowItem分组配置信息。 |
| int32_t index | 分组配置信息数组索引值。 |
| float rowGap | 行间距。 |

**OH_ArkUI_WaterFlowSectionOption_GetRowGap()**

```ets
float OH_ArkUI_WaterFlowSectionOption_GetRowGap(ArkUI_WaterFlowSectionOption* option, int32_t index)
```

描述：

通过FlowItem分组配置信息获取对应索引下的分组的行间距。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_WaterFlowSectionOption* option | FlowItem分组配置信息。 |
| int32_t index | 分组配置信息数组索引值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 行间距。 |

**OH_ArkUI_WaterFlowSectionOption_SetMargin()**

```ets
void OH_ArkUI_WaterFlowSectionOption_SetMargin(ArkUI_WaterFlowSectionOption* option, int32_t index,float marginTop, float marginRight, float marginBottom, float marginLeft)
```

描述：

设置分组的外边距。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_WaterFlowSectionOption* option | FlowItem分组配置信息。 |
| int32_t index | 分组配置信息数组索引值。 |
| float marginTop | FlowItem上外边距。 |
| float marginRight | FlowItem右外边距。 |
| float marginBottom | FlowItem下外边距。 |
| float marginLeft | FlowItem左外边距。 |

**OH_ArkUI_WaterFlowSectionOption_GetMargin()**

```ets
ArkUI_Margin OH_ArkUI_WaterFlowSectionOption_GetMargin(ArkUI_WaterFlowSectionOption* option, int32_t index)
```

描述：

通过FlowItem分组配置信息获取对应索引下的分组的外边距。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_WaterFlowSectionOption* option | FlowItem分组配置信息。 |
| int32_t index | 分组配置信息数组索引值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_Margin | 外边距。 |

**OH_ArkUI_WaterFlowSectionOption_RegisterGetItemMainSizeCallbackByIndex()**

```ets
void OH_ArkUI_WaterFlowSectionOption_RegisterGetItemMainSizeCallbackByIndex(ArkUI_WaterFlowSectionOption* option,int32_t index, float(*callback)(int32_t itemIndex))
```

描述：

通过FlowItem分组配置信息根据flowItemIndex获取指定Item的主轴大小。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_WaterFlowSectionOption* option | FlowItem分组配置信息。 |
| int32_t index | 分组配置信息数组索引值。 |
| callback | 根据index获取指定Item的主轴大小。itemIndex：FlowItem索引值。 |

**OH_ArkUI_WaterFlowSectionOption_RegisterGetItemMainSizeCallbackByIndexWithUserData()**

```ets
void OH_ArkUI_WaterFlowSectionOption_RegisterGetItemMainSizeCallbackByIndexWithUserData(ArkUI_WaterFlowSectionOption* option, int32_t index, void* userData,float (*callback)(int32_t itemIndex, void* userData))
```

描述：

通过FlowItem分组配置信息根据flowItemIndex获取指定Item的主轴大小。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_WaterFlowSectionOption* option | FlowItem分组配置信息。 |
| int32_t index | 分组配置信息数组索引值。 |
| void* userData | FlowItem自定义数据。 |
| callback | 根据index获取指定Item的主轴大小。itemIndex：FlowItem索引值。 |

**OH_ArkUI_GuidelineOption_Create()**

```ets
ArkUI_GuidelineOption* OH_ArkUI_GuidelineOption_Create(int32_t size)
```

描述：

创建[RelativeContainer](RelativeContainer.md)容器内的辅助线信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| int32_t size | 辅助线数量，取值范围：[0, +∞)。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_GuidelineOption* | 辅助线信息。 |

**OH_ArkUI_GuidelineOption_Dispose()**

```ets
void OH_ArkUI_GuidelineOption_Dispose(ArkUI_GuidelineOption* guideline)
```

描述：

销毁辅助线信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_GuidelineOption* guideline | 辅助线信息。 |

**OH_ArkUI_GuidelineOption_SetId()**

```ets
void OH_ArkUI_GuidelineOption_SetId(ArkUI_GuidelineOption* guideline, const char* value, int32_t index)
```

描述：

设置辅助线的Id。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_GuidelineOption* guideline | 辅助线信息。 |
| const char* value | id，必须是唯一的并且不可与容器内组件重名。 |
| int32_t index | 辅助线索引值。 |

**OH_ArkUI_GuidelineOption_SetDirection()**

```ets
void OH_ArkUI_GuidelineOption_SetDirection(ArkUI_GuidelineOption* guideline, ArkUI_Axis value, int32_t index)
```

描述：

设置辅助线的方向。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_GuidelineOption* guideline | 辅助线信息。 |
| ArkUI_Axis value | 方向。 |
| int32_t index | 辅助线索引值。 |

**OH_ArkUI_GuidelineOption_SetPositionStart()**

```ets
void OH_ArkUI_GuidelineOption_SetPositionStart(ArkUI_GuidelineOption* guideline, float value, int32_t index)
```

描述：

设置距离容器左侧或者顶部的距离。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_GuidelineOption* guideline | 辅助线信息。 |
| float value | 距离容器左侧或者顶部的距离，单位vp。 |
| int32_t index | 辅助线索引值。 |

**OH_ArkUI_GuidelineOption_SetPositionEnd()**

```ets
void OH_ArkUI_GuidelineOption_SetPositionEnd(ArkUI_GuidelineOption* guideline, float value, int32_t index)
```

描述：

设置距离容器右侧或者底部的距离。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_GuidelineOption* guideline | 辅助线信息。 |
| float value | 距离容器右侧或者底部的距离，单位vp。 |
| int32_t index | 辅助线索引值。 |

**OH_ArkUI_GuidelineOption_GetId()**

```ets
const char* OH_ArkUI_GuidelineOption_GetId(ArkUI_GuidelineOption* guideline, int32_t index)
```

描述：

获取辅助线的Id。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_GuidelineOption* guideline | 辅助线信息。 |
| int32_t index | 辅助线索引值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char* | Id。 |

**OH_ArkUI_GuidelineOption_GetDirection()**

```ets
ArkUI_Axis OH_ArkUI_GuidelineOption_GetDirection(ArkUI_GuidelineOption* guideline, int32_t index)
```

描述：

获取辅助线的方向。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_GuidelineOption* guideline | 辅助线信息。 |
| int32_t index | 辅助线索引值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_Axis | 方向。 |

**OH_ArkUI_GuidelineOption_GetPositionStart()**

```ets
float OH_ArkUI_GuidelineOption_GetPositionStart(ArkUI_GuidelineOption* guideline, int32_t index)
```

描述：

获取辅助线距离容器左侧或者顶部的距离。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_GuidelineOption* guideline | 辅助线信息。 |
| int32_t index | 辅助线索引值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 辅助线距离容器左侧或者顶部的距离。单位为vp。 |

**OH_ArkUI_GuidelineOption_GetPositionEnd()**

```ets
float OH_ArkUI_GuidelineOption_GetPositionEnd(ArkUI_GuidelineOption* guideline, int32_t index)
```

描述：

获取辅助线距离容器右侧或者底部的距离。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_GuidelineOption* guideline | 辅助线信息。 |
| int32_t index | 辅助线索引值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 辅助线距离容器右侧或者底部的距离。单位为vp。 |

**OH_ArkUI_BarrierOption_Create()**

```ets
ArkUI_BarrierOption* OH_ArkUI_BarrierOption_Create(int32_t size)
```

描述：

创建RelativeContainer容器内的屏障信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| int32_t size | 屏障数量，取值范围：[0, +∞)。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_BarrierOption* | 屏障信息。 |

**OH_ArkUI_BarrierOption_Dispose()**

```ets
void OH_ArkUI_BarrierOption_Dispose(ArkUI_BarrierOption* barrierStyle)
```

描述：

销毁屏障信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_BarrierOption* barrierStyle | 屏障信息。 |

**OH_ArkUI_BarrierOption_SetId()**

```ets
void OH_ArkUI_BarrierOption_SetId(ArkUI_BarrierOption* barrierStyle, const char* value, int32_t index)
```

描述：

设置屏障的Id。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_BarrierOption* barrierStyle | 屏障信息。 |
| const char* value | id，必须是唯一的并且不可与容器内组件重名。 |
| int32_t index | 屏障索引值。 |

**OH_ArkUI_BarrierOption_SetDirection()**

```ets
void OH_ArkUI_BarrierOption_SetDirection(ArkUI_BarrierOption* barrierStyle, ArkUI_BarrierDirection value, int32_t index)
```

描述：

设置屏障的方向。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_BarrierOption* barrierStyle | 屏障信息。 |
| ArkUI_BarrierDirection value | 方向。 |
| int32_t index | 屏障索引值。 |

**OH_ArkUI_BarrierOption_SetReferencedId()**

```ets
void OH_ArkUI_BarrierOption_SetReferencedId(ArkUI_BarrierOption* barrierStyle, const char* value, int32_t index)
```

描述：

设置屏障的依赖的组件。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_BarrierOption* barrierStyle | 屏障信息。 |
| const char* value | 依赖的组件的Id。 |
| int32_t index | 屏障索引值。 |

**OH_ArkUI_BarrierOption_GetId()**

```ets
const char* OH_ArkUI_BarrierOption_GetId(ArkUI_BarrierOption* barrierStyle, int32_t index)
```

描述：

获取屏障的Id。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_BarrierOption* barrierStyle | 屏障信息。 |
| int32_t index | 屏障索引值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char* | 屏障的Id。 |

**OH_ArkUI_BarrierOption_GetDirection()**

```ets
ArkUI_BarrierDirection OH_ArkUI_BarrierOption_GetDirection(ArkUI_BarrierOption* barrierStyle, int32_t index)
```

描述：

获取屏障的方向。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_BarrierOption* barrierStyle | 屏障信息。 |
| int32_t index | 屏障索引值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_BarrierDirection | 屏障的方向。 |

**OH_ArkUI_BarrierOption_GetReferencedId()**

```ets
const char* OH_ArkUI_BarrierOption_GetReferencedId(ArkUI_BarrierOption* barrierStyle, int32_t index , int32_t referencedIndex)
```

描述：

获取屏障的依赖的组件。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_BarrierOption* barrierStyle | 屏障信息。 |
| int32_t index | 屏障索引值。 |
| int32_t referencedIndex | 依赖的组件Id索引值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char* | 屏障的依赖的组件。 |

**OH_ArkUI_BarrierOption_GetReferencedIdSize()**

```ets
int32_t OH_ArkUI_BarrierOption_GetReferencedIdSize(ArkUI_BarrierOption* barrierStyle, int32_t index)
```

描述：

获取屏障的依赖的组件的个数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_BarrierOption* barrierStyle | 屏障信息。 |
| int32_t index | 屏障索引值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 屏障的依赖的组件的个数。 |

**OH_ArkUI_AlignmentRuleOption_Create()**

```ets
ArkUI_AlignmentRuleOption* OH_ArkUI_AlignmentRuleOption_Create()
```

描述：

创建相对容器中子组件的对齐规则信息。

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_AlignmentRuleOption* | 对齐规则信息。 |

**OH_ArkUI_AlignmentRuleOption_Dispose()**

```ets
void OH_ArkUI_AlignmentRuleOption_Dispose(ArkUI_AlignmentRuleOption* option)
```

描述：

销毁相对容器中子组件的对齐规则信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |

**OH_ArkUI_AlignmentRuleOption_SetStart()**

```ets
void OH_ArkUI_AlignmentRuleOption_SetStart(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_HorizontalAlignment alignment)
```

描述：

设置相对布局的左对齐方式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
| const char* id | 锚点的组件的id值。 |
| ArkUI_HorizontalAlignment alignment | 相对于锚点组件的对齐方式。 |

**OH_ArkUI_AlignmentRuleOption_SetEnd()**

```ets
void OH_ArkUI_AlignmentRuleOption_SetEnd(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_HorizontalAlignment alignment)
```

描述：

设置相对布局的右对齐方式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
| const char* id | 锚点的组件的id值。 |
| ArkUI_HorizontalAlignment alignment | 相对于锚点组件的对齐方式。 |

**OH_ArkUI_AlignmentRuleOption_SetCenterHorizontal()**

```ets
void OH_ArkUI_AlignmentRuleOption_SetCenterHorizontal(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_HorizontalAlignment alignment)
```

描述：

设置相对布局的横向居中对齐方式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
| const char* id | 锚点的组件的id值。 |
| ArkUI_HorizontalAlignment alignment | 相对于锚点组件的对齐方式 |

**OH_ArkUI_AlignmentRuleOption_SetTop()**

```ets
void OH_ArkUI_AlignmentRuleOption_SetTop(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_VerticalAlignment alignment)
```

描述：

设置相对布局的顶部对齐的方式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
| const char* id | 锚点的组件的id值。 |
| ArkUI_VerticalAlignment alignment | 相对于锚点组件的对齐方式 |

**OH_ArkUI_AlignmentRuleOption_SetBottom()**

```ets
void OH_ArkUI_AlignmentRuleOption_SetBottom(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_VerticalAlignment alignment)
```

描述：

设置相对布局的底部对齐的方式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
| const char* id | 锚点的组件的id值。 |
| ArkUI_VerticalAlignment alignment | 相对于锚点组件的对齐方式 |

**OH_ArkUI_AlignmentRuleOption_SetCenterVertical()**

```ets
void OH_ArkUI_AlignmentRuleOption_SetCenterVertical(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_VerticalAlignment alignment)
```

描述：

设置相对布局的纵向居中对齐方式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
| const char* id | 锚点的组件的id值。 |
| ArkUI_VerticalAlignment alignment | 相对于锚点组件的对齐方式。 |

**OH_ArkUI_AlignmentRuleOption_SetBiasHorizontal()**

```ets
void OH_ArkUI_AlignmentRuleOption_SetBiasHorizontal(ArkUI_AlignmentRuleOption* option, float horizontal)
```

描述：

设置组件在锚点约束下的水平方向上偏移参数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
| float horizontal | 水平方向上的bias值。 |

**OH_ArkUI_AlignmentRuleOption_SetBiasVertical()**

```ets
void OH_ArkUI_AlignmentRuleOption_SetBiasVertical(ArkUI_AlignmentRuleOption* option, float vertical)
```

描述：

设置组件在锚点约束下的垂直方向上偏移参数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
| float vertical | 垂直方向上的bias值。 |

**OH_ArkUI_AlignmentRuleOption_GetStartId()**

```ets
const char* OH_ArkUI_AlignmentRuleOption_GetStartId(ArkUI_AlignmentRuleOption* option)
```

描述：

获取左对齐锚点组件的Id。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char* | 左对齐锚点组件的Id。 |

**OH_ArkUI_AlignmentRuleOption_GetStartAlignment()**

```ets
ArkUI_HorizontalAlignment OH_ArkUI_AlignmentRuleOption_GetStartAlignment(ArkUI_AlignmentRuleOption* option)
```

描述：

获取左对齐方式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_HorizontalAlignment | 参数的对齐方式。 |

**OH_ArkUI_AlignmentRuleOption_GetEndId()**

```ets
const char* OH_ArkUI_AlignmentRuleOption_GetEndId(ArkUI_AlignmentRuleOption* option)
```

描述：

获取右对齐锚点组件的Id。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char* | 右对齐锚点组件的Id。 |

**OH_ArkUI_AlignmentRuleOption_GetEndAlignment()**

```ets
ArkUI_HorizontalAlignment OH_ArkUI_AlignmentRuleOption_GetEndAlignment(ArkUI_AlignmentRuleOption* option)
```

描述：

获取右对齐方式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_HorizontalAlignment | 右对齐方式。 |

**OH_ArkUI_AlignmentRuleOption_GetCenterIdHorizontal()**

```ets
const char* OH_ArkUI_AlignmentRuleOption_GetCenterIdHorizontal(ArkUI_AlignmentRuleOption* option)
```

描述：

获取横向居中对齐锚点组件的Id。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char* | 横向居中对齐锚点组件的Id。 |

**OH_ArkUI_AlignmentRuleOption_GetCenterAlignmentHorizontal()**

```ets
ArkUI_HorizontalAlignment OH_ArkUI_AlignmentRuleOption_GetCenterAlignmentHorizontal(ArkUI_AlignmentRuleOption* option)
```

描述：

获取横向居中对齐方式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_HorizontalAlignment | 横向居中对齐方式。 |

**OH_ArkUI_AlignmentRuleOption_GetTopId()**

```ets
const char* OH_ArkUI_AlignmentRuleOption_GetTopId(ArkUI_AlignmentRuleOption* option)
```

描述：

获取顶部对齐锚点组件的Id。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char* | 顶部对齐锚点组件的Id。 |

**OH_ArkUI_AlignmentRuleOption_GetTopAlignment()**

```ets
ArkUI_VerticalAlignment OH_ArkUI_AlignmentRuleOption_GetTopAlignment(ArkUI_AlignmentRuleOption* option)
```

描述：

获取顶部对齐的方式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_VerticalAlignment | 顶部对齐的方式。 |

**OH_ArkUI_AlignmentRuleOption_GetBottomId()**

```ets
const char* OH_ArkUI_AlignmentRuleOption_GetBottomId(ArkUI_AlignmentRuleOption* option)
```

描述：

获取底部对齐锚点组件的Id。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char* | 底部对齐锚点组件的Id。 |

**OH_ArkUI_AlignmentRuleOption_GetBottomAlignment()**

```ets
ArkUI_VerticalAlignment OH_ArkUI_AlignmentRuleOption_GetBottomAlignment(ArkUI_AlignmentRuleOption* option)
```

描述：

获取底部对齐的方式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_VerticalAlignment | 底部对齐的方式。 |

**OH_ArkUI_AlignmentRuleOption_GetCenterIdVertical()**

```ets
const char* OH_ArkUI_AlignmentRuleOption_GetCenterIdVertical(ArkUI_AlignmentRuleOption* option)
```

描述：

获取纵向居中对齐锚点组件的Id。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char* | 纵向居中对齐锚点组件的Id。 |

**OH_ArkUI_AlignmentRuleOption_GetCenterAlignmentVertical()**

```ets
ArkUI_VerticalAlignment OH_ArkUI_AlignmentRuleOption_GetCenterAlignmentVertical(ArkUI_AlignmentRuleOption* option)
```

描述：

获取纵向居中对齐方式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_VerticalAlignment | 纵向居中对齐方式。 |

**OH_ArkUI_AlignmentRuleOption_GetBiasHorizontal()**

```ets
float OH_ArkUI_AlignmentRuleOption_GetBiasHorizontal(ArkUI_AlignmentRuleOption* option)
```

描述：

获取水平方向上的bias值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 水平方向上的bias值。 |

**OH_ArkUI_AlignmentRuleOption_GetBiasVertical()**

```ets
float OH_ArkUI_AlignmentRuleOption_GetBiasVertical(ArkUI_AlignmentRuleOption* option)
```

描述：

获取垂直方向上的bias值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 垂直方向上的bias值。 |

**OH_ArkUI_SwiperIndicator_Create()**

```ets
ArkUI_SwiperIndicator* OH_ArkUI_SwiperIndicator_Create(ArkUI_SwiperIndicatorType type)
```

描述：

创建Swiper组件的导航指示器。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicatorType type | 导航指示器的类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_SwiperIndicator* | 导航指示器对象指针。 |

**OH_ArkUI_SwiperIndicator_Dispose()**

```ets
void OH_ArkUI_SwiperIndicator_Dispose(ArkUI_SwiperIndicator* indicator)
```

描述：

销毁Swiper组件的导航指示器指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |

**OH_ArkUI_SwiperIndicator_SetStartPosition()**

```ets
void OH_ArkUI_SwiperIndicator_SetStartPosition(ArkUI_SwiperIndicator* indicator, float value)
```

描述：

设置导航点距离Swiper组件左边的距离。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| float value | 导航点距离Swiper组件左边的距离。默认值：0，单位：vp。 |

**OH_ArkUI_SwiperIndicator_GetStartPosition()**

```ets
float OH_ArkUI_SwiperIndicator_GetStartPosition(ArkUI_SwiperIndicator* indicator)
```

描述：

获取导航点距离Swiper组件左边的距离。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 导航点距离Swiper组件左边的距离。单位：vp。 |

**OH_ArkUI_SwiperIndicator_SetTopPosition()**

```ets
void OH_ArkUI_SwiperIndicator_SetTopPosition(ArkUI_SwiperIndicator* indicator, float value)
```

描述：

设置导航点距离Swiper组件顶部的距离。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| float value | 导航点距离Swiper组件顶部的距离。默认值：0，单位：vp。 |

**OH_ArkUI_SwiperIndicator_GetTopPosition()**

```ets
float OH_ArkUI_SwiperIndicator_GetTopPosition(ArkUI_SwiperIndicator* indicator)
```

描述：

获取导航点距离Swiper组件顶部的距离。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 导航点距离Swiper组件顶部的距离。单位：vp。 |

**OH_ArkUI_SwiperIndicator_SetEndPosition()**

```ets
void OH_ArkUI_SwiperIndicator_SetEndPosition(ArkUI_SwiperIndicator* indicator, float value)
```

描述：

设置导航点距离Swiper组件右边的距离。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| float value | 导航点距离Swiper组件右边的距离。默认值：0，单位：vp。 |

**OH_ArkUI_SwiperIndicator_GetEndPosition()**

```ets
float OH_ArkUI_SwiperIndicator_GetEndPosition(ArkUI_SwiperIndicator* indicator)
```

描述：

获取导航点距离Swiper组件右边的距离。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 导航点距离Swiper组件右边的距离。单位：vp。 |

**OH_ArkUI_SwiperIndicator_SetBottomPosition()**

```ets
void OH_ArkUI_SwiperIndicator_SetBottomPosition(ArkUI_SwiperIndicator* indicator, float value)
```

描述：

设置导航点距离Swiper组件底部的距离。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| float value | 导航点距离Swiper组件底部的距离。默认值：0，单位：vp。 |

**OH_ArkUI_SwiperIndicator_GetBottomPosition()**

```ets
float OH_ArkUI_SwiperIndicator_GetBottomPosition(ArkUI_SwiperIndicator* indicator)
```

描述：

获取导航点距离Swiper组件底部的距离。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 导航点距离Swiper组件底部的距离。单位：vp。 |

**OH_ArkUI_SwiperIndicator_SetIgnoreSizeOfBottom()**

```ets
void OH_ArkUI_SwiperIndicator_SetIgnoreSizeOfBottom(ArkUI_SwiperIndicator* indicator, int32_t ignoreSize)
```

描述：

设置OH_ArkUI_SwiperIndicator_SetBottomPosition是否忽略导航点大小。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| int32_t ignoreSize | 是否忽略导航点大小。1表示忽略导航点大小，0表示不忽略，默认值0。 |

**OH_ArkUI_SwiperIndicator_GetIgnoreSizeOfBottom()**

```ets
int32_t OH_ArkUI_SwiperIndicator_GetIgnoreSizeOfBottom(ArkUI_SwiperIndicator* indicator)
```

描述：

获取OH_ArkUI_SwiperIndicator_SetBottomPosition是否忽略导航点大小。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 是否忽略导航点大小。 |

**OH_ArkUI_SwiperIndicator_SetItemWidth()**

```ets
void OH_ArkUI_SwiperIndicator_SetItemWidth(ArkUI_SwiperIndicator* indicator, float value)
```

描述：

设置Swiper组件圆点导航指示器的宽。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| float value | 圆点导航指示器的宽。默认值：12，单位：vp。 |

**OH_ArkUI_SwiperIndicator_GetItemWidth()**

```ets
float OH_ArkUI_SwiperIndicator_GetItemWidth(ArkUI_SwiperIndicator* indicator)
```

描述：

获取Swiper组件圆点导航指示器的宽。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 圆点导航指示器的宽。单位：vp。 |

**OH_ArkUI_SwiperIndicator_SetItemHeight()**

```ets
void OH_ArkUI_SwiperIndicator_SetItemHeight(ArkUI_SwiperIndicator* indicator, float value)
```

描述：

设置Swiper组件圆点导航指示器的高。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| float value | 圆点导航指示器的高。默认值：6，单位：vp。 |

**OH_ArkUI_SwiperIndicator_GetItemHeight()**

```ets
float OH_ArkUI_SwiperIndicator_GetItemHeight(ArkUI_SwiperIndicator* indicator)
```

描述：

获取Swiper组件圆点导航指示器的高。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 圆点导航指示器的高。单位：vp。 |

**OH_ArkUI_SwiperIndicator_SetSelectedItemWidth()**

```ets
void OH_ArkUI_SwiperIndicator_SetSelectedItemWidth(ArkUI_SwiperIndicator* indicator, float value)
```

描述：

设置被选中的Swiper组件圆点导航指示器的宽。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| float value | 圆点导航指示器的宽。默认值：12，单位：vp。 |

**OH_ArkUI_SwiperIndicator_GetSelectedItemWidth()**

```ets
float OH_ArkUI_SwiperIndicator_GetSelectedItemWidth(ArkUI_SwiperIndicator* indicator)
```

描述：

获取被选中Swiper组件圆点导航指示器的宽。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 圆点导航指示器的宽。单位：vp。 |

**OH_ArkUI_SwiperIndicator_SetSelectedItemHeight()**

```ets
void OH_ArkUI_SwiperIndicator_SetSelectedItemHeight(ArkUI_SwiperIndicator* indicator, float value)
```

描述：

设置被选中的Swiper组件圆点导航指示器的高。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| float value | 圆点导航指示器的高。默认值：6，单位：vp。 |

**OH_ArkUI_SwiperIndicator_GetSelectedItemHeight()**

```ets
float OH_ArkUI_SwiperIndicator_GetSelectedItemHeight(ArkUI_SwiperIndicator* indicator)
```

描述：

获取被选中Swiper组件圆点导航指示器的高。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 圆点导航指示器的高。单位：vp。 |

**OH_ArkUI_SwiperIndicator_SetMask()**

```ets
void OH_ArkUI_SwiperIndicator_SetMask(ArkUI_SwiperIndicator* indicator, int32_t mask)
```

描述：

设置是否显示Swiper组件圆点导航指示器的蒙版样式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| int32_t mask | 是否显示蒙版样式，1表示显示，0表示不显示。 默认值：0 |

**OH_ArkUI_SwiperIndicator_GetMask()**

```ets
int32_t OH_ArkUI_SwiperIndicator_GetMask(ArkUI_SwiperIndicator* indicator)
```

描述：

获取是否显示Swiper组件圆点导航指示器的蒙版样式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回1表示显示圆点导航指示器的蒙版样式，返回0表示不显示。 |

**OH_ArkUI_SwiperIndicator_SetColor()**

```ets
void OH_ArkUI_SwiperIndicator_SetColor(ArkUI_SwiperIndicator* indicator, uint32_t color)
```

描述：

设置Swiper组件圆点导航指示器的颜色。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| uint32_t color | 颜色类型，0xargb格式，形如 0xFFFF0000 表示红色。 默认值：'#1A182431'，浅灰色。 |

**OH_ArkUI_SwiperIndicator_GetColor()**

```ets
uint32_t OH_ArkUI_SwiperIndicator_GetColor(ArkUI_SwiperIndicator* indicator)
```

描述：

获取Swiper组件圆点导航指示器的颜色。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| uint32_t | 颜色类型，0xargb格式，形如 0xFFFF0000 表示红色。 |

**OH_ArkUI_SwiperIndicator_SetSelectedColor()**

```ets
void OH_ArkUI_SwiperIndicator_SetSelectedColor(ArkUI_SwiperIndicator* indicator, uint32_t selectedColor)
```

描述：

设置被选中Swiper组件圆点导航指示器的颜色。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| uint32_t selectedColor | 颜色类型，0xargb格式，形如 0xFFFF0000 表示红色。 |

**OH_ArkUI_SwiperIndicator_GetSelectedColor()**

```ets
uint32_t OH_ArkUI_SwiperIndicator_GetSelectedColor(ArkUI_SwiperIndicator* indicator)
```

描述：

获取被选中Swiper组件圆点导航指示器的颜色。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| uint32_t | 颜色类型，0xargb格式，形如 0xFFFF0000 表示红色。 |

**OH_ArkUI_SwiperIndicator_SetMaxDisplayCount()**

```ets
int32_t OH_ArkUI_SwiperIndicator_SetMaxDisplayCount(ArkUI_SwiperIndicator* indicator, int32_t maxDisplayCount)
```

描述：

设置圆点导航点指示器样式下，导航点显示个数的最大值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| int32_t maxDisplayCount | 导航点显示个数最大值，有效取值范围[6, 9]。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 如果maxDisplayCount设置范围错误, 返回错误码。 |

**OH_ArkUI_SwiperIndicator_GetMaxDisplayCount()**

```ets
int32_t OH_ArkUI_SwiperIndicator_GetMaxDisplayCount(ArkUI_SwiperIndicator* indicator)
```

描述：

获取圆点导航点指示器样式下，导航点显示个数的最大值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 导航点显示个数最大值，有效取值范围[6, 9]。 |

**OH_ArkUI_SwiperDigitIndicator_Create()**

```ets
ArkUI_SwiperDigitIndicator *OH_ArkUI_SwiperDigitIndicator_Create()
```

描述：

创建Swiper组件的数字导航指示器。

起始版本： 19

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_SwiperDigitIndicator * | 数字导航指示器对象指针。 |

**OH_ArkUI_SwiperDigitIndicator_Destroy()**

```ets
void OH_ArkUI_SwiperDigitIndicator_Destroy(ArkUI_SwiperDigitIndicator* indicator)
```

描述：

销毁Swiper组件的数字导航指示器指针。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |

**OH_ArkUI_SwiperDigitIndicator_SetStartPosition()**

```ets
void OH_ArkUI_SwiperDigitIndicator_SetStartPosition(ArkUI_SwiperDigitIndicator* indicator, float value)
```

描述：

设置数字导航指示器距离Swiper组件左边的距离。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
| float value | 数字导航指示器距离Swiper组件左边的距离，在从左至右显示的语言模式下，设置距离Swiper组件左边的距离；在从右至左显示的语言模式下，设置距离Swiper组件右边的距离。 默认值：0 单位：vp |

**OH_ArkUI_SwiperDigitIndicator_GetStartPosition()**

```ets
float OH_ArkUI_SwiperDigitIndicator_GetStartPosition(ArkUI_SwiperDigitIndicator* indicator)
```

描述：

获取数字导航指示器距离Swiper组件左边的距离。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 数字导航指示器距离Swiper组件左边的距离，在从左至右显示的语言模式下，返回距离Swiper组件左边的距离；在从右至左显示的语言模式下，返回距离Swiper组件右边的距离。 单位：vp |

**OH_ArkUI_SwiperDigitIndicator_SetTopPosition()**

```ets
void OH_ArkUI_SwiperDigitIndicator_SetTopPosition(ArkUI_SwiperDigitIndicator* indicator, float value)
```

描述：

设置数字导航指示器距离Swiper组件顶部的距离。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
| float value | 数字导航指示器距离Swiper组件顶部的距离。默认值：0，单位：vp。 |

**OH_ArkUI_SwiperDigitIndicator_GetTopPosition()**

```ets
float OH_ArkUI_SwiperDigitIndicator_GetTopPosition(ArkUI_SwiperDigitIndicator* indicator)
```

描述：

获取数字导航指示器距离Swiper组件顶部的距离。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 数字导航指示器距离Swiper组件顶部的距离。单位：vp。 |

**OH_ArkUI_SwiperDigitIndicator_SetEndPosition()**

```ets
void OH_ArkUI_SwiperDigitIndicator_SetEndPosition(ArkUI_SwiperDigitIndicator* indicator, float value)
```

描述：

设置数字导航指示器距离Swiper组件右边的距离。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
| float value | 数字导航指示器距离Swiper组件右边的距离。在从左至右显示的语言模式下，设置距离Swiper组件右边的距离；在从右至左显示的语言模式下，设置距离Swiper组件左边的距离。 默认值：0 单位：vp |

**OH_ArkUI_SwiperDigitIndicator_GetEndPosition()**

```ets
float OH_ArkUI_SwiperDigitIndicator_GetEndPosition(ArkUI_SwiperDigitIndicator* indicator)
```

描述：

获取数字导航指示器距离Swiper组件右边的距离。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 数字导航指示器距离Swiper组件右边的距离。在从左至右显示的语言模式下，返回距离Swiper组件右边的距离；在从右至左显示的语言模式下，返回距离Swiper组件左边的距离。 单位：vp |

**OH_ArkUI_SwiperDigitIndicator_SetBottomPosition()**

```ets
void OH_ArkUI_SwiperDigitIndicator_SetBottomPosition(ArkUI_SwiperDigitIndicator* indicator, float value)
```

描述：

设置数字导航指示器距离Swiper组件底部的距离。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
| float value | 数字导航指示器距离Swiper组件底部的距离。默认值：0，单位：vp。 |

**OH_ArkUI_SwiperDigitIndicator_GetBottomPosition()**

```ets
float OH_ArkUI_SwiperDigitIndicator_GetBottomPosition(ArkUI_SwiperDigitIndicator* indicator)
```

描述：

获取数字导航指示器距离Swiper组件底部的距离。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 数字导航指示器距离Swiper组件底部的距离。单位：vp。 |

**OH_ArkUI_SwiperDigitIndicator_SetFontColor()**

```ets
void OH_ArkUI_SwiperDigitIndicator_SetFontColor(ArkUI_SwiperDigitIndicator* indicator, uint32_t color)
```

描述：

设置Swiper组件数字导航指示器字体颜色。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
| uint32_t color | 颜色类型，0xargb格式，形如 0xFFFF0000 表示红色。默认值：0xFF182431。 |

**OH_ArkUI_SwiperDigitIndicator_GetFontColor()**

```ets
uint32_t OH_ArkUI_SwiperDigitIndicator_GetFontColor(ArkUI_SwiperDigitIndicator* indicator)
```

描述：

获取Swiper组件数字导航指示器字体颜色。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| uint32_t | 颜色类型，0xargb格式，形如 0xFFFF0000 表示红色。 |

**OH_ArkUI_SwiperDigitIndicator_SetSelectedFontColor()**

```ets
void OH_ArkUI_SwiperDigitIndicator_SetSelectedFontColor(ArkUI_SwiperDigitIndicator* indicator, uint32_t selectedColor)
```

描述：

设置被选中Swiper组件数字导航指示器字体颜色。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
| uint32_t selectedColor | 颜色类型，0xargb格式，形如 0xFFFF0000 表示红色。默认值：0xFF182431。 |

**OH_ArkUI_SwiperDigitIndicator_GetSelectedFontColor()**

```ets
uint32_t OH_ArkUI_SwiperDigitIndicator_GetSelectedFontColor(ArkUI_SwiperDigitIndicator* indicator)
```

描述：

获取被选中Swiper组件数字导航指示器字体颜色。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| uint32_t | 颜色类型，0xargb格式，形如 0xFFFF0000 表示红色。 |

**OH_ArkUI_SwiperDigitIndicator_SetFontSize()**

```ets
void OH_ArkUI_SwiperDigitIndicator_SetFontSize(ArkUI_SwiperDigitIndicator* indicator, float size)
```

描述：

设置Swiper组件数字导航指示器字体大小。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
| float size | 字体大小数值，单位为fp。 默认值：14 |

**OH_ArkUI_SwiperDigitIndicator_GetFontSize()**

```ets
float OH_ArkUI_SwiperDigitIndicator_GetFontSize(ArkUI_SwiperDigitIndicator* indicator)
```

描述：

获取Swiper组件数字导航指示器字体大小。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 字体大小数值，单位为fp。 |

**OH_ArkUI_SwiperDigitIndicator_SetSelectedFontSize()**

```ets
void OH_ArkUI_SwiperDigitIndicator_SetSelectedFontSize(ArkUI_SwiperDigitIndicator* indicator, float size)
```

描述：

设置被选中Swiper组件数字导航指示器字体大小。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
| float size | 字体大小数值，单位为fp。 默认值：14 |

**OH_ArkUI_SwiperDigitIndicator_GetSelectedFontSize()**

```ets
float OH_ArkUI_SwiperDigitIndicator_GetSelectedFontSize(ArkUI_SwiperDigitIndicator* indicator)
```

描述：

获取被选中Swiper组件数字导航指示器字体大小。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 字体大小数值，单位为fp。 |

**OH_ArkUI_SwiperDigitIndicator_SetFontWeight()**

```ets
void OH_ArkUI_SwiperDigitIndicator_SetFontWeight(ArkUI_SwiperDigitIndicator *indicator, ArkUI_FontWeight fontWeight)
```

描述：

设置Swiper组件数字导航指示器字体粗细属性。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator *indicator | 数字导航指示器对象指针。 |
| ArkUI_FontWeight fontWeight | 字体粗细样式ArkUI_FontWeight。 |

**OH_ArkUI_SwiperDigitIndicator_GetFontWeight()**

```ets
ArkUI_FontWeight OH_ArkUI_SwiperDigitIndicator_GetFontWeight(ArkUI_SwiperDigitIndicator* indicator)
```

描述：

获取Swiper组件数字导航指示器字体粗细属性。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_FontWeight | 字体粗细样式ArkUI_FontWeight。 |

**OH_ArkUI_SwiperDigitIndicator_SetSelectedFontWeight()**

```ets
void OH_ArkUI_SwiperDigitIndicator_SetSelectedFontWeight(ArkUI_SwiperDigitIndicator *indicator, ArkUI_FontWeight selectedFontWeight)
```

描述：

设置被选中Swiper组件数字导航指示器字体粗细属性。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator *indicator | 数字导航指示器对象指针。 |
| ArkUI_FontWeight selectedFontWeight | 字体粗细样式ArkUI_FontWeight。 |

**OH_ArkUI_SwiperDigitIndicator_GetSelectedFontWeight()**

```ets
ArkUI_FontWeight OH_ArkUI_SwiperDigitIndicator_GetSelectedFontWeight(ArkUI_SwiperDigitIndicator* indicator)
```

描述：

获取被选中Swiper组件数字导航指示器字体粗细属性。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_FontWeight | 字体粗细样式ArkUI_FontWeight。 |

**OH_ArkUI_SwiperArrowStyle_Create()**

```ets
ArkUI_SwiperArrowStyle *OH_ArkUI_SwiperArrowStyle_Create()
```

描述：

创建Swiper组件的导航箭头。

起始版本： 19

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_SwiperArrowStyle * | 导航箭头对象指针。 |

**OH_ArkUI_SwiperArrowStyle_Destroy()**

```ets
void OH_ArkUI_SwiperArrowStyle_Destroy(ArkUI_SwiperArrowStyle* arrowStyle)
```

描述：

销毁Swiper组件的导航箭头指针。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |

**OH_ArkUI_SwiperArrowStyle_SetShowBackground()**

```ets
void OH_ArkUI_SwiperArrowStyle_SetShowBackground(ArkUI_SwiperArrowStyle* arrowStyle, int32_t showBackground)
```

描述：

设置Swiper组件导航箭头底板是否显示。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |
| int32_t showBackground | 导航箭头底板是否显示，0：不显示，1：显示，默认值：0。 |

**OH_ArkUI_SwiperArrowStyle_GetShowBackground()**

```ets
int32_t OH_ArkUI_SwiperArrowStyle_GetShowBackground(ArkUI_SwiperArrowStyle* arrowStyle)
```

描述：

获取Swiper组件导航箭头底板是否显示。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 导航箭头底板是否显示，0：不显示，1：显示。 |

**OH_ArkUI_SwiperArrowStyle_SetShowSidebarMiddle()**

```ets
void OH_ArkUI_SwiperArrowStyle_SetShowSidebarMiddle(ArkUI_SwiperArrowStyle* arrowStyle, int32_t showSidebarMiddle)
```

描述：

设置Swiper组件导航箭头显示位置。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |
| int32_t showSidebarMiddle | 导航箭头显示位置，0：显示在导航指示器两侧，1：显示在Swiper组件两侧，默认值：0。 |

**OH_ArkUI_SwiperArrowStyle_GetShowSidebarMiddle()**

```ets
int32_t OH_ArkUI_SwiperArrowStyle_GetShowSidebarMiddle(ArkUI_SwiperArrowStyle* arrowStyle)
```

描述：

获取Swiper组件导航箭头显示位置。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 导航箭头显示位置，0：显示在导航指示器两侧，1：显示在Swiper组件两侧。 |

**OH_ArkUI_SwiperArrowStyle_SetBackgroundSize()**

```ets
void OH_ArkUI_SwiperArrowStyle_SetBackgroundSize(ArkUI_SwiperArrowStyle* arrowStyle, float backgroundSize)
```

描述：

设置Swiper组件导航箭头底板大小。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |
| float backgroundSize | 导航箭头底板大小，单位：vp。默认值：显示在导航指示器两侧24vp，显示在Swiper两侧32vp。 |

**OH_ArkUI_SwiperArrowStyle_GetBackgroundSize()**

```ets
float OH_ArkUI_SwiperArrowStyle_GetBackgroundSize(ArkUI_SwiperArrowStyle* arrowStyle)
```

描述：

获取Swiper组件导航箭头底板大小。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 导航箭头底板大小，单位：vp。 |

**OH_ArkUI_SwiperArrowStyle_SetBackgroundColor()**

```ets
void OH_ArkUI_SwiperArrowStyle_SetBackgroundColor(ArkUI_SwiperArrowStyle* arrowStyle, uint32_t backgroundColor)
```

描述：

设置Swiper组件导航箭头底板颜色。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |
| uint32_t backgroundColor | 导航箭头底板颜色，0xargb格式，形如 0xFFFF0000 表示红色。默认值：显示在导航指示器两侧为0x00000000，显示在Swiper两侧为0x19182431。 |

**OH_ArkUI_SwiperArrowStyle_GetBackgroundColor()**

```ets
uint32_t OH_ArkUI_SwiperArrowStyle_GetBackgroundColor(ArkUI_SwiperArrowStyle* arrowStyle)
```

描述：

获取Swiper组件导航箭头底板颜色。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| uint32_t | 导航箭头底板颜色，0xargb格式，形如 0xFFFF0000 表示红色。 |

**OH_ArkUI_SwiperArrowStyle_SetArrowSize()**

```ets
void OH_ArkUI_SwiperArrowStyle_SetArrowSize(ArkUI_SwiperArrowStyle* arrowStyle, float arrowSize)
```

描述：

设置Swiper组件导航箭头大小。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |
| float arrowSize | 导航箭头大小，单位：vp。 默认值：显示在导航指示器两侧18vp，显示在Swiper两侧24vp。显示导航箭头底板时，arrowSize固定为backgroundSize的3/4。 |

**OH_ArkUI_SwiperArrowStyle_GetArrowSize()**

```ets
float OH_ArkUI_SwiperArrowStyle_GetArrowSize(ArkUI_SwiperArrowStyle* arrowStyle)
```

描述：

获取Swiper组件导航箭头大小。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 导航箭头大小，单位：vp。 |

**OH_ArkUI_SwiperArrowStyle_SetArrowColor()**

```ets
void OH_ArkUI_SwiperArrowStyle_SetArrowColor(ArkUI_SwiperArrowStyle* arrowStyle, uint32_t arrowColor)
```

描述：

设置Swiper组件导航箭头颜色。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |
| uint32_t arrowColor | 导航箭头颜色，0xargb格式，形如0xFFFF0000表示红色。 默认值：'#182431'，深蓝色。 |

**OH_ArkUI_SwiperArrowStyle_GetArrowColor()**

```ets
uint32_t OH_ArkUI_SwiperArrowStyle_GetArrowColor(ArkUI_SwiperArrowStyle* arrowStyle)
```

描述：

获取Swiper组件导航箭头颜色。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| uint32_t | 导航箭头颜色，0xargb格式，形如 0xFFFF0000 表示红色。 |

**OH_ArkUI_SwiperIndicator_SetSpace()**

```ets
void OH_ArkUI_SwiperIndicator_SetSpace(ArkUI_SwiperIndicator* indicator, float space)
```

描述：

设置导航点间距。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| float space | 导航点间距。默认值：8，单位：vp。 |

**OH_ArkUI_SwiperIndicator_GetSpace()**

```ets
float OH_ArkUI_SwiperIndicator_GetSpace(ArkUI_SwiperIndicator* indicator)
```

描述：

获取导航点间距。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 导航点间距。单位：vp。 |

**OH_ArkUI_SwiperDigitIndicator_SetIgnoreSizeOfBottom()**

```ets
void OH_ArkUI_SwiperDigitIndicator_SetIgnoreSizeOfBottom(ArkUI_SwiperDigitIndicator* indicator, int32_t ignoreSize)
```

描述：

设置OH_ArkUI_SwiperDigitIndicator_SetBottomPosition是否忽略导航点大小。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 导航指示器对象指针。 |
| int32_t ignoreSize | 是否忽略导航点大小。1表示忽略导航点大小，0表示不忽略，默认值0。 |

**OH_ArkUI_SwiperDigitIndicator_GetIgnoreSizeOfBottom()**

```ets
int32_t OH_ArkUI_SwiperDigitIndicator_GetIgnoreSizeOfBottom(ArkUI_SwiperDigitIndicator* indicator)
```

描述：

获取OH_ArkUI_SwiperDigitIndicator_SetBottomPosition是否忽略导航点大小。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 导航指示器对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回1表示忽略导航点大小，返回0表示不忽略。 |

**OH_ArkUI_ListItemSwipeActionItem_Create()**

```ets
ArkUI_ListItemSwipeActionItem* OH_ArkUI_ListItemSwipeActionItem_Create()
```

描述：

创建ListItemSwipeActionItem接口设置的配置项。

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* | ListItemSwipeActionItem配置项实例。 |

**OH_ArkUI_ListItemSwipeActionItem_Dispose()**

```ets
void OH_ArkUI_ListItemSwipeActionItem_Dispose(ArkUI_ListItemSwipeActionItem* item)
```

描述：

销毁ListItemSwipeActionItem实例。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | 要销毁的ListItemSwipeActionItem实例。 |

**OH_ArkUI_ListItemSwipeActionItem_SetContent()**

```ets
void OH_ArkUI_ListItemSwipeActionItem_SetContent(ArkUI_ListItemSwipeActionItem* item, ArkUI_NodeHandle node)
```

描述：

设置ListItemSwipeActionItem的布局内容。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |
| ArkUI_NodeHandle node | 布局信息。 |

**OH_ArkUI_ListItemSwipeActionItem_SetActionAreaDistance()**

```ets
void OH_ArkUI_ListItemSwipeActionItem_SetActionAreaDistance(ArkUI_ListItemSwipeActionItem* item, float distance)
```

描述：

设置组件长距离滑动删除距离阈值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |
| float distance | 组件长距离滑动删除距离阈值。 |

**OH_ArkUI_ListItemSwipeActionItem_GetActionAreaDistance()**

```ets
float OH_ArkUI_ListItemSwipeActionItem_GetActionAreaDistance(ArkUI_ListItemSwipeActionItem* item)
```

描述：

获取组件长距离滑动删除距离阈值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 组件长距离滑动删除距离阈值。异常时返回值：0。 |

**OH_ArkUI_ListItemSwipeActionItem_SetOnEnterActionArea()**

```ets
void OH_ArkUI_ListItemSwipeActionItem_SetOnEnterActionArea(ArkUI_ListItemSwipeActionItem* item, void (*callback)())
```

描述：

设置滑动条目进入删除区域时调用的事件。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |
| callback | 回调事件。 |

**OH_ArkUI_ListItemSwipeActionItem_SetOnEnterActionAreaWithUserData()**

```ets
void OH_ArkUI_ListItemSwipeActionItem_SetOnEnterActionAreaWithUserData(ArkUI_ListItemSwipeActionItem* item,void* userData, void (*callback)(void* userData))
```

描述：

设置滑动条目进入删除区域时调用的事件。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |
| void* userData | 用户自定义数据。 |
| callback | 回调事件。 |

**OH_ArkUI_ListItemSwipeActionItem_SetOnAction()**

```ets
void OH_ArkUI_ListItemSwipeActionItem_SetOnAction(ArkUI_ListItemSwipeActionItem* item, void (*callback)())
```

描述：

设置组件进入长距删除区后删除ListItem时调用的事件。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |
| callback | 回调事件。 |

**OH_ArkUI_ListItemSwipeActionItem_SetOnActionWithUserData()**

```ets
void OH_ArkUI_ListItemSwipeActionItem_SetOnActionWithUserData(ArkUI_ListItemSwipeActionItem* item,void* userData, void (*callback)(void* userData))
```

描述：

设置组件进入长距删除区后删除ListItem时调用的事件。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |
| void* userData | 用户自定义数据。 |
| callback | 回调事件。 |

**OH_ArkUI_ListItemSwipeActionItem_SetOnExitActionArea()**

```ets
void OH_ArkUI_ListItemSwipeActionItem_SetOnExitActionArea(ArkUI_ListItemSwipeActionItem* item, void (*callback)())
```

描述：

设置滑动条目退出删除区域时调用的事件。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |
| callback | 回调事件。 |

**OH_ArkUI_ListItemSwipeActionItem_SetOnExitActionAreaWithUserData()**

```ets
void OH_ArkUI_ListItemSwipeActionItem_SetOnExitActionAreaWithUserData(ArkUI_ListItemSwipeActionItem* item,void* userData, void (*callback)(void* userData))
```

描述：

设置滑动条目退出删除区域时调用的事件。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |
| void* userData | 用户自定义数据。 |
| callback | 回调事件。 |

**OH_ArkUI_ListItemSwipeActionItem_SetOnStateChange()**

```ets
void OH_ArkUI_ListItemSwipeActionItem_SetOnStateChange(ArkUI_ListItemSwipeActionItem* item,void (*callback)(ArkUI_ListItemSwipeActionState swipeActionState))
```

描述：

设置列表项滑动状态变化时候触发的事件。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |
| callback | 回调事件。swipeActionState 变化后的状态。 |

**OH_ArkUI_ListItemSwipeActionItem_SetOnStateChangeWithUserData()**

```ets
void OH_ArkUI_ListItemSwipeActionItem_SetOnStateChangeWithUserData(ArkUI_ListItemSwipeActionItem* item,void* userData, void (*callback)(ArkUI_ListItemSwipeActionState swipeActionState, void* userData))
```

描述：

设置列表项滑动状态变化时候触发的事件。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |
| void* userData | 用户自定义数据。 |
| callback | 回调事件。swipeActionState 变化后的状态。 |

**OH_ArkUI_ListItemSwipeActionOption_Create()**

```ets
ArkUI_ListItemSwipeActionOption* OH_ArkUI_ListItemSwipeActionOption_Create()
```

描述：

创建ListItemSwipeActionOption接口设置的配置项。

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ListItemSwipeActionOption* | ListItemSwipeActionOption配置项实例。 |

**OH_ArkUI_ListItemSwipeActionOption_Dispose()**

```ets
void OH_ArkUI_ListItemSwipeActionOption_Dispose(ArkUI_ListItemSwipeActionOption* option)
```

描述：

销毁ListItemSwipeActionOption实例。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionOption* option | 要销毁的ListItemSwipeActionOption实例。 |

**OH_ArkUI_ListItemSwipeActionOption_SetStart()**

```ets
void OH_ArkUI_ListItemSwipeActionOption_SetStart(ArkUI_ListItemSwipeActionOption* option, ArkUI_ListItemSwipeActionItem* item)
```

描述：

设置ListItemSwipeActionItem的左侧（垂直布局）或上方（横向布局）布局内容。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionOption* option | ListItemSwipeActionItem实例。 |
| ArkUI_ListItemSwipeActionItem* item | 布局信息。 |

**OH_ArkUI_ListItemSwipeActionOption_SetEnd()**

```ets
void OH_ArkUI_ListItemSwipeActionOption_SetEnd(ArkUI_ListItemSwipeActionOption* option,ArkUI_ListItemSwipeActionItem* item)
```

描述：

设置ListItemSwipeActionItem的右侧（垂直布局）或下方（横向布局）布局内容。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionOption* option | ListItemSwipeActionItem实例。 |
| ArkUI_ListItemSwipeActionItem* item | 布局信息。 |

**OH_ArkUI_ListItemSwipeActionOption_SetEdgeEffect()**

```ets
void OH_ArkUI_ListItemSwipeActionOption_SetEdgeEffect(ArkUI_ListItemSwipeActionOption* option,ArkUI_ListItemSwipeEdgeEffect edgeEffect)
```

描述：

设置滑动效果。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionOption* option | ListItemSwipeActionItem实例。 |
| ArkUI_ListItemSwipeEdgeEffect edgeEffect | 滑动效果。 |

**OH_ArkUI_ListItemSwipeActionOption_GetEdgeEffect()**

```ets
int32_t OH_ArkUI_ListItemSwipeActionOption_GetEdgeEffect(ArkUI_ListItemSwipeActionOption* option)
```

描述：

获取滑动效果。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionOption* option | ListItemSwipeActionItem实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 滑动效果。默认返回值：ARKUI_LIST_ITEM_SWIPE_EDGE_EFFECT_SPRING。 |

**OH_ArkUI_ListItemSwipeActionOption_SetOnOffsetChange()**

```ets
void OH_ArkUI_ListItemSwipeActionOption_SetOnOffsetChange(ArkUI_ListItemSwipeActionOption* option,void (*callback)(float offset))
```

描述：

滑动操作偏移量更改时调用的事件。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionOption* option | ListItemSwipeActionItem实例。 |
| callback | 回调事件。offset 滑动偏移量。 |

**OH_ArkUI_ListItemSwipeActionOption_SetOnOffsetChangeWithUserData()**

```ets
void OH_ArkUI_ListItemSwipeActionOption_SetOnOffsetChangeWithUserData(ArkUI_ListItemSwipeActionOption* option,void* userData, void (*callback)(float offset, void* userData))
```

描述：

滑动操作偏移量更改时调用的事件。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionOption* option | ListItemSwipeActionItem实例。 |
| void* userData | 用户自定义数据。 |
| callback | 回调事件。offset 滑动偏移量。 |

**OH_ArkUI_ListItemSwipeAction_Expand()**

```ets
int32_t OH_ArkUI_ListItemSwipeAction_Expand(ArkUI_NodeHandle node, ArkUI_ListItemSwipeActionDirection direction)
```

描述：

展开指定ListItem的划出菜单。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | ListItem节点对象。 |
| ArkUI_ListItemSwipeActionDirection direction | ListItem划出菜单的展开方向。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_ERROR 传入的节点对象类型错误。 ARKUI_ERROR_CODE_NODE_NOT_ON_MAIN_TREE 传入的节点未挂载到组件树上。 |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

- 如果List组件NODE_LIST_CACHED_COUNT属性设置显示预加载ListItem，List显示区域外已预加载完成的ListItem支持展开，否则List显示区域外节点不支持展开。

**OH_ArkUI_ListItemSwipeAction_Collapse()**

```ets
int32_t OH_ArkUI_ListItemSwipeAction_Collapse(ArkUI_NodeHandle node)
```

描述：

收起指定ListItem的划出菜单。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | ListItem节点对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_ERROR 传入的节点对象类型错误。 ARKUI_ERROR_CODE_NODE_NOT_ON_MAIN_TREE 传入的节点未挂载到组件树上。 |

**OH_ArkUI_AccessibilityState_Create()**

```ets
ArkUI_AccessibilityState* OH_ArkUI_AccessibilityState_Create(void)
```

描述：

创建无障碍状态。

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_AccessibilityState* | 无障碍状态对象指针。如果对象返回空指针，表示创建失败，失败的可能原因是应用地址空间满。 |

**OH_ArkUI_AccessibilityState_Dispose()**

```ets
void OH_ArkUI_AccessibilityState_Dispose(ArkUI_AccessibilityState* state)
```

描述：

销毁无障碍状态指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityState* state | 无障碍状态对象指针。 |

**OH_ArkUI_AccessibilityState_SetDisabled()**

```ets
void OH_ArkUI_AccessibilityState_SetDisabled(ArkUI_AccessibilityState* state, int32_t isDisabled)
```

描述：

设置无障碍状态是否禁用。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityState* state | 无障碍状态对象指针。 |
| int32_t isDisabled | 无障碍状态是否禁用， 1表示禁用，0表示不禁用，默认为0。 |

**OH_ArkUI_AccessibilityState_IsDisabled()**

```ets
int32_t OH_ArkUI_AccessibilityState_IsDisabled(ArkUI_AccessibilityState* state)
```

描述：

获取无障碍状态是否禁用。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityState* state | 无障碍状态对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 是否禁用， 1表示禁用，0表示未禁用，默认为0; 若state为空，返回默认值。 |

**OH_ArkUI_AccessibilityState_SetSelected()**

```ets
void OH_ArkUI_AccessibilityState_SetSelected(ArkUI_AccessibilityState* state, int32_t isSelected)
```

描述：

设置无障碍状态是否选中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityState* state | 无障碍状态对象指针。 |
| int32_t isSelected | 是否被选中， 1表示选中，0表示未选中，默认为0。 |

**OH_ArkUI_AccessibilityState_IsSelected()**

```ets
int32_t OH_ArkUI_AccessibilityState_IsSelected(ArkUI_AccessibilityState* state)
```

描述：

获取无障碍状态是否选中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityState* state | 无障碍状态对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 是否被选中， 1表示选中，0表示未选中，默认为0; 若state为空，返回默认值。 |

**OH_ArkUI_AccessibilityState_SetCheckedState()**

```ets
void OH_ArkUI_AccessibilityState_SetCheckedState(ArkUI_AccessibilityState* state, int32_t checkedState)
```

描述：

设置无障碍状态复选框状态。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityState* state | 无障碍状态对象指针。 |
| int32_t checkedState | 复选框状态，参数类型ArkUI_AccessibilityCheckedState, 默认值：ARKUI_ACCESSIBILITY_UNCHECKED。 |

**OH_ArkUI_AccessibilityState_GetCheckedState()**

```ets
int32_t OH_ArkUI_AccessibilityState_GetCheckedState(ArkUI_AccessibilityState* state)
```

描述：

获取无障碍状态复选框状态。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityState* state | 无障碍状态对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 复选框状态，参数类型ArkUI_AccessibilityCheckedState, 默认值：ARKUI_ACCESSIBILITY_UNCHECKED; 若函数参数异常，返回默认值。 |

**OH_ArkUI_AccessibilityValue_Create()**

```ets
ArkUI_AccessibilityValue* OH_ArkUI_AccessibilityValue_Create(void)
```

描述：

创建无障碍信息。

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_AccessibilityValue* | 无障碍信息对象指针。 |

**OH_ArkUI_AccessibilityValue_Dispose()**

```ets
void OH_ArkUI_AccessibilityValue_Dispose(ArkUI_AccessibilityValue* value)
```

描述：

销毁无障碍信息指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 无障碍信息对象指针。 |

**OH_ArkUI_AccessibilityValue_SetMin()**

```ets
void OH_ArkUI_AccessibilityValue_SetMin(ArkUI_AccessibilityValue* value, int32_t min)
```

描述：

设置无障碍最小值信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 无障碍信息对象指针。 |
| int32_t min | 基于范围组件的最小值, 默认为-1。 |

**OH_ArkUI_AccessibilityValue_GetMin()**

```ets
int32_t OH_ArkUI_AccessibilityValue_GetMin(ArkUI_AccessibilityValue* value)
```

描述：

获取无障碍最小值信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 无障碍信息对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 基于范围组件的最小值, 默认为-1; 若函数参数异常，返回-1。 |

**OH_ArkUI_AccessibilityValue_SetMax()**

```ets
void OH_ArkUI_AccessibilityValue_SetMax(ArkUI_AccessibilityValue* value, int32_t max)
```

描述：

设置无障碍最大值信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 无障碍信息对象指针。 |
| int32_t max | 基于范围组件的最大值, 默认为-1。 |

**OH_ArkUI_AccessibilityValue_GetMax()**

```ets
int32_t OH_ArkUI_AccessibilityValue_GetMax(ArkUI_AccessibilityValue* value)
```

描述：

获取无障碍最大值信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 无障碍信息对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 基于范围组件的最大值, 默认为-1; 若函数参数异常，返回-1。 |

**OH_ArkUI_AccessibilityValue_SetCurrent()**

```ets
void OH_ArkUI_AccessibilityValue_SetCurrent(ArkUI_AccessibilityValue* value, int32_t current)
```

描述：

设置无障碍当前值信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 无障碍信息对象指针。 |
| int32_t current | 基于范围组件的当前值, 默认为-1。 |

**OH_ArkUI_AccessibilityValue_GetCurrent()**

```ets
int32_t OH_ArkUI_AccessibilityValue_GetCurrent(ArkUI_AccessibilityValue* value)
```

描述：

获取无障碍当前值信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 无障碍信息对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 基于范围组件的当前值, 默认为-1; 若函数参数异常，返回-1。 |

**OH_ArkUI_AccessibilityValue_SetRangeMin()**

```ets
void OH_ArkUI_AccessibilityValue_SetRangeMin(ArkUI_AccessibilityValue* value, int32_t rangeMin)
```

描述：

设置范围组件的无障碍最小值信息。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 需要设置最小值的范围组件无障碍信息对象指针。 |
| int32_t rangeMin | 基于范围组件的最小值, 默认为-1。 |

**OH_ArkUI_AccessibilityValue_GetRangeMin()**

```ets
int32_t OH_ArkUI_AccessibilityValue_GetRangeMin(ArkUI_AccessibilityValue* value)
```

描述：

获取范围组件的无障碍最小值信息。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 需要获取最小值的范围组件无障碍信息对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 基于范围组件的最小值, 默认为-1; 若函数参数异常，返回-1。 |

**OH_ArkUI_AccessibilityValue_SetRangeMax()**

```ets
void OH_ArkUI_AccessibilityValue_SetRangeMax(ArkUI_AccessibilityValue* value, int32_t rangeMax)
```

描述：

设置范围组件的无障碍最大值信息。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 需要设置最大值的范围组件无障碍信息对象指针。 |
| int32_t rangeMax | 基于范围组件的最大值, 默认为-1。 |

**OH_ArkUI_AccessibilityValue_GetRangeMax()**

```ets
int32_t OH_ArkUI_AccessibilityValue_GetRangeMax(ArkUI_AccessibilityValue* value)
```

描述：

获取范围组件的无障碍最大值信息。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 需要获取最小值的范围组件无障碍信息对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 基于范围组件的最大值, 默认为-1; 若函数参数异常，返回-1。 |

**OH_ArkUI_AccessibilityValue_SetRangeCurrent()**

```ets
void OH_ArkUI_AccessibilityValue_SetRangeCurrent(ArkUI_AccessibilityValue* value, int32_t rangeCurrent)
```

描述：

用于设置范围组件的无障碍当前值信息。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 需要设置当前值的范围组件无障碍信息对象指针。 |
| int32_t rangeCurrent | 基于范围组件的当前值, 默认为-1。 |

**OH_ArkUI_AccessibilityValue_GetRangeCurrent()**

```ets
int32_t OH_ArkUI_AccessibilityValue_GetRangeCurrent(ArkUI_AccessibilityValue* value)
```

描述：

用于获取范围组件的无障碍当前值信息。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 需要获取当前值的范围组件无障碍信息对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 基于范围组件的当前值, 默认为-1; 若函数参数异常，返回-1。 |

**OH_ArkUI_AccessibilityValue_SetText()**

```ets
void OH_ArkUI_AccessibilityValue_SetText(ArkUI_AccessibilityValue* value, const char* text)
```

描述：

设置无障碍文本描述信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 无障碍信息对象指针。 |
| const char* text | 组件的文本描述信息, 默认为空字符串。 |

**OH_ArkUI_AccessibilityValue_GetText()**

```ets
const char* OH_ArkUI_AccessibilityValue_GetText(ArkUI_AccessibilityValue* value)
```

描述：

获取无障碍文本描述信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 无障碍信息对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char* | 组件的文本描述信息, 默认为空字符串; 若函数参数异常，返回空指针。 |

**OH_ArkUI_ImageAnimatorFrameInfo_CreateFromString()**

```ets
ArkUI_ImageAnimatorFrameInfo* OH_ArkUI_ImageAnimatorFrameInfo_CreateFromString(char* src)
```

描述：

使用图片路径创建帧图片信息，图片格式为svg，png和jpg。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| char* src | 图片路径。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ImageAnimatorFrameInfo* | 帧图片对象指针。 |

**OH_ArkUI_ImageAnimatorFrameInfo_CreateFromDrawableDescriptor()**

```ets
ArkUI_ImageAnimatorFrameInfo* OH_ArkUI_ImageAnimatorFrameInfo_CreateFromDrawableDescriptor(ArkUI_DrawableDescriptor* drawable)
```

描述：

使用[DrawableDescriptor](ArkUI_DrawableDescriptor.md)对象创建帧图片信息，图片格式为Resource和PixelMap。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawableDescriptor* drawable | 使用Resource或PixelMap创建的ArkUI_DrawableDescriptor对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ImageAnimatorFrameInfo* | 帧图片对象指针。 |

**OH_ArkUI_ImageAnimatorFrameInfo_Dispose()**

```ets
void OH_ArkUI_ImageAnimatorFrameInfo_Dispose(ArkUI_ImageAnimatorFrameInfo* imageInfo)
```

描述：

销毁帧图片对象指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ImageAnimatorFrameInfo* imageInfo | 帧图片对象指针。 |

**OH_ArkUI_ImageAnimatorFrameInfo_SetWidth()**

```ets
void OH_ArkUI_ImageAnimatorFrameInfo_SetWidth(ArkUI_ImageAnimatorFrameInfo* imageInfo, int32_t width)
```

描述：

设置图片宽度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ImageAnimatorFrameInfo* imageInfo | 帧图片对象指针。 |
| int32_t width | 图片宽度，单位为PX。 |

**OH_ArkUI_ImageAnimatorFrameInfo_GetWidth()**

```ets
int32_t OH_ArkUI_ImageAnimatorFrameInfo_GetWidth(ArkUI_ImageAnimatorFrameInfo* imageInfo)
```

描述：

获取图片宽度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ImageAnimatorFrameInfo* imageInfo | 帧图片对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 图片宽度，单位为PX，imageInfo为空指针时返回0。 |

**OH_ArkUI_ImageAnimatorFrameInfo_SetHeight()**

```ets
void OH_ArkUI_ImageAnimatorFrameInfo_SetHeight(ArkUI_ImageAnimatorFrameInfo* imageInfo, int32_t height)
```

描述：

设置图片高度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ImageAnimatorFrameInfo* imageInfo | 帧图片对象指针。 |
| int32_t height | 图片高度，单位为PX。 |

**OH_ArkUI_ImageAnimatorFrameInfo_GetHeight()**

```ets
int32_t OH_ArkUI_ImageAnimatorFrameInfo_GetHeight(ArkUI_ImageAnimatorFrameInfo* imageInfo)
```

描述：

获取图片高度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ImageAnimatorFrameInfo* imageInfo | 帧图片对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 图片高度，单位为PX，imageInfo为空指针时返回0。 |

**OH_ArkUI_ImageAnimatorFrameInfo_SetTop()**

```ets
void OH_ArkUI_ImageAnimatorFrameInfo_SetTop(ArkUI_ImageAnimatorFrameInfo* imageInfo, int32_t top)
```

描述：

设置图片相对于组件左上角的纵向坐标。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ImageAnimatorFrameInfo* imageInfo | 帧图片对象指针。 |
| int32_t top | 图片相对于组件左上角的纵向坐标，单位为PX。 |

**OH_ArkUI_ImageAnimatorFrameInfo_GetTop()**

```ets
int32_t OH_ArkUI_ImageAnimatorFrameInfo_GetTop(ArkUI_ImageAnimatorFrameInfo* imageInfo)
```

描述：

获取图片相对于组件左上角的纵向坐标。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ImageAnimatorFrameInfo* imageInfo | 帧图片对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 图片相对于组件左上角的纵向坐标，单位为PX，imageInfo为空指针时返回0。 |

**OH_ArkUI_ImageAnimatorFrameInfo_SetLeft()**

```ets
void OH_ArkUI_ImageAnimatorFrameInfo_SetLeft(ArkUI_ImageAnimatorFrameInfo* imageInfo, int32_t left)
```

描述：

设置图片相对于组件左上角的横向坐标。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ImageAnimatorFrameInfo* imageInfo | 帧图片对象指针。 |
| int32_t left | 图片相对于组件左上角的横向坐标，单位为PX。 |

**OH_ArkUI_ImageAnimatorFrameInfo_GetLeft()**

```ets
int32_t OH_ArkUI_ImageAnimatorFrameInfo_GetLeft(ArkUI_ImageAnimatorFrameInfo* imageInfo)
```

描述：

获取图片相对于组件左上角的横向坐标。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ImageAnimatorFrameInfo* imageInfo | 帧图片对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 图片相对于组件左上角的横向坐标，单位为PX，imageInfo为空指针时返回0。 |

**OH_ArkUI_ImageAnimatorFrameInfo_SetDuration()**

```ets
void OH_ArkUI_ImageAnimatorFrameInfo_SetDuration(ArkUI_ImageAnimatorFrameInfo* imageInfo, int32_t duration)
```

描述：

设置图片的播放时长。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ImageAnimatorFrameInfo* imageInfo | 帧图片对象指针。 |
| int32_t duration | 图片的播放时长，单位为毫秒。 |

**OH_ArkUI_ImageAnimatorFrameInfo_GetDuration()**

```ets
int32_t OH_ArkUI_ImageAnimatorFrameInfo_GetDuration(ArkUI_ImageAnimatorFrameInfo* imageInfo)
```

描述：

获取图片的播放时长。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ImageAnimatorFrameInfo* imageInfo | 帧图片对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 图片的播放时长，单位为毫秒，imageInfo为空指针时返回0。 |

**OH_ArkUI_ListChildrenMainSizeOption_Create()**

```ets
ArkUI_ListChildrenMainSize* OH_ArkUI_ListChildrenMainSizeOption_Create()
```

描述：

创建ListChildrenMainSize接口设置的配置项。

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ListChildrenMainSize* | ListChildrenMainSize配置项实例。 |

**OH_ArkUI_ListChildrenMainSizeOption_Dispose()**

```ets
void OH_ArkUI_ListChildrenMainSizeOption_Dispose(ArkUI_ListChildrenMainSize* option)
```

描述：

销毁ListChildrenMainSize实例。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListChildrenMainSize* option | 要销毁的ListChildrenMainSize实例。 |

**OH_ArkUI_ListChildrenMainSizeOption_SetDefaultMainSize()**

```ets
int32_t OH_ArkUI_ListChildrenMainSizeOption_SetDefaultMainSize(ArkUI_ListChildrenMainSize* option, float defaultMainSize)
```

描述：

设置List组件的ChildrenMainSizeOption默认大小。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListChildrenMainSize* option | ListChildrenMainSize实例。 |
| float defaultMainSize | List下的ListItem的默认大小，单位为vp。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_ListChildrenMainSizeOption_GetDefaultMainSize()**

```ets
float OH_ArkUI_ListChildrenMainSizeOption_GetDefaultMainSize(ArkUI_ListChildrenMainSize* option)
```

描述：

获取List组件的ChildrenMainSizeOption默认大小。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListChildrenMainSize* option | ListChildrenMainSize实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | List下的ListItem的默认大小，默认为0，单位为vp，option为空指针时返回-1。 |

**OH_ArkUI_ListChildrenMainSizeOption_Resize()**

```ets
void OH_ArkUI_ListChildrenMainSizeOption_Resize(ArkUI_ListChildrenMainSize* option, int32_t totalSize)
```

描述：

重置List组件的ChildrenMainSizeOption的数组大小。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListChildrenMainSize* option | ListChildrenMainSize实例。 |
| int32_t totalSize | 数组大小。 |

**OH_ArkUI_ListChildrenMainSizeOption_Splice()**

```ets
int32_t OH_ArkUI_ListChildrenMainSizeOption_Splice(ArkUI_ListChildrenMainSize* option, int32_t index, int32_t deleteCount, int32_t addCount)
```

描述：

对List组件的ChildrenMainSizeOption数组操作大小调整。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListChildrenMainSize* option | ListChildrenMainSize实例。 |
| int32_t index | 要修改MainSize的数组起始位置。 |
| int32_t deleteCount | 要删除的MainSize数组从index开始的数量。 |
| int32_t addCount | 要添加的MainSize数组从index开始的数量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_ListChildrenMainSizeOption_UpdateSize()**

```ets
int32_t OH_ArkUI_ListChildrenMainSizeOption_UpdateSize(ArkUI_ListChildrenMainSize* option, int32_t index, float mainSize)
```

描述：

更新List组件的ChildrenMainSizeOption数组的值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListChildrenMainSize* option | ListChildrenMainSize实例。 |
| int32_t index | 要修改MainSize的数组起始位置。 |
| float mainSize | 实际修改的值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_ListChildrenMainSizeOption_GetMainSize()**

```ets
float OH_ArkUI_ListChildrenMainSizeOption_GetMainSize(ArkUI_ListChildrenMainSize* option, int32_t index)
```

描述：

获取List组件的ChildrenMainSizeOption数组的值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListChildrenMainSize* option | ListChildrenMainSize实例。 |
| int32_t index | 要获取的值的下标位置。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 数组具体位置的值。若函数参数异常，返回-1。 |

**OH_ArkUI_CustomSpanMeasureInfo_Create()**

```ets
ArkUI_CustomSpanMeasureInfo* OH_ArkUI_CustomSpanMeasureInfo_Create(void)
```

描述：

创建自定义段落组件测量信息。

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_CustomSpanMeasureInfo* | CustomSpanMeasureInfo实例。 如果返回空指针，可能是因为内存不足。 |

**OH_ArkUI_CustomSpanMeasureInfo_Dispose()**

```ets
void OH_ArkUI_CustomSpanMeasureInfo_Dispose(ArkUI_CustomSpanMeasureInfo* info)
```

描述：

销毁自定义段落组件测量信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomSpanMeasureInfo* info | 自定义段落组件测量信息指针。 |

**OH_ArkUI_CustomSpanMeasureInfo_GetFontSize()**

```ets
float OH_ArkUI_CustomSpanMeasureInfo_GetFontSize(ArkUI_CustomSpanMeasureInfo* info)
```

描述：

获取自定义段落组件的父节点Text的字体大小。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomSpanMeasureInfo* info | 自定义段落组件测量信息指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 父节点Text的字体大小。若函数参数异常，返回0.0f。 异常返回原因：传入参数验证失败，参数不能为空。 |

**OH_ArkUI_CustomSpanMetrics_Create()**

```ets
ArkUI_CustomSpanMetrics* OH_ArkUI_CustomSpanMetrics_Create(void)
```

描述：

创建自定义段落组件度量信息。

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_CustomSpanMetrics* | CustomSpanMetrics实例。 如果返回空指针，可能是因为内存不足。 |

**OH_ArkUI_CustomSpanMetrics_Dispose()**

```ets
void OH_ArkUI_CustomSpanMetrics_Dispose(ArkUI_CustomSpanMetrics* metrics)
```

描述：

销毁自定义段落组件度量信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomSpanMetrics* metrics | CustomSpanMetrics实例。 |

**OH_ArkUI_CustomSpanMetrics_SetWidth()**

```ets
int32_t OH_ArkUI_CustomSpanMetrics_SetWidth(ArkUI_CustomSpanMetrics* metrics, float width)
```

描述：

设置自定义段落组件的宽度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomSpanMetrics* metrics | CustomSpanMetrics实例。 |
| float width | 宽度大小，单位为vp。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 异常原因：传入参数验证失败，参数不能为空。 |

**OH_ArkUI_CustomSpanMetrics_SetHeight()**

```ets
int32_t OH_ArkUI_CustomSpanMetrics_SetHeight(ArkUI_CustomSpanMetrics* metrics, float height)
```

描述：

设置自定义段落组件的高度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomSpanMetrics* metrics | CustomSpanMetrics实例。 |
| float height | 高度大小，单位为vp。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 异常原因：传入参数验证失败，参数不能为空。 |

**OH_ArkUI_CustomSpanDrawInfo_Create()**

```ets
ArkUI_CustomSpanDrawInfo* OH_ArkUI_CustomSpanDrawInfo_Create(void)
```

描述：

创建自定义段落组件绘制信息。

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_CustomSpanDrawInfo* | CustomSpanDrawInfo实例。 如果返回空指针，可能是因为内存不足。 |

**OH_ArkUI_CustomSpanDrawInfo_Dispose()**

```ets
void OH_ArkUI_CustomSpanDrawInfo_Dispose(ArkUI_CustomSpanDrawInfo* info)
```

描述：

销毁自定义段落组件绘制信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomSpanDrawInfo* info | 自定义段落组件绘制信息指针。 |

**OH_ArkUI_CustomSpanDrawInfo_GetXOffset()**

```ets
float OH_ArkUI_CustomSpanDrawInfo_GetXOffset(ArkUI_CustomSpanDrawInfo* info)
```

描述：

获取自定义段落组件相对于挂载组件的x轴偏移值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomSpanDrawInfo* info | 自定义段落组件绘制信息指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | x轴偏移值。若函数参数异常，返回0.0f。 异常返回原因：传入参数验证失败，参数不能为空。 |

**OH_ArkUI_CustomSpanDrawInfo_GetLineTop()**

```ets
float OH_ArkUI_CustomSpanDrawInfo_GetLineTop(ArkUI_CustomSpanDrawInfo* info)
```

描述：

获取自定义段落组件相对于挂载组件的上边距。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomSpanDrawInfo* info | 自定义段落组件绘制信息指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 上边距值。若函数参数异常，返回0.0f。 异常返回原因：传入参数验证失败，参数不能为空。 |

**OH_ArkUI_CustomSpanDrawInfo_GetLineBottom()**

```ets
float OH_ArkUI_CustomSpanDrawInfo_GetLineBottom(ArkUI_CustomSpanDrawInfo* info)
```

描述：

获取自定义段落组件相对于挂载组件的下边距。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomSpanDrawInfo* info | 自定义段落组件绘制信息指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 下边距值。若函数参数异常，返回0.0f。 异常返回原因：传入参数验证失败，参数不能为空。 |

**OH_ArkUI_CustomSpanDrawInfo_GetBaseline()**

```ets
float OH_ArkUI_CustomSpanDrawInfo_GetBaseline(ArkUI_CustomSpanDrawInfo* info)
```

描述：

获取自定义段落组件相对于挂载组件的基线偏移量。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomSpanDrawInfo* info | 自定义段落组件绘制信息指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 基线偏移量值。若函数参数异常，返回0.0f。 异常返回原因：传入参数验证失败，参数不能为空。 |

**OH_ArkUI_CustomProperty_Destroy()**

```ets
void OH_ArkUI_CustomProperty_Destroy(ArkUI_CustomProperty* handle)
```

描述：

销毁CustomProperty实例。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomProperty* handle | 要销毁的CustomProperty实例。 |

**OH_ArkUI_CustomProperty_GetStringValue()**

```ets
const char* OH_ArkUI_CustomProperty_GetStringValue(ArkUI_CustomProperty* handle)
```

描述：

获取自定义属性value信息。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomProperty* handle | 自定义属性对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char* | 自定义属性value信息。 |

**OH_ArkUI_HostWindowInfo_GetName()**

```ets
const char* OH_ArkUI_HostWindowInfo_GetName(ArkUI_HostWindowInfo* info)
```

描述：

获取HostWindowInfo对象中的窗口名称。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_HostWindowInfo* info | HostWindowInfo对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char* | HostWindowInfo对象中的窗口名称。 |

**OH_ArkUI_HostWindowInfo_Destroy()**

```ets
void OH_ArkUI_HostWindowInfo_Destroy(ArkUI_HostWindowInfo* info)
```

描述：

销毁HostWindowInfo对象。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_HostWindowInfo* info | 要销毁的HostWindowInfo对象。 |

**OH_ArkUI_ActiveChildrenInfo_Destroy()**

```ets
void OH_ArkUI_ActiveChildrenInfo_Destroy(ArkUI_ActiveChildrenInfo* handle)
```

描述：

销毁ActiveChildrenInfo实例。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ActiveChildrenInfo* handle | 要销毁的ActiveChildrenInfo实例。 |

**OH_ArkUI_ActiveChildrenInfo_GetNodeByIndex()**

```ets
ArkUI_NodeHandle OH_ArkUI_ActiveChildrenInfo_GetNodeByIndex(ArkUI_ActiveChildrenInfo* handle, int32_t index)
```

描述：

获取ActiveChildrenInfo结构体的下标为index的子节点。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ActiveChildrenInfo* handle | 要获取信息的ActiveChildrenInfo实例。 |
| int32_t index | 子节点的下标。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_NodeHandle | 下标对应的子节点指针，异常时返回nullptr。 |

**OH_ArkUI_ActiveChildrenInfo_GetCount()**

```ets
int32_t OH_ArkUI_ActiveChildrenInfo_GetCount(ArkUI_ActiveChildrenInfo* handle)
```

描述：

获取ActiveChildrenInfo结构体内的节点数量。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ActiveChildrenInfo* handle | 要获取信息的ActiveChildrenInfo实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 子节点数量，默认值0. |

**OH_ArkUI_ProgressLinearStyleOption_Create()**

```ets
ArkUI_ProgressLinearStyleOption* OH_ArkUI_ProgressLinearStyleOption_Create(void)
```

描述：

创建线性进度条样式信息。

起始版本： 15

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ProgressLinearStyleOption* | ProgressLinearStyleOption实例。 如果返回空指针，可能是因为内存不足。 |

**OH_ArkUI_ProgressLinearStyleOption_Destroy()**

```ets
void OH_ArkUI_ProgressLinearStyleOption_Destroy(ArkUI_ProgressLinearStyleOption* option)
```

描述：

销毁线性进度条样式信息。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ProgressLinearStyleOption* option | 线性进度条样式信息。 |

**OH_ArkUI_ProgressLinearStyleOption_SetSmoothEffectEnabled()**

```ets
void OH_ArkUI_ProgressLinearStyleOption_SetSmoothEffectEnabled(ArkUI_ProgressLinearStyleOption* option, bool enabled)
```

描述：

设置进度平滑动效的开关。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ProgressLinearStyleOption* option | 线性进度条样式信息。 |
| bool enabled | 进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值。默认值：true。 |

**OH_ArkUI_ProgressLinearStyleOption_SetScanEffectEnabled()**

```ets
void OH_ArkUI_ProgressLinearStyleOption_SetScanEffectEnabled(ArkUI_ProgressLinearStyleOption* option, bool enabled)
```

描述：

设置扫光效果的开关。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ProgressLinearStyleOption* option | 线性进度条样式信息。 |
| bool enabled | 扫光效果的开关。默认值：false。 |

**OH_ArkUI_ProgressLinearStyleOption_SetStrokeWidth()**

```ets
void OH_ArkUI_ProgressLinearStyleOption_SetStrokeWidth(ArkUI_ProgressLinearStyleOption* option, float strokeWidth)
```

描述：

设置进度条宽度。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ProgressLinearStyleOption* option | 线性进度条样式信息。 |
| float strokeWidth | 进度条宽度值（不支持百分比设置），单位为vp，默认值：4.0vp。 |

**OH_ArkUI_ProgressLinearStyleOption_SetStrokeRadius()**

```ets
void OH_ArkUI_ProgressLinearStyleOption_SetStrokeRadius(ArkUI_ProgressLinearStyleOption* option, float strokeRadius)
```

描述：

设置进度条圆角半径。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ProgressLinearStyleOption* option | 线性进度条样式信息。 |
| float strokeRadius | 进度条圆角半径值，单位为vp，取值范围[0, strokeWidth/2]。默认值：strokeWidth/2。 |

**OH_ArkUI_ProgressLinearStyleOption_GetSmoothEffectEnabled()**

```ets
bool OH_ArkUI_ProgressLinearStyleOption_GetSmoothEffectEnabled(ArkUI_ProgressLinearStyleOption* option)
```

描述：

获取进度平滑动效的开关信息。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ProgressLinearStyleOption* option | 线性进度条样式信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 是否开启平滑动效。 |

**OH_ArkUI_ProgressLinearStyleOption_GetScanEffectEnabled()**

```ets
bool OH_ArkUI_ProgressLinearStyleOption_GetScanEffectEnabled(ArkUI_ProgressLinearStyleOption* option)
```

描述：

获取扫光效果的开关信息。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ProgressLinearStyleOption* option | 线性进度条样式信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 是否开启扫光效果。 |

**OH_ArkUI_ProgressLinearStyleOption_GetStrokeWidth()**

```ets
float OH_ArkUI_ProgressLinearStyleOption_GetStrokeWidth(ArkUI_ProgressLinearStyleOption* option)
```

描述：

获取进度条宽度。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ProgressLinearStyleOption* option | 线性进度条样式信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 进度条宽度值，单位为vp。 |

**OH_ArkUI_ProgressLinearStyleOption_GetStrokeRadius()**

```ets
float OH_ArkUI_ProgressLinearStyleOption_GetStrokeRadius(ArkUI_ProgressLinearStyleOption* option)
```

描述：

获取进度条圆角半径值。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ProgressLinearStyleOption* option | 线性进度条样式信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 进度条圆角半径值，单位为vp。 |

**OH_ArkUI_CreateSnapshotOptions()**

```ets
ArkUI_SnapshotOptions* OH_ArkUI_CreateSnapshotOptions()
```

描述：

创建一个截图选项，当返回值不再使用时必须通过[OH_ArkUI_DestroySnapshotOptions()](#ZH-CN_TOPIC_0000002553200995__oh_arkui_destroysnapshotoptions)释放。

起始版本： 15

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_SnapshotOptions* | 返回指向创建的截图选项对象的指针。如果对象返回空指针，则表示创建失败，失败的原因可能是地址空间已满。 |

**OH_ArkUI_DestroySnapshotOptions()**

```ets
void OH_ArkUI_DestroySnapshotOptions(ArkUI_SnapshotOptions* snapshotOptions)
```

描述：

销毁截图选项指针。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SnapshotOptions* snapshotOptions | 截图选项。 |

**OH_ArkUI_SnapshotOptions_SetScale()**

```ets
int32_t OH_ArkUI_SnapshotOptions_SetScale(ArkUI_SnapshotOptions* snapshotOptions, float scale)
```

描述：

配置截图选项中的缩放属性。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SnapshotOptions* snapshotOptions | 截图选项。 |
| float scale | 缩放值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 异常原因：传入参数验证失败，参数不能为空。 |

**OH_ArkUI_SnapshotOptions_SetColorMode()**

```ets
int32_t OH_ArkUI_SnapshotOptions_SetColorMode(ArkUI_SnapshotOptions* snapshotOptions, int32_t colorSpace, bool isAuto)
```

描述：

设置截图选项中的色彩空间。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SnapshotOptions* snapshotOptions | 截图选项指针。 |
| int32_t colorSpace | 指定截图使用的色彩空间。 如果知道需要截图的组件使用的色彩空间，可以通过colorSpace参数指定，并将isAuto设置为false，以达到预期的截图效果。 支持的取值为：3（RGB色域为Display P3类型）、4（RGB色域为SRGB类型）、27（RGB色域为DISPLAY BT2020类型）。 默认值：4 仅当isAuto设置为false，该参数设置生效。 |
| bool isAuto | 是否由系统自动决定所使用的色彩空间。 true表示系统自动决定所使用的色彩空间。在不确定组件使用的色彩空间时，建议将isAuto设置为true，让系统根据实际情况自动决定使用的色彩空间。 false表示使用通过colorSpace字段设置的色彩空间类型进行截图。 默认值：false |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_SnapshotOptions_SetDynamicRangeMode()**

```ets
int32_t OH_ArkUI_SnapshotOptions_SetDynamicRangeMode(ArkUI_SnapshotOptions* snapshotOptions, int32_t dynamicRangeMode, bool isAuto)
```

描述：

设置截图选项中的动态范围模式。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SnapshotOptions* snapshotOptions | 截图选项指针。 |
| int32_t dynamicRangeMode | 指定截图使用的动态范围模式。 如果知道截图对象使用的动态范围模式，可通过dynamicRangeMode参数指定动态范围模式，并将isAuto设置为false，以达到预期的截图效果。 支持的取值为：ArkUI_DynamicRangeMode枚举值。 默认值：ARKUI_DYNAMIC_RANGE_MODE_STANDARD 仅当isAuto设置为false，该参数设置生效。 |
| bool isAuto | 是否由系统自动决定所使用的动态范围模式。 true表示系统自动决定所使用的动态范围模式。在不确定组件使用的动态范围模式时，建议将isAuto设置为true，让系统根据实际情况自动决定使用的动态范围模式。 false表示使用通过dynamicRangeMode字段设置的动态范围模式进行截图。 默认值：false |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_CrossLanguageOption_Create()**

```ets
ArkUI_CrossLanguageOption* OH_ArkUI_CrossLanguageOption_Create(void)
```

描述：

创建跨语言配置项实例。

起始版本： 15

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_CrossLanguageOption* | 返回跨语言实例。如果对象返回空指针，则表示创建失败，失败的原因可能是地址空间已满。 |

**OH_ArkUI_CrossLanguageOption_Destroy()**

```ets
void OH_ArkUI_CrossLanguageOption_Destroy(ArkUI_CrossLanguageOption* option)
```

描述：

销毁跨语言配置项实例。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CrossLanguageOption* option | 要销毁的跨语言配置项实例。 |

**OH_ArkUI_CrossLanguageOption_SetAttributeSettingStatus()**

```ets
void OH_ArkUI_CrossLanguageOption_SetAttributeSettingStatus(ArkUI_CrossLanguageOption* option, bool enabled)
```

描述：

设置配置项中是否允许跨语言修改属性。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CrossLanguageOption* option | 跨语言配置项实例。 |
| bool enabled | 是否允许跨语言修改属性。默认值：false。 |

**OH_ArkUI_CrossLanguageOption_GetAttributeSettingStatus()**

```ets
bool OH_ArkUI_CrossLanguageOption_GetAttributeSettingStatus(ArkUI_CrossLanguageOption* option)
```

描述：

获取配置项中是否允许跨语言修改属性。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CrossLanguageOption* option | 跨语言配置项实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 是否允许跨语言修改属性。 |

**OH_ArkUI_VisibleAreaEventOptions_Create()**

```ets
ArkUI_VisibleAreaEventOptions* OH_ArkUI_VisibleAreaEventOptions_Create()
```

描述：

创建可见区域变化监听的参数。

起始版本： 17

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_VisibleAreaEventOptions* | 可见区域变化监听的参数。 |

**OH_ArkUI_VisibleAreaEventOptions_Dispose()**

```ets
void OH_ArkUI_VisibleAreaEventOptions_Dispose(ArkUI_VisibleAreaEventOptions* option)
```

描述：

销毁可见区域变化监听的参数。

起始版本： 17

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_VisibleAreaEventOptions* option | 需要销毁的实例。 |

**OH_ArkUI_VisibleAreaEventOptions_SetRatios()**

```ets
int32_t OH_ArkUI_VisibleAreaEventOptions_SetRatios(ArkUI_VisibleAreaEventOptions* option, float* value, int32_t size)
```

描述：

设置阈值数组。

起始版本： 17

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_VisibleAreaEventOptions* option | 可见区域变化监听的参数实例。 |
| float* value | 阈值数组。其中每个元素代表组件可见面积（即组件在屏幕显示区的面积，只计算父组件内的面积，超出父组件部分不会计算）与组件自身面积的比值。每个阈值的取值范围为[0.0, 1.0]，如果开发者设置的阈值超出该范围，则会实际取值0.0或1.0。 |
| int32_t size | 阈值数组大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 异常原因：传入参数验证失败，参数不能为空。 |

**OH_ArkUI_VisibleAreaEventOptions_SetExpectedUpdateInterval()**

```ets
int32_t OH_ArkUI_VisibleAreaEventOptions_SetExpectedUpdateInterval(ArkUI_VisibleAreaEventOptions *option, int32_t value)
```

描述：

设置预期更新间隔，单位为ms。定义了开发者期望的更新间隔。

起始版本： 17

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_VisibleAreaEventOptions *option | 可见区域变化监听的参数实例。 |
| int32_t value | 预期更新间隔，单位为ms。定义了开发者期望的更新间隔。默认值：1000。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 异常原因：传入参数验证失败，参数不能为空。 |

**OH_ArkUI_VisibleAreaEventOptions_SetMeasureFromViewport()**

```ets
int32_t OH_ArkUI_VisibleAreaEventOptions_SetMeasureFromViewport(ArkUI_VisibleAreaEventOptions* option, bool measureFromViewport)
```

描述：

设置可见区域计算模式。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_VisibleAreaEventOptions* option | 可见区域变化监听的参数实例。 |
| bool measureFromViewport | 设置可见区域计算模式。 当measureFromViewport设置为true时，系统在计算该组件的可见区域时，会考虑父组件的NODE_CLIP属性设置。如果父组件的NODE_CLIP为false，则认为其内的子组件可以超出其区域进行显示，因此超出父组件的区域也将被视为可见区域纳入计算；如果父组件的NODE_CLIP设置为true，则组件超出父组件的区域会被裁剪，无法显示，因此会被视为不可见区域进行计算。而当measureFromViewport设置为false时，则不考虑NODE_CLIP的影响，直接将组件超出父组件的部分视为不可见区域。 默认值：false |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 异常原因：传入参数验证失败，参数不能为空。 |

**OH_ArkUI_VisibleAreaEventOptions_GetRatios()**

```ets
int32_t OH_ArkUI_VisibleAreaEventOptions_GetRatios(ArkUI_VisibleAreaEventOptions* option, float* value, int32_t* size)
```

描述：

获取阈值数组。

起始版本： 17

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_VisibleAreaEventOptions* option | 可见区域变化监听的参数实例。 |
| float* value | 阈值数组。 |
| int32_t* size | 阈值数组大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR 数组大小不够。 异常原因：传入参数验证失败，参数不能为空。 |

**OH_ArkUI_VisibleAreaEventOptions_GetExpectedUpdateInterval()**

```ets
int32_t OH_ArkUI_VisibleAreaEventOptions_GetExpectedUpdateInterval(ArkUI_VisibleAreaEventOptions* option)
```

描述：

获取预期更新间隔。

起始版本： 17

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_VisibleAreaEventOptions* option | 可见区域变化监听的参数实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 预期更新间隔，单位为ms。定义了开发者期望的更新间隔。默认值：1000。 |

**OH_ArkUI_VisibleAreaEventOptions_GetMeasureFromViewport()**

```ets
bool OH_ArkUI_VisibleAreaEventOptions_GetMeasureFromViewport(ArkUI_VisibleAreaEventOptions* option)
```

描述：

获取可见区域计算模式。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_VisibleAreaEventOptions* option | 可见区域变化监听的参数实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 获取可见区域计算模式。 当measureFromViewport设置为true时，系统在计算该组件的可见区域时，会考虑父组件的NODE_CLIP属性设置。如果父组件的NODE_CLIP为false，则认为其内的子组件可以超出其区域进行显示，因此超出父组件的区域也将被视为可见区域纳入计算；如果父组件的NODE_CLIP设置为true，则组件超出父组件的区域会被裁剪，无法显示，因此会被视为不可见区域进行计算。而当measureFromViewport设置为false时，则不考虑NODE_CLIP的影响，直接将组件超出父组件的部分视为不可见区域。 默认值：false |

**OH_ArkUI_TextPickerRangeContentArray_Create()**

```ets
ArkUI_TextPickerRangeContentArray* OH_ArkUI_TextPickerRangeContentArray_Create(int32_t length)
```

描述：

创建[TextPickerRangeContent](ArkUI_TextPickerRangeContentArray.md)数组的对象。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| int32_t length | 指定TextPickerRangeContent数组的长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_TextPickerRangeContentArray* | 返回指向TextPickerRangeContent空数组的指针。 |

**OH_ArkUI_TextPickerRangeContentArray_SetIconAtIndex()**

```ets
void OH_ArkUI_TextPickerRangeContentArray_SetIconAtIndex(ArkUI_TextPickerRangeContentArray* handle, char* icon, int32_t index)
```

描述：

指定TextPickerRangeContent数组指定位置的icon数据。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextPickerRangeContentArray* handle | 指向TextPickerRangeContent数组的指针。 |
| char* icon | 图片地址。 |
| int32_t index | 数组位置，从0开始。 |

**OH_ArkUI_TextPickerRangeContentArray_SetTextAtIndex()**

```ets
void OH_ArkUI_TextPickerRangeContentArray_SetTextAtIndex(ArkUI_TextPickerRangeContentArray* handle, char* text, int32_t index)
```

描述：

指定TextPickerRangeContent数组指定位置的text数据。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextPickerRangeContentArray* handle | 指向TextPickerRangeContent数组的指针。 |
| char* text | 文本内容。 |
| int32_t index | 数组位置，从0开始。 |

**OH_ArkUI_TextPickerRangeContentArray_Destroy()**

```ets
void OH_ArkUI_TextPickerRangeContentArray_Destroy(ArkUI_TextPickerRangeContentArray* handle)
```

描述：

删除TextPickerRangeContent数组对象。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextPickerRangeContentArray* handle | 指向TextPickerRangeContent数组的指针。 |

**OH_ArkUI_TextCascadePickerRangeContentArray_Create()**

```ets
ArkUI_TextCascadePickerRangeContentArray* OH_ArkUI_TextCascadePickerRangeContentArray_Create(int32_t length)
```

描述：

创建[TextCascadePickerRangeContent](ArkUI_TextCascadePickerRangeContentArray.md)数组对象。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| int32_t length | 指向TextPickerRangeContent数组的长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_TextCascadePickerRangeContentArray* | 返回指向TextCascadePickerRangeContent空数组的指针。 |

**OH_ArkUI_TextCascadePickerRangeContentArray_SetTextAtIndex()**

```ets
void OH_ArkUI_TextCascadePickerRangeContentArray_SetTextAtIndex(ArkUI_TextCascadePickerRangeContentArray* handle, char* text, int32_t index)
```

描述：

指定TextCascadePickerRangeContent数组指定位置的text数据。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextCascadePickerRangeContentArray* handle | 指向TextCascadePickerRangeContentHandle的指针。 |
| char* text | 文本内容。 |
| int32_t index | 数组位置，从0开始。 |

**OH_ArkUI_TextCascadePickerRangeContentArray_SetChildAtIndex()**

```ets
void OH_ArkUI_TextCascadePickerRangeContentArray_SetChildAtIndex(ArkUI_TextCascadePickerRangeContentArray* handle, ArkUI_TextCascadePickerRangeContentArray* child, int32_t index)
```

描述：

指定TextCascadePickerRangeContent数组指定位置的child数据。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextCascadePickerRangeContentArray* handle | 指向TextCascadePickerRangeContentHandle的指针。 |
| ArkUI_TextCascadePickerRangeContentArray* child | 子节点数组指针。 |
| int32_t index | 数组位置，从0开始。 |

**OH_ArkUI_TextCascadePickerRangeContentArray_Destroy()**

```ets
void OH_ArkUI_TextCascadePickerRangeContentArray_Destroy(ArkUI_TextCascadePickerRangeContentArray* handle)
```

描述：

删除TextCascadePickerRangeContent数组对象。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextCascadePickerRangeContentArray* handle | 指向TextCascadePickerRangeContentHandle的指针。 |

**OH_ArkUI_EmbeddedComponentOption_Create()**

```ets
ArkUI_EmbeddedComponentOption* OH_ArkUI_EmbeddedComponentOption_Create()
```

描述：

创建EmbeddedComponent组件选项的对象。

起始版本： 20

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_EmbeddedComponentOption* | 返回指向EmbeddedComponent组件选项的对象的指针。 |

**OH_ArkUI_EmbeddedComponentOption_Dispose()**

```ets
void OH_ArkUI_EmbeddedComponentOption_Dispose(ArkUI_EmbeddedComponentOption* option)
```

描述：

删除EmbeddedComponent组件选项的对象。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_EmbeddedComponentOption* option | 要销毁的EmbeddedComponent组件选项的对象的指针。 |

**OH_ArkUI_EmbeddedComponentOption_SetOnError()**

```ets
void OH_ArkUI_EmbeddedComponentOption_SetOnError(ArkUI_EmbeddedComponentOption* option, void (*callback)(int32_t code, const char* name, const char* message))
```

描述：

设置EmbeddedComponent组件的onError回调。EmbeddedComponent组件在运行过程中发生异常时触发本回调。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_EmbeddedComponentOption* option | EmbeddedComponent组件选项的对象的指针。 |
| void (*callback)(int32_t code, const char* name, const char* message) | 开发者自定义回调函数。 - code：接口调用失败返回的错误码信息。错误码的详细介绍请参考UIExtension错误码。 - name：接口调用失败返回的名称信息。 - message：接口调用失败返回的详细信息。 |

**OH_ArkUI_EmbeddedComponentOption_SetOnTerminated()**

```ets
void OH_ArkUI_EmbeddedComponentOption_SetOnTerminated(ArkUI_EmbeddedComponentOption* option, void (*callback)(int32_t code, AbilityBase_Want* want))
```

描述：

设置EmbeddedComponent组件的onTerminated回调。EmbeddedComponent组件正常退出时触发本回调。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_EmbeddedComponentOption* option | EmbeddedComponent组件选项的对象的指针。 |
| void (*callback)(int32_t code, AbilityBase_Want* want) | 开发者自定义回调函数。 - code：被拉起EmbeddedUIExtensionAbility退出时返回的结果码。若Ability通过调用terminateSelfWithResult退出，结果码为Ability设置的值。若Ability通过调用terminateSelf退出，结果码为默认值"0"。 - want：被拉起EmbeddedUIExtensionAbility退出时返回的数据。 |

**OH_ArkUI_PositionEdges_Create()**

```ets
ArkUI_PositionEdges* OH_ArkUI_PositionEdges_Create()
```

描述：

创建PositionEdges属性对象。

起始版本： 21

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_PositionEdges* | 指向PositionEdges对象的指针。 |

**OH_ArkUI_PositionEdges_Copy()**

```ets
ArkUI_PositionEdges* OH_ArkUI_PositionEdges_Copy(const ArkUI_PositionEdges* edges)
```

描述：

深拷贝PositionEdges属性对象。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PositionEdges* edges | 指向PositionEdges对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_PositionEdges* | 指向新PositionEdges对象的指针。 |

**OH_ArkUI_PositionEdges_Dispose()**

```ets
void OH_ArkUI_PositionEdges_Dispose(ArkUI_PositionEdges* edges)
```

描述：

销毁PositionEdges属性对象。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PositionEdges* edges | 指向PositionEdges对象的指针。 |

**OH_ArkUI_PositionEdges_SetTop()**

```ets
void OH_ArkUI_PositionEdges_SetTop(ArkUI_PositionEdges* edges, float value)
```

描述：

设置PositionEdges属性对象的上方向值。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PositionEdges* edges | 指向PositionEdges对象的指针。 |
| float value | PositionEdges对应方向的值，单位vp。 |

**OH_ArkUI_PositionEdges_GetTop()**

```ets
int32_t OH_ArkUI_PositionEdges_GetTop(ArkUI_PositionEdges* edges, float* value)
```

描述：

获取PositionEdges属性对象的上方向值。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PositionEdges* edges | 指向PositionEdges对象的指针。 |
| float* value | PositionEdges对应方向的值，单位vp。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数无效。 |

**OH_ArkUI_PositionEdges_SetLeft()**

```ets
void OH_ArkUI_PositionEdges_SetLeft(ArkUI_PositionEdges* edges, float value)
```

描述：

设置PositionEdges属性对象的左方向值。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PositionEdges* edges | 指向PositionEdges对象的指针。 |
| float value | PositionEdges对应方向的值，单位vp。 |

**OH_ArkUI_PositionEdges_GetLeft()**

```ets
int32_t OH_ArkUI_PositionEdges_GetLeft(ArkUI_PositionEdges* edges, float* value)
```

描述：

获取PositionEdges属性对象的左方向值。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PositionEdges* edges | 指向PositionEdges对象的指针。 |
| float* value | PositionEdges对应方向的值，单位vp。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数无效。 |

**OH_ArkUI_PositionEdges_SetBottom()**

```ets
void OH_ArkUI_PositionEdges_SetBottom(ArkUI_PositionEdges* edges, float value)
```

描述：

设置PositionEdges属性对象的下方向值。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PositionEdges* edges | 指向PositionEdges对象的指针。 |
| float value | PositionEdges对应方向的值，单位vp。 |

**OH_ArkUI_PositionEdges_GetBottom()**

```ets
int32_t OH_ArkUI_PositionEdges_GetBottom(ArkUI_PositionEdges* edges, float* value)
```

描述：

获取PositionEdges属性对象的下方向值。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PositionEdges* edges | 指向PositionEdges对象的指针。 |
| float* value | PositionEdges对应方向的值，单位vp。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数无效。 |

**OH_ArkUI_PositionEdges_SetRight()**

```ets
void OH_ArkUI_PositionEdges_SetRight(ArkUI_PositionEdges* edges, float value)
```

描述：

设置PositionEdges属性对象的右方向值。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PositionEdges* edges | 指向PositionEdges对象的指针。 |
| float value | PositionEdges对应方向的值，单位vp。 |

**OH_ArkUI_PositionEdges_GetRight()**

```ets
int32_t OH_ArkUI_PositionEdges_GetRight(ArkUI_PositionEdges* edges, float* value)
```

描述：

获取PositionEdges属性对象的右方向值。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PositionEdges* edges | 指向PositionEdges对象的指针。 |
| float* value | PositionEdges对应方向的值，单位vp。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数无效。 |

**OH_ArkUI_PixelRoundPolicy_Create()**

```ets
ArkUI_PixelRoundPolicy* OH_ArkUI_PixelRoundPolicy_Create()
```

描述：

创建PixelRoundPolicy属性对象。

起始版本： 21

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_PixelRoundPolicy* | 指向PixelRoundPolicy对象的指针。 |

**OH_ArkUI_PixelRoundPolicy_Dispose()**

```ets
void OH_ArkUI_PixelRoundPolicy_Dispose(ArkUI_PixelRoundPolicy* policy)
```

描述：

释放PixelRoundPolicy属性对象。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PixelRoundPolicy* policy | 指向要释放的PixelRoundPolicy对象的指针。 |

**OH_ArkUI_PixelRoundPolicy_SetTop()**

```ets
void OH_ArkUI_PixelRoundPolicy_SetTop(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value)
```

描述：

设置PixelRoundPolicy属性对象的上部方向值。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PixelRoundPolicy* policy | 指向PixelRoundPolicy对象的指针。 |
| ArkUI_PixelRoundCalcPolicy value | PixelRoundPolicy对应方向的取整策略。 |

**OH_ArkUI_PixelRoundPolicy_GetTop()**

```ets
int32_t OH_ArkUI_PixelRoundPolicy_GetTop(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value)
```

描述：

获取PixelRoundPolicy属性对象的上部方向值。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PixelRoundPolicy* policy | 指向PixelRoundPolicy对象的指针。 |
| ArkUI_PixelRoundCalcPolicy* value | PixelRoundPolicy对应方向的取整策略。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数无效。 |

**OH_ArkUI_PixelRoundPolicy_SetStart()**

```ets
void OH_ArkUI_PixelRoundPolicy_SetStart(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value)
```

描述：

设置PixelRoundPolicy属性对象的前部方向值。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PixelRoundPolicy* policy | 指向PixelRoundPolicy对象的指针。 |
| ArkUI_PixelRoundCalcPolicy value | PixelRoundPolicy对应方向的取整策略。 |

**OH_ArkUI_PixelRoundPolicy_GetStart()**

```ets
int32_t OH_ArkUI_PixelRoundPolicy_GetStart(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value)
```

描述：

获取PixelRoundPolicy属性对象的前部方向值。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PixelRoundPolicy* policy | 指向PixelRoundPolicy对象的指针。 |
| ArkUI_PixelRoundCalcPolicy* value | PixelRoundPolicy对应方向的取整策略。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数无效。 |

**OH_ArkUI_PixelRoundPolicy_SetBottom()**

```ets
void OH_ArkUI_PixelRoundPolicy_SetBottom(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value)
```

描述：

设置PixelRoundPolicy属性对象的下部方向值。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PixelRoundPolicy* policy | 指向PixelRoundPolicy对象的指针。 |
| ArkUI_PixelRoundCalcPolicy value | PixelRoundPolicy对应方向的取整策略。 |

**OH_ArkUI_PixelRoundPolicy_GetBottom()**

```ets
int32_t OH_ArkUI_PixelRoundPolicy_GetBottom(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value)
```

描述：

获取PixelRoundPolicy属性对象的下部方向值。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PixelRoundPolicy* policy | 指向PixelRoundPolicy对象的指针。 |
| ArkUI_PixelRoundCalcPolicy* value | PixelRoundPolicy对应方向的取整策略。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数无效。 |

**OH_ArkUI_PixelRoundPolicy_SetEnd()**

```ets
void OH_ArkUI_PixelRoundPolicy_SetTop(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value)
```

描述：

设置PixelRoundPolicy属性对象的尾部方向值。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PixelRoundPolicy* policy | 指向PixelRoundPolicy对象的指针。 |
| ArkUI_PixelRoundCalcPolicy value | PixelRoundPolicy对应方向的取整策略。 |

**OH_ArkUI_PixelRoundPolicy_GetEnd()**

```ets
int32_t OH_ArkUI_PixelRoundPolicy_GetEnd(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value)
```

描述：

获取PixelRoundPolicy属性对象的尾部方向值。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PixelRoundPolicy* policy | 指向PixelRoundPolicy对象的指针。 |
| ArkUI_PixelRoundCalcPolicy* value | PixelRoundPolicy对应方向的取整策略。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数无效。 |

**OH_ArkUI_ContentTransitionEffect_Create()**

```ets
ArkUI_ContentTransitionEffect* OH_ArkUI_ContentTransitionEffect_Create(int32_t type)
```

描述：

创建ContentTransitionEffect属性对象。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| int32_t type | 指定动效的转场方式。值为0表示无动效转场，值为1时表示淡入淡出动效转场。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ContentTransitionEffect* | 指向ContentTransitionEffect对象的指针。 |

**OH_ArkUI_GridLayoutOptions_Create()**

```ets
ArkUI_GridLayoutOptions* OH_ArkUI_GridLayoutOptions_Create()
```

描述：

创建Grid布局选项。

起始版本： 22

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_GridLayoutOptions* | Grid布局选项。 |

**OH_ArkUI_GridLayoutOptions_Dispose()**

```ets
void OH_ArkUI_GridLayoutOptions_Dispose(ArkUI_GridLayoutOptions* option)
```

描述：

销毁Grid布局选项。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_GridLayoutOptions* option | Grid布局选项。 |

**OH_ArkUI_GridLayoutOptions_SetIrregularIndexes()**

```ets
int32_t OH_ArkUI_GridLayoutOptions_SetIrregularIndexes(ArkUI_GridLayoutOptions* option, uint32_t* irregularIndexes, int32_t size)
```

描述：

设置Grid中不规则GridItem的索引数组。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_GridLayoutOptions* option | Grid布局选项。 |
| uint32_t* irregularIndexes | GridItem索引数组。 |
| int32_t size | GridItem索引数组大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 异常原因：传入参数验证失败，参数不能为空。 |

**OH_ArkUI_GridLayoutOptions_GetIrregularIndexes()**

```ets
int32_t OH_ArkUI_GridLayoutOptions_GetIrregularIndexes(ArkUI_GridLayoutOptions* option, uint32_t* irregularIndexes, int32_t* size)
```

描述：

获取Grid中不规则GridItem的索引数组。当不设置OH_ArkUI_GridLayoutOptions_RegisterGetIrregularSizeByIndexCallback时，irregularIndexes中GridItem的默认大小为垂直滚动Grid的一整行或水平滚动Grid的一整列。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_GridLayoutOptions* option | Grid布局选项。 |
| uint32_t* irregularIndexes | GridItem索引数组。 |
| int32_t size | GridItem索引数组大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR 数组大小不够。 异常原因：传入参数验证失败，参数不能为空。 |

**OH_ArkUI_GridLayoutOptions_RegisterGetIrregularSizeByIndexCallback()**

```ets
void OH_ArkUI_GridLayoutOptions_RegisterGetIrregularSizeByIndexCallback(ArkUI_GridLayoutOptions* option, void* userData, ArkUI_GridItemSize (*callback)(int32_t itemIndex, void* userData))
```

描述：

Grid布局选项通过GridItem索引获取指定Item占用的行列数。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_GridLayoutOptions* option | Grid布局选项。 |
| void* userData | 用户自定义数据。 |
| ArkUI_GridItemSize (*callback)(int32_t itemIndex, void* userData) | 根据index获取指定Item占用的行列数。 itemIndex：GridItem索引值，取值范围来自OH_ArkUI_GridLayoutOptions_SetIrregularIndexes。 |

**OH_ArkUI_GridLayoutOptions_RegisterGetRectByIndexCallback()**

```ets
void OH_ArkUI_GridLayoutOptions_RegisterGetRectByIndexCallback(ArkUI_GridLayoutOptions* option, void* userData, ArkUI_GridItemRect (*callback)(int32_t itemIndex, void* userData))
```

描述：

Grid布局选项通过GridItem索引获取指定Item的起始行列和占用的行列数。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_GridLayoutOptions* option | Grid布局选项。 |
| void* userData | 用户自定义数据。 |
| ArkUI_GridItemRect (*callback)(int32_t itemIndex, void* userData) | 根据index获取指定Item的起始行列和占用的行列数。 itemIndex：GridItem索引值。 |

**OH_ArkUI_ShowCounterConfig_Create()**

```ets
ArkUI_ShowCounterConfig* OH_ArkUI_ShowCounterConfig_Create()
```

描述：

创建文本输入框计数器的配置对象。

起始版本： 22

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ShowCounterConfig* | 指向文本输入框计数器的配置对象的指针。 |

**OH_ArkUI_ShowCounterConfig_Dispose()**

```ets
void OH_ArkUI_ShowCounterConfig_Dispose(ArkUI_ShowCounterConfig* config)
```

描述：

销毁文本输入框计数器的配置对象。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ShowCounterConfig* config | 销毁文本输入框计数器的配置对象。 |

**OH_ArkUI_ShowCounterConfig_SetCounterTextColor()**

```ets
void OH_ArkUI_ShowCounterConfig_SetCounterTextColor(ArkUI_ShowCounterConfig* config, uint32_t color)
```

描述：

设置文本输入框未达到最大字符数时计数器的颜色。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ShowCounterConfig* config | 指向文本输入框计数器的配置对象指针。 |
| uint32_t color | 文本输入框未达到最大字符数时计数器的颜色，格式为0xARGB。 |

**OH_ArkUI_ShowCounterConfig_SetCounterTextOverflowColor()**

```ets
void OH_ArkUI_ShowCounterConfig_SetCounterTextOverflowColor(ArkUI_ShowCounterConfig* config, uint32_t color)
```

描述：

设置文本输入框超出最大字符数时计数器的颜色。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ShowCounterConfig* config | 指向文本输入框计数器的配置对象指针。 |
| uint32_t color | 文本输入框超出最大字符数时计数器的颜色，格式为0xARGB。 |

**OH_ArkUI_ShowCounterConfig_GetCounterTextColor()**

```ets
uint32_t OH_ArkUI_ShowCounterConfig_GetCounterTextColor(ArkUI_ShowCounterConfig* config)
```

描述：

获取文本输入框未达到最大字符数时计数器的颜色。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ShowCounterConfig* config | 指向文本输入框计数器的配置对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| uint32_t | 返回文本输入框未达到最大字符数时计数器的颜色，格式为0xARGB，如果未通过OH_ArkUI_ShowCounterConfig_SetCounterTextColor接口设置计数器颜色，则返回0。 |

**OH_ArkUI_ShowCounterConfig_GetCounterTextOverflowColor()**

```ets
uint32_t OH_ArkUI_ShowCounterConfig_GetCounterTextOverflowColor(ArkUI_ShowCounterConfig* config)
```

描述：

获取文本输入框超出最大字符数时计数器的颜色。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ShowCounterConfig* config | 指向文本输入框计数器的配置对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| uint32_t | 返回文本输入框超出最大字符数时计数器的颜色，格式为0xARGB，如果未通过OH_ArkUI_ShowCounterConfig_SetCounterTextOverflowColor接口设置计数器颜色，则返回0。 |

**OH_ArkUI_SelectionOptions_Create()**

```ets
ArkUI_SelectionOptions OH_ArkUI_SelectionOptions_Create()
```

描述：

创建选择选项。

起始版本： 23

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_SelectionOptions* | 指向选择选项对象的指针。 |

**OH_ArkUI_SelectionOptions_Dispose()**

```ets
void OH_ArkUI_SelectionOptions_Dispose(ArkUI_SelectionOptions* options)
```

描述：

释放选择选项对象。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SelectionOptions* options | 指向待释放的选择选项对象的指针。 |

**OH_ArkUI_SelectionOptions_SetMenuPolicy()**

```ets
void OH_ArkUI_SelectionOptions_SetMenuPolicy(ArkUI_SelectionOptions* options, ArkUI_MenuPolicy menuPolicy)
```

描述：

设置选择选项的菜单弹出策略。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SelectionOptions* options | 指向选择选项对象的指针。 |
| ArkUI_MenuPolicy  menuPolicy | 菜单弹出策略。 |

**OH_ArkUI_SelectionOptions_GetMenuPolicy()**

```ets
ArkUI_MenuPolicy  OH_ArkUI_SelectionOptions_GetMenuPolicy(ArkUI_SelectionOptions* options)
```

描述：

获取选择选项的菜单弹出策略。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SelectionOptions* options | 指向选择选项对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_MenuPolicy | 菜单弹出策略。 |

**OH_ArkUI_TextContentBaseController_Create()**

```ets
ArkUI_TextContentBaseController* OH_ArkUI_TextContentBaseController_Create()
```

描述：

创建文本内容基础控制器对象。

起始版本： 23

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_TextContentBaseController* | 指向控制器对象的指针。 |

**OH_ArkUI_TextContentBaseController_Dispose()**

```ets
void OH_ArkUI_TextContentBaseController_Dispose(ArkUI_TextContentBaseController* controller)
```

描述：

销毁文本内容基础控制器对象。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextContentBaseController* controller | 待销毁的控制器对象指针。 |

**OH_ArkUI_TextContentBaseController_DeleteBackward()**

```ets
void OH_ArkUI_TextContentBaseController_DeleteBackward(ArkUI_TextContentBaseController* controller)
```

描述：

在编辑态时删除光标前字符。其他状态删除输入框组件的最后一个字符。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextContentBaseController* controller | 待修改的配置对象指针。 |

**OH_ArkUI_TextContentBaseController_ScrollToVisible()**

```ets
void OH_ArkUI_TextContentBaseController_ScrollToVisible(ArkUI_TextContentBaseController* controller, int32_t start, int32_t end)
```

描述：

将起始索引与结束索引传递给与其绑定的输入框组件，并将此范围内的文字滚动到可视区域。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextContentBaseController* controller | 待修改的配置对象指针。 通过此controller将起始索引与结束索引传递给与其绑定的输入框组件并进行滚动操作。 |
| int32_t start | 起始文字索引值。 起始索引应小于等于结束索引，否则接口调用无效。取值范围[0, 输入框文本总长度]，起始索引小于0视为0，大于总长度视为总长度。 |
| int32_t end | 结束文字索引值。 结束索引应大于等于起始索引，否则接口调用无效。取值范围[0, 输入框文本总长度]，结束索引小于0视为0，大于总长度视为总长度。 |

**OH_ArkUI_TextMenuItem_Create()**

```ets
ArkUI_TextMenuItem* OH_ArkUI_TextMenuItem_Create()
```

描述

创建文本菜单项对象。

起始版本： 22

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_TextMenuItem* | 指向ArkUI_TextMenuItem对象的指针。 |

**OH_ArkUI_TextMenuItem_Dispose()**

```ets
void OH_ArkUI_TextMenuItem_Dispose(ArkUI_TextMenuItem* textMenuItem)
```

描述

释放文本菜单项对象。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMenuItem* textMenuItem | 指向ArkUI_TextMenuItem对象的指针。 |

**OH_ArkUI_TextMenuItem_SetContent()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextMenuItem_SetContent(ArkUI_TextMenuItem* item, const char* content)
```

描述

设置文本菜单项标题。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMenuItem* item | 指向ArkUI_TextMenuItem对象的指针。 |
| const char* content | 文本菜单项标题，默认为空字符串。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextMenuItem_GetContent()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextMenuItem_GetContent(const ArkUI_TextMenuItem* item, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

描述

获取文本菜单项标题。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_TextMenuItem* item | 指向ArkUI_TextMenuItem对象的指针。 |
| char* buffer | 缓冲区，由开发者创建分配内存，用于存储文本菜单项标题信息。 |
| int32_t bufferSize | 缓冲区大小。 |
| int32_t* writeLength | 返回值为ARKUI_ERROR_CODE_NO_ERROR时表示实际写入缓冲区的长度。 返回值为ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR时表示字符串完整写入缓冲区所需要的最小长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR 缓冲区大小不足。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextMenuItem_SetIcon()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextMenuItem_SetIcon(ArkUI_TextMenuItem* item, const char* icon)
```

描述

设置文本菜单项图标路径。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMenuItem* item | 指向ArkUI_TextMenuItem对象的指针。 |
| const char* icon | 文本菜单项图标路径，默认空字符串。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextMenuItem_GetIcon()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextMenuItem_GetIcon(const ArkUI_TextMenuItem* item, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

描述

获取文本菜单项图标路径。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_TextMenuItem* item | 指向ArkUI_TextMenuItem对象的指针。 |
| char* buffer | 缓冲区，由开发者创建分配内存，用于存储文本菜单项图标路径信息。 |
| int32_t bufferSize | 缓冲区大小。 |
| int32_t* writeLength | 返回值为ARKUI_ERROR_CODE_NO_ERROR时表示实际写入缓冲区的长度。 返回值为ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR时表示字符串完整写入缓冲区所需要的最小长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR 缓冲区大小不足。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextMenuItem_SetLabelInfo()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextMenuItem_SetLabelInfo(ArkUI_TextMenuItem* item, const char* labelInfo)
```

描述

设置文本菜单项快捷键提示，例如“复制”菜单项的快捷键提示可以设置为“Ctrl+C”。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMenuItem* item | 指向ArkUI_TextMenuItem对象的指针。 |
| const char* labelInfo | 文本菜单项快捷键提示，默认空字符串。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextMenuItem_GetLabelInfo()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextMenuItem_GetLabelInfo(const ArkUI_TextMenuItem* item, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

描述

获取文本菜单项快捷键提示，例如“复制”菜单项的快捷键提示一般为“Ctrl+C”。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_TextMenuItem* item | 指向ArkUI_TextMenuItem对象的指针。 |
| char* buffer | 缓冲区，由开发者创建分配内存，用于存储文本菜单项快捷键提示信息。 |
| int32_t bufferSize | 缓冲区大小。 |
| int32_t* writeLength | 返回值为ARKUI_ERROR_CODE_NO_ERROR时表示实际写入缓冲区的长度。 返回值为ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR时表示字符串完整写入缓冲区所需要的最小长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR 缓冲区大小不足。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextMenuItem_SetId()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextMenuItem_SetId(ArkUI_TextMenuItem* item, int32_t id)
```

描述

设置文本菜单项id。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMenuItem* item | 指向ArkUI_TextMenuItem对象的指针。 |
| int32_t id | 文本菜单项id。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextMenuItem_GetId()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextMenuItem_GetId(const ArkUI_TextMenuItem* item, int32_t* id)
```

描述

获取文本菜单项id。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_TextMenuItem* item | 指向ArkUI_TextMenuItem对象的指针。 |
| int32_t* id | 文本菜单项id。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextMenuItemArray_GetSize()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_GetSize(ArkUI_TextMenuItemArray* items, int32_t* size)
```

描述

获取文本菜单项数组大小。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMenuItemArray* items | 指向ArkUI_TextMenuItemArray对象的指针。 |
| int32_t* size | 文本菜单项数组大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextMenuItemArray_GetItem()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_GetItem(ArkUI_TextMenuItemArray* items, int32_t index, ArkUI_TextMenuItem** item)
```

描述

获取文本菜单项数组中指定索引位置的文本菜单项。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMenuItemArray* items | 指向ArkUI_TextMenuItemArray对象的指针。 |
| int32_t index | 指定索引位置。 |
| ArkUI_TextMenuItem** item | 指向ArkUI_TextMenuItem对象的二级指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextMenuItemArray_Insert()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_Insert(ArkUI_TextMenuItemArray* items, ArkUI_TextMenuItem* item, int32_t index)
```

描述

在文本菜单项数组中指定索引位置插入一个文本菜单项。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMenuItemArray* items | 指向ArkUI_TextMenuItemArray对象的指针。 |
| ArkUI_TextMenuItem* item | 指向ArkUI_TextMenuItem对象的指针。 |
| int32_t index | 要插入文本菜单项的索引位置。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextMenuItemArray_Erase()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_Erase(ArkUI_TextMenuItemArray* items, int32_t index)
```

描述

删除文本菜单项数组中指定索引位置的文本菜单项。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMenuItemArray* items | 指向ArkUI_TextMenuItemArray对象的指针。 |
| int32_t index | 要删除的文本菜单项索引位置。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextMenuItemArray_Clear()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_Clear(ArkUI_TextMenuItemArray* items)
```

描述

清除文本菜单项数组中所有的文本菜单项。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMenuItemArray* items | 指向ArkUI_TextMenuItemArray对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextEditMenuOptions_Create()**

```ets
ArkUI_TextEditMenuOptions* OH_ArkUI_TextEditMenuOptions_Create()
```

描述

创建文本菜单扩展项对象。

起始版本： 22

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_TextEditMenuOptions* editMenuOptions | 指向ArkUI_TextEditMenuOptions对象的指针。 |

**OH_ArkUI_TextEditMenuOptions_Dispose()**

```ets
void OH_ArkUI_TextEditMenuOptions_Dispose(ArkUI_TextEditMenuOptions* editMenuOptions)
```

描述

释放文本菜单扩展项对象。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextEditMenuOptions* editMenuOptions | 指向ArkUI_TextEditMenuOptions对象的指针。 |

**ArkUI_TextCreateMenuCallback()**

```ets
typedef void (*ArkUI_TextCreateMenuCallback)(ArkUI_TextMenuItemArray* items, void* userData)
```

描述

文本菜单创建事件回调函数，在文本菜单创建时会触发此回调函数，开发者可在此函数中设置菜单数据。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMenuItemArray* items | 指向ArkUI_TextMenuItemArray对象的指针，该数组对象由系统内部创建并释放，在回调函数中开发者可以调用OH_ArkUI_TextMenuItemArray_Insert，OH_ArkUI_TextMenuItemArray_Erase进行数组修改。 |
| void* userData | 用户自定义数据。 |

**ArkUI_TextPrepareMenuCallback()**

```ets
typedef void (*ArkUI_TextPrepareMenuCallback)(ArkUI_TextMenuItemArray* items, void* userData)
```

描述

文本菜单准备事件回调函数，当文本选择区域变化后显示菜单之前会触发此回调函数，开发者可在此函数中配置菜单数据。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMenuItemArray* items | 指向ArkUI_TextMenuItemArray对象的指针，该数组对象由系统内部创建并释放，在回调函数中开发者可以调用OH_ArkUI_TextMenuItemArray_Insert，OH_ArkUI_TextMenuItemArray_Erase进行数组修改。 |
| void* userData | 用户自定义数据。 |

**ArkUI_TextMenuItemClickCallback()**

```ets
typedef bool (*ArkUI_TextMenuItemClickCallback)(const ArkUI_TextMenuItem* item,int32_t start, int32_t end, void* userData)
```

描述

文本菜单项点击事件回调函数，在菜单项被点击时触发此回调函数，开发者可在此函数中对系统默认处理行为进行拦截。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_TextMenuItem* item | 指向ArkUI_TextMenuItem对象的指针，表示被点击的文本菜单项。 |
| int32_t start | 选中文本起始索引。 |
| int32_t end | 选中文本结束索引。 |
| void* userData | 用户自定义数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 是否拦截系统默认处理行为。 true：拦截系统默认处理行为，如点击“粘贴”、“复制”等文本菜单项时不再执行系统系统默认处理行为，仅执行开发者自定义处理行为。 false：不拦截系统默认处理行为，如点击“粘贴”、“复制”等文本菜单项时先执行开发者自定义处理行为，再执行系统默认处理行为。 |

**OH_ArkUI_TextEditMenuOptions_RegisterOnCreateMenuCallback()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextEditMenuOptions_RegisterOnCreateMenuCallback(ArkUI_TextEditMenuOptions* editMenuOptions, void* userData, ArkUI_TextCreateMenuCallback cb)
```

描述

注册文本菜单创建事件回调函数。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextEditMenuOptions* editMenuOptions | 指向ArkUI_TextEditMenuOptions对象的指针。 |
| void* userData | 用户自定义数据。 |
| ArkUI_TextCreateMenuCallback cb | 文本菜单创建事件回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextEditMenuOptions_RegisterOnPrepareMenuCallback()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextEditMenuOptions_RegisterOnPrepareMenuCallback(ArkUI_TextEditMenuOptions* editMenuOptions, void* userData, ArkUI_TextPrepareMenuCallback cb)
```

描述

注册文本菜单准备事件回调函数。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextEditMenuOptions* editMenuOptions | 指向ArkUI_TextEditMenuOptions对象的指针。 |
| void* userData | 用户自定义数据。 |
| ArkUI_TextPrepareMenuCallback cb | 文本菜单准备事件回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextEditMenuOptions_RegisterOnMenuItemClickCallback()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextEditMenuOptions_RegisterOnMenuItemClickCallback(ArkUI_TextEditMenuOptions* editMenuOptions, void* userData, ArkUI_TextMenuItemClickCallback cb)
```

描述

注册文本菜单项点击事件回调函数。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextEditMenuOptions* editMenuOptions | 指向ArkUI_TextEditMenuOptions对象的指针。 |
| void* userData | 用户自定义数据。 |
| ArkUI_TextMenuItemClickCallback cb | 文本菜单项点击事件回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextSelectionMenuOptions_Create()**

```ets
ArkUI_TextSelectionMenuOptions* OH_ArkUI_TextSelectionMenuOptions_Create();
```

描述

创建自定义文本选择菜单对象。

起始版本： 22

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_TextSelectionMenuOptions* | 指向ArkUI_TextSelectionMenuOptions对象的指针。 |

**OH_ArkUI_TextSelectionMenuOptions_Dispose()**

```ets
void OH_ArkUI_TextSelectionMenuOptions_Dispose(ArkUI_TextSelectionMenuOptions* selectionMenuOptions)
```

描述

释放自定义文本选择菜单对象。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextSelectionMenuOptions* selectionMenuOptions | 指向ArkUI_TextSelectionMenuOptions对象的指针。 |

**OH_ArkUI_TextSelectionMenuOptions_SetSpanType()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_SetSpanType(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_TextSpanType textSpanType)
```

描述

设置自定义文本选择菜单的文本识别类型。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextSelectionMenuOptions* selectionMenuOptions | 指向ArkUI_TextSelectionMenuOptions对象的指针。 |
| ArkUI_TextSpanType textSpanType | 自定义文本选择菜单的文本识别类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextSelectionMenuOptions_GetSpanType()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_GetSpanType(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_TextSpanType* spanType)
```

描述

获取自定义文本选择菜单的文本识别类型。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextSelectionMenuOptions* selectionMenuOptions | 指向ArkUI_TextSelectionMenuOptions对象的指针。 |
| ArkUI_TextSpanType* spanType | 自定义文本选择菜单的文本识别类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextSelectionMenuOptions_SetContentNode()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_SetContentNode(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_NodeHandle node)
```

描述

设置自定义文本选择菜单的内容节点。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextSelectionMenuOptions* selectionMenuOptions | 指向ArkUI_TextSelectionMenuOptions对象的指针。 |
| ArkUI_NodeHandle node | 自定义文本选择菜单的内容节点。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextSelectionMenuOptions_GetContentNode()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_GetContentNode(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_NodeHandle* node)
```

描述

获取自定义文本选择菜单的内容节点。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextSelectionMenuOptions* selectionMenuOptions | 指向ArkUI_TextSelectionMenuOptions对象的指针。 |
| ArkUI_NodeHandle* node | 自定义文本选择菜单的内容节点。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextSelectionMenuOptions_SetResponseType()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_SetResponseType(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_TextResponseType responseType)
```

描述

设置自定义文本选择菜单的响应类型。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextSelectionMenuOptions* selectionMenuOptions | 指向ArkUI_TextSelectionMenuOptions对象的指针。 |
| ArkUI_TextResponseType responseType | 自定义文本选择菜单的响应类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextSelectionMenuOptions_GetResponseType()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_GetResponseType(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_TextResponseType* responseType)
```

描述

获取自定义文本选择菜单的响应类型。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextSelectionMenuOptions* selectionMenuOptions | 指向ArkUI_TextSelectionMenuOptions对象的指针。 |
| ArkUI_TextResponseType* responseType | 自定义文本选择菜单的响应类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextSelectionMenuOptions_RegisterOnMenuShowCallback()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_RegisterOnMenuShowCallback(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, void* userData, void (*callback)(int32_t start, int32_t end, void* userData))
```

描述

注册自定义文本选择菜单显示事件回调。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextSelectionMenuOptions* selectionMenuOptions | 指向ArkUI_TextSelectionMenuOptions对象的指针。 |
| void* userData | 用户自定义数据，取任意值。设置后，会通过callback回调回传回来。 |
| void (*callback)(int32_t start, int32_t end, void* userData) | 自定义文本选择菜单显示事件回调。 start：选中文本的起始位置。 end：选中文本的结束位置。 userData：用户自定义数据，对应OH_ArkUI_TextSelectionMenuOptions_RegisterOnMenuShowCallback接口的入参userData。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextSelectionMenuOptions_RegisterOnMenuHideCallback()**

```ets
ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_RegisterOnMenuHideCallback(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, void* userData, void (*callback)(int32_t start, int32_t end, void* userData))
```

描述

注册自定义文本选择菜单隐藏事件回调。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextSelectionMenuOptions* selectionMenuOptions | 指向ArkUI_TextSelectionMenuOptions对象的指针。 |
| void* userData | 用户自定义数据，取任意值。设置后，会通过callback回调回传回来。 |
| void (*callback)(int32_t start, int32_t end, void* userData) | 自定义文本选择菜单隐藏事件回调。 start：选中文本的起始位置。 end：选中文本的结束位置。 userData：用户自定义数据，对应OH_ArkUI_TextSelectionMenuOptions_RegisterOnMenuHideCallback接口的入参userData。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_TextMarqueeOptions_Create**

```ets
ArkUI_TextMarqueeOptions* OH_ArkUI_TextMarqueeOptions_Create()
```

描述：

创建文本跑马灯模式配置项。

起始版本： 23

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_TextMarqueeOptions* | 创建文本跑马灯模式配置项的对象指针。 |

**OH_ArkUI_TextMarqueeOptions_Dispose**

```ets
void OH_ArkUI_TextMarqueeOptions_Dispose(ArkUI_TextMarqueeOptions* option)
```

描述：

销毁文本跑马灯模式配置项指针。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMarqueeOptions* option | 需要销毁的文本跑马灯模式配置项对象指针。 |

**OH_ArkUI_TextMarqueeOptions_SetStart**

```ets
void OH_ArkUI_TextMarqueeOptions_SetStart(ArkUI_TextMarqueeOptions* option, bool start)
```

描述：

设置文本跑马灯模式配置项是否播放。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMarqueeOptions* option | 文本跑马灯模式配置项。 |
| bool start | 是否播放。true表示播放，false表示不播放。 |

**OH_ArkUI_TextMarqueeOptions_GetStart**

```ets
bool OH_ArkUI_TextMarqueeOptions_GetStart(ArkUI_TextMarqueeOptions* option)
```

描述：

获取文本跑马灯模式配置项是否播放。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMarqueeOptions* option | 文本跑马灯模式配置项。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 是否播放。true表示播放，false表示不播放。 |

**OH_ArkUI_TextMarqueeOptions_SetStep**

```ets
void OH_ArkUI_TextMarqueeOptions_SetStep(ArkUI_TextMarqueeOptions* option, float step)
```

描述：

设置文本跑马灯模式配置项的步长。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMarqueeOptions* option | 文本跑马灯模式配置项。 |
| float step | 步长。单位：vp。 |

**OH_ArkUI_TextMarqueeOptions_GetStep**

```ets
float OH_ArkUI_TextMarqueeOptions_GetStep(ArkUI_TextMarqueeOptions* option)
```

描述：

获取文本跑马灯模式配置项的步长。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMarqueeOptions* option | 文本跑马灯模式配置项。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 步长。单位：vp。 |

**OH_ArkUI_TextMarqueeOptions_SetSpacing**

```ets
void OH_ArkUI_TextMarqueeOptions_SetSpacing(ArkUI_TextMarqueeOptions* option, float spacing)
```

描述：

设置文本跑马灯模式配置项的首尾间距。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMarqueeOptions* option | 文本跑马灯模式配置项。 |
| float spacing | 首尾间距。单位：vp。 |

**OH_ArkUI_TextMarqueeOptions_GetSpacing**

```ets
float OH_ArkUI_TextMarqueeOptions_GetSpacing(ArkUI_TextMarqueeOptions* option)
```

描述：

获取文本跑马灯模式配置项的首尾间距。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMarqueeOptions* option | 文本跑马灯模式配置项。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 首尾间距。单位：vp。 |

**OH_ArkUI_TextMarqueeOptions_SetLoop**

```ets
void OH_ArkUI_TextMarqueeOptions_SetLoop(ArkUI_TextMarqueeOptions* option, int32_t loop)
```

描述：

设置文本跑马灯模式配置项的重复滚动的次数，小于等于零时无限循环。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMarqueeOptions* option | 文本跑马灯模式配置项。 |
| int32_t loop | 设置的重复滚动的次数。 |

**OH_ArkUI_TextMarqueeOptions_GetLoop**

```ets
int32_t OH_ArkUI_TextMarqueeOptions_GetLoop(ArkUI_TextMarqueeOptions* option)
```

描述：

获取文本跑马灯模式配置项的重复滚动的次数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMarqueeOptions* option | 文本跑马灯模式配置项。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 重复滚动的次数。 |

**OH_ArkUI_TextMarqueeOptions_SetFromStart**

```ets
void OH_ArkUI_TextMarqueeOptions_SetFromStart(ArkUI_TextMarqueeOptions* option, bool fromStart)
```

描述：

设置文本跑马灯模式配置项的运行方向。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMarqueeOptions* option | 文本跑马灯模式配置项。 |
| bool fromStart | 跑马灯运行方向。true表示从头开始滚动，false表示反向滚动。 |

**OH_ArkUI_TextMarqueeOptions_GetFromStart**

```ets
bool OH_ArkUI_TextMarqueeOptions_GetFromStart(ArkUI_TextMarqueeOptions* option)
```

描述：

获取文本跑马灯模式配置项的运行方向。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMarqueeOptions* option | 文本跑马灯模式配置项。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 跑马灯运行方向。true表示从头开始滚动，false表示反向滚动。 |

**OH_ArkUI_TextMarqueeOptions_SetDelay**

```ets
void OH_ArkUI_TextMarqueeOptions_SetDelay(ArkUI_TextMarqueeOptions* option, int32_t delay)
```

描述：

设置文本跑马灯模式配置项的每轮滚动延迟时间。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMarqueeOptions* option | 文本跑马灯模式配置项。 |
| int32_t delay | 每轮滚动延迟时间，单位为毫秒。 |

**OH_ArkUI_TextMarqueeOptions_GetDelay**

```ets
int32_t OH_ArkUI_TextMarqueeOptions_GetDelay(ArkUI_TextMarqueeOptions* option)
```

描述：

获取文本跑马灯模式配置项的每轮滚动延迟时间。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMarqueeOptions* option | 文本跑马灯模式配置项。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回每轮滚动延迟时间，单位为毫秒。 |

**OH_ArkUI_TextMarqueeOptions_SetFadeout**

```ets
void OH_ArkUI_TextMarqueeOptions_SetFadeout(ArkUI_TextMarqueeOptions* option, bool fadeout)
```

描述：

设置文本跑马灯模式配置项是否支持文字超长时的渐隐效果。当Text内容超出显示范围时，未完全展现的文字边缘将应用渐隐效果。

若两端均有文字未完全显示，则两端同时应用渐隐效果。

在渐隐效果开启状态下，[NODE_CLIP](native_node.h.md#ZH-CN_TOPIC_0000002522081032__arkui_nodeattributetype)属性将自动锁定为true，不允许设置为false。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMarqueeOptions* option | 文本跑马灯模式配置项。 |
| bool fadeout | 跑马灯是否支持文字超长时的渐隐效果。 true表示支持渐隐效果，false表示不支持渐隐效果。 |

**OH_ArkUI_TextMarqueeOptions_GetFadeout**

```ets
bool OH_ArkUI_TextMarqueeOptions_GetFadeout(ArkUI_TextMarqueeOptions* option)
```

描述：

获取文本跑马灯模式配置项是否支持文字超长时的渐隐效果。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMarqueeOptions* option | 文本跑马灯模式配置项。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 是否支持文字超长时的渐隐效果。 |

**OH_ArkUI_TextMarqueeOptions_SetStartPolicy**

```ets
void OH_ArkUI_TextMarqueeOptions_SetStartPolicy(ArkUI_TextMarqueeOptions* option, ArkUI_MarqueeStartPolicy startPolicy)
```

描述：

设置文本跑马灯模式配置项的启动策略。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMarqueeOptions* option | 文本跑马灯模式配置项。 |
| ArkUI_MarqueeStartPolicy startPolicy | 启动策略。 |

**OH_ArkUI_TextMarqueeOptions_GetStartPolicy**

```ets
ArkUI_MarqueeStartPolicy OH_ArkUI_TextMarqueeOptions_GetStartPolicy(ArkUI_TextMarqueeOptions* option)
```

描述：

获取文本跑马灯模式配置项的启动策略。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMarqueeOptions* option | 文本跑马灯模式配置项。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_MarqueeStartPolicy | 启动策略。 |

**OH_ArkUI_TextMarqueeOptions_SetUpdatePolicy**

```ets
void OH_ArkUI_TextMarqueeOptions_SetUpdatePolicy(ArkUI_TextMarqueeOptions* option,
    ArkUI_MarqueeUpdatePolicy updatePolicy)
```

描述：

设置文本跑马灯模式配置项的更新策略。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMarqueeOptions* option | 文本跑马灯模式配置项。 |
| ArkUI_MarqueeUpdatePolicy updatePolicy | 更新策略。 |

**OH_ArkUI_TextMarqueeOptions_GetUpdatePolicy**

```ets
ArkUI_MarqueeUpdatePolicy OH_ArkUI_TextMarqueeOptions_GetUpdatePolicy(ArkUI_TextMarqueeOptions* option)
```

描述：

获取文本跑马灯模式配置项的更新策略。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMarqueeOptions* option | 文本跑马灯模式配置项。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_MarqueeUpdatePolicy | 更新策略。 |

**OH_ArkUI_SelectedDragPreviewStyle_Create()**

```ets
ArkUI_SelectedDragPreviewStyle* OH_ArkUI_SelectedDragPreviewStyle_Create();
```

描述

创建选中状态下拖拽文本预览样式对象。

起始版本： 23

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_SelectedDragPreviewStyle* | 指向ArkUI_SelectedDragPreviewStyle对象的指针。 |

**OH_ArkUI_SelectedDragPreviewStyle_Dispose()**

```ets
void OH_ArkUI_SelectedDragPreviewStyle_Dispose(ArkUI_SelectedDragPreviewStyle* config)
```

描述

销毁选中状态下拖拽文本预览样式对象。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SelectedDragPreviewStyle* config | 指向ArkUI_SelectedDragPreviewStyle对象的指针。 |

**OH_ArkUI_SelectedDragPreviewStyle_SetColor()**

```ets
void  OH_ArkUI_SelectedDragPreviewStyle_SetColor(ArkUI_SelectedDragPreviewStyle* config, uint32_t color);
```

描述

设置选中态拖拽文本预览样式的背景色。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SelectedDragPreviewStyle* config | 指向ArkUI_SelectedDragPreviewStyle对象的指针。 |
| uint32_t color | 选中态拖拽文本预览样式的的背景，格式为RGBA。 |

**OH_ArkUI_SelectedDragPreviewStyle_GetColor()**

```ets
uint32_t OH_ArkUI_SelectedDragPreviewStyle_GetColor(ArkUI_SelectedDragPreviewStyle* config)
```

描述

获取选中态拖拽文本预览样式的背景色。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SelectedDragPreviewStyle* config | 指向ArkUI_SelectedDragPreviewStyle对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| uint32_t color | 选中态拖拽文本预览样式的的背景，格式为RGBA。 |

**OH_ArkUI_MotionPathOptions_Create()**

```ets
ArkUI_MotionPathOptions* OH_ArkUI_MotionPathOptions_Create()
```

描述：

创建路径动画的运动路径配置项。

起始版本： 23

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_MotionPathOptions* | 指向路径动画的运动路径配置项ArkUI_MotionPathOptions的指针。 新建的ArkUI_MotionPathOptions对象中，路径动画的运动路径path值为空字符串，路径动画起点进度from值为0，路径动画终点进度to值为1，组件是否沿路径旋转rotatable值为false。 |

**OH_ArkUI_MotionPathOptions_Dispose()**

```ets
void OH_ArkUI_MotionPathOptions_Dispose(ArkUI_MotionPathOptions* options)
```

描述：

销毁路径动画的运动路径配置项。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_MotionPathOptions* options | 指向路径动画的运动路径配置项ArkUI_MotionPathOptions的指针。 |

**OH_ArkUI_MotionPathOptions_SetPath()**

```ets
ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_SetPath(ArkUI_MotionPathOptions* options, const char* svgPath)
```

描述：

设置路径动画的运动路径。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_MotionPathOptions* options | 指向路径动画的运动路径配置项ArkUI_MotionPathOptions的指针。 |
| const char* svgPath | 路径动画的运动路径字符串。 该路径支持使用"start"和"end"作为起点和终点的占位符，例如："Mstart.x start.y L50 50 Lend.x end.y Z"。路径字符串格式请参考绘制路径。若设置为空字符串，等效于未设置路径动画。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_MotionPathOptions_GetPath()**

```ets
ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_GetPath(const ArkUI_MotionPathOptions* options, char* svgPathBuffer, const int32_t bufferSize, int32_t* writeLength)
```

描述：

获取路径动画的运动路径配置项中存储的运动路径字符串。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_MotionPathOptions* options | 指向路径动画的运动路径配置项ArkUI_MotionPathOptions的指针。 |
| char* svgPathBuffer | 存储运动路径字符串的缓冲区指针。 |
| const int32_t bufferSize | svgPathBuffer参数的缓冲区大小。 |
| int32_t* writeLength | 返回ARKUI_ERROR_CODE_NO_ERROR时，表示实际写入缓冲区的字符串长度。 返回ARKUI_ERROR_CODE_PARAM_INVALID时，表示如果为入参异常，writeLength不会被赋值，如果为拷贝异常，writeLength为可容纳目标字符串的最小缓冲区大小。 返回ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR时，表示可容纳目标字符串的最小缓冲区大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR 缓冲区大小不足。 |

**OH_ArkUI_MotionPathOptions_SetFrom()**

```ets
ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_SetFrom(ArkUI_MotionPathOptions* options, const float from)
```

描述：

设置路径动画起点进度。进度指已移动路径长度与总路径长度的比值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_MotionPathOptions* options | 指向路径动画的运动路径配置项ArkUI_MotionPathOptions的指针。 |
| const float from | 路径动画的起点进度，取值范围为[0.0, 1.0]，且需满足from小于或等于终点进度to，否则将返回ARKUI_ERROR_CODE_PARAM_OUT_OF_RANGE错误码。 to的含义参考OH_ArkUI_MotionPathOptions_SetTo。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 ARKUI_ERROR_CODE_PARAM_OUT_OF_RANGE from超出[0.0, 1.0]范围，或from大于终点进度to。 |

**OH_ArkUI_MotionPathOptions_GetFrom()**

```ets
ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_GetFrom(const ArkUI_MotionPathOptions* options, float* from)
```

描述：

获取路径动画的运动路径配置项中的路径动画起点进度。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_MotionPathOptions* options | 指向路径动画的运动路径配置项ArkUI_MotionPathOptions的指针。 |
| float* from | 用于接收路径动画的运动路径配置项ArkUI_MotionPathOptions中起点进度值的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_MotionPathOptions_SetTo()**

```ets
ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_SetTo(ArkUI_MotionPathOptions* options, const float to)
```

描述：

设置路径动画终点进度。进度指已移动路径长度与总路径长度的比值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_MotionPathOptions* options | 指向路径动画的运动路径配置项ArkUI_MotionPathOptions的指针。 |
| const float to | 路径动画的终点进度，取值范围为[0.0, 1.0]，且需满足to大或等于起点进度from；否则将返回ARKUI_ERROR_CODE_PARAM_OUT_OF_RANGE错误码。 from的含义参考OH_ArkUI_MotionPathOptions_SetFrom。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 ARKUI_ERROR_CODE_PARAM_OUT_OF_RANGE to超出[0.0, 1.0]范围，或to小于起点进度from。 |

**OH_ArkUI_MotionPathOptions_GetTo()**

```ets
ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_GetTo(const ArkUI_MotionPathOptions* options, float* to)
```

描述：

获取路径动画的运动路径配置项中的路径动画终点进度。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_MotionPathOptions* options | 指向路径动画的运动路径配置项ArkUI_MotionPathOptions的指针。 |
| float* to | 用于接收路径动画的运动路径配置项ArkUI_MotionPathOptions中终点进度值的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_MotionPathOptions_SetRotatable()**

```ets
ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_SetRotatable(ArkUI_MotionPathOptions* options, const bool rotatable)
```

描述：

设置组件是否沿运动路径旋转。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_MotionPathOptions* options | 指向路径动画的运动路径配置项ArkUI_MotionPathOptions的指针。 |
| const bool rotatable | 组件是否沿路径旋转。true表示组件沿路径旋转；false表示组件不沿路径旋转。默认值：false。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_MotionPathOptions_GetRotatable()**

```ets
ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_GetRotatable(const ArkUI_MotionPathOptions* options, bool* rotatable)
```

描述：

获取组件是否沿运动路径旋转。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_MotionPathOptions* options | 指向路径动画的运动路径配置项ArkUI_MotionPathOptions的指针。 |
| bool* rotatable | 用于接收路径动画的运动路径配置项ArkUI_MotionPathOptions中rotatable参数值的指针，表示组件是否沿路径旋转。 true表示组件沿路径旋转；false表示组件不沿路径旋转。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_PickerIndicatorStyle_Create()**

```ets
ArkUI_PickerIndicatorStyle* OH_ArkUI_PickerIndicatorStyle_Create(ArkUI_PickerIndicatorType type)
```

描述

创建选中项指示器的样式实例。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PickerIndicatorType type | 选择器选中项样式枚举类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_PickerIndicatorStyle* | ArkUI_PickerIndicatorStyle实例。如果返回空指针，表示创建失败，失败原因可是地址空间已满或类型不支持。 |

**OH_ArkUI_PickerIndicatorStyle_Dispose()**

```ets
void OH_ArkUI_PickerIndicatorStyle_Dispose(ArkUI_PickerIndicatorStyle* style)
```

描述

销毁选中项指示器的样式实例。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PickerIndicatorStyle* style | 要销毁的ArkUI_PickerIndicatorStyle实例。 |

**OH_ArkUI_PickerIndicatorStyle_ConfigureBackground()**

```ets
ArkUI_ErrorCode OH_ArkUI_PickerIndicatorStyle_ConfigureBackground(ArkUI_PickerIndicatorStyle* style, ArkUI_PickerIndicatorBackground* background)
```

描述

设置背景样式参数，此接口仅当选择器选中项样式枚举类型为[ARKUI_PICKER_INDICATOR_BACKGROUND](native_type.h.md#ZH-CN_TOPIC_0000002553200995__arkui_pickerindicatortype)时生效。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PickerIndicatorStyle* style | 选中项指示器样式ArkUI_PickerIndicatorStyle的实例。 |
| ArkUI_PickerIndicatorBackground* background | 背景样式参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

**OH_ArkUI_PickerIndicatorStyle_ConfigureDivider()**

```ets
ArkUI_ErrorCode OH_ArkUI_PickerIndicatorStyle_ConfigureDivider(ArkUI_PickerIndicatorStyle* style, ArkUI_PickerIndicatorDivider* divider)
```

描述

设置分割线样式参数，此接口仅当选择器选中项样式枚举类型为[ARKUI_PICKER_INDICATOR_DIVIDER](native_type.h.md#ZH-CN_TOPIC_0000002553200995__arkui_pickerindicatortype)时生效。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PickerIndicatorStyle* style | 选中项指示器样式ArkUI_PickerIndicatorStyle的实例。 |
| ArkUI_PickerIndicatorDivider* divider | 分割线样式参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |