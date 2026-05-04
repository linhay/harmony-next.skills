# Connectivity Kit术语

本文根据华为开发者官网 `terminology` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/terminology>
更新时间：2026-04-30 02:41:24

## BLE
Bluetooth Low Energy，即低功耗蓝牙。从蓝牙4.0开始支持的协议，相比于传统蓝牙，是支持低功耗、长续航的蓝牙通信技术。

## UUID
Universally Unique Identifier，即通用唯一标识，是一个128比特的数据格式。在蓝牙技术中，可用于标识不同的Profile协议，也可用于GATT协议中的服务、特征值和描述符。

## MTU
Maximum Transmission Unit，即最大传输单元。表示网络中单次传输的最大数据包大小，单位是字节。

## Bluetooth SIG
Bluetooth Special Interest Group，即蓝牙技术联盟，发布蓝牙技术规范的组织。开发者可以在其官网获取详细的蓝牙技术文档。

## Profile
在蓝牙子系统中，一般特指某种蓝牙技术协议或者能力。例如：A2DP、HFP和HID协议等。

## HID
Human Interface Device Profile，即人机接口协议，为传统蓝牙设计。可用于实现蓝牙无线人机交互设备连接间的低延迟双向通信。例如：键盘、鼠标、游戏手柄等设备与主机（如手机、平板）间传输数据。该协议定义了2种角色：HID Host和HID Device。
在HID协议中， 数据传输通道分为2种，分别是中断通道和控制通道。其中中断通道用于传输单向低延迟实时数据；控制通道用于传输双向可靠实时数据，包含以下三种请求：
GET_REPORT：表示HID主机发起的数据读取请求，用于获取HID设备的状态信息。
SET_REPORT：表示HID主机发起的数据写入请求，用于向HID设备发送控制指令。
SET_PROTOCOL：表示HID主机发起的协议模式切换请求。

## HID Device
HID设备，是向HID Host设备提供人机数据输入/输出的设备。典型设备如：鼠标、键盘等。

## HID Host
HID主机设备，负责处理和接收HID Device的输入数据，并执行对应操作。典型设备如：手机、平板等。

## A2DP
Advanced Audio Distribution Profile，即增强音频分发协议。支持传输高品质音频。例如：使用蓝牙耳机听音乐。该协议定义了2种角色：A2DP Source和A2DP Sink。

## A2DP Sink
A2DP协议中的音频接收设备，负责解码并播放音频。典型设备如：蓝牙耳机、音箱等。

## A2DP Source
A2DP协议中的音频源设备端，负责编码并发送音频数据。典型设备如：手机、平板等。

## HFP
Hands-Free Profile，即免提协议。用于实现蓝牙设备间的免提通话，支持双向语音通话和控制等功能。该协议定义了2种角色：HFP AG和HF。

## HF
Hands-Free unit，即HFP协议中的免提设备。是蓝牙通话音频中的远程控制端‌，提供物理交互界面（如按钮）及音频输入/输出（如麦克风、扬声器）。典型设备如：蓝牙耳机、车载蓝牙等。

## HFP AG
Hands-Free Audio Gateway，即HFP协议中的音频网关。是蓝牙通话音频中的音频处理中心，负责通话控制（如执行接听/挂断指令）、管理音频输入/输出等功能。典型设备如：手机、平板等。

## MSE
Message Server Equipment，即MAP协议中的消息服务端，存储原始消息数据（如短信或邮件）。典型设备如‌：手机。

## GATT
Generic Attribute Profile，即通用属性协议。是BLE的核心协议，定义了基于服务（Service）、特征值（Characteristic）和描述符（Descriptor）进行蓝牙通信和传输数据的机制。

## SDP
Service Discovery Protocol，即服务发现协议。用于发现和识别其他蓝牙设备所提供的服务。

## PAN
Personal Area Network，即蓝牙个人局域网协议。支持设备间网络共享。在该协议中，NAP和PANU是两种核心角色。

## NAP
Network Access Point，即PAN协议中的网络接入点，充当网关设备，提供互联网接入或本地网络共享功能。典型设备如：手机、平板等。

## PBAP
Phone Book Access Profile，即蓝牙电话簿访问协议。可用于实现蓝牙设备间的电话簿数据同步，支持联系人、通话记录等数据传输。该协议定义了2种角色：PCE和PSE。
