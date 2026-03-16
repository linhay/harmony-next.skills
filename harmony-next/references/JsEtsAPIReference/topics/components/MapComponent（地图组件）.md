# MapComponent（地图组件）

本模块提供Map组件，您需要提供mapOptions和回调，通过回调获取MapComponentController对象。

**起始版本：**4.1.0(11)

#### 导入模块

```ets
import { MapComponent } from '@kit.MapKit';
```

#### MapComponent

MapComponent提供map组件，通过回调获取MapComponentController对象。

**装饰器类型：**@Component

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数**：

**名称**

**类型**

只读

可选

**说明**

mapOptions

[mapCommon.MapOptions](../misc/mapCommon（地图属性模型）.md#section816451553012)

否

否

地图初始化参数。

mapCallback

AsyncCallback<[map.MapComponentController](MapComponentController.md)>

否

否

回调函数，返回[map.MapComponentController](MapComponentController.md)。

**示例：**

```ets
import { MapComponent, mapCommon, map } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

@Entry
@Component
struct HuaweiMapDemo {
  private TAG = "HuaweiMapDemo";
  private mapOptions?: mapCommon.MapOptions;
  private callback?: AsyncCallback<map.MapComponentController>;
  private mapController?: map.MapComponentController;
  private mapEventManager?: map.MapEventManager;

  aboutToAppear(): void {
    // 地图初始化参数，设置地图中心点坐标及层级
    this.mapOptions = {
      position: {
        target: {
          latitude: 39.9,
          longitude: 116.4
        },
        zoom: 10
      }
    };

    // 地图初始化的回调
    this.callback = async (err, mapController) => {
      if (!err) {
        // 获取地图的控制器类，用来操作地图
        this.mapController = mapController;
        this.mapEventManager = this.mapController.getEventManager();
        let callback = () => {
          console.info(this.TAG, `on-mapLoad`);
        }
        this.mapEventManager.on("mapLoad", callback);
      }
    };
  }

  build() {
    Stack() {
      // 调用MapComponent组件初始化地图
      MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback }).width('100%').height('100%')
    }.height('100%')
  }
}
```

#### build

build(): void

struct的默认构造函数，无法直接调用此方法。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

#### customInfoWindow

@BuilderParam customInfoWindow: customInfoWindowCallback

自定义信息窗。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

参数名

**类型**

必填

**说明**

customInfoWindow

[customInfoWindowCallback](#section1038016522147)

是

自定义信息窗。

**示例：**

```ets
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { customInfoWindowCallback } from '@hms.core.map.MapComponent';

@Entry
@Component
struct MarkerDemo {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;

  aboutToAppear(): void {
    this.mapOptions = {
      position: {
        target: {
          latitude: 32.120750,
          longitude: 118.788765
        },
        zoom: 15
      }
    }

    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        let markerOptions: mapCommon.MarkerOptions = {
          position: {
            latitude: 32.120750,
            longitude: 118.788765
          },
          clickable: true,
          // 设置信息窗标题
          title: "自定义信息窗"
        };
        await this.mapController?.addMarker(markerOptions);
      }
    }
  }

  build() {
    Stack() {
      Column() {
        MapComponent({
          mapOptions: this.mapOptions,
          mapCallback: this.callback,
          // 自定义信息窗
          customInfoWindow: this.customInfoWindow
        })
          .width('100%')
          .height('100%')
      }.width('100%')
    }.height('100%')
  }

  // 自定义信息窗BuilderParam
  @BuilderParam customInfoWindow: customInfoWindowCallback = this.customInfoWindowBuilder;

  // 自定义信息窗Builder
  @Builder
  customInfoWindowBuilder($$: map.MarkerDelegate) {
    if ($$.marker) {
      Text($$.marker.getTitle())
        .width("50%")
        .height(50)
        .backgroundColor(Color.Green)
        .textAlign(TextAlign.Center)
        .fontColor(Color.Black)
        .font({ size: 25, weight: 10, style: FontStyle.Italic })
        .border({
          width: 3,
          color: Color.Black,
          radius: 25,
          style: BorderStyle.Dashed
        })
    }
  }
}
```

#### customInfoWindowCallback

type customInfoWindowCallback = (markerDelegate: map.MarkerDelegate) => void

自定义信息窗回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数**：

参数名

**类型**

必填

**说明**

markerDelegate

[map.MarkerDelegate](../media/MarkerDelegate.md)

是

用于显示代理的标记。