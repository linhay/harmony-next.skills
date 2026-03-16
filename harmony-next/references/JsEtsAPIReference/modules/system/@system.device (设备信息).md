# @system.device (设备信息)

本模块提供当前设备的信息。

-

从API Version 6开始，该接口不再维护，推荐使用新接口[@ohos.deviceInfo](../ohos/@ohos.deviceInfo (设备信息).md)进行设备信息查询。

-

本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import device from '@system.device';
```

#### device.getInfo(deprecated)

getInfo(options?: GetDeviceOptions): void

获取当前设备的信息。

在首页的onShow生命周期之前不建议调用device.getInfo接口。

**系统能力：** SystemCapability.Startup.SystemInfo.Lite

**参数：**

参数名类型必填说明options[GetDeviceOptions](#ZH-CN_TOPIC_0000002529285513__getdeviceoptionsdeprecated)否定义设备信息获取的参数选项。

#### GetDeviceOptions(deprecated)

定义设备信息获取的参数选项。

**系统能力：** SystemCapability.Startup.SystemInfo.Lite

名称类型必填说明success(data: DeviceResponse) => void否接口调用成功的回调函数。 data为成功返回的设备信息，具体参考[DeviceResponse](#ZH-CN_TOPIC_0000002529285513__deviceresponsedeprecated)。fail(data：any,code:number）=> void否

接口调用失败的回调函数。 code为失败返回的错误码。

code:200，表示返回结果中存在无法获得的信息。

complete（）=> void否接口调用结束的回调函数。

#### DeviceResponse(deprecated)

设备信息。

**系统能力：** SystemCapability.Startup.SystemInfo.Lite

名称类型说明brandstring品牌。manufacturerstring生产商。modelstring型号。productstring代号。language4+string系统语言。region4+string系统地区。windowWidthnumber可使用的窗口宽度。windowHeightnumber可使用的窗口高度。screenDensity4+number屏幕密度。screenShape4+string

屏幕形状。可取值：

- rect：方形屏；

- circle：圆形屏。

apiVersion4+number系统API版本号。deviceType4+string设备类型。

**示例：**

```ets
export default {
  getInfo() {
    device.getInfo({
      success: function(data) {
        console.log('Device information obtained successfully. Device brand:' + data.brand);
      },
      fail: function(data, code) {
        console.log('Failed to obtain device information. Error code:'+ code + '; Error information: ' + data);
      },
    });
  },
}
```