# 粒子动画 (Particle)

粒子动画是在一定范围内随机生成的大量粒子产生运动而组成的动画。动画元素是一个个粒子，这些粒子可以是圆点、图片。通过对粒子在颜色、透明度、大小、速度、加速度、自旋角度等维度变化做动画，来营造一种氛围感，比如下雪的动效，雪花飘舞就相当于一个个雪花粒子在做动画。

粒子动画的效果通过Particle组件展现。

-

该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

Particle在息屏之后再次打开或者切换后台再次唤起，粒子动画会自动暂停。

#### 子组件

无

#### 接口

```ets
interface ParticleInterface {
  <
    PARTICLE extends ParticleType,
    COLOR_UPDATER extends ParticleUpdater,
    OPACITY_UPDATER extends ParticleUpdater,
    SCALE_UPDATER extends ParticleUpdater,
    ACC_SPEED_UPDATER extends ParticleUpdater,
    ACC_ANGLE_UPDATER extends ParticleUpdater,
    SPIN_UPDATER extends ParticleUpdater
  >(particles: Particles<
      PARTICLE,
      COLOR_UPDATER,
      OPACITY_UPDATER,
      SCALE_UPDATER,
      ACC_SPEED_UPDATER,
      ACC_ANGLE_UPDATER,
      SPIN_UPDATER
    >): ParticleAttribute;
}
```

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

名称类型只读可选说明particles

[Particles](#ZH-CN_TOPIC_0000002497604932__particles18)<

[PARTICLE](#ZH-CN_TOPIC_0000002497604932__particletype),

[COLOR_UPDATER](#ZH-CN_TOPIC_0000002497604932__particleupdater),

[OPACITY_UPDATER](#ZH-CN_TOPIC_0000002497604932__particleupdater),

[SCALE_UPDATER](#ZH-CN_TOPIC_0000002497604932__particleupdater),

[ACC_SPEED_UPDATER](#ZH-CN_TOPIC_0000002497604932__particleupdater),

[ACC_ANGLE_UPDATER](#ZH-CN_TOPIC_0000002497604932__particleupdater),

[SPIN_UPDATER](#ZH-CN_TOPIC_0000002497604932__particleupdater)

>

否否粒子动画的集合，详见[Particles](#ZH-CN_TOPIC_0000002497604932__particles18)属性说明。

#### 属性

除支持[通用属性](../misc/通用属性.md)外还支持以下属性：

#### disturbanceFields12+

disturbanceFields(fields: Array<DisturbanceFieldOptions>)

设置扰动场。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明fieldsArray<[DisturbanceFieldOptions](#ZH-CN_TOPIC_0000002497604932__disturbancefieldoptions12)>是扰动场数组。

#### emitter12+

emitter(value: Array<EmitterProperty>)

支持发射器位置动态更新

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueArray<[EmitterProperty](#ZH-CN_TOPIC_0000002497604932__emitterproperty12)>是需要更新的emitter参数数组

#### rippleFields22+

rippleFields(fields: Array<RippleFieldOptions>|undefined)

设置粒子波动场。波动场会对影响范围内的粒子施加按波形变化的力，产生类似波纹扩散的效果。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明fieldsArray<[RippleFieldOptions](#ZH-CN_TOPIC_0000002497604932__ripplefieldoptions22)>|undefined是粒子波动场数组。通过数组形式可以设置多个粒子波动场。当设置为undefined时，表示无波动场。

#### velocityFields22+

velocityFields(fields: Array<VelocityFieldOptions>|undefined)

设置粒子速度场。速度场会对影响范围内的粒子施加一个力，使粒子在原有速度的基础上叠加速度场指定的速度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明fieldsArray<[VelocityFieldOptions](#ZH-CN_TOPIC_0000002497604932__velocityfieldoptions22)>|undefined是粒子速度场数组。通过数组形式可设置多个粒子速度场。设置为undefined时表示无速度场。

#### 事件

支持[通用事件](../misc/通用事件.md)。

#### ParticleOptions

```ets
interface ParticleOptions<
  PARTICLE extends ParticleType,
  COLOR_UPDATER extends ParticleUpdater,
  OPACITY_UPDATER extends ParticleUpdater,
  SCALE_UPDATER extends ParticleUpdater,
  ACC_SPEED_UPDATER extends ParticleUpdater,
  ACC_ANGLE_UPDATER extends ParticleUpdater,
  SPIN_UPDATER extends ParticleUpdater
> {
  emitter: EmitterOptions<PARTICLE>;
  color?: ParticleColorPropertyOptions<COLOR_UPDATER>;
  opacity?: ParticlePropertyOptions<number, OPACITY_UPDATER>;
  scale?: ParticlePropertyOptions<number, SCALE_UPDATER>;
  velocity?: VelocityOptions;
  acceleration?: AccelerationOptions<ACC_SPEED_UPDATER, ACC_ANGLE_UPDATER>;
  spin?: ParticlePropertyOptions<number, SPIN_UPDATER>;
}
```

设置粒子参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明emitter[EmitterOptions](#ZH-CN_TOPIC_0000002497604932__emitteroptions)<[PARTICLE](#ZH-CN_TOPIC_0000002497604932__particletype)>否否粒子发射器配置。color[ParticleColorPropertyOptions](#ZH-CN_TOPIC_0000002497604932__particlecolorpropertyoptions)<[COLOR_UPDATER](#ZH-CN_TOPIC_0000002497604932__particleupdater)>否是

粒子颜色配置。

**说明**：

默认值：{ range:[Color.White,Color.White] } 。图片粒子不支持设置颜色。

opacity[ParticlePropertyOptions](#ZH-CN_TOPIC_0000002497604932__particlepropertyoptions)<number, [OPACITY_UPDATER](#ZH-CN_TOPIC_0000002497604932__particleupdater)>否是

粒子透明度配置。

默认值：{ range:[1.0,1.0] }

scale[ParticlePropertyOptions](#ZH-CN_TOPIC_0000002497604932__particlepropertyoptions)<number, [SCALE_UPDATER](#ZH-CN_TOPIC_0000002497604932__particleupdater)>否是

粒子大小配置。

默认值：{ range:[1.0,1.0] }

velocity[VelocityOptions](#ZH-CN_TOPIC_0000002497604932__velocityoptions18)否是

粒子速度配置。

**说明**：

speed表示速度大小。angle表示速度的方向（单位为角度），以元素几何中心为坐标原点，水平方向为X轴，正数表示顺时针方向旋转角度。

默认值：{ speed:[0.0,0.0],angle:[0.0,0.0] }

acceleration[AccelerationOptions](#ZH-CN_TOPIC_0000002497604932__accelerationoptions18)<[ACC_SPEED_UPDATER](#ZH-CN_TOPIC_0000002497604932__particleupdater), [ACC_ANGLE_UPDATER](#ZH-CN_TOPIC_0000002497604932__particleupdater)>否是

粒子加速度配置。

**说明**：

speed表示加速度大小，angle表示加速度方向（单位为角度）。

默认值：{ speed:{range:[0.0,0.0]},angle:{range:[0.0,0.0]} }

spin[ParticlePropertyOptions](#ZH-CN_TOPIC_0000002497604932__particlepropertyoptions)<number, [SPIN_UPDATER](#ZH-CN_TOPIC_0000002497604932__particleupdater)>否是

粒子自旋角度配置。

默认值：{range:[0.0,0.0]}

方向：正数表示顺时针旋转，负数表示逆时针旋转。

#### EmitterOptions

```ets
interface EmitterOptions<PARTICLE extends ParticleType> {
  particle: EmitterParticleOptions<PARTICLE>;
  emitRate?: number;
  shape?: ParticleEmitterShape;
  position?: ParticleTuple<Dimension, Dimension>;
  size?: ParticleTuple<Dimension, Dimension>;
  annulusRegion?: ParticleAnnulusRegion;
}
```

粒子发射器的配置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明particle[EmitterParticleOptions](#ZH-CN_TOPIC_0000002497604932__emitterparticleoptions18)<[PARTICLE](#ZH-CN_TOPIC_0000002497604932__particletype)>否否

粒子配置。

-type表示粒子类型，可以选择图片或者是点。

-config表示对应类型的配置。

-config类型和type值有关联：

1. 如果type为ParticleType.POINT，则config类型为[PointParticleParameters](#ZH-CN_TOPIC_0000002497604932__pointparticleparameters) 。

2. 如果type为ParticleType.IMAGE，则config类型为[ImageParticleParameters](#ZH-CN_TOPIC_0000002497604932__imageparticleparameters) 。

-count表示发射的粒子总数，count取值>=-1,当count为-1表示粒子总数无限大。

-lifetime表示单个粒子的生命周期，默认值1000（即1000ms，1s）,lifetime>=-1,当lifetime为-1表示粒子生命周期无限大。当lifetime<-1，取默认值。

**说明**：如果不需要动画一直播放，建议不要将生命周期设置为-1，可能对性能造成较大影响。

lifeTimeRange表示粒子生命周期取值范围，设置lifeTimeRange后粒子的生命周期为 [lifetime-lifeTimeRange,lifeTime+lifeTimeRange]中间的一个随机整数。lifeTimeRange 默认值为0，取值范围为0到正无穷。设置为负值时取默认值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

emitRatenumber否是

发射器发射速率（即每秒发射粒子数）。 默认值：5，小于0时取默认值5。emitRate值超过5000时会极大影响性能，建议设置参数小于5000。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

shape[ParticleEmitterShape](#ZH-CN_TOPIC_0000002497604932__particleemittershape)否是

发射器形状。

默认值：ParticleEmitterShape.RECTANGLE

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

position[ParticleTuple](#ZH-CN_TOPIC_0000002497604932__particletuple18)<[Dimension](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10), [Dimension](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)>否是

发射器位置（距离组件左上角的位置。第一个参数为x方向上的相对偏移，第二个参数为y轴方向相对偏移。）

默认值：[0.0, 0.0]

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

size[ParticleTuple](#ZH-CN_TOPIC_0000002497604932__particletuple18)<[Dimension](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10), [Dimension](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)>否是

发射窗口的大小。第一个参数为发射器宽，第二个参数为发射器高。

默认值：['100%','100%'](即发射窗口占满Particle组件)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

annulusRegion20+[ParticleAnnulusRegion](粒子动画 (Particle).md#ZH-CN_TOPIC_0000002497604932__particleannulusregion20)否是

环形发射器参数。需要发射器形状为环形（即shape参数为ParticleEmitterShape.ANNULUS）时才生效，且对于环形发射器，形状信息必须通过annulusRegion参数指定，position和size不生效。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

#### ParticleConfigs

设置粒子配置项。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明[ParticleType.POINT][PointParticleParameters](#ZH-CN_TOPIC_0000002497604932__pointparticleparameters)否否点状粒子配置。[ParticleType.IMAGE][ImageParticleParameters](#ZH-CN_TOPIC_0000002497604932__imageparticleparameters)否否图片粒子配置。

#### PointParticleParameters

设置粒子半径。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明radius[VP](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__vp10)否否粒子半径。

#### ImageParticleParameters

设置图片选项。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明src[ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否否

图片路径，支持本地图片和网络图片，引用方式请参考[加载图片资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-graphics-display#加载图片资源)。

暂不支持svg图片类型。

src未发生变化时，会优先使用缓存的资源，无法动态切换资源。如需动态切换资源建议切换为不同的src。

size[ParticleTuple](#ZH-CN_TOPIC_0000002497604932__particletuple18)<[Dimension](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10), [Dimension](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)>否否图像尺寸。objectFit[ImageFit](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__imagefit)否是图片显示模式。

#### ParticleColorPropertyOptions

```ets
interface ParticleColorPropertyOptions<UPDATER extends ParticleUpdater> {
  range: ParticleTuple<ResourceColor, ResourceColor>;
  distributionType?: DistributionType;
  updater?: ParticleColorUpdaterOptions<UPDATER>;
}
```

设置粒子颜色属性更新器配置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明range[ParticleTuple](#ZH-CN_TOPIC_0000002497604932__particletuple18)<[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor), [ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)>否否

粒子初始颜色区间，粒子发射器生成粒子的初始颜色在range区间随机取值。

默认值：range:[Color.White,Color.White]

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

distributionType12+[DistributionType](#ZH-CN_TOPIC_0000002497604932__distributiontype12)否是

粒子初始颜色随机值分布，允许用户选择颜色随机值生成的分布类型，支持均匀分布或正态（高斯）分布。

默认值：DistributionType.UNIFORM

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

updater[ParticleColorUpdaterOptions](#ZH-CN_TOPIC_0000002497604932__particlecolorupdateroptions18)<[UPDATER](#ZH-CN_TOPIC_0000002497604932__particleupdater)>否是

颜色属性变化配置。颜色属性变化类型type有三类：

1、当type为ParticleUpdater.NONE，表示无变化，则config类型为[ParticleColorPropertyUpdaterConfigs](#ZH-CN_TOPIC_0000002497604932__particlecolorpropertyupdaterconfigs)[ParticleUpdater.NONE]。

2、type为ParticleUpdater.RANDOM，表示随机变化，则config类型为[ParticleColorPropertyUpdaterConfigs](#ZH-CN_TOPIC_0000002497604932__particlecolorpropertyupdaterconfigs)[ParticleUpdater.RANDOM]。

3、type为ParticleUpdater.CURVE,表示按动画曲线变化，则config类型为[ParticleColorPropertyUpdaterConfigs](#ZH-CN_TOPIC_0000002497604932__particlecolorpropertyupdaterconfigs)[ParticleUpdater.CURVE]。

默认值：type默认为 ParticleUpdater.NONE。

**说明**：

当type为ParticleUpdater.RANDOM或者ParticleUpdater.CURVE时，updater中颜色配置的优先级高于range中的颜色配置。在updater配置的动画时间周期内，以updater中的颜色配置来变化；在updater配置的动画时间周期外，以range中的颜色配置来变化。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

#### ParticleColorPropertyUpdaterConfigs

设置粒子颜色属性更新器的配置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明[ParticleUpdater.NONE]void否否无变化。[ParticleUpdater.RANDOM][ParticleColorOptions](#ZH-CN_TOPIC_0000002497604932__particlecoloroptions18)否否表示变化方式为均匀变化的时候，在区间内随机生成一个差值。r、g、b、a四个颜色通道每秒分别使用差值叠加当前颜色值，生成目标颜色值。实现颜色随机变化的效果。[ParticleUpdater.CURVE]Array<[ParticlePropertyAnimation](#ZH-CN_TOPIC_0000002497604932__particlepropertyanimation)<[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)>>否否表示变化方式为曲线变化时，颜色变化的配置。数组类型表示当前属性可以设置多段动画，如0ms-3000ms，3000ms-5000ms，5000ms-8000ms分别设置动画。

#### ParticlePropertyOptions

```ets
interface ParticlePropertyOptions<TYPE, UPDATER extends ParticleUpdater> {
  range: ParticleTuple<TYPE, TYPE>;
  updater?: ParticleUpdaterOptions<TYPE, UPDATER>;
}
```

设置粒子属性选项。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明range[ParticleTuple](#ZH-CN_TOPIC_0000002497604932__particletuple18)<[TYPE](#ZH-CN_TOPIC_0000002497604932__particleupdater), [TYPE](#ZH-CN_TOPIC_0000002497604932__particleupdater)>否否

粒子初始属性值区间，粒子发射器生成粒子的属性值在range区间随机取值。

**说明**

各项属性的非法输入取默认值，当最大值小于最小值的时候取默认区间。TYPE为number。

不同属性的默认值不同：

1、opacity属性：range:[1.0,1.0]，取值范围为[0, 1]，默认值为1.0。

2、scale属性：range:[1.0,1.0]，取值范围为[0, 10000]，默认值为1.0。

3、acceleration加速度speed属性：range:[0.0,0.0]，取值范围为[0, 10000]，默认值为0.0。

4、acceleration加速度angle属性：range:[0.0,0.0]，取值范围为[-10000, 10000]，默认值为0.0。

5、spin属性：range:[0.0,0.0]，取值范围为[-10000, 10000]，默认值为0.0。

updater[ParticleUpdaterOptions](#ZH-CN_TOPIC_0000002497604932__particleupdateroptions18)<[TYPE](#ZH-CN_TOPIC_0000002497604932__particleupdater), [UPDATER](#ZH-CN_TOPIC_0000002497604932__particleupdater)>否是

属性变化配置。属性变化类型type有三类：

1、当type为ParticleUpdater.NONE，表示无变化，则config类型为[ParticlePropertyUpdaterConfigs](#ZH-CN_TOPIC_0000002497604932__particlepropertyupdaterconfigs)[ParticleUpdater.NONE]。

2、当type为ParticleUpdater.RANDOM，表示变化类型为随机变化，则config类型为[ParticlePropertyUpdaterConfigs](#ZH-CN_TOPIC_0000002497604932__particlepropertyupdaterconfigs)[ParticleUpdater.RANDOM]。

3、当type为ParticleUpdater.CURVE，表示变化类型为曲线变化，则config类型为[ParticlePropertyUpdaterConfigs](#ZH-CN_TOPIC_0000002497604932__particlepropertyupdaterconfigs)[ParticleUpdater.CURVE]

默认值：type默认为ParticleUpdater.NONE。

#### ParticlePropertyUpdaterConfigs

```ets
interface ParticlePropertyUpdaterConfigs<T> {
    [ParticleUpdater.NONE]: void;
    [ParticleUpdater.RANDOM]: ParticleTuple<T, T>;
    [ParticleUpdater.CURVE]: Array<ParticlePropertyAnimation<T>>;
}
```

设置粒子属性更新器配置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明[ParticleUpdater.NONE]void否否无变化。[ParticleUpdater.RANDOM][ParticleTuple](#ZH-CN_TOPIC_0000002497604932__particletuple18)<T, T>否否

表示变化方式为匀速变化时，每秒的变化差值为设置区间随机生成的值。

目标属性值为当前属性值叠加变化差值。如当前属性值为0.2，config取[0.1,1.0]:

1、如果变化差值在区间[0.1,1.0]取随机值0.5，则目标属性值为0.2+0.5 = 0.7；

2、变化差值也可以取负值。如当前属性值为0.2，config为 [-3.0,2.0],如果变化差值在区间[-3.0,2.0]取随机值-2.0，则目标属性值为0.2-2.0 = -1.8。

**说明：**

config配置的是变化差值的取值范围，差值的最大最小值没有约束。但是如果当前属性值叠加差值大于属性最大值，目标属性值取属性最大值；如果当前属性值叠加差值小于属性最小值，目标属性值取属性最小值。T为number。

例如：opacity的取值范围[0.0,1.0]则当当前属性值叠加差值超过1.0，则取1.0。

[ParticleUpdater.CURVE]Array<[ParticlePropertyAnimation](#ZH-CN_TOPIC_0000002497604932__particlepropertyanimation)<T>>否否表示变化方式为曲线变化时，属性变化的配置。数组类型表示当前属性可以设置多段动画，如0ms-3000ms，3000ms-5000ms，5000ms-8000ms分别设置动画。T为number。

#### ParticlePropertyAnimation

```ets
interface ParticlePropertyAnimation<T> {
  from: T;
  to: T;
  startMillis: number;
  endMillis: number;
  curve?: Curve | ICurve;
}
```

设置粒子属性声明周期。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明fromT否否属性起始值。非法输入取对应属性的默认值。toT否否属性目标值。非法输入取对应属性的默认值。startMillisnumber否否

动画开始时间。

单位：毫秒。

取值范围：[0, +∞)。

endMillisnumber否否

动画结束时间。

单位：毫秒。

取值范围：[0, +∞)。

curve[Curve](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__curve) | [ICurve](../../modules/ohos/@ohos.curves (插值计算).md#ZH-CN_TOPIC_0000002497604788__icurve9)否是

设置动画曲线。

默认值：Curve.Linear

#### ParticleType

粒子类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明POINT'point'点状粒子IMAGE'image'图片粒子

#### ParticleEmitterShape

粒子发射器形状。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明RECTANGLE'rectangle'

粒子发射器为矩形。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

CIRCLE'circle'

粒子发射器为圆形。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

ELLIPSE'ellipse'

粒子发射器为椭圆形。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

ANNULUS20+'annulus'

粒子发射器为环形。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

#### DistributionType12+

初始颜色随机值分布类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明UNIFORM0初始颜色随机值分布为均匀分布。GAUSSIAN1初始颜色随机值分布为高斯分布。

#### ParticleUpdater

粒子变化类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明NONE'none'无变化RANDOM'random'随机变化CURVE'curve'动画曲线变化

#### DisturbanceFieldOptions12+

设置粒子扰动场参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明strengthnumber否是

场强，表示场从中心向外的排斥力的强度，默认值0。正数表示排斥力方向朝外，负数表示吸引力，方向朝内。

取值范围：(-∞, +∞)。

shape[DisturbanceFieldShape](#ZH-CN_TOPIC_0000002497604932__disturbancefieldshape12)否是

场的形状。

默认为DisturbanceFieldShape.RECT。

size[SizeT](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__sizett12)<number>否是

场的大小。

默认值 {width:0，height:0}。

width和height的取值范围：[0, +∞)。

position[PositionT](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__positiont12)<number>否是

场的位置。

默认值{x:0，y:0}。

x、y的取值范围：(-∞, +∞)。

feathernumber否是

羽化值，表示场从中心点到场边缘的衰减程度，取值范围0到100的整数，如果0则表示场是一个刚体，所有范围内的粒子都被排斥在外。羽化值越大场的缓和程度越大，场范围内出现越多靠近中心点的粒子。

默认值为0。

noiseScalenumber否是

噪声尺度，用于控制噪声图案的整体大小，取值大于等于0。

默认值1。

noiseFrequencynumber否是

噪声频率，频率越大噪声越细腻，取值大于等于0。

默认值1。

noiseAmplitudenumber否是

噪声震幅，噪声的波动的范围，震幅越大噪音之间差异越大。取值大于等于0。

默认值1。

#### DisturbanceFieldShape12+

粒子形状。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明RECT0长方形。CIRCLE1圆。ELLIPSE2椭圆。

#### EmitterProperty12+

设置发射器属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明indexnumber否否

索引，取整，按初始化参数中发射器的数组索引指定对应的发射器。异常默认值为0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

emitRatenumber否是

发射器发射速率，即每秒发射粒子的数量。

未传入时保持其当前的发射速率， 传入值小于0时取默认值5。emitRate值超过5000时会极大影响性能，建议设置参数小于5000。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

position[PositionT](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__positiont12)<number>否是

发射器位置的数组，只支持number类型。

未传入时保持其当前的发射器位置。需传入两个有效参数，若其中一个为异常值，则position不生效。

x、y的取值范围：(-∞, +∞)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

size[SizeT](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__sizett12)<number>否是

发射窗口的大小，只支持number类型。

未传入时保持其当前发射窗口大小。需传入两个有效参数且都大于0，若其中一个为异常值，则size不生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

annulusRegion20+[ParticleAnnulusRegion](粒子动画 (Particle).md#ZH-CN_TOPIC_0000002497604932__particleannulusregion20)否是

环形发射器参数。需要对应index的发射器形状为环形才生效。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

#### ParticleTuple18+

```ets
declare type ParticleTuple<T1, T2> = [T1, T2];
```

粒子元组，表示定义一些动画参数的类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明[T1, T2]一些动画参数的类型，可能是任何类型。

#### Particles18+

```ets
interface Particles<
  PARTICLE extends ParticleType,
  COLOR_UPDATER extends ParticleUpdater,
  OPACITY_UPDATER extends ParticleUpdater,
  SCALE_UPDATER extends ParticleUpdater,
  ACC_SPEED_UPDATER extends ParticleUpdater,
  ACC_ANGLE_UPDATER extends ParticleUpdater,
  SPIN_UPDATER extends ParticleUpdater
> {
  particles: Array<
    ParticleOptions<
      PARTICLE,
      COLOR_UPDATER,
      OPACITY_UPDATER,
      SCALE_UPDATER,
      ACC_SPEED_UPDATER,
      ACC_ANGLE_UPDATER,
      SPIN_UPDATER
    >
  >;
}
```

粒子动画的集合。

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明particles10+

Array<

ParticleOptions<

PARTICLE,

COLOR_UPDATER,

OPACITY_UPDATER,

SCALE_UPDATER,

ACC_SPEED_UPDATER,

ACC_ANGLE_UPDATER,

SPIN_UPDATER

>

>

否否

粒子动画的集合。每一个的粒子动画（[ParticleOptions](#ZH-CN_TOPIC_0000002497604932__particleoptions)）包含粒子发射，同时可配置粒子的颜色、透明度、大小、速度、加速度与旋转速度，旋转速度，详见[ParticleOptions](#ZH-CN_TOPIC_0000002497604932__particleoptions)属性说明。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

#### VelocityOptions18+

粒子速度配置。

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明speed10+[ParticleTuple](#ZH-CN_TOPIC_0000002497604932__particletuple18)<number, number>否否

表示速度大小。

默认值：{range:[0.0,0.0]}

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

angle10+[ParticleTuple](#ZH-CN_TOPIC_0000002497604932__particletuple18)<number, number>否否

表示速度的方向（单位为角度）。以元素几何中心为坐标原点，水平方向为X轴，正数表示顺时针方向旋转角度。

默认值：{range:[0.0,0.0]}

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

#### AccelerationOptions18+

```ets
declare interface AccelerationOptions<
  ACC_SPEED_UPDATER extends ParticleUpdater,
  ACC_ANGLE_UPDATER extends ParticleUpdater
> {
  speed?: ParticlePropertyOptions<number, ACC_SPEED_UPDATER>;
  angle?: ParticlePropertyOptions<number, ACC_ANGLE_UPDATER>;
}
```

粒子加速度配置。

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明speed10+[ParticlePropertyOptions](#ZH-CN_TOPIC_0000002497604932__particlepropertyoptions)<number, [ACC_SPEED_UPDATER](#ZH-CN_TOPIC_0000002497604932__particleupdater)>否是

表示加速度大小。

默认值：{range:[0.0,0.0]}

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

angle10+[ParticlePropertyOptions](#ZH-CN_TOPIC_0000002497604932__particlepropertyoptions)<number, [ACC_ANGLE_UPDATER](#ZH-CN_TOPIC_0000002497604932__particleupdater)>否是

表示加速度方向（单位为角度）。

默认值：{range:[0.0,0.0]}

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

#### EmitterParticleOptions18+

```ets
interface EmitterParticleOptions<PARTICLE extends ParticleType> {
  type: PARTICLE;
  config: ParticleConfigs[PARTICLE];
  count: number;
  lifetime?: number;
  lifetimeRange?: number;
}
```

粒子配置。

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明type10+[PARTICLE](#ZH-CN_TOPIC_0000002497604932__particletype)否否

表示粒子类型，可以选择图片或者是点。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

config10+[ParticleConfigs](#ZH-CN_TOPIC_0000002497604932__particleconfigs)[PARTICLE]否否

表示对应类型的配置。

config类型和type值有关联：

1. 如果type为ParticleType.POINT，则config类型为[PointParticleParameters](#ZH-CN_TOPIC_0000002497604932__pointparticleparameters) 。

2. 如果type为ParticleType.IMAGE，则config类型为[ImageParticleParameters](#ZH-CN_TOPIC_0000002497604932__imageparticleparameters) 。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

count10+number否否

表示发射的粒子总数，count取值>=-1,当count为-1表示粒子总数无限大。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

lifetime10+number否是

表示单个粒子的生命周期，默认值1000（即1000ms，1s），lifetime>=-1。当lifetime为-1表示粒子生命周期无限大。当lifetime<-1，取默认值。

**说明**：如果不需要动画一直播放，建议不要将生命周期设置为-1，可能对性能造成较大影响。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

lifetimeRange12+number否是

表示粒子生命周期取值范围，设置lifetimeRange后粒子的生命周期为 [lifetime-lifetimeRange,lifeTime+lifetimeRange]中间的一个随机整数。lifetimeRange 默认值为0，取值范围为0到正无穷。设置为负值时取默认值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

#### ParticleUpdaterOptions18+

```ets
interface ParticleUpdaterOptions<TYPE, UPDATER extends ParticleUpdater> {
  type: UPDATER;
  config: ParticlePropertyUpdaterConfigs<TYPE>[UPDATER];
}
```

颜色属性变化配置。

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明type10+[UPDATER](#ZH-CN_TOPIC_0000002497604932__particleupdater)否否

表示颜色属性变化类型。

默认值：type默认为ParticleUpdater.NONE。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。

config10+[ParticlePropertyUpdaterConfigs](#ZH-CN_TOPIC_0000002497604932__particlepropertyupdaterconfigs)<[TYPE](#ZH-CN_TOPIC_0000002497604932__particleupdater)>[[UPDATER](#ZH-CN_TOPIC_0000002497604932__particleupdater)]否否

属性变化配置。属性变化类型type有三类：

1、当type为ParticleUpdater.NONE，表示无变化，则config类型为[ParticlePropertyUpdaterConfigs](#ZH-CN_TOPIC_0000002497604932__particlepropertyupdaterconfigs)[ParticleUpdater.NONE]。

2、当type为ParticleUpdater.RANDOM，表示变化类型为随机变化，则config类型为[ParticlePropertyUpdaterConfigs](#ZH-CN_TOPIC_0000002497604932__particlepropertyupdaterconfigs)[ParticleUpdater.RANDOM]。

3、当type为ParticleUpdater.CURVE，表示变化类型为曲线变化，则config类型为[ParticlePropertyUpdaterConfigs](#ZH-CN_TOPIC_0000002497604932__particlepropertyupdaterconfigs)[ParticleUpdater.CURVE]。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。

#### ParticleColorUpdaterOptions18+

```ets
interface ParticleColorUpdaterOptions<UPDATER extends ParticleUpdater> {
  type: UPDATER;
  config: ParticleColorPropertyUpdaterConfigs[UPDATER];
}
```

颜色属性变化配置。

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明type10+[UPDATER](#ZH-CN_TOPIC_0000002497604932__particleupdater)否否

表示颜色属性变化类型。

默认值：type默认为 ParticleUpdater.NONE。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

config10+[ParticleColorPropertyUpdaterConfigs](#ZH-CN_TOPIC_0000002497604932__particlecolorpropertyupdaterconfigs)[[UPDATER](#ZH-CN_TOPIC_0000002497604932__particleupdater)]否否

颜色属性变化类型type有三类：

1、当type为ParticleUpdater.NONE，表示无变化，则config类型为[ParticleColorPropertyUpdaterConfigs](#ZH-CN_TOPIC_0000002497604932__particlecolorpropertyupdaterconfigs)[ParticleUpdater.NONE]。

2、type为ParticleUpdater.RANDOM，表示随机变化，则config类型为[ParticleColorPropertyUpdaterConfigs](#ZH-CN_TOPIC_0000002497604932__particlecolorpropertyupdaterconfigs)[ParticleUpdater.RANDOM]。

3、type为ParticleUpdater.CURVE,表示按动画曲线变化，则config类型为[ParticleColorPropertyUpdaterConfigs](#ZH-CN_TOPIC_0000002497604932__particlecolorpropertyupdaterconfigs)[ParticleUpdater.CURVE]。

**说明**：

当type为ParticleUpdater.RANDOM或者ParticleUpdater.CURVE时，updater中颜色配置的优先级高于range中的颜色配置。在updater配置的动画时间周期内，以updater中的颜色配置来变化；在updater配置的动画时间周期前，以range中的颜色配置来变化。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

#### ParticleColorOptions18+

颜色变化方式为均匀变化的时候，在区间内随机生成一个差值。r、g、b、a四个颜色通道每秒分别使用差值叠加当前颜色值，生成目标颜色值。实现颜色随机变化的效果。

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明r10+[ParticleTuple](#ZH-CN_TOPIC_0000002497604932__particletuple18)<number, number>否否r颜色通道的差值。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。g10+[ParticleTuple](#ZH-CN_TOPIC_0000002497604932__particletuple18)<number, number>否否g颜色通道的差值。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。b10+[ParticleTuple](#ZH-CN_TOPIC_0000002497604932__particletuple18)<number, number>否否b颜色通道的差值。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。a10+[ParticleTuple](#ZH-CN_TOPIC_0000002497604932__particletuple18)<number, number>否否a颜色通道的差值。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。

#### ParticleAnnulusRegion20+

用于设置环形发射器区域的配置信息。

-

outerRadius、innerRadius小于零或使用百分比单位时，会按零进行处理。

-

当outerRadius小于innerRadius时（即外圆半径小于内圆半径时），会将当前较小的值作为新的内圆半径，将较大的值作为新的外圆半径。

-

当endAngle小于startAngle时（即结束角度小于起始角度时），会将当前较小的值作为新的起始角度，将较大的值作为新的结束角度。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明center[PositionT](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__positiont12)<[LengthMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12)>否是圆环的圆心坐标，组件的左上角为坐标原点。默认值：{x:LengthMetrics.percent(0.5),y:LengthMetrics.percent(0.5)}outerRadius[LengthMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12)否否圆环的外圆半径。innerRadius[LengthMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12)否否圆环的内圆半径。startAnglenumber否是

圆环的起始角度。

单位：度

默认值：0

endAnglenumber否是

圆环的结束角度。

单位：度

默认值：360

#### Vector2T<T>22+

type Vector2T<T> = Vector2T<T>

定义Vector2T类型。其中Vector2T类型包含x和y两个属性值。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明[Vector2T<T>](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__vector2tt12)

用于表示T类型的包含x和y两个值的向量。x表示向量x轴方向的值。y表示向量y轴方向的值。

单位：vp

#### FieldRegion22+

用于设置粒子场的区域信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明shape[DisturbanceFieldShape](#ZH-CN_TOPIC_0000002497604932__disturbancefieldshape12)否是

粒子场的区域形状。

默认值：DisturbanceFieldShape.RECT

position[PositionT](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__positiont12)<number>否是

粒子场的区域中心位置。坐标单位为vp。

默认值：{x:0, y:0}

size[SizeT](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__sizett12)<number>否是

粒子场的区域大小。值的单位为vp。

默认值：{width:0, height:0}

取值范围：

width：[0, +∞)

height：[0, +∞)

当size的width（或height）设置为负值时取width（或height）的默认值。

#### RippleFieldOptions22+

用于描述粒子波动场信息的参数。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明amplitudenumber否是

描述粒子波动场波的幅值。幅值越大，波动场的力越大。

取值范围：[0, +∞)

默认值：0

设置为负值时取默认值。

wavelengthnumber否是

描述粒子波动场的波长，即一个波周期的变化距离。波长越大，则随距离的变化，波的变化越慢，波动越不明显。

取值范围：[0, +∞)

默认值：0

设置为负值时取默认值。

waveSpeednumber否是

描述粒子波动场的波速。波速越大，则随时间的变化，波的变化越快，波动越明显。

取值范围：[0, +∞)

默认值：0

设置为负值时取默认值。

attenuationnumber否是

描述粒子波动场波的衰减系数。衰减系数越大，则随时间的变化，波的衰减越快。

取值范围：[0, 1]

默认值：0.0

设置的数值不在范围内时取默认值。

center[PositionT](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__positiont12)<number>否是

粒子波动场产生力的中心位置。组件的左上角为坐标原点。坐标单位为vp。

默认值：{x:0, y:0}

region[FieldRegion](粒子动画 (Particle).md#ZH-CN_TOPIC_0000002497604932__fieldregion22)否是

粒子波动场影响的区域信息，其中区域信息包括区域形状、区域大小以及区域中心位置。

默认值：{shape:DisturbanceFieldShape.RECT, position:{x:0, y:0}, size:{width:0, height:0}}

#### VelocityFieldOptions22+

用于描述粒子速度场信息的参数。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明velocity[Vector2T](#ZH-CN_TOPIC_0000002497604932__vector2tt22)<number>否是

粒子速度场的各方向速度值。粒子只有在速度场作用范围内时获得该速度，离开速度场范围后不受该速度场影响，不获得该额外的速度。

默认值：{x:0, y:0}

region[FieldRegion](粒子动画 (Particle).md#ZH-CN_TOPIC_0000002497604932__fieldregion22)否是

粒子速度场影响的区域信息，其中区域信息包括区域形状、区域大小以及区域中心位置。

默认值：{shape:DisturbanceFieldShape.RECT, position:{x:0, y:0}, size:{width:0, height:0}}

#### 示例

#### 示例1（圆形初始化粒子）

描述粒子动画基础用法，通过圆形初始化粒子。

```ets
@Entry
@Component
struct ParticleExample {
  build() {
    Stack() {
      Text()
        .width(300).height(300).backgroundColor(Color.Black)
      Particle({
        particles: [
          {
            emitter: {
              particle: {
                type: ParticleType.POINT, //粒子类型
                config: {
                  radius: 10//圆点半径
                },
                count: 500, //粒子总数
                lifetime: 10000, //粒子生命周期，单位ms
                lifetimeRange: 100//粒子生命周期取值范围，单位ms
              },
              emitRate: 10, //每秒发射粒子数
              position: [0, 0],
              shape: ParticleEmitterShape.RECTANGLE//发射器形状
            },
            color: {
              range: [Color.Red, Color.Yellow], //初始颜色范围
              distributionType: DistributionType.GAUSSIAN, // 初始颜色随机值分布
              updater: {
                type: ParticleUpdater.CURVE, //变化方式为曲线变化
                config: [
                  {
                    from: Color.White, //变化起始值
                    to: Color.Pink, //变化终点值
                    startMillis: 0, //开始时间
                    endMillis: 3000, //结束时间
                    curve: Curve.EaseIn//变化曲线
                  },
                  {
                    from: Color.Pink,
                    to: Color.Orange,
                    startMillis: 3000,
                    endMillis: 5000,
                    curve: Curve.EaseIn
                  },
                  {
                    from: Color.Orange,
                    to: Color.Pink,
                    startMillis: 5000,
                    endMillis: 8000,
                    curve: Curve.EaseIn
                  },
                ]
              }
            },
            opacity: {
              range: [0.0, 1.0], //粒子透明度的初始值从【0.0到1.0】随机产生
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0.0,
                    to: 1.0,
                    startMillis: 0,
                    endMillis: 3000,
                    curve: Curve.EaseIn
                  },
                  {
                    from: 1.0,
                    to: 0.0,
                    startMillis: 5000,
                    endMillis: 10000,
                    curve: Curve.EaseIn
                  }
                ]
              }
            },
            scale: {
              range: [0.0, 0.0],
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0.0,
                    to: 0.5,
                    startMillis: 0,
                    endMillis: 3000,
                    curve: Curve.EaseIn
                  }
                ]
              }
            },
            acceleration: {
              //加速度的配置，从大小和方向两个维度变化，speed表示加速度大小，angle表示加速度方向
              speed: {
                range: [3, 9],
                updater: {
                  type: ParticleUpdater.RANDOM, //Speed的变化方式是随机变化
                  config: [1, 20]
                }
              },
              angle: {
                range: [90, 90]
              }
            }

          }
        ]
      }).width(300).height(300)
    }.width('100%').height('100%').align(Alignment.Center)
  }
}
```

#### 示例2（图片初始化粒子）

描述粒子动画基础用法，通过图片初始化粒子。

```ets
@Entry
@Component
struct ParticleExample {
  @State
  myCount: number = 100
  flag: boolean = false;

  build() {
    Column() {
      Stack() {
        Particle({
          particles: [
            {
              emitter: {
                particle: {
                  type: ParticleType.IMAGE,
                  config: {
                    src: $r("app.media.book"),
                    size: [10, 10]
                  },
                  count: this.myCount,
                  lifetime: 10000,
                  lifetimeRange: 100
                },
                emitRate: 3,
                shape: ParticleEmitterShape.CIRCLE
              },
              color: {
                range: [Color.White, Color.White]
              },
              opacity: {
                range: [1.0, 1.0],
                updater: {
                  type: ParticleUpdater.CURVE,
                  config: [
                    {
                      from: 0,
                      to: 1.0,
                      startMillis: 0,
                      endMillis: 6000
                    },
                    {
                      from: 1.0,
                      to: 0,
                      startMillis: 6000,
                      endMillis: 10000
                    }
                  ]
                }
              },
              scale: {
                range: [0.1, 1.0],
                updater: {
                  type: ParticleUpdater.CURVE,
                  config: [
                    {
                      from: 0,
                      to: 1.5,
                      startMillis: 0,
                      endMillis: 8000,
                      curve: Curve.EaseIn
                    }

                  ]
                }
              },
              acceleration: {
                speed: {
                  range: [3, 9],
                  updater: {
                    type: ParticleUpdater.CURVE,
                    config: [
                      {
                        from: 10,
                        to: 20,
                        startMillis: 0,
                        endMillis: 3000,
                        curve: Curve.EaseIn
                      },
                      {
                        from: 10,
                        to: 2,
                        startMillis: 3000,
                        endMillis: 8000,
                        curve: Curve.EaseIn
                      }
                    ]
                  }
                },
                angle: {
                  range: [0, 180],
                  updater: {
                    type: ParticleUpdater.CURVE,
                    config: [{
                      from: 1,
                      to: 2,
                      startMillis: 0,
                      endMillis: 1000,
                      curve: Curve.EaseIn
                    },
                      {
                        from: 50,
                        to: -50,
                        startMillis: 1000,
                        endMillis: 3000,
                        curve: Curve.EaseIn
                      },
                      {
                        from: 3,
                        to: 5,
                        startMillis: 3000,
                        endMillis: 8000,
                        curve: Curve.EaseIn
                      }
                    ]
                  }
                }
              },
              spin: {
                range: [0.1, 1.0],
                updater: {
                  type: ParticleUpdater.CURVE,
                  config: [
                    {
                      from: 0,
                      to: 360,
                      startMillis: 0,
                      endMillis: 8000,
                      curve: Curve.EaseIn
                    }
                  ]
                }
              },
            }
            , {
            emitter: {
              particle: {
                type: ParticleType.IMAGE,
                config: {
                  src: $r('app.media.heart'),
                  size: [10, 10]
                },
                count: this.myCount,
                lifetime: 10000,
                lifetimeRange: 100
              },
              emitRate: 3,
              shape: ParticleEmitterShape.CIRCLE
            },
            color: {
              range: [Color.White, Color.White]
            },
            opacity: {
              range: [1.0, 1.0],
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0,
                    to: 1.0,
                    startMillis: 0,
                    endMillis: 6000
                  },
                  {
                    from: 1.0,
                    to: 0,
                    startMillis: 6000,
                    endMillis: 10000
                  }
                ]
              }
            },
            scale: {
              range: [0.1, 1.0],
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0,
                    to: 2.0,
                    startMillis: 0,
                    endMillis: 10000,
                    curve: Curve.EaseIn
                  }

                ]
              }
            },
            acceleration: {
              speed: {
                range: [3, 9],
                updater: {
                  type: ParticleUpdater.CURVE,
                  config: [
                    {
                      from: 10,
                      to: 20,
                      startMillis: 0,
                      endMillis: 3000,
                      curve: Curve.EaseIn
                    },
                    {
                      from: 10,
                      to: 2,
                      startMillis: 3000,
                      endMillis: 8000,
                      curve: Curve.EaseIn
                    }
                  ]
                }
              },
              angle: {
                range: [0, 180],
                updater: {
                  type: ParticleUpdater.CURVE,
                  config: [{
                    from: 1,
                    to: 2,
                    startMillis: 0,
                    endMillis: 1000,
                    curve: Curve.EaseIn
                  },
                    {
                      from: 50,
                      to: -50,
                      startMillis: 0,
                      endMillis: 3000,
                      curve: Curve.EaseIn
                    },
                    {
                      from: 3,
                      to: 5,
                      startMillis: 3000,
                      endMillis: 10000,
                      curve: Curve.EaseIn
                    }
                  ]
                }
              }
            },
            spin: {
              range: [0.1, 1.0],
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0,
                    to: 360,
                    startMillis: 0,
                    endMillis: 10000,
                    curve: Curve.EaseIn
                  }
                ]
              }
            },
          }, {
            emitter: {
              particle: {
                type: ParticleType.IMAGE,
                config: {
                  src: $r('app.media.sun'),
                  size: [10, 10]
                },
                count: this.myCount,
                lifetime: 10000,
                lifetimeRange: 100
              },
              emitRate: 3,
              shape: ParticleEmitterShape.CIRCLE
            },
            color: {
              range: [Color.White, Color.White]
            },
            opacity: {
              range: [1.0, 1.0],
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0,
                    to: 1.0,
                    startMillis: 0,
                    endMillis: 6000
                  },
                  {
                    from: 1.0,
                    to: 0,
                    startMillis: 6000,
                    endMillis: 10000
                  }
                ]
              }
            },
            scale: {
              range: [0.1, 1.0],
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0,
                    to: 2.0,
                    startMillis: 0,
                    endMillis: 10000,
                    curve: Curve.EaseIn
                  }

                ]
              }
            },
            acceleration: {
              speed: {
                range: [3, 9],
                updater: {
                  type: ParticleUpdater.CURVE,
                  config: [
                    {
                      from: 10,
                      to: 20,
                      startMillis: 0,
                      endMillis: 3000,
                      curve: Curve.EaseIn
                    },
                    {
                      from: 10,
                      to: 2,
                      startMillis: 3000,
                      endMillis: 8000,
                      curve: Curve.EaseIn
                    }
                  ]
                }
              },
              angle: {
                range: [0, 180],
                updater: {
                  type: ParticleUpdater.CURVE,
                  config: [{
                    from: 1,
                    to: 2,
                    startMillis: 0,
                    endMillis: 1000,
                    curve: Curve.EaseIn
                  },
                    {
                      from: 50,
                      to: -50,
                      startMillis: 1000,
                      endMillis: 3000,
                      curve: Curve.EaseIn
                    },
                    {
                      from: 3,
                      to: 5,
                      startMillis: 3000,
                      endMillis: 8000,
                      curve: Curve.EaseIn
                    }
                  ]
                }
              }
            },
            spin: {
              range: [0.1, 1.0],
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0,
                    to: 360,
                    startMillis: 0,
                    endMillis: 10000,
                    curve: Curve.EaseIn
                  }
                ]
              }
            },
          }
          ]
        }).width(300).height(300)

      }.width(500).height(500).align(Alignment.Center)
    }.width("100%").height("100%")

  }
}
```

#### 示例3（粒子扰动场的干扰下运动轨迹发生变化）

该示例主要演示如何通过粒子扰动场的干扰下来实现运动轨迹发生变化的效果。

```ets
@Entry
@Component
struct ParticleExample3 {
  build() {
    Stack() {
      Text()
        .width(300).height(300).backgroundColor(Color.Black)
      Particle({
        particles: [
          {
            emitter: {
              particle: {
                type: ParticleType.POINT, //粒子类型
                config: {
                  radius: 10//圆点半径
                },
                count: 500, //粒子总数
                lifetime: 10000//粒子生命周期，单位ms
              },
              emitRate: 10, //每秒发射粒子数
              position: [0, 0],
              shape: ParticleEmitterShape.RECTANGLE//发射器形状
            },
            color: {
              range: [Color.Red, Color.Yellow], //初始颜色范围
              updater: {
                type: ParticleUpdater.CURVE, //变化方式为曲线变化
                config: [
                  {
                    from: Color.White, //变化起始值
                    to: Color.Pink, //变化终点值
                    startMillis: 0, //开始时间
                    endMillis: 3000, //结束时间
                    curve: Curve.EaseIn//变化曲线
                  },
                  {
                    from: Color.Pink,
                    to: Color.Orange,
                    startMillis: 3000,
                    endMillis: 5000,
                    curve: Curve.EaseIn
                  },
                  {
                    from: Color.Orange,
                    to: Color.Pink,
                    startMillis: 5000,
                    endMillis: 8000,
                    curve: Curve.EaseIn
                  },
                ]
              }
            },
            opacity: {
              range: [0.0, 1.0], //粒子透明度的初始值从[0.0,1.0]随机产生
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0.0,
                    to: 1.0,
                    startMillis: 0,
                    endMillis: 3000,
                    curve: Curve.EaseIn
                  },
                  {
                    from: 1.0,
                    to: 0.0,
                    startMillis: 5000,
                    endMillis: 10000,
                    curve: Curve.EaseIn
                  }
                ]
              }
            },
            scale: {
              range: [0.0, 0.0],
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0.0,
                    to: 0.5,
                    startMillis: 0,
                    endMillis: 3000,
                    curve: Curve.EaseIn
                  }
                ]
              }
            },
            acceleration: {
              //加速度的配置，从大小和方向两个维度变化，speed表示加速度大小，angle表示加速度方向
              speed: {
                range: [3, 9],
                updater: {
                  type: ParticleUpdater.RANDOM,
                  config: [1, 20]
                }
              },
              angle: {
                range: [90, 90]
              }
            }

          }
        ]
      }).width(300).height(300).disturbanceFields([{
        strength: 10,
        shape: DisturbanceFieldShape.RECT,
        size: { width: 100, height: 100 },
        position: { x: 100, y: 100 },
        feather: 15,
        noiseScale: 10,
        noiseFrequency: 15,
        noiseAmplitude: 5
      }])
    }.width('100%').height('100%').align(Alignment.Center)
  }
}
```

#### 示例4（调整粒子发射器位置）

通过emitter()调整粒子发射器的位置。

```ets
@Entry
@Component
struct ParticleExample4 {
  @State emitterProperties: Array<EmitterProperty> = [
    {
      index: 0,
      emitRate: 100,
      position: { x: 60, y: 80 },
      size: { width: 200, height: 200 }
    }
  ];

  build() {
    Stack() {
      Text()
        .width(300).height(300).backgroundColor(Color.Black)
      Particle({
        particles: [
          {
            emitter: {
              particle: {
                type: ParticleType.POINT, // 粒子类型
                config: {
                  radius: 5// 圆点半径
                },
                count: 400, // 粒子总数
                lifetime: -1// 粒子的生命周期，-1表示粒子生命周期无限大
              },
              emitRate: 10, // 每秒发射粒子数
              position: [0, 0], // 粒子发射位置
              shape: ParticleEmitterShape.CIRCLE// 发射器形状
            },
            color: {
              range: [Color.Red, Color.Yellow], // 初始颜色范围
              updater: {
                type: ParticleUpdater.CURVE, // 变化方式为曲线变化
                config: [
                  {
                    from: Color.White,
                    to: Color.Pink,
                    startMillis: 0,
                    endMillis: 3000,
                    curve: Curve.EaseIn
                  },
                  {
                    from: Color.Pink,
                    to: Color.Orange,
                    startMillis: 3000,
                    endMillis: 5000,
                    curve: Curve.EaseIn
                  },
                  {
                    from: Color.Orange,
                    to: Color.Pink,
                    startMillis: 5000,
                    endMillis: 8000,
                    curve: Curve.EaseIn
                  },
                ]
              }
            },
          },
        ]
      })
        .width(300)
        .height(300)
        .emitter(this.emitterProperties)
    }.width('100%').height('100%').align(Alignment.Center)
  }
}
```

#### 示例5（环形发射器创建）

描述粒子动画环形发射器创建的基础用法。

```ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct ParticleExample5 {
  build() {
    Stack() {
      Text()
        .width(300).height(300).backgroundColor(Color.Black)
      Particle({
        particles: [
          {
            emitter: {
              particle: {
                type: ParticleType.POINT, //粒子类型
                config: {
                  radius: 5//圆点半径
                },
                count: 2000, //粒子总数
                lifetime: 10000, //粒子生命周期，单位ms
                lifetimeRange: 100//粒子生命周期取值范围，单位ms
              },
              emitRate: 100, //每秒发射粒子数
              shape: ParticleEmitterShape.ANNULUS,//环形发射器
              annulusRegion:{
                center:{x:LengthMetrics.percent(0.5),y:LengthMetrics.percent(0.5)}, // 圆环的圆心坐标
                innerRadius:LengthMetrics.vp(100), // 圆环的外圆半径
                outerRadius:LengthMetrics.vp(120), // 圆环的内圆半径
                startAngle:0, // 圆环的起始角度
                endAngle:360 // 圆环的结束角度
              }
            },
            color: {
              range: [Color.Pink, Color.White],
            },
            opacity: {
              range: [0.0, 1.0],
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0.0,
                    to: 1.0,
                    startMillis: 0,
                    endMillis: 3000,
                    curve: Curve.EaseIn
                  },
                  {
                    from: 1.0,
                    to: 0.0,
                    startMillis: 5000,
                    endMillis: 10000,
                    curve: Curve.EaseIn
                  }
                ]
              }
            },
            scale: {
              range: [0.0, 0.0],
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0.0,
                    to: 0.5,
                    startMillis: 0,
                    endMillis: 3000,
                    curve: Curve.EaseIn
                  }
                ]
              }
            },
          }
        ]
      }).width(300).height(300)
    }.width('100%').height('100%').align(Alignment.Center)
  }
}
```

#### 示例6（环形发射器更新）

描述粒子动画环形发射器更新的基础用法。

```ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct ParticleExample6 {

  @State radius: number = 1;
  @State shape: ParticleEmitterShape = ParticleEmitterShape.ANNULUS;
  @State emitRate: number = 200;
  @State count: number = 2000;
  private timerID: number = -1;
  private centerX: LengthMetrics = LengthMetrics.percent(0.5);
  private centerY: LengthMetrics = LengthMetrics.percent(0.5);
  private inRadius: LengthMetrics = LengthMetrics.vp(120);
  private outRadius: LengthMetrics = LengthMetrics.vp(120);
  private startAngle: number = 0;
  private endAngle: number = 90;
  @State emitterProperties: Array<EmitterProperty> = [
    {
      index: 0,
      emitRate: 100,
      annulusRegion: {
        center:{x:this.centerX, y: this.centerY}, // 圆环的圆心坐标
        outerRadius: this.outRadius, // 圆环的外圆半径
        innerRadius: this.inRadius, // 圆环的内圆半径
        startAngle: -90, // 圆环的起始角度
        endAngle: 0 // 圆环的结束角度
      }
    }
  ]
  @State region: ParticleAnnulusRegion = {
    center:{x:this.centerX, y: this.centerY},
    outerRadius: this.outRadius,
    innerRadius: this.inRadius,
    startAngle: -90,
    endAngle: 0
  }

  aboutToDisappear(): void {
    // 页面销毁时清除计时器
    if (this.timerID != -1) {
      clearInterval(this.timerID);
    }
  }

  build() {
    Column({ space: 10}) {
      Stack() {
        Text()
          .width(300).height(300).backgroundColor(Color.Black)

        Particle({
          particles: [
            {
              emitter: {
                particle: {
                  type: ParticleType.POINT, // 粒子类型
                  config: {
                    radius: this.radius // 圆点半径
                  },
                  count: this.count, // 粒子总数
                  lifetime: -1 // 粒子的生命周期，-1表示粒子生命周期无限大
                },
                emitRate: this.emitRate, // 每秒发射粒子数
                shape: this.shape, //发射器形状
                annulusRegion: this.region
              },
              color: {
                range: [Color.White, Color.Pink], // 初始颜色范围
              },
            },
          ]
        }).width('100%')
          .height('100%')
          .emitter(this.emitterProperties)
          .onClick(()=>{
            // 清除已有定时器
            if (this.timerID != -1) {
              clearInterval(this.timerID);
            }

            // 创建定时器（每秒更新）
            this.timerID = setInterval(() => {
              this.emitterProperties = [
                {
                  index: 0,
                  emitRate: this.emitRate,
                  annulusRegion: {
                    center:{x:this.centerX, y: this.centerY},
                    outerRadius: this.outRadius,
                    innerRadius: this.inRadius,
                    startAngle: this.startAngle,
                    endAngle: this.endAngle
                  }
                }
              ];
              if (this.endAngle >= 270) {
                if (this.timerID != -1) {
                  clearInterval(this.timerID);
                }
                return;
              }
              // 更新角度值（30度/秒）
              this.startAngle += 30;
              this.endAngle += 30;
            }, 1000);

          })
      }
      .width('100%')
      .height('100%')
      .align(Alignment.Center)
    }
  }
}
```

#### 示例7（设置波动场和速度场）

从API version 22开始，支持设置粒子波动场和速度场。该示例演示如何通过rippleFields接口设置粒子波动场，产生类似波纹扩散的效果。通过velocityFields接口设置粒子速度场，使粒子在原有速度的基础上叠加速度场指定的速度。

```ets
// xxx.ets
@Entry
@Component
struct ParticleExample {
  @State count: number = 1000
  @State particle: EmitterParticleOptions<ParticleType> = {
    type: ParticleType.POINT, // 粒子类型
    config: {
      radius: 1 // 圆点半径
    },
    count: this.count, // 粒子总数
    lifetime: 9000, // 粒子生命周期，单位ms
    lifetimeRange: 100 // 粒子生命周期取值范围，单位ms
  }
  build() {
    Column() {
      Text('波动场')
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
      Stack() {
        Text()
          .width(300).height(300).backgroundColor(Color.Black)
        Particle({
          particles: [
            {
              emitter: {
                particle: this.particle,
                emitRate: 10000, // 每秒发射粒子数
                position: [0, 0],
                shape: ParticleEmitterShape.RECTANGLE // 发射器形状
              },
              color: {
                range: [Color.White, Color.White], // 初始颜色范围
              },
              scale: {
                range: [0.2, 1.5], // 初始大小范围
              },
              opacity	: {
                range: [0.2, 0.8], // 初始透明度范围
              }
            }
          ]
        }).width(300).height(300)
          .rippleFields([
            {
              amplitude: 120, // 波动场幅值
              wavelength: 500, // 波动场的波长
              waveSpeed: 220, // 波动场的波速
              center: { x: 150, y: 150 }, // 波动场的力的中心
              attenuation: 0, // 波动场随时间的衰减系数
              region: {
                // 波动场的影响区域
                shape: DisturbanceFieldShape.RECT, // 波动场影响区域的形状
                position: { x: 150, y: 150 }, // 波动场影响区域的区域中心
                size: { width: 300, height: 300 } // 波动场影响区域的大小
              }
            }
          ])
      }.width("100%").height(300).align(Alignment.Center)
      Text('速度场')
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
      Stack() {
        Text()
          .width(300).height(300).backgroundColor(Color.Black)
        Particle({
          particles: [
            {
              emitter: {
                particle: {
                  type: ParticleType.POINT, // 粒子类型
                  config: {
                    radius: 2 // 圆点半径
                  },
                  count: 1000, // 粒子总数
                  lifetime: 1000, // 粒子生命周期，单位ms
                  lifetimeRange: 0 // 粒子生命周期取值范围，单位ms
                },
                emitRate: 120, // 每秒发射粒子数
                position: [0, 0],
                size: [300, 300],
                shape: ParticleEmitterShape.RECTANGLE // 发射器形状
              },
              color: {
                range: [Color.White, Color.White], // 初始颜色范围
              },
              opacity: {
                range: [1.0, 1.0],
                updater: {
                  type: ParticleUpdater.CURVE, // 透明度按曲线变化
                  config: [
                    {
                      from: 1.0,
                      to: 0.0,
                      startMillis: 0,
                      endMillis: 1000,
                      curve: Curve.EaseIn
                    }
                  ]
                }
              },
            }
          ]
        }).width(300).height(300)
          .margin({ top: 30 })
          .velocityFields([
            {
              velocity: { x: 100, y: 0 }, // 速度场的速度值
              region: {
                // 速度场的影响区域
                shape: DisturbanceFieldShape.RECT, // 速度场影响区域的形状
                position: { x: 150, y: 150 }, // 速度场影响区域的区域中心
                size: { width: 200, height: 200 } // 速度场影响区域的大小
              }
            }
          ])
      }.width("100%").height(300).align(Alignment.Center)
    }
  }
}
```