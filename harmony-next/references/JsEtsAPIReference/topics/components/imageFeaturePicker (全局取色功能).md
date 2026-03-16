# imageFeaturePicker (全局取色功能)

全局取色的功能入口类。

**系统能力：**SystemCapability.Stylus.ColorPicker

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { imageFeaturePicker } from '@kit.Penkit';
```

#### PickedColorInfo

全局取色结果对象，包含取色的基本信息。

**系统能力：**SystemCapability.Stylus.ColorPicker

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

color

[common2D.Color](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-graphics-common2d#color)

否

否

色值。

colorSpace

[colorSpaceManager.ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-colorspacemanager#colorspace)

否

否

色域空间。

timestamp

number

否

否

时间戳，自系统启动以来经过的时间，单位：ms。

#### pickForResult

pickForResult(x?:number, y?:number):Promise<PickedColorInfo>

全局取色，使用Promise异步回调。

**系统能力：**SystemCapability.Stylus.ColorPicker

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

x

number

否

取色器初始位置的x轴坐标。取值范围：0~屏幕的实际宽度，单位：像素。默认值：100

y

number

否

取色器初始位置的y轴坐标。取值范围：0~屏幕的实际高度，单位：像素。默认值：100

**返回值：**

类型

说明

Promise<[PickedColorInfo](#section579673518478)>

Promise对象，返回取色执行的结果。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API 错误码](../../errors/ArkTS API 错误码.md)。

错误码ID

错误信息（此处仅提供错误抛出的关键信息）

401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

801

api is not supported.

1013900001

IPC communication failed.

1013900002

memory is insufficient.

1013900003

service is invalid.

1013900004

multi app call.

1013900005

background service call.

**示例：**

```ets
async colorPick(x?: number, y?: number): Promise<imageFeaturePicker.PickedColorInfo> {
  const pickedColorInfo = await imageFeaturePicker.pickForResult(x, y);
  return pickedColorInfo;
}
```

#### pickForResult

pickForResult(x?:number, y?:number, showValue?:boolean):Promise<PickedColorInfo>

全局取色，使用Promise异步回调。

**系统能力：**SystemCapability.Stylus.ColorPicker

**起始版本：**5.1.0(18)

**参数：**

参数名

类型

必填

说明

x

number

否

取色器初始位置的x轴坐标。取值范围：0~屏幕的实际宽度，单位：像素。默认值：100

y

number

否

取色器初始位置的y轴坐标。取值范围：0~屏幕的实际高度，单位：像素。默认值：100

showValue

boolean

否

是否显示RGB值。true：显示RGB值，false：不显示RGB值。

默认值：false。

**返回值：**

类型

说明

Promise<[PickedColorInfo](#section579673518478)>

Promise对象，返回取色执行的结果。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API 错误码](../../errors/ArkTS API 错误码.md)。

错误码ID

错误信息（此处仅提供错误抛出的关键信息）

401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

801

api is not supported.

1013900001

IPC communication failed.

1013900002

memory is insufficient.

1013900003

service is invalid.

1013900004

multi app call.

1013900005

background service call.

**示例：**

```ets
async colorPick(x?: number, y?: number): Promise<imageFeaturePicker.PickedColorInfo> {
  const pickedColorInfo = await imageFeaturePicker.pickForResult(x, y, true);
  return pickedColorInfo;
}
```