# bm工具

本文根据华为开发者官网 `bm-tool` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/bm-tool>
更新时间：2026-04-30 02:41:24

## 环境要求（hdc工具）
在使用本工具前，开发者需要先获取hdc工具，执行hdc shell。

## bm工具命令列表
命令
描述
help
帮助命令，用于查询bm支持的命令信息。
install
安装命令，用于安装应用。
uninstall
卸载命令，用于卸载应用。
dump
查询命令，用于查询应用的相关信息。
clean
清理命令，用于清理应用的缓存和数据。在user版本下打开开发者模式可用。

## 帮助命令（help）
# 显示帮助信息 bm help

## 参数说明

## userId
表示当前系统账号的编号，系统账号的相关接口请参考系统账号管理模块，下面给出几种常见的系统账号。
userId = 100，表示编号为100的系统账号，系统默认账号，在设备出厂首次启动时由系统账号管理模块创建，且创建完成后会在100账号下安装所有的预置应用。
userId = 102，表示编号为102的系统账号，由系统账号管理模块创建，仅支持系统应用创建账号。在100账号下安装的应用，在102账号下不会显示，如有需求，需要在102账号下重新安装。在创建102账号过程中，系统会在102账号下安装预置系统应用。
userId = 0，表示共有系统账号，也叫账号0，该共有系统账号和系统账号编号不同，不是系统账号管理模块创建的。在账号0下安装的应用，所有系统账号共享，会在每个系统账号下都会显示。所有三方应用都不能安装到账号0下。

## 安装命令（install）
bm install [-h] [-p filePath] [-r] [-w waitingTime] [-s hspDirPath] [-u userId] [-d] [-g]
安装命令参数列表
参数
参数说明
-h
帮助信息。
-p
可选参数，指定待安装的HAP/HSP路径，多HAP/HSP应用可指定多HAP/HSP所在文件夹路径。从API version 22开始，支持指定待安装的APP路径，也可指定只存在一个APP的文件夹路径。
-r
可选参数，覆盖安装一个HAP/HSP。默认缺省，缺省时表示覆盖安装。
-s
安装应用间HSP时为必选参数，其他场景为可选参数。用于指定待安装应用间HSP的路径。从API version 24开始，当指定目录时，路径目录下可以存在多个同包名、不同模块名的HSP。API version 23及之前版本，路径目录下只能存在一个HSP。

## 卸载命令（uninstall）
bm uninstall [-h] [-n bundleName] [-m moduleName] [-k] [-s] [-v versionCode] [-u userId]
卸载命令参数列表
参数
参数说明
-h
帮助信息。
-n
必选参数，指定Bundle名称卸载应用。
-m
可选参数，应用模块名称，指定卸载应用的一个模块。默认卸载所有模块。
-k
可选参数，卸载应用时保存应用数据。默认卸载应用时不保存应用数据。

## 查询应用信息命令（dump）
bm dump [-h] [-a] [-g] [-n bundleName] [-s shortcutInfo] [-d deviceId] [-l label] [-u userId]
查询命令参数列表
参数
参数说明
-h
帮助信息。
-a
可选参数，查询系统已经安装的所有应用。
-g
可选参数，查询系统中签名为调试类型的应用包名。
-n
可选参数，查询指定Bundle名称的详细信息。

## 清理命令（clean）
bm clean [-h] [-c] [-n bundleName] [-d] [-i appIndex] [-u userId]
清理命令参数列表
参数
参数说明
-h
帮助信息。
-c -n
-n为必选参数，-c为可选参数。清除指定Bundle名称的缓存数据。
-d -n
-n为必选参数，-d为可选参数。清除指定Bundle名称的数据目录。
-i
可选参数，清除分身应用的数据目录。默认为0。

## 获取udid命令（get）
bm get [-h] [-u]
获取udid命令参数列表
参数
参数说明
-h
帮助信息。
-u
必选参数，获取设备的udid。
示例：
# 获取设备的udid bm get -u # 执行结果 udid of current device is : 23CADE0C

## 快速修复命令（quickfix）
bm quickfix [-h] [-a -f filePath [-t targetPath] [-d] [-o]] [-q -b bundleName] [-r -b bundleName]
注：hqf文件制作方式可参考HQF打包指令。
快速修复命令参数列表
参数
参数说明
-h
帮助信息。
-a -f
-a为可选参数，指定-a后，-f为必选参数。执行快速修复补丁安装命令，file-path对应hqf文件，支持传递1个或多个hqf文件，或传递hqf文件所在的目录。
-q -b
-q为可选参数，指定-q后，-b为必选参数。根据包名查询补丁信息。
-r -b

## 共享库查询命令（dump-shared）
bm dump-shared [-h] [-a] [-n bundleName]
共享库查询命令参数列表
参数
参数说明
-h
帮助信息。
-a
可选参数，查询系统中所有已安装的共享库。
-n
可选参数，查询指定包名的共享库详细信息。
示例：
# 显示所有已安装共享库包名 bm dump-shared -a # 显示该共享库的详细信息 bm dump-shared -n com.ohos.lib
