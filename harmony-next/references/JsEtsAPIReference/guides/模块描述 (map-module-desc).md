[]()[]()

# 模块描述

map（地图显示功能）为开发者提供易于上手的接口，开发者可以通过相关接口便捷地在HarmonyOS应用/元服务中加入地图相关的功能，包括显示地图、在地图上绘制（覆盖物）、添加动画、与地图交互、更新地图状态、常用工具函数等功能。

该模块提供以下地图常用功能：

- [MapComponentController](../topics/components/MapComponentController.md)：显示地图，与地图有关的所有方法从此处接入。

地图覆盖物：

- [Marker](../topics/media/Marker.md)：标记。
- [MapPolyline](../topics/graphics/MapPolyline.md)：折线。
- [MapArc](../topics/components/MapArc.md)：弧线。
- [MapPolygon](../topics/system-services/MapPolygon.md)：多边形。
- [MapCircle](../topics/misc/MapCircle.md)：圆形。
- [PointAnnotation](../topics/misc/PointAnnotation.md)：点注释。
- [Bubble](../topics/misc/Bubble.md)：气泡。
- [ClusterOverlay](../topics/misc/ClusterOverlay.md)：点聚合。
- [ImageOverlay](../topics/graphics/ImageOverlay.md)：图片覆盖物。
- [BuildingOverlay](../topics/misc/BuildingOverlay.md)：3D建筑。
- [TraceOverlay](../topics/misc/TraceOverlay.md)：动态轨迹。
- [TileOverlay](../topics/misc/TileOverlay.md)：瓦片图层。
- [Heatmap](../topics/misc/Heatmap.md)：热力图。
- [MvtOverlay](../topics/misc/MvtOverlay.md)：矢量图层。
- [FlowFieldOverlay](../topics/misc/FlowFieldOverlay.md)：流场图层。
- [MassPointOverlay](../topics/misc/MassPointOverlay.md)：海量点图层。

添加动画：

- [Animation](../topics/misc/Animation.md)：动画抽象类。
- [AlphaAnimation](../topics/misc/AlphaAnimation.md)：控制透明度的动画类。
- [RotateAnimation](../topics/misc/RotateAnimation.md)：控制旋转的动画类。
- [ScaleAnimation](../topics/misc/ScaleAnimation.md)：控制缩放的动画类。
- [TranslateAnimation](../topics/misc/TranslateAnimation.md)：控制移动的动画类。
- [FontSizeAnimation](../topics/misc/FontSizeAnimation.md)：控制字体大小的动画类。
- [PlayImageAnimation](../topics/graphics/PlayImageAnimation.md)：控制多张图片的帧动画类。
- [AnimationSet](../topics/misc/AnimationSet.md)：动画类集合。

与地图交互：

- [MapEventManager](../topics/misc/MapEventManager.md)：地图监听事件管理器。

更新地图状态：

- [newLatLng](../topics/misc/newLatLng.md)：设置地图的中心点和缩放层级。
- [newLatLngBounds](../topics/misc/newLatLngBounds (map-map-newlatlngbounds-1).md)：设置地图经纬度范围、地图区域和边界之间的距离。
- [newLatLngBounds](../topics/misc/newLatLngBounds (map-map-newlatlngbounds-2).md)：设置地图经纬度范围、经纬度矩形范围的高和宽、地图区域和边界之间的距离。
- [newLatLngBounds](../topics/misc/newLatLngBounds (map-map-newlatlngbounds-3).md)：设置地图经纬度范围和4个方向与边界之间的距离。
- [scrollBy](../topics/components/scrollBy.md)：按像素移动地图中心点。
- [zoomBy](../topics/misc/zoomBy.md)：根据给定增量并以给定的屏幕像素点为中心点缩放地图级别。
- [zoomIn](../topics/misc/zoomIn.md)：放大地图缩放级别，在当前地图显示的级别基础上加1。
- [zoomOut](../topics/misc/zoomOut.md)：缩小地图缩放级别，在当前地图显示的级别基础上减1。
- [zoomTo](../topics/misc/zoomTo.md)：设置地图缩放级别。

常用工具函数：

- [calculateDistance](../topics/misc/calculateDistance.md)：计算坐标点之间的距离。
- [convertCoordinate](../topics/misc/convertCoordinate.md)：坐标系转换，使用Promise异步回调。
- [convertCoordinateSync](../topics/misc/convertCoordinateSync.md)：坐标系转换。
- [rectifyCoordinate](../topics/misc/rectifyCoordinate.md)：根据用户输入的坐标系和坐标以及获取当前的路由地，判断是否需要修正坐标。

[]()[]()

#### 导入模块

```ets
import { map } from '@kit.MapKit';
```