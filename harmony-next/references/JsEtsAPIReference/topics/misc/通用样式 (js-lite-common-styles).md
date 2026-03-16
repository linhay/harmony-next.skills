[]()[]()

# 通用样式

组件普遍支持的可以在style或css中设置组件外观样式。

名称类型默认值必填描述width<length> | <percentage>5+-否

设置组件自身的宽度。

未设置时组件宽度默认为0。

height<length> | <percentage>5+-否

设置组件自身的高度。

未设置时组件高度默认为0。

padding<length>0否

使用简写属性设置所有的内边距属性。

 该属性可以有1到4个值：

- 指定一个值时，该值指定四个边的内边距。

- 指定两个值时，第一个值指定上下两边的内边距，第二个指定左右两边的内边距。

- 指定三个值时，第一个指定上边的内边距，第二个指定左右两边的内边距，第三个指定下边的内边距。

- 指定四个值时分别为上、右、下、左边的内边距（顺时针顺序）。

padding-[left|top|right|bottom]<length>0否设置左、上、右、下内边距属性。margin<length> | <percentage>5+0否

使用简写属性设置所有的外边距属性，该属性可以有1到4个值。

- 只有一个值时，这个值会被指定给全部的四个边。

- 两个值时，第一个值被匹配给上和下，第二个值被匹配给左和右。

- 三个值时，第一个值被匹配给上, 第二个值被匹配给左和右，第三个值被匹配给下。

- 四个值时，会依次按上、右、下、左的顺序匹配 (即顺时针顺序)。

margin-[left|top|right|bottom]<length> | <percentage>5+0否设置左、上、右、下外边距属性。border-width<length>0否使用简写属性设置元素的所有边框宽度。border-color<color>black否使用简写属性设置元素的所有边框颜色。border-radius<length>-否border-radius属性是设置元素的外边框圆角半径。background-color<color>-否设置背景颜色。opacity5+number1否元素的透明度，取值范围为0到1，1表示为不透明，0表示为完全透明。displaystringflex否

确定一个元素所产生的框的类型，可选值为：

- flex：弹性布局。

- none：不渲染此元素。

[left|top]<length> | <percentage>6+-否

left|top确定元素的偏移位置。

- left属性规定元素的左边缘。该属性定义了定位元素左外边距边界与其包含块左边界之间的偏移。

- top属性规定元素的顶部边缘。该属性定义了一个定位元素的上外边距边界与其包含块上边界之间的偏移。

通用样式都不是必填项。

 目前，样式支持的颜色格式如下：

-

rgb(255, 255, 255)

-

rgba(255, 255, 255, 1.0)

-

HEX格式：#rrggbb，#aarrggbb

-

枚举格式：black，white等，详见 **表1** 当前支持的颜色枚举。Script脚本中不支持枚举格式。

**表1** 当前支持的颜色枚举

枚举名称对应颜色颜色aliceblue#f0f8ffantiquewhite#faebd7aqua#00ffffaquamarine#7fffd4azure#f0ffffbeige#f5f5dcbisque#ffe4c4black#000000blanchedalmond#ffebcdblue#0000ffblueviolet#8a2be2brown#a52a2aburlywood#deB887cadetblue#5f9ea0chartreuse#7fff00chocolate#d2691ecoral#ff7f50cornflowerblue#6495edcornsilk#fff8dccrimson#dc143ccyan#00ffffdarkblue#00008bdarkcyan#008b8bdarkgoldenrod#b8860bdarkgray#a9a9a9darkgreen#006400darkgrey#a9a9a9darkkhaki#bdb76bdarkmagenta#8b008bdarkolivegreen#556b2fdarkorange#ff8c00darkorchid#9932ccdarkred#8b0000darksalmon#e9967adarkseagreen#8fbc8fdarkslateblue#483d8bdarkslategray#2f4f4fdarkslategrey#2f4f4fdarkturquoise#00ced1darkviolet#9400d3deeppink#ff1493deepskyblue#00bfffdimgray#696969dimgrey#696969dodgerblue#1e90fffirebrick#b22222floralwhite#fffaf0forestgreen#228b22fuchsia#ff00ffgainsboro#dcdcdcghostwhite#f8f8ffgold#ffd700goldenrod#daa520gray#808080green#008000greenyellow#adff2fgrey#808080honeydew#f0fff0hotpink#ff69b4indianred#cd5c5cindigo#4b0082ivory#fffff0khaki#f0e68clavender#e6e6falavenderblush#fff0f5lawngreen#7cfc00lemonchiffon#fffacdlightblue#add8e6lightcoral#f08080lightcyan#e0fffflightgoldenrodyellow#fafad2lightgray#d3d3d3lightgreen#90ee90lightpink#ffb6c1lightsalmon#ffa07alightseagreen#20b2aalightskyblue#87cefalightslategray#778899lightslategrey#778899lightsteelblue#b0c4delightyellow#ffffe0lime#00ff00limegreen#32cd32linen#faf0e6magenta#ff00ffmaroon#800000mediumaquamarine#66cdaamediumblue#0000cdmediumorchid#ba55d3mediumpurple#9370dbmediumseagreen#3cb371mediumslateblue#7b68eemediumspringgreen#00fa9amediumturquoise#48d1ccmediumvioletred#c71585midnightblue#191970mintcream#f5fffamistyrose#ffe4e1moccasin#ffe4b5navajowhite#ffdeadnavy#000080oldlace#fdf5e6olive#808000olivedrab#6b8e23orange#ffa500orangered#ff4500orchid#da70d6palegoldenrod#eee8aapalegreen#98fb98paleturquoise#afeeeepalevioletred#db7093papayawhip#ffefd5peachpuff#ffdab9peru#cd853fpink#ffc0cbplum#dda0ddpowderblue#b0e0e6purple#800080rebeccapurple#663399red#ff0000rosybrown#bc8f8froyalblue#4169e1saddlebrown#8b4513salmon#fa8072sandybrown#f4a460seagreen#2e8b57seashell#fff5eesienna#a0522dsilver#c0c0c0skyblue#87ceebslateblue#6a5acdslategray#708090slategrey#708090snow#fffafaspringgreen#00ff7fsteelblue#4682b4tan#d2b48cteal#008080thistle#d8Bfd8tomato#ff6347turquoise#40e0d0violet#ee82eewheat#f5deb3white#ffffffwhitesmoke#f5f5f5yellow#ffff00yellowgreen#9acd32