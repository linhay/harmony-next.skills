# native_xcomponent_key_event.h

**概述**

声明用于访问Native XComponent键盘事件所使用到的枚举类型。

引用文件： <ace/xcomponent/native_xcomponent_key_event.h>

库： libace_ndk.z.so

系统能力： SystemCapability.ArkUI.ArkUI.Full

起始版本： 10

相关模块： [OH_NativeXComponent Native XComponent](OH_NativeXComponent Native XComponent.md)

相关示例： [NativeXComponentSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeXComponentSample)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_NativeXComponent_KeyCode | OH_NativeXComponent_KeyCode | 按键事件的键码。 |
| OH_NativeXComponent_KeyAction | OH_NativeXComponent_KeyAction | 按键事件动作。 |

**枚举类型说明**

**OH_NativeXComponent_KeyCode**

```ets
enum OH_NativeXComponent_KeyCode
```

描述：

按键事件的键码。

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| KEY_UNKNOWN = -1 | 未知按键。 |
| KEY_FN = 0 | 功能（Fn）键。 |
| KEY_HOME = 1 | 功能（Home）键。 |
| KEY_BACK = 2 | 返回键。 |
| KEY_MEDIA_PLAY_PAUSE = 10 | 多媒体键，播放/暂停。 |
| KEY_MEDIA_STOP = 11 | 多媒体键，停止。 |
| KEY_MEDIA_NEXT = 12 | 多媒体键，下一首。 |
| KEY_MEDIA_PREVIOUS = 13 | 多媒体键，上一首。 |
| KEY_MEDIA_REWIND = 14 | 多媒体键，快退。 |
| KEY_MEDIA_FAST_FORWARD = 15 | 多媒体键，快进。 |
| KEY_VOLUME_UP = 16 | 音量增加键。 |
| KEY_VOLUME_DOWN = 17 | 音量减小键。 |
| KEY_POWER = 18 | 电源键。 |
| KEY_CAMERA = 19 | 拍照键。 |
| KEY_VOLUME_MUTE = 22 | 扬声器静音键。 |
| KEY_MUTE = 23 | 话筒静音键。 |
| KEY_BRIGHTNESS_UP = 40 | 亮度调节按键，调亮。 |
| KEY_BRIGHTNESS_DOWN = 41 | 亮度调节按键，调暗。 |
| KEY_0 = 2000 | 按键'0'。 |
| KEY_1 = 2001 | 按键'1'。 |
| KEY_2 = 2002 | 按键'2'。 |
| KEY_3 = 2003 | 按键'3'。 |
| KEY_4 = 2004 | 按键'4'。 |
| KEY_5 = 2005 | 按键'5'。 |
| KEY_6 = 2006 | 按键'6'。 |
| KEY_7 = 2007 | 按键'7'。 |
| KEY_8 = 2008 | 按键'8'。 |
| KEY_9 = 2009 | 按键'9'。 |
| KEY_STAR = 2010 | 按键'*'。 |
| KEY_POUND = 2011 | 按键'#'。 |
| KEY_DPAD_UP = 2012 | 导航键，向上。 |
| KEY_DPAD_DOWN = 2013 | 导航键，向下。 |
| KEY_DPAD_LEFT = 2014 | 导航键，向左。 |
| KEY_DPAD_RIGHT = 2015 | 导航键，向右。 |
| KEY_DPAD_CENTER = 2016 | 导航键，确定键。 |
| KEY_A = 2017 | 按键'A'。 |
| KEY_B = 2018 | 按键'B'。 |
| KEY_C = 2019 | 按键'C'。 |
| KEY_D = 2020 | 按键'D'。 |
| KEY_E = 2021 | 按键'E'。 |
| KEY_F = 2022 | 按键'F'。 |
| KEY_G = 2023 | 按键'G'。 |
| KEY_H = 2024 | 按键'H'。 |
| KEY_I = 2025 | 按键'I'。 |
| KEY_J = 2026 | 按键'J'。 |
| KEY_K = 2027 | 按键'K'。 |
| KEY_L = 2028 | 按键'L'。 |
| KEY_M = 2029 | 按键'M'。 |
| KEY_N = 2030 | 按键'N'。 |
| KEY_O = 2031 | 按键'O'。 |
| KEY_P = 2032 | 按键'P'。 |
| KEY_Q = 2033 | 按键'Q'。 |
| KEY_R = 2034 | 按键'R'。 |
| KEY_S = 2035 | 按键'S'。 |
| KEY_T = 2036 | 按键'T'。 |
| KEY_U = 2037 | 按键'U'。 |
| KEY_V = 2038 | 按键'V'。 |
| KEY_W = 2039 | 按键'W'。 |
| KEY_X = 2040 | 按键'X'。 |
| KEY_Y = 2041 | 按键'Y'。 |
| KEY_Z = 2042 | 按键'Z'。 |
| KEY_COMMA = 2043 | 按键','。 |
| KEY_PERIOD = 2044 | 按键'.'。 |
| KEY_ALT_LEFT = 2045 | 左Alt键。 |
| KEY_ALT_RIGHT = 2046 | 右Alt键。 |
| KEY_SHIFT_LEFT = 2047 | 左Shift键。 |
| KEY_SHIFT_RIGHT = 2048 | 右Shift键。 |
| KEY_TAB = 2049 | Tab键。 |
| KEY_SPACE = 2050 | 空格键。 |
| KEY_SYM = 2051 | 符号修改器按键。 |
| KEY_EXPLORER = 2052 | 浏览器功能键，此键用于启动浏览器应用程序。 |
| KEY_ENVELOPE = 2053 | 电子邮件功能键，此键用于启动电子邮件应用程序。 |
| KEY_ENTER = 2054 | 回车键。 |
| KEY_DEL = 2055 | 退格键。 |
| KEY_GRAVE = 2056 | 按键'`'。 |
| KEY_MINUS = 2057 | 按键'-'。 |
| KEY_EQUALS = 2058 | 按键'='。 |
| KEY_LEFT_BRACKET = 2059 | 按键'['。 |
| KEY_RIGHT_BRACKET = 2060 | 按键']'。 |
| KEY_BACKSLASH = 2061 | 按键'\'。 |
| KEY_SEMICOLON = 2062 | 按键';'。 |
| KEY_APOSTROPHE = 2063 | 按键''' (单引号)。 |
| KEY_SLASH = 2064 | 按键'/'。 |
| KEY_AT = 2065 | 按键'@'。 |
| KEY_PLUS = 2066 | 按键'+'。 |
| KEY_MENU = 2067 | 菜单键。 |
| KEY_PAGE_UP = 2068 | 向上翻页键。 |
| KEY_PAGE_DOWN = 2069 | 向下翻页键。 |
| KEY_ESCAPE = 2070 | ESC键。 |
| KEY_FORWARD_DEL = 2071 | 删除键。 |
| KEY_CTRL_LEFT = 2072 | 左Ctrl键。 |
| KEY_CTRL_RIGHT = 2073 | 右Ctrl键。 |
| KEY_CAPS_LOCK = 2074 | 大写锁定键。 |
| KEY_SCROLL_LOCK = 2075 | 滚动锁定键。 |
| KEY_META_LEFT = 2076 | 左元修改器键。 |
| KEY_META_RIGHT = 2077 | 右元修改器键。 |
| KEY_FUNCTION = 2078 | 功能键。 |
| KEY_SYSRQ = 2079 | 系统请求/打印屏幕键。 |
| KEY_BREAK = 2080 | Break/Pause键。 |
| KEY_MOVE_HOME = 2081 | 光标移动到开始键。 |
| KEY_MOVE_END = 2082 | 光标移动到末尾键。 |
| KEY_INSERT = 2083 | 插入键。 |
| KEY_FORWARD = 2084 | 前进键。 |
| KEY_MEDIA_PLAY = 2085 | 多媒体键，播放。 |
| KEY_MEDIA_PAUSE = 2086 | 多媒体键，暂停。 |
| KEY_MEDIA_CLOSE = 2087 | 多媒体键，关闭。 |
| KEY_MEDIA_EJECT = 2088 | 多媒体键，弹出。 |
| KEY_MEDIA_RECORD = 2089 | 多媒体键，录音。 |
| KEY_F1 = 2090 | 按键'F1'。 |
| KEY_F2 = 2091 | 按键'F2'。 |
| KEY_F3 = 2092 | 按键'F3'。 |
| KEY_F4 = 2093 | 按键'F4'。 |
| KEY_F5 = 2094 | 按键'F5'。 |
| KEY_F6 = 2095 | 按键'F6'。 |
| KEY_F7 = 2096 | 按键'F7'。 |
| KEY_F8 = 2097 | 按键'F8'。 |
| KEY_F9 = 2098 | 按键'F9'。 |
| KEY_F10 = 2099 | 按键'F10'。 |
| KEY_F11 = 2100 | 按键'F11'。 |
| KEY_F12 = 2101 | 按键'F12'。 |
| KEY_NUM_LOCK = 2102 | 小键盘锁。 |
| KEY_NUMPAD_0 = 2103 | 小键盘按键'0'。 |
| KEY_NUMPAD_1 = 2104 | 小键盘按键'1'。 |
| KEY_NUMPAD_2 = 2105 | 小键盘按键'2'。 |
| KEY_NUMPAD_3 = 2106 | 小键盘按键'3'。 |
| KEY_NUMPAD_4 = 2107 | 小键盘按键'4'。 |
| KEY_NUMPAD_5 = 2108 | 小键盘按键'5'。 |
| KEY_NUMPAD_6 = 2109 | 小键盘按键'6'。 |
| KEY_NUMPAD_7 = 2110 | 小键盘按键'7'。 |
| KEY_NUMPAD_8 = 2111 | 小键盘按键'8'。 |
| KEY_NUMPAD_9 = 2112 | 小键盘按键'9'。 |
| KEY_NUMPAD_DIVIDE = 2113 | 小键盘按键'/'。 |
| KEY_NUMPAD_MULTIPLY = 2114 | 小键盘按键'*'。 |
| KEY_NUMPAD_SUBTRACT = 2115 | 小键盘按键'-'。 |
| KEY_NUMPAD_ADD = 2116 | 小键盘按键'+'。 |
| KEY_NUMPAD_DOT = 2117 | 小键盘按键'.'。 |
| KEY_NUMPAD_COMMA = 2118 | 小键盘按键','。 |
| KEY_NUMPAD_ENTER = 2119 | 小键盘按键回车。 |
| KEY_NUMPAD_EQUALS = 2120 | 小键盘按键'='。 |
| KEY_NUMPAD_LEFT_PAREN = 2121 | 小键盘按键'('。 |
| KEY_NUMPAD_RIGHT_PAREN = 2122 | 小键盘按键')'。 |
| KEY_VIRTUAL_MULTITASK = 2210 | 虚拟多任务键。 |
| KEY_SLEEP = 2600 | 睡眠键。 |
| KEY_ZENKAKU_HANKAKU = 2601 | 日文全宽/半宽键。 |
| KEY_102ND = 2602 | 102nd按键。 |
| KEY_RO = 2603 | 日文Ro键。 |
| KEY_KATAKANA = 2604 | 日文片假名键。 |
| KEY_HIRAGANA = 2605 | 日文平假名键。 |
| KEY_HENKAN = 2606 | 日文转换键。 |
| KEY_KATAKANA_HIRAGANA = 2607 | 日语片假名/平假名键。 |
| KEY_MUHENKAN = 2608 | 日文非转换键。 |
| KEY_LINEFEED = 2609 | 换行键。 |
| KEY_MACRO = 2610 | 宏键。 |
| KEY_NUMPAD_PLUSMINUS = 2611 | 数字键盘上的加号/减号键。 |
| KEY_SCALE = 2612 | 扩展键。 |
| KEY_HANGUEL = 2613 | 日文韩语键。 |
| KEY_HANJA = 2614 | 日文汉语键。 |
| KEY_YEN = 2615 | 日元键。 |
| KEY_STOP = 2616 | 停止键。 |
| KEY_AGAIN = 2617 | 重复键。 |
| KEY_PROPS = 2618 | 道具键。 |
| KEY_UNDO = 2619 | 撤消键。 |
| KEY_COPY = 2620 | 复制键。 |
| KEY_OPEN = 2621 | 打开键。 |
| KEY_PASTE = 2622 | 粘贴键。 |
| KEY_FIND = 2623 | 查找键。 |
| KEY_CUT = 2624 | 剪切键。 |
| KEY_HELP = 2625 | 帮助键。 |
| KEY_CALC = 2626 | 计算器特殊功能键，用于启动计算器应用程序。 |
| KEY_FILE = 2627 | 文件按键。 |
| KEY_BOOKMARKS = 2628 | 书签键。 |
| KEY_NEXT = 2629 | 下一个按键。 |
| KEY_PLAYPAUSE = 2630 | 播放/暂停键。 |
| KEY_PREVIOUS = 2631 | 上一个按键。 |
| KEY_STOPCD = 2632 | CD停止键。 |
| KEY_CONFIG = 2634 | 配置键。 |
| KEY_REFRESH = 2635 | 刷新键。 |
| KEY_EXIT = 2636 | 退出键。 |
| KEY_EDIT = 2637 | 编辑键。 |
| KEY_SCROLLUP = 2638 | 向上滚动键。 |
| KEY_SCROLLDOWN = 2639 | 向下滚动键。 |
| KEY_NEW = 2640 | 新建键。 |
| KEY_REDO = 2641 | 恢复键。 |
| KEY_CLOSE = 2642 | 关闭键。 |
| KEY_PLAY = 2643 | 播放键。 |
| KEY_BASSBOOST = 2644 | 低音增强键。 |
| KEY_PRINT = 2645 | 打印键。 |
| KEY_CHAT = 2646 | 聊天键。 |
| KEY_FINANCE = 2647 | 金融键。 |
| KEY_CANCEL = 2648 | 取消键。 |
| KEY_KBDILLUM_TOGGLE = 2649 | 键盘灯光切换键。 |
| KEY_KBDILLUM_DOWN = 2650 | 键盘灯光调亮键。 |
| KEY_KBDILLUM_UP = 2651 | 键盘灯光调暗键。 |
| KEY_SEND = 2652 | 发送键。 |
| KEY_REPLY = 2653 | 答复键。 |
| KEY_FORWARDMAIL = 2654 | 邮件转发键。 |
| KEY_SAVE = 2655 | 保存键。 |
| KEY_DOCUMENTS = 2656 | 文件键。 |
| KEY_VIDEO_NEXT = 2657 | 下一个视频键。 |
| KEY_VIDEO_PREV = 2658 | 上一个视频键。 |
| KEY_BRIGHTNESS_CYCLE = 2659 | 背光渐变键。 |
| KEY_BRIGHTNESS_ZERO = 2660 | 亮度调节为0键。 |
| KEY_DISPLAY_OFF = 2661 | 显示关闭键。 |
| KEY_BTN_MISC = 2662 | 游戏手柄上的各种按键。 |
| KEY_GOTO = 2663 | 进入键。 |
| KEY_INFO = 2664 | 信息查看键。 |
| KEY_PROGRAM = 2665 | 程序键。 |
| KEY_PVR = 2666 | 个人录像机(PVR)键。 |
| KEY_SUBTITLE = 2667 | 字幕键。 |
| KEY_FULL_SCREEN = 2668 | 全屏键。 |
| KEY_KEYBOARD = 2669 | 键盘。 |
| KEY_ASPECT_RATIO = 2670 | 屏幕纵横比调节键。 |
| KEY_PC = 2671 | 端口控制键。 |
| KEY_TV = 2672 | TV键。 |
| KEY_TV2 = 2673 | TV键2。 |
| KEY_VCR = 2674 | 录像机开启键。 |
| KEY_VCR2 = 2675 | 录像机开启键2。 |
| KEY_SAT = 2676 | SIM卡应用工具包（SAT）键。 |
| KEY_CD = 2677 | CD键。 |
| KEY_TAPE = 2678 | 磁带键。 |
| KEY_TUNER = 2679 | 调谐器键。 |
| KEY_PLAYER = 2680 | 播放器键。 |
| KEY_DVD = 2681 | DVD键。 |
| KEY_AUDIO = 2682 | 音频键。 |
| KEY_VIDEO = 2683 | 视频键。 |
| KEY_MEMO = 2684 | 备忘录键。 |
| KEY_CALENDAR = 2685 | 日历键。 |
| KEY_RED = 2686 | 红色指示器。 |
| KEY_GREEN = 2687 | 绿色指示器。 |
| KEY_YELLOW = 2688 | 黄色指示器。 |
| KEY_BLUE = 2689 | 蓝色指示器。 |
| KEY_CHANNELUP = 2690 | 频道向上键。 |
| KEY_CHANNELDOWN = 2691 | 频道向下键。 |
| KEY_LAST = 2692 | 末尾键。 |
| KEY_RESTART = 2693 | 重启键。 |
| KEY_SLOW = 2694 | 慢速键。 |
| KEY_SHUFFLE = 2695 | 随机播放键。 |
| KEY_VIDEOPHONE = 2696 | 可视电话键。 |
| KEY_GAMES = 2697 | 游戏键。 |
| KEY_ZOOMIN = 2698 | 放大键。 |
| KEY_ZOOMOUT = 2699 | 缩小键。 |
| KEY_ZOOMRESET = 2700 | 缩放重置键。 |
| KEY_WORDPROCESSOR = 2701 | 文字处理键。 |
| KEY_EDITOR = 2702 | 编辑器键。 |
| KEY_SPREADSHEET = 2703 | 电子表格键。 |
| KEY_GRAPHICSEDITOR = 2704 | 图形编辑器键。 |
| KEY_PRESENTATION = 2705 | 演示文稿键。 |
| KEY_DATABASE = 2706 | 数据库键标。 |
| KEY_NEWS = 2707 | 新闻键。 |
| KEY_VOICEMAIL = 2708 | 语音信箱。 |
| KEY_ADDRESSBOOK = 2709 | 通讯簿。 |
| KEY_MESSENGER = 2710 | 通信键。 |
| KEY_BRIGHTNESS_TOGGLE = 2711 | 亮度切换键。 |
| KEY_SPELLCHECK = 2712 | AL拼写检查。 |
| KEY_COFFEE = 2713 | 终端锁/屏幕保护程序。 |
| KEY_MEDIA_REPEAT = 2714 | 媒体循环键。 |
| KEY_IMAGES = 2715 | 图像键。 |
| KEY_BUTTONCONFIG = 2716 | 按键配置键。 |
| KEY_TASKMANAGER = 2717 | 任务管理器。 |
| KEY_JOURNAL = 2718 | 日志按键。 |
| KEY_CONTROLPANEL = 2719 | 控制面板键。 |
| KEY_APPSELECT = 2720 | 应用程序选择键。 |
| KEY_SCREENSAVER = 2721 | 屏幕保护程序键。 |
| KEY_ASSISTANT = 2722 | 辅助键。 |
| KEY_KBD_LAYOUT_NEXT = 2723 | 下一个键盘布局键。 |
| KEY_BRIGHTNESS_MIN = 2724 | 最小亮度键。 |
| KEY_BRIGHTNESS_MAX = 2725 | 最大亮度键。 |
| KEY_KBDINPUTASSIST_PREV = 2726 | 键盘输入Assist_Previous。 |
| KEY_KBDINPUTASSIST_NEXT = 2727 | 键盘输入Assist_Next。 |
| KEY_KBDINPUTASSIST_PREVGROUP = 2728 | 键盘输入Assist_Previous。 |
| KEY_KBDINPUTASSIST_NEXTGROUP = 2729 | 键盘输入Assist_Next。 |
| KEY_KBDINPUTASSIST_ACCEPT = 2730 | 键盘输入Assist_Accept。 |
| KEY_KBDINPUTASSIST_CANCEL = 2731 | 键盘输入Assist_Cancel。 |
| KEY_FRONT = 2800 | 挡风玻璃除雾器开关。 |
| KEY_SETUP = 2801 | 设置键。 |
| KEY_WAKEUP = 2802 | 唤醒键。 |
| KEY_SENDFILE = 2803 | 发送文件按键。 |
| KEY_DELETEFILE = 2804 | 删除文件按键。 |
| KEY_XFER = 2805 | 文件传输(XFER)按键。 |
| KEY_PROG1 = 2806 | 程序键1。 |
| KEY_PROG2 = 2807 | 程序键2。 |
| KEY_MSDOS = 2808 | MS-DOS键（微软磁盘操作系统）。 |
| KEY_SCREENLOCK = 2809 | 屏幕锁定键。 |
| KEY_DIRECTION_ROTATE_DISPLAY = 2810 | 方向旋转显示键。 |
| KEY_CYCLEWINDOWS = 2811 | Windows循环键。 |
| KEY_COMPUTER = 2812 | 按键。 |
| KEY_EJECTCLOSECD = 2813 | 弹出CD键。 |
| KEY_ISO = 2814 | ISO键。 |
| KEY_MOVE = 2815 | 移动键。 |
| KEY_F13 = 2816 | 按键'F13'。 |
| KEY_F14 = 2817 | 按键'F14'。 |
| KEY_F15 = 2818 | 按键'F15'。 |
| KEY_F16 = 2819 | 按键'F16'。 |
| KEY_F17 = 2820 | 按键'F17'。 |
| KEY_F18 = 2821 | 按键'F18'。 |
| KEY_F19 = 2822 | 按键'F19'。 |
| KEY_F20 = 2823 | 按键'F20'。 |
| KEY_F21 = 2824 | 按键'F21'。 |
| KEY_F22 = 2825 | 按键'F22'。 |
| KEY_F23 = 2826 | 按键'F23'。 |
| KEY_F24 = 2827 | 按键'F24'。 |
| KEY_PROG3 = 2828 | 程序键3。 |
| KEY_PROG4 = 2829 | 程序键4。 |
| KEY_DASHBOARD = 2830 | 仪表板。 |
| KEY_SUSPEND = 2831 | 挂起键。 |
| KEY_HP = 2832 | 高阶路径键。 |
| KEY_SOUND = 2833 | 音量键。 |
| KEY_QUESTION = 2834 | 疑问按键。 |
| KEY_CONNECT = 2836 | 连接键。 |
| KEY_SPORT = 2837 | 运动按键。 |
| KEY_SHOP = 2838 | 商城键。 |
| KEY_ALTERASE = 2839 | 交替键。 |
| KEY_SWITCHVIDEOMODE = 2841 | 在可用视频之间循环输出（监视器/LCD/TV输出/等）。 |
| KEY_BATTERY = 2842 | 电池按键。 |
| KEY_BLUETOOTH = 2843 | 蓝牙按键。 |
| KEY_WLAN = 2844 | 无线局域网。 |
| KEY_UWB = 2845 | 超宽带（UWB）。 |
| KEY_WWAN_WIMAX = 2846 | WWAN WiMAX按键。 |
| KEY_RFKILL = 2847 | 控制所有收音机的键。 |
| KEY_CHANNEL = 3001 | 向上频道键。 |
| KEY_BTN_0 = 3100 | 按键0。 |
| KEY_BTN_1 = 3101 | 按键1。 |
| KEY_BTN_2 = 3102 | 按键2。 |
| KEY_BTN_3 = 3103 | 按键3。 |
| KEY_BTN_4 = 3104 | 按键4。 |
| KEY_BTN_5 = 3105 | 按键5。 |
| KEY_BTN_6 = 3106 | 按键6。 |
| KEY_BTN_7 = 3107 | 按键7。 |
| KEY_BTN_8 = 3108 | 按键8。 |
| KEY_BTN_9 = 3109 | 按键9。 |

**OH_NativeXComponent_KeyAction**

```ets
enum OH_NativeXComponent_KeyAction
```

描述：

按键事件动作。

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| OH_NATIVEXCOMPONENT_KEY_ACTION_UNKNOWN = -1 | 未知的按键动作。 |
| OH_NATIVEXCOMPONENT_KEY_ACTION_DOWN = 0 | 按键按下动作。 |
| OH_NATIVEXCOMPONENT_KEY_ACTION_UP = 1 | 按键抬起动作。 |