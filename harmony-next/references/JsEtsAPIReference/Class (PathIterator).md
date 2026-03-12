# Class (PathIterator)

表示路径操作迭代器，可通过遍历迭代器读取path的操作指令。

-

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本Class首批接口从API version 18开始支持。

-

本模块使用屏幕物理像素单位px。

-

本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

#### 导入模块

```ets
import { drawing } from '@kit.ArkGraphics2D';
```

#### constructor18+

constructor(path: Path)

构造迭代器并绑定路径。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明path[Path](Class (Path).md)是迭代器绑定的路径对象。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
let iter: drawing.PathIterator = new drawing.PathIterator(path);
```

#### next18+

next(points: Array<common2D.Point>, offset?: number): PathIteratorVerb

返回当前路径的下一个操作，并将迭代器置于该操作。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明pointsArray<[common2D.Point](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__point12)>是坐标点数组，长度必须至少为偏移量加4，以确保能容纳所有类型的路径数据。操作执行后，该数组会被覆盖。填入的坐标点数量取决于操作类型，其中，MOVE填入1个坐标点，LINE填入2个坐标点，QUAD填入3个坐标点，CONIC填入3个坐标点 + 1个权重值（共3.5组），CUBIC填入4个坐标点，CLOSE和DONE不填入任何点。offsetnumber否数组中写入位置相对起始点的偏移量，默认为0，取值范围为[0, size-4]，size是指坐标点数组长度。

**返回值：**

类型说明[PathIteratorVerb](Enums.md#ZH-CN_TOPIC_0000002529285977__pathiteratorverb18)迭代器包含的路径操作类型。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(10, 20);
let iter: drawing.PathIterator = new drawing.PathIterator(path);
let verbStr: Array<string> = ["MOVE", "LINE", "QUAD", "CONIC", "CUBIC", "CLOSE", "DONE"];
let pointCount: Array<number> = [1,2,3,4,4,0,0]; //1,2,3,3.5,4,0,0
let points: Array<common2D.Point> = [{x: 0, y: 0}, {x: 0, y: 0}, {x: 0, y: 0}, {x: 0, y: 0}];
let offset = 0;
let verb = iter.next(points, offset);
let outputMessage: string = "pathIteratorNext: ";
outputMessage += "verb =" + verbStr[verb] + "; has " + pointCount[verb] + " pairs: ";
for (let j = 0; j < pointCount[verb] + offset; j++) {
  outputMessage += "[" + points[j].x + ", " + points[j].y + "]";
}
console.info(outputMessage);
```

#### peek18+

peek(): PathIteratorVerb

返回当前路径的下一个操作，迭代器保持在原操作。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明[PathIteratorVerb](Enums.md#ZH-CN_TOPIC_0000002529285977__pathiteratorverb18)迭代器包含的路径操作类型。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
let iter: drawing.PathIterator = new drawing.PathIterator(path);
let res = iter.peek();
```

#### hasNext18+

hasNext(): boolean

判断路径操作迭代器中是否还有下一个操作。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明boolean判断路径操作迭代器中是否还有下一个操作。true表示有，false表示没有。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
let iter: drawing.PathIterator = new drawing.PathIterator(path);
let res = iter.hasNext();
```