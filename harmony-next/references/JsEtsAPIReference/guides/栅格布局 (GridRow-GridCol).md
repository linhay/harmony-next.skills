# 栅格布局 (GridRow/GridCol)

本文根据华为开发者官网 `arkts-layout-development-grid-layout` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-grid-layout>
更新时间：2026-04-30 02:41:24

## 概述
栅格布局是一种通用的辅助定位工具，对移动设备的界面设计有较好的借鉴作用。主要优势包括：
提供可循的规律：栅格布局可以为布局提供规律性的结构，解决多尺寸多设备的动态布局问题。通过将页面划分为等宽的列数和行数，可以方便地对页面元素进行定位和排版。
统一的定位标注：栅格布局可以为系统提供一种统一的定位标注，保证不同设备上各个模块的布局一致性。这可以减少设计和开发的复杂度，提高工作效率。
灵活的间距调整方法：栅格布局可以提供一种灵活的间距调整方法，满足特殊场景布局调整的需求。通过调整列与列之间和行与行之间的间距，可以控制整个页面的排版效果。
自动换行和自适应：栅格布局可以完成一对多布局的自动换行和自适应。当页面元素的数量超出了一行或一列的容量时，他们会自动换到下一行或下一列，并且在不同的设备上自适应排版，使得页面布局更加灵活和适应性强。
GridRow为栅格容器组件，需与栅格子组件GridCol在栅格布局场景中联合使用。

## 栅格容器GridRow

## 栅格容器断点
栅格容器以设备的水平宽度（像素单位，单位vp）作为断点依据，定义设备的宽度类型，形成了一套断点规则。开发者可根据需求在不同的断点区间实现不同的页面布局效果。
栅格容器默认断点将设备宽度分为xs、sm、md、lg四类，尺寸范围如下：
断点名称
取值范围（vp）
设备描述
xs
[0, 320）
最小宽度类型设备。
sm
[320, 600)
小宽度类型设备。
md

## 布局的总列数
GridRow中通过columns设置栅格布局的总列数。
API version 20之前，columns默认值为12，即在未设置columns时，任何断点下，栅格布局均被分成12列。
API version 20及以后，columns默认值为{ xs: 2, sm: 4, md: 8, lg: 12, xl: 12, xxl: 12 }。
// xxx.ets @Entry @Component struct GridColumnsWithDefaults { @State bgColors: ResourceColor[] = ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)', 'rgb(255,192,0)', 'rgb(170,10,33)', 'rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)']; build() { GridRow() { ForEach(this.bgColors, (item: ResourceColor, index?: number | undefined) => { GridCol({ span: 1 }) { Row() { Text(`${index}`) }.width('100%').height('50') }.backgroundColor(item) }) } } }
API version 20之前布局显示：
API version 20及以后布局显示（以sm设备为例，默认栅格列数为4）：
columns支持number和GridRowColumnOption两种类型, 可按两种方式设置栅格布局的总列数。
当columns类型为number时，栅格布局在任何尺寸设备下都被分为同一列数。下面分别设置栅格布局列数为4和8，子元素占一列，效果如下：
// xxx.ets @Entry @Component struct FixedFourColumnGrid { @State bgColors: ResourceColor[] = ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)', 'rgb(255,192,0)', 'rgb(170,10,33)']; build() { Column({ space: 6 }) { Text('columns：4').alignSelf(ItemAlign.Start) Row() { GridRow({ columns: 4 }) { ForEach(this.bgColors, (item: ResourceColor, index?: number | undefined) => { GridCol({ span: 1 }) { Row() { Text(`${index}`) }.width('100%').height('50') }.backgroundColor(item) }) } .width('100%').height('100%') } .height(160) .border({ color: 'rgb(39,135,217)', width: 2 }) .width('90%') } } }
// xxx.ets @Entry @Component struct FixedEightColumnGrid { @State bgColors: ResourceColor[] = ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)', 'rgb(255,192,0)', 'rgb(170,10,33)']; build() { Column({ space: 6 }) { Text('columns：8').alignSelf(ItemAlign.Start) Row() { GridRow({ columns: 8 }) { ForEach(this.bgColors, (item: ResourceColor, index?: number | undefined) => { GridCol({ span: 1 }) { Row() { Text(`${index}`) }.width('100%').height('50') }.backgroundColor(item) }) } .width('100%').height('100%') } .height(160) .border({ color: 'rgb(39,135,217)', width: 2 }) .width('90%') } } }
当columns类型为GridRowColumnOption时，支持下面6种不同尺寸（xs，sm，md，lg，xl，xxl）设备的栅格列数设置，不同尺寸的设备支持配置不同的栅格列数。
@Entry @Component struct GridRowColumnOptionLayout { @State bgColors: ResourceColor[] = ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)', 'rgb(255,192,0)', 'rgb(170,10,33)']; build() { GridRow({ columns: { sm: 4, md: 8 }, breakpoints: { value: ['320vp', '600vp', '840vp', '1440vp', '1600vp'] // 表示在保留默认断点['320vp', '600vp', '840vp']的同时自定义增加'1440vp', '1600vp'的断点，实际开发中需要根据实际使用场景，合理设置断点值实现一次开发多端适配。 } }) { ForEach(this.bgColors, (item: ResourceColor, index?: number | undefined) => { GridCol({ span: 1 }) { Row() { Text(`${index}`) }.width('100%').height('50') }.backgroundColor(item) }) } .height(200) .border({ color: 'rgb(39,135,217)', width: 2 }) } }

## 排列方向
栅格布局中，可以通过设置GridRow的direction属性来指定栅格子组件在栅格容器中的排列方向。该属性可以设置为GridRowDirection.Row（从左往右排列）或GridRowDirection.RowReverse（从右往左排列），以满足不同的布局需求。通过合理的direction属性设置，可以使得页面布局更加灵活和符合设计要求。
子组件默认从左往右排列。
GridRow({ direction: GridRowDirection.Row }) { /* ... */ }
子组件从右往左排列。
GridRow({ direction: GridRowDirection.RowReverse }) { /* ... */ }

## 子组件间距
GridRow中通过gutter属性设置子元素在水平和垂直方向的间距。
当gutter类型为number时，同时设置栅格子组件间水平和垂直方向边距且相等。下例中，设置子组件水平与垂直方向距离相邻元素的间距为10。
GridRow({ gutter: 10 }) { /* ... */ }
当gutter类型为GutterOption时，单独设置栅格子组件水平垂直边距，x属性为水平方向间距，y为垂直方向间距。
GridRow({ gutter: { x: 20, y: 50 } }) { /* ... */ }

## 子组件GridCol
GridCol组件作为GridRow组件的子组件，通过给GridCol传参或者设置属性两种方式，设置span（占用列数），offset（偏移列数），order（元素序号）的值。
设置span。
let gSpan:Record<string,number> = { 'xs': 1, 'sm': 2, 'md': 3, 'lg': 4 }
GridCol({ span: 2 }){} GridCol({ span: { xs: 1, sm: 2, md: 3, lg: 4 } }){} GridCol(){}.span(2) GridCol(){}.span(gSpan)
设置offset。
let gOffset:Record<string,number> = { 'xs': 1, 'sm': 2, 'md': 3, 'lg': 4 }
GridCol({ offset: 2, span: 1 }){} GridCol({ offset: { xs: 2, sm: 2, md: 2, lg: 2 }, span: 1 }){} GridCol({ span: 1 }){}.offset(gOffset)
设置order。
let gOrder:Record<string,number> = { 'xs': 1, 'sm': 2, 'md': 3, 'lg': 4 }
GridCol({ order: 2, span: 1 }){} GridCol({ order: { xs: 1, sm: 2, md: 3, lg: 4 }, span: 1 }){} GridCol({ span: 1 }){}.order(2) GridCol({ span: 1 }){}.order(gOrder)

## span
子组件占栅格布局的列数，决定了子组件的宽度。默认值为1。
span支持number和GridColColumnOption两种类型, 可按两种方式设置栅格子组件占栅格容器的列数。
当span类型为number时，子组件在所有尺寸设备下占用的列数相同。
// xxx.ets @Entry @Component struct SpanNumberExample { @State bgColors: ResourceColor[] = ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)', 'rgb(255,192,0)', 'rgb(170,10,33)']; build() { GridRow({ columns: 8 }) { ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => { GridCol({ span: 2 }) { Row() { Text(`${index}`) }.width('100%').height('50vp') } .backgroundColor(color) }) } .border({ color: 'rgb(39,135,217)', width: 2 }) .height('150vp') } }
当span类型为GridColColumnOption时，支持6种不同尺寸（xs，sm，md，lg，xl，xxl）设备中子组件所占列数设置，不同尺寸的设备下子组件支持配置不同列数。若仅部分设置sm、md的列数，未配置的xs、lg、xl、xxl设备根据列数补全取默认值。
@Entry @Component struct SpanColumnOptionExample { @State currentBp: string = "unknown" @State bgColors: ResourceColor[] = ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)', 'rgb(255,192,0)', 'rgb(170,10,33)']; build() { Column({ space: 6 }) { GridRow({ columns: 8 }) { ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => { GridCol({ span: { xs: 1, sm: 2, md: 3, lg: 4 } }) { Row() { Text(`${index}`) }.width('100%').height('50vp') } .backgroundColor(color) }) } .border({ color: 'rgb(39,135,217)', width: 2 }) .height('150vp') .onBreakpointChange((breakPoint) => { this.currentBp = breakPoint }) Text(this.currentBp) } } }

## offset
栅格子组件相对于前一个子组件的偏移列数，默认为0。
当offset类型为number时，子组件偏移相同列数。
@Entry @Component struct OffsetNumberExample { @State bgColors: ResourceColor[] = ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)', 'rgb(255,192,0)', 'rgb(170,10,33)']; build() { Column() { GridRow({ columns: 12 }) { ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => { GridCol({ offset: 2, span: 1 }) { Row() { Text('' + index) }.width('100%').height('50vp') } .backgroundColor(color) }) } Blank().width('100%').height(150) }.border({ color: 'rgb(39,135,217)', width: 2 }) } }
在lg及以上尺寸的设备上，栅格分成12列，每一个子组件占1列，偏移2列，每个子组件及间距共占3列，1行放4个子组件。
当offset类型为GridColColumnOption时，支持6种不同尺寸（xs，sm，md，lg，xl，xxl）设备中子组件所占列数设置，各个尺寸下数值可不同。
@Entry @Component struct OffsetColumnOptionExample { @State currentBp: string = "unknown" @State bgColors: ResourceColor[] = ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)', 'rgb(255,192,0)', 'rgb(170,10,33)']; build() { Column({ space: 6 }) { GridRow({ columns: 12 }) { ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => { GridCol({ offset: { xs: 1, sm: 2, md: 3, lg: 4 }, span: 1 }) { Row() { Text('' + index) }.width('100%').height('50vp') } .backgroundColor(color) }) } .height(200) .border({ color: 'rgb(39,135,217)', width: 2 }) .onBreakpointChange((breakPoint) => { this.currentBp = breakPoint }) Text(this.currentBp) } } }
