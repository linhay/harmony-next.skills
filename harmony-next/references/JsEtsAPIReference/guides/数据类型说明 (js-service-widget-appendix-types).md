[]()[]()

# 数据类型说明

从API Version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

[]()[]()

#### 长度类型

名称类型定义描述lengthstring | number

用于描述尺寸单位，输入为number类型时，使用px单位。输入为string类型时，需要显式指定像素单位，当前支持的像素单位有：

- px：逻辑尺寸单位。

- fp：字体尺寸单位，随系统字体大小设置发生变化，仅支持文本类组件设置相应的字体大小。

percentagestring百分比尺寸单位，如“50%”。[]()[]()

#### 颜色类型

名称类型定义描述colorstring |颜色枚举

用于描述颜色信息。

 字符串格式如下：

- 'rgb(255, 255, 255)'。

- 'rgba(255, 255, 255, 1.0)'。

- HEX格式：'#rrggbb'，'#aarrggbb'。

- 枚举格式：'black'，'white'。

JS脚本中不支持颜色枚举格式。

**表1** 当前支持的颜色枚举

枚举名称对应颜色颜色aliceblue#f0f8ffantiquewhite#faebd7aqua#00ffffaquamarine#7fffd4azure#f0ffffbeige#f5f5dcbisque#ffe4c4black#000000blanchedalmond#ffebcdblue#0000ffblueviolet#8a2be2brown#a52a2aburlywood#deB887cadetblue#5f9ea0chartreuse#7fff00chocolate#d2691ecoral#ff7f50cornflowerblue#6495edcornsilk#fff8dccrimson#dc143ccyan#00ffffdarkblue#00008bdarkcyan#008b8bdarkgoldenrod#b8860bdarkgray#a9a9a9darkgreen#006400darkgrey#a9a9a9darkkhaki#bdb76bdarkmagenta#8b008bdarkolivegreen#556b2fdarkorange#ff8c00darkorchid#9932ccdarkred#8b0000darksalmon#e9967adarkseagreen#8fbc8fdarkslateblue#483d8bdarkslategray#2f4f4fdarkslategrey#2f4f4fdarkturquoise#00ced1darkviolet#9400d3deeppink#ff1493deepskyblue#00bfffdimgray#696969dimgrey#696969dodgerblue#1e90fffirebrick#b22222floralwhite#fffaf0forestgreen#228b22fuchsia#ff00ffgainsboro#dcdcdcghostwhite#f8f8ffgold#ffd700goldenrod#daa520gray#808080green#008000greenyellow#adff2fgrey#808080honeydew#f0fff0hotpink#ff69b4indianred#cd5c5cindigo#4b0082ivory#fffff0khaki#f0e68clavender#e6e6falavenderblush#fff0f5lawngreen#7cfc00lemonchiffon#fffacdlightblue#add8e6lightcoral#f08080lightcyan#e0fffflightgoldenrodyellow#fafad2lightgray#d3d3d3lightgreen#90ee90lightpink#ffb6c1lightsalmon#ffa07alightseagreen#20b2aalightskyblue#87cefalightslategray#778899lightslategrey#778899lightsteelblue#b0c4delightyellow#ffffe0lime#00ff00limegreen#32cd32linen#faf0e6magenta#ff00ffmaroon#800000mediumaquamarine#66cdaamediumblue#0000cdmediumorchid#ba55d3mediumpurple#9370dbmediumseagreen#3cb371mediumslateblue#7b68eemediumspringgreen#00fa9amediumturquoise#48d1ccmediumvioletred#c71585midnightblue#191970mintcream#f5fffamistyrose#ffe4e1moccasin#ffe4b5navajowhite#ffdeadnavy#000080oldlace#fdf5e6olive#808000olivedrab#6b8e23orange#ffa500orangered#ff4500orchid#da70d6palegoldenrod#eee8aapalegreen#98fb98paleturquoise#afeeeepalevioletred#db7093papayawhip#ffefd5peachpuff#ffdab9peru#cd853fpink#ffc0cbplum#dda0ddpowderblue#b0e0e6purple#800080rebeccapurple#663399red#ff0000rosybrown#bc8f8froyalblue#4169e1saddlebrown#8b4513salmon#fa8072sandybrown#f4a460seagreen#2e8b57seashell#fff5eesienna#a0522dsilver#c0c0c0skyblue#87ceebslateblue#6a5acdslategray#708090slategrey#708090snow#fffafaspringgreen#00ff7fsteelblue#4682b4tan#d2b48cteal#008080thistle#d8Bfd8tomato#ff6347turquoise#40e0d0violet#ee82eewheat#f5deb3white#ffffffwhitesmoke#f5f5f5yellow#ffff00yellowgreen#9acd32