# @ohos.multimodalInput.keyCode.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS;
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * @file Keycode
 * @kit InputKit
 */
/**
 * The **keyCode** module provides key codes of key devices, including keyboards, CDs, and gamepads.
 *
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @atomicservice [since 12]
 * @since 9
 */
export declare enum KeyCode {
    /**
     * Function (Fn) key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_FN = 0,
    /**
     * Unknown key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_UNKNOWN = -1,
    /**
     * Function (Home) key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_HOME = 1,
    /**
     * Back key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BACK = 2,
    /**
     * Search key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 13
     */
    KEYCODE_SEARCH = 9,
    /**
     * Play/Pause key
     *
     * Difference between this key and **KEYCODE_PLAYPAUSE**:
     *
     * **KEYCODE_PLAYPAUSE** is an earlier definition, while **KEYCODE_MEDIA_PLAY_PAUSE** is designed for modern media key
     * devices.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    KEYCODE_MEDIA_PLAY_PAUSE = 10,
    /**
     * Media: Stop Key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    KEYCODE_MEDIA_STOP = 11,
    /**
     * Next key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    KEYCODE_MEDIA_NEXT = 12,
    /**
     * Previous key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    KEYCODE_MEDIA_PREVIOUS = 13,
    /**
     * Rewind key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    KEYCODE_MEDIA_REWIND = 14,
    /**
     * Fast forward key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    KEYCODE_MEDIA_FAST_FORWARD = 15,
    /**
     * Volume Up key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_VOLUME_UP = 16,
    /**
     * Volume Down key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_VOLUME_DOWN = 17,
    /**
     * Power key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_POWER = 18,
    /**
     * Camera key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_CAMERA = 19,
    /**
     * Speaker Mute key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_VOLUME_MUTE = 22,
    /**
     * Mute key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_MUTE = 23,
    /**
     * Brightness Up key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BRIGHTNESS_UP = 40,
    /**
     * Brightness Down key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BRIGHTNESS_DOWN = 41,
    /**
     * Key 0
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_0 = 2000,
    /**
     * Key 1
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_1 = 2001,
    /**
     * Key 2
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_2 = 2002,
    /**
     * Key 3
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_3 = 2003,
    /**
     * Key 4
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_4 = 2004,
    /**
     * Key 5
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_5 = 2005,
    /**
     * Key 6
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_6 = 2006,
    /**
     * Key 7
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_7 = 2007,
    /**
     * Key 8
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_8 = 2008,
    /**
     * Key 9
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_9 = 2009,
    /**
     * Key /
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_STAR = 2010,
    /**
     * Key /
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_POUND = 2011,
    /**
     * Up key on D-pad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_DPAD_UP = 2012,
    /**
     * Down key on D-pad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_DPAD_DOWN = 2013,
    /**
     * Left key on D-pad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_DPAD_LEFT = 2014,
    /**
     * Right key on D-pad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_DPAD_RIGHT = 2015,
    /**
     * Center key on D-pad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_DPAD_CENTER = 2016,
    /**
     * Key A
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_A = 2017,
    /**
     * Key B
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_B = 2018,
    /**
     * Key C
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_C = 2019,
    /**
     * Key D
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_D = 2020,
    /**
     * Key E
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_E = 2021,
    /**
     * Key F
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F = 2022,
    /**
     * Key G
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_G = 2023,
    /**
     * Key H
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_H = 2024,
    /**
     * Key I
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_I = 2025,
    /**
     * Key J
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_J = 2026,
    /**
     * Key K
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_K = 2027,
    /**
     * Key L
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_L = 2028,
    /**
     * Key M
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_M = 2029,
    /**
     * Key N
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_N = 2030,
    /**
     * Key O
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_O = 2031,
    /**
     * Key P
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_P = 2032,
    /**
     * Key Q
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_Q = 2033,
    /**
     * Key R
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_R = 2034,
    /**
     * Key S
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_S = 2035,
    /**
     * Key T
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_T = 2036,
    /**
     * Key U
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_U = 2037,
    /**
     * Key V
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_V = 2038,
    /**
     * Key W
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_W = 2039,
    /**
     * Key X
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_X = 2040,
    /**
     * Key Y
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_Y = 2041,
    /**
     * Key Z
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_Z = 2042,
    /**
     * Key ,
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_COMMA = 2043,
    /**
     * Key .
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_PERIOD = 2044,
    /**
     * Left Alt key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_ALT_LEFT = 2045,
    /**
     * Right Alt key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_ALT_RIGHT = 2046,
    /**
     * Left Shift key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SHIFT_LEFT = 2047,
    /**
     * Right Shift key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SHIFT_RIGHT = 2048,
    /**
     * Tab key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_TAB = 2049,
    /**
     * Space key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SPACE = 2050,
    /**
     * Symbol key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SYM = 2051,
    /**
     * Explorer key, which is used to start the explorer application
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_EXPLORER = 2052,
    /**
     * Email key, which is used to start the email application
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_ENVELOPE = 2053,
    /**
     * Enter key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_ENTER = 2054,
    /**
     * Delete key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_DEL = 2055,
    /**
     * Key /
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_GRAVE = 2056,
    /**
     * Key -
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_MINUS = 2057,
    /**
     * Key =
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_EQUALS = 2058,
    /**
     * Key [
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_LEFT_BRACKET = 2059,
    /**
     * Key ]
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_RIGHT_BRACKET = 2060,
    /**
     * Key \
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BACKSLASH = 2061,
    /**
     * Key ;
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SEMICOLON = 2062,
    /**
     * Key '
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_APOSTROPHE = 2063,
    /**
     * Key /
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SLASH = 2064,
    /**
     * Key /
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_AT = 2065,
    /**
     * Key +
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_PLUS = 2066,
    /**
     * Menu key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_MENU = 2067,
    /**
     * Page Up key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_PAGE_UP = 2068,
    /**
     * Page Down key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_PAGE_DOWN = 2069,
    /**
     * Esc key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_ESCAPE = 2070,
    /**
     * Forward Delete key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_FORWARD_DEL = 2071,
    /**
     * Left Ctrl key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_CTRL_LEFT = 2072,
    /**
     * Right Ctrl key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_CTRL_RIGHT = 2073,
    /**
     * Caps Lock key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_CAPS_LOCK = 2074,
    /**
     * Scroll Lock key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SCROLL_LOCK = 2075,
    /**
     * Left Meta key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_META_LEFT = 2076,
    /**
     * Right Meta key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_META_RIGHT = 2077,
    /**
     * Function key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_FUNCTION = 2078,
    /**
     * System Request/Print Screen key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SYSRQ = 2079,
    /**
     * Break/Pause key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BREAK = 2080,
    /**
     * Move to Home key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_MOVE_HOME = 2081,
    /**
     * Move to End key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_MOVE_END = 2082,
    /**
     * Insert key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_INSERT = 2083,
    /**
     * Forward key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_FORWARD = 2084,
    /**
     * Play key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    KEYCODE_MEDIA_PLAY = 2085,
    /**
     * Media: Pause Key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    KEYCODE_MEDIA_PAUSE = 2086,
    /**
     * Media: Close Key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_MEDIA_CLOSE = 2087,
    /**
     * Media: Eject Key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_MEDIA_EJECT = 2088,
    /**
     * Record key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_MEDIA_RECORD = 2089,
    /**
     * F1 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F1 = 2090,
    /**
     * F2 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F2 = 2091,
    /**
     * F3 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F3 = 2092,
    /**
     * F4 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F4 = 2093,
    /**
     * F5 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F5 = 2094,
    /**
     * F6 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F6 = 2095,
    /**
     * F7 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F7 = 2096,
    /**
     * F8 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F8 = 2097,
    /**
     * F9 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F9 = 2098,
    /**
     * F10 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F10 = 2099,
    /**
     * F11 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F11 = 2100,
    /**
     * F12 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F12 = 2101,
    /**
     * Number Lock key on numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUM_LOCK = 2102,
    /**
     * Key 0 on numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUMPAD_0 = 2103,
    /**
     * Key 1 on numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUMPAD_1 = 2104,
    /**
     * Key 2 on numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUMPAD_2 = 2105,
    /**
     * Key 3 on numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUMPAD_3 = 2106,
    /**
     * Key 4 on numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUMPAD_4 = 2107,
    /**
     * Key 5 on numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUMPAD_5 = 2108,
    /**
     * Key 6 on numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUMPAD_6 = 2109,
    /**
     * Key 7 on numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUMPAD_7 = 2110,
    /**
     * Key 8 on numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUMPAD_8 = 2111,
    /**
     * Key 9 on numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUMPAD_9 = 2112,
    /**
     * Key / on numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUMPAD_DIVIDE = 2113,
    /**
     * Key * on numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUMPAD_MULTIPLY = 2114,
    /**
     * Key - on numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUMPAD_SUBTRACT = 2115,
    /**
     * Key + on numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUMPAD_ADD = 2116,
    /**
     * Key . on numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUMPAD_DOT = 2117,
    /**
     * Key , on numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUMPAD_COMMA = 2118,
    /**
     * Enter key on numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUMPAD_ENTER = 2119,
    /**
     * Key = on numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUMPAD_EQUALS = 2120,
    /**
     * Key ( on numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUMPAD_LEFT_PAREN = 2121,
    /**
     * Key ) on numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUMPAD_RIGHT_PAREN = 2122,
    /**
     * Multi-task key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_VIRTUAL_MULTITASK = 2210,
    /**
     * Joystick key A
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 15
     */
    KEYCODE_BUTTON_A = 2301,
    /**
     * Joystick key B
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 15
     */
    KEYCODE_BUTTON_B = 2302,
    /**
     * Joystick key X
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 15
     */
    KEYCODE_BUTTON_X = 2304,
    /**
     * Joystick key Y
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 15
     */
    KEYCODE_BUTTON_Y = 2305,
    /**
     * Joystick key L1
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 15
     */
    KEYCODE_BUTTON_L1 = 2307,
    /**
     * Joystick key R1
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 15
     */
    KEYCODE_BUTTON_R1 = 2308,
    /**
     * Joystick key L2
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 15
     */
    KEYCODE_BUTTON_L2 = 2309,
    /**
     * Joystick key R2
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 15
     */
    KEYCODE_BUTTON_R2 = 2310,
    /**
     * Joystick key Select
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 15
     */
    KEYCODE_BUTTON_SELECT = 2311,
    /**
     * Joystick key Start
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 15
     */
    KEYCODE_BUTTON_START = 2312,
    /**
     * Joystick key Mode
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 15
     */
    KEYCODE_BUTTON_MODE = 2313,
    /**
     * Joystick key THUMBL
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 15
     */
    KEYCODE_BUTTON_THUMBL = 2314,
    /**
     * Joystick key THUMBR
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 15
     */
    KEYCODE_BUTTON_THUMBR = 2315,
    /**
     * Sleep key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SLEEP = 2600,
    /**
     * Zenkaku/Hankaku key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_ZENKAKU_HANKAKU = 2601,
    /**
     * International Keyboard Extension key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_102ND = 2602,
    /**
     * Ro key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_RO = 2603,
    /**
     * Katakana key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_KATAKANA = 2604,
    /**
     * Hiragana key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_HIRAGANA = 2605,
    /**
     * Henkan key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_HENKAN = 2606,
    /**
     * Katakana/Hiragana key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_KATAKANA_HIRAGANA = 2607,
    /**
     * Muhenkan key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_MUHENKAN = 2608,
    /**
     * Linefeed key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_LINEFEED = 2609,
    /**
     * Macro key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_MACRO = 2610,
    /**
     * Plus/Minus key on the numeric keypad
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NUMPAD_PLUSMINUS = 2611,
    /**
     * Scale key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SCALE = 2612,
    /**
     * Hanguel key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_HANGUEL = 2613,
    /**
     * Hanja key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_HANJA = 2614,
    /**
     * Yen key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_YEN = 2615,
    /**
     * Stop key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_STOP = 2616,
    /**
     * Again key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_AGAIN = 2617,
    /**
     * Props key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_PROPS = 2618,
    /**
     * Undo key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_UNDO = 2619,
    /**
     * Copy key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_COPY = 2620,
    /**
     * Open key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_OPEN = 2621,
    /**
     * Paste key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_PASTE = 2622,
    /**
     * Find key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_FIND = 2623,
    /**
     * Cut key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_CUT = 2624,
    /**
     * Help key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_HELP = 2625,
    /**
     * Calc key, which is used to start the calculator application
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_CALC = 2626,
    /**
     * File key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_FILE = 2627,
    /**
     * Bookmarks key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BOOKMARKS = 2628,
    /**
     * Page Down key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NEXT = 2629,
    /**
     * Play/Pause key
     *
     * Difference between this key and **KEYCODE_MEDIA_PLAY_PAUSE**:
     *
     * **KEYCODE_PLAYPAUSE** is an earlier definition, while **KEYCODE_MEDIA_PLAY_PAUSE** is designed for modern media key
     * devices.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_PLAYPAUSE = 2630,
    /**
     * Page Up key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_PREVIOUS = 2631,
    /**
     * Stop CD key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_STOPCD = 2632,
    /**
     * Config key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_CONFIG = 2634,
    /**
     * Refresh key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_REFRESH = 2635,
    /**
     * Exit key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_EXIT = 2636,
    /**
     * Edit key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_EDIT = 2637,
    /**
     * Scroll Up key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SCROLLUP = 2638,
    /**
     * Scroll Down key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SCROLLDOWN = 2639,
    /**
     * New key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NEW = 2640,
    /**
     * Redo key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_REDO = 2641,
    /**
     * Close key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_CLOSE = 2642,
    /**
     * Play key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_PLAY = 2643,
    /**
     * Bass Boost key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BASSBOOST = 2644,
    /**
     * Print key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_PRINT = 2645,
    /**
     * Chat key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_CHAT = 2646,
    /**
     * Finance key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_FINANCE = 2647,
    /**
     * Cancel key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_CANCEL = 2648,
    /**
     * Keyboard Illumination Toggle key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_KBDILLUM_TOGGLE = 2649,
    /**
     * Keyboard Illumination Down key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_KBDILLUM_DOWN = 2650,
    /**
     * Keyboard Illumination Up key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_KBDILLUM_UP = 2651,
    /**
     * Send key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SEND = 2652,
    /**
     * Reply key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_REPLY = 2653,
    /**
     * Forward Mail key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_FORWARDMAIL = 2654,
    /**
     * Save key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SAVE = 2655,
    /**
     * Documents key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_DOCUMENTS = 2656,
    /**
     * Next Video key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_VIDEO_NEXT = 2657,
    /**
     * Previous Video key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_VIDEO_PREV = 2658,
    /**
     * Brightness Cycle key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BRIGHTNESS_CYCLE = 2659,
    /**
     * Brightness Zero key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BRIGHTNESS_ZERO = 2660,
    /**
     * Display Off key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_DISPLAY_OFF = 2661,
    /**
     * Misc Button key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BTN_MISC = 2662,
    /**
     * Goto key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_GOTO = 2663,
    /**
     * Info key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_INFO = 2664,
    /**
     * Program key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_PROGRAM = 2665,
    /**
     * PVR key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_PVR = 2666,
    /**
     * Subtitle key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SUBTITLE = 2667,
    /**
     * Full Screen key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_FULL_SCREEN = 2668,
    /**
     * Keyboard.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_KEYBOARD = 2669,
    /**
     * Aspect Ratio key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_ASPECT_RATIO = 2670,
    /**
     * Port Control key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_PC = 2671,
    /**
     * TV key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_TV = 2672,
    /**
     * TV key 2
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_TV2 = 2673,
    /**
     * VCR key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_VCR = 2674,
    /**
     * VCR key 2
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_VCR2 = 2675,
    /**
     * SAT key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SAT = 2676,
    /**
     * CD key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_CD = 2677,
    /**
     * Tape key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_TAPE = 2678,
    /**
     * Tuner key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_TUNER = 2679,
    /**
     * Player key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_PLAYER = 2680,
    /**
     * DVD key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_DVD = 2681,
    /**
     * Audio key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_AUDIO = 2682,
    /**
     * Video key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_VIDEO = 2683,
    /**
     * Memo key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_MEMO = 2684,
    /**
     * Calendar key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_CALENDAR = 2685,
    /**
     * Red indicator.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_RED = 2686,
    /**
     * Green indicator.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_GREEN = 2687,
    /**
     * Yellow indicator.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_YELLOW = 2688,
    /**
     * Blue indicator.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BLUE = 2689,
    /**
     * Channel Up key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_CHANNELUP = 2690,
    /**
     * Channel Down key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_CHANNELDOWN = 2691,
    /**
     * Last key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_LAST = 2692,
    /**
     * Restart key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_RESTART = 2693,
    /**
     * Slow key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SLOW = 2694,
    /**
     * Shuffle key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SHUFFLE = 2695,
    /**
     * Videophone key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_VIDEOPHONE = 2696,
    /**
     * Games key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_GAMES = 2697,
    /**
     * Zoom in
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_ZOOMIN = 2698,
    /**
     * Zoom out
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_ZOOMOUT = 2699,
    /**
     * Zoom Reset key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_ZOOMRESET = 2700,
    /**
     * Word Processor key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_WORDPROCESSOR = 2701,
    /**
     * Editor key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_EDITOR = 2702,
    /**
     * Spreadsheet key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SPREADSHEET = 2703,
    /**
     * Graphics Editor key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_GRAPHICSEDITOR = 2704,
    /**
     * Presentation key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_PRESENTATION = 2705,
    /**
     * Database key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_DATABASE = 2706,
    /**
     * News key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_NEWS = 2707,
    /**
     * Voicemail key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_VOICEMAIL = 2708,
    /**
     * Address book key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_ADDRESSBOOK = 2709,
    /**
     * Messenger key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_MESSENGER = 2710,
    /**
     * Brightness Toggle key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BRIGHTNESS_TOGGLE = 2711,
    /**
     * Spell Check key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SPELLCHECK = 2712,
    /**
     * Coffee key, which is used to launch screen lock or screen saver
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_COFFEE = 2713,
    /**
     * Media Repeat key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_MEDIA_REPEAT = 2714,
    /**
     * Images key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_IMAGES = 2715,
    /**
     * Button Configuration key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BUTTONCONFIG = 2716,
    /**
     * Task Manager key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_TASKMANAGER = 2717,
    /**
     * Log key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_JOURNAL = 2718,
    /**
     * Control Panel key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_CONTROLPANEL = 2719,
    /**
     * App Select key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_APPSELECT = 2720,
    /**
     * Screen Saver key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SCREENSAVER = 2721,
    /**
     * Smart key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_ASSISTANT = 2722,
    /**
     * Next Keyboard Layout key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_KBD_LAYOUT_NEXT = 2723,
    /**
     * Min Brightness key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BRIGHTNESS_MIN = 2724,
    /**
     * Max Brightness key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BRIGHTNESS_MAX = 2725,
    /**
     * Assist_Previous key, used to view historical inputs
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_KBDINPUTASSIST_PREV = 2726,
    /**
     * Assist_Next key, used to view predictive inputs
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_KBDINPUTASSIST_NEXT = 2727,
    /**
     * Assist_Previous_Group key, used to switch to the previous input method in the input group
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_KBDINPUTASSIST_PREVGROUP = 2728,
    /**
     * Assist_Next_Group key, used to switch to the next input method in the input group
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_KBDINPUTASSIST_NEXTGROUP = 2729,
    /**
     * Keyboard Input-assisted Accept key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_KBDINPUTASSIST_ACCEPT = 2730,
    /**
     * Keyboard Input-assisted Cancel key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_KBDINPUTASSIST_CANCEL = 2731,
    /**
     * Mouse AI assistant key.
     *
     * **Starting Version:** 26.0.0
     *
     * **Model constraint:** This API can only be used in the stage model.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    KEYCODE_MOUSE_ASSISTANT = 2732,
    /**
     * Mouse smart selection key.
     *
     * **Starting Version:** 26.0.0
     *
     * **Model constraint:** This API can only be used in the stage model.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    KEYCODE_MOUSE_INTELLIGENCE_SELECTION = 2733,
    /**
     * Phone touchscreen single-click event, used in Always-On Display (AOD) mode.
     *
     * **Starting Version:** 26.0.0
     *
     * **Model constraint:** This API can only be used in the stage model.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    KEYCODE_AOD_SINGLE_CLICK = 2740,
    /**
     * Front key, which is used to launch the windshield defogger
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_FRONT = 2800,
    /**
     * Setup key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SETUP = 2801,
    /**
     * Wakeup key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_WAKEUP = 2802,
    /**
     * Send File key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SENDFILE = 2803,
    /**
     * Delete File key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_DELETEFILE = 2804,
    /**
     * XFER key, which is used to start file transfer
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_XFER = 2805,
    /**
     * Program key 1
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_PROG1 = 2806,
    /**
     * Program key 2
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_PROG2 = 2807,
    /**
     * DOS key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_MSDOS = 2808,
    /**
     * Screen Lock key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SCREENLOCK = 2809,
    /**
     * Directional Rotation Display key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_DIRECTION_ROTATE_DISPLAY = 2810,
    /**
     * Window Cycle key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_CYCLEWINDOWS = 2811,
    /**
     * Key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_COMPUTER = 2812,
    /**
     * Eject CD key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_EJECTCLOSECD = 2813,
    /**
     * ISO key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_ISO = 2814,
    /**
     * Move key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_MOVE = 2815,
    /**
     * F13 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F13 = 2816,
    /**
     * F14 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F14 = 2817,
    /**
     * F15 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F15 = 2818,
    /**
     * F16 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F16 = 2819,
    /**
     * F17 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F17 = 2820,
    /**
     * F18 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F18 = 2821,
    /**
     * F19 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F19 = 2822,
    /**
     * F20 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F20 = 2823,
    /**
     * F21 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F21 = 2824,
    /**
     * F22 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F22 = 2825,
    /**
     * F23 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F23 = 2826,
    /**
     * F24 key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_F24 = 2827,
    /**
     * Program key 3
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_PROG3 = 2828,
    /**
     * Program key 4
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_PROG4 = 2829,
    /**
     * Dashboard key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_DASHBOARD = 2830,
    /**
     * Suspend key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SUSPEND = 2831,
    /**
     * HP key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_HP = 2832,
    /**
     * Sound key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SOUND = 2833,
    /**
     * Question key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_QUESTION = 2834,
    /**
     * Connect key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_CONNECT = 2836,
    /**
     * Sport key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SPORT = 2837,
    /**
     * Shop key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SHOP = 2838,
    /**
     * Alternate key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_ALTERASE = 2839,
    /**
     * Switch Video Mode key (monitor, LCD, and TV, etc.)
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_SWITCHVIDEOMODE = 2841,
    /**
     * Battery key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BATTERY = 2842,
    /**
     * Bluetooth key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BLUETOOTH = 2843,
    /**
     * WLAN key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_WLAN = 2844,
    /**
     * Ultra-wideband key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_UWB = 2845,
    /**
     * Mobile Network Control key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_WWAN_WIMAX = 2846,
    /**
     * RF Kill key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_RFKILL = 2847,
    /**
     * Channel key
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_CHANNEL = 3001,
    /**
     * Button 0
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BTN_0 = 3100,
    /**
     * Button 1
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BTN_1 = 3101,
    /**
     * Button 2
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BTN_2 = 3102,
    /**
     * Button 3
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BTN_3 = 3103,
    /**
     * Button 4
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BTN_4 = 3104,
    /**
     * Button 5
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BTN_5 = 3105,
    /**
     * Button 6
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BTN_6 = 3106,
    /**
     * Button 7
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BTN_7 = 3107,
    /**
     * Button 8
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BTN_8 = 3108,
    /**
     * Button 9
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    KEYCODE_BTN_9 = 3109,
    /**
     * Single tapping the smart watch's X-TAP sensor
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 18
     */
    KEYCODE_DAGGER_CLICK = 3211,
    /**
     * Double tapping the smart watch's X-TAP sensor
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 18
     */
    KEYCODE_DAGGER_DOUBLE_CLICK = 3212,
    /**
     * Long-pressing the smart watch's X-TAP sensor
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 18
     */
    KEYCODE_DAGGER_LONG_PRESS = 3213,
    /**
     * Left button of the smart watch
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 20
     */
    KEYCODE_DIV = 3220,
    /**
     * Custom hotkey
     *
     * **Since:** 26.0.0
     *
     * **Model restriction:** This API can only be used in the stage model.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    KEYCODE_XKEY = 3232,
    /**
     * Smart control key slide-up
     *
     * **Since:** 26.0.0
     *
     * **Model restriction:** This API can only be used in the stage model.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    KEYCODE_FINGERPRINT_SLIDE_UP = 3233,
    /**
     * Smart control key slide-down
     *
     * **Since:** 26.0.0
     *
     * **Model restriction:** This API can only be used in the stage model.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    KEYCODE_FINGERPRINT_SLIDE_DOWN = 3234
}

```
