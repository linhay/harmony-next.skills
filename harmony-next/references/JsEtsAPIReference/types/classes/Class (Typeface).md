# Class (Typeface)

字体，如宋体、楷体等。

-

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本模块使用屏幕物理像素单位px。

-

本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

#### 导入模块

```ets
import { drawing } from '@kit.ArkGraphics2D';
```

#### getFamilyName

getFamilyName(): string

获取字体的族名，即一套字体设计的名称。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明string返回字体的族名。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

const font = new drawing.Font();
let typeface = font.getTypeface();
let familyName = typeface.getFamilyName();
```

#### makeFromCurrent20+

makeFromCurrent(typefaceArguments: TypefaceArguments): Typeface

基于当前字体结合字体属性构造新的字体对象。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明typefaceArguments[TypefaceArguments](Class (TypefaceArguments).md)是字体属性。

**返回值：**

类型说明[Typeface](Class (Typeface).md)返回字体对象（异常情况下会返回空指针）。

**示例：**

```ets
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class TextRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    const canvas = context.canvas;
    let typeArguments = new drawing.TypefaceArguments();
    typeArguments.addVariation("wght", 100);
    const myTypeFace = drawing.Typeface.makeFromFile("/system/fonts/HarmonyOS_Sans_SC.ttf");
    const typeFace1 = myTypeFace.makeFromCurrent(typeArguments);
    let font = new drawing.Font();
    font.setTypeface(typeFace1);
    const textBlob = drawing.TextBlob.makeFromString("Hello World", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
    canvas.drawTextBlob(textBlob, 60, 100);
  }
}
```

#### makeFromFile12+

static makeFromFile(filePath: string): Typeface

从指定字体文件构造字体。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明filePathstring是表示字体资源存放的路径。应用沙箱路径和真实物理路径的对应关系请参考[应用沙箱路径和真实物理路径的对应关系](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory#应用沙箱路径和真实物理路径的对应关系)。

**返回值：**

类型说明[Typeface](Class (Typeface).md)返回Typeface对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class TextRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    const canvas = context.canvas;
    let font = new drawing.Font();
    let str = "/system/fonts/HarmonyOS_Sans_Italic.ttf";
    const mytypeface = drawing.Typeface.makeFromFile(str);
    font.setTypeface(mytypeface);
    const textBlob = drawing.TextBlob.makeFromString("Hello World", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
    canvas.drawTextBlob(textBlob, 60, 100);
  }
}
```

#### makeFromRawFile18+

static makeFromRawFile(rawfile: Resource): Typeface

使用指定的字体文件构造字体，其中要求指定的字体文件需保存在应用资源文件夹的rawfile路径下。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rawfile[Resource](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)是指定字体文件对应的资源对象。当前只支持$rawfile格式引用的资源对象，对应格式写为$rawfile('filePath')，其中filePath为指定字体文件相对于工程中resources/rawfile目录的相对路径。如将字体文件直接存放在resources/rawfile目录下，则引用格式应写为：$rawfile('HarmonyOS_Sans_Bold.ttf')；也可以创建子目录，将字体文件存放在resources/rawfile/ttf下，则引用格式应写为：$rawfile('ttf/HarmonyOS_Sans_Bold.ttf')。

**返回值：**

类型说明[Typeface](Class (Typeface).md)返回Typeface对象（异常情况下会返回空指针）。

**示例：**

```ets
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class TextRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    const canvas = context.canvas;
    let font = new drawing.Font();
    const myTypeFace = drawing.Typeface.makeFromRawFile($rawfile('HarmonyOS_Sans_Bold.ttf'));
    font.setTypeface(myTypeFace);
    const textBlob = drawing.TextBlob.makeFromString("Hello World", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
    canvas.drawTextBlob(textBlob, 60, 100);
  }
}
```

#### makeFromFileWithArguments20+

static makeFromFileWithArguments(filePath: string, typefaceArguments: TypefaceArguments): Typeface

根据字体文件路径和字体属性构造新的字体。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明filePathstring是表示字体资源存放的路径。应用沙箱路径和真实物理路径的对应关系请参考[应用沙箱路径和真实物理路径的对应关系](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory#应用沙箱路径和真实物理路径的对应关系)。typefaceArguments[TypefaceArguments](Class (TypefaceArguments).md)是表示字体属性。

**返回值：**

类型说明[Typeface](Class (Typeface).md)返回字体对象（异常情况下会返回空指针）。

**示例：**

```ets
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class TextRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    const canvas = context.canvas;
    let font = new drawing.Font();
    let str = "/system/fonts/HarmonyOS_Sans_Italic.ttf";
    let typeFaceArgument = new drawing.TypefaceArguments();
    const myTypeFace = drawing.Typeface.makeFromFileWithArguments(str, typeFaceArgument);
    font.setTypeface(myTypeFace);
    const textBlob = drawing.TextBlob.makeFromString("Hello World", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
    canvas.drawTextBlob(textBlob, 60, 100);
  }
}
```

#### makeFromRawFileWithArguments20+

static makeFromRawFileWithArguments(rawfile: Resource, typefaceArguments: TypefaceArguments): Typeface

使用指定的字体文件和字体属性构造字体，其中要求指定的字体文件需保存在应用资源文件夹的rawfile路径下。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rawfile[Resource](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)是指定字体文件对应的资源对象。当前只支持$rawfile格式引用的资源对象，对应格式写为$rawfile('filePath')，其中filePath为指定字体文件相对于工程中resources/rawfile目录的相对路径。typefaceArguments[TypefaceArguments](Class (TypefaceArguments).md)是表示字体属性。

**返回值：**

类型说明[Typeface](Class (Typeface).md)返回字体对象（异常情况下会返回空指针）。

**示例：**

```ets
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class TextRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    const canvas = context.canvas;
    let font = new drawing.Font();
    let typeFaceArgument = new drawing.TypefaceArguments();
    const myTypeFace = drawing.Typeface.makeFromRawFileWithArguments($rawfile('HarmonyOS_Sans_Bold.ttf'), typeFaceArgument);
    font.setTypeface(myTypeFace);
    const textBlob = drawing.TextBlob.makeFromString("Hello World", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
    canvas.drawTextBlob(textBlob, 60, 100);
  }
}
```