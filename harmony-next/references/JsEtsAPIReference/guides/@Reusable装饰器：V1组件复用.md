# @Reusable装饰器：V1组件复用

本文根据华为开发者官网 `arkts-reusable` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-reusable>
更新时间：2026-04-30 02:41:24

## 概述
@Reusable用于装饰自定义组件，表示该自定义组件具有被复用的能力。
在开发复杂界面时，UI渲染效率是一个需要考虑的问题。例如在长列表快速滑动时，大量列表项的创建和销毁可能导致界面卡顿。组件复用是一种优化UI性能的重要方法。通过复用先前创建并且已经下树的组件对象，降低组件创建和销毁的频率，从而减小计算开销，提升UI渲染效率。
@Reusable装饰的自定义组件在从组件树中移除时，自定义组件（包含视图节点、组件实例和状态上下文）将被放入其父自定义组件的缓存池中。后续创建新自定义组件节点时，将优先复用缓存池中的节点，从而节约组件重新创建的时间。
@Reusable提供了aboutToRecycle和aboutToReuse两个生命周期，在组件被回收时调用aboutToRecycle，在组件被复用时调用aboutToReuse。开发者可以在这两个生命周期中实现组件回收、复用相关的业务逻辑。
@Reusable装饰的自定义组件下有子组件时，会在回收和复用时递归调用子组件的aboutToRecycle和aboutToReuse（与子组件是否被@Reusable标记无关），直到遍历完所有子组件。
组件复用前后应保持组件结构不变。针对组件结构存在差异的场景，可以使用reuseId来区分不同结构的复用组件。

## 限制条件

## 仅用于自定义组件
@Reusable装饰器仅用于自定义组件@Component，不可与@Builder搭配使用。
@Reusable不支持跟@ComponentV2搭配使用，@ComponentV2组件复用推荐@ReusableV2装饰器。
import { ComponentContent } from '@kit.ArkUI'; // @Builder不能与@Reusable搭配使用。 // @Reusable @Builder function buildCreativeLoadingDialog(closedClick: () => void) { Crash(); } @Component export struct Crash { build() { Column() { Text('Crash') .fontSize(12) .lineHeight(18) .fontColor(Color.Blue) .margin({ left: 6 }) }.width('100%') .height('100%') .justifyContent(FlexAlign.Center) } } @Entry @Component struct Index { @State message: string = 'Hello World'; private uiContext = this.getUIContext(); build() { RelativeContainer() { Text(this.message) .id('Index') .fontSize(50) .fontWeight(FontWeight.Bold) .alignRules({ center: { anchor: '__container__', align: VerticalAlign.Center }, middle: { anchor: '__container__', align: HorizontalAlign.Center } }) .onClick(() => { let contentNode = new ComponentContent(this.uiContext, wrapBuilder(buildCreativeLoadingDialog), () => { }); this.uiContext.getPromptAction().openCustomDialog(contentNode); }) } .height('100%') .width('100%') } }

## 状态变量更新限制
被@Reusable装饰的自定义组件在复用时，会递归调用该自定义组件及其所有子组件的aboutToReuse回调函数。若在子组件的aboutToReuse函数中修改了父组件的状态变量，此次修改将不会生效，请避免此类用法。若需设置父组件的状态变量，可使用setTimeout设置延迟执行，将任务移出组件复用的作用范围，使修改生效。
【反例】
在子组件的aboutToReuse中，直接修改父组件的状态变量。
class IncorrectBasicDataSource implements IDataSource { private listener: DataChangeListener | undefined = undefined; public dataArray: number[] = []; totalCount(): number { return this.dataArray.length; } getData(index: number): number { return this.dataArray[index]; } registerDataChangeListener(listener: DataChangeListener): void { this.listener = listener; } unregisterDataChangeListener(listener: DataChangeListener): void { this.listener = undefined; } } @Entry @Component struct IncorrectIndex { private data: IncorrectBasicDataSource = new IncorrectBasicDataSource(); aboutToAppear(): void { for (let index = 1; index < 20; index++) { this.data.dataArray.push(index); } } build() { List() { LazyForEach(this.data, (item: number, index: number) => { ListItem() { IncorrectReuseComponent({ num: item }); } }, (item: number, index: number) => index.toString()) }.cachedCount(0) } } @Reusable @Component struct IncorrectReuseComponent { @State num: number = 0; aboutToReuse(params: ESObject): void { this.num = params.num; } build() { Column() { Text('ReuseComponent num:' + this.num.toString()) IncorrectReuseComponentChild({ num: this.num }) Button('plus') .onClick(() => { this.num += 10; }) } .height(200) } } @Component struct IncorrectReuseComponentChild { @Link num: number; aboutToReuse(params: ESObject): void { this.num = -1 * params.num; } build() { Text('ReuseComponentChild num:' + this.num.toString()) } }
【正例】
在子组件的aboutToReuse中，使用setTimeout，将修改移出组件复用的作用范围。
class BasicDataSource implements IDataSource { private listener: DataChangeListener | undefined = undefined; public dataArray: number[] = []; totalCount(): number { return this.dataArray.length; } getData(index: number): number { return this.dataArray[index]; } registerDataChangeListener(listener: DataChangeListener): void { this.listener = listener; } unregisterDataChangeListener(listener: DataChangeListener): void { this.listener = undefined; } } @Entry @Component struct Index { private data: BasicDataSource = new BasicDataSource(); aboutToAppear(): void { for (let index = 1; index <= 20; index++) { // 循环20次 this.data.dataArray.push(index); } } build() { List() { LazyForEach(this.data, (item: number, index: number) => { ListItem() { ReuseComponent({ num: item }) } }, (item: number, index: number) => index.toString()) }.cachedCount(0) } } @Reusable @Component struct ReuseComponent { @State num: number = 0; aboutToReuse(params: ESObject): void { this.num = params.num; } build() { Column() { Text('ReuseComponent num:' + this.num.toString()) ReuseComponentChild({ num: this.num }) Button('plus') .onClick(() => { this.num += 10; // 每次点击增加10 }) } .height(200) } } @Component struct ReuseComponentChild { @Link num: number; aboutToReuse(params: ESObject): void { setTimeout(() => { this.num = -1 * params.num; }, 1) } build() { Text('ReuseComponentChild num:' + this.num.toString()); } }

## 组件结构需一致
被@Reusable装饰的自定义组件在复用前后，应保持组件的结构不变。否则，会在复用过程中创建或销毁子组件，降低复用效率和性能，甚至造成应用行为异常。
对于复用过程中创建的子组件，框架会在其创建后依次调用aboutToReuse方法和aboutToAppear方法。在调用aboutToReuse方法时，由于其aboutToAppear方法还未执行，且内部子组件还未创建，因此aboutToReuse方法中依赖aboutToAppear方法执行结果，或依赖内部子组件状态的相关操作会引起预期外的行为。在调用aboutToReuse方法后，框架会再调用aboutToAppear方法并初始化组件。
针对组件结构存在差异的场景，开发者需要通过设定不同的reuseId来进行区分，具体方式请参考多种条目类型使用场景。
【反例】
组件结构存在差异，但未通过reuseId进行区分。
以下示例中，先点击“show/hide branch A”按钮，组件被回收，再点击“show/hide branch B”按钮，组件被复用。子组件ReusableChildB在复用过程中被创建，aboutToReuse方法和aboutToAppear方法被依次调用。
import { hilog } from '@kit.PerformanceAnalysisKit'; const TAG = '[Sample_ReusableComponent]'; const DOMAIN = 0xF811; const BUNDLE = 'ReusableComponent_'; @Entry @Component struct Index { @State showBranchA: boolean = true; @State showBranchB: boolean = false; build() { Column({ space: 5 }) { Button('show/hide branch A') .onClick(() => { this.showBranchA = !this.showBranchA; }) if (this.showBranchA) { ReusableComponent({ flag: true }) } Button('show/hide branch B') .onClick(() => { this.showBranchB = !this.showBranchB; }) if (this.showBranchB) { ReusableComponent({ flag: false }) } } } } @Reusable @Component struct ReusableComponent { @Require @Prop flag: boolean = true; aboutToAppear() { hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableComponent aboutToAppear'); } aboutToReuse(params: ESObject) { hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableComponent aboutToReuse'); this.flag = params.flag; } build() { Column({ space: 5 }) { Text('ReusableComponent') if (this.flag) { ReusableChildA() } else { ReusableChildB() } }.border({ width: 1 }) } } @Component struct ReusableChildA { aboutToAppear() { hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableChildA aboutToAppear'); } aboutToReuse() { hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableChildA aboutToReuse'); } build() { Text('ReusableChildA') .border({ width: 1 }) } } @Component struct ReusableChildB { aboutToAppear() { hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableChildB aboutToAppear'); } aboutToReuse() { hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableChildB aboutToReuse'); } build() { Text('ReusableChildB') .border({ width: 1 }) } }
【正例】
组件结构存在差异，通过reuseId进行区分。
import { hilog } from '@kit.PerformanceAnalysisKit'; const TAG = '[Sample_ReusableComponent]'; const DOMAIN = 0xF811; const BUNDLE = 'ReusableComponent_'; @Entry @Component struct Index { @State showBranchA: boolean = true; @State showBranchB: boolean = false; build() { Column({ space: 5 }) { Button('show/hide branch A') .onClick(() => { this.showBranchA = !this.showBranchA; }) if (this.showBranchA) { ReusableComponent({ flag: true }) .reuseId('ReuseA') // 通过reuseId区分不同结构的复用组件 } Button('show/hide branch B') .onClick(() => { this.showBranchB = !this.showBranchB; }) if (this.showBranchB) { ReusableComponent({ flag: false }) .reuseId('ReuseB') // 通过reuseId区分不同结构的复用组件 } } } } @Reusable @Component struct ReusableComponent { @Require @Prop flag: boolean = true; aboutToAppear() { hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableComponent aboutToAppear'); } aboutToReuse(params: ESObject) { hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableComponent aboutToReuse'); this.flag = params.flag; } build() { Column({ space: 5 }) { Text('ReusableComponent') if (this.flag) { ReusableChildA() } else { ReusableChildB() } }.border({ width: 1 }) } } @Component struct ReusableChildA { aboutToAppear() { hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableChildA aboutToAppear'); } aboutToReuse() { hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableChildA aboutToReuse'); } build() { Text('ReusableChildA') .border({ width: 1 }) } } @Component struct ReusableChildB { aboutToAppear() { hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableChildB aboutToAppear'); } aboutToReuse() { hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableChildB aboutToReuse'); } build() { Text('ReusableChildB') .border({ width: 1 }) } }

## 不支持ComponentContent
ComponentContent不支持传入@Reusable装饰器装饰的自定义组件。
import { ComponentContent } from '@kit.ArkUI'; @Builder function buildCreativeLoadingDialog(closedClick: () => void) { Crash(); } // 如果注释掉就可以正常弹出弹窗，如果加上@Reusable就直接crash。 @Reusable @Component export struct Crash { build() { Column() { Text('Crash') .fontSize(12) .lineHeight(18) .fontColor(Color.Blue) .margin({ left: 6 }) }.width('100%') .height('100%') .justifyContent(FlexAlign.Center) } } @Entry @Component struct Index { @State message: string = 'Hello World'; private uiContext = this.getUIContext(); build() { RelativeContainer() { Text(this.message) .id('Index') .fontSize(50) .fontWeight(FontWeight.Bold) .alignRules({ center: { anchor: '__container__', align: VerticalAlign.Center }, middle: { anchor: '__container__', align: HorizontalAlign.Center } }) .onClick(() => { // ComponentContent底层是BuilderNode，BuilderNode不支持传入@Reusable注解的自定义组件。 let contentNode = new ComponentContent(this.uiContext, wrapBuilder(buildCreativeLoadingDialog), () => { }); this.uiContext.getPromptAction().openCustomDialog(contentNode); }) } .height('100%') .width('100%') } }

## 不建议嵌套使用
@Reusable装饰器不建议嵌套使用，会增加内存，降低复用效率，加大维护难度。嵌套使用会导致额外缓存池的生成，各缓存池拥有相同树状结构，复用效率低下。此外，嵌套使用会使生命周期管理复杂，资源和变量共享困难。

## 使用场景

## 动态布局更新
重复创建与移除视图可能引起频繁的布局计算，从而影响帧率。采用组件复用可以避免不必要的视图创建与布局计算，提升性能。
以下示例中，将Child自定义组件标记为复用组件，通过Button点击更新Child，触发复用。
// xxx.ets export class Message { public value: string | undefined; constructor(value: string) { this.value = value; } } @Entry @Component struct Index { @State switch: boolean = true; build() { Column() { Button('Hello') .fontSize(30) .fontWeight(FontWeight.Bold) .onClick(() => { this.switch = !this.switch; }) if (this.switch) { // 如果只有一个复用的组件，可以不用设置reuseId。 Child({ message: new Message('Child') }) .reuseId('Child'); } } .height('100%') .width('100%') } } @Reusable @Component struct Child { @State message: Message = new Message('AboutToReuse'); aboutToReuse(params: Record<string, ESObject>) { this.message = params.message as Message; } build() { Column() { Text(this.message.value) .fontSize(30) } .borderWidth(1) .height(100) } }
