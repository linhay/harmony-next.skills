# oh_key_code.h

#### 概述

按键设备的键值。

**引用文件：** <multimodalinput/oh_key_code.h>

**库：** libohinput.so

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**相关模块：**[input](../../topics/input/input.md)

#### 汇总

#### 枚举

名称typedef关键字描述[Input_KeyCode](#ZH-CN_TOPIC_0000002497605574__input_keycode)Input_KeyCode键值。

#### 枚举类型说明

#### Input_KeyCode

```ets
enum Input_KeyCode
```

**描述**

键值。

**起始版本：** 12

枚举项描述KEYCODE_UNKNOWN = -1未知按键KEYCODE_FN = 0功能（Fn）键KEYCODE_HOME = 1

功能（Home）键

**起始版本：** 22

KEYCODE_BACK = 2

返回键

**起始版本：** 22

KEYCODE_SEARCH = 9

搜索键

**起始版本：** 22

KEYCODE_MEDIA_PLAY_PAUSE = 10

多媒体键：播放/暂停。

**起始版本：** 22

与KEYCODE_PLAYPAUSE的区别为：

KEYCODE_PLAYPAUSE是较早的定义，KEYCODE_MEDIA_PLAY_PAUSE为现代媒体键设备设计，常见于较新的媒体键设备。

KEYCODE_MEDIA_STOP = 11

光盘停止键

**起始版本：** 22

KEYCODE_MEDIA_NEXT = 12

多媒体键：下一首

**起始版本：** 22

KEYCODE_MEDIA_PREVIOUS = 13

多媒体键：上一首

**起始版本：** 22

KEYCODE_MEDIA_REWIND = 14

多媒体键：快退

**起始版本：** 22

KEYCODE_MEDIA_FAST_FORWARD = 15

多媒体键：快进

**起始版本：** 22

KEYCODE_VOLUME_UP = 16音量增加键KEYCODE_VOLUME_DOWN = 17音量减小键KEYCODE_POWER = 18电源键KEYCODE_CAMERA = 19拍照键KEYCODE_VOLUME_MUTE = 22扬声器静音键KEYCODE_MUTE = 23话筒静音键KEYCODE_BRIGHTNESS_UP = 40亮度调节按键：调亮KEYCODE_BRIGHTNESS_DOWN = 41亮度调节按键：调暗KEYCODE_0 = 2000按键'0'KEYCODE_1 = 2001按键'1'KEYCODE_2 = 2002按键'2'KEYCODE_3 = 2003按键'3'KEYCODE_4 = 2004按键'4'KEYCODE_5 = 2005按键'5'KEYCODE_6 = 2006按键'6'KEYCODE_7 = 2007按键'7'KEYCODE_8 = 2008按键'8'KEYCODE_9 = 2009按键'9'KEYCODE_STAR = 2010按键'*'KEYCODE_POUND = 2011按键'#'KEYCODE_DPAD_UP = 2012导航键：向上KEYCODE_DPAD_DOWN = 2013导航键：向下KEYCODE_DPAD_LEFT = 2014导航键：向左KEYCODE_DPAD_RIGHT = 2015导航键：向右KEYCODE_DPAD_CENTER = 2016导航键：确定键KEYCODE_A = 2017按键'A'KEYCODE_B = 2018按键'B'KEYCODE_C = 2019按键'C'KEYCODE_D = 2020按键'D'KEYCODE_E = 2021按键'E'KEYCODE_F = 2022按键'F'KEYCODE_G = 2023按键'G'KEYCODE_H = 2024按键'H'KEYCODE_I = 2025按键'I'KEYCODE_J = 2026按键'J'KEYCODE_K = 2027按键'K'KEYCODE_L = 2028按键'L'KEYCODE_M = 2029按键'M'KEYCODE_N = 2030按键'N'KEYCODE_O = 2031按键'O'KEYCODE_P = 2032按键'P'KEYCODE_Q = 2033按键'Q'KEYCODE_R = 2034按键'R'KEYCODE_S = 2035按键'S'KEYCODE_T = 2036按键'T'KEYCODE_U = 2037按键'U'KEYCODE_V = 2038按键'V'KEYCODE_W = 2039按键'W'KEYCODE_X = 2040按键'X'KEYCODE_Y = 2041按键'Y'KEYCODE_Z = 2042按键'Z'KEYCODE_COMMA = 2043按键','KEYCODE_PERIOD = 2044按键'.'KEYCODE_ALT_LEFT = 2045左Alt键KEYCODE_ALT_RIGHT = 2046右Alt键KEYCODE_SHIFT_LEFT = 2047左Shift键KEYCODE_SHIFT_RIGHT = 2048右Shift键KEYCODE_TAB = 2049Tab键KEYCODE_SPACE = 2050空格键KEYCODE_SYM = 2051符号修改器按键KEYCODE_EXPLORER = 2052浏览器功能键，此键用于启动浏览器应用程序KEYCODE_ENVELOPE = 2053电子邮件功能键，此键用于启动电子邮件应用程序KEYCODE_ENTER = 2054回车键KEYCODE_DEL = 2055退格键KEYCODE_GRAVE = 2056按键'`'KEYCODE_MINUS = 2057按键'-'KEYCODE_EQUALS = 2058按键'='KEYCODE_LEFT_BRACKET = 2059按键'['KEYCODE_RIGHT_BRACKET = 2060按键']'KEYCODE_BACKSLASH = 2061按键''KEYCODE_SEMICOLON = 2062按键';'KEYCODE_APOSTROPHE = 2063按键''' (单引号)KEYCODE_SLASH = 2064按键'/'KEYCODE_AT = 2065按键'@'KEYCODE_PLUS = 2066按键'+'KEYCODE_MENU = 2067菜单键KEYCODE_PAGE_UP = 2068向上翻页键KEYCODE_PAGE_DOWN = 2069向下翻页键KEYCODE_ESCAPE = 2070ESC键KEYCODE_FORWARD_DEL = 2071删除键KEYCODE_CTRL_LEFT = 2072左Ctrl键KEYCODE_CTRL_RIGHT = 2073右Ctrl键KEYCODE_CAPS_LOCK = 2074大写锁定键KEYCODE_SCROLL_LOCK = 2075滚动锁定键KEYCODE_META_LEFT = 2076左元修改器键KEYCODE_META_RIGHT = 2077右元修改器键KEYCODE_FUNCTION = 2078功能键KEYCODE_SYSRQ = 2079系统请求/打印屏幕键KEYCODE_BREAK = 2080Break/Pause键KEYCODE_MOVE_HOME = 2081光标移动到开始键KEYCODE_MOVE_END = 2082光标移动到末尾键KEYCODE_INSERT = 2083插入键KEYCODE_FORWARD = 2084前进键KEYCODE_MEDIA_PLAY = 2085多媒体键：播放KEYCODE_MEDIA_PAUSE = 2086多媒体键：暂停KEYCODE_MEDIA_CLOSE = 2087多媒体键：关闭KEYCODE_MEDIA_EJECT = 2088多媒体键：弹出KEYCODE_MEDIA_RECORD = 2089多媒体键：录音KEYCODE_F1 = 2090按键'F1'KEYCODE_F2 = 2091按键'F2'KEYCODE_F3 = 2092按键'F3'KEYCODE_F4 = 2093按键'F4'KEYCODE_F5 = 2094按键'F5'KEYCODE_F6 = 2095按键'F6'KEYCODE_F7 = 2096按键'F7'KEYCODE_F8 = 2097按键'F8'KEYCODE_F9 = 2098按键'F9'KEYCODE_F10 = 2099按键'F10'KEYCODE_F11 = 2100按键'F11'KEYCODE_F12 = 2101按键'F12'KEYCODE_NUM_LOCK = 2102小键盘锁KEYCODE_NUMPAD_0 = 2103小键盘按键'0'KEYCODE_NUMPAD_1 = 2104小键盘按键'1'KEYCODE_NUMPAD_2 = 2105小键盘按键'2'KEYCODE_NUMPAD_3 = 2106小键盘按键'3'KEYCODE_NUMPAD_4 = 2107小键盘按键'4'KEYCODE_NUMPAD_5 = 2108小键盘按键'5'KEYCODE_NUMPAD_6 = 2109小键盘按键'6'KEYCODE_NUMPAD_7 = 2110小键盘按键'7'KEYCODE_NUMPAD_8 = 2111小键盘按键'8'KEYCODE_NUMPAD_9 = 2112小键盘按键'9'KEYCODE_NUMPAD_DIVIDE = 2113小键盘按键'/'KEYCODE_NUMPAD_MULTIPLY = 2114小键盘按键'*'KEYCODE_NUMPAD_SUBTRACT = 2115小键盘按键'-'KEYCODE_NUMPAD_ADD = 2116小键盘按键'+'KEYCODE_NUMPAD_DOT = 2117小键盘按键'.'KEYCODE_NUMPAD_COMMA = 2118小键盘按键','KEYCODE_NUMPAD_ENTER = 2119小键盘按键回车KEYCODE_NUMPAD_EQUALS = 2120小键盘按键'='KEYCODE_NUMPAD_LEFT_PAREN = 2121小键盘按键'('KEYCODE_NUMPAD_RIGHT_PAREN = 2122小键盘按键')'KEYCODE_VIRTUAL_MULTITASK = 2210

虚拟多任务键

**起始版本：** 22

KEYCODE_BUTTON_A = 2301

游戏手柄按键'A'

**起始版本：** 22

KEYCODE_BUTTON_B = 2302

游戏手柄按键'B'

**起始版本：** 22

KEYCODE_BUTTON_X = 2304

游戏手柄按键'X'

**起始版本：** 22

KEYCODE_BUTTON_Y = 2305

游戏手柄按键'Y'

**起始版本：** 22

KEYCODE_BUTTON_L1 = 2307

游戏手柄按键'L1'

**起始版本：** 22

KEYCODE_BUTTON_R1 = 2308

游戏手柄按键'R1'

**起始版本：** 22

KEYCODE_BUTTON_L2 = 2309

游戏手柄按键'L2'

**起始版本：** 22

KEYCODE_BUTTON_R2 = 2310

游戏手柄按键'R2'

**起始版本：** 22

KEYCODE_BUTTON_SELECT = 2311

游戏手柄按键'Select'

**起始版本：** 22

KEYCODE_BUTTON_START = 2312

游戏手柄按键'Start'

**起始版本：** 22

KEYCODE_BUTTON_MODE = 2313

游戏手柄按键'Mode'

**起始版本：** 22

KEYCODE_BUTTON_THUMBL = 2314

游戏手柄按键'THUMBL'

**起始版本：** 22

KEYCODE_BUTTON_THUMBR = 2315

游戏手柄按键'THUMBR'

**起始版本：** 22

KEYCODE_SLEEP = 2600

睡眠键

**起始版本：** 22

KEYCODE_ZENKAKU_HANKAKU = 2601

日文全宽/半宽键

**起始版本：** 22

KEYCODE_102ND = 2602

102nd按键

**起始版本：** 22

KEYCODE_RO = 2603

日文Ro键

**起始版本：** 22

KEYCODE_KATAKANA = 2604

日文片假名键

**起始版本：** 22

KEYCODE_HIRAGANA = 2605

日文平假名键

**起始版本：** 22

KEYCODE_HENKAN = 2606

日文转换键

**起始版本：** 22

KEYCODE_KATAKANA_HIRAGANA = 2607

日语片假名/平假名键

**起始版本：** 22

KEYCODE_MUHENKAN = 2608

日文非转换键

**起始版本：** 22

KEYCODE_LINEFEED = 2609

换行键

**起始版本：** 22

KEYCODE_MACRO = 2610

宏键

**起始版本：** 22

KEYCODE_NUMPAD_PLUSMINUS = 2611

数字键盘上的加号/减号键

**起始版本：** 22

KEYCODE_SCALE = 2612

扩展键

**起始版本：** 22

KEYCODE_HANGUEL = 2613

日文韩语键

**起始版本：** 22

KEYCODE_HANJA = 2614

日文汉语键

**起始版本：** 22

KEYCODE_YEN = 2615

日元键

**起始版本：** 22

KEYCODE_STOP = 2616

停止键

**起始版本：** 22

KEYCODE_AGAIN = 2617

重复键

**起始版本：** 22

KEYCODE_PROPS = 2618

道具键

**起始版本：** 22

KEYCODE_UNDO = 2619

撤消键

**起始版本：** 22

KEYCODE_COPY = 2620

复制键

**起始版本：** 22

KEYCODE_OPEN = 2621

打开键

**起始版本：** 22

KEYCODE_PASTE = 2622

粘贴键

**起始版本：** 22

KEYCODE_FIND = 2623

查找键

**起始版本：** 22

KEYCODE_CUT = 2624

剪切键

**起始版本：** 22

KEYCODE_HELP = 2625

帮助键

**起始版本：** 22

KEYCODE_CALC = 2626

计算器特殊功能键，用于启动计算器应用程序

**起始版本：** 22

KEYCODE_FILE = 2627

文件按键

**起始版本：** 22

KEYCODE_BOOKMARKS = 2628

书签键

**起始版本：** 22

KEYCODE_NEXT = 2629

Page Down键

**起始版本：** 22

KEYCODE_PLAYPAUSE = 2630

多媒体键：播放/暂停。

**起始版本：** 22

与KEYCODE_MEDIA_PLAY_PAUSE的区别为：

KEYCODE_PLAYPAUSE是较早的定义，KEYCODE_MEDIA_PLAY_PAUSE为现代媒体键设备设计，常见于较新的媒体键设备。

KEYCODE_PREVIOUS = 2631

Page Up键

**起始版本：** 22

KEYCODE_STOPCD = 2632

CD停止键

**起始版本：** 22

KEYCODE_CONFIG = 2634

配置键

**起始版本：** 22

KEYCODE_REFRESH = 2635

刷新键

**起始版本：** 22

KEYCODE_EXIT = 2636

退出键

**起始版本：** 22

KEYCODE_EDIT = 2637

编辑键

**起始版本：** 22

KEYCODE_SCROLLUP = 2638

向上滚动键

**起始版本：** 22

KEYCODE_SCROLLDOWN = 2639

向下滚动键

**起始版本：** 22

KEYCODE_NEW = 2640

新建键

**起始版本：** 22

KEYCODE_REDO = 2641

恢复键

**起始版本：** 22

KEYCODE_CLOSE = 2642

关闭键

**起始版本：** 22

KEYCODE_PLAY = 2643

播放键

**起始版本：** 22

KEYCODE_BASSBOOST = 2644

低音增强键

**起始版本：** 22

KEYCODE_PRINT = 2645

打印键

**起始版本：** 22

KEYCODE_CHAT = 2646

聊天键

**起始版本：** 22

KEYCODE_FINANCE = 2647

金融键

**起始版本：** 22

KEYCODE_CANCEL = 2648

取消键

**起始版本：** 22

KEYCODE_KBDILLUM_TOGGLE = 2649

键盘灯光切换键

**起始版本：** 22

KEYCODE_KBDILLUM_DOWN = 2650

键盘灯光调暗键

**起始版本：** 22

KEYCODE_KBDILLUM_UP = 2651

键盘灯光调亮键

**起始版本：** 22

KEYCODE_SEND = 2652

发送键

**起始版本：** 22

KEYCODE_REPLY = 2653

答复键

**起始版本：** 22

KEYCODE_FORWARDMAIL = 2654

邮件转发键

**起始版本：** 22

KEYCODE_SAVE = 2655

保存键

**起始版本：** 22

KEYCODE_DOCUMENTS = 2656

文件键

**起始版本：** 22

KEYCODE_VIDEO_NEXT = 2657

下一个视频键

**起始版本：** 22

KEYCODE_VIDEO_PREV = 2658

上一个视频键

**起始版本：** 22

KEYCODE_BRIGHTNESS_CYCLE = 2659

背光渐变键

**起始版本：** 22

KEYCODE_BRIGHTNESS_ZERO = 2660

亮度调节为0键

**起始版本：** 22

KEYCODE_DISPLAY_OFF = 2661

显示关闭键

**起始版本：** 22

KEYCODE_BTN_MISC = 2662

游戏手柄上的各种按键

**起始版本：** 22

KEYCODE_GOTO = 2663

进入键

**起始版本：** 22

KEYCODE_INFO = 2664

信息查看键

**起始版本：** 22

KEYCODE_PROGRAM = 2665

程序键

**起始版本：** 22

KEYCODE_PVR = 2666

个人录像机（PVR）键

**起始版本：** 22

KEYCODE_SUBTITLE = 2667

字幕键

**起始版本：** 22

KEYCODE_FULL_SCREEN = 2668

全屏键

**起始版本：** 22

KEYCODE_KEYBOARD = 2669

键盘

**起始版本：** 22

KEYCODE_ASPECT_RATIO = 2670

屏幕纵横比调节键

**起始版本：** 22

KEYCODE_PC = 2671

端口控制键

**起始版本：** 22

KEYCODE_TV = 2672

TV键

**起始版本：** 22

KEYCODE_TV2 = 2673

TV键2

**起始版本：** 22

KEYCODE_VCR = 2674

录像机开启键

**起始版本：** 22

KEYCODE_VCR2 = 2675

录像机开启键2

**起始版本：** 22

KEYCODE_SAT = 2676

SIM卡应用工具包（SAT）键

**起始版本：** 22

KEYCODE_CD = 2677

CD键

**起始版本：** 22

KEYCODE_TAPE = 2678

磁带键

**起始版本：** 22

KEYCODE_TUNER = 2679

调谐器键

**起始版本：** 22

KEYCODE_PLAYER = 2680

播放器键

**起始版本：** 22

KEYCODE_DVD = 2681

DVD键

**起始版本：** 22

KEYCODE_AUDIO = 2682

音频键

**起始版本：** 22

KEYCODE_VIDEO = 2683

视频键

**起始版本：** 22

KEYCODE_MEMO = 2684

备忘录键

**起始版本：** 22

KEYCODE_CALENDAR = 2685

日历键

**起始版本：** 22

KEYCODE_RED = 2686

红色指示器

**起始版本：** 22

KEYCODE_GREEN = 2687

绿色指示器

**起始版本：** 22

KEYCODE_YELLOW = 2688

黄色指示器

**起始版本：** 22

KEYCODE_BLUE = 2689

蓝色指示器

**起始版本：** 22

KEYCODE_CHANNELUP = 2690

频道向上键

**起始版本：** 22

KEYCODE_CHANNELDOWN = 2691

频道向下键

**起始版本：** 22

KEYCODE_LAST = 2692

末尾键

**起始版本：** 22

KEYCODE_RESTART = 2693

重启键

**起始版本：** 22

KEYCODE_SLOW = 2694

慢速键

**起始版本：** 22

KEYCODE_SHUFFLE = 2695

随机播放键

**起始版本：** 22

KEYCODE_VIDEOPHONE = 2696

可视电话键

**起始版本：** 22

KEYCODE_GAMES = 2697

游戏键

**起始版本：** 22

KEYCODE_ZOOMIN = 2698

放大键

**起始版本：** 22

KEYCODE_ZOOMOUT = 2699

缩小键

**起始版本：** 22

KEYCODE_ZOOMRESET = 2700

缩放重置键

**起始版本：** 22

KEYCODE_WORDPROCESSOR = 2701

文字处理键

**起始版本：** 22

KEYCODE_EDITOR = 2702

编辑器键

**起始版本：** 22

KEYCODE_SPREADSHEET = 2703

电子表格键

**起始版本：** 22

KEYCODE_GRAPHICSEDITOR = 2704

图形编辑器键

**起始版本：** 22

KEYCODE_PRESENTATION = 2705

演示文稿键

**起始版本：** 22

KEYCODE_DATABASE = 2706

数据库键标

**起始版本：** 22

KEYCODE_NEWS = 2707

新闻键

**起始版本：** 22

KEYCODE_VOICEMAIL = 2708

语音信箱

**起始版本：** 22

KEYCODE_ADDRESSBOOK = 2709

通讯簿

**起始版本：** 22

KEYCODE_MESSENGER = 2710

通信键

**起始版本：** 22

KEYCODE_BRIGHTNESS_TOGGLE = 2711

亮度切换键

**起始版本：** 22

KEYCODE_SPELLCHECK = 2712

AL拼写检查

**起始版本：** 22

KEYCODE_COFFEE = 2713

终端锁/屏幕保护程序

**起始版本：** 22

KEYCODE_MEDIA_REPEAT = 2714

媒体循环键

**起始版本：** 22

KEYCODE_IMAGES = 2715

图像键

**起始版本：** 22

KEYCODE_BUTTONCONFIG = 2716

按键配置键

**起始版本：** 22

KEYCODE_TASKMANAGER = 2717

任务管理器

**起始版本：** 22

KEYCODE_JOURNAL = 2718

日志按键

**起始版本：** 22

KEYCODE_CONTROLPANEL = 2719

控制面板键

**起始版本：** 22

KEYCODE_APPSELECT = 2720

应用程序选择键

**起始版本：** 22

KEYCODE_SCREENSAVER = 2721

屏幕保护程序键

**起始版本：** 22

KEYCODE_ASSISTANT = 2722

智慧键

**起始版本：** 22

KEYCODE_KBD_LAYOUT_NEXT = 2723

下一个键盘布局键

**起始版本：** 22

KEYCODE_BRIGHTNESS_MIN = 2724

最小亮度键

**起始版本：** 22

KEYCODE_BRIGHTNESS_MAX = 2725

最大亮度键

**起始版本：** 22

KEYCODE_KBDINPUTASSIST_PREV = 2726

键盘输入Assist_Previous，查看输入法输入记录

**起始版本：** 22

KEYCODE_KBDINPUTASSIST_NEXT = 2727

键盘输入Assist_Next，查看输入法输入拓展

**起始版本：** 22

KEYCODE_KBDINPUTASSIST_PREVGROUP = 2728

键盘输入Assist_Previous，切换输入组中上一个输入法

**起始版本：** 22

KEYCODE_KBDINPUTASSIST_NEXTGROUP = 2729

键盘输入Assist_Next，切换输入组中下一个输入法

**起始版本：** 22

KEYCODE_KBDINPUTASSIST_ACCEPT = 2730

键盘输入Assist_Accept

**起始版本：** 22

KEYCODE_KBDINPUTASSIST_CANCEL = 2731

键盘输入Assist_Cancel

**起始版本：** 22

KEYCODE_FRONT = 2800

挡风玻璃除雾器开关

**起始版本：** 22

KEYCODE_SETUP = 2801

设置键

**起始版本：** 22

KEYCODE_WAKEUP = 2802

唤醒键

**起始版本：** 22

KEYCODE_SENDFILE = 2803

发送文件按键

**起始版本：** 22

KEYCODE_DELETEFILE = 2804

删除文件按键

**起始版本：** 22

KEYCODE_XFER = 2805

文件传输（XFER）按键

**起始版本：** 22

KEYCODE_PROG1 = 2806

程序键1

**起始版本：** 22

KEYCODE_PROG2 = 2807

程序键2

**起始版本：** 22

KEYCODE_MSDOS = 2808

MS-DOS键（微软磁盘操作系统）

**起始版本：** 22

KEYCODE_SCREENLOCK = 2809

屏幕锁定键

**起始版本：** 22

KEYCODE_DIRECTION_ROTATE_DISPLAY = 2810

方向旋转显示键

**起始版本：** 22

KEYCODE_CYCLEWINDOWS = 2811

Windows循环键

**起始版本：** 22

KEYCODE_COMPUTER = 2812

按键

**起始版本：** 22

KEYCODE_EJECTCLOSECD = 2813

弹出CD键

**起始版本：** 22

KEYCODE_ISO = 2814

ISO键

**起始版本：** 22

KEYCODE_MOVE = 2815

移动键

**起始版本：** 22

KEYCODE_F13 = 2816

按键'F13'

**起始版本：** 22

KEYCODE_F14 = 2817

按键'F14'

**起始版本：** 22

KEYCODE_F15 = 2818

按键'F15'

**起始版本：** 22

KEYCODE_F16 = 2819

按键'F16'

**起始版本：** 22

KEYCODE_F17 = 2820

按键'F17'

**起始版本：** 22

KEYCODE_F18 = 2821

按键'F18'

**起始版本：** 22

KEYCODE_F19 = 2822

按键'F19'

**起始版本：** 22

KEYCODE_F20 = 2823

按键'F20'

**起始版本：** 22

KEYCODE_F21 = 2824

按键'F21'

**起始版本：** 22

KEYCODE_F22 = 2825

按键'F22'

**起始版本：** 22

KEYCODE_F23 = 2826

按键'F23'

**起始版本：** 22

KEYCODE_F24 = 2827

按键'F24'

**起始版本：** 22

KEYCODE_PROG3 = 2828

程序键3

**起始版本：** 22

KEYCODE_PROG4 = 2829

程序键4

**起始版本：** 22

KEYCODE_DASHBOARD = 2830

仪表板

**起始版本：** 22

KEYCODE_SUSPEND = 2831

挂起键

**起始版本：** 22

KEYCODE_HP = 2832

高阶路径键

**起始版本：** 22

KEYCODE_SOUND = 2833

音量键

**起始版本：** 22

KEYCODE_QUESTION = 2834

疑问按键

**起始版本：** 22

KEYCODE_CONNECT = 2836

连接键

**起始版本：** 22

KEYCODE_SPORT = 2837

运动按键

**起始版本：** 22

KEYCODE_SHOP = 2838

商城键

**起始版本：** 22

KEYCODE_ALTERASE = 2839

交替键

**起始版本：** 22

KEYCODE_SWITCHVIDEOMODE = 2841

在可用视频之间循环输出（监视器/LCD/TV输出/等）

**起始版本：** 22

KEYCODE_BATTERY = 2842

电池按键

**起始版本：** 22

KEYCODE_BLUETOOTH = 2843

蓝牙按键

**起始版本：** 22

KEYCODE_WLAN = 2844

无线局域网

**起始版本：** 22

KEYCODE_UWB = 2845

超宽带（UWB）

**起始版本：** 22

KEYCODE_WWAN_WIMAX = 2846

WWAN WiMAX按键

**起始版本：** 22

KEYCODE_RFKILL = 2847

控制所有收音机的键

**起始版本：** 22

KEYCODE_CHANNEL = 3001

向上频道键

**起始版本：** 22

KEYCODE_BTN_0 = 3100

按键0

**起始版本：** 22

KEYCODE_BTN_1 = 3101

按键1

**起始版本：** 22

KEYCODE_BTN_2 = 3102

按键2

**起始版本：** 22

KEYCODE_BTN_3 = 3103

按键3

**起始版本：** 22

KEYCODE_BTN_4 = 3104

按键4

**起始版本：** 22

KEYCODE_BTN_5 = 3105

按键5

**起始版本：** 22

KEYCODE_BTN_6 = 3106

按键6

**起始版本：** 22

KEYCODE_BTN_7 = 3107

按键7

**起始版本：** 22

KEYCODE_BTN_8 = 3108

按键8

**起始版本：** 22

KEYCODE_BTN_9 = 3109

按键9

**起始版本：** 22

KEYCODE_DAGGER_CLICK = 3211

智能手表智感窗按键单击

**起始版本：** 22

KEYCODE_DAGGER_DOUBLE_CLICK = 3212

智能手表智感窗按键双击

**起始版本：** 22

KEYCODE_DAGGER_LONG_PRESS = 3213

智能手表智感窗按键长按

**起始版本：** 22

KEYCODE_DIV = 3220

智能手表左按键

**起始版本：** 22