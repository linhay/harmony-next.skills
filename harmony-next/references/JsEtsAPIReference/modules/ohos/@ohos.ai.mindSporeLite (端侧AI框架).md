# @ohos.ai.mindSporeLite (端侧AI框架)

MindSpore Lite是一个轻量化、高性能的端侧AI引擎，提供了标准的模型推理和训练接口，内置通用硬件高性能算子库，支持Neural Network Runtime Kit使能AI专用芯片加速推理，助力打造全场景智能应用。

本模块主要介绍MindSpore Lite AI引擎支持模型端侧推理/训练的相关能力。

-

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。示例代码使用模型均为MindSpore端侧模型。

-

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { mindSporeLite } from '@kit.MindSporeLiteKit';
```

#### mindSporeLite.loadModelFromFile

loadModelFromFile(model: string, callback: Callback<Model>): void

从完整路径加载输入模型，用于CPU推理。使用callback异步回调。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

参数名类型必填说明modelstring是模型的完整输入路径。字符串长度限制跟随文件系统。callbackCallback<[Model](#ZH-CN_TOPIC_0000002529286125__model)>是回调函数。返回模型对象。

**示例：**

```ets
let modelFile : string = '/path/to/xxx.ms';
mindSporeLite.loadModelFromFile(modelFile, (mindSporeLiteModel : mindSporeLite.Model) => {
  let modelInputs : mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS_LITE_ERR: getInputs failed.')
  } else {
    console.info(modelInputs[0].name);
  }
})
```

#### mindSporeLite.loadModelFromFile

loadModelFromFile(model: string, context: Context, callback: Callback<Model>): void

从完整路径加载输入模型用于推理。使用callback异步回调。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

参数名类型必填说明modelstring是模型的完整输入路径。字符串长度限制跟随文件系统。context[Context](#ZH-CN_TOPIC_0000002529286125__context)是运行环境的配置信息。callbackCallback<[Model](#ZH-CN_TOPIC_0000002529286125__model)>是回调函数。返回模型对象。

**示例：**

```ets
let context: mindSporeLite.Context = {};
context.target = ['cpu'];
let modelFile : string = '/path/to/xxx.ms';
mindSporeLite.loadModelFromFile(modelFile, context, (mindSporeLiteModel : mindSporeLite.Model) => {
  let modelInputs : mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS_LITE_ERR: getInputs failed.')
  } else {
    console.info(modelInputs[0].name);
  }
})
```

#### mindSporeLite.loadModelFromFile

loadModelFromFile(model: string, context?: Context): Promise<Model>

从完整路径加载输入模型用于推理。使用Promise异步函数。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

参数名类型必填说明modelstring是模型的完整输入路径。字符串长度限制跟随文件系统。context[Context](#ZH-CN_TOPIC_0000002529286125__context)否运行环境的配置信息。默认使用CpuDevice初始化。

**返回值：**

类型说明Promise<[Model](#ZH-CN_TOPIC_0000002529286125__model)>Promise对象。返回Model对象。

**示例：**

```ets
let modelFile = '/path/to/xxx.ms';
mindSporeLite.loadModelFromFile(modelFile).then((mindSporeLiteModel : mindSporeLite.Model) => {
  let modelInputs : mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS_LITE_ERR: getInputs failed.')
  } else {
    console.info(modelInputs[0].name);
  }
})
```

#### mindSporeLite.loadModelFromBuffer

loadModelFromBuffer(model: ArrayBuffer, callback: Callback<Model>): void

从内存加载输入模型，用于CPU推理。使用callback异步回调。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

参数名类型必填说明modelArrayBuffer是包含模型的内存。callbackCallback<[Model](#ZH-CN_TOPIC_0000002529286125__model)>是回调函数。返回模型对象。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let modelFile = 'xxx.ms';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext().resourceManager.getRawFileContent(modelFile).then((buffer: Uint8Array) => {
  let modelBuffer = buffer.buffer;
  mindSporeLite.loadModelFromBuffer(modelBuffer, (mindSporeLiteModel: mindSporeLite.Model) => {
    let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
    console.info('MS_LITE_LOG: ' + modelInputs[0].name);
  })
}).catch((error: BusinessError) => {
  console.error("getRawFileContent promise error is " + error);
});
```

#### mindSporeLite.loadModelFromBuffer

loadModelFromBuffer(model: ArrayBuffer, context: Context, callback: Callback<Model>): void

从内存加载输入模型用于推理。使用callback异步回调。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

参数名类型必填说明modelArrayBuffer是包含模型的内存。context[Context](#ZH-CN_TOPIC_0000002529286125__context)是运行环境的配置信息。callbackCallback<[Model](#ZH-CN_TOPIC_0000002529286125__model)>是回调函数。返回模型对象。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let modelFile = 'xxx.ms';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext().resourceManager.getRawFileContent(modelFile).then((buffer: Uint8Array) => {
  let modelBuffer = buffer.buffer;
  let context: mindSporeLite.Context = {};
  context.target = ['cpu'];
  mindSporeLite.loadModelFromBuffer(modelBuffer, context, (mindSporeLiteModel: mindSporeLite.Model) => {
    let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
    console.info('MS_LITE_LOG: ' + modelInputs[0].name);
  })
}).catch((error: BusinessError) => {
  console.error("getRawFileContent promise error is " + error);
});
```

#### mindSporeLite.loadModelFromBuffer

loadModelFromBuffer(model: ArrayBuffer, context?: Context): Promise<Model>

从内存加载输入模型用于推理。使用Promise异步函数。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

参数名类型必填说明modelArrayBuffer是包含模型的内存。context[Context](#ZH-CN_TOPIC_0000002529286125__context)否运行环境的配置信息。默认使用CpuDevice初始化。

**返回值：**

类型说明Promise<[Model](#ZH-CN_TOPIC_0000002529286125__model)>Promise对象。返回Model对象。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let modelFile = 'xxx.ms';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext().resourceManager.getRawFileContent(modelFile).then((buffer: Uint8Array) => {
  let modelBuffer = buffer.buffer;
  mindSporeLite.loadModelFromBuffer(modelBuffer).then((mindSporeLiteModel: mindSporeLite.Model) => {
    let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
    console.info('MS_LITE_LOG: ' + modelInputs[0].name);
  })
}).catch((error: BusinessError) => {
  console.error("getRawFileContent promise error is " + error);
});
```

#### mindSporeLite.loadModelFromFd

loadModelFromFd(model: number, callback: Callback<Model>): void

从文件描述符加载输入模型，用于CPU推理。使用callback异步回调。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

参数名类型必填说明modelnumber是模型的文件描述符。跟随文件系统返回fd值传入。callbackCallback<[Model](#ZH-CN_TOPIC_0000002529286125__model)>是回调函数。返回模型对象。

**示例：**

```ets
import { fileIo } from '@kit.CoreFileKit';
let modelFile = '/path/to/xxx.ms';
let file = fileIo.openSync(modelFile, fileIo.OpenMode.READ_ONLY);
mindSporeLite.loadModelFromFd(file.fd, (mindSporeLiteModel : mindSporeLite.Model) => {
  let modelInputs : mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS_LITE_ERR: getInputs failed.')
  } else {
    console.info(modelInputs[0].name);
  }
})
```

#### mindSporeLite.loadModelFromFd

loadModelFromFd(model: number, context: Context, callback: Callback<Model>): void

从文件描述符加载输入模型用于推理。使用callback异步回调。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

参数名类型必填说明modelnumber是模型的文件描述符。跟随文件系统返回fd值传入。context[Context](#ZH-CN_TOPIC_0000002529286125__context)是运行环境的配置信息。callbackCallback<[Model](#ZH-CN_TOPIC_0000002529286125__model)>是回调函数。返回模型对象。

**示例：**

```ets
import { fileIo } from '@kit.CoreFileKit';
let modelFile = '/path/to/xxx.ms';
let context : mindSporeLite.Context = {};
context.target = ['cpu'];
let file = fileIo.openSync(modelFile, fileIo.OpenMode.READ_ONLY);
mindSporeLite.loadModelFromFd(file.fd, context, (mindSporeLiteModel : mindSporeLite.Model) => {
  let modelInputs : mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS_LITE_ERR: getInputs failed.')
  } else {
    console.info(modelInputs[0].name);
  }
})
```

#### mindSporeLite.loadModelFromFd

loadModelFromFd(model: number, context?: Context): Promise<Model>

从文件描述符加载输入模型用于推理。使用Promise异步函数。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

参数名类型必填说明modelnumber是模型的文件描述符。跟随文件系统返回fd值传入。context[Context](#ZH-CN_TOPIC_0000002529286125__context)否运行环境的配置信息。默认使用CpuDevice初始化。

**返回值：**

类型说明Promise<[Model](#ZH-CN_TOPIC_0000002529286125__model)>Promise对象。返回Model对象。

**示例：**

```ets
import { fileIo } from '@kit.CoreFileKit';
let modelFile = '/path/to/xxx.ms';
let file = fileIo.openSync(modelFile, fileIo.OpenMode.READ_ONLY);
mindSporeLite.loadModelFromFd(file.fd).then((mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS_LITE_ERR: getInputs failed.')
  } else {
    console.info(modelInputs[0].name);
  }
})
```

#### mindSporeLite.loadTrainModelFromFile12+

loadTrainModelFromFile(model: string, trainCfg?: TrainCfg, context?: Context): Promise<Model>

根据路径加载训练模型文件。使用Promise异步回调。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

参数名类型必填说明modelstring是模型的完整输入路径。字符串长度限制跟随文件系统。trainCfg[TrainCfg](#ZH-CN_TOPIC_0000002529286125__traincfg12)否模型训练配置。默认值为TrainCfg各属性默认值。context[Context](#ZH-CN_TOPIC_0000002529286125__context)否运行环境的配置信息。默认使用CpuDevice初始化。

**返回值：**

类型说明Promise<[Model](#ZH-CN_TOPIC_0000002529286125__model)>Promise对象。返回Model对象。

**示例：**

```ets
let modelFile = '/path/to/xxx.ms';
mindSporeLite.loadTrainModelFromFile(modelFile).then((mindSporeLiteModel : mindSporeLite.Model) => {
  let modelInputs : mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS_LITE_ERR: getInputs failed.')
  } else {
    console.info(modelInputs[0].name);
  }
})
```

#### mindSporeLite.loadTrainModelFromBuffer12+

loadTrainModelFromBuffer(model: ArrayBuffer, trainCfg?: TrainCfg, context?: Context): Promise<Model>

从内存缓冲区加载训练模型。使用Promise异步回调。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

参数名类型必填说明modelArrayBuffer是包含训练模型的内存。trainCfg[TrainCfg](#ZH-CN_TOPIC_0000002529286125__traincfg12)否模型训练配置。默认值为TrainCfg各属性默认值。context[Context](#ZH-CN_TOPIC_0000002529286125__context)否运行环境的配置信息。默认使用CpuDevice初始化。

**返回值：**

类型说明Promise<[Model](#ZH-CN_TOPIC_0000002529286125__model)>Promise对象。返回Model对象。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let modelFile = 'xxx.ms';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext().resourceManager.getRawFileContent(modelFile).then((buffer: Uint8Array) => {
  let modelBuffer = buffer.buffer;
  mindSporeLite.loadTrainModelFromBuffer(modelBuffer).then((mindSporeLiteModel: mindSporeLite.Model) => {
    console.info("MSLITE trainMode: ", mindSporeLiteModel.trainMode);
  })
}).catch((error: BusinessError) => {
  console.error("getRawFileContent promise error is " + error);
});
```

#### mindSporeLite.loadTrainModelFromFd12+

loadTrainModelFromFd(model: number, trainCfg?: TrainCfg, context?: Context): Promise<Model>

从文件描述符加载训练模型文件。使用Promise异步回调。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

参数名类型必填说明modelnumber是训练模型的文件描述符。跟随文件系统返回fd值传入。trainCfg[TrainCfg](#ZH-CN_TOPIC_0000002529286125__traincfg12)否模型训练配置。默认值为TrainCfg各属性默认值。context[Context](#ZH-CN_TOPIC_0000002529286125__context)否运行环境的配置信息。默认使用CpuDevice初始化。

**返回值：**

类型说明Promise<[Model](#ZH-CN_TOPIC_0000002529286125__model)>Promise对象。返回Model对象。

**示例：**

```ets
import { fileIo } from '@kit.CoreFileKit';
let modelFile = '/path/to/xxx.ms';
let file = fileIo.openSync(modelFile, fileIo.OpenMode.READ_ONLY);
mindSporeLite.loadTrainModelFromFd(file.fd).then((mindSporeLiteModel: mindSporeLite.Model) => {
  console.info("MSLITE trainMode: ", mindSporeLiteModel.trainMode);
});
```

#### mindSporeLite.getAllNNRTDeviceDescriptions12+

getAllNNRTDeviceDescriptions() : NNRTDeviceDescription[]

获取NNRt中的所有设备描述。

**系统能力：** SystemCapability.AI.MindSporeLite

**返回值：**

类型说明[NNRTDeviceDescription](#ZH-CN_TOPIC_0000002529286125__nnrtdevicedescription12)[]NNRt设备描述信息数组。

**示例：**

```ets
let allDevices = mindSporeLite.getAllNNRTDeviceDescriptions();
if (allDevices == null) {
  console.error('MS_LITE_LOG: getAllNNRTDeviceDescriptions is NULL.');
}
```

#### Context

定义运行环境的配置信息。

**系统能力：** SystemCapability.AI.MindSporeLite

名称类型只读可选说明targetstring[]否是配置目标后端。可选'cpu'，'nnrt'，默认'cpu'。cpu[CpuDevice](#ZH-CN_TOPIC_0000002529286125__cpudevice)否是CPU后端设备选项。只有当target包含'cpu'时，才能设置此属性。默认值为CpuDevice各属性默认值。nnrt[NNRTDevice](#ZH-CN_TOPIC_0000002529286125__nnrtdevice)否是NNRt后端设备选项。只有当target包含'nnrt'时，才能设置此属性。默认值为NNRTDevice各属性默认值。

**示例：**

```ets
let context: mindSporeLite.Context = {};
context.target = ['cpu','nnrt'];
```

#### CpuDevice

CPU后端设备选项。

**系统能力：** SystemCapability.AI.MindSporeLite

名称类型只读可选说明threadNumnumber否是设置运行时的线程数，默认值：2。threadAffinityMode[ThreadAffinityMode](#ZH-CN_TOPIC_0000002529286125__threadaffinitymode)否是设置运行时的CPU绑核策略模式，默认值为不绑核：mindSporeLite.ThreadAffinityMode.NO_AFFINITIES。threadAffinityCoreListnumber[]否是设置运行时的CPU绑核列表，设置绑核策略模式后使能，当绑核策略模式为mindSporeLite.ThreadAffinityMode.NO_AFFINITIES时，绑核列表为空。列表中的数字代表核的序号。默认值：[]。precisionModestring否是设置是否使能**Float16推理模式**，设置为'preferred_fp16'代表使能半精度推理，其余设置情况均为不支持，默认设置'enforce_fp32'表示不使能半精度推理。

**Float16推理模式**： Float16又称半精度，它使用16比特表示一个数。Float16推理模式表示推理的时候用半精度进行推理。

**示例：**

```ets
let context: mindSporeLite.Context = {};
context.cpu = {};
context.target = ['cpu'];
context.cpu.threadNum = 2;
context.cpu.threadAffinityMode = 0;
context.cpu.precisionMode = 'preferred_fp16';
context.cpu.threadAffinityCoreList = [0, 1, 2];
```

#### ThreadAffinityMode

设置运行时的CPU绑核策略模式，有效值为0-2，0为默认不绑核，1为绑大核，2为绑中核。

**系统能力：** SystemCapability.AI.MindSporeLite

名称值说明NO_AFFINITIES0不绑核。BIG_CORES_FIRST1绑大核优先。LITTLE_CORES_FIRST2绑中核优先。

#### NNRTDevice

Neural Network Runtime表示神经网络运行时，简称NNRt。作为中间桥梁，连通上层 AI 推理框架和底层加速芯片，实现 AI 模型的跨芯片推理计算。MindSpore Lite 可配置NNRt后端。

**系统能力：** SystemCapability.AI.MindSporeLite

名称类型只读可选说明deviceID12+bigint否是NNRt设备ID。默认值为0。performanceMode12+[PerformanceMode](#ZH-CN_TOPIC_0000002529286125__performancemode12)否是NNRt设备的工作性能模式。默认值为PERFORMANCE_NONE。priority12+[Priority](#ZH-CN_TOPIC_0000002529286125__priority12)否是NNRt推理任务优先级。默认值为PRIORITY_MEDIUM。extensions12+[Extension](#ZH-CN_TOPIC_0000002529286125__extension12)[]否是NNRt设备的扩展配置。默认为空。

#### PerformanceMode12+

NNRt设备的工作性能模式枚举。

**系统能力：** SystemCapability.AI.MindSporeLite

名称值说明PERFORMANCE_NONE0无特殊设置。PERFORMANCE_LOW1低功耗模式。PERFORMANCE_MEDIUM2功耗-性能均衡模式。PERFORMANCE_HIGH3高性能模式。PERFORMANCE_EXTREME4极致性能模式。

#### Priority12+

NNRt推理任务优先级枚举。

**系统能力：** SystemCapability.AI.MindSporeLite

名称值说明PRIORITY_NONE0无优先级偏好。PRIORITY_LOW1低优先级任务。PRIORITY_MEDIUM2中优先级任务。PRIORITY_HIGH3高优先级任务。

#### Extension12+

定义NNRt设备的扩展信息。

**系统能力：** SystemCapability.AI.MindSporeLite

名称类型只读可选说明name12+string否否扩展名称。value12+ArrayBuffer否否包含扩展的内存。

#### NNRTDeviceDescription12+

NNRt设备信息描述，包含设备ID，设备名称等信息。

**系统能力：** SystemCapability.AI.MindSporeLite

#### deviceID12+

deviceID() : bigint

获取NNRt设备ID。

**系统能力：** SystemCapability.AI.MindSporeLite

**返回值：**

类型说明bigintNNRt设备ID。

**示例：**

```ets
let context: mindSporeLite.Context = {};
context.target = ["nnrt"];
context.nnrt = {};
let allDevices = mindSporeLite.getAllNNRTDeviceDescriptions();
if (allDevices == null) {
  console.error('getAllNNRTDeviceDescriptions is NULL.');
} else {
  for (let i: number = 0; i < allDevices.length; i++) {
    console.info(allDevices[i].deviceID().toString());
  }
}
```

#### deviceType12+

deviceType() : NNRTDeviceType

获取NNRt设备类型。

**系统能力：** SystemCapability.AI.MindSporeLite

**返回值：**

类型说明[NNRTDeviceType](#ZH-CN_TOPIC_0000002529286125__nnrtdevicetype12)NNRt设备类型。

**示例：**

```ets
let context: mindSporeLite.Context = {};
context.target = ["nnrt"];
context.nnrt = {};
let allDevices = mindSporeLite.getAllNNRTDeviceDescriptions();
if (allDevices == null) {
  console.error('getAllNNRTDeviceDescriptions is NULL.');
} else {
  for (let i: number = 0; i < allDevices.length; i++) {
    console.info(allDevices[i].deviceType().toString());
  }
}
```

#### deviceName12+

deviceName() : string

获取NNRt设备名称。

**系统能力：** SystemCapability.AI.MindSporeLite

**返回值：**

类型说明stringNNRt设备名称。

**示例：**

```ets
let context: mindSporeLite.Context = {};
context.target = ["nnrt"];
context.nnrt = {};
let allDevices = mindSporeLite.getAllNNRTDeviceDescriptions();
if (allDevices == null) {
  console.error('getAllNNRTDeviceDescriptions is NULL.');
} else {
  for (let i: number = 0; i < allDevices.length; i++) {
    console.info(allDevices[i].deviceName().toString());
  }
}
```

#### NNRTDeviceType12+

NNRt设备类型枚举。

**系统能力：** SystemCapability.AI.MindSporeLite

名称值说明NNRTDEVICE_OTHERS0设备类型不属于以下3种，则属于其它。NNRTDEVICE_CPU1CPU设备。NNRTDEVICE_GPU2GPU设备。NNRTDEVICE_ACCELERATOR3特定的加速设备。

#### TrainCfg12+

端侧训练相关参数的配置文件。

**系统能力：** SystemCapability.AI.MindSporeLite

名称类型只读可选说明lossName12+string[]否是损失函数的名称列表。默认值为["loss_fct", "_loss_fn", "SigmoidCrossEntropy"]。optimizationLevel12+[OptimizationLevel](#ZH-CN_TOPIC_0000002529286125__optimizationlevel12)否是端侧训练的网络优化等级。默认值为O0。

**示例：**

```ets
let cfg: mindSporeLite.TrainCfg = {};
cfg.lossName = ["loss_fct", "_loss_fn", "SigmoidCrossEntropy"];
cfg.optimizationLevel = mindSporeLite.OptimizationLevel.O0;
```

#### OptimizationLevel12+

端侧训练的网络优化等级枚举。

**系统能力：** SystemCapability.AI.MindSporeLite

名称值说明O00无优化等级。O22将网络转换为float16，保持批量归一化层和损失函数为float32。O33将网络转换为float16，包括批量归一化层。AUTO4根据设备选择优化等级。

#### QuantizationType12+

量化类型信息，有效值为0-2。

**系统能力：** SystemCapability.AI.MindSporeLite

名称值说明NO_QUANT0不做量化。WEIGHT_QUANT1权重量化。FULL_QUANT2全量化。

#### Model

模型实例。描述Model对象的属性和方法。

下例API示例中都需先使用[loadModelFromFile()](#ZH-CN_TOPIC_0000002529286125__mindsporeliteloadmodelfromfile)、[loadModelFromBuffer()](#ZH-CN_TOPIC_0000002529286125__mindsporeliteloadmodelfrombuffer)、[loadModelFromFd()](#ZH-CN_TOPIC_0000002529286125__mindsporeliteloadmodelfromfd)中的任一方法获取到Model实例，再通过此实例调用对应方法。

#### 属性

**系统能力：** SystemCapability.AI.MindSporeLite

名称类型只读可选说明learningRate12+number否是训练模型的学习率。默认值从加载的模型中读取。trainMode12+boolean否是模型是否为训练模式。true表示训练模式，false表示非训练模式。如果是训练模型，trainMode默认是true；如果是推理模型，trainMode默认是false。

#### getInputs

getInputs(): MSTensor[]

获取模型的输入用于推理。

**系统能力：** SystemCapability.AI.MindSporeLite

**返回值：**

类型说明[MSTensor](#ZH-CN_TOPIC_0000002529286125__mstensor)[]返回MSTensor对象。

**示例：**

```ets
let modelFile = '/path/to/xxx.ms';
mindSporeLite.loadModelFromFile(modelFile).then((mindSporeLiteModel : mindSporeLite.Model) => {
  let modelInputs : mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS_LITE_ERR: getInputs failed.')
  } else {
    console.info(modelInputs[0].name);
  }
})
```

#### predict

predict(inputs: MSTensor[], callback: Callback<MSTensor[]>): void

执行推理模型。使用callback异步回调。需要确保调用时模型对象不被资源回收。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

参数名类型必填说明inputs[MSTensor](#ZH-CN_TOPIC_0000002529286125__mstensor)[]是模型的输入列表。MSTensor对象。callbackCallback<[MSTensor](#ZH-CN_TOPIC_0000002529286125__mstensor)[]>是回调函数。返回MSTensor对象。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let inputName = 'input_data.bin';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext().resourceManager.getRawFileContent(inputName).then(async (buffer : Uint8Array) => {
  let inputBuffer = buffer.buffer;
  let modelFile : string = '/path/to/xxx.ms';
  let mindSporeLiteModel : mindSporeLite.Model = await mindSporeLite.loadModelFromFile(modelFile);
  let modelInputs : mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();

  modelInputs[0].setData(inputBuffer);
  mindSporeLiteModel.predict(modelInputs, (mindSporeLiteTensor : mindSporeLite.MSTensor[]) => {
    let output = new Float32Array(mindSporeLiteTensor[0].getData());
    for (let i = 0; i < output.length; i++) {
      console.info('MS_LITE_LOG: ' + output[i].toString());
    }
  })
}).catch((error: BusinessError) => {
  console.error("getRawFileContent promise error is " + error);
});
```

#### predict

predict(inputs: MSTensor[]): Promise<MSTensor[]>

执行推理模型，返回推理结果。使用Promise异步回调。需要确保调用时模型对象不被资源回收。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

参数名类型必填说明inputs[MSTensor](#ZH-CN_TOPIC_0000002529286125__mstensor)[]是模型的输入列表。MSTensor对象。

**返回值：**

类型说明Promise<[MSTensor](#ZH-CN_TOPIC_0000002529286125__mstensor)[]>Promise对象。返回MSTensor对象列表。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let inputName = 'input_data.bin';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext().resourceManager.getRawFileContent(inputName).then(async (buffer : Uint8Array) => {
  let inputBuffer = buffer.buffer;
  let modelFile = '/path/to/xxx.ms';
  let mindSporeLiteModel : mindSporeLite.Model = await mindSporeLite.loadModelFromFile(modelFile);
  let modelInputs : mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  modelInputs[0].setData(inputBuffer);
  mindSporeLiteModel.predict(modelInputs).then((mindSporeLiteTensor : mindSporeLite.MSTensor[]) => {
    let output = new Float32Array(mindSporeLiteTensor[0].getData());
    for (let i = 0; i < output.length; i++) {
      console.info(output[i].toString());
    }
  })
}).catch((error: BusinessError) => {
  console.error("getRawFileContent promise error is " + error);
});
```

#### resize

resize(inputs: MSTensor[], dims: Array<Array<number>>): boolean

重新设置张量大小。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

参数名类型必填说明inputs[MSTensor](#ZH-CN_TOPIC_0000002529286125__mstensor)[]是模型的输入列表。dimsArray<Array<number>>是需要修改的目标张量大小。

**返回值：**

类型说明boolean返回是否设置成功的结果。true表示重新设置张量大小成功；false表示重新设置张量大小失败。

**示例：**

```ets
let modelFile = '/path/to/xxx.ms';
mindSporeLite.loadModelFromFile(modelFile).then((mindSporeLiteModel : mindSporeLite.Model) => {
  let modelInputs : mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  let new_dim = new Array([1,32,32,1]);
  mindSporeLiteModel.resize(modelInputs, new_dim);
})
```

#### runStep12+

runStep(inputs: MSTensor[]): boolean

单步训练模型，仅用于端侧训练。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

参数名类型必填说明inputs[MSTensor](#ZH-CN_TOPIC_0000002529286125__mstensor)[]是模型的输入列表。

**返回值：**

类型说明boolean返回单步训练模型是否成功的结果。true表示单步训练模型成功，false表示单步训练模型失败。

**示例：**

```ets
let modelFile = '/path/to/xxx.ms';
mindSporeLite.loadTrainModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
  mindSporeLiteModel.trainMode = true;
  const modelInputs = mindSporeLiteModel.getInputs();
  let ret = mindSporeLiteModel.runStep(modelInputs);
  if (ret == false) {
    console.error('MS_LITE_LOG: runStep failed.')
  }
})
```

#### getWeights12+

getWeights(): MSTensor[]

获取模型的所有权重，仅用于端侧训练。

**系统能力：** SystemCapability.AI.MindSporeLite

**返回值：**

类型说明[MSTensor](#ZH-CN_TOPIC_0000002529286125__mstensor)[]返回模型的权重张量。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let modelFile = 'xxx.ms';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext().resourceManager.getRawFileContent(modelFile).then((modelBuffer : Uint8Array) => {
  mindSporeLite.loadTrainModelFromBuffer(modelBuffer.buffer.slice(0)).then((mindSporeLiteModel: mindSporeLite.Model) => {
    mindSporeLiteModel.trainMode = true;
    const weights = mindSporeLiteModel.getWeights();
    for (let i = 0; i < weights.length; i++) {
      let printStr = weights[i].name + ", ";
      printStr += weights[i].shape + ", ";
      printStr += weights[i].dtype + ", ";
      printStr += weights[i].dataSize + ", ";
      printStr += weights[i].getData();
      console.info("MS_LITE weights: ", printStr);
    }
  })
}).catch((error: BusinessError) => {
  console.error("getRawFileContent promise error is " + error);
});
```

#### updateWeights12+

updateWeights(weights: MSTensor[]): boolean

更新模型的权重，仅用于端侧训练。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

参数名类型必填说明weights[MSTensor](#ZH-CN_TOPIC_0000002529286125__mstensor)[]是权重张量列表。

**返回值：**

类型说明boolean返回是否更新权重成功的结果。true表示更新权重成功，false表示更新权重失败。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let modelFile = 'xxx.ms';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext().resourceManager.getRawFileContent(modelFile).then((modelBuffer : Uint8Array) => {
  mindSporeLite.loadTrainModelFromBuffer(modelBuffer.buffer.slice(0)).then((mindSporeLiteModel: mindSporeLite.Model) => {
    mindSporeLiteModel.trainMode = true;
    const weights = mindSporeLiteModel.getWeights();
    let ret = mindSporeLiteModel.updateWeights(weights);
    if (ret == false) {
      console.error('MS_LITE_LOG: updateWeights failed.')
    }
  })
}).catch((error: BusinessError) => {
  console.error("getRawFileContent promise error is " + error);
});
```

#### setupVirtualBatch12+

setupVirtualBatch(virtualBatchMultiplier: number, lr: number, momentum: number): boolean

设置虚拟批次用于训练，仅用于端侧训练。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

参数名类型必填说明virtualBatchMultipliernumber是虚拟批次乘法器，当设置值小于1时，表示禁用虚拟batch。lrnumber是学习率。momentumnumber是动量。

**返回值：**

类型说明boolean返回是否设置虚拟批次成功的结果。true表示设置虚拟批次成功，false表示设置虚拟批次失败。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let modelFile = 'xxx.ms';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext().resourceManager.getRawFileContent(modelFile).then((modelBuffer : Uint8Array) => {
  mindSporeLite.loadTrainModelFromBuffer(modelBuffer.buffer.slice(0)).then((mindSporeLiteModel: mindSporeLite.Model) => {
    mindSporeLiteModel.trainMode = true;
    let ret = mindSporeLiteModel.setupVirtualBatch(2,-1,-1);
    if (ret == false) {
      console.error('MS_LITE setupVirtualBatch failed.')
    }
  })
}).catch((error: BusinessError) => {
  console.error("getRawFileContent promise error is " + error);
});
```

#### exportModel12+

exportModel(modelFile: string, quantizationType?: QuantizationType, exportInferenceOnly?: boolean, outputTensorName?: string[]): boolean

导出训练模型，仅用于端侧训练。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

参数名类型必填说明modelFilestring是导出模型的文件路径。字符串长度限制跟随文件系统。quantizationType[QuantizationType](#ZH-CN_TOPIC_0000002529286125__quantizationtype12)否量化类型，默认为NO_QUANT。exportInferenceOnlyboolean否是否只导出推理模型。true表示只导出推理模型，false表示导出训练和推理两个模型。默认为true。outputTensorNamestring[]否设置导出模型的输出张量的名称。默认为空字符串数组，表示全量导出。

**返回值：**

类型说明boolean返回是否导出训练模型成功的结果。true表示导出训练模型成功，false表示导出训练模型失败。

**示例：**

```ets
let modelFile = '/path/to/xxx.ms';
let newPath = '/newpath/to';
mindSporeLite.loadTrainModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
  mindSporeLiteModel.trainMode = true;
  let ret = mindSporeLiteModel.exportModel(newPath + "/new_model.ms", mindSporeLite.QuantizationType.NO_QUANT, true);
  if (ret == false) {
    console.error('MS_LITE exportModel failed.')
  }
})
```

#### exportWeightsCollaborateWithMicro12+

exportWeightsCollaborateWithMicro(weightFile: string, isInference?: boolean, enableFp16?: boolean, changeableWeightsName?: string[]): boolean

导出供**micro推理**使用的模型权重，仅用于端侧训练。

**micro推理**：MindSpore Lite针对MCUs（MicroControllerUnits）部署硬件后端，提供了一种超轻量Micro AI部署解决方案，离线阶段直接将模型生成轻量化代码，不再需要在线解析模型和图编译。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

参数名类型必填说明weightFilestring是权重文件路径。字符串长度限制跟随文件系统。isInferenceboolean否是否从推理模型中导出权重。true表示从推理模型中导出权重，目前只支持true，默认为true。enableFp16boolean否浮点权重是否以float16格式保存。true表示以float16格式保存，false表示不以float16格式保存。默认为false。changeableWeightsNamestring[]否设置可变权重的名称。默认为空字符串数组。

**返回值：**

类型说明boolean返回是否导出供micro推理使用的模型权重成功的结果。true表示导出供micro推理使用的模型权重成功，false表示导出供micro推理使用的模型权重失败。

**示例：**

```ets
let modelFile = '/path/to/xxx.ms';
let microWeight = '/path/to/xxx.bin';
mindSporeLite.loadTrainModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
  let ret = mindSporeLiteModel.exportWeightsCollaborateWithMicro(microWeight);
  if (ret == false) {
    console.error('MSLITE exportWeightsCollaborateWithMicro failed.')
  }
})
```

#### MSTensor

模型张量实例。描述MSTensor对象的属性和方法。它与数组和矩阵非常相似，是MindSpore Lite网络运算中的基本数据结构。

下例API示例中都需先使用[getInputs()](#ZH-CN_TOPIC_0000002529286125__getinputs)获取到MSTensor实例，再通过此实例调用对应方法。

#### 属性

**系统能力：** SystemCapability.AI.MindSporeLite

名称类型只读可选说明namestring否否张量的名称。shapenumber[]否否张量的维度数组。elementNumnumber否否张量的维度数组的长度。dataSizenumber否否张量的数据的长度。dtype[DataType](#ZH-CN_TOPIC_0000002529286125__datatype)否否张量的数据类型。format[Format](#ZH-CN_TOPIC_0000002529286125__format)否否张量的数据排布方式。

**示例：**

```ets
let modelFile = '/path/to/xxx.ms';
mindSporeLite.loadModelFromFile(modelFile).then((mindSporeLiteModel : mindSporeLite.Model) => {
  let modelInputs : mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  console.info(modelInputs[0].name);
  console.info(modelInputs[0].shape.toString());
  console.info(modelInputs[0].elementNum.toString());
  console.info(modelInputs[0].dtype.toString());
  console.info(modelInputs[0].format.toString());
  console.info(modelInputs[0].dataSize.toString());
})
```

#### getData

getData(): ArrayBuffer

获取张量的数据。

**系统能力：** SystemCapability.AI.MindSporeLite

**返回值：**

类型说明ArrayBuffer返回张量的数据指针。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let inputName = 'input_data.bin';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext().resourceManager.getRawFileContent(inputName).then(async (buffer : Uint8Array) => {
  let inputBuffer = buffer.buffer;
  let modelFile = '/path/to/xxx.ms';
  let mindSporeLiteModel : mindSporeLite.Model = await mindSporeLite.loadModelFromFile(modelFile);
  let modelInputs : mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  modelInputs[0].setData(inputBuffer);
  mindSporeLiteModel.predict(modelInputs).then((mindSporeLiteTensor : mindSporeLite.MSTensor[]) => {
    let output = new Float32Array(mindSporeLiteTensor[0].getData());
    for (let i = 0; i < output.length; i++) {
      console.info(output[i].toString());
    }
  })
}).catch((error: BusinessError) => {
  console.error("getRawFileContent promise error is " + error);
});
```

#### setData

setData(inputArray: ArrayBuffer): void

设置张量的数据。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

参数名类型必填说明inputArrayArrayBuffer是张量的输入数据缓冲区。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let inputName = 'input_data.bin';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext().resourceManager.getRawFileContent(inputName).then(async (buffer : Uint8Array) => {
  let inputBuffer = buffer.buffer;
  let modelFile = '/path/to/xxx.ms';
  let mindSporeLiteModel : mindSporeLite.Model = await mindSporeLite.loadModelFromFile(modelFile);
  let modelInputs : mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  modelInputs[0].setData(inputBuffer);
}).catch((error: BusinessError) => {
  console.error("getRawFileContent promise error is " + error);
});
```

#### DataType

张量的数据类型。

**系统能力：** SystemCapability.AI.MindSporeLite

名称值说明TYPE_UNKNOWN0未知类型。NUMBER_TYPE_INT832保持Int8的类型。NUMBER_TYPE_INT1633保持Int16的类型。NUMBER_TYPE_INT3234保持Int32的类型。NUMBER_TYPE_INT6435保持Int64的类型。NUMBER_TYPE_UINT837保持UInt8的类型。NUMBER_TYPE_UINT1638保持UInt16的类型。NUMBER_TYPE_UINT3239保持UInt32的类型。NUMBER_TYPE_UINT6440保持UInt64的类型。NUMBER_TYPE_FLOAT1642保持Float16的类型。NUMBER_TYPE_FLOAT3243保持Float32的类型。NUMBER_TYPE_FLOAT6444保持Float64的类型。

#### Format

张量的数据排布方式。

**系统能力：** SystemCapability.AI.MindSporeLite

名称值说明DEFAULT_FORMAT-1未知数据排布方式。NCHW0数据排布方式为NCHW。NHWC1数据排布方式为NHWC。NHWC42数据排布方式为NHWC4。HWKC3数据排布方式为HWKC。HWCK4数据排布方式为HWCK。KCHW5数据排布方式为KCHW。